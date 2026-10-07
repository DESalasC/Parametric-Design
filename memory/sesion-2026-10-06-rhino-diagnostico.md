# Sesión 2026-10-06 (noche) — Diagnóstico de cuelgues de Rhino en la estación + preparación de mantenimiento

## Resumen
Pedido del operador: diagnosticar Rhino («se queda bloqueado» + mensaje de error «al inicio» relacionado con .NET), preparar el mantenimiento del equipo con un script listo para ejecutar, y cierre de sesión (vault + memoria + commit de respaldo). Resultado: dos hallazgos distintos claramente separados, plan de mantenimiento con script probado, y cierre registrado.

## Hallazgos
1. **Cuelgues de Rhino (capturados en vivo, 21:52–22:08).** Proceso «No responde» con **hilo al 100 % CPU** + **tormenta de ~200–250 conexiones TCP** hacia `127.0.0.1:19724` (Live Connection/Tapir de ArchiCAD); editor Python de GH colgado (LADOS v06.8); se recuperó solo; ~205 sockets quedaron abiertos. Patrón: bucle de reconexión del puente GH↔ArchiCAD.
2. **Crashes «de .NET».** 11 terminaciones de `Rhino.exe` en días recientes por bug de **WebView2 WPF** en el finalizador (`InvalidCastException` → `HwndHost.Finalize`); último 21:34:49. El .NET del sistema está sano → no hay nada que reparar en .NET; acción = actualizar Rhino + reportar a McNeel.
3. **Estación.** 60 días: 20 Kernel-Power 41, 5 BSOD, 70 WHEA; discos E: 1 %, F: 0 %, G: 6 % libres; disco WD5000AAKS (ID 2) con 28 errores de lectura no corregidos; RTX 4070 Ti (driver ago-2026); 64 GB DDR5.
4. **Puertos.** AutoClaw `127.0.0.1:19723`; portproxy `192.168.100.1:19723 → 127.0.0.1:19724` intacto (fix de la tarde); ArchiCAD en 19724; MCP de Rhino en 1999. Al cierre: Rhino/ArchiCAD cerrados por el usuario; backup mínimo F: en curso.

## Entregables
- **Script**: `D:\Work\Scripts\mantenimiento-equipo.ps1` — fases `Diagnostico` / `Reparacion` (DISM+SFC+chkdsk /scan); `-RhinoDumps` (WER LocalDumps → `D:\Work\CrashDumps\Rhino`); `-PruebaMemoria` (mdsched). Probado: fase Diagnóstico OK (logs en `D:\Work\Scripts\logs\`).
- **Informe**: `D:\Users\Work\.openclaw-autoclaw\workspace\diagnosticos\2026-10-06-diagnostico-rhino.md` + capturas.
- **Vault**: acta de cierre + procedimiento + 2 lecciones + diario + mapa actualizados.

## Pendientes
- Ventana de mantenimiento (Reparacion + mdsched); drivers chipset/GPU; BIOS.
- Actualizar Rhino; reportar WebView2 a McNeel; capturar el mensaje exacto si reaparece.
- Vigilar cuelgues (si repiten: `-RhinoDumps` + aislar Raven/Tapir).
- Gestionar discos E/F/G; backup mínimo F:; seguimiento del disco con errores de lectura.
- (Proyecto, arrastre) patch canvas v13.1 por el operador; validación offline; integración F3; pendientes 10-05.

## Referencias
- Vault: [[2026-10-06-acta-sesion-cierre-rhino-diagnostico]] · [[2026-10-06-procedimiento-mantenimiento-equipo]] · [[2026-10-06-leccion-cuelgue-de-rhino-bucle-conexiones-gh-archicad]] · [[2026-10-06-leccion-crash-de-rhino-por-webview2-finalizador]]
- Commits: vault + Scripts (selectivo) + proyecto; backup `backup_projects.ps1 -Real`.
