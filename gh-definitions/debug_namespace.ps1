# Debug the namespace strings to see what's actually there
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

    $types = $asm.GetTypes()
    Write-Host "Total types: $($types.Length)"

    # Look specifically for types in what should be the Serialization namespace
    Write-Host "`nChecking all types for Serialization namespace:"
    foreach($type in $types) {
        if($type.Namespace) {
            # Write debug info about the namespace
            $ns = $type.Namespace
            Write-Host ("Type: {0}.{1}" -f $ns, $type.Name)

            # Check if it matches our target
            if($ns -eq 'Grasshopper.IO.Serialization') {
                Write-Host ("  --> MATCHES TARGET!")
            } elseif($ns -like '*Serialization*') {
                Write-Host ("  --> CONTAINS 'Serialization'")
            }
        } else {
            Write-Host ("Type: <null>.{$($type.Name)}")
        }
    }

    # Let's also check what the actual namespace strings look like
    Write-Host "`nExamining namespace strings more closely:"
    $serializationTypes = $types | Where-Object { $_.Namespace -like '*Serialization*' }
    foreach($type in $serializationTypes) {
        if($type.Namespace) {
            $ns = $type.Namespace
            Write-Host ("Namespace: '$ns'")
            Write-Host ("  Length: $($ns.Length)")
            Write-Host ("  Chars: [$($ns.ToCharArray() | For-Object { '[{0:X2}]' -f [int]$_} ] -join '')]")

            # Compare with expected
            $expected = 'Grasshopper.IO.Serialization'
            Write-Host ("  Expected: '$expected'")
            Write-Host ("  Expected length: $($expected.Length)")
            Write-Host ("  Are they equal? $($ns -eq $expected)")
        }
    }
} else {
    Write-Host "Could not find GH_IO assembly" -ForegroundColor Red
}