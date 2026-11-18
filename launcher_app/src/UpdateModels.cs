using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Web.Script.Serialization;

namespace CampusRomance.Launcher
{
    public sealed class UpdateFailure : Exception
    {
        public readonly string Code;
        public UpdateFailure(string code, string message) : base(message) { Code = code; }
        public UpdateFailure(string code, string message, Exception inner) : base(message, inner) { Code = code; }
    }
    public sealed class ChunkSpec { public string sha256; public long size; public string url; }
    public sealed class FileSpec { public string path; public long size; public string sha256; public List<ChunkSpec> chunks; }
    public sealed class ReleaseSpec
    {
        public int schema; public string product; public string version; public long build;
        public string executable; public long total_bytes; public List<FileSpec> files; public string[] release_notes;
    }
    public sealed class InstalledState
    {
        public int schema = 1; public string product = "campus-romance"; public string version;
        public long build; public string transaction; public string manifest_sha256; public string manifest_base64;
        public string signature_base64; public string installed_utc;
    }
    public sealed class VerifiedRelease
    {
        public ReleaseSpec Release; public byte[] Raw; public byte[] Signature; public string Hash;
    }
    public sealed class StoredRelease { public InstalledState State; public VerifiedRelease Verified; }
    public sealed class ProgressInfo
    {
        public string phase; public string file; public long bytes; public long total;
        public ProgressInfo(string phase, string file, long bytes, long total) { this.phase = phase; this.file = file; this.bytes = bytes; this.total = total; }
    }
    public sealed class UpdateReport
    {
        public string status = "ok"; public string code = "OK"; public string message = "";
        public string command; public string root; public bool qa;
        public long installed_build; public long latest_build; public string installed_version; public string version;
        public bool update_available; public bool first_install; public bool recovery_performed;
        public List<string> changed_files = new List<string>(); public List<string> deleted_files = new List<string>();
        public List<string> preserved_modified_files = new List<string>();
        public long downloaded_chunks; public long downloaded_bytes; public long reused_chunks; public long total_bytes;
        public string[] release_notes = new string[0]; public string executable;
    }
    public sealed class EngineOptions
    {
        public string Root; public Uri FeedBase; public string PublicKeyXml; public bool Qa;
        public int FailAfterApply; public int CrashAfterApply; public int HoldLockMilliseconds;
        public System.Threading.CancellationToken Cancellation;
        public Action<ProgressInfo> Progress;
    }
    public sealed class JournalOperation
    {
        public string path; public string kind; public bool existed; public string expected_sha256;
    }
    public sealed class ApplyJournal
    {
        public int schema = 1; public string transaction; public string phase;
        public long target_build; public string manifest_sha256; public List<JournalOperation> operations;
    }
    internal static class Json
    {
        internal static JavaScriptSerializer Serializer()
        {
            return new JavaScriptSerializer { MaxJsonLength = 32 * 1024 * 1024, RecursionLimit = 64 };
        }
        public static string Write(object value) { return Serializer().Serialize(value); }
        public static T Read<T>(string value) { return Serializer().Deserialize<T>(value); }
        static IDictionary<string, object> Obj(object value)
        {
            var result = value as IDictionary<string, object>;
            if (result == null) throw new UpdateFailure("MANIFEST_INVALID", "업데이트 정보의 구조가 올바르지 않습니다.");
            return result;
        }
        static object Required(IDictionary<string, object> obj, string name)
        {
            object value;
            if (!obj.TryGetValue(name, out value) || value == null) throw new UpdateFailure("MANIFEST_INVALID", "필수 업데이트 정보가 없습니다: " + name);
            return value;
        }
        static string Str(IDictionary<string, object> obj, string name)
        {
            var value = Required(obj, name) as string;
            if (value == null) throw new UpdateFailure("MANIFEST_INVALID", "문자열 정보가 올바르지 않습니다: " + name);
            return value;
        }
        static long Num(IDictionary<string, object> obj, string name)
        {
            var value = Required(obj, name);
            if (value is int) return (int)value;
            if (value is long) return (long)value;
            throw new UpdateFailure("MANIFEST_INVALID", "정수 정보가 올바르지 않습니다: " + name);
        }
        static IList Arr(IDictionary<string, object> obj, string name)
        {
            var result = Required(obj, name) as IList;
            if (result == null) throw new UpdateFailure("MANIFEST_INVALID", "목록 정보가 올바르지 않습니다: " + name);
            return result;
        }
        public static ReleaseSpec ParseManifest(byte[] raw)
        {
            try
            {
                string text = new UTF8Encoding(false, true).GetString(raw).TrimStart('\uFEFF');
                var obj = Obj(Serializer().DeserializeObject(text));
                var result = new ReleaseSpec { schema = checked((int)Num(obj, "schema")), product = Str(obj, "product"), version = Str(obj, "version"),
                    build = Num(obj, "build"), executable = Str(obj, "executable"), total_bytes = Num(obj, "total_bytes"), files = new List<FileSpec>() };
                IList files = Arr(obj, "files");
                if (files.Count < 1 || files.Count > 50000) throw new UpdateFailure("MANIFEST_INVALID", "업데이트 파일 수가 올바르지 않습니다.");
                foreach (object item in files)
                {
                    var file = Obj(item);
                    var spec = new FileSpec { path = Str(file, "path"), size = Num(file, "size"), sha256 = Str(file, "sha256"), chunks = new List<ChunkSpec>() };
                    foreach (object part in Arr(file, "chunks"))
                    {
                        var chunk = Obj(part);
                        spec.chunks.Add(new ChunkSpec { sha256 = Str(chunk, "sha256"), size = Num(chunk, "size"), url = Str(chunk, "url") });
                    }
                    result.files.Add(spec);
                }
                var notes = Arr(obj, "release_notes");
                result.release_notes = new string[notes.Count];
                for (int i = 0; i < notes.Count; i++)
                {
                    if (!(notes[i] is string)) throw new UpdateFailure("MANIFEST_INVALID", "변경 내용이 올바르지 않습니다.");
                    result.release_notes[i] = (string)notes[i];
                }
                return result;
            }
            catch (UpdateFailure) { throw; }
            catch (Exception ex) { throw new UpdateFailure("MANIFEST_INVALID", "업데이트 정보를 읽을 수 없습니다.", ex); }
        }
    }
}
