$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
Write-Host "Wildcard path: $wildcardPath"
$resolvedPath = Resolve-Path -Path $wildcardPath
Write-Host "Resolved path: $resolvedPath"
if (Test-Path $resolvedPath) {
    Write-Host "File EXISTS"
} else {
    Write-Host "File does NOT exist"
}