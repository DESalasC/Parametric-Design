$path = 'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx'
Write-Host "Testing path: $path"
if(Test-Path -LiteralPath $path) {
    Write-Host "File EXISTS"
} else {
    Write-Host "File does NOT exist"
}