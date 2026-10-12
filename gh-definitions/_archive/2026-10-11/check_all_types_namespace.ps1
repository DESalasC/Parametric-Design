$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Add-Type -Path $ghioPath

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

"Assembly: {0}" -f $asm.FullName

$types = $asm.GetTypes()
"Total types: {0}" -f $types.Count

# List all types with their full names
foreach($type in $types) {
    "{0}.{1}" -f $type.Namespace, $type.Name
}