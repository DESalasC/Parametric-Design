$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
Add-Type -Path $ghioPath

$ghxPath = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
Write-Host "Path: $ghxPath"
Write-Host "Test-Path: $(Test-Path $ghxPath)"
try {
    $doc = New-Object GH_IO.Serialization.GH_Archive
    $doc.ReadFromFile($ghxPath)
    Write-Host "Success"
} catch {
    Write-Host "Error: $_"
}
