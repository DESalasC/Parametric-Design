Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
Write-Host "GH_IO.dll loaded"
$doc = New-Object GH_IO.Serialization.GH_Archive
Write-Host "GH_Archive created"
$backupPath = ".\gh-definitions\F1_CONTEXTO_v11.ghx.bak-2026-09-17-1732"
Write-Host ("Trying backup: {0}" -f $backupPath)
try {
    $doc.ReadFromFile($backupPath)
    Write-Host "Backup file loaded successfully"
} catch {
    Write-Host "Error loading backup file: $($_.Exception.Message)"
    exit 1
}
$objects = $doc.Objects
Write-Host ("Number of objects in backup: {0}" -f $objects.Count)
if ($objects.Count -gt 0) {
    $objects | ForEach-Object { Write-Host "NickName: $($_.NickName)" }
} else {
    Write-Host "No objects found in backup"
}
