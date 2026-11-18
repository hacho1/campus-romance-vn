using System;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Threading;
using System.Windows.Forms;

namespace CampusRomance.Launcher
{
    internal sealed class SoftPanel : Panel
    {
        public Color Fill = Color.White;
        public SoftPanel() { DoubleBuffered = true; BackColor = Color.Transparent; }
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            using (GraphicsPath path = Rounded(new RectangleF(1, 1, Width - 3, Height - 3), 16))
            using (var fill = new SolidBrush(Fill))
            using (var border = new Pen(Color.FromArgb(226, 230, 240)))
            { e.Graphics.FillPath(fill, path); e.Graphics.DrawPath(border, path); }
            base.OnPaint(e);
        }
        internal static GraphicsPath Rounded(RectangleF r, float radius)
        {
            var path = new GraphicsPath(); float d = radius * 2;
            path.AddArc(r.X, r.Y, d, d, 180, 90); path.AddArc(r.Right - d, r.Y, d, d, 270, 90);
            path.AddArc(r.Right - d, r.Bottom - d, d, d, 0, 90); path.AddArc(r.X, r.Bottom - d, d, d, 90, 90); path.CloseFigure(); return path;
        }
    }
    internal sealed class CalmButton : Button
    {
        public Color Fill = Color.White, Ink = Color.FromArgb(47, 63, 88);
        bool hover;
        public CalmButton()
        {
            FlatStyle = FlatStyle.Flat; FlatAppearance.BorderSize = 0; Cursor = Cursors.Hand;
            Font = new Font("맑은 고딕", 10, FontStyle.Bold); UseVisualStyleBackColor = false;
            SetStyle(ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint | ControlStyles.OptimizedDoubleBuffer, true);
        }
        protected override void OnMouseEnter(EventArgs e) { hover = true; Invalidate(); base.OnMouseEnter(e); }
        protected override void OnMouseLeave(EventArgs e) { hover = false; Invalidate(); base.OnMouseLeave(e); }
        protected override void OnPaint(PaintEventArgs e)
        {
            // Paint the complete backing surface before the rounded face so
            // no native/transparent button background leaks into its corners.
            var surface = Parent as SoftPanel;
            Color backing = surface == null ? BackColor : surface.Fill;
            if (backing.A != 255) backing = FindForm() == null ? Color.FromArgb(244, 246, 251) : FindForm().BackColor;
            e.Graphics.Clear(backing);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            Color fill = Enabled ? (hover ? ControlPaint.Light(Fill, 0.10f) : Fill) : Color.FromArgb(230, 234, 242);
            using (var path = SoftPanel.Rounded(new RectangleF(1, 1, Width - 3, Height - 3), 12))
            using (var brush = new SolidBrush(fill))
            using (var pen = new Pen(Fill == Color.White ? Color.FromArgb(218, 225, 237) : fill))
            { e.Graphics.FillPath(brush, path); e.Graphics.DrawPath(pen, path); }
            TextRenderer.DrawText(e.Graphics, Text, Font, ClientRectangle, Enabled ? Ink : Color.FromArgb(138, 148, 167), TextFormatFlags.HorizontalCenter | TextFormatFlags.VerticalCenter | TextFormatFlags.SingleLine | TextFormatFlags.NoPadding);
            if (Focused && ShowFocusCues) ControlPaint.DrawFocusRectangle(e.Graphics, Rectangle.Inflate(ClientRectangle, -6, -6));
        }
    }
    internal sealed class ThinProgress : Control
    {
        public double Value;
        public ThinProgress() { DoubleBuffered = true; }
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            using (var brush = new SolidBrush(Color.FromArgb(223, 229, 240)))
            using (var track = SoftPanel.Rounded(new RectangleF(0, 0, Width, Height), Height / 2f)) e.Graphics.FillPath(brush, track);
            int width = (int)(Width * Math.Max(0, Math.Min(1, Value)));
            if (width > 3)
                using (var brush = new SolidBrush(Color.FromArgb(112, 133, 183)))
                using (var path = SoftPanel.Rounded(new RectangleF(0, 0, width, Height), Height / 2f)) e.Graphics.FillPath(brush, path);
        }
    }
    public sealed class LauncherForm : Form
    {
        static readonly Color Ink = Color.FromArgb(43, 58, 82), Muted = Color.FromArgb(100, 113, 137);
        readonly TextBox rootBox;
        readonly Label installedLabel, latestLabel, statusLabel, bytesLabel, installedBuild, latestBuild;
        readonly TextBox notes;
        readonly CalmButton checkButton, updateButton, playButton, browseButton, cancelButton;
        readonly ThinProgress progress;
        readonly Panel installationPage, noticePage;
        readonly CalmButton installationTab, noticeTab;
        readonly Label noticeVersionLabel, noticeBuildLabel;
        string selectedPage = "install";
        public string SelectedPage { get { return selectedPage; } }
        readonly CheckBox legacyCheck;
        readonly bool legacyDetected;
        const string LegacySource = @"D:\CampusRomance_VN\renpy_project\saves";
        BackgroundWorker worker; CancellationTokenSource cancellation;
        bool closingWhenIdle; readonly bool automaticCheck; DateTime lastProgress;
        public LauncherForm() : this(true) { }
        // The false constructor is suitable for headless DrawToBitmap QA.
        // Construction performs no network access or installation mutation.
        public LauncherForm(bool automaticCheck)
        {
            this.automaticCheck = automaticCheck;
            Text = "우리 사이, 그 이상 런처"; ClientSize = new Size(960, 710);
            FormBorderStyle = FormBorderStyle.FixedSingle; MaximizeBox = false;
            StartPosition = FormStartPosition.CenterScreen; BackColor = Color.FromArgb(244, 246, 251);
            Font = new Font("맑은 고딕", 10); ForeColor = Ink; AutoScaleMode = AutoScaleMode.None;
            Icon = LoadLauncherIcon(); DoubleBuffered = true; KeyPreview = true;
            AddLabel(this, "우리 사이, 그 이상", 32, 26, 690, 42, 23, FontStyle.Bold, Ink);
            AddLabel(this, "한 번 설치하고, 다음부터는 바뀐 파일만.", 35, 75, 680, 26, 10, FontStyle.Regular, Muted);
            AddLabel(this, "CAMPUS  /  LAUNCHER", 714, 40, 210, 30, 9, FontStyle.Bold, Color.FromArgb(106, 112, 146)).TextAlign = ContentAlignment.MiddleRight;

            installationTab = Button(this, "설치", 32, 110, 100, 38, Color.FromArgb(226, 231, 247), Ink);
            noticeTab = Button(this, "공지", 144, 110, 100, 38, Color.White, Ink);
            installationTab.Name = "installationTab"; noticeTab.Name = "noticeTab";
            installationTab.AccessibleRole = AccessibleRole.PageTab; noticeTab.AccessibleRole = AccessibleRole.PageTab;
            installationTab.AccessibleName = "설치 탭"; noticeTab.AccessibleName = "공지 탭";
            installationTab.TabIndex = 0; noticeTab.TabIndex = 1;
            installationTab.Click += delegate { SelectPage("install"); };
            noticeTab.Click += delegate { SelectPage("notice"); };
            installationPage = new Panel { Name = "installationPage", Left = 0, Top = 164, Width = 960, Height = 330, BackColor = BackColor, TabIndex = 2 };
            noticePage = new Panel { Name = "noticePage", Left = 0, Top = 164, Width = 960, Height = 330, BackColor = BackColor, TabIndex = 3 };
            Controls.Add(installationPage); Controls.Add(noticePage);

            var location = Card(installationPage, 32, 0, 896, 130);
            AddLabel(location, "게임 설치 위치", 20, 13, 680, 24, 10, FontStyle.Bold, Ink);
            var pathPanel = new Panel { Left = 21, Top = 44, Width = 712, Height = 38, BackColor = Color.FromArgb(246, 248, 252) };
            rootBox = new TextBox { Left = 12, Top = 9, Width = 688, Height = 24, BorderStyle = BorderStyle.None, Font = new Font("맑은 고딕", 10), BackColor = pathPanel.BackColor, ForeColor = Ink, Text = Program.DefaultRoot() };
            rootBox.Leave += delegate { RefreshInstalled(); }; pathPanel.Controls.Add(rootBox); location.Controls.Add(pathPanel);
            browseButton = Button(location, "폴더 선택", 746, 43, 128, 40, Color.White, Ink);
            browseButton.Click += delegate
            {
                using (var dialog = new FolderBrowserDialog { Description = "게임과 런처를 둘 설치 폴더를 선택해 주세요.", SelectedPath = rootBox.Text, ShowNewFolderButton = true })
                    if (dialog.ShowDialog(this) == DialogResult.OK) { rootBox.Text = dialog.SelectedPath; RefreshInstalled(); }
            };
            // Offscreen QA uses automaticCheck=false, which deliberately avoids
            // even detecting files in this PC's real source save directory.
            legacyDetected = automaticCheck && SaveMigration.HasCoherentSource(LegacySource);
            legacyCheck = new CheckBox { Left = 21, Top = 93, Width = 850, Height = 24, Font = new Font("맑은 고딕", 9), ForeColor = Muted, BackColor = Color.Transparent, Text = "이 PC의 기존 플레이 기록 가져오기" + (legacyDetected ? "  ·  첫 설치 때만 복사" : "  ·  감지된 기록 없음"), Checked = legacyDetected, Enabled = legacyDetected };
            location.Controls.Add(legacyCheck);

            var current = Card(installationPage, 32, 146, 440, 98); var latest = Card(installationPage, 488, 146, 440, 98);
            AddLabel(current, "내 PC", 20, 13, 350, 22, 9, FontStyle.Bold, Muted);
            installedLabel = AddLabel(current, "미설치", 20, 36, 260, 36, 20, FontStyle.Bold, Ink);
            installedBuild = AddLabel(current, "", 245, 48, 172, 24, 8, FontStyle.Regular, Muted); installedBuild.TextAlign = ContentAlignment.MiddleRight;
            AddLabel(latest, "업데이트 채널", 20, 13, 350, 22, 9, FontStyle.Bold, Muted);
            latestLabel = AddLabel(latest, "확인 전", 20, 36, 260, 36, 20, FontStyle.Bold, Ink);
            latestBuild = AddLabel(latest, "", 245, 48, 172, 24, 8, FontStyle.Regular, Muted); latestBuild.TextAlign = ContentAlignment.MiddleRight;

            AddLabel(installationPage, "처음에는 게임 전체를, 그다음에는 달라진 파일만 받습니다.\n진행 중에도 공지 탭에서 새 소식을 읽을 수 있어요.", 36, 272, 856, 44, 9, FontStyle.Regular, Muted);

            var news = Card(noticePage, 32, 0, 896, 330);
            AddLabel(news, "새 소식", 22, 16, 850, 30, 14, FontStyle.Bold, Ink);
            noticeVersionLabel = AddLabel(news, "업데이트 확인 전", 22, 54, 600, 28, 11, FontStyle.Bold, Ink);
            noticeVersionLabel.Name = "noticeVersionLabel";
            noticeBuildLabel = AddLabel(news, "", 642, 54, 230, 28, 9, FontStyle.Regular, Muted);
            noticeBuildLabel.Name = "noticeBuildLabel"; noticeBuildLabel.TextAlign = ContentAlignment.MiddleRight;
            news.Controls.Add(new Panel { Left = 22, Top = 94, Width = 852, Height = 1, BackColor = Color.FromArgb(228, 232, 242) });
            notes = new TextBox { Name = "releaseNotes", Left = 24, Top = 110, Width = 848, Height = 198, Multiline = true, WordWrap = true, ReadOnly = true, BorderStyle = BorderStyle.None, ScrollBars = ScrollBars.Vertical, Font = new Font("맑은 고딕", 10), BackColor = Color.White, ForeColor = Muted, Text = "업데이트 확인을 누르면 새 버전과 변경 내용을 보여드려요." };
            news.Controls.Add(notes);

            statusLabel = AddLabel(this, "시작할 준비가 되었어요.", 34, 514, 790, 25, 10, FontStyle.Bold, Ink);
            cancelButton = Button(this, "취소", 836, 508, 92, 35, Color.White, Ink); cancelButton.Visible = false;
            cancelButton.Click += delegate { if (cancellation != null) { cancellation.Cancel(); statusLabel.Text = "안전하게 작업을 정리하고 있어요…"; cancelButton.Enabled = false; } };
            progress = new ThinProgress { Left = 34, Top = 550, Width = 892, Height = 8 }; Controls.Add(progress);
            bytesLabel = AddLabel(this, "", 34, 568, 892, 23, 9, FontStyle.Regular, Muted);
            checkButton = Button(this, "업데이트 확인", 32, 608, 180, 54, Color.White, Ink);
            updateButton = Button(this, "설치 · 업데이트", 224, 608, 270, 54, Color.FromArgb(226, 231, 247), Ink);
            playButton = Button(this, "게임 시작", 510, 608, 418, 54, Color.FromArgb(63, 84, 121), Color.White);
            checkButton.TabIndex = 10; updateButton.TabIndex = 11; playButton.TabIndex = 12; cancelButton.TabIndex = 9;
            checkButton.Click += delegate { Run("check"); }; updateButton.Click += delegate { Run("update"); }; playButton.Click += delegate { Run("play"); };
            AddLabel(this, "우리의 다음 이야기를 기다리며  ·  Launcher 1.1", 34, 677, 892, 22, 8, FontStyle.Regular, Muted);
            Shown += delegate { if (this.automaticCheck) Run("check"); };
            FormClosing += delegate(object sender, FormClosingEventArgs e)
            {
                if (worker != null && worker.IsBusy) { e.Cancel = true; closingWhenIdle = true; if (cancellation != null) cancellation.Cancel(); statusLabel.Text = "작업을 정리한 뒤 닫을게요…"; }
            };
            SelectPage("install"); RefreshInstalled();
        }
        static Icon LoadLauncherIcon()
        {
            try
            {
                using (var stream = Assembly.GetExecutingAssembly().GetManifestResourceStream("CampusRomance.LauncherIcon"))
                    if (stream != null)
                        using (var embedded = new Icon(stream)) return (Icon)embedded.Clone();
            }
            catch { /* A missing or invalid cosmetic resource must not block play. */ }
            return (Icon)SystemIcons.Application.Clone();
        }
        internal void SelectPage(string page)
        {
            if (page != "install" && page != "notice") throw new ArgumentException("Unknown launcher page.", "page");
            selectedPage = page;
            bool installing = page == "install";
            installationPage.Visible = installing; noticePage.Visible = !installing;
            installationTab.Fill = installing ? Color.FromArgb(226, 231, 247) : Color.White;
            noticeTab.Fill = installing ? Color.White : Color.FromArgb(226, 231, 247);
            installationTab.AccessibleDescription = (installing ? "선택됨. " : "") + "설치 위치와 버전. Ctrl+1";
            noticeTab.AccessibleDescription = (!installing ? "선택됨. " : "") + "최신 버전과 업데이트 공지. Ctrl+2";
            installationTab.Invalidate(); noticeTab.Invalidate();
            // Controls remain mounted: location, selection, notice scroll and
            // the running worker are deliberately untouched by navigation.
        }
        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            if (keyData == (Keys.Control | Keys.D1)) { SelectPage("install"); installationTab.Focus(); return true; }
            if (keyData == (Keys.Control | Keys.D2)) { SelectPage("notice"); noticeTab.Focus(); return true; }
            if (keyData == (Keys.Control | Keys.Tab) || keyData == (Keys.Control | Keys.Shift | Keys.Tab))
            {
                SelectPage(selectedPage == "install" ? "notice" : "install");
                if (selectedPage == "install") installationTab.Focus(); else noticeTab.Focus();
                return true;
            }
            return base.ProcessCmdKey(ref msg, keyData);
        }
        internal void ApplyReleaseReport(UpdateReport result)
        {
            if (result == null) throw new ArgumentNullException("result");
            latestLabel.Text = result.version;
            latestBuild.Text = "build " + result.latest_build;
            noticeVersionLabel.Text = result.version;
            noticeBuildLabel.Text = "build " + result.latest_build;
            string[] releaseNotes = result.release_notes ?? new string[0];
            notes.Text = releaseNotes.Length == 0 ? "이번 버전에 등록된 공지가 없습니다." : String.Join(Environment.NewLine + Environment.NewLine, releaseNotes);
        }
        SoftPanel Card(Control parent, int x, int y, int w, int h)
        {
            var panel = new SoftPanel { Left = x, Top = y, Width = w, Height = h }; parent.Controls.Add(panel); return panel;
        }
        static Label AddLabel(Control parent, string text, int x, int y, int w, int h, float size, FontStyle style, Color color)
        {
            var label = new Label { Text = text, Left = x, Top = y, Width = w, Height = h, Font = new Font("맑은 고딕", size, style), ForeColor = color, BackColor = Color.Transparent, TextAlign = ContentAlignment.MiddleLeft, AutoEllipsis = true };
            parent.Controls.Add(label); return label;
        }
        static CalmButton Button(Control parent, string text, int x, int y, int w, int h, Color fill, Color ink)
        {
            var surface = parent as SoftPanel;
            var button = new CalmButton { Text = text, Left = x, Top = y, Width = w, Height = h, Fill = fill, Ink = ink, BackColor = surface == null ? parent.BackColor : surface.Fill }; parent.Controls.Add(button); return button;
        }
        void RefreshInstalled()
        {
            try
            {
                var state = new UpdateEngine(Program.ProductionOptions(rootBox.Text.Trim())).InspectInstalled();
                installedLabel.Text = state == null ? "미설치" : state.version;
                installedBuild.Text = state == null ? "" : "build " + state.build;
                playButton.Enabled = state != null;
                updateButton.Text = state == null ? "게임 설치" : "설치 · 업데이트";
                legacyCheck.Enabled = state == null && legacyDetected;
                if (state != null) legacyCheck.Checked = false;
            }
            catch (Exception ex)
            {
                installedLabel.Text = "확인 필요"; installedBuild.Text = ""; playButton.Enabled = false;
                statusLabel.Text = ex.Message;
            }
        }
        void Busy(bool busy)
        {
            checkButton.Enabled = !busy; updateButton.Enabled = !busy; browseButton.Enabled = !busy; rootBox.Enabled = !busy;
            legacyCheck.Enabled = !busy && legacyDetected && installedLabel.Text == "미설치";
            playButton.Enabled = !busy && installedLabel.Text != "미설치" && installedLabel.Text != "확인 필요";
            cancelButton.Visible = busy; cancelButton.Enabled = busy;
        }
        void Run(string command)
        {
            if (worker != null && worker.IsBusy) return;
            EngineOptions options;
            try { options = Program.ProductionOptions(rootBox.Text.Trim()); new UpdateEngine(options); }
            catch (Exception ex) { statusLabel.Text = ex.Message; return; }
            cancellation = new CancellationTokenSource(); options.Cancellation = cancellation.Token;
            bool importExisting = command == "update" && legacyCheck.Enabled && legacyCheck.Checked;
            worker = new BackgroundWorker { WorkerReportsProgress = true };
            lastProgress = DateTime.MinValue;
            options.Progress = delegate(ProgressInfo info)
            {
                if ((DateTime.UtcNow - lastProgress).TotalMilliseconds < 80 && info.phase != "완료") return;
                lastProgress = DateTime.UtcNow; worker.ReportProgress(0, info);
            };
            worker.ProgressChanged += delegate(object sender, ProgressChangedEventArgs e)
            {
                var info = e.UserState as ProgressInfo; if (info == null) return;
                statusLabel.ForeColor = Ink; statusLabel.Text = info.phase + (String.IsNullOrEmpty(info.file) ? "…" : " · " + Path.GetFileName(info.file));
                progress.Value = info.total > 0 ? (double)info.bytes / info.total : 0; progress.Invalidate();
                bytesLabel.Text = info.phase == "변경된 파일 다운로드" ? FormatBytes(info.bytes) + " / " + FormatBytes(info.total) : "";
            };
            worker.DoWork += delegate(object sender, DoWorkEventArgs e)
            {
                var engine = new UpdateEngine(options);
                if (command == "check") e.Result = engine.Check();
                else if (command == "update")
                {
                    var result = engine.Update();
                    if (result.first_install && importExisting)
                    {
                        try { result.message += " " + SaveMigration.ImportIfEmpty(LegacySource, Path.Combine(SafePaths.CanonicalRoot(options.Root), "Game", "saves")).Message; }
                        catch (Exception ex) { result.message += " 기존 기록 가져오기는 완료하지 못했어요: " + ex.Message; }
                    }
                    e.Result = result;
                }
                else e.Result = engine.Play();
            };
            worker.RunWorkerCompleted += delegate(object sender, RunWorkerCompletedEventArgs e)
            {
                Busy(false);
                if (e.Error != null)
                {
                    statusLabel.ForeColor = Color.FromArgb(150, 66, 80);
                    statusLabel.Text = e.Error is OperationCanceledException ? "작업을 취소했습니다. 기존 게임은 그대로예요." : e.Error.Message;
                    bytesLabel.Text = "다시 시도해도 검증된 다운로드 조각은 이어서 사용합니다.";
                }
                else
                {
                    var result = (UpdateReport)e.Result;
                    if (command != "play") ApplyReleaseReport(result);
                    statusLabel.ForeColor = Ink; statusLabel.Text = result.message;
                    if (command == "update")
                    {
                        progress.Value = 1; progress.Invalidate();
                        bytesLabel.Text = "받은 데이터 " + FormatBytes(result.downloaded_bytes) + " · 변경된 파일 " + result.changed_files.Count + "개";
                        if (result.first_install)
                        {
                            try { InstallLauncher(rootBox.Text.Trim()); }
                            catch (Exception ex) { bytesLabel.Text = "게임 설치 완료 · 런처 바로가기 생성은 완료하지 못했어요: " + ex.Message; }
                        }
                    }
                    RefreshInstalled();
                }
                cancellation.Dispose(); cancellation = null;
                if (closingWhenIdle) Close();
            };
            Busy(true); statusLabel.ForeColor = Ink; statusLabel.Text = command == "play" ? "게임 실행을 준비하고 있어요…" : "업데이트 채널을 확인하고 있어요…";
            progress.Value = 0; progress.Invalidate(); bytesLabel.Text = ""; worker.RunWorkerAsync();
        }
        public static string FormatBytes(long value)
        {
            if (value >= 1024L * 1024 * 1024) return ((double)value / (1024L * 1024 * 1024)).ToString("0.00") + " GB";
            if (value >= 1024L * 1024) return ((double)value / (1024L * 1024)).ToString("0.0") + " MB";
            if (value >= 1024) return ((double)value / 1024).ToString("0.0") + " KB";
            return value + " B";
        }
        static void InstallLauncher(string selectedRoot)
        {
            // Called only after a real GUI first install. CLI/QA never reaches it.
            string root = SafePaths.CanonicalRoot(selectedRoot);
            string target = SafePaths.Within(root, "CampusRomanceLauncher.exe");
            string current = Application.ExecutablePath;
            if (!String.Equals(Path.GetFullPath(current), target, StringComparison.OrdinalIgnoreCase))
            {
                if (!File.Exists(target)) File.Copy(current, target, false);
                else if (UpdateEngine.HashBytes(File.ReadAllBytes(target)) != UpdateEngine.HashBytes(File.ReadAllBytes(current)))
                    throw new IOException("같은 이름의 다른 런처가 있어 덮어쓰지 않았습니다. 현재 받은 런처를 계속 사용할 수 있어요.");
            }
            if (!File.Exists(target)) throw new IOException("설치된 런처를 찾을 수 없습니다.");
            string desktop = Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory);
            string shortcut = Path.Combine(desktop, "우리 사이, 그 이상 런처.lnk");
            object shell = null, link = null;
            try
            {
                Type type = Type.GetTypeFromProgID("WScript.Shell", true); shell = Activator.CreateInstance(type);
                if (File.Exists(shortcut))
                {
                    object old = type.InvokeMember("CreateShortcut", BindingFlags.InvokeMethod, null, shell, new object[] { shortcut });
                    string oldTarget = (string)old.GetType().InvokeMember("TargetPath", BindingFlags.GetProperty, null, old, null);
                    Marshal.FinalReleaseComObject(old);
                    if (String.Equals(oldTarget, target, StringComparison.OrdinalIgnoreCase)) return;
                    int suffix = 2;
                    do { shortcut = Path.Combine(desktop, "우리 사이, 그 이상 런처 (" + suffix++ + ").lnk"); } while (File.Exists(shortcut));
                }
                link = type.InvokeMember("CreateShortcut", BindingFlags.InvokeMethod, null, shell, new object[] { shortcut });
                Type linkType = link.GetType();
                linkType.InvokeMember("TargetPath", BindingFlags.SetProperty, null, link, new object[] { target });
                linkType.InvokeMember("WorkingDirectory", BindingFlags.SetProperty, null, link, new object[] { root });
                linkType.InvokeMember("Description", BindingFlags.SetProperty, null, link, new object[] { "우리 사이, 그 이상 · 업데이트 및 게임 시작" });
                linkType.InvokeMember("IconLocation", BindingFlags.SetProperty, null, link, new object[] { target + ",0" });
                linkType.InvokeMember("Save", BindingFlags.InvokeMethod, null, link, null);
            }
            finally { if (link != null) Marshal.FinalReleaseComObject(link); if (shell != null) Marshal.FinalReleaseComObject(shell); }
        }
    }
}
