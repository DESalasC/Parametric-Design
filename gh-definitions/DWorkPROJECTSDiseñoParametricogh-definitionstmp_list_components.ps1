Add-Type -Path 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
$doc = New-Object GH_IO.Document.GH_Document
$doc.Load('D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx')
$objects = $doc.AllObjects($true)
foreach ($obj in $objects) {
    if ($obj.TypeName -like '*Python*') {
        Write-Output ("NickName: {0}, TypeName: {1}" -f $obj.NickName, $obj.TypeName)
    }
}
