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
if ($defObjChunk) {
    Write-Host "Found DefinitionObjects chunk: ItemCount=$($defObjChunk.ItemCount), ChunkCount=$($defObjChunk.ChunkCount)"
} else {
    Write-Host "DefinitionObjects chunk not found."
    exit 1
}

# The DefinitionObjects chunk seems to have one item and many sub-chunks.
# Let's look at its sub-chunks, which should be the Object chunks.
Write-Host "`nExamining sub-chunks of DefinitionObjects (should be Object chunks):"
for($i=0; $i -lt [Math]::Min(5, $defObjChunk.ChunkCount); $i++) {
    $objChunk = $defObjChunk.Chunks[$i]
    Write-Host ("  Chunk {0}: Name='{1}', ItemCount={2}, ChunkCount={3}" -f $i, $objChunk.Name, $objChunk.ItemCount, $objChunk.ChunkCount)
    # Now look at the items in this chunk
    for($j=0; $j -lt $objChunk.ItemCount; $j++) {
        $item = $objChunk.Items[$j]
        Write-Host ("    Item {0}: Name='{1}', NickName='{2}', Type={3}" -f $j, $item.Name, $item.NickName, $item.Type)
    }
    # Also, if this chunk has sub-chunks, we might look there too, but let's first see if the item is the object.
}

# Let's also try to see if we can get the object from the GH_Archive using ExtractObject with a different approach
Write-Host "`nTrying ExtractObject with nickname..."
try {
    # The ExtractObject method might require a type parameter? Let's check the overloads.
    $method = $doc.GetType().GetMethod("ExtractObject", @([System.Type], [string]))
    if ($method) {
        Write-Host "Found ExtractObject with Type and string parameters."
        # We need to know what type to pass. Let's try GH_Object.
        $ghObjectType = [GH_IO.GH_Object]
        $obj = $method.Invoke($doc, @($ghObjectType, "F1_ETAPA1_CONTEXTO_v02"))
        if ($obj) {
            Write-Host "Extracted object: $($obj.GetType().Name)"
            Write-Host "NickName: $($obj.NickName)"
        } else {
            Write-Host "ExtractObject returned null."
        }
    } else {
        Write-Host "ExtractObject with Type and string not found."
        # Try the overload with just string?
        $method2 = $doc.GetType().GetMethod("ExtractObject", @([string]))
        if ($method2) {
            Write-Host "Found ExtractObject with string parameter."
            $obj = $method2.Invoke($doc, @("F1_ETAPA1_CONTEXTO_v02"))
            if ($obj) {
                Write-Host "Extracted object: $($obj.GetType().Name)"
                Write-Host "NickName: $($obj.NickName)"
            } else {
                Write-Host "ExtractObject returned null."
            }
        } else {
            Write-Host "No ExtractObject overload found."
        }
    }
} catch {
    Write-Error "Error in ExtractObject: $_"
}