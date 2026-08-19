# Resumen de sesión — 2026-08-18

Cierre de la feature "vecinos por lado" (clasificación de frentes, confirmación
del operador y mapeo a NORMATIVA) en DiseñoParametrico.

## Resumen de sesión — 2026-08-18 (cierre de vecinos por lado)

### Errores encontrados
1. **Confusión vecino vs vía/espacio público.** El clasificador original solo
   inspeccionaba `vecinos` e ignoraba `vias_oficiales` (42 geometrías) y
   `espacios_publicos` (12 polígonos), por lo que marcaba calles y zonas verdes
   como predios colindantes.
2. **Conversión errónea `empate_posterior_m → pisos`** (F0 v01.1). Se corrigió:
   `empate_posterior_pisos` y `empate_posterior_m` son INDEPENDIENTES (edificio
   vecino existente, sin relación con `floor_height_user`).
3. **Mapeo `Servicios → COMUNAL`** incorrecto; el vocabulario NORMATIVA exige
   `Servicios → EQUIPAMIENTO`.
4. **Falsos positivos por datos incompletos:** vía en esquina (Muzú occidente),
   vías faltantes del Eje_vial (La Candelaria oriente/occidente), zonas verdes
   guardadas como "vecinos" (El Prado occidente).
5. **Bug de parcheo propio:** al reemplazar `_a_normativa_vecinos` en F0, una
   ancla de fin incorrecta borró la lógica principal del script. Se revirtió con
   `git checkout` y se re-aplicó acotando solo la función.

### Modificaciones solicitadas
1. Distinguir `predio` de `via`/`espacio_publico` en la clasificación por lado.
2. `empate_posterior_pisos` y `empate_posterior_m` independientes (no convertir).
3. `Servicios → EQUIPAMIENTO` en `tipo_bonificacion`.
4. Confirmación del operador: el formulario debe variar según si los vecinos
   detectados corresponden a la realidad (plantilla dinámica).
5. Listado final + referencia de almacenamiento al cierre de cada respuesta.
6. Resumen de sesión guardado en el vault y en el repositorio.

### Lecciones aprendidas
1. La geobase del POT es imperfecta; la clasificación automática es **sugerencia**,
   no verdad. El override manual del operador es la solución correcta (no "arreglar"
   la geobase).
2. La lógica de mapeo se mantiene en 3 lugares (Python + IronPython + JS): exige
   tests unitarios para no divergir.
3. IronPython 2.7 (GHPython): sin f-strings, pathlib, type hints ni walrus.
4. Derivados (`data/pot-cache/*`) se regeneran y NO se commitean.
5. Al parchear con anclas de texto, validar que el ancla final no abarque código
   ajeno; ante error, revertir con git y re-aplicar acotado.

### Soluciones entregadas
- `vecinos_por_lado.py`: `frente` (predio/via/espacio_publico/libre) + sub-índices,
  `segmentos_vecinos`, `frente_override`, `a_normativa_vecinos_por_lado` (respeta
  `corresponde` + `vecinos_manuales`).
- `index.html` sección 1b: confirmación dinámica (`pendiente`/`confirmado`/`faltan`/
  `sobran`/`no_es_predio`) + alturas/pisos + botón "Generar JSON NORMATIVA".
- `F0_LOAD_PROYECTO_v01` v01.3: salida `vecinos_por_lado_json` (port IronPython).
- `CABLEADO_F0.md` v01.3 sincronizado en `src/orquestador/` y `gh-definitions/`.
- Suite de tests: **232 passed**.

### Pendientes de esta sesión
1. Cableado manual del canvas en Rhino (F0 → NORMATIVA_v08.vecinos_por_lado_json).
2. Validar en el navegador la confirmación dinámica y la entrada manual de vecino
   (caso real Muzú occidente: lado `via` que en realidad es `predio`).
3. (Persistente) Cargar listas definitivas de usos por sector (Sinupot / CU-5.4.x).
4. (Persistente) Validar `pago_parcial_pct` de F2 contra un caso real.

## Resumen de sesión — 2026-08-18 (cierre: usos por área de actividad + F3 v07.25 + follow-ups)

### Errores encontrados
1. **Anexo 5 ≠ cuadro de usos.** El PDF `anexo_no._5_manual_comunes_tramientos_urbanisticos_.pdf`
   (86 págs) es el "Manual de Normas Comunes para Tratamientos Urbanísticos"; NO trae la
   tabla principal/complementario/prohibido. Esa tabla está en el cuerpo del Decreto 555
   (Art. 233–243) y se leyó de `LIBRARIES/POT_Bogota/Marco normativo (Art. 233-243).md`.
2. **Resolver usos por UPZ era un aproximado.** La clave normativa es el ÁREA DE ACTIVIDAD
   (P/C/R/prohibido), no la UPZ. Por eso EL PRADO estaba `pendiente-usos`.
3. **3 categorías insuficientes.** El cuadro tiene 4 niveles (principal/complementario/
   restringido/prohibido); el modelo viejo confundía "restringido" con "prohibido".
4. **`servidor.py` NO calcula GFA.** Cadena real: forma → `proyecto.json` → `F0_LOAD_PROYECTO`
   → canvas `NORMATIVA_v08` → `F1_EXPORTAR_GFA_v02` → `gfa-gh.json` → `_calcular_f2`.
   GFA actual 826.58 m² (antes 1186.87); anomalías: "0 lados/0 vecinos", antejardín default 3.0 m, sin lado posterior.
5. **Fuente/docstring desactualizados en `F1_EXPORTAR_GFA_v02`** (`v00`→`v02`, refs `v04`→`v08`).

### Modificaciones solicitadas
1. Actualizar usos por sector desde fuente oficial (cuadro de usos del suelo).
2. Corregir fuente/docstring de `F1_EXPORTAR_GFA_v02`.
3. Habilitar ejecución del canvas "Tapir" (3 vías: auto-solve / Rhino.Compute-Hops / Tapir-ArchiCAD API).
4. Mecanismo Morph → Story(Layer) con GuBIMclass y niveles reales (sin v07.25 falso).
5. `mejora menor`: escenario `mix_usos` (D_MIXTO).
6. Desarrollar `F3_VOLUM_GENERADOR` v07.25 con salida `usos_pisos`.

### Lecciones aprendidas
1. Usos = Área de Actividad + 4 categorías (P/C/R/prohibido); PEMP (BIC) cae a fallback base (régimen propio).
2. Verificar la fuente real antes de asumir: el Anexo 5 es el Manual de Normas Comunes, no el cuadro de usos.
3. IronPython 2.7 (GHPython): sin f-strings/pathlib; capas con estándar GuBIMclass; niveles con nombres reales de ArchiCAD.
4. Derivados (`anexo5_pdf_extract.txt`, `gfa-gh.json`, resultados F2/F3) no se commitean.

### Soluciones entregadas
- `data/pot-bogota/usos-por-sector.json` v02: `areas_actividad` (Proximidad/Estructurante/GSM
  → principal/complementario/restringido/prohibido) + `aa_taxonomia` + `base` 4 categorías.
- `servidor.py`: `_categoria_aa()` + `_catalogo_usos()` 4 categorías + `_usos()` por AA (→sector→base),
  campo `categoria_area_actividad`.
- `index.html`: categoría "Restringidos".
- `F3_VOLUM_GENERADOR_v07.25`: salida `usos_pisos` (1:1 con `volumenes_por_uso`).
- `F3_MORPH_ATRIBUTOS_v01.py`: Morph → Layer GuBIMclass + Story (nivel) → `morph-manifest.json`.
- `EJECUCION_TAPIR.md`: 3 vías de disparo del canvas.
- `F1_EXPORTAR_GFA_v02.py`: fuente v02 + SUBVERSIONES INTERNAS v02.1.
- Suite: **240 passed**.

### Pendientes de esta sesión
1. Cablear `usos_pisos` (F3) → entrada `pisos` de `F3_MORPH_ATRIBUTOS_v01`; completar Paso 3
   (Story/Layer en ArchiCAD vía Tapir/Live Connection — verificar si `archicad` ac29 soporta
   Modify; `F3_StorySync_v01` es read-only).
2. Validar `pago_parcial_pct` F2 contra un caso real.
3. Regenerar GFA en Rhino (826.58 vs 1186.87) y revisar las anomalías de vecinos/antejardín.
4. F4 Ladybug (ambiental) y F5 BIM (inyección) — fases posteriores.
