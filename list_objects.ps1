Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"

$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile("D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx")

$objects = $doc.Objects
Write-Host ("Found {0} objects" -f $objects.Count)
for($i=0; $i -lt $objects.Count; $i++) {
    $obj = $objects[$i]
    Write-Host ("  [{0}] NickName: {1}, TypeName: {2}" -f $i, $obj.NickName, $obj.TypeName)
}