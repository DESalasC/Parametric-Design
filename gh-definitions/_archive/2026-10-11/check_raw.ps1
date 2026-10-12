$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

$content = Get-Content -Path $path -Raw
if ($content -like "*CodeInput*") {
    Write-Host "File contains the string CodeInput"
    # Find the position
    $pos = $content.IndexOf("CodeInput")
    Write-Host ("First occurrence at position: {0}" -f $pos)
    $start = [Math]::Max(0, $pos - 50)
    $end = [Math]::Min($content.Length, $pos + 50)
    Write-Host ("Context: {0}" -f $content.Substring($start, $end - $start))
} else {
    Write-Host "File does NOT contain the string CodeInput"
}