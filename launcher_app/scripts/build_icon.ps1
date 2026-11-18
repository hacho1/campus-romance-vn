param(
    [string]$SourcePng = 'D:\CampusRomance_VN\launcher_app\assets\launcher-source.png'
)
$ErrorActionPreference = 'Stop'
$appRoot = Split-Path -Parent $PSScriptRoot
$assetRoot = Join-Path $appRoot 'assets'
New-Item -ItemType Directory -Path $assetRoot -Force | Out-Null
$iconBuilderSource = @'
using System;
using System.IO;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
public static class CampusLauncherIconBuilder {
    public static int Main(string[] args) {
        if (args.Length != 2) return 2;
        Build(args[0], args[1]); return 0;
    }
    public static void Build(string source, string output) {
        int[] sizes = {16,24,32,48,64,128,256};
        var payloads = new byte[sizes.Length][];
        int payloadIndex = 0;
        using (var original = new Bitmap(source)) {
            if (original.Width != original.Height) throw new InvalidDataException("A square original icon is required.");
            foreach (int size in sizes) {
                using (var scaled = new Bitmap(size, size, PixelFormat.Format32bppArgb)) {
                    using (var graphics = Graphics.FromImage(scaled)) {
                        graphics.InterpolationMode = InterpolationMode.HighQualityBicubic;
                        graphics.PixelOffsetMode = PixelOffsetMode.HighQuality;
                        graphics.CompositingQuality = CompositingQuality.HighQuality;
                        graphics.DrawImage(original, new Rectangle(0,0,size,size));
                    }
                    using (var bytes = new MemoryStream()) {
                        if (size >= 128) scaled.Save(bytes, ImageFormat.Png);
                        else using (var writer = new BinaryWriter(bytes, System.Text.Encoding.UTF8, true)) {
                            int maskStride = ((size + 31) / 32) * 4;
                            writer.Write(40); writer.Write(size); writer.Write(size * 2);
                            writer.Write((short)1); writer.Write((short)32); writer.Write(0);
                            writer.Write(size * size * 4 + maskStride * size);
                            writer.Write(0); writer.Write(0); writer.Write(0); writer.Write(0);
                            for (int y=size-1; y>=0; y--) for (int x=0; x<size; x++) {
                                var pixel=scaled.GetPixel(x,y);
                                writer.Write(pixel.B); writer.Write(pixel.G); writer.Write(pixel.R); writer.Write(pixel.A);
                            }
                            writer.Write(new byte[maskStride * size]);
                        }
                        payloads[payloadIndex++] = bytes.ToArray();
                    }
                }
            }
        }
        using (var stream=File.Create(output)) using (var writer=new BinaryWriter(stream)) {
            writer.Write((short)0); writer.Write((short)1); writer.Write((short)sizes.Length);
            int offset=6+16*sizes.Length;
            for(int index=0;index<sizes.Length;index++) {
                writer.Write((byte)(sizes[index]==256 ? 0 : sizes[index]));
                writer.Write((byte)(sizes[index]==256 ? 0 : sizes[index]));
                writer.Write((byte)0); writer.Write((byte)0); writer.Write((short)1); writer.Write((short)32);
                writer.Write(payloads[index].Length); writer.Write(offset); offset+=payloads[index].Length;
            }
            foreach(var payload in payloads) writer.Write(payload);
        }
    }
}
'@
$target = Join-Path $assetRoot 'launcher.ico'
$buildRoot = Join-Path $appRoot 'build'
New-Item -ItemType Directory -Path $buildRoot -Force | Out-Null
$builderSourcePath = Join-Path $buildRoot 'IconBuilder.cs'
$builderExePath = Join-Path $buildRoot 'IconBuilder.exe'
[IO.File]::WriteAllText($builderSourcePath, $iconBuilderSource, [Text.UTF8Encoding]::new($false))
& 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe' /nologo /target:exe /r:System.Drawing.dll ('/out:' + $builderExePath) $builderSourcePath
if ($LASTEXITCODE -ne 0) { throw 'Icon format converter compilation failed.' }
& $builderExePath $SourcePng $target
if ($LASTEXITCODE -ne 0) { throw 'Icon format conversion failed.' }
[ordered]@{
    source = $SourcePng
    source_sha256 = (Get-FileHash -LiteralPath $SourcePng -Algorithm SHA256).Hash.ToLowerInvariant()
    icon = $target
    sizes = @(16,24,32,48,64,128,256)
    icon_sha256 = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
    policy = 'Original supplied artwork preserved. Only icon format conversion and uniform scaling.'
} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $assetRoot 'icon_manifest.json') -Encoding utf8
Get-Item -LiteralPath $target | Select-Object FullName, Length
