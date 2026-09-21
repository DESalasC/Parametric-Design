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

# Search for NickName elements with the specific value
$nickNameNodes = $xml.SelectNodes("//NickName[text()='F1_ETAPA1_CONTEXTO_v02']")
if ($nickNameNodes.Count -gt 0) {
    Write-Host ("Found {0} NickName element(s) with value 'F1_ETAPA1_CONTEXTO_v02':" -f $nickNameNodes.Count)
    for($i=0; $i -lt $nickNameNodes.Count; $i++) {
        $node = $nickNameNodes[$i]
        Write-Host ("  Node {0}: " -f ($i+1))
        # Try to get parent Object element
        $parent = $node.ParentNode
        while ($parent -and $parent.Name -ne 'Object') {
            $parent = $parent.ParentNode
        }
        if ($parent) {
            Write-Host "    Found parent Object element"
            # Get the TypeName if available
            $typeNameNode = $parent.SelectSingleNode("TypeName")
            if ($typeNameNode) {
                Write-Host ("    TypeName: {0}" -f $typeNameNode.InnerText)
            }
            # Get the Name if available
            $nameNode = $parent.SelectSingleNode("Name")
            if ($nameNode) {
                Write-Host ("    Name: {0}" -f $nameNode.InnerText)
            }
        } else {
            Write-Host "    No parent Object element found"
        }
        # Show surrounding XML for context
        $outerXml = $node.OuterXml
        Write-Host "    OuterXml: $outerXml"
    }
} else {
    Write-Host "No NickName element with value 'F1_ETAPA1_CONTEXTO_v02' found."

    # Let's see what NickName elements exist
    $allNickNames = $xml.SelectNodes("//NickName")
    Write-Host ("Total NickName elements found: {0}" -f $allNickNames.Count)
    if ($allNickNames.Count -gt 0) {
        Write-Host "First 10 NickName values:"
        for($i=0; $i -lt [Math]::Min(10, $allNickNames.Count); $i++) {
            Write-Host ("  {0}: {1}" -f ($i+1), $allNickNames[$i].InnerText)
        }
    }
}