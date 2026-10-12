# Load GH_IO.dll and check Serialization namespace types
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading GH_IO.dll from: $ghioPath"

try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."
} catch {
    Write-Host "Failed to load GH_IO.dll: $_" -ForegroundColor Red
    exit 1
}

# Get the assembly
$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

if($asm) {
    Write-Host "Assembly: $($asm.FullName)"

    # Get Serialization namespace types
    $serializationTypes = $asm.GetTypes() |
                          Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' } |
                          Sort-Object Name

    Write-Host ("Grasshopper.IO.Serialization types ({0}):" -f $serializationTypes.Length)
    foreach($type in $serializationTypes) {
        Write-Host "  {0}" -f $type.Name
    }

    # Check specifically for GH_Archive
    $ghArchiveType = $asm.GetType("Grasshopper.IO.Serialization.GH_Archive")
    if($ghArchiveType) {
        Write-Host "Found GH_Archive type: $($ghArchiveType.FullName)"
    } else {
        Write-Host "GH_Archive type NOT found"
    }

} else {
    Write-Host "Could not find GH_IO assembly"
}