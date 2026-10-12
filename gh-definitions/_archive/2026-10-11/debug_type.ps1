$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Add-Type -Path $ghioPath

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

$asm.FullName

$types = $asm.GetType("Grasshopper.IO.Serialization.GH_Archive")
if($types) {
    "Type found: {0}" -f $types.FullName
} else {
    "Type NOT found"

    # Let's see what serialization types we HAVE got
    $serializationTypes = $asm.GetTypes() | Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' }
    foreach($t in $serializationTypes) {
        "Serialization type: {0}" -f $t.FullName
    }
}