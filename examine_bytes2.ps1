# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

$bytes = [System.IO.File]::ReadAllBytes($path)
Write-Host ("File size: {0} bytes" -f $bytes.Length)
Write-Host "First 50 bytes:"
for($i=0; $i -lt [Math]::Min(50, $bytes.Length); $i++) {
    Write-Host -NoNewline ("{0:X2} " -f $bytes[$i])
    if (($i + 1) % 10 -eq 0) { Write-Host "" }
}
Write-Host ""
Write-Host "Last 50 bytes:"
$start = [Math]::Max(0, $bytes.Length - 50)
for($i=$start; $i -lt $bytes.Length; $i++) {
    Write-Host -NoNewline ("{0:X2} " -f $bytes[$i])
    if (($i + 1) % 10 -eq 0) { Write-Host "" }
}
Write-Host ""

# Try to interpret as text
Write-Host "First 200 characters as text:"
$text = [System.Text.Encoding]::UTF8.GetString($bytes, 0, [Math]::Min(200, $bytes.Length))
Write-Host $text