# ==============================================================================
# stop-compute.ps1
# ------------------------------------------------------------------------------
# Detiene Rhino.Compute si está corriendo en el puerto 6001.
# ==============================================================================

#Requires -Version 7.0

param(
    [int]$Port = 6001
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  stop-compute.ps1" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1] Buscando proceso en puerto $Port..." -ForegroundColor Yellow

$conn = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue | Select-Object -First 1

if (-not $conn) {
    Write-Host "    [OK] No hay proceso en puerto $Port" -ForegroundColor Green
    exit 0
}

$processId = $conn.OwningProcess
$process = Get-Process -Id $processId -ErrorAction SilentlyContinue

if (-not $process) {
    Write-Host "    [OK] Puerto libre, proceso ya terminado" -ForegroundColor Green
    exit 0
}

Write-Host "    [INFO] Proceso: $($process.ProcessName) (PID: $processId)" -ForegroundColor Cyan

# Confirmar si es compute
if ($process.ProcessName -notlike "*compute*" -and $process.ProcessName -notlike "*rhino*") {
    Write-Host "    [WARN] El proceso NO parece ser Rhino.Compute: $($process.ProcessName)" -ForegroundColor Yellow
    $confirm = Read-Host "    ¿Detener de todas formas? (s/N)"
    if ($confirm -ne "s") {
        Write-Host "    [ABORT] Operación cancelada" -ForegroundColor Yellow
        exit 0
    }
}

# Detener proceso
Write-Host ""
Write-Host "[2] Deteniendo PID $processId..." -ForegroundColor Yellow

try {
    Stop-Process -Id $processId -Force -ErrorAction Stop
    Start-Sleep -Seconds 2
    Write-Host "    [OK] Proceso detenido" -ForegroundColor Green
} catch {
    Write-Host "    [ERROR] No se pudo detener: $_" -ForegroundColor Red
    exit 1
}

# Verificar
$conn2 = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
if ($conn2) {
    Write-Host "    [WARN] Puerto $Port aún ocupado" -ForegroundColor Yellow
} else {
    Write-Host "    [OK] Puerto $Port liberado" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  COMPUTE DETENIDO" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
