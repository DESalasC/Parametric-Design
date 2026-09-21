Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
Write-Host "GH_IO.dll loaded"
$doc = New-Object GH_IO.Serialization.GH_Archive
$path = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
$doc.ReadFromFile($path)
Write-Host "File loaded"
$root = $doc.GetRootNode
Write-Host ("Root: {0}, Items: {1}, Chunks: {2}" -f $root.Name, $root.ItemCount, $root.ChunkCount)