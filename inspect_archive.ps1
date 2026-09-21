$asm = [System.Reflection.Assembly]::LoadFrom('C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll')
$t = $asm.GetType('GH_Archive')
if ($t) {
    Write-Host "Found GH_Archive"
    Write-Host "Methods:"
    $t.GetMethods() | Where-Object { $_.IsPublic } | Select-Object Name, ReturnType | Format-Table -AutoSize | Out-String | Write-Host
    Write-Host "`nProperties:"
    $t.GetProperties() | Where-Object { $_.CanRead } | Select-Object Name, PropertyType | Format-Table -AutoSize | Out-String | Write-Host
} else {
    Write-Host "GH_Archive not found"
}