# Debug script to check assembly loading and type creation
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading GH_IO.dll from: $ghioPath"

try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."
} catch {
    Write-Host "Failed to load GH_IO.dll: $_" -ForegroundColor Red
    exit 1
}

# Check what types are actually available
$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

if($asm) {
    Write-Host "Assembly: $($asm.FullName)"
    $types = $asm.GetTypes()
    Write-Host ("Total types: {0}" -f $types.Length)

    # Group by namespace
    $groups = $types | Group-Object Namespace
    foreach($group in $groups) {
        $namespaceName = if($group.Name) { $group.Name } else { '<null>' }
        Write-Host ("Namespace: {0} ({1} types)" -f $namespaceName, $group.Count)
        # Show first few types in each namespace
        $count = 0
        foreach($type in $group.Group) {
            if($count -lt 5) {
                Write-Host ("  {0}" -f $type.Name)
                $count++
            }
        }
        if($group.Count -gt 5) {
            Write-Host ("  ... and {0} more" -f ($group.Count - 5))
        }
    }
} else {
    Write-Host "Could not find GH_IO assembly"
}