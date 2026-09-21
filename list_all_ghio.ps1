$asm = [System.Reflection.Assembly]::LoadFrom('C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll')
$asm.GetTypes() | Sort-Object Name | ForEach-Object {
    Write-Host ($_.Name)
}