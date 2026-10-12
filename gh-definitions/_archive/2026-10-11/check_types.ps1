# Load GH_IO.dll and list all types to find the correct one
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading GH_IO.dll from: $ghioPath"

try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."

    # Get the assembly
    $asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
           Where-Object { $_.FullName -like 'GH_IO,*' } |
           Select-Object -First 1

    if($asm) {
        Write-Host "Found assembly: $($asm.FullName)"

        # List all types
        $types = $asm.GetTypes()
        Write-Host "Found $($types.Length) types"

        # Look for archive-related types
        $archiveTypes = $types | Where-Object { $_.Name -like '*Archive*' }
        Write-Host "Found $($archiveTypes.Length) archive-related types:"
        foreach($type in $archiveTypes) {
            Write-Host "  $($type.Namespace).$($type.Name)"
        }

        # Look for GH_Archive specifically
        $ghArchive = $types | Where-Object { $_.Name -eq 'GH_Archive' }
        if($ghArchive) {
            Write-Host "Found GH_Archive: $($ghArchive.Namespace).$($ghArchive.Name)"
        } else {
            Write-Host "GH_Archive not found by exact name"
        }

    } else {
        Write-Host "Could not find GH_IO assembly"
    }

} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}