# Resumen de sesión 2026-09-29 — Acople §2→§4 (usos → modelado) + parámetros básicos de bloques

**Tema:** corrección del desacople entre la sección 2 (Normativa/usos) y la sección 4 (Modelado)
del orquestador, y primera implementación de la lógica de multivolumen (nº de bloques,
distribución, desniveles). *(Terreno/polilíneas en ArchiCAD: en curso — canvas v12.)*

---

## Tema 1 — Acople sección 2 → modelado (usos/normativa → F3)

**Actividades propuestas:** que "Generar masa (F3)" y "Pipeline completo" produzcan el modelado
correspondiente a lo solicitado en las secciones 2–3 (usos, normativa, escenarios), eliminando el
caso pre-generado como fuente de la generación.

**Actividades realizadas:**
- `F3_DISTRIBUCION_v02.py`: nuevo `--usos` que filtra el mix del escenario F2 a los usos marcados
  y renormaliza `pct_gfa`/`gfa_m2`/unidades (GFA total conservado). Mapeo de etiquetas UI:
  "Comercio…"→`Local comercial`, "Salud"→`Consultorios`, "Salud✱/institucional"→`Institucional salud`.
- `servidor.py`: `/api/generar-f3` y `/api/pipeline` aceptan `usos`; `_derivar_escenario_f3()`
  infiere `D_MIXTO_SALUD` cuando hay usos de salud (si no, `D_MIXTO`); `_generar_f3` construye el
  comando F3 con `--usos`.
- `index.html`: la sección 4 muestra en vivo "Se modelará según §2–§3: escenario · usos · bloques";
  los botones envían la selección real del formulario.
- El selector de la sección 4 pasó a llamarse "Escenario pre-generado (referencia)" (solo VER).

**Resultados:** B regenerado con mix completo (5 niveles, huella 663 m²). Con `--usos "Vivienda"`
se obtiene el programa solo-vivienda renormalizado (núcleo 1 ascensor, balance 3069,5). Tests
nuevos 7/7; suite relacionada 19/19.

**Condiciones y limitaciones:** el filtro renormaliza porcentajes (no re-optimiza el mix
financiero); la optimización fina del mix por escenario sigue siendo tarea del motor F2.
**Validación esperada:** en el front-end, el texto "Se modelará según §2–§3…" debe reflejar
cualquier cambio de usos/bloques antes de pulsar el botón.

---

## Tema 2 — Multivolumen: parámetros básicos (bloques)

**Actividades propuestas:** poder definir cuántos bloques salen, cómo se distribuyen en el lote y
las diferencias de altura entre uno y otro (caso inclinado La Candelaria).

**Actividades realizadas:**
- Parámetros en la sección 4: `bloques_num` (1–6), `bloques_distribucion` (a lo largo/ancho del
  lote), `bloques_separacion_m` (mín. 6,00 m, Anexo 5 §1.10.b), `bloques_desnivel_m` (negativo
  desciende).
- `generar_bloques()` en F3 v02: corta el **polígono real del lote** (mín. rectángulo rotado) en
  N franjas con la separación pedida (clamp a 6,00 m con aviso), recorta cada franja contra el
  lote y escribe `bloques.json` con: `id`, `poligono_local`, `area_lote_m2`,
  `huella_objetivo_m2`, `pisos`, `z_base_m = i × desnivel_m`, `gfa_objetivo_m2`.
- El resumen de bloques se adjunta a `programa-areas.json` (`bloques`) y la fila `bloques` quedó
  en `ARCHIVOS_INTERCAMBIO.md` como contrato para el canvas (VOLUM v09).

**Resultados:** corrida de 3 bloques OK (separación 6,00 m, desniveles 0/−3,4/−6,8 m, polígonos
del lote de La Candelaria). Suite verde.

**Condiciones y limitaciones:** los polígonos son un reparto esquemático del lote (sin retiros);
el re-encaje fino en la envolvente F1 y las cotas de terreno se harán en el canvas v09.
**Validación esperada:** con n>1, el mensaje del botón F3 indica "N bloques (sep, desnivel)".

---

## Tema 3 — Terreno en ArchiCAD 3D y polilíneas drapeadas (en curso)

**Diagnóstico (de la validación):**
- Las polilíneas se aplanan a Z=0 (fix v04.2 para la Live Connection) → no siguen el terreno.
- `topo_mesh` existe en el canvas (#21) pero quedó **huérfana** (sin nodo LC de malla).
- Los elementos enviados por "2D Polyline" son elementos 2D de planta → **no visibles en 3D**.

**Plan (canvas v12 — no pisar v11):**
- ETAPA1 v05 con salidas drapeadas: `terreno_mesh` (ya existe como topo_mesh) + bandas de
  perímetro (lote/vecinos/vías/EP) como mallas de cinta que siguen la cota del MDT.
- Parche por GUID: agregar nodos LC "Morph Solid" para (a) terreno → capa
  `10-20-10_Topografia`, (b) banda del lote → `00-00-10_Lote_proyecto` (y por capas para el
  resto); regenerar `.gh` y validar en sesión viva (AutoClaw cerrado; puerto 19723).

**Resultado esperado:** vista 3D de ArchiCAD con terreno + perímetros visibles y volúmenes
vecinos anclados a cotas (`z_base_m`).

---

## Verificación de esta sesión
- `pytest tests/test_f3_bloques_usos.py tests/test_f3_chip_generico.py tests/test_orquestador.py` → **19/19**.
- Smoke servidor: derivación de escenario y variables nuevas OK.
- `node --check` del JS del front-end → OK.
- Corrida canónica B (mix completo) regenerada.

## Documentos
- `src/fase-3-masa/F3_DISTRIBUCION_v02.py` · `src/orquestador/servidor.py` · `index.html` ·
  `tests/test_f3_bloques_usos.py` · `casos/AAA0030JKOE/bloques.json`
- READMEs actualizados (raíz, fase-3, orquestador, ARCHIVOS_INTERCAMBIO).
- Memoria: `D:\Work\PROJECTS\DiseñoParametrico\memory\sesion-2026-09-29-acople-seccion2-modelado.md`.

## Etiquetas
#fase-3 #orquestador #multivolumen #terreno #candelaria
