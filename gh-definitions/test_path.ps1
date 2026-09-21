# Simple path test
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
Write-Host "Testing wildcard path: $wildcardPath"
$resolvedPath = Resolve-Path -Path $wildcardPath
Write-Host "Resolved path: $($resolvedPath.Path)"
if (Test-Path $resolvedPath.Path) {
    Write-Host "File exists!"
    # Try to read it as XML
    try {
        [xml]$xml = Get-Content -Path $resolvedPath.Path
        Write-Host "XML loaded successfully."
        Write-Host "Root element: $($xml.Name)"
    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}