using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace CampusRomance.Launcher
{
    public static class SafePaths
    {
        static readonly HashSet<string> ProtectedParts = new HashSet<string>(new string[] { "saves", "userdata", "user_data", "logs", "screenshots", "captures", "exports", ".campus-launcher", ".git" }, StringComparer.OrdinalIgnoreCase);
        static readonly HashSet<string> ProtectedNames = new HashSet<string>(new string[] { "persistent", "log.txt", "traceback.txt", "errors.txt", ".installed-state.json" }, StringComparer.OrdinalIgnoreCase);
        public static string CanonicalRoot(string root)
        {
            if (String.IsNullOrWhiteSpace(root) || !Path.IsPathRooted(root) || root.StartsWith("\\\\")) throw new UpdateFailure("UNSAFE_PATH", "설치 위치는 로컬 드라이브의 폴더로 선택해 주세요.");
            string path = Path.GetFullPath(root).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
            if (path.Length < 4 || path.IndexOf(':') != 1 || path.Substring(2).IndexOf(':') >= 0) throw new UpdateFailure("UNSAFE_PATH", "드라이브 최상위 대신 설치 폴더를 선택해 주세요.");
            CheckNoReparse(path);
            return path;
        }
        public static void ValidateRelative(string relative)
        {
            if (String.IsNullOrEmpty(relative) || relative.Length > 220 || relative.StartsWith("/") || relative.IndexOf('\\') >= 0 || relative.IndexOf(':') >= 0 || Path.IsPathRooted(relative)) throw new UpdateFailure("UNSAFE_PATH", "안전하지 않은 업데이트 경로입니다: " + relative);
            string[] parts = relative.Split('/');
            for (int index = 0; index < parts.Length; index++)
            {
                string part = parts[index];
                if (part.Length == 0 || part == "." || part == ".." || part.EndsWith(".") || part.EndsWith(" ") || part.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0 || part.Any(c => Char.IsControl(c))) throw new UpdateFailure("UNSAFE_PATH", "안전하지 않은 파일 이름입니다: " + relative);
                string stem = part.Split('.')[0];
                if (Regex.IsMatch(stem, "^(CON|PRN|AUX|NUL|COM[0-9]|LPT[0-9])$", RegexOptions.IgnoreCase)) throw new UpdateFailure("UNSAFE_PATH", "Windows 예약 파일 이름은 사용할 수 없습니다: " + relative);
                // renpy/exports is an official Python engine package, not a
                // player's exported files. Only this exact module path is exempt.
                bool engineExports = index == 1 && String.Equals(parts[0], "renpy", StringComparison.OrdinalIgnoreCase) && String.Equals(part, "exports", StringComparison.OrdinalIgnoreCase);
                if ((ProtectedParts.Contains(part) && !engineExports) || ProtectedNames.Contains(part) || part.EndsWith(".save", StringComparison.OrdinalIgnoreCase) || part.EndsWith(".log", StringComparison.OrdinalIgnoreCase)) throw new UpdateFailure("PROTECTED_PATH", "저장 기록과 사용자 파일은 업데이트할 수 없습니다: " + relative);
            }
        }
        public static string Within(string parent, string relative)
        {
            string full = Path.GetFullPath(Path.Combine(parent, relative.Replace('/', Path.DirectorySeparatorChar)));
            string prefix = Path.GetFullPath(parent).TrimEnd(Path.DirectorySeparatorChar) + Path.DirectorySeparatorChar;
            if (!full.StartsWith(prefix, StringComparison.OrdinalIgnoreCase)) throw new UpdateFailure("UNSAFE_PATH", "업데이트가 설치 폴더를 벗어났습니다.");
            CheckNoReparse(full);
            return full;
        }
        public static void CheckNoReparse(string path)
        {
            string current = Path.GetFullPath(path);
            while (!String.IsNullOrEmpty(current))
            {
                try
                {
                    if ((File.GetAttributes(current) & FileAttributes.ReparsePoint) != 0) throw new UpdateFailure("UNSAFE_PATH", "연결된 폴더나 심볼릭 링크에는 설치할 수 없습니다: " + current);
                }
                catch (FileNotFoundException) { }
                catch (DirectoryNotFoundException) { }
                string parent = Path.GetDirectoryName(current);
                if (parent == current) break;
                current = parent;
            }
        }
        public static void DeletePrivateTree(string baseDirectory, string directory)
        {
            string full = Path.GetFullPath(directory);
            string guard = Path.GetFullPath(baseDirectory).TrimEnd(Path.DirectorySeparatorChar) + Path.DirectorySeparatorChar;
            if (!full.StartsWith(guard, StringComparison.OrdinalIgnoreCase)) throw new UpdateFailure("UNSAFE_PATH", "임시 폴더의 범위가 올바르지 않습니다.");
            if (!Directory.Exists(full)) return;
            CheckNoReparse(full);
            foreach (string child in Directory.GetFileSystemEntries(full))
            {
                CheckNoReparse(child);
                if (Directory.Exists(child)) DeletePrivateTree(baseDirectory, child);
                else { File.SetAttributes(child, File.GetAttributes(child) & ~FileAttributes.ReadOnly); File.Delete(child); }
            }
            Directory.Delete(full);
        }
    }
}
