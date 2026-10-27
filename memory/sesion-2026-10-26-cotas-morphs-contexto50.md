---
fecha: 2026-10-26
tipo: memoria_proyecto
proyecto: DiseñoParamétrico
sesion: 2026-10-26 (tarde)
tags: [memoria, sesion, contexto50, morphs, cotas, mdt, z-base, archicad]
---

# Memoria de sesión — DiseñoParamétrico 2026-10-26 (cotas de los morphs del Contexto50)

## Síntoma reportado
Al arrancar el script hoy, **todos** los volúmenes de Morph del Contexto50 aparecían a la
misma altura. El acuerdo vigente (2026-10-25) era que cada morph apoyara en la cota
**mínima** de su propia huella (no en el centroide) para que ninguno quedara "flotando"
dentro de su predio.

## Causa raíz (confirmada con evidencia)
1. El `.3dm` exportado hoy a las 17:00 (`exports/contexto50/AAA0030JKOE-contexto50.3dm`)
   tenía **71 volúmenes con `min Z` idéntico = 14,4875 m** (lectura con `rhino3dm`): el
   mismo plano para todos, 14,5 m sobre el terreno (malla ETAPA1: −0,03…14,43).
2. `data/pot-cache/AAA0030JKOE-contexto50.json` tenía **0/90 edificios con `z_base_m`**.
   El respaldo `.bak-zbase-20261025-2046` sí tenía 90/90: el anclaje del 25-10 (450
   puntos, mínimo por huella) se había hecho bien y **se perdió después**.
3. El culpable era `F1_CONTEXTO50_FETCH_v01.py`: reconstruye los edificios desde la
   geobase y **nunca escribió `z_base_m`**. Cada corrida del orquestador
   (`f1_contexto50`, la última a las 22:43 del 25-10) borraba el anclaje.
4. `F1_CONTEXTO50_BUILD_v01.2.py` convertía `z_base_m` ausente en `0.0`; con
   `desplazamiento_z = −14,488` (marco ETAPA1) eso daba `z_base_ajustado = +14,488`
   **para todos** → el plano único observado.

## Cambios aplicados
1. **`src/fase-1-contexto/F1_CONTEXTO50_FETCH_v01.py`** — `heredar_cotas_zbase()`:
   al regenerar el JSON conserva `z_base_*` del archivo vigente. El `id` catastral NO es
   único (90 registros / 45 ids), así que empareja por **id + centroide de huella**
   (≤ 0,5 m) y no reutiliza dos veces la misma cota. Avisa por consola cuando quedan
   edificios sin cota.
2. **`src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01.2.py`** (componente #45 del canvas):
   `altura_de()` devuelve `None` cuando no hay cota; el volumen se coloca en el datum
   ETAPA1 (0,0) con `ALERTA: N sin cota MDT`, en vez de flotar 14,5 m. El mensaje ahora
   informa `z_base (ajustado) a-b m (N con cota de M)` y avisa si **todos** los volúmenes
   quedan a la misma altura. Además: sin `CHIP-contexto.json` hermano ya no lanza
   `IOError` (antes devolvía 0 volúmenes con ERROR).
3. **`src/orquestador/run_pipeline_v01.py`** — paso nuevo **1.2b `f1_contexto50_cotas`**
   (`anclar_contexto50_zbase.py --chip`), `auto`, `depends_on f1_contexto50`; estado
   `hecho` solo con cobertura 100 %. Se añadió a `orden`, `nombres`, `pasos_auto_base` y
   al checklist HTML.
4. **`scripts/utilities/diagnosticar-cotas-contexto.py`** — ahora **falla** (exit 1) si
   hay edificios sin `z_base_m` o si todas las bases están a la misma altura
   (dispersión < 0,05 m); informa `edificios con cota = N/M` y la dispersión.
5. **`scripts/utilities/sincronizar-codeinput-ghx.py`** (nuevo) — escribe el código de
   `src/` en el `CodeInput` del `.ghx` del componente correspondiente, in situ (sin
   reserializar el XML), con backup y validación `ET.parse`. Complementa a
   `verificar-paridad-canvas-src.py`.
6. **Tests**: `src/fase-1-contexto/tests/test_contexto50_cotas.py` (9 casos: herencia,
   id repetido, huella movida, JSON corrupto, diagnóstico). `test_contexto50_build.py` y
   `test_contexto50_helpers.py` apuntaban a **`F1_CONTEXTO50_BUILD_v01b.py`** (copia
   obsoleta): ahora prueban el script vigente v01.2 y el contrato nuevo (`z_base = None`
   sin cota). `tests/test_orquestador.py` incluye el paso 1.2b y su cobertura.

## Verificación ejecutada
- `anclar_contexto50_zbase.py --chip AAA0030JKOE`: **90 ok, 0 fallidos, 450 puntos, 229 s**;
  `z_base_m` −21,150…−0,060 m (dispersión 21,09 m; 84 valores distintos); ajuste
  min−centroide promedio **1,06 m**, máximo 4,65 m.
- `diagnosticar-cotas-contexto.py`: `edificios con cota = 90/90`, dispersión 21,09 m. Las
  tres FALLA que quedan son las **preexistentes** de vías/EP/vecinos planos en ETAPA1
  (pendiente "opción C: drape o exclusión").
- **Regresión del fetch**: se re-ejecutó `fetch-contexto-completo_v01.py --solo-50` real →
  `Cotas MDT heredadas: 90/90` y comparación registro a registro por id+centroide:
  **90 cotas idénticas, 0 distintas**.
- **Réplica headless del componente** (stubs de Rhino, JSON real): 71/90 volúmenes, bases
  de **−6,662 a 14,428 m**, **67 valores distintos** → cada morph en su terreno.
- Paridad canvas ↔ src: **7/7 IGUAL** tras re-embeder el #45.
- Suite: **430 pasan / 10 fallan**. Los 10 fallos son **preexistentes** (verificados sobre
  `HEAD` en un worktree limpio): `test_esquina_fuente`, `test_lados_v06_fuente` (2),
  `test_morph_atributos_fuente`, `test_normativa_v09_fuente`, `test_orquestador` (2),
  `test_storysync_v02_plan` (2), `test_f3_volum_v081_zonas_stories`.

## Hallazgos colaterales (NO corregidos, fuera de alcance)
- `_generar_html()` del orquestador revienta con `KeyError: ' --ok'`: el CSS del template
  (`:root { --ok:… }`) choca con `.format()`. **`--checklist` está roto** en HEAD.
- El `.ghx` guarda el `CodeInput` con una línea en blanco entre cada línea (doble
  espaciado); el verificador de paridad lo ignora (filtra vacías). El componente #45 se
  re-embebió con espaciado normal.
- El contexto50 trae **90 registros con 45 ids**: la capa `Cons` repite `ConCodigo` para
  varias construcciones del mismo predio. Cualquier cruce por id debe ser por id+huella.
- `exports/contexto50/AAA0030JKOE-contexto50.3dm` sigue siendo el archivo **viejo**
  (todo a 14,4875): hay que re-exportarlo desde el canvas.

## Pendientes actualizados
1. Reabrir `F1_CONTEXTO_v13.6.ghx` en Grasshopper y re-ejecutar #45 (bake/exportar) →
   los 71 morphs deben caer en −6,7…14,4 m; verificar con censo/Tapir que el `min Z` de
   cada morph coincide con su `z_base`.
2. Re-exportar el `.3dm` (el actual está obsoleto).
3. `--checklist` roto (KeyError del CSS) — decidir si se corrige.
4. Sigue pendiente: drape vs exclusión de vías/EP (opción C), censo 20/20 zonas,
   `F3_StorySync_v02 --check` 8/8.

---

# Segunda parte de la sesión — ZONAS a la cota del borde bajo (2026-10-26, tarde)

## Síntoma reportado
Con el contexto ya bien localizado, los volúmenes de **ZONAS** seguían apareciendo
"localizados con base en el centroide y no contra el borde en la cota más baja".

## Causa raíz
`F3_DISTRIBUCION_v03.py` (`#200`, v03.9) calculaba la cota de arranque de cada bloque
con **una sola muestra en el centroide**:

```
cx = sum(xs)/len(xs); cy = sum(ys)/len(ys)
z0 = _terreno(cx, cy)          # una muestra
"criterio_arranque": "terreno en centroide (o cota fija)"
```

Ese `cota_arranque_m` es lo que `F3_VOLUM_GENERADOR_v08` (`#201`) usa para las zonas:
`z = cota_arranque_m + fi*floor_h` (rama `barras_implantadas_json`, DataTree de zonas).
En ladera, el bloque arrancaba a la cota del centro y su borde de aguas abajo quedaba
flotando.

## Corrección (v03.10)
- `_cotas_huella()`: muestrea **centroide + vértices + puntos medios** del borde y
  `cota_arranque_m = min(...)` (misma regla que los morphs del contexto).
- Nuevos campos por bloque: `cota_arranque_centroide_m`, `cota_arranque_max_m`,
  `cota_arranque_n_puntos`, y `criterio_arranque` explícito.
- `cota_arranque_m` como **entrada** del componente sigue mandando (cota fija del operador).
- Aviso nuevo en `avisos`: "cota de arranque por minimo de huella: bajada media X m (max Y m)".
- Re-embebido en el canvas (#200) + paridad 7/7.
- Tests nuevos `tests/test_f3_distribucion_cotas.py` (4): ladera sintética z=0,1·y → cada
  bloque arranca en su borde bajo y **no comparten cota**; cota fija manda; sin malla se
  mantiene el respaldo z0=0 con aviso.

## ¿Se puede ejecutar el .ghx sin el operador? — hallazgos
- **No hay MCP de Grasshopper** en esta sesión. El MCP del proyecto es **Tapir/ArchiCAD** y su
  API no estaba escuchando (19724 cerrado).
- **Rhino.Compute** 8.0 responde en `localhost:6500` (`/version` OK), pero `POST /grasshopper`
  con el `.ghx` (base64) devuelve **HTTP 500**: el canvas no es Hops-ready (componentes AC_* de
  Live Connection + interacción con `RhinoDoc`).
- **RhinoCode CLI** (`C:\Program Files\Rhino 8\System\RhinoCode.exe`) lista las instancias vivas
  (`rhinocode_remotepipe_12332`), pero `script -r <id>` no ejecutó el script (sin salida ni
  efectos): la sesión de shell corre como otro usuario de Windows ("Work") distinto del que
  tiene Rhino abierto ("Dario Salas").
- **Vía que sí funciona**: ejecutar el código del componente en CPython con stubs de Rhino
  (lo usado para #45 y #200). Es determinista, sin efectos laterales y reproduce los números.

## Deuda técnica asumida
Los 10 tests que fallan no se archivan: quedan registrados con causa y corrección propuesta en
`docs/planes/2026-10-26-deuda-tecnica/DEUDA-TECNICA.md` (2 defectos reales: `--checklist` y el
plan de stories; 6 tests desactualizados; pendientes operativos).

## Consecuencia operativa de esta corrección
Al bajar la cota de arranque al mínimo de la huella, el **plan de stories** debe regenerarse
(`F3_StorySync_v02 --plan`) antes de re-sincronizar niveles en ArchiCAD: la base GF baja con
los bloques.

## Verificación de esta segunda parte
- `pytest tests/test_f3_distribucion_cotas.py` → 4/4.
- Suite completa: **434 pasan / 10 fallan** (los 10 de la deuda, ninguno nuevo).
- Paridad canvas ↔ src: **7/7** tras re-embeber #200.

---

# Tercera parte (2026-10-26, tarde-noche) — puerto 19723, usuario del shell, alzado sobre la vía

## Puerto de la API de ArchiCAD: **19723** (hipótesis confirmada)
- `19723` escucha y responde a Tapir: **ArchiCAD 29 build 5101 INT** (PID de `Archicad`).
- `19724` y `19725`: cerrados. En la versión nueva de AutoClaw el 19723 quedó libre.
- Herramienta: `scripts/utilities/detectar-puerto-archicad.py` (código 0 = API hallada;
  `--json` para el MCP). Anotado como hecho verificado en `CLAUDE.md`.
- Ojo: una sonda TCP cruda (enviar JSON y esperar respuesta) da falso negativo;
  hay que usar el cliente `archicad` (`ACConnection(port=…)`; en Tapir 1.5.x no acepta `host=`).

## “El shell corre en otro usuario”: **no era cierto**
- `whoami` = `ARQUITECTURA\Dario Salas`; `quser` muestra una sola sesión (consola, id 1).
  Es el mismo usuario que tiene Rhino abierto. `D:\Users\Work\…` es solo dónde se instaló
  Python 3.12, no otro perfil.
- La causa real de que RhinoCode no ejecutara scripts era la **falta de la directiva de
  runner** `#! python3` en la primera línea. Con ella, `RhinoCode.exe -r <instancia> script …`
  ejecuta dentro de Rhino (probado: Rhino 8.36, Grasshopper importable).
  → Ya es posible pilotar Grasshopper/Rhino desde el agente sin MCP.

## Alzado del lote sobre la vía frontal (`generar-alzado-via.py`)
- **Qué dibuja:** el lote visto de frente desde su calle, con perfil del lindero y de la
  franja de calle, puntos de muestreo del MDT, líneas candidatas a `{z=0}` (color calle,
  color lindero, color mínimo del lote), la línea seleccionada y la **banda POT/PEMP**
  sombreada desde el z=0 elegido; volúmenes del contexto50 como referencia.
- **Lado frontal:** el que el canvas marcó como calle de acceso (`bloques.json` →
  `orientacion.calle_acceso.lado_id` = 25, “Occidente-2”, 14,98 m). Avenida de Los Cerros
  queda a 45 m: **no** es la vía frontal de este predio.
- **MDT:** los puntos de calle caen fuera de la malla ETAPA1 (que cubre lote + ~5 m), así que
  el muestreo va por **REST Catastro** (30 puntos, ~20 s), no por IDW. Con IDW la calle salía
  *más alta* que el lindero (extrapolación).
- **Marco de los vecinos:** el contexto50 vive en su propio marco; sin `+ancla_canvas_local`
  y `z − desplazamiento_z` los volúmenes se dibujaban a −100 m del frente. Corregido.
- **Salidas:** `exports/alzado-via/<CHIP>-alzado-via.html` (+ `.json` con el payload).
- **Integración:** paso `1.2 f1_alzado_via` del orquestador; en `servidor.py`:
  `GET /alzado?chip=…` (página interactiva), `GET /api/alzado?chip=…` (datos) y
  `POST /api/z0` → escribe `data/pot-cache/<CHIP>-z0.json` + `parametros_pipeline.json`.
- **Verificado:** GET /alzado 200 con botones y JS; POST /api/z0 escribió el datum y se
  **restauró** al valor vigente (0,2661 / `min_lote` / 2634,7871) tras la prueba.
- **Datos del caso (AAA0030JKOE):** calle 0,03–0,15 m · lindero 0,27–1,76 m ·
  mínimo del lote 0,27 m · altura PZCB 7,00 m.

## Deuda técnica: de 10 fallos a 1
Cerrados A1 (checklist), B1–B6 y A2a (tests del plan al marco ADR-024).
Abierto A2b: **dos planificadores de stories** (F3_VOLUM en marco de cálculo vs StorySync en
marco ArchiCAD) — requiere decidir cuál es canónico. Detalle en
`docs/planes/2026-10-26-deuda-tecnica/DEUDA-TECNICA.md`.

## Verificación de la tercera parte
- `pytest` completa: **450 pasan / 1 falla** (solo A2b).
- `run_pipeline_v01.py --status` lista “1.2 Alzado sobre la vía frontal (z=0)”.
- `run_pipeline_v01.py --checklist` genera el HTML (antes reventaba).
- Paridad canvas ↔ src: 7/7 (sin cambios de canvas en esta parte).

## Alzado v2 — escala de vecinos laterales y los cuatro lados del lote
Petición del operador: que se vea la cara (a escala) de los vecinos **inmediatamente
laterales** y que estén marcados **todos los lados** del lote, como referencia de
las diferencias de altura.

- **Vecinos con rol**: `vecinos[].rol` = `lateral_izq` / `lateral_der` / `frente` / `fondo`.
  Lateral = mismo paramento (`|prof| ≤ 12 m`) y huella que toca el extremo del frente
  (`x ≈ 0` o `x ≈ L`). Se dibujan con cara rellena, contorno y su **altura rotulada**,
  y su altura entra en la ventana vertical → comparación a escala real.
- **Los cuatro lados**: `lados_lote[]` (Frente, Lateral del extremo izquierdo,
  Lateral del extremo derecho, Posterior) con `z_min`, `z_max`, `desnivel_m` y
  `largo_m`. Se rotulan: esquinas del frente con su cota, línea del fondo del lote,
  **planta en miniatura** con los lados (F/L/P) y **tabla** bajo el gráfico.
  La segmentación es geométrica (normal de cada arista + tramo contiguo más largo)
  porque el chip **no tiene exportado** el cuadro de lados del canvas (`<CHIP>-lados.json`).
- **Panel “Detalle del datum”**: segundo SVG con zoom (x2) de la zona de decisión;
  el alzado principal está a escala real (incluye vecinos de 11–20 m), así que las
  cinco líneas candidatas quedan a pocos píxeles y el detalle las separa.
- Verificado: 9/9 tests del alzado; suite **452 pasan / 1 falla**.

## Alzado v3 — cota absoluta (msnm) por linea propuesta
- Cada línea candidata, la seleccionada y las esquinas muestran **cota local + cota msnm**
  (en el alzado, en el detalle y en la tabla).
- **Regla:** `msnm = z_local + origen_sirgas.z`, con `origen_sirgas.z = 2634,521` para
  AAA0030JKOE (el marco local del canvas arranca en el mínimo del MDT, NO en el ancla del lote).
  Cota del frente: **2634,56–2636,28 msnm**; z=0 vigente: **2634,79 msnm**.
- **Corrección de paso:** `_z0_guardar` (servidor) sumaba ADEMÁS `ancla_canvas_local.z`
  (14,52 m) al calcular `z0_abs_m`; el valor bueno es `origen_sirgas.z + z0_m`
  (2634,7871 para z0 = 0,2661, que es el que ya estaba en `parametros_pipeline.json`).
- Verificado: 10/10 tests del alzado; suite **453 pasan / 1 falla**.

## Alzado v4 — StorySync canonico, lados del canvas, predio propio fuera y colores
- **StorySync canónico (A2b cerrado):** `F3_VOLUM_GENERADOR_v08._plan_stories` emite el
  mismo esquema ADR-024 que StorySync (`elevation` marco ArchiCAD, `zgf_m`,
  `elevacion_modelo_m`); el JSON exportado agrega `zgf_m`. Re-embebido #201 → paridad 7/7.
  Suite: **457 pasan / 0 fallan**.
- **Flag de LADOS:** el generador del alzado enciende `data/pot-cache/lados-export-flag.json`
  cuando falta `<CHIP>-lados.json`, para que el canvas lo exporte y quede como **fuente única**
  de linderos. El alzado informa qué fuente usó (`lados_fuente`).
- **Predio propio fuera:** se excluyen los edificios del contexto50 con la mayoría de sus
  vértices dentro del lote (`excluidos_predio_propio = 2` en AAA0030JKOE). El volumen
  construido del predio no se dibuja nunca.
- **Colores por lindero:** se usa la MISMA paleta de la planta de selección de vías
  (`index.html`: via #2563eb, via_no_frontal #60a5fa, predio #d97706,
  espacio_público #16a34a, libre #9ca3af). El tipo de cada lado se deriva geométricamente
  si no hay lados.json: Frente=via, laterales=predio, posterior=espacio_público.
- **Niveles:** se dibujan solo con un plan en esquema ADR-024 (línea + nombre + escalera
  vertical con el entrepiso). Si el plan está en marco viejo, **no se dibuja** y se avisa
  (evita líneas 12 m bajo el terreno). Hoy `casos/AAA0030JKOE/niveles_deseados.json` está
  en marco antiguo → regenerar con `F3_StorySync_v02 --plan`.
- Verificado: 13/13 tests del alzado; suite completa 457/0.

## Altura reglamentaria: 10,00 m (verificado) — NO 7,00 m
- **Origen del 7,00 m (error):** `ALTURA_CODIGOS_ESPECIALES` del fetch v7 traduce el codigo
  `CHB` de la GDB a **7,0 m** por tabla. En AAA0030JKOE la GDB devuelve `CHB` por error
  (el predio **no** es patrimonio, segun la nota del propio override desde 2026-09-28).
- **Por que no se corregia solo:** `_aplicar_norma_override()` **no mapeaba**
  `altura_maxima_m`; solo derivaba la altura de los pisos *si el campo estaba vacio*, y el
  CHB ya lo habia llenado con 7,0.
- **Verificacion:** la nota normativa del chip ya decia *"altura maxima 10 m (referencia
  tipologica)"*; el operador lo confirmo en **visita fisica al IDPC (2026-10-26)**.
  10,00 m es el valor vigente; 7,00 m queda solo como referencia PZCB.
- **Correccion:** `fetch-urban-context-v7._aplicar_norma_override` ahora mapea
  `altura_maxima_m`, `altura_maxima_m_referencia_pzcb` y `altura_maxima_fuente`;
  `data/pot-bogota/norma-override.json` fija 10,0 m con la fuente IDPC; `pot_data` de los
  tres contexto vivos quedo en 10,0 m. Anotado en CLAUDE.md (trampa del CHB).
- **En el alzado:** banda a **10,00 m** (linea verde) + linea roja discontinua de
  **referencia PZCB 7,00 m**; los niveles que superen la altura vigente se pintan en rojo.

## Mejoras didacticas aplicadas al alzado
1. **Escala grafica** (regla de 10 m) dentro del dibujo.
2. **Cota acotada vertical** del vecino lateral mas alto (`vecino 11,40 m`), para leer
   alturas sin calcular.
3. **Rotulos F / L / P** en los extremos del alzado (frente y laterales).
4. **Panel comparativo del datum:** la misma seccion con z=0 en `min_lote` (+0,27 m,
   2634,79 msnm) vs en la calle baja (+0,03 m, 2634,56 msnm), con el techo permitido de cada
   escenario y el delta (0,23 m).
- Verificado: 15/15 tests del alzado; suite completa **459 pasan / 0 fallan**.
