# Check all loaded assemblies to see what GH_IO assemblies we have
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading GH_IO.dll from: $ghioPath"

try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."
} catch {
    Write-Host "Failed to load GH.IO.dll: $_" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll loaded assemblies containing 'GH_IO':"
$assemblies = [System.AppDomain]::CurrentDomain.GetAssemblies() |
              Where-Object { $_.FullName -like 'GH_IO,*' }

if($assemblies) {
    foreach($asm in $assemblies) {
        Write-Host "  $($asm.FullName)"
        Write-Host "    Location: $($asm.Location)"

        # Check serialization types in this assembly
        $serializationTypes = $asm.GetTypes() | Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' }
        Write-Host "    Serialization types: $($serializationTypes.Length)"
        if($serializationTypes.Length -gt 0) {
            foreach($t in $serializationTypes) {
                Write-Host "      $($t.Name)"
            }
        }
        Write-Host ""
    }
} else {
    Write-Host "  No GH_IO assemblies found"
}