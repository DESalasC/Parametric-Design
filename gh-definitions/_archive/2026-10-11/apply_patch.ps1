# Define paths
$ghxPath = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
$targetString = "F1_ETAPA1_CONTEXTO_v02"
$newCodePath = "D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA1_CONTEXTO_v04.py"

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

# Run the patching script
& "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\patch_component_by_content.ps1" `
    -ghxPath $ghxPath `
    -targetString $targetString `
    -newCodePath $newCodePath

if ($LASTEXITCODE -eq 0) {
    Write-Host "Patching completed successfully."
} else {
    Write-Host "Patching failed."
    exit $LASTEXITCODE
}