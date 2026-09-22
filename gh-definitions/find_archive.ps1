# Find GH_Archive type in GH_IO.dll
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'

try {
    Add-Type -Path $ghioPath
} catch {
    exit 1
}

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

if($asm) {
    $types = $asm.GetTypes()

    # Look for types with Archive in the name
    $archiveTypes = $types | Where-Object { $_.Name -like '*Archive*' }

    foreach($type in $archiveTypes) {
        "{0}.{1}" -f $type.Namespace, $type.Name
    }

    # Specifically check for known GH_Archive locations
    $knownPaths = @(
        'Grasshopper.IO.GH_Archive',
        'Grasshopper.IO.Serialization.GH_Archive'
    )

    foreach($path in $knownPaths) {
        $type = $asm.GetType($path)
        if($type) {
            "FOUND: {0}" -f $path
        }
    }
} else {
    "ASSEMBLY NOT FOUND"
}