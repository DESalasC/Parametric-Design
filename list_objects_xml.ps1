# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

try {
    [xml]$xml = Get-Content -Path $path
    Write-Host "Loaded XML successfully"
} catch {
    Write-Error "Failed to load XML: $_"
    exit 1
}

# Find all Object elements
$objects = $xml.SelectNodes("//Object")
Write-Host "Found $($objects.Count) Object elements."

if ($objects.Count -gt 0) {
    Write-Host "`nFirst 20 Objects:"
    for($i=0; $i -lt [Math]::Min(20, $objects.Count); $i++) {
        $obj = $objects[$i]
        $nickName = $obj.SelectSingleNode("NickName")
        $typeName = $obj.SelectSingleNode("TypeName")
        $name = $obj.SelectSingleNode("Name")
        Write-Host ("{0,3}: NickName='{1}', TypeName='{2}', Name='{3}'" -f ($i+1),
            if($nickName) { $nickName.InnerText } else { "" },
            if($typeName) { $typeName.InnerText } else { "" },
            if($name) { $name.InnerText } else { "" })
    }
} else {
    Write-Host "No Object elements found."
}

// Also, let's see what types of objects we have by looking at TypeName values
Write-Host "`nCollecting unique TypeName values:"
$typeNames = @()
foreach($obj in $objects) {
    $typeNameNode = $obj.SelectSingleNode("TypeName")
    if ($typeNameNode) {
        $typeNames += $typeNameNode.InnerText
    }
}
$uniqueTypes = $typeNames | Sort-Object -Unique
Write-Host ("Found {0} unique TypeName(s):" -f $uniqueTypes.Count)
for($i=0; $i -lt $uniqueTypes.Count; $i++) {
    Write-Host "  {0}: {1}" -f ($i+1), $uniqueTypes[$i]
}

// Let's also look for any NickName elements regardless of value
Write-Host "`nAll NickName elements found:"
$nickNameNodes = $xml.SelectNodes("//NickName")
Write-Host "Found $($nickNameNodes.Count) NickName elements."
if ($nickNameNodes.Count -gt 0) {
    for($i=0; $i -lt [Math]::Min(10, $nickNameNodes.Count); $i++) {
        $node = $nickNameNodes[$i]
        Write-Host ("  {0}: '{1}'" -f ($i+1), $node.InnerText)
    }
}