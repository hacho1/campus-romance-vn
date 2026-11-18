using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace CampusRomance.Launcher
{
    public sealed class SaveMigrationResult
    {
        public string Status { get; set; }
        public int CopiedFiles { get; set; }
        public string Message { get; set; }
    }
    public static class SaveMigration
    {
        static bool PlayerFile(string path)
        {
            return String.Equals(Path.GetFileName(path), "persistent", StringComparison.OrdinalIgnoreCase) || String.Equals(Path.GetExtension(path), ".save", StringComparison.OrdinalIgnoreCase);
        }
        static bool TargetHasPlayerFiles(string directory)
        {
            if (!Directory.Exists(directory)) return false;
            SafePaths.CheckNoReparse(directory);
            foreach (string entry in Directory.GetFileSystemEntries(directory))
            {
                // An unknown linked subtree is not an empty player directory.
                if ((File.GetAttributes(entry) & FileAttributes.ReparsePoint) != 0) return true;
                if (Directory.Exists(entry)) { if (TargetHasPlayerFiles(entry)) return true; }
                else if (PlayerFile(entry)) return true;
            }
            return false;
        }
        public static bool HasCoherentSource(string sourceDirectory)
        {
            try
            {
                SafePaths.CheckNoReparse(sourceDirectory);
                return Directory.Exists(sourceDirectory) && File.Exists(Path.Combine(sourceDirectory, "persistent")) && Directory.GetFiles(sourceDirectory, "*", SearchOption.TopDirectoryOnly).Any(p => String.Equals(Path.GetExtension(p), ".save", StringComparison.OrdinalIgnoreCase));
            }
            catch { return false; }
        }
        // Explicit source/target arguments keep fixture QA independent of real
        // user folders. Only GUI first-install code supplies the local source.
        public static SaveMigrationResult ImportIfEmpty(string sourceDirectory, string targetDirectory)
        {
            string source = Path.GetFullPath(sourceDirectory).TrimEnd(Path.DirectorySeparatorChar);
            string target = Path.GetFullPath(targetDirectory).TrimEnd(Path.DirectorySeparatorChar);
            SafePaths.CheckNoReparse(source); SafePaths.CheckNoReparse(target);
            if (String.Equals(source, target, StringComparison.OrdinalIgnoreCase) || target.StartsWith(source + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase)) return Skip("기존 기록과 대상 폴더가 겹쳐 가져오지 않았어요.");
            if (!HasCoherentSource(source)) return Skip("가져올 기존 플레이 기록이 없어요.");
            if (TargetHasPlayerFiles(target)) return Skip("대상에 플레이 기록이 있어 덮어쓰지 않았어요.");
            string[] files = Directory.GetFiles(source, "*", SearchOption.TopDirectoryOnly).Where(PlayerFile).OrderBy(p => p, StringComparer.OrdinalIgnoreCase).ToArray();
            string parent = Path.GetDirectoryName(target);
            if (!Directory.Exists(parent)) throw new IOException("게임 설치 폴더가 없습니다.");
            string stage = Path.Combine(parent, ".campus-save-import-" + Guid.NewGuid().ToString("N"));
            var hashes = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            var timestamps = new Dictionary<string, long>(StringComparer.OrdinalIgnoreCase);
            var moved = new List<string>();
            Directory.CreateDirectory(stage);
            try
            {
                foreach (string file in files)
                {
                    SafePaths.CheckNoReparse(file);
                    string name = Path.GetFileName(file);
                    timestamps[name] = File.GetLastWriteTimeUtc(file).Ticks;
                    string copy = Path.Combine(stage, name);
                    using (var input = new FileStream(file, FileMode.Open, FileAccess.Read, FileShare.Read))
                    using (var output = new FileStream(copy, FileMode.CreateNew, FileAccess.Write, FileShare.None)) { input.CopyTo(output); output.Flush(true); }
                    hashes[name] = UpdateEngine.HashBytes(File.ReadAllBytes(copy));
                    File.SetLastWriteTimeUtc(copy, new DateTime(timestamps[name], DateTimeKind.Utc));
                }
                string[] after = Directory.GetFiles(source, "*", SearchOption.TopDirectoryOnly).Where(PlayerFile).OrderBy(p => p, StringComparer.OrdinalIgnoreCase).ToArray();
                if (!files.SequenceEqual(after, StringComparer.OrdinalIgnoreCase)) return Skip("복사 중 원본 기록이 바뀌어 가져오기를 멈췄어요.");
                foreach (string file in files)
                {
                    SafePaths.CheckNoReparse(file); string name = Path.GetFileName(file);
                    if (File.GetLastWriteTimeUtc(file).Ticks != timestamps[name] || UpdateEngine.HashBytes(File.ReadAllBytes(file)) != hashes[name]) return Skip("복사 중 원본 기록이 바뀌어 가져오기를 멈췄어요.");
                }
                SafePaths.CheckNoReparse(target);
                if (TargetHasPlayerFiles(target)) return Skip("대상에 새 플레이 기록이 생겨 덮어쓰지 않았어요.");
                Directory.CreateDirectory(target);
                foreach (string file in files)
                {
                    string name = Path.GetFileName(file); string destination = Path.Combine(target, name);
                    SafePaths.CheckNoReparse(destination);
                    File.Move(Path.Combine(stage, name), destination); moved.Add(destination);
                }
                return new SaveMigrationResult { Status = "copied", CopiedFiles = moved.Count, Message = "기존 플레이 기록 " + moved.Count + "개를 가져왔어요. 원본은 그대로예요." };
            }
            catch
            {
                // Roll back only files created by this import, never a source
                // file or pre-existing destination record.
                foreach (string path in moved)
                    if (File.Exists(path) && UpdateEngine.HashBytes(File.ReadAllBytes(path)) == hashes[Path.GetFileName(path)]) File.Delete(path);
                throw;
            }
            finally { SafePaths.DeletePrivateTree(parent, stage); }
        }
        static SaveMigrationResult Skip(string message) { return new SaveMigrationResult { Status = "skipped", CopiedFiles = 0, Message = message }; }
    }
}
