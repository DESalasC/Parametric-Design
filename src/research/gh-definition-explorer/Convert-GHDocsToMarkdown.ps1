param(
    # Carpeta raíz del repo clonado
    [string]$SourceRoot = "C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\grasshopper-api-docs",
    # Carpeta donde quieres la salida Markdown (obsidian / notebooklm / graphify)
    [string]$OutputRoot = "C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
)

Import-Module MarkdownPrince -ErrorAction Stop

# Carpeta donde están los .htm del SDK
$HtmlRoot = Join-Path $SourceRoot "api\grasshopper\html"

Write-Host "Fuente HTML: $HtmlRoot"
Write-Host "Salida Markdown: $OutputRoot"

# Crear carpeta de salida si no existe
if (-not (Test-Path $OutputRoot)) {
    New-Item -ItemType Directory -Path $OutputRoot | Out-Null
}

# Recorrer todos los .htm
$files = Get-ChildItem -Path $HtmlRoot -Recurse -Filter *.htm

foreach ($file in $files) {
    $relativePath = $file.FullName.Substring($HtmlRoot.Length).TrimStart('\')

    # Cambiar extensión a .md
    $mdRelativePath = [System.IO.Path]::ChangeExtension($relativePath, ".md")
    $destPath = Join-Path $OutputRoot $mdRelativePath

    # Crear carpeta destino si no existe
    $destDir = Split-Path $destPath -Parent
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    Write-Host "Convirtiendo: $($file.FullName) -> $destPath"

    # Convertir HTML a Markdown (Github-flavored, ajustable)
    try {
        ConvertFrom-HTMLToMarkdown `
            -Path $file.FullName `
            -UnknownTags Bypass `
            -GithubFlavored `
            -DestinationPath $destPath `
            -ErrorAction Stop
    }
    catch {
        Write-Warning "Error al convertir $($file.FullName): $_"
    }
}