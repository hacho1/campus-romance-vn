param([switch]$CliOnly)
$ErrorActionPreference = 'Stop'
$appRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $appRoot 'src'
$output = Join-Path $appRoot 'build'
$compiler = 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$key = Join-Path $appRoot 'config\update_public_key.xml'
if (-not (Test-Path -LiteralPath $key)) { throw 'Pinned update public key is missing.' }
New-Item -ItemType Directory -Path $output -Force | Out-Null
$references = @('/r:System.dll','/r:System.Core.dll','/r:System.Drawing.dll','/r:System.Windows.Forms.dll','/r:System.Web.Extensions.dll')
$resources = @('/resource:' + $key + ',CampusRomance.UpdatePublicKey')
$feed = Join-Path $appRoot 'config\feed_config.json'
if (Test-Path -LiteralPath $feed) { $resources += '/resource:' + $feed + ',CampusRomance.FeedConfig' }
$common = @((Join-Path $source 'UpdateModels.cs'),(Join-Path $source 'SafePaths.cs'),(Join-Path $source 'UpdateEngine.cs'),(Join-Path $source 'Program.cs'))
& $compiler /nologo /optimize+ /target:exe /define:CLI ('/out:' + (Join-Path $output 'CampusRomanceUpdater.Cli.exe')) @references @resources @common
if ($LASTEXITCODE -ne 0) { throw 'CLI build failed.' }
if (-not $CliOnly) {
    $icon = Join-Path $appRoot 'assets\launcher.ico'
    if (-not (Test-Path -LiteralPath $icon)) { throw 'Launcher icon is missing. Run scripts/build_icon.ps1 first.' }
    $guiResources = @('/resource:' + $icon + ',CampusRomance.LauncherIcon')
    $gui = @((Join-Path $source 'LauncherForm.cs'),(Join-Path $source 'SaveMigration.cs'))
    & $compiler /nologo /optimize+ /target:winexe ('/win32icon:' + $icon) ('/out:' + (Join-Path $output 'CampusRomanceLauncher.exe')) @references @resources @guiResources @common @gui
    if ($LASTEXITCODE -ne 0) { throw 'GUI launcher build failed.' }
}
Get-ChildItem -LiteralPath $output -Filter '*.exe' | Select-Object Name,Length
