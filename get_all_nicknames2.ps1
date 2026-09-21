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

# Find all NickName elements
$nickNameNodes = $xml.SelectNodes("//NickName")
Write-Host "Found $($nickNameNodes.Count) NickName elements."

if ($nickNameNodes.Count -gt 0) {
    $values = @()
    foreach($node in $nickNameNodes) {
        $values += $node.InnerText
    }
    Write-Host "NickName values: $($values -join ', ')"
} else {
    Write-Host "No NickName elements found."
}

# Search for any element that might contain the nickname as text (like in a description)
Write-Host "`nSearching for any element containing the string 'F1_ETAPA1_CONTEXTO_v02'..."
$matches = $xml.SelectNodes("//*[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
if ($matches) {
    Write-Host "Found $($matches.Count) element(s) containing the string:"
    foreach($node in $matches) {
        Write-Host "  Element: $($node.Name)"
        Write-Host "    Text: $($node.InnerText)"
    }
} else {
    Write-Host "No elements contain the string."
}