$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Add-Type -Path $ghioPath

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

Write-Host "Assembly: $($asm.FullName)"

# Get all types
$types = $asm.GetTypes()
Write-Host "Total types: $($types.Length)"

# Let's manually iterate through all types and check their namespaces
Write-Host "`nChecking all types:"
$foundSerialization = $false
foreach($t in $types) {
    $ns = $t.Namespace
    $name = $t.Name
    if($ns -like '*Serialization*') {
        Write-Host ("  {0}.{1}" -f $ns, $name)
        $foundSerialization = $true
    }
    if($name -like '*Archive*') {
        Write-Host ("  [ARCHIVE] {0}.{1}" -f $ns, $name)
    }
}

if(-not $foundSerialization) {
    Write-Host "`nNo types found with Serialization in namespace"
}

# Let's also check what namespaces actually exist
Write-Host "`nAll namespaces:"
$namespaces = $types | Select-Object -ExpandProperty Namespace | Get-Unique
foreach($ns in $namespaces) {
    $nsDisplay = if($ns) { $ns } else { '<null>' }
    Write-Host "  $nsDisplay"
}