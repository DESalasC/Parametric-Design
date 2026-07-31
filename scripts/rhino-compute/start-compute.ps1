# ==============================================================================
# start-compute.ps1
# ------------------------------------------------------------------------------
# Inicia Rhino.Compute en modo headless en el puerto 6001.
#
# Requisitos:
#   - Rhino 8 (o 7) instalado en C:\Program Files\Rhino 8\
#   - compute.rhino3d.exe en la subcarpeta System\compute\
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\start-compute.ps1
#   powershell -ExecutionPolicy Bypass -File .\start-compute.ps1 -Port 6001
#   powershell -ExecutionPolicy Bypass -File .\start-compute.ps1 -Detach
# ==============================================================================

#Requires -Version 7.0

param(
    [int]$Port = 6001,
    [switch]$Detach = $false,
    [string]$RhinoVersion = "8"
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  start-compute.ps1" -ForegroundColor Cyan
Write-Host "  Rhino.Compute headless" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ---------------------------------------------------------------------------
# Buscar compute.rhino3d.exe
# ---------------------------------------------------------------------------
$computePaths = @(
    "C:\Program Files\Rhino $RhinoVersion\System\compute\compute.rhino3d.exe",
    "C:\Program Files\Rhino $($RhinoVersion - 1)\System\compute\compute.rhino3d.exe",
    "C:\Program Files\Rhino 8 WIP\System\compute\compute.rhino3d.exe"
)

$computeExe = $null
foreach ($path in $computePaths) {
    if (Test-Path $path) {
        $computeExe = $path
        break
    }
}

if (-not $computeExe) {
    Write-Host "[ERROR] No se encontró compute.rhino3d.exe" -ForegroundColor Red
    Write-Host "        Rutas buscadas:" -ForegroundColor Red
    foreach ($p in $computePaths) {
        Write-Host "        - $p" -ForegroundColor Gray
    }
    Write-Host ""
    Write-Host "        Instala Rhino 8 desde https://www.rhino3d.com/download" -ForegroundColor Yellow
    exit 1
}

Write-Host "[INFO] Compute encontrado: $computeExe" -ForegroundColor Green

# ---------------------------------------------------------------------------
# Verificar que el puerto no esté en uso
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[1] Verificando puerto $Port..." -ForegroundColor Yellow

$portInUse = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
if ($portInUse) {
    $processId = $portInUse.OwningProcess
    $process = Get-Process -Id $processId -ErrorAction SilentlyContinue
    if ($process.ProcessName -like "*compute*") {
        Write-Host "    [OK] Rhino.Compute ya está corriendo (PID: $processId)" -ForegroundColor Green
        Write-Host "    [INFO] Si necesitas reiniciarlo, ejecuta stop-compute.ps1 primero." -ForegroundColor Cyan
        exit 0
    } else {
        Write-Host "    [ERROR] Puerto $Port ocupado por: $($process.ProcessName) (PID: $processId)" -ForegroundColor Red
        Write-Host "           Libera el puerto o usa -Port <otro>." -ForegroundColor Yellow
        exit 1
    }
} else {
    Write-Host "    [OK] Puerto $Port libre" -ForegroundColor Green
}

# ---------------------------------------------------------------------------
# Iniciar Rhino.Compute
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[2] Iniciando Rhino.Compute..." -ForegroundColor Yellow

$arguments = @("--port", $Port, "--childof", $PID)

if ($Detach) {
    Write-Host "    [INFO] Modo detach (background)" -ForegroundColor Cyan
    $process = Start-Process -FilePath $computeExe -ArgumentList $arguments -WindowStyle Hidden -PassThru
} else {
    # Modo foreground: mostrar output en consola
    Write-Host "    [INFO] Modo foreground (Ctrl+C para detener)" -ForegroundColor Cyan
    Write-Host "    [INFO] Para background, usar -Detach" -ForegroundColor Gray
    $process = Start-Process -FilePath $computeExe -ArgumentList $arguments -PassThru
}

Write-Host "    [INFO] PID: $($process.Id)" -ForegroundColor Green

# ---------------------------------------------------------------------------
# Esperar a que responda
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "[3] Esperando respuesta en http://127.0.0.1:$Port/health..." -ForegroundColor Yellow

$maxRetries = 30
$retryDelay = 1  # segundos
$healthy = $false

for ($i = 1; $i -le $maxRetries; $i++) {
    try {
        $response = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/health" -Method Get -TimeoutSec 2 -ErrorAction Stop
        if ($response) {
            $healthy = $true
            Write-Host "    [OK] Compute respondiendo en intento $i" -ForegroundColor Green
            break
        }
    } catch {
        Write-Host "    [$i/$maxRetries] Esperando..." -ForegroundColor Gray
        Start-Sleep -Seconds $retryDelay
    }
}

if (-not $healthy) {
    Write-Host "    [ERROR] Compute no respondió en $maxRetries intentos" -ForegroundColor Red
    Write-Host "           Verifica que Rhino 8 esté activado (licencia)." -ForegroundColor Yellow
    exit 1
}

# ---------------------------------------------------------------------------
# Resumen final
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  RHINO.COMPUTE INICIADO" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "URL:      http://127.0.0.1:$Port" -ForegroundColor White
Write-Host "Health:   http://127.0.0.1:$Port/health" -ForegroundColor White
Write-Host "PID:      $($process.Id)" -ForegroundColor White
Write-Host ""
Write-Host "Para detener:" -ForegroundColor Yellow
Write-Host "  powershell -File stop-compute.ps1" -ForegroundColor Gray
Write-Host ""
Write-Host "Para verificar estado:" -ForegroundColor Yellow
Write-Host "  powershell -File health-check.ps1" -ForegroundColor Gray
Write-Host ""

if (-not $Detach) {
    Write-Host "[INFO] Manteniendo consola abierta. Ctrl+C para detener compute." -ForegroundColor Cyan
    Write-Host ""
    $process.WaitForExit()
}
