# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

# Search for NickName element
Write-Host "Searching for <NickName>F1_ETAPA1_CONTEXTO_v02</NickName>"
$matches = Select-String -Path $path -Pattern '<NickName>F1_ETAPA1_CONTEXTO_v02</NickName>' -SimpleMatch
if ($matches) {
    Write-Host "Found element:"
    $matches | ForEach-Object { Write-Host "$($_.LineNumber): $($_.Line)" }
} else {
    Write-Host "Not found."
}

# Search for NickName attribute with double quotes
Write-Host "`nSearching for NickName=""F1_ETAPA1_CONTEXTO_v02"" (double quotes)"
$matches = Select-String -Path $path -Pattern 'NickName="F1_ETAPA1_CONTEXTO_v02"' -SimpleMatch
if ($matches) {
    Write-Host "Found attribute:"
    $matches | ForEach-Object { Write-Host "$($_.LineNumber): $($_.Line)" }
} else {
    Write-Host "Not found."
}

# Search for NickName attribute with single quotes
Write-Host "`nSearching for NickName='F1_ETAPA1_CONTEXTO_v02' (single quotes)"
$matches = Select-String -Path $path -Pattern "NickName='F1_ETAPA1_CONTEXTO_v02'" -SimpleMatch
if ($matches) {
    Write-Host "Found attribute:"
    $matches | ForEach-Object { Write-Host "$($_.LineNumber): $($_.Line)" }
} else {
    Write-Host "Not found."
}

# Also search for the string without tags to see context
Write-Host "`nSearching for the string F1_ETAPA1_CONTEXTO_v02 (anywhere)"
$matches = Select-String -Path $path -Pattern 'F1_ETAPA1_CONTEXTO_v02' -SimpleMatch
if ($matches) {
    Write-Host "Found $($matches.Count) occurrences:"
    for($i=0; $i -lt [Math]::Min(5, $matches.Count); $i++) {
        Write-Host "$($matches[$i].LineNumber): $($matches[$i].Line)"
    }
} else {
    Write-Host "Not found."
}