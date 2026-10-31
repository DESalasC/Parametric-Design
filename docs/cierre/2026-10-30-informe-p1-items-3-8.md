# Informe P1 — Items 3 a 8 (etapas de validación viva ArchiCAD)

**Fecha:** 2026-10-30  
**Proyecto:** DiseñoParametrico  
**CHIP de referencia:** AAA0030JKOE (La Candelaria)  
**Canvas:** `gh-definitions/F1_CONTEXTO_v13.7.ghx`

---

## Resumen ejecutivo

Los items P1 3-8 requieren trabajo mixto: configuración de canvas (sin código nuevo) y creación de un archivo nuevo (F5_MAPEO_TAPIR_v01.py). Los endpoints GET/POST `/api/norma-override` y POST `/api/z0` **ya existen** en `servidor.py`; falta solo `GET /api/z0-vista`. El patrimonio aplica SOLO al primer segmento norte-occidental (lado 0), limitado a la longitud del volumen de contexto50 en ese costado; al oriente de ese segmento no aplica retiro patrimonial.

---

## Estado de cada item

### Item 3 — Corrida limpia canvas + censo 20/20 zonas ArchiCAD

**Estado:** Pendiente (acción del operador en canvas + ArchiCAD)

**Qué hay que hacer:**
1. Ejecutar `scripts\utilities\fetch-urban-context-v7.py --chip AAA0030JKOE` para regenerar `data\pot-cache\AAA0030JKOE-contexto.json` (requerido por ETAPA1; si falta, el canvas detiene con "No se encontró el JSON").
2. Abrir `F1_CONTEXTO_v13.7.ghx` y ejecutar corrida limpia (ETAPA1 → LADOS v06 → PATIO v03 → NORMATIVA v10 → EXPORTAR_GFA v02.4).
3. En ArchiCAD, censar 20/20 zonas: verificar que las capas `00-00-10_Lote_proyecto`, `00-20-20_Elementos_entorno_urbano`, `70-20-20_Perimetros_vecinos`, `70-50-10_Zonas_verdes_publicas` existan y tengan geometría clasificada.

**Causa raíz (subagente a260f46b319adcac2, completado):**
- No existe componente `AC_GetElements` en el canvas. El predio y las vías no se consultan a ArchiCAD en vivo.
- Las curvas entran vía `Deconstruct 2D Polyline` → salida C tipificada como "Planar Curve" (plugin Live Connection, sin `ClosestPoint`). `filtrar_curvas()` las descarta si no se convierten a curva nativa.
- Corrección: Type Hint = Curve, Access = List, Mapping = Flatten en las entradas geométricas de LADOS; conectar salida C del Deconstruct DIRECTO al input de LADOS (sin Params > Geometry Polyline); opcionalmente poner un componente Curve nativo de GH tras la salida C para forzar conversión.
- Actualizar Panel `json_path` de ETAPA1 a `data\pot-cache\AAA0030JKOE-contexto.json`.

**Criterio de cierre:** ETAPA1 reporta Vecinos > 0 y Vías > 0; LADOS sin avisos de "item(s) NO convertibles"; `sides_table_json` reporta al menos un lado Frontal (vía) y laterales Lateral (vecinos).

---

### Item 4 — F3_StorySync_v02 --check → 8/8 niveles, 0 faltantes

**Estado:** Pendiente (regenerar `niveles_deseados.json` primero)

**Qué hay que hacer:**
1. Regenerar `casos/AAA0030JKOE/niveles_deseados.json` con `F3_StorySync_v02 --plan` (el actual está en marco antiguo: base −11,565, sin `zgf_m`; ADR-024 requiere GF=0 en ArchiCAD).
2. Ejecutar `F3_StorySync_v02 --check` comparando contra stories de ArchiCAD (puerto 19724 para JSON/Python API).
3. Objetivo: 8/8 niveles, 0 faltantes. Validación viva caso B.

**Nota:** `plan_stories` ya emite esquema ADR-024 idéntico (`elevation` en marco ArchiCAD con GF=0, `zgf_m`, `elevacion_modelo_m`). El JSON exportado incluye `zgf_m`.

---

### Item 5 — Conectar `zgf_m` al canvas en F3_VOLUM_GENERADOR

**Estado:** Pendiente (cableado en canvas)

**Qué hay que hacer:**
- `zgf_m` (cota del Ground Floor, desde `data/pot-cache/<CHIP>-z0.json` generado por `_z0_guardar`) debe entrar como input a `F3_VOLUM_GENERADOR_v08` en el canvas.
- `F3_VOLUM_GENERADOR_v08._plan_stories` ya acepta `zgf_m` y eleva ArchiCAD = elevación_modelo − zgf_m, GF=0.
- No hay cambio de código en `F3_VOLUM_GENERADOR_v08.py` pendiente; solo conectar el input en el canvas GH.

---

### Item 6 — Endpoints servidor.py norma-override GET/POST, pantalla patrimonio, filtrado por lado

**Estado:** Parcialmente resuelto (endpoints ya existen)

**Endpoints existentes (verificado en `servidor.py`):**
- `GET /api/norma-override` (línea 1903): devuelve `contexto_pot` + `override` del chip.
- `POST /api/norma-override` (línea 2029): guarda/mergea override para un chip.
- `POST /api/z0` (línea 1938): guarda `data/pot-cache/<CHIP>-z0.json`.
- **Falta:** `GET /api/z0-vista` (lectura del z0 guardado).

**Pantalla patrimonio y filtrado por lado:**
- `norma-override.json` para AAA0030JKOE ya tiene `vecino_patrimonio_por_lado`: `[{"lado_id": 0, "nivel": 2, "patrimonio": true}]`, `retiro_patrimonial_m: 3.0` y `franja_patrimonial_longitud_m: 10.5` (derivado de `vertices` del edificio colindante al lado 0 en `AAA0030JKOE-contexto50.json`).
- **Especificación del subsegmento:** el retiro patrimonial (3.0 m) se aplica SOLO al primer segmento norte-occidental del lado 0, limitado por la franja `[0, t1]` donde `t1 = min(1.0, franja_patrimonial_longitud_m / longitud_lado_0)` y `longitud_lado_0 = vertices_lote[0].DistanceTo(vertices_lote[1])` (arista 0→1 = lado 0 norte-occidental). Con `franja_patrimonial_longitud_m = 10.5`, `t1 = min(1.0, 10.5 / longitud_lado_0)`. Al oriente de `t1` no aplica retiro patrimonial; se llega hasta el lindero propio.
- NORMATIVA v10 implementa este scope en 4 sitios (`_subsegmentos_piso` ×2, modo intervalos, `escalonados`): para el lado 0, el retiro patrimonial solo si el subtramo inicia dentro de `[0, franja_t1]`; fuera de la franja, retiro normal por empates/otros. Sin franja definida, comportamiento legacy (retiro sobre todo el lado patrimonio).
- El contexto50 NO tiene bandera de patrimonio ni campo `longitud_m` (subagente a6e3ddce47504496c, completado): solo tiene `vertices`, `pisos`, `altura_m`, `area_m2`, `z_base_m*`. La longitud se deriva de las coordenadas de `vertices` del edificio que colinda con el lado 0 (vértices coincidentes <0.10 m con el lote).

**Acción de código completada:** `franja_patrimonial_longitud_m = 10.5` en `norma-override.json` para AAA0030JKOE; NORMATIVA v10 aplica el retiro patrimonial solo al primer segmento norte-occidental limitado por la franja. Pruebas: `tests/test_normativa_v10_patrimonio.py` (2 tests, pasan).

---

### Item 7 — Re-exportar contexto50 .3dm (z_base_m corregido)

**Estado:** Pendiente (acción en canvas/Rhino)

**Qué hay que hacer:**
- Re-exportar `exports/contexto50/AAA0030JKOE-contexto50.3dm`. El actual quedó con los 71 morphs a +14,4875 m (cota incorrecta).
- Corregir `z_base_m` en la exportación. El contexto50 ya trae `z_base_m`, `z_base_centroide_m`, `z_base_min_m`, `z_base_max_m` por edificio (subagente a6e3ddce47504496c).
- La exportación del 3dm está apagada por defecto en el canvas (toggle `bake`+`exportar`); encenderla para esta corrida.

---

### Item 8 — Crear F5_MAPEO_TAPIR_v01.py (Fase 5)

**Estado:** No existe. Debe crearse.

**Qué hay que hacer:**
- Crear `src/fase-5-bim/F5_MAPEO_TAPIR_v01.py`.
- Mapeo GH → ArchiCAD vía protocolo Tapir (paquete Python `archicad`, puerto 19724 para JSON/Python API; 19723 solo para Live Connection canvas).
- Mapear `AC_Slab`, `AC_Wall`, `AC_Zone` desde la geometría de Fase 1/3.
- **Bloqueador resuelto 2026-10-06:** puerto 19723 (portproxy VM→host funcional). Antes de lanzar: `python scripts/utilities/detectar-puerto-archicad.py` (código 0 = API encontrada).
- El README de `src/fase-5-bim/README.md` solo describe lo que hay que crear; no hay código aún.

---

## Aclaración crítica: patrimonio (solo primer segmento norte-occidental)

El usuario aclaró que el lote patrimonial está al OCCIDENTE frente a la vía, al NORTE del predio en la **primera parte más cercana a la vía**, pero NO todo el lado norte es patrimonial — solo la longitud correspondiente al volumen existente en contexto50 en ese mismo costado (occidente). Al ORIENTE de ese segmento, NO aplica aislamiento patrimonial y se puede llegar hasta el lindero propio.

**Consecuencia:** Los aislamientos actuales están CRUZADOS (están al norte u oriente cuando deberían estar solo en ese segmento norte-occidental, el primer segmento lateral norte perpendicular a la vía). El aislamiento debe aplicarse SOLO sobre ese primer segmento lateral norte, limitado por la longitud del volumen del vecino de conservación en contexto50.

**Implementación:** `franja_patrimonial_longitud_m` en `norma-override.json` debe contener esa longitud (derivada de `vertices` del edificio colindante al lado 0 en contexto50), y NORMATIVA v10 debe aplicar el retiro patrimonial solo a ese sub-segmento, no a todo el lado norte.

---

## Próximos pasos recomendados (orden de ejecución)

1. **Item 6 (código):** Rellenar `franja_patrimonial_longitud_m` en `norma-override.json` para AAA0030JKOE (derivar de contexto50 `vertices` del edificio colindante al lado 0).
2. **Item 6 (servidor):** Añadir `GET /api/z0-vista` a `servidor.py` si se necesita lectura del z0.
3. **Item 3 (canvas):** Corrida limpia `F1_CONTEXTO_v13.7.ghx` con correcciones de entrada de curvas (Curve nativo, Type Hint=Curve, List+Flatten).
4. **Item 4:** Regenerar `niveles_deseados.json` con `F3_StorySync_v02 --plan`, luego `--check` → 8/8.
5. **Item 5:** Conectar `zgf_m` al canvas en `F3_VOLUM_GENERADOR_v08`.
6. **Item 7:** Re-exportar `AAA0030JKOE-contexto50.3dm` con `z_base_m` corregido.
7. **Item 8:** Crear `F5_MAPEO_TAPIR_v01.py`.

---

## Bloqueadores conocidos

- Puerto 19723: AutoCwall escritorio lo reclama. Workaround: `diagnostico_puerto_19723.ps1 -Liberar` o cerrar/reabrir en orden (ArchiCAD → Grasshopper → AutoClaw). Verificado 2026-10-26: 19723 quedó libre para ArchiCAD.
- `contexto50-actual.json` no existe para AAA0030JKOE (no bloquea: se usa `AAA0030JKOE-contexto50.json` directamente).
- Contexto50 no tiene bandera de patrimonio: la protección patrimonial se define en `norma-override.json` (override del operador), no en la geobase.
