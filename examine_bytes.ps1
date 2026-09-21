$path = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
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