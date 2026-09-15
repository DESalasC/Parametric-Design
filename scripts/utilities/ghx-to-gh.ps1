<#
    ghx-to-gh.ps1
    Convierte un archivo Grasshopper .ghx (XML) a .gh (binario) usando GH_IO.dll de Rhino 8.
    No requiere abrir Rhino ni Grasshopper: GH_IO.GH_Archive soporta ambos formatos
    y decide binario/XML por la extension del archivo de salida.

    Uso:
        pwsh -NoProfile -File ghx-to-gh.ps1
        pwsh -NoProfile -File ghx-to-gh.ps1 -InputGhx <ruta.ghx> -OutputGh <ruta.gh>

    Requisitos:
        - PowerShell 7 (pwsh). Ver nota de codificacion abajo.
        - Rhino 8 instalado (GH_IO.dll).

    Nota: guardar este archivo como UTF-8 con BOM para que Windows PowerShell 5.1
    tambien lo pueda leer sin corromper rutas con acentos.
#>
[CmdletBinding()]
param(
    [string]$InputGhx,
    [string]$OutputGh,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
if (-not $InputGhx) { $InputGhx = Join-Path $projectRoot 'gh-definitions\F1_Contexto_Base-Editado_v03.ghx' }
if (-not $OutputGh) { $OutputGh = [System.IO.Path]::ChangeExtension($InputGhx, '.gh') }

Write-Host "Entrada : $InputGhx"
Write-Host "Salida  : $OutputGh"

if (-not (Test-Path -LiteralPath $InputGhx)) { throw "No existe el archivo .ghx: $InputGhx" }

$ghIo = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
if (-not (Test-Path -LiteralPath $ghIo)) { throw "No se encontro GH_IO.dll en: $ghIo" }
if (-not ('GH_IO.Serialization.GH_Archive' -as [type])) { Add-Type -Path $ghIo }

if (Test-Path -LiteralPath $OutputGh) {
    if ($Force) {
        Remove-Item -LiteralPath $OutputGh -Force
    }
    else {
        $stamp = Get-Date -Format 'yyyyMMdd-HHmm'
        $backup = "$OutputGh.bak-$stamp"
        Move-Item -LiteralPath $OutputGh -Destination $backup
        Write-Host "Backup  : $backup"
    }
}

$archive = New-Object GH_IO.Serialization.GH_Archive
$read = $archive.ReadFromFile($InputGhx)
if (-not $read) { throw "GH_Archive no pudo leer el .ghx (archivo invalido o corrupto)." }

$warnings = $archive.MessageCount()
if ($warnings -gt 0) { Write-Host "Avisos del archivo: $warnings (ver GH_Archive.Messages en Rhino)" }

$written = $archive.WriteToFile($OutputGh, $true, $false)
if (-not $written) { throw "GH_Archive no pudo escribir el .gh de salida." }

$out = Get-Item -LiteralPath $OutputGh
Write-Host ("OK: {0} ({1:N0} bytes)" -f $out.FullName, $out.Length)
