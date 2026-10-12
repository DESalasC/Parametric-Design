$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
Add-Type -Path $ghioPath

$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile('F1_CONTEXTO_v11.ghx')
$objects = $doc.Objects
$count = 0
foreach ($obj in $objects) {
    if ($count -lt 20) {
        Write-Output ('{0}: NickName: {1}, TypeName: {2}' -f $count, $obj.NickName, $obj.TypeName)
        $count++
    }
}
