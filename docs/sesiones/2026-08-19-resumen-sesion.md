# Resumen de sesión - 2026-08-19

**Tema:** Round-trip ArchiCAD ↔ Grasshopper (ida: Stories/Capas/Zonas) y conexión Tapir.

## Contexto
Continuación del sistema round-trip. Foco en el "ida": crear Stories/Capas/Zonas en
ArchiCAD desde Grasshopper, y conectar el plugin Tapir (ENZYME-APD) para disparar
comandos (SetStories, CreateWall, etc.).

## Errores encontrados
1. **Tapir "Failed to connect to Archicad".** Los componentes Tapir no conectan,
   aunque la Live Connection sí dibuja morphs.
2. **Confusión Tapir vs Live Connection** en la documentación del vault (dos
   mecanismos distintos).
3. **Falta runtime Python 3.7+.** La JSON API de ArchiCAD responde en 19724 pero
   devuelve `command not found` para todo (incluso `GetProjectInfo`), porque la
   "Python Connection" exige Python 3.7+ instalado, y no lo está.
4. **`F3_StorySync_v01.py` sin dependencia** (`archicad` no instalado vía pip).
5. **Puerto 19723 ocupado por AutoClaw** (app de escritorio) → ArchiCAD se corre
   al 19724 (esperado, pero confunde al diagnosticar).

## Modificaciones solicitadas
1. Escribir `F0_STORIES_v01.py` (helper de Stories desde `programa-areas.json`).
2. Verificar la última versión de Tapir y buscar el error en issues.
3. Instalar Python 3.7+ (pendiente del operador).

## Lecciones aprendidas
1. Tapir (JSON/Python API) ≠ Live Connection (AC_*): la Live Connection no necesita
   Python; Tapir sí (Python 3.7+).
2. La JSON API escanea 19723→19743 y se corre sola si el puerto está ocupado.
3. `command not found` en la JSON API = capa de comandos no cargada (Python ausente),
   no un problema de red/firewall/puerto.
4. Verificar dependencias antes de citar un script como funcional.

## Soluciones entregadas
- `src/orquestador/F0_STORIES_v01.py` (GHPython, IronPython 2.7): deriva
  `story_names` / `story_elevations` / `show_on_sections` desde `programa-areas.json`
  (mismo `altura_z` que F3) para Tapir `SetStories`. Compilado y probado.
- Diagnóstico completo del fallo de conexión (causa raíz: Python 3.7+ faltante).

## Pendientes
1. Instalar Python 3.7+ (64-bit; 3.11 o 3.12).
2. Re-testear JSON API en 19724 (GetProjectInfo debe dejar de dar "not found").
3. Reintentar Tapir (SetStories) → prueba de 1 piso (offset ~-4000 mm).
4. Cableado directo Home Story + Layer en Settings de Morph/Slab/Roof/Zone.
5. Fases P1-P5 del round-trip (materialización, zonas, skills, overrides, ambiental).
6. Commit de `F0_STORIES_v01.py` (sin commitear).
7. Plan B: pre-crear Stories a mano + Live Connection para el resto.

## Referencias de diagnóstico (evidencia)
- Tapir GH plugin = 1.5.8 (última release), vía Rhino package manager.
- Add-On `TapirAddOn_AC29_Win.apx` en `Add-Ons\Local` de ArchiCAD 29.
- JSON API responde `HTTP 200` en 19724, pero `command not found` (code 2002) para
  `GetProjectInfo`, `GetElementTypes` y `TapirCommand.*`.
- AutoClaw (PID 14064) escucha `127.0.0.1:19723`; ArchiCAD escucha `0.0.0.0:19724`.
- Fuente Graphisoft: "Python Connection requires only the installed Python
  environment (version 3.7 or above) and a running Archicad instance (24+)".
