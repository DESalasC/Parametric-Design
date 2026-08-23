# Próxima sesión - puntos para continuar (2026-08-23, tarde)

Handoff para retomar. Estado consolidado tras el cierre de la sesión (override de
norma + diagnóstico GFA).

## Estado vigente (versiones)
- F0_LOAD_PROYECTO **v01.4** (emite `frente_override_json`), F0_STORIES v01.
- F1 NORMATIVA **v08.2**, LADOS **v06** (+esquina), PATIO **v02.1**.
- `fetch-urban-context-v6.py` fusiona `data/pot-bogota/norma-override.json` en
  `pot_data` (gana sobre la geobase).
- Orquestador: panel "Completar norma" + `GET/POST /api/norma-override`.
- `scripts/utilities/verificar-gfa.py` (chequeo post-run del GFA).
- Suite: **267 passed**.

## Terminado en esta sesión (2026-08-23, tarde)
- **Override de norma** por CHIP (`norma-override.json`), editable en el orquestador.
- Diagnóstico del GFA: (1) conexión GH↔ArchiCAD (LADOS NoneType) y (2) rango
  erróneo "1" → "3" (→ 4 pisos).
- Reconciliación `tratamiento` + proyecto **EdificioDeysy** renombrado y completado.
- Fuente exacta de la norma (ficha + resolución 00865/2006), sin OCR.

## Pendiente (orden sugerido)
1. **Reabrir Live Connection GH↔ArchiCAD** (arregla huella 46,3 m²) y
   **re-ejecutar canvas F1** (ETAPA1 → LADOS → NORMATIVA → EXPORTAR_GFA).
2. **Reconectar `io_maximo`** en EXPORTAR_GFA ← NORMATIVA `io_maximo` (0,70), no
   `ic_maximo` (4 pisos). Es cableado de canvas, no código.
3. **Correr** `.venv\Scripts\python.exe scripts\utilities\verificar-gfa.py` → todo OK.
4. Validar anomalía de áreas de vecinos AAA0240ZXJH (Norte1 vs Norte2).
5. F2: `recursos_disponibles`, `saldo`, `financiacion_saldo[]`, acabados, multi-escenario.
6. Zonas de mercado + actualización periódica.
7. Cleanup git (`gh-definition-explorer`, `git rm --cached` derivados).
8. F3 → Zonas (no Morphs) para Ladybug.
9. OCR de la ficha 041 Muzú (solo si la curaduría lo exige).

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib/type hints); entradas SIEMPRE
  `globals().get()`.
- Derivados (`pot-cache/*`, `gfa-gh.json`, `proyectos/`) **no se commitean**;
  `norma-override.json` y `data/predios/<CHIP>/proyecto.json` **sí**.
- El **override de norma** (orquestador) completa lo que la geobase no trae y
  **gana sobre la geobase**; `upz`/`tratamiento` se dejan fuera (ya vienen bien).
- Matching orquestador↔canvas por **cardinal** (normal saliente), no por índice.
- Para operar el canvas: cerrar AutoClaw → reiniciar equipo → abrir en orden
  ArchiCAD/Grasshopper → reabrir AutoClaw (conexión frágil).

## Notas del vault (esta sesión)
- `10-arquitectura/2026-08-23-override-norma-gfa.md`
