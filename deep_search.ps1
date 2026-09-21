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

# Function to find a chunk by name recursively
function Find-ChunkByName {
    param(
        [GH_IO.Serialization.GH_Chunk]$chunk,
        [string]$name
    )
    if ($chunk.Name -eq $name) {
        return $chunk
    }
    for($i=0; $i -lt $chunk.ChunkCount; $i++) {
        $subChunk = $chunk.Chunks[$i]
        $result = Find-ChunkByName -chunk $subChunk -name $name
        if ($result) { return $result }
    }
    return $null
}

# Find the DefinitionObjects chunk
$defObjChunk = Find-ChunkByName -chunk $root -name "DefinitionObjects"
if (-not $defObjChunk) {
    Write-Host "DefinitionObjects chunk not found."
    exit 1
}

Write-Host "Found DefinitionObjects chunk: ItemCount=$($defObjChunk.ItemCount), ChunkCount=$($defObjChunk.ChunkCount)"

# Function to search for NickName in a chunk and its sub-chunks
function Find-NickNameInObjectChunk {
    param(
        [GH_IO.Serialization.GH_Chunk]$objChunk,
        [int]$index
    )
    Write-Host "`nExamining Object chunk $index:"
    Write-Host "  Chunk: Name='$($objChunk.Name)', ItemCount=$($objChunk.ItemCount), ChunkCount=$($objChunk.ChunkCount)"

    # Look at direct items in this chunk
    for($i=0; $i -lt $objChunk.ItemCount; $i++) {
        $item = $objChunk.Items[$i]
        Write-Host "    Item $i: Name='$($item.Name)', NickName='$($item.NickName)', Type=$($item.Type)"
        if ($item.NickName -eq 'F1_ETAPA1_CONTEXTO_v02') {
            Write-Host "    >>> FOUND TARGET NICKNAME IN DIRECT ITEM!"
            return $item
        }
    }

    # Look in sub-chunks (like Container)
    for($i=0; $i -lt $objChunk.ChunkCount; $i++) {
        $subChunk = $objChunk.Chunks[$i]
        Write-Host "    Sub-chunk $i: Name='$($subChunk.Name)', ItemCount=$($subChunk.ItemCount), ChunkCount=$($subChunk.ChunkCount)"

        # Look at items in sub-chunk
        for($j=0; $j -lt $subChunk.ItemCount; $j++) {
            $item = $subChunk.Items[$j]
            Write-Host "      Item $j: Name='$($item.Name)', NickName='$($item.NickName)', Type=$($item.Type)"
            if ($item.NickName -eq 'F1_ETAPA1_CONTEXTO_v02') {
                Write-Host "      >>> FOUND TARGET NICKNAME IN SUB-CHUNK ITEM!"
                return $item
            }
        }

        # Look in sub-sub-chunks (like Attributes, ParameterData)
        for($j=0; $j -lt $subChunk.ChunkCount; $j++) {
            $subSubChunk = $subChunk.Chunks[$j]
            Write-Host "      Sub-sub-chunk $j: Name='$($subSubChunk.Name)', ItemCount=$($subSubChunk.ItemCount), ChunkCount=$($subSubChunk.ChunkCount)"

            # Look at items in sub-sub-chunk
            for($k=0; $k -lt $subSubChunk.ItemCount; $k++) {
                $item = $subSubChunk.Items[$k]
                Write-Host "        Item $k: Name='$($item.Name)', NickName='$($item.NickName)', Type=$($item.Type)"
                if ($item.NickName -eq 'F1_ETAPA1_CONTEXTO_v02') {
                    Write-Host "        >>> FOUND TARGET NICKNAME IN SUB-SUB-CHUNK ITEM!"
                    return $item
                }
            }
        }
    }
    return $null
}

# Search through all Object chunks in DefinitionObjects
Write-Host "`nSearching through Object chunks..."
$found = $null
for($i=0; $i -lt [Math]::Min(10, $defObjChunk.ChunkCount); $i++) {  # Check first 10 Object chunks
    $objChunk = $defObjChunk.Chunks[$i]
    if ($objChunk.Name -eq 'Object') {
        $result = Find-NickNameInObjectChunk -objChunk $objChunk -index $i
        if ($result) {
            $found = $result
            break
        }
    }
}

if ($found) {
    Write-Host "`nSUCCESS: Found the target object with NickName 'F1_ETAPA1_CONTEXTO_v02'"
} else {
    Write-Host "`nFAILURE: Target object not found in first 10 Object chunks."
    // Let's try to search more chunks or look for patterns
    Write-Host "`nLet's check if any NickName has any value at all..."
    $anyNickName = $null
    for($i=0; $i -lt [Math]::Min(20, $defObjChunk.ChunkCount) -and -not $anyNickName; $i++) {
        $objChunk = $defObjChunk.Chunks[$i]
        if ($objChunk.Name -eq 'Object') {
            for($j=0; $j -lt $objChunk.ItemCount; $j++) {
                $item = $objChunk.Items[$j]
                if ($item.NickName) {
                    $anyNickName = $item
                    Write-Host "Found NickName with value: '$($item.NickName)' in Object $i, Item $j"
                    break
                }
            }
            if (-not $anyNickName) {
                for($j=0; $j -lt $objChunk.ChunkCount; $j++) {
                    $subChunk = $objChunk.Chunks[$j]
                    for($k=0; $k -lt $subChunk.ItemCount; $k++) {
                        $item = $subChunk.Items[$k]
                        if ($item.NickName) {
                            $anyNickName = $item
                            Write-Host "Found NickName with value: '$($item.NickName)' in Object $i, Sub-chunk $j, Item $k"
                            break
                        }
                    }
                    if ($anyNickName) { break }
                }
            }
        }
    }
    if (-not $anyNickName) {
        Write-Host "No NickName with any value found in first 20 Object chunks."
    }
}