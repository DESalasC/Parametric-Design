# diagnostico_puerto_19723.ps1
# Diagnostica el conflicto del puerto 19723 (ArchiCAD Live Connection / Python API
# vs conector "ArchiCAD Live Connection" de AutoClaw). Uso:
#   powershell -ExecutionPolicy Bypass -File diagnostico_puerto_19723.ps1
#   powershell -ExecutionPolicy Bypass -File diagnostico_puerto_19723.ps1 -Liberar
#
# HALLAZGO (2026-08-15): ArchiCAD escucha en 0.0.0.0:19723 (todas las interfaces)
# y AutoClaw en 127.0.0.1:19723 (solo loopback). Cuando el Live Connection de GH
# AVISO 2026-08-23: mover a 19724 SOLO sirve para la JSON/Python API (paquete 'archicad').
# La Live Connection de Grasshopper (AC_*) solo conecta por 19723 y NO respeta este cambio;
# para el canvas usar diagnostico_puerto_19723.ps1 -Liberar o cerrar/reabrir AutoClaw.
# reconecta a "localhost" recibe a AutoClaw, no a ArchiCAD. SOLUCION: conectar GH
# a la IP LAN (p.ej. 192.168.1.2) en vez de localhost -> la conexion enruta al
# socket 0.0.0.0 de ArchiCAD y AutoClaw nunca la ve (direcciones diferentes).

param([switch]$Liberar)

$puerto = 19723
Write-Host "=== Diagnostico puerto $puerto ===" -ForegroundColor Cyan

# --- IP LAN recomendada ---
$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {
    $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.254.*" -and
    $_.PrefixOrigin -ne "WellKnown" } | Select-Object -First 1).IPAddress
if (-not $ip) { $ip = "127.0.0.1" }
Write-Host "IP LAN de esta maquina (usar esta en el Host del Live Connection): $ip" -ForegroundColor Yellow

# --- Quien escucha ---
$lineas = Get-NetTCPConnection -LocalPort $puerto -ErrorAction SilentlyContinue
if (-not $lineas) {
    Write-Host "OK: nadie escucha en $puerto. ArchiCAD debe estar abierto con el add-on habilitado." -ForegroundColor Green
} else {
    $proc_archicad = $false
    $proc_autoclaw = $false
    foreach ($l in $lineas) {
        $proc = Get-Process -Id $l.OwningProcess -ErrorAction SilentlyContinue
        $nombre = if ($proc) { $proc.ProcessName } else { "PID $($l.OwningProcess)" }
        if ($nombre -match "Archicad") { $proc_archicad = $true }
        if ($nombre -match "AutoClaw") { $proc_autoclaw = $true }
        Write-Host ("{0,-16} {1}  -> {2}" -f $l.LocalAddress, $l.State, $nombre)
    }
    if ($proc_archicad -and $proc_autoclaw) {
        Write-Host "CONFLICTO: ArchiCAD (0.0.0.0) y AutoClaw (127.0.0.1) ambos en $puerto." -ForegroundColor Red
        Write-Host "Conecta el Live Connection de GH a la IP LAN ($ip), NO a localhost."
    } elseif (-not $proc_archicad) {
        Write-Host "ArchiCAD NO esta escuchando: solo AutoClaw. El Live Connection no podra conectar" -ForegroundColor Red
        Write-Host "hasta que ArchiCAD este activo. Al reconectar, usa el Host $ip (no localhost)."
    } else {
        Write-Host "ArchiCAD activo y AutoClaw escuchando en loopback: conectar GH por $ip." -ForegroundColor Green
    }
}

# --- Test TCP a ambas direcciones (con ArchiCAD abierto) ---
Write-Host ""
Write-Host "--- Test de conexion (ArchiCAD debe estar abierto) ---"
foreach ($dest in @("127.0.0.1", $ip)) {
    $res = Test-NetConnection -ComputerName $dest -Port $puerto -WarningAction SilentlyContinue
    $ok = if ($res.TcpTestSucceeded) { "CONECTA" } else { "rechazado" }
    Write-Host ("{0}:{1} -> {2}" -f $dest, $puerto, $ok)
}

Write-Host ""
Write-Host "RECOMENDACION (config del Live Connection de Tapir en Grasshopper):"
Write-Host "  Host: $ip  |  Puerto: $puerto (FIJO, no cambiarlo)"
Write-Host "Asi la reconexion tras inactividad va siempre a ArchiCAD y AutoClaw"
Write-Host "(solo loopback) no la intercepta."
Write-Host ""
Write-Host "=== ESTADO REAL (actualizado 2026-08-23) ===" -ForegroundColor Cyan
Write-Host "La Live Connection de GH (AC_*) SOLO conecta por 19723 (localhost)."
Write-Host "Mover ArchiCAD a 19724 (cambiar_puerto_archicad.ps1) SOLO sirve para la"
Write-Host "JSON/Python API (paquete 'archicad', F3_StorySync), NO para el canvas."
Write-Host "AutoClaw escritorio ocupa 127.0.0.1:19723 (hardcodeado, sin config)."
Write-Host ""
Write-Host "WORKAROUND REAL para operar el canvas:"
Write-Host "  1. Cierra AutoClaw (o -Liberar desde una consola Administrador) y opera ArchiCAD/GH."
Write-Host "  2. Al reabrir, orden: ArchiCAD -> Grasshopper -> AutoClaw (conexion fragil)."
Write-Host "  3. Soporte de AutoClaw (ticket abierto): pedir que 19723 sea configurable."
Write-Host ""
Write-Host "Verificacion con ArchiCAD abierto:"
foreach ($p in @(19723, 19724)) {
    $res = Test-NetConnection -ComputerName 127.0.0.1 -Port $p -WarningAction SilentlyContinue
    $ok = if ($res.TcpTestSucceeded) { "CONECTA" } else { "rechazado" }
    Write-Host ("  127.0.0.1:{0} -> {1}" -f $p, $ok)
}
Write-Host "Esperado (Live Connection): 19723 = ArchiCAD (CONECTA); si AutoClaw lo tiene, cerrar/liberar AutoClaw."

if ($Liberar) {
    foreach ($l in $lineas) {
        $proc = Get-Process -Id $l.OwningProcess -ErrorAction SilentlyContinue
        if ($proc -and $proc.ProcessName -match "AutoClaw") {
            $resp = Read-Host "Matar PID $($l.OwningProcess) (AutoClaw) para liberar el puerto? [s/N]"
            if ($resp -match '^(s|si|y|yes)$') {
                $ok = $false
                taskkill /PID $l.OwningProcess /F 2>&1 | Out-Null
                $ok = ($LASTEXITCODE -eq 0)
                if (-not $ok) {
                    try {
                        Stop-Process -Id $l.OwningProcess -Force -ErrorAction Stop
                        $ok = $true
                    } catch {
                        $ok = $false
                    }
                }
                if ($ok) {
                    Write-Host "Puerto $puerto liberado (AutoClaw se relanza al reactivar el conector)." -ForegroundColor Green
                } else {
                    Write-Host "ERROR: no se pudo terminar el PID $($l.OwningProcess) (acceso denegado)." -ForegroundColor Red
                    Write-Host "  Causa: AutoClaw corre con mas privilegios que esta consola." -ForegroundColor Yellow
                    Write-Host "  Opciones: 1) cierra AutoClaw desde su interfaz (forma confiable)," -ForegroundColor Yellow
                    Write-Host "            2) ejecuta este script 'como Administrador' y repite -Liberar." -ForegroundColor Yellow
                }
            }
        }
    }
}
