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

# Get the root node
$root = $doc.GetRootNode
Write-Host ("Root node: Name='{0}', ItemCount={1}, ChunkCount={2}" -f $root.Name, $root.ItemCount, $root.ChunkCount)

# Function to list chunks recursively
function List-Chunks {
    param(
        [GH_IO.Serialization.GH_Chunk]$chunk,
        [int]$depth
    )
    $indent = "  " * $depth
    Write-Host ("{0}Chunk: Name='{1}', ItemCount={2}, ChunkCount={3}" -f $indent, $chunk.Name, $chunk.ItemCount, $chunk.ChunkCount)
    # List sub-chunks
    for($i=0; $i -lt $chunk.ChunkCount; $i++) {
        $subChunk = $chunk.Chunks[$i]
        List-Chunks -chunk $subChunk -depth ($depth+1)
    }
}

Write-Host "`nListing chunks:"
List-Chunks -chunk $root -depth 0