Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
Write-Host "GH_IO.dll loaded"
$doc = New-Object GH_IO.Serialization.GH_Archive
Write-Host "GH_Archive created"
try {
    $doc.ReadFromFile(".\gh-definitions\F1_CONTEXTO_v11.ghx")
    Write-Host "File loaded successfully"
} catch {
    Write-Host "Error loading file: $($_.Exception.Message)"
    exit 1
}
$objects = $doc.Objects
Write-Host ("Number of objects: {0}" -f $objects.Count)
if ($objects.Count -gt 0) {
    $objects | ForEach-Object { Write-Host "NickName: $($_.NickName)" }
} else {
    Write-Host "No objects found"
}
