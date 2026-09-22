$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Add-Type -Path $ghioPath

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

Write-Host "Assembly: $($asm.FullName)"
Write-Host "Assembly Location: $($asm.Location)"

# Get all types and look for our target
$types = $asm.GetTypes()
Write-Host "Total types: $($types.Length)"

# Look for GH_Archive specifically
$matchingTypes = $types | Where-Object { $_.Name -eq 'GH_Archive' -and $_.Namespace -eq 'Grasshopper.IO.Serialization' }
Write-Host "Matching types (GH_Archive in Grasshopper.IO.Serialization): $($matchingTypes.Length)"

if($matchingTypes) {
    foreach($t in $matchingTypes) {
        Write-Host "Found: $($t.FullName)"
        Write-Host "  Assembly: $($t.Assembly.FullName)"
    }
} else {
    Write-Host "No exact match found"

    # Let's see what Serialization types we have
    $serializationTypes = $types | Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' }
    Write-Host "Serialization namespace types: $($serializationTypes.Length)"
    foreach($t in $serializationTypes) {
        Write-Host "  $($t.Name)"
    }

    # Let's see what types have Archive in the name
    $archiveTypes = $types | Where-Object { $_.Name -like '*Archive*' }
    Write-Host "Types with 'Archive' in name: $($archiveTypes.Length)"
    foreach($t in $archiveTypes) {
        Write-Host "  $($t.Namespace).$($t.Name)"
    }
}