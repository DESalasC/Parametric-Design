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
