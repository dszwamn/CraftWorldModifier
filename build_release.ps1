[CmdletBinding()]
param(
    [string]$Python = "python"
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workPath = Join-Path $projectRoot 'pyinstaller-work'
$distPath = Join-Path $projectRoot 'pyinstaller-dist'
$specPath = Join-Path $projectRoot 'pyinstaller-spec'
$releasePath = Join-Path $projectRoot '发布包'

& $Python -m PyInstaller --version | Out-Null

& $Python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name 'CraftWorldModifier' `
    --icon (Join-Path $projectRoot 'app_icon.ico') `
    --add-data ((Join-Path $projectRoot 'ui_v1.0.html') + ';resources') `
    --add-data ((Join-Path $projectRoot 'block_data.py') + ';resources') `
    --add-data ((Join-Path $projectRoot 'item_translations.txt') + ';resources') `
    --add-data ((Join-Path $projectRoot 'config\marks.json') + ';resources\config') `
    --workpath $workPath `
    --distpath $distPath `
    --specpath $specPath `
    (Join-Path $projectRoot 'craft_web_v1.0.py')

$builtExe = Join-Path $distPath 'CraftWorldModifier.exe'
if (-not (Test-Path -LiteralPath $builtExe)) {
    throw "构建没有生成 CraftWorldModifier.exe"
}

New-Item -ItemType Directory -Force -Path $releasePath | Out-Null
Copy-Item -LiteralPath $builtExe -Destination (Join-Path $releasePath 'CraftWorldModifier.exe') -Force
Get-FileHash -LiteralPath (Join-Path $releasePath 'CraftWorldModifier.exe') -Algorithm SHA256 |
    Select-Object Algorithm, Hash, Path
