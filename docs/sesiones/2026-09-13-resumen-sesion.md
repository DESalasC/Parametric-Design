# Resumen de sesión 2026-09-13 — Volumetrías de contexto 50 m (canvas ArchiCAD-GH)

> Cierre de sesión. Detalle completo en el vault:
> `D:\Work\NOTES\obsidian-vault\10-arquitectura\2026-09-13-resumen-sesion-contexto50-archicad.md`
> y ADR-016. Memoria del proyecto: `memory/sesion-2026-09-13.md`.

## Objetivo

Corregir `src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01a.py` para que produzca
las volumetrías de vecinos dentro del entorno ArchiCAD-Grasshopper
(canvas `gh-definitions/F1_Contexto_Base-Editado_v03.gh(x)`).

## Problemas encontrados y resolución

1. **0 volúmenes por entrada sin `unwrap()`** — entradas a prueba de GH
   (`unwrap`/`to_float`/`parse_bool`).
2. **Ruta canónica equivocada** (leía `CHIP-contexto.json` de ETAPA1, 74
   vecinos-lote) — corregida por el usuario; se creó el activo literal
   `data/pot-cache/CHIP-contexto50.json`.
3. **Escalado ×1000 anti-regla #11** — metros directos + aviso si el doc no
   está en metros.
4. **Deduplicación de vértices perdida** — restaurada (`TOL_CIERRE = 0.01`).
5. **Extrusión frágil (loft + capado)** — `Extrusion.Create` capado con la
   misma huella publicada (regla de oro).
6. **Alturas negativas** — anillos GIS horarios → normal −Z; se fuerza
   antihorario (shoelace).
7. **Andenes/anexos como volúmenes de 1 piso** — filtro área < 15 m² o
   compacidad > 6.0 (24 excluidos).
8. **Predio de referencia con volumen** — exclusión automática por
   contención en `lote_objetivo` (hermano `CHIP-contexto.json` + ancla;
   4 excluidos, id 004413004056...).
9. **Registro corrupto mataba el componente** — try/except por edificio.

## Resultado

- `Volumenes 66/94 | Excluidos: 4 predio objetivo, 24 andenes/menores |
  Alturas 3.8-19.0m | Fallbacks 0`.
- Canvas parcheado (`.ghx` + `.gh` regenerado con GH_IO.dll); backups
  `.bak-2026-09-13-1429/-1514/-1527`.
- Tests: `src/fase-1-contexto/tests/test_contexto50_build_v01a.py` — 11/11.
- Herramienta: `scripts/utilities/patch-ghx-contexto50-v03.py`.

## Pendientes

1. Verificación en vivo del usuario (reabrir canvas; mensaje esperado
   `Volumenes 66/94`).
2. Conectar `volumenes` → Create Elements (Morphs) del Live Connection y
   validar en ArchiCAD (capa `70-20-30_Volumetrias_vecinas`, z=0).
3. Arrastrados del 2026-09-11: reset AutoClaw vs `openclaw.json` (ADR-015),
   subagentes fcc-claude en vivo, idioma app, perfil Work, puerto 19723,
   filesystem MCP, agentes permanentes (pospuesto).

## Lecciones

Ver `memory/sesion-2026-09-13.md` y las notas del vault
(`2026-09-13-leccion-canvas-ghx-y-gh-io`,
`2026-09-13-leccion-volumetrias-contexto50-filtros`).
