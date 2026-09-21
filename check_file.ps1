Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"

$path = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
Write-Host "Checking file: $path"
if(Test-Path $path) {
    Write-Host "File exists"
    try {
        $doc = New-Object GH_IO.Serialization.GH_Archive
        $doc.ReadFromFile($path)
        Write-Host "File loaded successfully"
        Write-Host "Objects count: $($doc.Objects.Count)"
        for($i=0; $i -lt $doc.Objects.Count; $i++) {
            $obj = $doc.Objects[$i]
            Write-Host ("  [{0}] NickName: {1}, TypeName: {2}" -f $i, $obj.NickName, $obj.TypeName)
        }
    } catch {
        Write-Host "Error loading file: $($_.Exception.Message)"
    }
} else {
    Write-Host "File does not exist"
}