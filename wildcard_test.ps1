$path = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
Write-Host "Path: $path"
if (Test-Path $path) {
    Write-Host "Exists"
} else {
    Write-Host "Does not exist"
}