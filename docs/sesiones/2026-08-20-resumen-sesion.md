# Resumen de sesión - 2026-08-20

**Tema:** Cierre de inconsistencias + reorganización `_legacy` + preparación de Morphs funcionales.

## Contexto
Revisión completa del contexto del proyecto, resolución de 6 inconsistencias de
código/documentación, fix de encoding en Fase 1 y atributos BIM para `F3_MORPH_ATRIBUTOS`.

## Errores encontrados
1. **Test roto.** `tests/test_f3_volum_v07_fuente.py` apuntaba a
   `src/fase-3-masa/F3_VOLUM_GENERADOR_v07.py`, ya movido a `_legacy` → FileNotFoundError.
2. **Drift v07 → v08.** README, CLAUDE y `run_pipeline_v01.py` citaban
   `F3_VOLUM_GENERADOR_v07` (v07.24); el vigente es v08.
3. **Encoding.** `F1_ETAPA1_CONTEXTO_v02`: `'unknown' codec can't decode byte 0xf3`
   (ó en cp1252 leído como utf-8). Causa: JSON guardado fuera de la ruta UTF-8.
4. **Type hints.** #211 (Morph Settings) y #207 (F0_STORIES) reciben Text en inputs
   tipados Layer/Story → "Data conversion failed".
5. **Derivado rastreado.** `data/fase-2-demanda/AAA0127AZPA-gfa-gh.json` versionado
   pese a ser derivado.

## Modificaciones solicitadas
1. Resolver las 6 inconsistencias.
2. `_legacy` como archivo pasivo (copias en ambos lados, no apuntar tests a `_legacy`).
3. Commit `.gh/.ghx` por precaución.
4. Corregir codificación JSON.
5. Atributos BIM en `F3_MORPH_ATRIBUTOS` (Building_Material, ID, Structural_Functions,
   Position, Renovation_Status).
6. `F1_LAYERS_XML_v02` con entrada `.json`.
7. Funcionalizar Morphs primero; luego Zonas con 4 niveles de jerarquía.

## Lecciones aprendidas
1. `_legacy` pasivo; si un test pinea una versión vieja, copia en activo + copia en `_legacy`.
2. IronPython 2.7: lectura tolerante utf-8 → latin-1 para JSON.
3. Tests "fuente" pinean rutas; actualizarlos al mover archivos.
4. "Sucio" = sin commitear; "derivado" = generado (no versionar).

## Soluciones entregadas
- 6 fixes + `tests/test_f3_volum_v08_fuente.py` (guard v08).
- `_legacy`: 12 archivos solo en `_legacy`; 5 (LADOS v04/v05, NORMATIVA v06/v07,
  VOLUM_GENERADOR v07) en activo + `_legacy` idénticos.
- Lectura JSON tolerante en `F1_ETAPA1_CONTEXTO_v02` y `F1_LAYERS_XML_v02`.
- `F3_MORPH_ATRIBUTOS_v01`: id, building_material, structural_function, position,
  renovation_status + salida `layers_json` + `_enums` en manifest.
- `F1_LAYERS_XML_v02`: entrada `json_path`.
- `.gitignore`: `data/fase-2-demanda/*-gfa-gh.json`.
- Suite: **248 passed**.

## Pendientes de esta sesión
1. Cambiar type hints de #211/#207 a Text (manual en Rhino).
2. Cablear `layers_json` → `F1_LAYERS_XML_v02`.
3. Regenerar GFA en Rhino (826.58 vs 1186.87 m²) y revisar anomalías.
4. Validar `pago_parcial_pct` F2 contra caso real.
5. F4 Ladybug y F5 BIM.
6. Zonas con 4 niveles de jerarquía (nivel → unidad vivienda/comercio → habitaciones).

## Commits
- `0fda2ca8` fix: drift F3 v07->v08, guard v08, legacy F1 y untrack gfa-gh
- `db84f53` chore(rhino): backup canvas F1_Contexto_Base-Editado_v02
- `0068005f` fix(f1-f3): lectura JSON tolerante, atributos BIM por morph y json_path
