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

# Search for NickName as element with the specific value
$nickNameNodes = $xml.SelectNodes("//NickName[text()='F1_ETAPA1_CONTEXTO_v02']")
if ($nickNameNodes.Count -gt 0) {
    Write-Host ("Found {0} NickName element(s) with value 'F1_ETAPA1_CONTEXTO_v02':" -f $nickNameNodes.Count)
    exit 0
}

# Search for NickName as attribute with the specific value
$nickNameAttrs = $xml.SelectNodes("//*[@NickName='F1_ETAPA1_CONTEXTO_v02']")
if ($nickNameAttrs.Count -gt 0) {
    Write-Host ("Found {0} attribute(s) NickName='F1_ETAPA1_CONTEXTO_v02':" -f $nickNameAttrs.Count)
    for($i=0; $i -lt $nickNameAttrs.Count; $i++) {
        $node = $nickNameAttrs[$i]
        Write-Host ("  Node {0}: Name='{1}'" -f ($i+1), $node.Name)
        # Show surrounding XML for context
        $outerXml = $node.OuterXml
        Write-Host "    OuterXml: $outerXml"
    }
    exit 0
}

Write-Host "No NickName element or attribute with value 'F1_ETAPA1_CONTEXTO_v02' found."

# Let's see what NickName elements exist (as elements)
$allNickNameElements = $xml.SelectNodes("//NickName")
Write-Host ("Total NickName elements found: {0}" -f $allNickNameElements.Count)
if ($allNickNameElements.Count -gt 0) {
    Write-Host "First 10 NickName element values:"
    for($i=0; $i -lt [Math]::Min(10, $allNickNameElements.Count); $i++) {
        Write-Host ("  {0}: {1}" -f ($i+1), $allNickNameElements[$i].InnerText)
    }
} else {
    Write-Host "No NickName elements found."
}

# Let's see what NickName attributes exist
$allNickNameAttrs = $xml.SelectNodes("//*[@NickName]")
Write-Host ("Total NickName attributes found: {0}" -f $allNickNameAttrs.Count)
if ($allNickNameAttrs.Count -gt 0) {
    Write-Host "First 10 NickName attribute values:"
    for($i=0; $i -lt [Math]::Min(10, $allNickNameAttrs.Count); $i++) {
        $node = $allNickNameAttrs[$i]
        Write-Host ("  {0}: NodeName='{1}', Value='{2}'" -f ($i+1), $node.Name, $node.NickName)
    }
} else {
    Write-Host "No NickName attributes found."
}