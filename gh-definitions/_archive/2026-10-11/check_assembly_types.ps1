# Check what types are actually in the loaded GH_IO assembly
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
    Write-Host "Location: $($asm.Location)"

    $types = $asm.GetTypes()
    Write-Host "Total types in assembly: $($types.Length)"

    # Group by namespace and show counts
    $groups = $types | Group-Object Namespace
    foreach($group in $groups) {
        $ns = if($group.Name) { $group.Name } else { '<null>' }
        Write-Host "Namespace '$ns': $($group.Count) types"

        # Show first few types in each namespace
        $shown = 0
        foreach($type in $group.Group) {
            if($shown -lt 5) {
                Write-Host "  $($type.Name)"
                $shown++
            }
        }
        if($group.Count -gt 5) {
            Write-Host "  ... and $($group.Count - 5) more"
        }
        Write-Host ""
    }

    # Specifically look for serialization and archive types
    Write-Host "Serialization namespace types:"
    $serializationTypes = $types | Where-Object { $_.Namespace -eq 'Grasshopper.IO.Serialization' }
    if($serializationTypes.Length -gt 0) {
        foreach($t in $serializationTypes) {
            Write-Host "  $($t.Name)"
        }
    } else {
        Write-Host "  None found"
    }

    Write-Host ""
    Write-Host "Types with 'Archive' in name:"
    $archiveTypes = $types | Where-Object { $_.Name -like '*Archive*' }
    if($archiveTypes.Length -gt 0) {
        foreach($t in $archiveTypes) {
            Write-Host "  $($t.Namespace).$($t.Name)"
        }
    } else {
        Write-Host "  None found"
    }

} else {
    Write-Host "Could not find GH_IO assembly" -ForegroundColor Red
}