# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

# Load GH_IO.dll
$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
Add-Type -Path $ghioPath

# Load the GHX document
$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile($path)

# Get the root node (it's a property, not a method)
$root = $doc.GetRootNode
Write-Host "Root node: Name=$($root.Name), ItemCount=$($root.ItemCount), ChunkCount=$($root.ChunkCount)"

# Function to traverse chunks and items recursively and look for GH_Item with NickName
function Find-NickNameInChunk {
    param(
        [GH_IO.Serialization.GH_Chunk]$chunk,
        [int]$depth
    )
    $indent = "  " * $depth
    # Process items in this chunk
    for($i=0; $i -lt $chunk.ItemCount; $i++) {
        $item = $chunk.Items[$i]
        # Check if this item is a GH_Item (which has a NickName property)
        if ($item -is [GH_IO.Types.GH_Item]) {
            Write-Host "$indent`tItem[$i]: Name=$($item.Name), NickName=$($item.NickName)"
            if ($item.NickName -eq 'F1_ETAPA1_CONTEXTO_v02') {
                Write-Host "$indent`t>>> FOUND TARGET NICKNAME: $($item.NickName)"
                return $item
            }
        }
    }
    # Process sub-chunks
    for($i=0; $i -lt $chunk.ChunkCount; $i++) {
        $subChunk = $chunk.Chunks[$i]
        $result = Find-NickNameInChunk -chunk $subChunk -depth ($depth+1)
        if ($result) { return $result }
    }
    return $null
}

# Traverse the root node
Write-Host "Searching for NickName 'F1_ETAPA1_CONTEXTO_v02'..."
$found = Find-NickNameInChunk -chunk $root -depth 0
if ($found) {
    Write-Host "SUCCESS: Found the target object."
} else {
    Write-Host "FAILURE: Target object not found."
}

// Also, let's check the Objects property again but with the correct type
Write-Host ""
Write-Host "Objects property count: $($doc.Objects.Count)"
if ($doc.Objects.Count -gt 0) {
    for($i=0; $i -lt $doc.Objects.Count; $i++) {
        $obj = $doc.Objects[$i]
        Write-Host "  Object[$i]: NickName=$($obj.NickName), TypeName=$($obj.GetType().Name)"
    }
} else {
    Write-Host "Objects property is empty"
}