$asm = [System.Reflection.Assembly]::LoadFrom('C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll')
$t = $asm.GetType('GH_Archive')
if ($t) {
    Write-Host "GH_Archive found"
    Write-Host "Constructors:"
    $t.GetConstructors() | ForEach-Object { Write-Host $_.ToString() }
    Write-Host "`nMethods (public instance):"
    $t.GetMethods([System.Reflection.BindingFlags]'Instance,Public') | Where-Object { $_.Name -match 'FromXml|CreateArchive|Load|Open|Save|Write' } | ForEach-Object { Write-Host $_.ToString() }
    Write-Host "`nProperties:"
    $t.GetProperties([System.Reflection.BindingFlags]'Instance,Public') | ForEach-Object { Write-Host $_.ToString() }
} else {
    Write-Host "GH_Archive not found"
}