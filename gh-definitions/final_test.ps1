# Final test with correct namespace
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

    # Try with the correct namespace
    $typeName = "GH_IO.Serialization.GH_Archive"
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
    }
} else {
    Write-Host "Could not find GH_IO assembly" -ForegroundColor Red
}