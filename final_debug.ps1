# Resolve the path first
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$ghxPath = $resolvedPath.Path

Write-Host "Using GHX path: $ghxPath"

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
    $doc.ReadFromFile($ghxPath)
    Write-Host "Successfully loaded GHX file"
} catch {
    Write-Error "Failed to load GHX document: $_"
    exit 1
}

# List all objects by NickName
$objects = $doc.Objects
Write-Host ("Found {0} objects:" -f $objects.Count)
if($objects.Count -gt 0) {
    for($i=0; $i -lt $objects.Count; $i++) {
        $obj = $objects[$i]
        Write-Host ("  [{0}] NickName: {1}, TypeName: {2}" -f $i, $obj.NickName, $obj.TypeName)
    }
} else {
    Write-Host "No objects found"
}

# Let's also try to get the root node differently
try {
    $rootNode = $doc.GetRootNode()
    Write-Host ("Root node type: {0}" -f $rootNode.GetType().FullName)
    Write-Host ("Root node name: {0}" -f $rootNode.Name)
    Write-Host ("Root node item count: {0}" -f $rootNode.ItemCount)
    Write-Host ("Root node chunk count: {0}" -f $rootNode.ChunkCount)
} catch {
    Write-Warning "Could not get root node: $_"
}