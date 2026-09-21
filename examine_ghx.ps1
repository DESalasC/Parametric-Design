Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"

$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile("D:/Work/PROJECTS/DiseñoParametrico/gh-definitions/F1_CONTEXTO_v11.ghx")

$root = $doc.GetRootNode()
Write-Host "Root node:"
Write-Host ("  Type: {0}" -f $root.GetType().FullName)
Write-Host ("  Name: {0}" -f $root.Name)
Write-Host ("  ItemCount: {0}" -f $root.ItemCount)
Write-Host ("  ChunkCount: {0}" -f $root.ChunkCount)

Write-Host "Items:"
for($i=0; $i -lt $root.ItemCount; $i++) {
    $item = $root.Items[$i]
    Write-Host ("  [{0}] Name: {1}, Type: {2}" -f $i, $item.Name, $item.Type)
}

Write-Host "Chunks:"
for($i=0; $i -lt $root.ChunkCount; $i++) {
    $chunk = $root.Chunks[$i]
    Write-Host ("  [{0}] Name: {1}, Type: {2}" -f $i, $chunk.Name, $chunk.GetType().FullName)

    # If this chunk has items, show them too
    if($chunk.ItemCount -gt 0) {
        Write-Host ("    Items:")
        for($j=0; $j -lt $chunk.ItemCount; $j++) {
            $subItem = $chunk.Items[$j]
            Write-Host ("      [{0}] Name: {1}, Type: {2}" -f $j, $subItem.Name, $subItem.Type)
        }
    }

    # If this chunk has sub-chunks, show them too
    if($chunk.ChunkCount -gt 0) {
        Write-Host ("    Sub-chunks:")
        for($j=0; $j -lt $chunk.ChunkCount; $j++) {
            $subChunk = $chunk.Chunks[$j]
            Write-Host ("      [{0}] Name: {1}, Type: {2}" -f $j, $subChunk.Name, $subChunk.GetType().FullName)
        }
    }
}

# Now let's look for objects directly
Write-Host ""
Write-Host "Direct Objects collection:"
$objects = $doc.Objects
Write-Host ("Found {0} objects:" -f $objects.Count)
for($i=0; $i -lt $objects.Count; $i++) {
    $obj = $objects[$i]
    Write-Host ("  [{0}] NickName: {1}, TypeName: {2}" -f $i, $obj.NickName, $obj.TypeName)
}