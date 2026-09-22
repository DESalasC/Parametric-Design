# Test accessing GH_Archive type directly
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

    # Try to get the type directly
    $typeName = "Grasshopper.IO.Serialization.GH_Archive"
    Write-Host "Trying to get type: $typeName"

    $type = $asm.GetType($typeName)
    if($type) {
        Write-Host "SUCCESS: Found type $($type.FullName)"

        # Try to create an instance
        try {
            $ctor = $type.GetConstructor(@())
            if($ctor) {
                Write-Host "Found parameterless constructor"
                $instance = $ctor.Invoke(@($null))
                Write-Host "SUCCESS: Created instance of $($type.FullName)"
                $instance.Dispose()
            } else {
                Write-Host "No parameterless constructor found"
            }
        } catch {
            Write-Host "Error creating instance: $($_.Exception.Message)" -ForegroundColor Red
        }
    } else {
        Write-Host "ERROR: Could not find type $typeName" -ForegroundColor Red

        # Let's see what types ARE available in Serialization
        Write-Host "`nChecking Serialization namespace types manually:"
        $serializationTypes = $asm.GetTypes() | Where-Object {
            if($_.Namespace) { $_.Namespace -eq 'Grasshopper.IO.Serialization' } else { $false }
        }
        Write-Host "Found $($serializationTypes.Length) types via manual namespace check:"
        foreach($t in $serializationTypes) {
            Write-Host "  $($t.Name)"
        }

        # Let's also try with exact string comparison
        Write-Host "`nTrying exact string comparison:"
        $exactMatchTypes = $asm.GetTypes() | Where-Object {
            $_.Namespace -eq 'Grasshopper.IO.Serialization'
        }
        Write-Host "Found $($exactMatchTypes.Length) types via exact match:"
        foreach($t in $exactMatchTypes) {
            Write-Host "  $($t.Name)"
        }
    }
} else {
    Write-Host "Could not find GH_IO assembly" -ForegroundColor Red
}