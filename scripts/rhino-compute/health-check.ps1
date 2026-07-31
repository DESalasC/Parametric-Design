# ==============================================================================
# health-check.ps1
# ------------------------------------------------------------------------------
# Verifica el estado de todos los servicios del stack:
#   - Rhino.Compute (puerto 6001)
#   - Ollama (puerto 11434)
#   - fcc-server (puerto 8787)
#   - Obsidian (proceso)
#   - Git (versión)
#   - Python (versión)
#   - rhino3dm (librería Python)
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\health-check.ps1
# ==============================================================================

#Requires -Version 7.0

$ErrorActionPreference = "Continue"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  HEALTH CHECK — DiseñoParametrico" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
function Test-Port {
    param([int]$Port, [string]$Name, [string]$ExpectedPath = "/health")

    $url = "http://127.0.0.1:$Port$ExpectedPath"
    try {
        $response = Invoke-RestMethod -Uri $url -Method Get -TimeoutSec 3 -ErrorAction Stop
        Write-Host "  [OK]   $Name (puerto $Port)" -ForegroundColor Green
        return $true
    } catch {
        if ($_.Exception.Response -ne $null) {
            # Hay respuesta pero error HTTP
            Write-Host "  [WARN] $Name (puerto $Port) - responde pero con error" -ForegroundColor Yellow
            return $false
        } else {
            Write-Host "  [FAIL] $Name (puerto $Port) - no responde" -ForegroundColor Red
            return $false
        }
    }
}

function Test-Command {
    param([string]$Command, [string]$DisplayName)

    $cmd = Get-Command $Command -ErrorAction SilentlyContinue
    if ($cmd) {
        try {
            $version = & $Command --version 2>&1 | Select-Object -First 1
            Write-Host "  [OK]   $DisplayName : $version" -ForegroundColor Green
        } catch {
            Write-Host "  [OK]   $DisplayName (versión no detectada)" -ForegroundColor Green
        }
    } else {
        Write-Host "  [FAIL] $DisplayName no encontrado en PATH" -ForegroundColor Red
    }
}

# ---------------------------------------------------------------------------
# 1. Servicios HTTP
# ---------------------------------------------------------------------------
Write-Host "[1] Servicios HTTP" -ForegroundColor Cyan

$computeOk = Test-Port -Port 6001 -Name "Rhino.Compute"
$ollamaOk = Test-Port -Port 11434 -Name "Ollama" -ExpectedPath "/api/tags"
$fccOk = Test-Port -Port 8787 -Name "fcc-server"

# ---------------------------------------------------------------------------
# 2. Comandos
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[2] Comandos disponibles" -ForegroundColor Cyan

Test-Command -Command "git" -DisplayName "Git"
Test-Command -Command "python" -DisplayName "Python"
Test-Command -Command "node" -DisplayName "Node.js"
Test-Command -Command "pwsh" -DisplayName "PowerShell 7"
Test-Command -Command "ollama" -DisplayName "Ollama"
Test-Command -Command "claude" -DisplayName "Claude Code"

# ---------------------------------------------------------------------------
# 3. Variables de entorno
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[3] Variables de entorno" -ForegroundColor Cyan

$envVars = @(
    "OLLAMA_HOST",
    "OLLAMA_MODELS",
    "RHINO_COMPUTE_URL",
    "ANTHROPIC_BASE_URL",
    "DISENO_PARAMETRICO_ROOT",
    "POT_GPKG_PATH"
)

foreach ($var in $envVars) {
    $val = [Environment]::GetEnvironmentVariable($var, "User")
    if ($val) {
        Write-Host "  [OK]   $var = $val" -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] $var no definida (User scope)" -ForegroundColor Red
    }
}

# ---------------------------------------------------------------------------
# 4. Rutas críticas
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[4] Rutas críticas" -ForegroundColor Cyan

$criticalPaths = @(
    @{ Path = "D:\WORK"; Name = "WORK root" },
    @{ Path = "D:\WORK\PROJECTS\DiseñoParametrico"; Name = "Proyecto" },
    @{ Path = "D:\WORK\NOTES\obsidian-vault"; Name = "Vault Obsidian" },
    @{ Path = "D:\Work\AI\ollama\ollama.exe"; Name = "Ollama binario" },
    @{ Path = "D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"; Name = "POT .gpkg" }
)

foreach ($item in $criticalPaths) {
    if (Test-Path $item.Path) {
        Write-Host "  [OK]   $($item.Name): $($item.Path)" -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] $($item.Name): $($item.Path)" -ForegroundColor Red
    }
}

# ---------------------------------------------------------------------------
# 5. Modelos Ollama descargados
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[5] Modelos Ollama" -ForegroundColor Cyan

if ($ollamaOk) {
    try {
        $models = Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -Method Get -TimeoutSec 3
        if ($models.models.Count -eq 0) {
            Write-Host "  [WARN] No hay modelos descargados" -ForegroundColor Yellow
            Write-Host "         Descarga con: ollama pull qwen2.5-coder:14b" -ForegroundColor Gray
        } else {
            foreach ($m in $models.models) {
                $sizeGB = [math]::Round($m.size / 1GB, 2)
                Write-Host "  [OK]   $($m.name) (${sizeGB}GB)" -ForegroundColor Green
            }
        }
    } catch {
        Write-Host "  [FAIL] No se pudo listar modelos" -ForegroundColor Red
    }
} else {
    Write-Host "  [SKIP] Ollama no responde, no se pueden listar modelos" -ForegroundColor Gray
}

# ---------------------------------------------------------------------------
# 6. Librerías Python
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[6] Librerías Python" -ForegroundColor Cyan

$pythonLibs = @("rhino3dm", "shapely", "pyogrio", "fiona", "click", "rich", "pyproj")

foreach ($lib in $pythonLibs) {
    $result = & python -c "import $lib; print($lib.__version__)" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK]   $lib ($result)".Trim() -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] $lib no instalado" -ForegroundColor Red
    }
}

# ---------------------------------------------------------------------------
# 7. Resumen
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  RESUMEN" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$allOk = $computeOk -and $ollamaOk -and $fccOk
if ($allOk) {
    Write-Host "  [TODO OK] Stack completo operativo" -ForegroundColor Green
} else {
    Write-Host "  [ATENCIÓN] Algunos servicios no están corriendo:" -ForegroundColor Yellow
    if (-not $computeOk) { Write-Host "    - Rhino.Compute: ejecuta start-compute.ps1" -ForegroundColor Gray }
    if (-not $ollamaOk) { Write-Host "    - Ollama: ejecuta 'ollama serve' o reinicia servicio" -ForegroundColor Gray }
    if (-not $fccOk) { Write-Host "    - fcc-server: cd D:\WORK\AI\fcc-server && npm start" -ForegroundColor Gray }
}

Write-Host ""
