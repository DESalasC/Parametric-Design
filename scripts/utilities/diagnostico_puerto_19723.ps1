# diagnostico_puerto_19723.ps1
# Diagnostica el conflicto del puerto 19723 (ArchiCAD Live Connection / Python API
# vs conector "ArchiCAD Live Connection" de AutoClaw). Uso:
#   powershell -ExecutionPolicy Bypass -File diagnostico_puerto_19723.ps1
#   powershell -ExecutionPolicy Bypass -File diagnostico_puerto_19723.ps1 -Liberar
#
# HALLAZGO (2026-08-15): ArchiCAD escucha en 0.0.0.0:19723 (todas las interfaces)
# y AutoClaw en 127.0.0.1:19723 (solo loopback). Cuando el Live Connection de GH
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
Write-Host "=== SOLUCION DEFINITIVA (investigada 2026-08-15) ===" -ForegroundColor Cyan
Write-Host "En ArchiCAD 29 NO hay UI para el puerto (la Python palette solo configura"
Write-Host "el interprete). El puerto del servidor CommandConnection (Python/JSON API y"
Write-Host "Live Connection comparten el mismo servidor) vive en el REGISTRO:"
Write-Host "  HKCU\Software\Graphisoft\Archicad\Archicad 29.0.0 INT R1\CommandConnection"
Write-Host "  HTTPServerFirstPort = 19723  (REG_SZ) | HTTPServerPortCount = 100"
Write-Host ""
Write-Host "Pasos (script: cambiar_puerto_archicad.ps1 en scripts/utilities):"
Write-Host "  1. Cierra ArchiCAD (el registro se lee al arrancar)."
Write-Host "  2. Cambia HTTPServerFirstPort a 19724 (script con backup automatico)."
Write-Host "  3. Abre ArchiCAD -> escuchara en 19724."
Write-Host "  4. Grasshopper (panel de Tapir / Live Connection): puerto 19724."
Write-Host "  5. AutoClaw se queda en 19723 -> nunca mas interfiere."
Write-Host "  6. archicad_bridge.py: --puerto 19724."
Write-Host ""
Write-Host "Verificacion con ArchiCAD abierto:"
foreach ($p in @(19723, 19724)) {
    $res = Test-NetConnection -ComputerName 127.0.0.1 -Port $p -WarningAction SilentlyContinue
    $ok = if ($res.TcpTestSucceeded) { "CONECTA" } else { "rechazado" }
    Write-Host ("  127.0.0.1:{0} -> {1}" -f $p, $ok)
}
Write-Host "Esperado: 19723 = AutoClaw (irrelevante) | 19724 = ArchiCAD (CONECTA)"

if ($Liberar) {
    foreach ($l in $lineas) {
        $proc = Get-Process -Id $l.OwningProcess -ErrorAction SilentlyContinue
        if ($proc -and $proc.ProcessName -match "AutoClaw") {
            $resp = Read-Host "Matar PID $($l.OwningProcess) (AutoClaw) para liberar el puerto? [s/N]"
            if ($resp -match '^(s|si|y|yes)$') {
                taskkill /PID $l.OwningProcess /F
                Write-Host "Puerto $puerto liberado (AutoClaw se relanza al reactivar el conector)." -ForegroundColor Green
            }
        }
    }
}
