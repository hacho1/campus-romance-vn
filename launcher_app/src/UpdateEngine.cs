using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;

namespace CampusRomance.Launcher
{
    public sealed class UpdateEngine
    {
        const int MaximumManifest = 8 * 1024 * 1024;
        const int MaximumChunk = 8 * 1024 * 1024;
        readonly EngineOptions options;
        readonly string root, game, metadata, transactions, journalPath, statePath, chunks;
        public UpdateReport Report { get; private set; }
        public UpdateEngine(EngineOptions options)
        {
            this.options = options;
            root = SafePaths.CanonicalRoot(options.Root);
            game = SafePaths.Within(root, "Game");
            metadata = SafePaths.Within(root, ".campus-launcher");
            transactions = SafePaths.Within(metadata, "transactions");
            chunks = SafePaths.Within(metadata, "chunks");
            journalPath = SafePaths.Within(metadata, "journal.json");
            statePath = SafePaths.Within(root, ".installed-state.json");
            if (options.FeedBase == null || !options.FeedBase.IsAbsoluteUri || !String.IsNullOrEmpty(options.FeedBase.UserInfo) || !String.IsNullOrEmpty(options.FeedBase.Query) || !String.IsNullOrEmpty(options.FeedBase.Fragment)) throw new UpdateFailure("FEED_INVALID", "업데이트 주소가 올바르지 않습니다.");
            if (options.FeedBase.Scheme != Uri.UriSchemeHttps && !(options.Qa && options.FeedBase.Scheme == Uri.UriSchemeHttp && options.FeedBase.IsLoopback)) throw new UpdateFailure("FEED_INVALID", "업데이트는 HTTPS 연결만 사용할 수 있습니다.");
            if (!options.FeedBase.AbsoluteUri.EndsWith("/")) throw new UpdateFailure("FEED_INVALID", "업데이트 기본 주소는 /로 끝나야 합니다.");
            Report = new UpdateReport { root = root, qa = options.Qa };
        }
        public static string HashBytes(byte[] value)
        {
            using (var sha = SHA256.Create()) return Hex(sha.ComputeHash(value));
        }
        static string Hex(byte[] value) { return BitConverter.ToString(value).Replace("-", "").ToLowerInvariant(); }
        string HashFile(string path)
        {
            SafePaths.CheckNoReparse(path);
            using (var sha = SHA256.Create())
            using (var input = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                byte[] buffer = new byte[1024 * 1024]; int count;
                while ((count = input.Read(buffer, 0, buffer.Length)) != 0)
                {
                    options.Cancellation.ThrowIfCancellationRequested();
                    sha.TransformBlock(buffer, 0, count, null, 0);
                }
                sha.TransformFinalBlock(new byte[0], 0, 0);
                return Hex(sha.Hash);
            }
        }
        bool Matches(string path, long size, string hash)
        {
            SafePaths.CheckNoReparse(path);
            return File.Exists(path) && new FileInfo(path).Length == size && HashFile(path) == hash;
        }
        void Progress(string phase, string file, long current, long total)
        {
            if (options.Progress != null) options.Progress(new ProgressInfo(phase, file, current, total));
        }
        byte[] ReadRemote(Uri uri, int maximum)
        {
            options.Cancellation.ThrowIfCancellationRequested();
            try
            {
                var request = (HttpWebRequest)WebRequest.Create(uri);
                request.UserAgent = "CampusRomanceLauncher/1.0";
                request.AllowAutoRedirect = false; request.Timeout = 25000; request.ReadWriteTimeout = 25000;
                request.AutomaticDecompression = DecompressionMethods.GZip | DecompressionMethods.Deflate;
                request.CachePolicy = new System.Net.Cache.RequestCachePolicy(System.Net.Cache.RequestCacheLevel.NoCacheNoStore);
                using (var response = (HttpWebResponse)request.GetResponse())
                {
                    if (response.StatusCode != HttpStatusCode.OK) throw new UpdateFailure("FEED_UNAVAILABLE", "업데이트 채널에 접근할 수 없습니다. 공개 상태와 인터넷 연결을 확인해 주세요.");
                    if (response.ContentLength > maximum) throw new UpdateFailure("MANIFEST_INVALID", "업데이트 정보의 크기가 제한을 초과했습니다.");
                    using (var stream = response.GetResponseStream())
                    using (var output = new MemoryStream())
                    {
                        byte[] buffer = new byte[65536]; int count;
                        while ((count = stream.Read(buffer, 0, buffer.Length)) != 0)
                        {
                            options.Cancellation.ThrowIfCancellationRequested();
                            if (output.Length + count > maximum) throw new UpdateFailure("MANIFEST_INVALID", "업데이트 정보의 크기가 제한을 초과했습니다.");
                            output.Write(buffer, 0, count);
                        }
                        return output.ToArray();
                    }
                }
            }
            catch (UpdateFailure) { throw; }
            catch (OperationCanceledException) { throw; }
            catch (Exception ex) { throw new UpdateFailure("FEED_UNAVAILABLE", "업데이트 채널을 불러오지 못했습니다. 인터넷 연결 또는 채널의 접근 권한을 확인해 주세요.", ex); }
        }
        void VerifySignature(byte[] raw, byte[] signature)
        {
            try
            {
                using (var rsa = new RSACryptoServiceProvider())
                {
                    rsa.PersistKeyInCsp = false;
                    rsa.FromXmlString(options.PublicKeyXml);
                    if (rsa.KeySize != 2048 || signature.Length != 256 || !rsa.VerifyData(raw, CryptoConfig.MapNameToOID("SHA256"), signature)) throw new UpdateFailure("SIGNATURE_INVALID", "업데이트 서명을 확인하지 못했습니다. 설치 파일은 변경하지 않았습니다.");
                }
            }
            catch (UpdateFailure) { throw; }
            catch (Exception ex) { throw new UpdateFailure("SIGNATURE_INVALID", "업데이트 서명이 올바르지 않습니다.", ex); }
        }
        VerifiedRelease Verified(byte[] raw, byte[] signature)
        {
            // No JSON parsing or filesystem mutation precedes this verification.
            VerifySignature(raw, signature);
            ReleaseSpec release = Json.ParseManifest(raw);
            Validate(release);
            return new VerifiedRelease { Release = release, Raw = raw, Signature = signature, Hash = HashBytes(raw) };
        }
        VerifiedRelease FetchRelease()
        {
            Progress("업데이트 정보 확인", "", 0, 0);
            byte[] raw = ReadRemote(new Uri(options.FeedBase, "releases/latest.json"), MaximumManifest);
            // Bind the detached signature to the exact bytes already fetched.
            // A release-pointer switch between these two requests is harmless.
            byte[] signatureText = ReadRemote(new Uri(options.FeedBase, "releases/latest.sig?manifest=" + HashBytes(raw)), 16384);
            byte[] signature;
            try { signature = Convert.FromBase64String(Encoding.ASCII.GetString(signatureText).Trim()); }
            catch (Exception ex) { throw new UpdateFailure("SIGNATURE_INVALID", "서명 파일을 읽을 수 없습니다. 채널의 접근 권한을 확인해 주세요.", ex); }
            return Verified(raw, signature);
        }
        void Validate(ReleaseSpec release)
        {
            if (release.schema != 1 || release.product != "campus-romance" || release.build <= 0 || release.total_bytes < 0 || String.IsNullOrWhiteSpace(release.version) || release.version.Length > 80) throw new UpdateFailure("MANIFEST_INVALID", "지원하지 않는 업데이트 정보입니다.");
            SafePaths.ValidateRelative(release.executable);
            if (!release.executable.EndsWith(".exe", StringComparison.OrdinalIgnoreCase)) throw new UpdateFailure("MANIFEST_INVALID", "게임 실행 파일이 올바르지 않습니다.");
            var paths = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
            var chunkSizes = new Dictionary<string, long>(StringComparer.OrdinalIgnoreCase);
            long total = 0;
            foreach (FileSpec file in release.files)
            {
                SafePaths.ValidateRelative(file.path);
                SafePaths.Within(game, file.path);
                if (!paths.Add(file.path) || file.size < 0 || !IsHash(file.sha256)) throw new UpdateFailure("MANIFEST_INVALID", "중복되거나 잘못된 업데이트 파일입니다: " + file.path);
                file.sha256 = file.sha256.ToLowerInvariant();
                long partTotal = 0;
                foreach (ChunkSpec chunk in file.chunks)
                {
                    if (!IsHash(chunk.sha256) || chunk.size <= 0 || chunk.size > MaximumChunk) throw new UpdateFailure("MANIFEST_INVALID", "업데이트 조각의 정보가 올바르지 않습니다.");
                    chunk.sha256 = chunk.sha256.ToLowerInvariant();
                    if (chunk.url != "payload/chunks/" + chunk.sha256 + ".bin") throw new UpdateFailure("UNSAFE_PATH", "업데이트 조각의 주소가 올바르지 않습니다.");
                    long known;
                    if (chunkSizes.TryGetValue(chunk.sha256, out known) && known != chunk.size) throw new UpdateFailure("MANIFEST_INVALID", "같은 조각의 크기가 서로 다릅니다.");
                    chunkSizes[chunk.sha256] = chunk.size;
                    partTotal = checked(partTotal + chunk.size);
                }
                if (partTotal != file.size || (file.size == 0 && file.sha256 != HashBytes(new byte[0]))) throw new UpdateFailure("MANIFEST_INVALID", "파일과 조각의 크기가 일치하지 않습니다: " + file.path);
                total = checked(total + file.size);
            }
            if (!paths.Contains(release.executable) || total != release.total_bytes) throw new UpdateFailure("MANIFEST_INVALID", "실행 파일 또는 전체 크기 정보가 올바르지 않습니다.");
            string[] ordered = paths.OrderBy(p => p, StringComparer.OrdinalIgnoreCase).ToArray();
            for (int i = 1; i < ordered.Length; i++) if (ordered[i].StartsWith(ordered[i - 1] + "/", StringComparison.OrdinalIgnoreCase)) throw new UpdateFailure("UNSAFE_PATH", "파일과 폴더 경로가 충돌합니다.");
        }
        static bool IsHash(string value) { return value != null && Regex.IsMatch(value, "^[0-9a-fA-F]{64}$"); }
        StoredRelease ReadInstalled()
        {
            SafePaths.CheckNoReparse(statePath);
            if (!File.Exists(statePath)) return null;
            try
            {
                if (new FileInfo(statePath).Length > 16 * 1024 * 1024) throw new Exception("State too large.");
                var state = Json.Read<InstalledState>(File.ReadAllText(statePath, Encoding.UTF8));
                if (state == null || state.schema != 1 || state.product != "campus-romance") throw new Exception("Bad state.");
                var verified = Verified(Convert.FromBase64String(state.manifest_base64), Convert.FromBase64String(state.signature_base64));
                if (state.manifest_sha256 != verified.Hash || state.build != verified.Release.build || state.version != verified.Release.version) throw new Exception("State does not match signed manifest.");
                return new StoredRelease { State = state, Verified = verified };
            }
            catch (UpdateFailure) { throw; }
            catch (Exception ex) { throw new UpdateFailure("STATE_INVALID", "설치 기록을 확인할 수 없습니다. 기존 게임과 저장 기록은 유지했습니다.", ex); }
        }
        public InstalledState InspectInstalled()
        {
            var stored = ReadInstalled(); return stored == null ? null : stored.State;
        }
        void Populate(VerifiedRelease latest, StoredRelease installed)
        {
            Report.latest_build = latest.Release.build; Report.version = latest.Release.version;
            Report.total_bytes = latest.Release.total_bytes; Report.release_notes = latest.Release.release_notes;
            Report.installed_build = installed == null ? 0 : installed.State.build;
            Report.installed_version = installed == null ? null : installed.State.version;
            Report.first_install = installed == null;
            Report.update_available = installed == null || latest.Release.build > installed.State.build;
            if (installed != null && latest.Release.build < installed.State.build) throw new UpdateFailure("DOWNGRADE_BLOCKED", "설치된 버전보다 이전 업데이트입니다. 현재 게임을 유지했습니다.");
            if (installed != null && latest.Release.build == installed.State.build && latest.Hash != installed.Verified.Hash) throw new UpdateFailure("RELEASE_CONFLICT", "같은 빌드 번호의 내용이 바뀌었습니다. 새 빌드가 게시될 때까지 현재 게임을 유지합니다.");
        }
        List<FileSpec> Changed(ReleaseSpec release)
        {
            var changed = new List<FileSpec>(); long inspected = 0;
            foreach (FileSpec file in release.files)
            {
                options.Cancellation.ThrowIfCancellationRequested();
                string target = SafePaths.Within(game, file.path);
                if (Directory.Exists(target)) throw new UpdateFailure("UNSAFE_PATH", "파일 위치에 폴더가 있습니다: " + file.path);
                if (!Matches(target, file.size, file.sha256)) changed.Add(file);
                inspected += file.size; Progress("설치 파일 검사", file.path, inspected, release.total_bytes);
            }
            Report.changed_files = changed.Select(p => p.path).ToList();
            if (changed.Count > 0) Report.update_available = true;
            return changed;
        }
        List<FileSpec> Stale(ReleaseSpec release, StoredRelease installed)
        {
            var result = new List<FileSpec>();
            if (installed == null) return result;
            var current = new HashSet<string>(release.files.Select(f => f.path), StringComparer.OrdinalIgnoreCase);
            foreach (var file in installed.Verified.Release.files)
            {
                if (current.Contains(file.path)) continue;
                string target = SafePaths.Within(game, file.path);
                if (Matches(target, file.size, file.sha256)) result.Add(file);
                else if (File.Exists(target)) Report.preserved_modified_files.Add(file.path);
            }
            return result;
        }
        public UpdateReport Check()
        {
            Report.command = "check";
            var latest = FetchRelease();
            using (var gate = AcquireGate(false))
            {
                if (File.Exists(journalPath)) throw new UpdateFailure("RECOVERY_REQUIRED", "중단된 업데이트가 있습니다. 설치·업데이트를 눌러 복구해 주세요.");
                Populate(latest, ReadInstalled());
                Changed(latest.Release);
            }
            Report.message = Report.update_available ? "설치 또는 업데이트를 할 수 있습니다." : "최신 버전입니다.";
            return Report;
        }
        public UpdateReport HoldLock()
        {
            if (!options.Qa) throw new UpdateFailure("QA_ONLY", "테스트 전용 명령입니다.");
            Report.command = "hold-lock"; FetchRelease();
            using (var gate = AcquireGate(false)) Thread.Sleep(Math.Max(1, Math.Min(30000, options.HoldLockMilliseconds)));
            return Report;
        }
        public UpdateReport Update()
        {
            Report.command = "update";
            VerifiedRelease latest = FetchRelease();
            using (var gate = AcquireGate(true))
            {
                EnsureGameStopped();
                if (File.Exists(journalPath)) { Recover(); Report.recovery_performed = true; }
                var installed = ReadInstalled();
                Populate(latest, installed);
                List<FileSpec> changed = Changed(latest.Release);
                List<FileSpec> stale = Stale(latest.Release, installed);
                if (changed.Count == 0 && stale.Count == 0 && installed != null && latest.Hash == installed.Verified.Hash)
                {
                    Report.update_available = false; Report.message = "최신 버전이며 모든 파일이 정상입니다."; return Report;
                }
                options.Cancellation.ThrowIfCancellationRequested();
                string id = Guid.NewGuid().ToString("N");
                string transaction = SafePaths.Within(transactions, id);
                string stage = SafePaths.Within(transaction, "stage");
                string backup = SafePaths.Within(transaction, "backup");
                Directory.CreateDirectory(stage); Directory.CreateDirectory(backup);
                bool journalWritten = false; bool committed = false;
                try
                {
                    StageAll(changed, stage);
                    options.Cancellation.ThrowIfCancellationRequested();
                    EnsureGameStopped();
                    var ops = new List<JournalOperation>();
                    foreach (FileSpec file in changed) ops.Add(new JournalOperation { path = file.path, kind = "write", existed = File.Exists(SafePaths.Within(game, file.path)), expected_sha256 = file.sha256 });
                    foreach (FileSpec file in stale) ops.Add(new JournalOperation { path = file.path, kind = "delete", existed = true, expected_sha256 = file.sha256 });
                    var journal = new ApplyJournal { transaction = id, phase = "prepared", target_build = latest.Release.build, manifest_sha256 = latest.Hash, operations = ops };
                    AtomicJson(journalPath, journal); journalWritten = true;
                    journal.phase = "applying"; AtomicJson(journalPath, journal);
                    int applied = 0;
                    foreach (var op in ops)
                    {
                        EnsureGameStopped();
                        string target = SafePaths.Within(game, op.path);
                        string old = SafePaths.Within(backup, op.path);
                        if (op.existed)
                        {
                            Directory.CreateDirectory(Path.GetDirectoryName(old));
                            if (!File.Exists(target)) throw new IOException("Expected old file disappeared: " + op.path);
                            File.Move(target, old);
                        }
                        else if (File.Exists(target)) throw new IOException("A file appeared during installation: " + op.path);
                        if (op.kind == "write")
                        {
                            Directory.CreateDirectory(Path.GetDirectoryName(target));
                            File.Move(SafePaths.Within(stage, op.path), target);
                        }
                        applied++; Progress("업데이트 적용", op.path, applied, ops.Count);
                        if (options.Qa && options.CrashAfterApply > 0 && applied == options.CrashAfterApply) Environment.Exit(73);
                        if (options.Qa && options.FailAfterApply > 0 && applied == options.FailAfterApply) throw new IOException("QA injected apply failure.");
                    }
                    var state = new InstalledState { version = latest.Release.version, build = latest.Release.build, transaction = id, manifest_sha256 = latest.Hash,
                        manifest_base64 = Convert.ToBase64String(latest.Raw), signature_base64 = Convert.ToBase64String(latest.Signature), installed_utc = DateTime.UtcNow.ToString("o") };
                    AtomicJson(statePath, state); committed = true;
                    Report.deleted_files = stale.Select(f => f.path).ToList();
                    Report.installed_build = latest.Release.build; Report.installed_version = latest.Release.version;
                    Report.update_available = false; Report.message = "설치가 완료되었습니다. 게임을 시작할 수 있어요.";
                    // The atomically replaced signed state is the commit point.
                    // If cleanup is interrupted, the next run recognizes it.
                    try { journal.phase = "committed"; AtomicJson(journalPath, journal); CleanupJournal(transaction); }
                    catch { Report.message += " 임시 파일은 다음 확인 때 정리됩니다."; }
                    Progress("완료", "", Report.downloaded_bytes, Report.downloaded_bytes);
                    return Report;
                }
                catch (Exception ex)
                {
                    if (!committed)
                    {
                        if (journalWritten)
                        {
                            try { Recover(); Report.recovery_performed = true; }
                            catch (Exception recovery) { throw new UpdateFailure("RECOVERY_REQUIRED", "업데이트가 중단되었습니다. 게임을 닫고 다시 업데이트해 복구해 주세요. 저장 기록은 변경하지 않았습니다.", recovery); }
                        }
                        else { try { SafePaths.DeletePrivateTree(transactions, transaction); } catch { } }
                    }
                    if (ex is UpdateFailure) throw;
                    if (ex is OperationCanceledException) throw;
                    throw new UpdateFailure("APPLY_FAILED", "업데이트를 적용하지 못해 이전 상태로 복구했습니다. 게임과 사용 중인 프로그램을 닫고 다시 시도해 주세요.", ex);
                }
            }
        }
        void StageAll(List<FileSpec> changed, string stage)
        {
            Directory.CreateDirectory(chunks);
            var required = new Dictionary<string, ChunkSpec>();
            foreach (FileSpec file in changed) foreach (ChunkSpec part in file.chunks) required[part.sha256] = part;
            long transfer = 0;
            foreach (ChunkSpec part in required.Values) if (!Matches(SafePaths.Within(chunks, part.sha256 + ".bin"), part.size, part.sha256)) transfer += part.size;
            foreach (FileSpec file in changed)
            {
                options.Cancellation.ThrowIfCancellationRequested();
                string target = SafePaths.Within(stage, file.path);
                Directory.CreateDirectory(Path.GetDirectoryName(target));
                using (var output = new FileStream(target, FileMode.CreateNew, FileAccess.Write, FileShare.None))
                {
                    foreach (ChunkSpec part in file.chunks)
                    {
                        string cached = SafePaths.Within(chunks, part.sha256 + ".bin");
                        if (!Matches(cached, part.size, part.sha256)) DownloadChunk(part, cached, file.path, transfer);
                        else Report.reused_chunks++;
                        using (var input = new FileStream(cached, FileMode.Open, FileAccess.Read, FileShare.Read)) input.CopyTo(output);
                    }
                    output.Flush(true);
                }
                if (!Matches(target, file.size, file.sha256)) throw new UpdateFailure("HASH_MISMATCH", "완성된 업데이트 파일을 검증하지 못했습니다: " + file.path);
            }
        }
        void DownloadChunk(ChunkSpec part, string destination, string file, long transfer)
        {
            options.Cancellation.ThrowIfCancellationRequested();
            SafePaths.CheckNoReparse(destination);
            string temporary = destination + "." + Guid.NewGuid().ToString("N") + ".part";
            try
            {
                Report.downloaded_chunks++;
                var request = (HttpWebRequest)WebRequest.Create(new Uri(options.FeedBase, part.url));
                request.AllowAutoRedirect = false; request.Timeout = 25000; request.ReadWriteTimeout = 25000;
                request.UserAgent = "CampusRomanceLauncher/1.0";
                request.CachePolicy = new System.Net.Cache.RequestCachePolicy(System.Net.Cache.RequestCacheLevel.NoCacheNoStore);
                using (var response = (HttpWebResponse)request.GetResponse())
                {
                    if (response.StatusCode != HttpStatusCode.OK || (response.ContentLength >= 0 && response.ContentLength != part.size)) throw new UpdateFailure("HASH_MISMATCH", "업데이트 조각의 크기가 올바르지 않습니다.");
                    using (var input = response.GetResponseStream())
                    using (var output = new FileStream(temporary, FileMode.CreateNew, FileAccess.Write, FileShare.None))
                    {
                        byte[] buffer = new byte[65536]; int count; long read = 0;
                        while ((count = input.Read(buffer, 0, buffer.Length)) != 0)
                        {
                            options.Cancellation.ThrowIfCancellationRequested();
                            read += count; Report.downloaded_bytes += count;
                            if (read > part.size) throw new UpdateFailure("HASH_MISMATCH", "업데이트 조각의 크기가 올바르지 않습니다.");
                            output.Write(buffer, 0, count);
                            Progress("변경된 파일 다운로드", file, Report.downloaded_bytes, transfer);
                        }
                        output.Flush(true);
                    }
                }
                if (!Matches(temporary, part.size, part.sha256)) throw new UpdateFailure("HASH_MISMATCH", "다운로드한 조각의 SHA-256이 일치하지 않습니다. 기존 게임은 그대로입니다.");
                if (File.Exists(destination)) File.Delete(destination);
                File.Move(temporary, destination);
            }
            catch (UpdateFailure) { throw; }
            catch (OperationCanceledException) { throw; }
            catch (Exception ex) { throw new UpdateFailure("DOWNLOAD_FAILED", "업데이트 다운로드가 중단되었습니다. 다시 시도하면 검증된 조각을 이어서 사용합니다.", ex); }
            finally { if (File.Exists(temporary)) File.Delete(temporary); }
        }
        void Recover()
        {
            SafePaths.CheckNoReparse(journalPath);
            if (!File.Exists(journalPath)) return;
            ApplyJournal journal;
            try { journal = Json.Read<ApplyJournal>(File.ReadAllText(journalPath, Encoding.UTF8)); }
            catch (Exception ex) { throw new UpdateFailure("RECOVERY_REQUIRED", "복구 기록을 읽을 수 없습니다.", ex); }
            if (journal == null || journal.schema != 1 || !Regex.IsMatch(journal.transaction ?? "", "^[0-9a-f]{32}$") || journal.operations == null || !IsHash(journal.manifest_sha256)) throw new UpdateFailure("RECOVERY_REQUIRED", "복구 기록이 올바르지 않습니다.");
            foreach (var op in journal.operations)
            {
                SafePaths.ValidateRelative(op.path);
                if ((op.kind != "write" && op.kind != "delete") || !IsHash(op.expected_sha256)) throw new UpdateFailure("RECOVERY_REQUIRED", "복구 작업이 올바르지 않습니다.");
            }
            string transaction = SafePaths.Within(transactions, journal.transaction);
            StoredRelease state = ReadInstalled();
            if (state != null && state.State.transaction == journal.transaction && state.State.build == journal.target_build && state.Verified.Hash == journal.manifest_sha256)
            {
                CleanupJournal(transaction); return;
            }
            Progress("이전 업데이트 복구", "", 0, journal.operations.Count);
            // Cancellation must not interrupt rollback of an already-applied transaction.
            CancellationToken previous = options.Cancellation; options.Cancellation = CancellationToken.None;
            try
            {
                foreach (var op in journal.operations.AsEnumerable().Reverse())
                {
                    string target = SafePaths.Within(game, op.path);
                    string old = SafePaths.Within(SafePaths.Within(transaction, "backup"), op.path);
                    string staged = SafePaths.Within(SafePaths.Within(transaction, "stage"), op.path);
                    if (File.Exists(old))
                    {
                        if (File.Exists(target))
                        {
                            if (op.kind != "write" || HashFile(target) != op.expected_sha256) throw new UpdateFailure("RECOVERY_REQUIRED", "업데이트 중 파일이 다른 프로그램에 의해 바뀌었습니다: " + op.path);
                            File.Delete(target);
                        }
                        Directory.CreateDirectory(Path.GetDirectoryName(target)); File.Move(old, target);
                    }
                    else if (!op.existed && op.kind == "write" && !File.Exists(staged) && File.Exists(target))
                    {
                        if (HashFile(target) != op.expected_sha256) throw new UpdateFailure("RECOVERY_REQUIRED", "새 파일이 변경되어 자동 복구를 멈췄습니다: " + op.path);
                        File.Delete(target);
                    }
                }
                CleanupJournal(transaction);
            }
            finally { options.Cancellation = previous; }
        }
        void CleanupJournal(string transaction)
        {
            SafePaths.DeletePrivateTree(transactions, transaction);
            SafePaths.CheckNoReparse(journalPath); if (File.Exists(journalPath)) File.Delete(journalPath);
        }
        static void AtomicJson(string path, object value)
        {
            SafePaths.CheckNoReparse(path);
            Directory.CreateDirectory(Path.GetDirectoryName(path));
            string temp = path + "." + Guid.NewGuid().ToString("N") + ".tmp";
            try
            {
                using (var output = new FileStream(temp, FileMode.CreateNew, FileAccess.Write, FileShare.None))
                {
                    byte[] bytes = new UTF8Encoding(false).GetBytes(Json.Write(value));
                    output.Write(bytes, 0, bytes.Length); output.Flush(true);
                }
                if (File.Exists(path)) File.Replace(temp, path, null, true);
                else File.Move(temp, path);
            }
            finally { if (File.Exists(temp)) File.Delete(temp); }
        }
        sealed class Gate : IDisposable
        {
            public Mutex Mutex; public FileStream File;
            public void Dispose() { if (File != null) File.Dispose(); if (Mutex != null) { Mutex.ReleaseMutex(); Mutex.Dispose(); } }
        }
        IDisposable AcquireGate(bool write)
        {
            string name = "Local\\CampusRomanceUpdate-" + HashBytes(Encoding.UTF8.GetBytes(root.ToUpperInvariant()));
            var gate = new Gate { Mutex = new Mutex(false, name) };
            bool acquired;
            try { acquired = gate.Mutex.WaitOne(0); }
            catch (AbandonedMutexException) { acquired = true; }
            if (!acquired) { gate.Mutex.Dispose(); gate.Mutex = null; throw new UpdateFailure("UPDATE_BUSY", "같은 설치 위치에서 다른 런처가 작업 중입니다."); }
            try
            {
                if (write)
                {
                    EnsureGameStopped(); SafePaths.CheckNoReparse(metadata); Directory.CreateDirectory(metadata);
                    string lockFile = SafePaths.Within(metadata, "update.lock");
                    gate.File = new FileStream(lockFile, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.None);
                    if (options.Qa && options.HoldLockMilliseconds > 0) Thread.Sleep(Math.Min(30000, options.HoldLockMilliseconds));
                }
                return gate;
            }
            catch (IOException ex) { gate.Dispose(); throw new UpdateFailure("UPDATE_BUSY", "설치 폴더가 다른 작업에서 사용 중입니다.", ex); }
            catch { gate.Dispose(); throw; }
        }
        public void EnsureGameStopped()
        {
            string prefix = game.TrimEnd(Path.DirectorySeparatorChar) + Path.DirectorySeparatorChar;
            foreach (var process in Process.GetProcesses())
            {
                using (process)
                {
                    if (process.Id == Process.GetCurrentProcess().Id) continue;
                    string executable = null;
                    try { executable = process.MainModule.FileName; }
                    catch { continue; }
                    if (executable != null && Path.GetFullPath(executable).StartsWith(prefix, StringComparison.OrdinalIgnoreCase)) throw new UpdateFailure("GAME_RUNNING", "게임이 실행 중입니다. 게임을 완전히 종료한 뒤 업데이트해 주세요.");
                }
            }
        }
        public UpdateReport Play()
        {
            Report.command = "play";
            using (var gate = AcquireGate(false))
            {
                if (File.Exists(journalPath)) throw new UpdateFailure("RECOVERY_REQUIRED", "중단된 업데이트를 먼저 복구해 주세요.");
                var installed = ReadInstalled();
                if (installed == null) throw new UpdateFailure("NOT_INSTALLED", "게임을 먼저 설치해 주세요.");
                string relative = installed.Verified.Release.executable;
                FileSpec executable = installed.Verified.Release.files.First(f => String.Equals(f.path, relative, StringComparison.OrdinalIgnoreCase));
                string target = SafePaths.Within(game, relative);
                if (!Matches(target, executable.size, executable.sha256)) throw new UpdateFailure("GAME_INVALID", "실행 파일이 없거나 바뀌었습니다. 설치·업데이트로 복구해 주세요.");
                EnsureGameStopped();
                Report.installed_build = installed.State.build; Report.installed_version = installed.State.version; Report.version = installed.State.version; Report.executable = target;
                if (!options.Qa) Process.Start(new ProcessStartInfo(target) { WorkingDirectory = game, UseShellExecute = false });
                Report.message = options.Qa ? "QA: 실행 파일 검증 완료. 실제 게임은 실행하지 않았습니다." : "게임을 시작했습니다.";
                return Report;
            }
        }
    }
}
