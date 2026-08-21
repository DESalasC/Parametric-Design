# Próxima sesión - puntos para continuar (2026-08-20)

Handoff para retomar en una nueva sesión. Estado consolidado tras el cierre
de inconsistencias y la preparación de Morphs funcionales.

## Estado vigente (versiones)
- F1 NORMATIVA **v08**, LADOS **v06**, canvas **F1_Contexto_Base-Editado_v02**.
- F3_VOLUM_GENERADOR **v08** (salidas `usos_pisos` + `circulacion_pisos`/
  `servicios_pisos`/`losas_pisos`/`nucleo_pisos`), F3_MORPH_ATRIBUTOS **v01.1**
  (atributos BIM + `layers_json`).
- F0_LOAD_PROYECTO **v01.3**, F0_STORIES **v01**, F2 motores **v03**.
- `usos-por-sector.json` **v02** (usos por Área de Actividad, 4 categorías).
- Suite: **248 passed**.
- Linaje: versiones viejas de F1 en `src/fase-1-contexto/_legacy/` (las que tienen
  guard "fuente" mantienen copia idéntica en el directorio activo).

## Terminado en esta sesión (2026-08-20)
- 6 inconsistencias resueltas (test roto, drift v07→v08, docstring, `_legacy` F1,
  contradicción `docs/`, derivado `gfa-gh.json` untrack).
- `_legacy` reorganizado como archivo pasivo.
- Fix de encoding (lectura JSON tolerante utf-8→latin-1) en `F1_ETAPA1_CONTEXTO_v02`.
- `F3_MORPH_ATRIBUTOS_v01.1`: id + building_material + structural_function +
  position + renovation_status + `layers_json`.
- `F1_LAYERS_XML_v02`: entrada `json_path`.
- Backup del canvas `.gh/.ghx` commiteado.

## Bloqueado / pendiente (orden sugerido)
1. **Canvas (manual, Rhino)**: cambiar type hints de los inputs de #211 (Morph
   Settings) y #207 (F0_STORIES) a **Text** para resolver "Data conversion failed
   Text→Layer / Text→Story".
2. **Cablear `layers_json`** (F3_MORPH_ATRIBUTOS) → `F1_LAYERS_XML_v02`
   (`json_text` o `json_path`) para generar el XML de capas de los morphs antes de
   crearlos.
3. **GFA**: regenerar en Rhino (826.58 vs 1186.87 m²) y revisar anomalías (vecinos
   0 lados, antejardín default 3.0 m, sin lado posterior).
4. **F2**: validar `pago_parcial_pct` contra un caso real.
5. **Fases posteriores**: F4 Ladybug (ambiental), F5 BIM (inyección).
6. **Zonas** (siguiente fase): crear "Zonas" desde Grasshopper con 4 niveles de
   jerarquía (nivel → unidad vivienda/comercio → habitaciones → …), en paralelo a
   los Morphs ya funcionales.

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib/type hints); componente "Script",
  no "Python 3 Script".
- `_legacy` es archivo pasivo: no referenciarlo desde tests/código activo.
- Lectura de JSON en GHPython: bytes crudos + `utf-8` con fallback `latin-1`.
- Capas con estándar GuBIMclass (`data\GuBIMclass_Layers_v3.xml`); niveles con
  nombres reales de ArchiCAD.
- Derivados (`data/pot-cache/*`, `gfa-gh.json`, resultados F2/F3, `anexo5_pdf_extract.txt`)
  NO se commitean.
- `servidor.py` NO calcula GFA; lo hace la cadena Grasshopper (F0 → NORMATIVA_v08 →
  F1_EXPORTAR_GFA_v02).
