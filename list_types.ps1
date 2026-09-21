Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
$asm = [System.Reflection.Assembly]::LoadFrom("C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll")
$types = $asm.GetTypes() | Where-Object { $_.Name -like "*Item*" -or $_.Name -like "*Object*" }
foreach($t in $types) {
    Write-Host $t.FullName
}