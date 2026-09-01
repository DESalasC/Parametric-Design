# Ejecución del canvas por Tapir — DiseñoParametrico (F0 → F3)

## Qué es "Tapir" en este proyecto

Tapir es el protocolo JSON-RPC del **ArchiCAD Python API** (paquete Python
`archicad` de Graphisoft), que conecta al CommandConnection de ArchiCAD en el
puerto **19723** (en este equipo, 19724 en la práctica). Ya lo usa
`src/interfases-archicad/F3_StorySync_v01.py` para LEER los Stories de ArchiCAD.

> No confundir con los componentes AC_* de la Grasshopper–ArchiCAD Live
> Connection (plugin Graphisoft), que es la vía por la que F3 envía los Morphs.

## Objetivo

`F0_LOAD_PROYECTO_v01` lee `proyecto.json` al resolver el canvas. Ya está
cableado; falta **disparar la solución sin clic manual**: re-escribir el
`proyecto.json` (lo hace el formulario `POST /api/proyecto`) y provocar que el
canvas se recalcule.

## Tres vías (de menor a mayor automatización)

| Vía | Cómo dispara | Limitación |
|---|---|---|
| **1. Auto-solve de Grasshopper** | Mantener "Recompute" automático en el canvas; al re-escribir `proyecto.json`, GH recalcula solo. | Requiere sesión de Rhino/GH abierta y el toggle de recálculo activo. |
| **2. Rhino.Compute / Hops** | Exponer la definición F1 como endpoint REST (`scripts/rhino-compute/`) y recomputar headless. | La Live Connection necesita la sesión viva de ArchiCAD; no sirve para el flujo con Morphs en vivo. |
| **3. Tapir (ArchiCAD API)** | Un script del paquete `archicad` (a) confirma conexión a ArchiCAD, (b) re-escribe `proyecto.json`, (c) verifica Stories. Es el "gatillo" del lado ArchiCAD que confirma que la Live Connection está lista; no dispara GH directamente. | El paquete `archicad` (ac29) solo expone LECTURA (GetStoryNavigatorItems); no dispara la solución de GH. |

## Acción pendiente (decisión del operador)

El disparo real del canvas depende de **qué vía** se quiere automatizar:

1. Si basta con **recálculo automático** (vía 1): solo falta activar el
   auto-solve del canvas y confirmar que `ruta_json` apunta al `proyecto.json`
   del orquestador (`data/activo/proyecto.json`; espejo reescrito por
   `POST /api/proyecto` en cada guardado, ver Actualizacion 2026-09-01).
2. Si se quiere **disparar desde ArchiCAD** (vía 3): construir un script Tapir
   que conecte (`ACConnection.connect(19723)`), lea stories (como
   `F3_StorySync_v01`), re-escriba `proyecto.json` y emita un log de "listo".
   No reemplaza el clic de resolver de GH: solo automatiza el lado ArchiCAD.
3. Si se quiere **recompute headless** (vía 2): usar Rhino.Compute/Hops, con la
   salvedad de que no aplica al flujo Morphs/Live Connection en vivo.

## Recomendación

Para el flujo actual (Rhino + ArchiCAD abiertos, Morphs por Live Connection), la
vía más directa es la **1 + 3 combinadas**: el formulario re-escribe el JSON y
un script Tapir confirma el estado de ArchiCAD; el operador conserva el clic de
resolver en GH (o deja el auto-solve). Implementar la vía 3 es el siguiente paso
concreto; la vía 2 se reserva para cuando se quiera CI/headless sin ArchiCAD.

## Actualizacion 2026-09-01 - espejo activo `proyecto.json`

`POST /api/proyecto` escribe, ademas del proyecto con nombre o `_provisional`,
un **espejo literal** en `data/activo/proyecto.json` (constante
`ACTIVO_PROYECTO` en `servidor.py`). Esa es la ruta estable que debe consumir
`F0_LOAD_PROYECTO` via el input `ruta_json`: al re-seleccionar chip/caso o
guardar variables, el espejo se reescribe y el canvas recalcula sin tocar el
cableado. Con esto queda cerrada la parte de datos del pendiente #4 del
cierre 2026-08-23 (activo `proyecto.json` espejo); la eleccion de via de
disparo (1+3 combinadas) sigue abierta para la proxima sesion.
