# Evaluación y propuesta — Lote en pendiente · La Candelaria (CHIP AAA0030JKOE)

**Proyecto:** DiseñoParametrico · **Fecha:** 2026-09-28 · **Estado:** propuesta para revisión del operador
**Alcance:** cómo implementar el proceso completo (selección de lote → terreno → lados/envolvente → patios/aislamientos/separaciones → masa) para un predio con: **pendiente fuerte**, **varios volúmenes con separaciones** (no necesariamente patios), **dos vías de acceso**, **restricción de altura** y **empate parcial** contra un inmueble de conservación.

> Fuentes: código y datos del repo (rutas citadas), muestreo directo del MDT de Catastro Bogotá (evidencia adjunta en `evidencia/`), `data/pot-cache/AAA0030JKOE-norma-manual.json` (consulta oficial 2020), Decreto 492/2007 (PZCB) y PEMP referenciados por el propio proyecto. Los valores de cota provienen del **MDT urbano (estimado)** y deben validarse con topografía real (plan `170006A001` citado en la norma manual).

---

## 0. Resumen ejecutivo

1. **El predio ya está en el sistema** como caso B (`AAA0030JKOE`), pero corre con **supuestos de lote plano**: la topografía llega en **ceros** (bug de parser en el fetch), la masa se extruye como **un solo cuerpo desde z=0**, y la norma manual de Candelaria **no está cableada** al override.
2. **La pendiente es real y severa:** muestreo del MDT (63 puntos) → desnivel **14,25 m** en el lote, pendiente media **≈26 % (14,7°)**, descenso general hacia el **NO**; costado alto **~2 647 m** vs costado bajo **~2 635 m** (**Δ 11,7 m**). Esto obliga a estrategia de **plataformas/terrazas** y cotas por volumen.
3. **La mayoría de los cambios son extensiones acotadas, no un rediseño:** ya existen *override de frente por lado*, *vecinos por sub-segmento con alturas* (v08), *empate + separación sísmica*, *envelope por piso* y *export F1.5 con flag*. Faltan: **topografía viva**, **multi-volumen con separaciones**, **multi-frente (dos vías)** y **empate de conservación + cap de altura**.
4. **Propuesta:** 1 corrección de datos (fetch) + 1 componente F1 nuevo (terreno) + 2 componentes F3 nuevos (plataformas, multi-volumen) + 3 extensiones (NORMATIVA v09, ACCESOS v03, UI/datos). Plan por fases **P0–P3** con pruebas y criterios de aceptación (§2.5).
5. **Decisiones** (§2.6): *Resueltas (2026-09-28):* área (geobase, 946,45 m²); criterio de altura (**5 pisos**); vía oriental (en obra + Parque Pueblo Viejo al frente); separación entre volúmenes (**≥6,00 m**); empate parcial (**2 pisos × primeros ~20 m**, ver §4.1). *Restan:* ubicación exacta del tramo y visto bueno IDPC; "Norma 3 pisos" del alzado; confirmación de la 2.ª vía para overrides.

---

## 1. Evaluación

### 1.1 El predio, con datos verificados

| Dato | Valor | Fuente |
|---|---|---|
| CHIP / catastro | `AAA0030JKOE` / 00310033519, KR 1 12 D 54 | norma-manual |
| Área | **946,45 m²** (polígono geobase; perímetro 146,8 m, 30 vértices) — **válida** (el ~976 m² era aproximado; confirmado 2026-09-28) | `AAA0030JKOE-contexto.json` |
| UPZ | 94 – La Candelaria | norma-manual |
| Norma | Decreto **492/07** (PZCB): uso Residencial, **IO 0,70**; 3 pisos + 2 (**Nota Ñ** — la ficha oficial la escribe Ñ; el norma-manual la citó como "N") = **5 pisos**, altura máx. **10,0 m**; el predio **NO** es patrimonio (la GDB devolvía "CHB" por error) | ficha 2020 + norma-manual |
| Pendiente | **≈26,3 % (14,7°)**; desnivel **14,25 m** (máx 2 649,0 – mín 2 634,8); descenso hacia el **NO** (azimut de bajada ≈318°) | muestreo MDT (ver §A) |
| Cotas de frentes | costado alto **≈2 647,1 m**; costado bajo **≈2 635,4 m** (**Δ 11,7 m**) | muestreo MDT |
| Vías | **Dos carreras**; la **oriental en proceso de construcción** con el **Parque Pueblo Viejo** (PEMP, proyecto detonante 27) **al otro lado de la calle** (aclarado por el operador, 2026-09-28); **sin antejardín** en ambos frentes (al límite predial) | operador + PEMP |
| Colindancia norte | Predio **Conservación Básica** (**2 pisos**, sobre los **primeros ~20 m** del lado norte — dato operador 2026-09-28; la consulta 2020 decía ~12 m) | operador + norma-manual |
| Colindancia sur | Edificación de **5 pisos** sobre **~25 m** del lado sur (dato operador 2026-09-28) | operador |
| Vías digitalizadas | **Incompletas** en `Eje_vial`: la clasificación automática marca E/O como "predio"; el override del operador existe para corregirlo | `VECINOS_POR_LADO.md` |

**Puntos a confirmar (inconsistencias detectadas):**
- E/O: **aclarado por el operador (2026-09-28)** — la vía oriental está **en proceso de construcción** (frente al Parque Pueblo Viejo). Actualizar la nota "occidente_fondo" del norma-manual, hoy inconsistente.
- Drift de pisos: norma manual = 5 pisos; modelo F3 actual = 6 niveles; cap altura 10 m sin aplicación → definir corrida vigente de B.
- Área: **resuelta** — se adopta la de la geobase (946,45 m²).

### 1.2 Lo que ya sirve (palancas del sistema actual)

- **Selección/activación de lote**: front-end (sección 1) + `POST /api/nuevo-chip` + `_activar_chip()` + activos `CHIP-*.json` (el canvas lee rutas fijas).
- **Frentes por lado con override**: `frente_override_json` (F0 v01.4 → NORMATIVA v08.2). Ideal para marcar **las dos vías** sin depender de la geobase.
- **Vecinos por sub-segmento con alturas** (NORMATIVA v08): un lado se subdivide en tramos por vecino, con recorte por **semiplanos** — base directa para un **empate parcial** en un tramo de ~12 m.
- **Empate + sismo**: reglas `1/5·h` con mínimo, empate posterior (5.4.c) y lateral (1.9.c) + separación NSR-10 A.6.5 (se toma el mayor).
- **Envelope por piso** (`envelope_por_piso`, `retiros_por_piso`) ya consumido por F3; `altura_z`/`altura_piso` por piso ya previstos en el contrato del programa F3.
- **F1.5 verificación**: patrón flag → `<CHIP>-lados.json` (PATIO v02.4) — extensible a terreno/empates.
- **Arnés de pruebas** con stub de Rhino (CPython): los nuevos componentes pueden probarse sin Rhino.

### 1.3 Brechas frente a las condiciones nuevas

#### G1 · Terreno en pendiente
- **Bug de topografía (z=0 en todos los chips)**: el fetch lee `results[0].get("value")`, pero el servicio MDT devuelve `attributes["Stretch.Pixel Value"]` → cae al default `"0"`. **Verificado**: consultando con la clave correcta, 63/63 puntos devuelven cotas reales (2 634,8 a 2 649,0 m).
- Muestreo actual **solo en el borde** del lote (vértices + puntos medios + centroide): insuficiente para pendiente interna; `estado` fijo en "ESTIMADA"; sin cotas de calle por frente.
- **Nada aguas abajo consume pendiente**: LADOS/PATIO/NORMATIVA son 2D; F3 extruye desde z=0 (`_extruir(curva, h, z)` acumulando altura por piso) → volúmenes "flotando" en un plano.

#### G2 · Varios volúmenes con separaciones (no necesariamente patios)
- F3 genera **un volumen continuo por piso** (con exclusión de núcleo). No existe fraccionar la masa en bloques ni **tipificar separaciones** (junta / pasaje / luz).
- PATIO v02.4 solo genera el **patio normativo** (≥9 m², claridad ≥3 m) desde el vértice N. En un predio *entre dos carreras*, muchos vértices son vía+vecino → ese automatismo pierde protagonismo; los vacíos del esquema multi-volumen nacen del **fraccionamiento**, que hoy no existe.
- No hay **validador de vacíos**: ¿ilumina? (⇒ reglas de patio) ¿es paso? (⇒ ancho mínimo) ¿es junta estructural? (⇒ registro en metadatos).

#### G3 · Dos vías de acceso
- Clasificación auto de E/O = "predio" (geobase incompleta) → **requiere override del operador** (maquinaria lista; el archivo de override para B aún no existe).
- NORMATIVA maneja **un solo frente**: entradas únicas `ancho_via_m` / `antejardin_m` (y un voladizo derivado). Con dos carreras de anchos distintos, antejardín/voladizo deben ser **por lado** (LADOS v06.5 ya emite `ancho_via_m` por lado frontal — falta consumirlo).
- ACCESOS v02 asigna "Frontal" genérico y no distingue vía; sin reparto de accesos entre dos calles ni **fases** (vía proyectada ≠ usable hoy).

#### G4 · Restricción de altura y empate parcial con conservación
- `altura_max_pot` es **obsoleto** ("se ignora, pero se mantiene para no romper el canvas"): el **cap efectivo de 10 m** no entra al envelope; `altura_total = pisos × floor_h` (5×3 m = 15 m > 10 m).
- El empate por tramos existe, pero **sin modo "conservación"**, sin altura del vecino (hoy `altura_m: null` para el vecino norte) y sin longitud del tramo de empate. El carácter **"parcial"** (tramo acotado; hoy ~20 m según datos de campo) no está modelado.
- No hay bandera de trámite (**Nota N** ⇒ anteproyecto aprobado por **IDPC + MinCultura**) ni salida específica para revisión patrimonial.

#### G5 · Norma manual de Candelaria sin cablear
- `AAA0030JKOE-norma-manual.json` (consulta oficial 2020) existe, pero **no está en `norma-override.json`** (solo A y C). El fetch no lo toma: UPZ, rango, IO, pisos y nota N hay que **portarlos**.

#### G6 · Datos menores
- Área 946,45 vs ~976 m².
- Alturas de vecinos sin capturar (`altura_m: null`).
- Inconsistencia E/O (existente vs "aún no construida").
- Drift B: 5 pisos (norma) vs 6 niveles (modelo F3 actual).

### 1.4 Impacto si se corre el caso B hoy, sin cambios
Con los supuestos actuales: topografía en ceros → sin pendiente; un único volumen extruido desde z=0 → imposible ver terraza/cortes; antejardín calculado sobre **un** frente → incorrecto para el segundo; sin empate de conservación ni cap de 10 m → envolvente y GFA no representativos del predio. **Conclusión: el caso B actual es un placeholder; hay que ejecutar los cambios antes de usarlo como base de diseño.**

---

## 2. Propuesta

### 2.1 Concepto — el lote en pendiente se trabaja en 4 capas

| Capa | Función | Estado |
|---|---|---|
| **1. TERRENO** | cotas reales → malla, curvas de nivel, perfil por lado, pendiente, cotas de acceso por frente | *nueva* |
| **2. ENVOLVENTE NORMATIVA** | retiros por lado (**multi-frente**), cap de altura, **empate de conservación**, patios normativos | *extensión* (sigue 2D + pisos; la pendiente entra como cotas de referencia y tope por pisos/altura) |
| **3. FRAGMENTACIÓN** | **plataformas** (terrazas) + corte en N volúmenes + **separaciones tipificadas**: `patio` (norma 9 m²/3 m), `pasaje` (paso/circulación, ancho mínimo), `junta` (técnica) — ancho entre volúmenes ≥ máx(2/5·h_prom; **6,00 m**) (Anexo 5 §1.10.b, ver §4.2) | *nueva* |
| **4. MASA Y FLUJOS** | accesos repartidos entre las **dos vías**, núcleos, volúmenes finales a Morphs con cota base | *extensión* |

Clave de la Capa 3 (respuesta directa a "volúmenes con separaciones, no necesariamente patios"): **toda separación queda clasificada y validada con su propia regla**; solo las que funcionan como iluminación/ventilación heredan los requisitos de patio (≥9 m², claridad ≥3 m). Las demás exigen ancho mínimo funcional (p. ej., pasaje 1,5–2,2 m según decisión) o son juntas técnicas registradas. Nada se fuerza a "patio".

### 2.2 Cambios concretos por componente

| # | Componente | Tipo | Cambio principal | Prioridad |
|---|---|---|---|---|
| 1 | `fetch-urban-context-v6.py` → **v7** | ext. | Parser MDT corregido (`attributes["Stretch.Pixel Value"]`, fallback numérico); muestreo densificado (rejilla interior ≤5 m + anillo perimetral + 2–4 puntos por frente); guarda `pendiente_pct`, `delta_m`, `cotas_frente`, `estado` (ESTIMADA/REAL) | **P0** |
| 2 | `norma-override.json` | datos | Alta del bloque B portado desde `norma-manual.json`: `upz 94`, `tratamiento`, `rango`, `io_maximo 0.70`, `altura_maxima_pisos 5`, `fuente Decreto 492/07 + Nota N` | **P0** |
| 3 | **`F1_ETAPA4_TERRENO_v01`** (GHPython, nuevo) | nuevo | Malla de terreno, curvas de nivel (1 m), **perfil de cota por lado**, pendiente y cotas de acceso; salidas para canvas y F3 | P2 |
| 4 | `F1_ETAPA2_LADOS_v06.5` → **v07** | ext. | Mantiene clasificación; añade a `sides_table` el **perfil de cota por lado** y marca `frente_alto`/`frente_bajo` (sin cambiar LADOS/retiros) | P2 |
| 5 | `F1_ETAPA2_NORMATIVA_v08` → **v09** | ext. | (a) **multi-frente**: antejardín y voladizo **por lado frontal** (consume `ancho_via_m` por lado de LADOS); (b) **cap de altura** `altura_maxima_m` efectivo; (c) **empate de conservación** por sub-segmento (nuevos campos en `vecinos_por_lado`: `conservacion`, `altura_m`, `empate{tramo_m, altura_ref_m, modo}`); (d) salida `envolvente_conservacion_json` + bandera IDPC/MinCultura | **P1** |
| 6 | `F1_ETAPA2_PATIO_v02.4` | — | **Sin cambios**: las reglas vigentes (≥9 m², claridad ≥3 m; simplificación <2.5°) se conservan para vacíos que iluminan | — |
| 7 | **`F3_PLATAFORMAS_v01`** (nuevo) | nuevo | Terrazas sobre el terreno (Δz objetivo ≈1 piso, talud máx configurable, balance corte/lleno); salida: polígonos de plataforma + `z_top` + `z_base` por plataforma | P2 |
| 8 | **`F3_MULTIVOLUMEN_v01`** (nuevo) | nuevo | Divide la envolvente en **N volúmenes** respetando plataformas, accesos y fachadas; **genera y clasifica separaciones** (patio/pasaje/junta) + **validador de vacíos**; salidas listas para VOLUM | P2 |
| 9 | `F3_VOLUM_GENERADOR_v08` → **v09** | ext. | `z_base` por volumen/piso (terraza real, no z=0); juntas de la fragmentación; salidas Morph con cota corregida | P2 |
| 10 | `F3_ACCESOS_INTEGRADOR_v02` → **v03** | ext. | Reparto de accesos entre **dos vías** (público/privado/vehicular); **fases** (si la 2.ª vía no existe aún); coherencia con plataformas | P3 |
| 11 | Orquestador / UI (`index.html`, `servidor.py`) | ext. | "Análisis de terreno" tras fetch (`/api/contexto` + alerta si pendiente >15 % y ESTIMADA); campos por vecino (conservación S/N, altura, tramo de empate); export F1.5 ampliado (terreno + empates) | P1–P2 |

### 2.3 Flujo end-to-end actualizado (respuesta directa a "cómo implementar todo el proceso")

0. **Selección de lote** *(igual que hoy + 1 añadido)*: UI → elegir CHIP existente o "Procesar CHIP nuevo" → fetch base + 50 m → activación de activos. **Añadido**: al terminar, panel "terreno" con pendiente, cotas y cotas de los dos frentes; si `pendiente > 15 %` y estado ESTIMADA → aviso "recomendar levantamiento" (estado REAL cuando exista).
1. **Datos del lote (fetch v7)**: cotas corregidas y densificadas; se guardan perfiles de cota por frente (para definir accesos arriba/abajo).
2. **Operador (UI §1/1b)**: confirmar frentes → **marcar las dos vías** (override E/O); marcar el **vecino de conservación** (tramo ~12 m, altura del inmueble, modo de empate); completar alturas de los demás vecinos. Guardar (por CHIP).
3. **Canvas F1**: `ETAPA1` (terreno real) → `LADOS v07` (clasificación + perfiles) → `PATIO v02.4` (sin cambios) → **`NORMATIVA v09`** (multi-frente + cap altura + empate conservación) → `EXPORTAR_GFA` → **export F1.5 ampliado** (terreno + empates en `<CHIP>-lados.json`).
4. **Verificación F1.5** (patrón flag; se amplía el JSON de diagnóstico: pendiente, cotas de frentes, tramo de empate aplicado, cap de altura).
5. **F2 demanda**: mismo contrato (GFA). ⚠️ Con el cap de 10 m/pisos efectivos el GFA puede cambiar → **revisar la corrida vigente de B** (hoy 3 312,6 m² con 6 niveles).
6. **F3 masa**: `DISTRIBUCION` (layout) + `ACCESOS v03` (reparto entre vías, fases) + **`PLATAFORMAS`** + **`MULTIVOLUMEN`** (fraccionamiento + separaciones + validador) + `VOLUM v09` (z por volumen; núcleo; salidas Morph con cota).
7. **Morphs a ArchiCAD** (misma ruta; cota base corregida por volumen).
8. **Documentación + tests + ADRs** (candidatos: terreno/multi-volumen; empate de conservación).

**Aplicado a Candelaria (ilustrativo, a decidir con datos finales):** 4 plataformas de ~3,5 m → 3–4 volúmenes escalonados bajando hacia la carrera baja/parque; acceso desde la vía alta en el volumen 1 (cota ~2 647) y desde la vía baja en el volumen 3/4 (cota ~2 635); separaciones: pasaje central (circulación/conexión entre calles) + 1 patio normativo si algún recinto lo requiere + juntas técnicas (separación entre volúmenes ≥ 6,00 m, §4.2). Empate: solo el tramo norte de ~20 m contra el inmueble de conservación (2 pisos).

### 2.4 Modelo de datos (nuevo / extendido)

```jsonc
// (1) topografia v2 — dentro de <CHIP>-contexto.json
"topografia": {
  "estado": "ESTIMADA",                  // ESTIMADA | REAL
  "fuente": "Catastro_REST_API_MDT",
  "pendiente_media_pct": 26.3,
  "delta_m": 14.25,
  "cotas_frente": { "Oriente": 2647.1, "Occidente": 2635.4 },
  "malla_terreno": [ { "id": "P0", "x_local": 0.0, "y_local": 0.0, "z_local": 8.2 }, "..." ],
  "muestras_auditoria": [ "..." ]        // puntos consultados (trazabilidad)
}
```

```jsonc
// (2) vecino con empate de conservación — extensión de <CHIP>-vecinos-por-lado.json
{ "lados": [ { "id": 2, "cardinal": "Norte", "vecinos": [
    { "chip": "...", "longitud_m": 20.0, "altura_m": 6.0,
      "conservacion": true,
      "empate": { "modo": "parcial", "tramo_m": 20.0, "altura_ref_m": 6.0,
                  "criterio": "empate_cornisa", "aprobacion": "IDPC+MinCultura" } } ] } ] }
```

```jsonc
// (3) plataformas — casos/<CASO>/plataformas.json (F3_PLATAFORMAS_v01)
{ "talud_max_pct": 40, "balance_corte_lleno": 0.92,
  "plataformas": [ { "id": "P1", "z_top": 2643.2, "z_base": 2640.0, "area_m2": 260.0, "poligono": [ "..." ] }, "..." ] }
```

```jsonc
// (4) volúmenes y separaciones — casos/<CASO>/separaciones.json (F3_MULTIVOLUMEN_v01)
{ "volumenes": [ { "id": "V1", "plataforma": "P1", "z_base": 2640.0, "huella_m2": 240.0 }, "..." ],
  "separaciones": [ { "id": "S1", "tipo": "pasaje", "entre": ["V1","V2"], "ancho_m": 2.0, "largo_m": 26.0,
                      "estado": "valida" },
                    { "id": "S2", "tipo": "patio",  "entre": ["V2","V3"], "area_m2": 9.6, "claridad_m": 3.1,
                      "estado": "valida" },
                    { "id": "S3", "tipo": "junta",  "entre": ["V3","V4"], "ancho_m": 0.05, "nota": "estructural" } ] }
```

### 2.5 Plan de implementación (fases, entregables, aceptación)

| Fase | Tareas | Entregables | Criterio de aceptación | Estimado |
|---|---|---|---|---|
| **P0 — Datos y correcciones ✅ (2026-09-28)** | (1) fix parser MDT + muestreo denso ✅; (2) norma B al override ✅; (3) re-fetch completo de B ✅ | fetch v7; `norma-override` B; `AAA0030JKOE-contexto.json` con cotas reales | Re-fetch B: pendiente **25,85 %** / **Δ 16,12 m** ✅; tests **303/303** ✅ (incl. regresión EP-cubre-lote); cotas visibles en canvas ⏳ (AutoClaw cerrado; resta vista del operador) | ~1 día (real) |
| **P1 — Envolvente** | (4) NORMATIVA v09 (multi-frente + cap altura + empate conservación + salida IDPC); (5) UI vecinos/empate + export F1.5 ampliado | NORMATIVA v09 + tests conductuales; JSON F1.5 extendido | Para B: antejardín por frente según cada vía; tramo 12 m empata a `H_ref` sin excederlo sin retiro; cap 10 m aplicado (regla a decidir); GFA por piso reportado | 3–5 días |
| **P2 — Terreno y fragmentación** | (6) F1_ETAPA4_TERRENO; (7) F3_PLATAFORMAS; (8) F3_MULTIVOLUMEN + VOLUM v09 (z_base) | 3 componentes nuevos + pruebas con stub | Corrida B genera ≥3 volúmenes con `z_base` distintos (Δ≥10 m), separaciones clasificadas y validadas; export `.3dm` OK | 1–2 semanas |
| **P3 — Accesos y cierre** | (9) ACCESOS v03 (dos frentes + fases); (10) docs/ADR + validación en vivo | ACCESOS v03; ADRs; manual actualizado | Dos accesos peatonales distribuidos + vehicular definida; fase 1 coherente con vía existente | 3–5 días |

*Nota:* P0 y P1 se pueden ejecutar ya (sin Rhino); P2 requiere sesión de canvas (cerrar AutoClaw por el puerto 19723).

### 2.6 Decisiones abiertas (operador / IDPC)

1. **"Empate parcial" — CERRADA (2026-09-28):** aplica **por sub-tramo** al **primer tramo de ~20 m del lado norte** (colindancia con el inmueble de conservación, **2 pisos de altura**); por encima del nivel de empate rige el aislamiento reglamentario (1/5 h, mín. 4 m, + NSR-10 el mayor) — ver §4.1 y anexo de insumos. Pendiente: visto bueno IDPC/MinCultura (Nota N) y ubicación exacta del tramo en planos.
2. **Criterio altura↔pisos — CERRADO (2026-09-28):** rige **5 pisos** como criterio (los 10 m de la consulta 2020 quedan como referencia tipológica). El estimador ya produce `pisos_finales=5` (rango "4"); NORMATIVA v09 mantiene el conteo por pisos. ⚠️ Revisar la corrida vigente de B (hoy modelada a 6 niveles) contra este criterio.
3. **Área del predio — RESUELTA (2026-09-28):** se usa la de la geobase (946,45 m²); el ~976 m² era una idea aproximada.
4. **Vías — aclarado (2026-09-28):** la **vía oriental está en proceso de construcción** y el **parque metropolitano (Parque Pueblo Viejo, PEMP Proyecto 27)** queda **al otro lado de la calle**. Actualizar overrides de frentes (E = vía) y la nota del norma-manual; modelar la fase hasta la terminación de obra.
5. **Anchos mínimos de separación — validado (2026-09-28; ver §4.2):** Consolidación = **2/5 de la altura promedio de los volúmenes que se aíslan, mínimo 6,00 m** (Anexo 5 §1.10.b). Para volúmenes de 4 pisos ⇒ **6,00 m**. Si el vacío ilumina/ventila, suman las reglas de patios (§1.12.b: lado ≥ 1/3 de la mayor altura, mín. 3 m) y §1.25.
6. **Inmueble de conservación — DATO RECIBIDO (2026-09-28):** **2 pisos**, sobre los **primeros ~20 m del lado norte** (ubicación exacta a precisar en planos). Nota normativa: al ser <3 pisos, el empate volumétrico del §5.5.c no es exigible como tal → se mantiene como condición de diseño/régimen de conservación (validar con IDPC).
7. **"Norma 3 pisos" del alzado PEMP** ("Carrera 1 entre Calle 12F y 12D", lámina EN-D1 P43.2): verificar si describe el contexto existente o restringe el frente oriental (vs ficha del predio: 5 pisos + Nota N).
8. **Frentes/vías — aclarado (2026-09-28):** las dos calles son **Occidente (construida, acceso actual)** y **Oriente (Carrera 1, en obra)**; **sin antejardín** en ninguna (frentes al límite). Los tramos de empate se **miden desde la calle occidental**: norte = primeros ~20 m (BIC, 2 p.) y sur = ~25 m (5 p.) desde el occidente. Queda aplicarlo como override de frentes en la UI.

### 2.7 Próximos pasos inmediatos (sugeridos)

1. **Fix topo + re-fetch B** (P0.1–P0.3) — barato y de altísimo impacto: hoy es un bug de una línea de parser.
2. **Portar norma B** al override (P0.2) y confirmar decisiones §2.6 en una revisión corta.
3. Aplicar en la UI los overrides de **dos vías** + capturar alturas de vecinos (incluida la del conservado).
4. Decidir si el fraccionamiento multi-volumen se prototipa (P2) o si, mientras tanto, se estudia el caso B con "cajas" manuales para tantear la estrategia de plataformas.

---

## Apéndice A — Evidencia del muestreo MDT

- Archivo: [`evidencia/mdt-muestreo-AAA0030JKOE.json`](evidencia/mdt-muestreo-AAA0030JKOE.json) (63 puntos: 30 vértices + 30 puntos medios + centroide + 2 frentes).
- Servicio: `https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/identify` (consulta EPSG:3116).
- Resultados: z mín. **2 634,79 m** / z máx. **2 649,04 m** / **Δ 14,25 m**; pendiente media **26,3 % (14,74°)**; azimut de bajada ≈**318,2°**; frentes ≈**2 647,1 m** y **2 635,4 m** (Δ **11,71 m**).
- Nota de método: el fetch v6 devuelve 0,0 para todos los puntos porque lee la clave `value`; el servicio responde `attributes["Stretch.Pixel Value"]`. Corregir esa clave habilita cotas reales (verificado 63/63 puntos).
- Límites: MDT urbano **estimado**; validar con levantamiento/nivelación (plan `170006A001` citado en la norma manual). Los valores son consistentes de forma relativa (pendiente/desniveles); la cota absoluta conviene contrastarla con una referencia conocida.

## Apéndice B — Referencias

**Código (repo):**
- `scripts/utilities/fetch-urban-context-v6.py` (topografía; función `get_elevation_from_api` l.~147–167)
- `src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v08.py` (empate/semiplanos; l.~998–1035)
- `src/fase-1-contexto/F1_ETAPA2_LADOS_v06.py` (v06.5; contrato de lados)
- `src/fase-1-contexto/F1_ETAPA2_PATIO_v02.py` (v02.4; reglas de patio)
- `src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py` / `F3_ACCESOS_INTEGRADOR_v02.py` / `F3_DISTRIBUCION_v01.py`
- `src/orquestador/servidor.py` (casos A/B/C; `CASO_CHIP`; endpoints), `run_pipeline_v01.py`
- `data/pot-cache/AAA0030JKOE-norma-manual.json`, `data/pot-bogota/norma-override.json`

**Normativa (consulta web de esta evaluación, para verificación del operador):**
- Decreto 492 de 2007 — Operación Estratégica del Centro de Bogotá / Plan Zonal del Centro (PZCB): <https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=27312> · <https://www.sdp.gov.co/gestion-socioeconomica/operaciones-estrategicas/estrategias/operacion-estrategica-del-centro-de-bogota>
- PEMP Centro Histórico (IDPC): <https://idpc.gov.co/PEMP/Diagnostico/10%20Habitacional.pdf>
- POT vigente: Decreto 555 de 2021 (Anexo 5 — secciones 1.9.b/1.9.c, 5.4.b/5.4.c usadas por el código) · NSR-10 (A.6.5).
- **Copia local (vault):** originales descargados + fichas de consulta en `30-referencia/pot-bogota/reglamentacion-base/` (POT 555; Anexo 5 466/2024 + cartilla ilustrada; Anexo 6 Conservación; PZCB 492/07 + planos 094 + 172/2010; PEMP Res. 0088 + planos; FAQ SDP; mapas CU-5.4.22 y CU-5.5) — registro 2026-09-28.

---

## 3. Registro de ejecución

### 2026-09-28 — P0 ejecutado (aprobación del operador)

- **Fetch v7 — topografía real** (`scripts/utilities/fetch-urban-context-v7.py`, nuevo; el v6 queda como respaldo):
  - Parser del MDT corregido: el servicio devuelve la cota en `attributes["Stretch.Pixel Value"]` (el v6 leía `value` → 0.0 silencioso).
  - Muestreo densificado: rejilla interior 5 m + anillo exterior 6 m (paso 8 m) + vértices/medios/centroide → **118 puntos** para B (tope 400).
  - Salidas nuevas: `topografia.resumen` (delta, pendiente media por ajuste de plano, dirección de bajada, fallidos), `topografia.perfil_lados` (por arista), `malla_terreno[].tipo`; cierre del polígono corregido; vecinos/vías/EP al datum local.
  - Referencias actualizadas: `fetch-contexto-completo_v01.py`, `servidor.py`, `run_pipeline_v01.py`, `F1_CONTEXTO50_FETCH_v01.py` + docs (CLAUDE.md, README, fase-1, orquestador, ARCHIVOS_INTERCAMBIO).
- **Normas de La Candelaria en `norma-override.json`**: bloque `AAA0030JKOE` (Decreto 492/07): UPZ 94, Consolidación, rango "4" → 5 pisos, IO 0,70, fuente + Nota N (aprobación IDPC + MinCultura).
- **Re-fetch completo de B** (`fetch-contexto-completo_v01.py --chip AAA0030JKOE`):
  - Contexto base OK (override aplicado) + **contexto 50 m OK** (90 construcciones).
  - Topografía: **118/118 puntos**, cota 2634,52–2650,65 m (**Δ 16,12 m**), pendiente media **25,85 % (14,5°)**; z local del lote 0,27–14,52 m; perfil de **30 aristas**.
  - ⚠️ `pot_data.altura_maxima_m` quedó en 7,0 (residuo del código CHB de la GDB); el cap efectivo de 10 m entra con NORMATIVA v09 (P1).
- **Pruebas**: nuevo `tests/test_fetch_topo_v7.py` (+13) → **302/302** verdes.
- **Pendiente para cerrar P0**: vista en canvas con AutoClaw cerrado (activar chip B; `contexto50-actual.json` quedó apuntando a B y el orquestador repone el canónico por chip según frescura).
- **Fix del clasificador de vecinos** (`vecinos_por_lado.py`): ignora espacios públicos que **cubren el lote** (caso "Pueblo Viejo", estructurante propuesto con fragmentos sobre el predio) — evitaba que lados reales (Sur = predio ×5) se clasificaran como EP. Test de regresión añadido; suite **303/303**.
- **Consulta normativa** (empates, separaciones, patios, entorno) con las fuentes locales del proyecto y del operador — resultados en **§4**.
- **Datos de empate recibidos del operador (2026-09-28):** criterio **5 pisos**; conservación norte **2 pisos × ~20 m**; colindante sur **5 pisos × ~25 m** → registrados en §2.6/§4.1 y `anexos/insumos-operador-2026-09-28.json` (listos para NORMATIVA v09).
- **Corrida B actualizada a 5 niveles (2026-09-28):** fix de precisión en `F3_DISTRIBUCION_v01` (tolerancia ceil 1e-9→1e-6 + huella sin redondeo — el redondeo a 662,5 daba 6 niveles por 0,075 m²); lote B/B_SALUD 931→**946,45**; regenerados `casos/B` y `casos/B_SALUD` (programa, layout, planos, `.3dm`) + accesos. Suite **303/303**.
- **Registrados:** antejardín **0** (ambas vías, al límite), medición de tramos desde la calle occidental, y validación del **piso de bonificación** — ver §4.4.
- **Reglamentación base descargada y registrada en el vault (2026-09-28):** `30-referencia/pot-bogota/reglamentacion-base/` — POT 555, Anexo 5 (466/2024 + cartilla ilustrada), Anexo 6 Conservación, PZCB 492/07 + planos 094 + 172/2010, PEMP Res. 0088 + planos, FAQ SDP y mapas CU (PDFs originales + fichas `.md`; entrada añadida al mapa de conocimiento).

### 2026-09-28 (noche) — Revisión de integración contexto50 + correcciones aplicadas

- **Revisión del componente** `F1_ETAPA3_CONTEXTO50` frente al esquema de terreno inclinado: (a) la resolución defensiva del template estaba **muerta** (comparación case-sensitive que nunca disparaba + corte `[:-12]` sobre "-contexto.json" que mide 14); (b) **deriva ETAPA3↔builder** (faltaban: sentido antihorario, exclusiones predio objetivo/menores, try/except por edificio); (c) tests del linaje apuntando a `..._v01a.py` (renombrado a v01b en el cierre de hoy); (d) activos del canvas (`CHIP-contexto.json`) pendientes de activar para B.
- **Correcciones aplicadas:** `F1_ETAPA3_CONTEXTO50` **v01.2** (fix defensiva + paridad con el builder: antihorario, exclusiones, try/except, stats/mensaje) · `F1_CONTEXTO50_BUILD_v01b` fix **v01c** (defensiva) · canvas v11 re-embebido (`scripts/utilities/patch-ghx-contexto50-defensiva.py`) y `.gh` regenerado · tests repuntados/aislados (`test_contexto50_build.py`, `test_contexto50_helpers.py`, nuevo `test_etapa3_contexto50.py` — 31/31).
- **Encargo P2 añadido:** extender el fetch del contexto50 con **cota base por edificio** (`z_base_m` vía muestreo MDT) y consumirla en ETAPA3/BUILD (`z_base` de extrusión) para anclar los volúmenes vecinos al terreno real (hoy extruyen desde z=0; Δ 16,12 m en B).

---

## 4. Validación normativa y definiciones (2026-09-28)

### 4.1 "Empate parcial" — semántica exacta

La norma (Anexo 5 — Manual de normas comunes, actualizado por Decreto 466/2024) define el **empate volumétrico**:

- **§1.6 (Empates de alturas — Consolidación/Mejoramiento):** en predios que comparten lindero con edificaciones **sin aislamiento** existentes a la entrada en vigencia del Decreto 555/2021: si el colindante es **más alto** que la altura de los mapas CU-5.4.x → *"se permite prever empate volumétrico con la edificación de mayor altura en toda la longitud de la fachada, previendo aislamiento lateral por el costado que colinde con la edificación de menor altura"*; si es de **igual altura** → puede replicarse la altura existente; si es **menor** que el mapa → **no se exige empate**.
- **§5.5.c (lateral, Consolidación):** *"…se permite prever empate volumétrico con la altura de dichas edificaciones [3+ pisos existentes], a partir de cuyo nivel se exige aislamiento lateral reglamentario respecto de la altura en metros que alcance la edificación, medida desde el nivel del empate."* (§5.4.c equivalente para posterior.)
- Dimensionamiento del aislamiento sobre el empate: **1/5 de la altura** (medida desde el nivel de empate), **mínimo 4,00 m** en Consolidación; se compara con la **separación sísmica NSR-10 A.6.5** y rige el mayor.

**Definición operativa del proyecto — "empate parcial":** empate volumétrico aplicado **por sub-tramo de fachada** (solo el tramo de ~20 m que colinda con el inmueble de conservación [2 pisos], no los ~52 m completos del lado norte) y **hasta la altura del inmueble conservado**; por encima de ese nivel rige el aislamiento reglamentario (1/5·h, mín. 4 m, + sismo) y el tope del predio (5 pisos / 10 m). Por tratarse de colindante con BIC aplican además las disposiciones específicas (Decreto 555 art. 368; Anexo 6; PEMP → anteproyecto IDPC + MinCultura). *Modelado en P1: parámetros `tramo_m`, `altura_ref_m`, `modo` por sub-segmento (NORMATIVA v09).*

**Datos de campo (operador, 2026-09-28):** inmueble colindante norte = **2 pisos**, sobre los **primeros ~20 m** del lado norte; colindante sur = edificación de **5 pisos** sobre **~25 m**. Con ello: (a) norte → empate parcial acotado a esos ~20 m y altura ~2 pisos; (b) sur → empate volumétrico hasta ~15 m en esos ~25 m (§5.5.c sí aplica: colindante ≥3 pisos). Nota: para el tramo norte (2 pisos <3), el empate no es exigible por §5.5.c — se mantiene como condición de diseño/IDPC.

*Detalle estructurado: [`anexos/insumos-operador-2026-09-28.json`](anexos/insumos-operador-2026-09-28.json).*

**Antecedentes IDPC (anteproyecto ago-2021, documentos del lote):** el esquema empató "con el predio norte en fachada", con un muro que "empata con el nivel de la **cumbrera** del predio N-2"; IDPC pidió que el aislamiento norte "sea más generoso con el inmueble N-2" y solicitó un **aislamiento adicional de 3,00 × 3,00 m**. → Incorporar como condicionantes del tramo BIC (empate a cumbrera + mayor generosidad norte + 3×3).

### 4.2 Separación entre volúmenes — validado

**§1.10.b (Aislamientos entre edificaciones** — aplica a edificaciones aisladas entre sí en un mismo proyecto, uno o varios lotes; se exige **a partir del nivel en que se proyectan como aisladas**):

| Tratamiento | Proporción | Mínimo |
|---|---|---|
| **Consolidación** (y Renovación Urbana / Mejoramiento Integral) | **2/5 de la altura promedio** de las edificaciones que se aíslan | **6,00 m** |
| Desarrollo (rangos 1–3, 4A/4B) | 1/3 de la altura promedio | 6,00 m |
| Desarrollo (rangos 4C/4D) | 1/2 de la altura promedio | 6,00 m |

- Verificación del operador ("≈5 m para volúmenes de 4 pisos"): la norma efectiva es **máx(2/5 × h_promedio; 6,00 m)** ⇒ **6,00 m** para volúmenes de ~4 pisos (2/5×12 m = 4,8 m < 6 → gobierna el mínimo).
- Si la separación supera 6,00 m se permiten **avances de fachada de 0,50 m** (hasta 30 % de esa fachada).
- Si el vacío además **ilumina/ventila** recintos: **patios §1.12.b** — cuadrado interior de lado ≥ **1/3 de la mayor altura** de las edificaciones que enmarcan el patio, **mínimo 3,00 m** (+ condiciones §1.25). *(El criterio operativo vigente del proyecto — 9 m² / claridad ≥3 m — queda más laxo en edificios altos: revisar alineación en P1.)*
- Cuerpos estructuralmente independientes: sumar junta/separación NSR-10 (rige el mayor).

### 4.3 Entorno en obra — Parque Pueblo Viejo (PEMP) y Carrera 1

- El PEMP Centro Histórico (Res. 0088/2021 IDPC) incluye como **proyecto detonante Nº 27 "Parque Pueblo Viejo"**: parque urbano de conectividad ecológica con los cerros orientales, **Aula Ambiental del CHB**, arboretum y SUDS; **entre la Carrera Primera y la Avenida Circunvalar**, de La Media Torta a la Plaza de Mercado La Concordia; ~30.600 m² en el corto plazo (con cesiones aledañas, globo >5 ha).
- Lámina **EN-D1 (P43.2)**: *"ALZADO LONGITUDINAL CARRERA 1 ENTRE CALLE 12F Y 12D — **Norma 3 pisos**"* → **verificar alcance** (¿norma del frente? ¿contexto existente?) frente a la ficha del predio (5 pisos + Nota N).
- **Dato POT:** el parque figura como **"Parque Estructurante Propuesto"** (capa Parque, SIN CERTIFICAR). El fetch v7 lo capturó; el clasificador de vecinos fue corregido para **ignorar EP que cubren el lote** (overlap >5 m² → caso "Pueblo Viejo") — regresión cerrada con test.
- Lectura de diseño: el frente oriental (Carrera 1, en obra) quedará **frente al parque** — fachada activa del acceso principal; refuerza la estrategia de volúmenes escalonados y el pasaje hacia el interior.

---

### 4.4 Piso adicional / de bonificación — validación (2026-09-28)

- **Base normativa firme:** 3 pisos + 2 adicionales (**Nota Ñ**, Plano 094 Edificabilidad, Decreto 492/07) = **5 pisos** (ficha del lote 2020-01-29: "Edificable 3 pisos (dos adicionales a la altura básica)"; Nota Ñ: +2 pisos en manzanas con frentes/categoría reedificables — verificar cumplimiento de la condición de manzana).
- **El "+1" del expediente = "posible piso de bonificación":** los documentos del lote (2020-2021) trabajaron un **piso adicional en la parte posterior del lote, costado oriental (sobre la Carrera 1ª este)**; las gestiones buscaban que "se pueda brindar el beneficio de un piso adicional" (IDU/Patrimonio); IDPC señaló que era **"arriesgado dar un veredicto sin las suficientes pruebas"**. → **No consta como derecho; se trata como escenario.**
- **Servicios complementarios:** el PEMP sugiere apoyarse en el **Decreto 190/2004** para servicios que el PEMP no desarrolla (parqueos, salones comunales, cesiones B) — base usada por las propuestas NEOS para su cálculo de servicios.
- **Decisión de modelo:** corrida **base = 5 niveles** (B y B_SALUD regeneradas); el **+1 queda como variante habilitable** (`piso_adicional`) en la parte posterior/oriental, para cuando IDPC/Patrimonio confirme. Retomar el punto con IDPC en el anteproyecto (memorando ago-2021 como antecedente).

---

*Documento vivo — P0 ejecutado y validación normativa 2026-09-28 (ver §3–§4.4).*
