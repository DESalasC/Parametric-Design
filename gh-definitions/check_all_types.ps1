# Load GH_IO.dll and check all types and namespaces
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

    # Get all types grouped by namespace
    $types = $asm.GetTypes()
    $groups = $types | Group-Object Namespace

    Write-Host ("Found {0} namespaces with types:" -f $groups.Count)
    foreach($group in $groups) {
        $namespaceName = if($group.Name) { $group.Name } else { '<null>' }
        Write-Host "Namespace: {0} ({1} types)" -f $namespaceName, $group.Count
        # Show first few types in each namespace
        $count = 0
        foreach($type in $group.Group) {
            if($count -lt 10) {  # Show first 10 types
                Write-Host "  {0}" -f $type.Name
                $count++
            }
        }
        if($group.Count -gt 10) {
            Write-Host "  ... and {0} more" -f ($group.Count - 10)
        }
    }

    # Specifically look for any type containing "Archive" in the name
    $archiveTypes = $types | Where-Object { $_.Name -like '*Archive*' }
    Write-Host ("Found {0} types with 'Archive' in name:" -f $archiveTypes.Length)
    foreach($type in $archiveTypes) {
        Write-Host "  {0}.{1}" -f $type.Namespace, $type.Name
    }

} else {
    Write-Host "Could not find GH_IO assembly"
}