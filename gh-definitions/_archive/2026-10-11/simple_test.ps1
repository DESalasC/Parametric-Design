# Simple test to verify we can access GH_Archive type
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading GH_IO.dll from: $ghioPath"

try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."
} catch {
    Write-Host "Failed to load GH.IO.dll: $_" -ForegroundColor Red
    exit 1
}

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

if($asm) {
    Write-Host "Assembly: $($asm.FullName)"

    $type = $asm.GetType("Grasshopper.IO.Serialization.GH_Archive")
    if($type) {
        Write-Host "SUCCESS: Found GH_Archive type: $($type.FullName)"

        # Try to create an instance
        try {
            $obj = $type.GetConstructor(@()).Invoke(@($null))
            Write-Host "SUCCESS: Created GH_Archive instance"
            $obj.Dispose()
        } catch {
            Write-Host "Error creating instance: $($_.Exception.Message)" -ForegroundColor Red
        }
    } else {
        Write-Host "ERROR: Could not find GH_Archive type" -ForegroundColor Red

        # Let's see what Serialization types we have
        $serializationTypes = $asm.GetTypes() | Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' }
        Write-Host "Serialization types found: $($serializationTypes.Length)"
        foreach($t in $serializationTypes) {
            Write-Host "  $($t.Name)"
        }
    }
} else {
    Write-Host "Could not find GH_IO assembly" -ForegroundColor Red
}