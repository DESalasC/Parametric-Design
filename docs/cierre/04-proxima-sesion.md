# Próxima sesión — puntos para continuar (2026-08-18)

Handoff para retomar en una nueva sesión. Estado consolidado del cierre.

## Estado vigente (versiones)
- F1 NORMATIVA **v08**, LADOS **v06**, canvas **F1_Contexto_Base-Editado_v02**.
- F3_VOLUM_GENERADOR **v07.25** (salida `usos_pisos`), F3_MORPH_ATRIBUTOS **v01**.
- F0_LOAD_PROYECTO **v01.3**, F2 motores **v03**.
- `usos-por-sector.json` **v02** (usos por Área de Actividad, 4 categorías).
- Suite: **240 passed**.

## Terminado en esta sesión
- Usos por sector → resueltos por Área de Actividad (P/C/R/prohibido); servidor + UI actualizados.
- `F3_VOLUM_GENERADOR_v07.25` con salida `usos_pisos`.
- `F3_MORPH_ATRIBUTOS_v01` (morph-manifest.json: Morph → Layer GuBIMclass + Story).
- `EJECUCION_TAPIR.md` (3 vías de disparo del canvas).
- `mix_usos` → escenario D_MIXTO.

## Bloqueado / pendiente (orden sugerido)
1. **Cablear F3 → Morph**: `usos_pisos` (F3) → entrada `pisos` de `F3_MORPH_ATRIBUTOS_v01`;
   luego Paso 3 (asignar Story/Layer en ArchiCAD vía Tapir/Live Connection). Verificar si
   el paquete `archicad` ac29 soporta Modify (F3_StorySync_v01 es read-only).
2. **GFA**: regenerar en Rhino (826.58 vs 1186.87 m²) y revisar anomalías (vecinos 0 lados,
   antejardín default 3.0 m, sin lado posterior).
3. **F2**: validar `pago_parcial_pct` contra un caso real.
4. **Fases posteriores**: F4 Ladybug (ambiental), F5 BIM (inyección).

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib); componente "Script", no "Python 3 Script".
- Capas con estándar GuBIMclass (`data\GuBIMclass_Layers_v3.xml`); niveles con nombres reales de ArchiCAD.
- Derivados (`data/pot-cache/*`, `gfa-gh.json`, resultados F2/F3, `anexo5_pdf_extract.txt`) NO se commitean.
- `servidor.py` NO calcula GFA; lo hace la cadena Grasshopper (F0 → NORMATIVA_v08 → F1_EXPORTAR_GFA_v02).
