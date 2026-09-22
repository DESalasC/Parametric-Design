# Test loading the assembly and checking available types
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading assembly from: $ghioPath"

try {
    $asm = [System.Reflection.Assembly]::LoadFrom($ghioPath)
    Write-Host "Assembly loaded: $($asm.FullName)"

    # List all types in the assembly
    $types = $asm.GetTypes()
    Write-Host "Found $($types.Length) types in assembly"

    # Look for types containing "Archive" in the name
    $archiveTypes = $types | Where-Object { $_.Name -like '*Archive*' }
    Write-Host "Found $($archiveTypes.Length) types with 'Archive' in name:"
    foreach($type in $archiveTypes) {
        Write-Host "  $($type.Namespace).$($type.Name)"
    }

} catch {
    Write-Host "Error loading assembly: $($_.Exception.Message)" -ForegroundColor Red
}