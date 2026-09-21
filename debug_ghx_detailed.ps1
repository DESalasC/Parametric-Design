# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

# Load GH_IO.dll
$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
try {
    Add-Type -Path $ghioPath
    Write-Host "Successfully loaded GH_IO.dll"
} catch {
    Write-Error "Failed to load GH_IO.dll: $_"
    exit 1
}

# Load the GHX document
try {
    $doc = New-Object GH_IO.Serialization.GH_Archive
    $doc.ReadFromFile($path)
    Write-Host "Successfully loaded GHX file"
} catch {
    Write-Error "Failed to load GHX document: $_"
    exit 1
}

# Get the root node (it's a property, not a method)
try {
    $root = $doc.GetRootNode
    Write-Host ("Root node type: {0}" -f $root.GetType().FullName)
    Write-Host ("Root node name: {0}" -f $root.Name)
    Write-Host ("Root node item count: {0}" -f $root.ItemCount)
    Write-Host ("Root node chunk count: {0}" -f $root.ChunkCount)
} catch {
    Write-Error "Failed to get root node: $_"
    exit 1
}

# Function to traverse chunks and items recursively
function TraverseChunk {
    param(
        [GH_IO.Serialization.GH_Chunk]$chunk,
        [int]$depth
    )
    $indent = "  " * $depth
    Write-Host ("{0}Chunk: Name='{1}', ItemCount={2}, ChunkCount={3}" -f $indent, $chunk.Name, $chunk.ItemCount, $chunk.ChunkCount)
    # Process items in this chunk
    for($i=0; $i -lt $chunk.ItemCount; $i++) {
        $item = $chunk.Items[$i]
        Write-Host ("{0}  Item[{1}]: Name='{2}', Type='{3}'" -f $indent, $i, $item.Name, $item.Type)
        # Check if this item has a NickName property (it might be a GH_Object)
        if ($item -is [GH_IO.GH_Object]) {
            Write-Host ("{0}    NickName: '{1}'" -f $indent, $item.NickName)
        }
    }
    # Process sub-chunks
    for($i=0; $i -lt $chunk.ChunkCount; $i++) {
        $subChunk = $chunk.Chunks[$i]
        TraverseChunk -chunk $subChunk -depth ($depth+1)
    }
}

# Traverse the root node
Write-Host "Traversing root node:"
TraverseChunk -chunk $root -depth 0

# Also, let's try to use the Objects property and see what it says
Write-Host ""
Write-Host ("Objects property count: {0}" -f $doc.Objects.Count)
if ($doc.Objects.Count -gt 0) {
    for($i=0; $i -lt $doc.Objects.Count; $i++) {
        $obj = $doc.Objects[$i]
        Write-Host ("  Object[{0}]: NickName='{1}', TypeName='{2}'" -f $i, $obj.NickName, $obj.TypeName)
    }
} else {
    Write-Host "Objects property is empty"
}