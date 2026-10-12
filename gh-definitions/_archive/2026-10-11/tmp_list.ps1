$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
Add-Type -Path $ghioPath

$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile('F1_CONTEXTO_v11.ghx')
$objects = $doc.Objects
foreach ($obj in $objects) {
    if ($obj.TypeName -like '*Python*') {
        Write-Output ('NickName: {0}, TypeName: {1}' -f $obj.NickName, $obj.TypeName)
    }
}
