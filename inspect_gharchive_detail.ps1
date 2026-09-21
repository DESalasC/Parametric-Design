$asm = [System.Reflection.Assembly]::LoadFrom('C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll')
$t = $asm.GetType('GH_IO.Serialization.GH_Archive')
if ($t) {
    Write-Host "Found GH_IO.Serialization.GH_Archive"
    Write-Host "Constructors:"
    $t.GetConstructors() | ForEach-Object { Write-Host $_.ToString() }
    Write-Host "`nMethods (public instance):"
    $t.GetMethods([System.Reflection.BindingFlags]'Instance,Public') | Sort-Object Name | ForEach-Object { Write-Host $_.ToString() }
    Write-Host "`nMethods (public static):"
    $t.GetMethods([System.Reflection.BindingFlags]'Static,Public') | Sort-Object Name | ForEach-Object { Write-Host $_.ToString() }
    Write-Host "`nProperties:"
    $t.GetProperties([System.Reflection.BindingFlags]'Instance,Public') | Sort-Object Name | ForEach-Object { Write-Host $_.ToString() }
} else {
    Write-Host "GH_IO.Serialization.GH_Archive not found"
}