using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Reflection;
using System.Text;
using System.Threading;
using System.Windows.Forms;

[assembly: AssemblyTitle("우리 사이, 그 이상 런처")]
[assembly: AssemblyProduct("CampusRomance Launcher")]
[assembly: AssemblyVersion("1.1.0.0")]
[assembly: AssemblyFileVersion("1.1.0.0")]

namespace CampusRomance.Launcher
{
    public static class Program
    {
        public const string DefaultFeed = "https://campus-romance-playtest.naiski.chatgpt.site/";
        public static string EmbeddedText(string name)
        {
            using (var stream = Assembly.GetExecutingAssembly().GetManifestResourceStream(name))
            {
                if (stream == null) return null;
                using (var reader = new StreamReader(stream, Encoding.UTF8)) return reader.ReadToEnd();
            }
        }
        public static EngineOptions ProductionOptions(string root)
        {
            string feed = DefaultFeed;
            string config = EmbeddedText("CampusRomance.FeedConfig");
            if (config != null)
            {
                var obj = Json.Read<Dictionary<string, object>>(config);
                object value;
                if (obj.TryGetValue("feed_base_url", out value) && value is string) feed = (string)value;
            }
            return new EngineOptions { Root = root, FeedBase = new Uri(feed), PublicKeyXml = EmbeddedText("CampusRomance.UpdatePublicKey"), Cancellation = CancellationToken.None };
        }
        public static string DefaultRoot()
        {
            string own = AppDomain.CurrentDomain.BaseDirectory.TrimEnd(Path.DirectorySeparatorChar);
            if (File.Exists(Path.Combine(own, ".installed-state.json")) || Directory.Exists(Path.Combine(own, "Game"))) return own;
            if (Directory.Exists("D:\\")) return @"D:\CampusRomance_VN\Installed";
            return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "CampusRomance");
        }
        [STAThread]
        public static int Main(string[] args)
        {
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
#if !CLI
            if (args.Length == 0)
            {
                Application.EnableVisualStyles(); Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new LauncherForm()); return 0;
            }
#endif
            UpdateEngine engine = null;
            var report = new UpdateReport();
            try
            {
                Console.OutputEncoding = new UTF8Encoding(false);
                if (args.Length == 0 || args[0] == "--help" || args[0] == "help")
                {
                    Console.WriteLine(Json.Write(new { status = "ok", usage = "check|update|play --root INSTALL_ROOT [--qa --feed-base http://127.0.0.1:PORT/ --public-key QA.xml]", qa_faults = "--fail-after-apply N | --crash-after-apply N; hold-lock --hold-lock-ms N" })); return 0;
                }
                string command = args[0];
                if (command != "check" && command != "update" && command != "play" && command != "hold-lock") throw new UpdateFailure("ARGUMENT_INVALID", "지원하지 않는 명령입니다.");
                var values = new Dictionary<string, string>(StringComparer.Ordinal);
                bool qa = false;
                for (int i = 1; i < args.Length; i++)
                {
                    string name = args[i];
                    if (name == "--qa") { qa = true; continue; }
                    if (name != "--root" && name != "--feed-base" && name != "--public-key" && name != "--fail-after-apply" && name != "--crash-after-apply" && name != "--hold-lock-ms") throw new UpdateFailure("ARGUMENT_INVALID", "알 수 없는 옵션입니다: " + name);
                    if (++i >= args.Length || values.ContainsKey(name)) throw new UpdateFailure("ARGUMENT_INVALID", "명령 옵션의 값이 없거나 중복되었습니다.");
                    values[name] = args[i];
                }
#if !CLI
                if (qa) throw new UpdateFailure("QA_ONLY", "테스트 옵션은 전용 CLI에서만 사용할 수 있습니다.");
#endif
                if (!qa && (values.ContainsKey("--public-key") || values.ContainsKey("--feed-base") || values.ContainsKey("--fail-after-apply") || values.ContainsKey("--crash-after-apply") || values.ContainsKey("--hold-lock-ms") || command == "hold-lock")) throw new UpdateFailure("QA_ONLY", "공개키·채널·오류 주입 옵션은 QA 전용입니다.");
                string root;
                if (!values.TryGetValue("--root", out root)) throw new UpdateFailure("ARGUMENT_INVALID", "CLI에는 --root 설치 위치가 필요합니다.");
                EngineOptions options = ProductionOptions(root); options.Qa = qa;
                if (values.ContainsKey("--feed-base")) options.FeedBase = new Uri(values["--feed-base"]);
                if (values.ContainsKey("--public-key")) options.PublicKeyXml = File.ReadAllText(values["--public-key"], Encoding.UTF8);
                options.FailAfterApply = IntegerOption(values, "--fail-after-apply");
                options.CrashAfterApply = IntegerOption(values, "--crash-after-apply");
                options.HoldLockMilliseconds = IntegerOption(values, "--hold-lock-ms");
                if (options.FailAfterApply > 0 && options.CrashAfterApply > 0) throw new UpdateFailure("ARGUMENT_INVALID", "오류 주입은 한 종류만 선택해 주세요.");
                engine = new UpdateEngine(options);
                if (command == "check") report = engine.Check();
                else if (command == "update") report = engine.Update();
                else if (command == "play") report = engine.Play();
                else report = engine.HoldLock();
                Console.WriteLine(Json.Write(report)); return 0;
            }
            catch (Exception ex)
            {
                if (engine != null) report = engine.Report;
                report.status = "error";
                var failure = ex as UpdateFailure;
                report.code = failure == null ? (ex is OperationCanceledException ? "CANCELLED" : "IO_ERROR") : failure.Code;
                report.message = failure == null ? (ex is OperationCanceledException ? "작업을 취소했습니다. 기존 게임은 유지됩니다." : "작업을 완료하지 못했습니다: " + ex.Message) : failure.Message;
                try { Console.WriteLine(Json.Write(report)); } catch { }
                return ExitCode(report.code);
            }
        }
        static int IntegerOption(Dictionary<string, string> values, string name)
        {
            string value; int result;
            if (!values.TryGetValue(name, out value)) return 0;
            if (!Int32.TryParse(value, out result) || result < 0) throw new UpdateFailure("ARGUMENT_INVALID", "정수 옵션이 올바르지 않습니다: " + name);
            return result;
        }
        static int ExitCode(string code)
        {
            if (code == "SIGNATURE_INVALID") return 2;
            if (code == "MANIFEST_INVALID" || code == "UNSAFE_PATH" || code == "PROTECTED_PATH" || code == "FEED_INVALID") return 3;
            if (code == "DOWNGRADE_BLOCKED" || code == "RELEASE_CONFLICT") return 4;
            if (code == "UPDATE_BUSY" || code == "GAME_RUNNING") return 5;
            if (code == "FEED_UNAVAILABLE" || code == "DOWNLOAD_FAILED" || code == "HASH_MISMATCH" || code == "APPLY_FAILED" || code == "RECOVERY_REQUIRED" || code == "IO_ERROR") return 6;
            return 1;
        }
    }
}
