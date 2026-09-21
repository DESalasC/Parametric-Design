$asm = [System.Reflection.Assembly]::LoadFrom('C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll')
$types = $asm.GetTypes() | Where-Object { $_.Name -like '*Document*' }
foreach ($t in $types) {
    Write-Host "Name: $($t.Name)"
    Write-Host "FullName: $($t.FullName)"
    Write-Host "---"
}