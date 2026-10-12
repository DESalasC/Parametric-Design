$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
Add-Type -Path $ghioPath

$ghxPath = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile($ghxPath)
$objects = $doc.Objects
Write-Output ("Total objects: {0}" -f $objects.Count)
foreach ($obj in $objects) {
    if ($obj.TypeName -like '*Python*') {
        Write-Output ("Python: NickName: {0}, TypeName: {1}" -f $obj.NickName, $obj.TypeName)
    }
}
