# Test path resolution for new code file
$wildcardPath = 'D:\Work\PROJECTS\Dise*/src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.py'
Write-Host "Testing wildcard path: $wildcardPath"
try {
    $resolvedPath = Resolve-Path -Path $wildcardPath
    Write-Host "Resolved path: $($resolvedPath.Path)"
    if (Test-Path $resolvedPath.Path) {
        Write-Host "File exists!"
        # Try to read it
        $content = Get-Content -Path $resolvedPath.Path -Raw
        Write-Host ("File length: {0} characters" -f $content.Length)
    } else {
        Write-Host "File does not exist."
    }
} catch {
    Write-Host "Error resolving path: $_"
}