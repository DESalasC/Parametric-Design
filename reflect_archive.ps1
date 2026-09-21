Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
$doc = New-Object GH_IO.Serialization.GH_Archive
Write-Host "Properties of GH_Archive:"
$doc.GetType().GetProperties() | ForEach-Object {
    Write-Host "$($_.Name) : $($_.PropertyType)"
}
Write-Host "`nMethods of GH_Archive (selected):"
$doc.GetType().GetMethods() | Where-Object { $_.Name -like '*Object*' -or $_.Name -like '*Extract*' } | ForEach-Object {
    Write-Host "$($_.Name)"
}