# Define paths using wildcard to handle special characters
$wildcardPathGhx = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPathGhx = Resolve-Path -Path $wildcardPathGhx
$ghxPath = $resolvedPathGhx.Path

$wildcardPathNewCode = 'D:\Work\PROJECTS\Dise*/src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.py'
$resolvedPathNewCode = Resolve-Path -Path $wildcardPathNewCode
$newCodePath = $resolvedPathNewCode.Path

$targetString = "F1_ETAPA1_CONTEXTO_v02"

Write-Host "=== DEBUG INFO ==="
Write-Host "GHX wildcard: $wildcardPathGhx"
Write-Host "GHX resolved: $ghxPath"
Write-Host "GHX exists: $(Test-Path $ghxPath)"
Write-Host ""
Write-Host "New code wildcard: $wildcardPathNewCode"
Write-Host "New code resolved: $newCodePath"
Write-Host "New code exists: $(Test-Path $newCodePath)"
Write-Host ""
Write-Host "Target string: $targetString"
Write-Host "=================="

# Check if files exist
if (-not (Test-Path $ghxPath)) {
    Write-Host "ERROR: GHX file not found at $ghxPath"
    exit 1
}

if (-not (Test-Path $newCodePath)) {
    Write-Host "ERROR: New code file not found at $newCodePath"
    exit 1
}

Write-Host "GHX file: $ghxPath"
Write-Host "Target string: $targetString"
Write-Host "New code file: $newCodePath"

# Run the patching script with explicit parameters
Write-Host "`nRunning patch script..."
& "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\patch_component_by_content.ps1" `
    -ghxPath $ghxPath `
    -targetString $targetString `
    -newCodePath $newCodePath

write-host "Exit code: $LASTEXITCODE"