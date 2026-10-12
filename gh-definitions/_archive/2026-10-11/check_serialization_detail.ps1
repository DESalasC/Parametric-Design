$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Add-Type -Path $ghioPath

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

"Assembly: {0}" -f $asm.FullName

$serializationTypes = $asm.GetTypes() | Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' } | Sort-Object Name

"Found {0} serialization types:" -f $serializationTypes.Count
foreach($type in $serializationTypes) {
    "{0}" -f $type.Name
}