# cambiar_puerto_archicad.ps1
# Cambia el puerto del servidor CommandConnection de ArchiCAD 29 (Python/JSON API
# y Grasshopper Live Connection comparten este servidor) para evitar el conflicto
# con AutoClaw, que ocupa 127.0.0.1:19723.
# AVISO 2026-08-23: mover a 19724 SOLO sirve para la JSON/Python API (paquete 'archicad').
# La Live Connection de Grasshopper (AC_*) solo conecta por 19723 y NO respeta este cambio;
# para el canvas usar diagnostico_puerto_19723.ps1 -Liberar o cerrar/reabrir AutoClaw.
#
# HALLAZGO (2026-08-15): en ArchiCAD 29 NO existe UI para el puerto (la "Python
# palette" solo configura la ubicacion del interprete). El puerto vive en el
# registro de Windows:
#   HKCU\Software\Graphisoft\Archicad\Archicad 29.0.0 INT R1\CommandConnection
#     HTTPServerFirstPort = 19723   (REG_SZ)
#     HTTPServerPortCount = 100     (REG_SZ, rango de 100 puertos)
# La "teoria dice que si" (el puerto es configurable) -> via registro.
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File cambiar_puerto_archicad.ps1           # a 19724
#   powershell -ExecutionPolicy Bypass -File cambiar_puerto_archicad.ps1 -Puerto 19725
#   powershell -ExecutionPolicy Bypass -File cambiar_puerto_archicad.ps1 -Restaurar
#
# REQUISITO: ArchiCAD CERRADO (el registro se lee al arrancar).

param(
    [int]$Puerto = 19724,
    [switch]$Restaurar
)

$ruta = "HKCU:\Software\Graphisoft\Archicad\Archicad 29.0.0 INT R1\CommandConnection"
$valor = "HTTPServerFirstPort"
$nuevo = if ($Restaurar) { 19723 } else { $Puerto }

Write-Host "=== Cambio de puerto CommandConnection de ArchiCAD 29 ===" -ForegroundColor Cyan

if (-not (Test-Path $ruta)) {
    Write-Host "ERROR: no existe $ruta" -ForegroundColor Red
    exit 1
}

$actual = (Get-ItemProperty -Path $ruta -Name $valor -ErrorAction SilentlyContinue).$valor
if ($null -eq $actual) {
    Write-Host "ERROR: no existe la clave $valor" -ForegroundColor Red
    exit 1
}
Write-Host "Valor actual: HTTPServerFirstPort = $actual"
Write-Host "Nuevo valor : HTTPServerFirstPort = $nuevo"

# ArchiCAD debe estar cerrado
$proc = Get-Process -Name Archicad -ErrorAction SilentlyContinue
if ($proc) {
    Write-Host "ARchiCAD ESTA ABIERTO (PID $($proc.Id -join ', '))." -ForegroundColor Yellow
    Write-Host "Guarda el proyecto y cierra ArchiCAD antes de continuar, o el cambio se"
    Write-Host "sobrescribira al salir."
    $resp = Read-Host "Continuar de todos modos? [s/N]"
    if ($resp -notmatch '^(s|si|y|yes)$') { exit 0 }
}

Set-ItemProperty -Path $ruta -Name $valor -Value "$nuevo"
$verif = (Get-ItemProperty -Path $ruta -Name $valor).$valor
if ($verif -eq "$nuevo") {
    Write-Host "OK: HTTPServerFirstPort = $verif (anterior: $actual)" -ForegroundColor Green
    Write-Host ""
    Write-Host "Siguientes pasos:"
    Write-Host "  1. Abre ArchiCAD (su servidor JSON/Live Connection escuchara en $nuevo)."
    Write-Host "  2. En Grasshopper (panel de conexion de Tapir / Live Connection):"
    Write-Host "     puerto $nuevo (el panel acepta la secuencia numerica; host localhost)."
    Write-Host "  3. AutoClaw se queda en 19723 -> ya no interfiere."
    Write-Host "  4. archicad_bridge.py: usar --puerto $nuevo."
} else {
    Write-Host "ERROR: la verificacion fallo ($verif). Reintenta." -ForegroundColor Red
}
