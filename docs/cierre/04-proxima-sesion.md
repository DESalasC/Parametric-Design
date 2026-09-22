# Próxima sesión - puntos para continuar (2026-08-23, noche)

Handoff para retomar. Estado consolidado tras el cierre de la sesión (noche):
cardinal, `via_no_frontal`, puerto 19723 y diagnóstico del lote AAA0240ZXJH.

## Estado vigente (versiones)
- F0_LOAD_PROYECTO **v01.4** (emite `frente_override_json`), F0_STORIES v01.
- F1 NORMATIVA **v08.3** (via_no_frontal cuenta como vía en esquina), LADOS **v06.2**
  (cardinal + guard ancho vía), PATIO **v02.1**.
- `fetch-urban-context-v6.py` fusiona `data/pot-bogota/norma-override.json` en
  `pot_data` (gana sobre la geobase).
- Orquestador: panel "Completar norma" + `GET/POST /api/norma-override`; frente
  `via_no_frontal` disponible en el SVG y en los FRENTES.
- `scripts/utilities/verificar-gfa.py` y `diagnostico_puerto_19723.ps1 -Liberar`.
- Suite: **272 passed**.

## Terminado en esta sesión (2026-08-23, tarde + noche)
- Override de norma por CHIP + diagnóstico GFA (tarde).
- Cardinal por lado en LADOS v06.2; frente `via_no_frontal`; esquina cuenta
  `via_no_frontal` como vía (v08.3).
- Docs del conflicto de puerto 19723 (CLAUDE.md, MANUAL, scripts) + `-Liberar`
  corregido (reporta acceso denegado real).
- Cleanup git: 24.460 derivados des-versionados.

## Pendiente (orden sugerido)
1. **Re-exportar F1 al .gh/.ghx**: el canvas aún corre v06.1/v08.1 (los .py ya son
   v06.2/v08.3). Editar el GHPython no actualiza el canvas.
2. **Frame de coordenadas (ROOT CAUSE del GFA)**: `ep:41.26m`, `via 41.7m`,
   Ocup 1,6 m², GFA 27,9 m² → vía/EP/vecinos en coordenadas distintas al lote
   (SIRGAS global vs local). Validar en Rhino/ArchiCAD que vías/EP/vecinos usen el
   MISMO origen local del lote (regla de desplazamiento global, CLAUDE.md 6 y 19).
3. **Área del orquestador 450 vs 99,72** (el contexto JSON trae 99,72 correcto);
   verificar chip por defecto AAA0127AZPA y la sección que muestra el área.
4. **Codificación**: decodificar entidades HTML (`&iacute;`) en sección 2 normativa
   y normalizar mojibake en labels (`Antejard�n`, `Segǧn`) de .py/.md/.json.
5. **Nicknames en LADOS/NORMATIVA**: incluir los nombres del orquestador por lado
   para validar la clasificación (hoy: 2 frontales auto vs 1 frontal + 1
   via_no_frontal ground-truth).
6. **Parámetros financieros por CHIP** (`parametros_AAA0240ZXJH_*`), con el valor
   del lote como primer INPUT (no output) y valores de mercado editables.
7. **Persistencia por CHIP**: restaurar 1b-1c + normativa al re-seleccionar el mismo
   CHIP.
8. **1b-1c**: lista de vecinos solo en "+Agregar" (el SVG ya resuelve la selección).
9. F2: `recursos_disponibles`, `saldo`, `financiacion_saldo[]`, acabados, multi-escenario.
10. F3 → Zonas (no Morphs) para Ladybug. OCR de la ficha 041 Muzú (si lo exige curaduría).

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib/type hints); entradas SIEMPRE
  `globals().get()`.
- Derivados (`pot-cache/*`, `gfa-gh.json`, `proyectos/`) **no se commitean**;
  `norma-override.json` y `data/predios/<CHIP>/proyecto.json` **sí**.
- El **override de norma** completa lo que la geobase no trae y **gana sobre la
  geobase**; `upz`/`tratamiento` se dejan fuera.
- Matching orquestador↔canvas por **cardinal** (normal saliente), no por índice.
- El .gh/.ghx **embebe el código**: tras editar un .py, re-exportar el GHPython.
- Consola PowerShell corrompe acentos: editar/leer con `encoding="utf-8"`.
- Para operar el canvas: cerrar AutoClaw → reiniciar → abrir ArchiCAD → Grasshopper
  → reabrir AutoClaw. La Live Connection solo conecta por **19723** (19724 solo API
  Python). `diagnostico_puerto_19723.ps1 -Liberar` solo mata AutoClaw si se ejecuta
  como Administrador.

## Notas del vault (esta sesión)
- `memory/2026-08-23.md` (workspace) + `MEMORY.md` (lecciones durables).
- `docs/sesiones/2026-08-23-resumen-sesion.md` (tarde + noche).


---

## Actualización 2026-08-23 (madrugada, 22:17–23:17)

Handoff posterior al cierre "noche". Se resolvieron varios pendientes y se introdujo la
**regla del canvas (archivos ACTIVOS literales `CHIP`/`CASO`)**.

### Resuelto (de la lista anterior)
- **Área 450 → 99,72**: `_area_shoelace_local` desde `vertices_3d_local` en contexto y financiero.
- **Codificación**: entidades HTML (`&iacute;`) corregidas en la sección 2 del formulario.
- **Parámetros financieros por CHIP**: área real como INPUT + valores de mercado editables +
  "Guardar financiero" (genera `parametros_<CHIP>_mercado2026.json`).
- **Persistencia por CHIP**: vecinos/frentes se guardan y recargan (`POST /api/vecinos-por-lado`).
- **1b·1c**: lista de vecinos colapsada tras "Detalle de vecinos (N)".
- `n_vertices`/`perímetro` corregidos.

### Nuevo en esta sesión
- Activos literales `CHIP-contexto.json`, `CHIP-vecinos-por-lado.json`, `casos/CASO/`.
- `POST /api/activar-chip` (auto al cambiar CHIP) y `POST /api/activar-caso` (auto al cambiar caso).
- Exportación GFA por flag `gfa-export-flag.json` (`true` → exporta → `false`),
  `F1_EXPORTAR_GFA_v02.py` v02.2.
- Docs: vault `10-arquitectura/instructivo-cableado-canvas.md` y `10-arquitectura/archivos-intercambio-canonicos.md`,
  `src/orquestador/ARCHIVOS_INTERCAMBIO.md`.

### Pendiente (orden sugerido)
1. **Re-exportar GHPython en el canvas** (`F1_EXPORTAR_GFA_v02` y el resto) — el `.gh`/`.ghx`
   embebe el código; los `.py` ya están actualizados.
2. **Frame de coordenadas** (ROOT CAUSE ancho de vía 41,7 m → antejardín 7 m): validar
   vías/EP/vecinos en el MISMO origen local del lote.
3. **Nicknames** en LADOS/NORMATIVA (`nombre`/`cardinal_label` por lado).
4. **Activo `proyecto.json`** (espejo literal para `F0_LOAD_PROYECTO.ruta_json`).
5. F3 → Zonas (no Morphs) para Ladybug; OCR ficha 041 Muzú (si lo exige curaduría).
6. F2: `recursos_disponibles`, `saldo`, `financiacion_saldo[]`, acabados, multi-escenario.

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib/type hints); entradas SIEMPRE
  `globals().get()`; re-exportar el componente "Script" tras editar el `.py`.
- Dentro del canvas: nombres literales `CHIP`/`CASO`; el orquestador sobreescribe el activo.
- Derivados (`pot-cache/*`, `gfa-gh.json`, `proyectos/`, `casos/CASO/`, `gfa-export-flag.json`)
  **no se commitean**; sí `norma-override.json`, `financiero-override.json`, `.py` y docs.
