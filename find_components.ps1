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
    Write-Host "Root node: Name=$($root.Name), ItemCount=$($root.ItemCount), ChunkCount=$($root.ChunkCount)"
} catch {
    Write-Error "Failed to get root node: $_"
    exit 1
}

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
            Write-Host "$indent`tItem[$i]: Name=$($item.Name), NickName=$($item.NickName), Type=$($item.Type)"
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
Write-Host "Searching for NickName 'F1_ETAPA1_CONTEXTO_v02' in chunks..."
$found = Find-NickNameInChunk -chunk $root -depth 0
if ($found) {
    Write-Host "SUCCESS: Found the target object."
} else {
    Write-Host "FAILURE: Target object not found in chunks."
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

// Let's also try to use the ExtractObject method to see if we can get objects by nickname
Write-Host ""
Write-Host "Trying to extract object by nickname using ExtractObject..."
try {
    $extracted = $doc.ExtractObject($null, "F1_ETAPA1_CONTEXTO_v02")
    if ($extracted) {
        Write-Host "Extracted object: $($extracted.GetType().Name)"
    } else {
        Write-Host "ExtractObject returned null."
    }
} catch {
    Write-Error "ExtractObject failed: $_"
}