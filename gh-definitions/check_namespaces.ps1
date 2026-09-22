$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Add-Type -Path $ghioPath

$asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
       Where-Object { $_.FullName -like 'GH_IO,*' } |
       Select-Object -First 1

"Assembly: {0}" -f $asm.FullName

$types = $asm.GetTypes()
$namespaces = $types | Select-Object -ExpandProperty Namespace | Get-Unique

"Found {0} namespaces:" -f $namespaces.Count
foreach($ns in $namespaces) {
    $namespaceName = if($ns) { $ns } else { '<null>' }
    $count = ($types | Where-Object { $_.Namespace -eq $ns }).Count
    "{0} ({1} types)" -f $namespaceName, $count
}