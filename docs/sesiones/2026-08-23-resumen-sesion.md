# Resumen de sesión - 2026-08-23 (tarde)

**Tema:** Override de norma (completar datos faltantes de la geobase POT) +
diagnóstico del GFA de AAA0240ZXJH (UPZ 41 Muzú).

## Contexto
El GFA del lote AAA0240ZXJH quedaba clavado en 46,3 m² con huella 46,3 m² en vez
de ~64–68 m². Se diagnosticó que eran dos problemas: (1) la conexión
Grasshopper↔ArchiCAD cerrada (LADOS con geometría NoneType) y (2) datos normativos
faltantes/erróneos en la geobase POT para Renovación (`rango_edificabilidad = "1"`
en vez de "3"). Se implementó un override de norma editable desde el orquestador.

## Errores encontrados
1. **GFA/huella 46,3 m²**: conexión GH↔ArchiCAD cerrada → `vias_curves`/
   `vecinos_curves` NoneType → 2 lados "Frontal" (fallback) → doble retiro.
2. **`rango_edificabilidad = "1"`**: fetch leía `Rango_edificabilidad_desarro`
   (capa de Desarrollo) para un lote Renovación; `ALTURA_MAXIMA` en blanco → 1 piso.
3. **`io_maximo` exportado = 4,0** (no 0,70): cableado EXPORTAR_GFA.io_maximo ←
   NORMATIVA.ic_maximo (pisos) en vez de io_maximo.
4. **`tratamiento` "Consolidación"** en `proyecto.json` vs "Renovación" en geobase.
5. **"Edificio Deysy"** (proyecto del orquestador) con chip vacío + tratamiento
   "Consolidación".

## Modificaciones solicitadas
1. Override de norma presentado en el orquestador y editable desde ahí, para
   completar los datos faltantes del GeoJSON base.
2. Reconciliar el tratamiento.
3. Dejar la nota del documento exacto (fuente), sin OCR por ahora.
4. Renombrar "Edificio Deysy" → "EdificioDeysy".
5. Script de verificación post-run del GFA.

## Lecciones aprendidas
1. La geobase POT es incompleta para Renovación/Consolidación → override por CHIP.
2. El override debe ganar sobre la geobase y limitarse a lo faltante/incorrecto.
3. El código usa `ic_maximo` como nº de pisos (no ratio IC) → confusión io/ic.
4. El NoneType de LADOS era conexión cerrada, no código → reiniciar en orden.
5. Los PDF de UPZ_CONSOLIDACION son escaneados → cita/referencia, no fuente automática.

## Soluciones entregadas
- `data/pot-bogota/norma-override.json` (clave por CHIP) + entrada Muzú 41.
- `fetch-urban-context-v6.py`: fusón del override en `pot_data`.
- `servidor.py` + `index.html`: `GET/POST /api/norma-override` + panel.
- Reconciliación `tratamiento` + `EdificioDeysy`.
- Fuente exacta (ficha + resolución 00865/2006).
- `scripts/utilities/verificar-gfa.py`.

## Pendientes de esta sesión
1. Reabrir Live Connection GH↔ArchiCAD y re-ejecutar canvas F1 (manual).
2. Reconectar `io_maximo` en EXPORTAR_GFA (manual en canvas).
3. Correr `verificar-gfa.py` → todo OK.
4. OCR de la ficha (deferido).
5. F2: `recursos_disponibles`, `saldo`, `financiacion_saldo[]`, acabados, multi-escenario.

## Commits
- `cierre(f1+orq)`: override de norma + verificar-gfa + EdificioDeysy (2026-08-23).


---

# Resumen de sesión - 2026-08-23 (noche)

**Tema:** nomenclatura cardinal, frente `via_no_frontal`, conflicto de puerto 19723
y diagnóstico del lote AAA0240ZXJH (área, orientación, coordenadas y financiero).

## Soluciones entregadas (commits)
- `898a50a` LADOS **v06.2**: cardinal por lado (misma convención que NORMATIVA_v08
  y `vecinos_por_lado.py`) + guard `MAX_ANCHO_VIA_M = 100.0` + test.
- `e870c49` Frente **`via_no_frontal`** (vía sin antejardín) en NORMATIVA + UI del
  orquestador (FRENTES/CICLO_FRENTE/COLORES/ETIQUETA/leyenda) + 3 tests.
- `3f3ff83` **`via_no_frontal` cuenta como vía** en la regla de esquina (v08.3) +
  docs del conflicto de puerto 19723 (CLAUDE.md, MANUAL_DE_EJECUCION.md, scripts).
- `15a98b7` `diagnostico_puerto_19723.ps1 -Liberar` reporta fallo real (acceso
  denegado) + fallback `Stop-Process -Force` + sección "ESTADO REAL".
- `b49aa717` + `adbba01f` cleanup git: 24.460 derivados des-versionados.

## Errores encontrados (nuevos, pendientes de corrección)
1. **Área del lote en orquestador = 450 m²** vs real 99,72 m² (el contexto JSON ya
   trae `area_m2: 99.72` correcto; sospecha: chip por defecto AAA0127AZPA o sección
   distinta). El SVG sí muestra el área correcta.
2. **Codificación HTML** en sección 2 (normativa): `Antejard&iacute;n frontal
   m&iacute;nimo (m)` mostrado literal (entidades HTML sin decodificar). Además hay
   mojibake generalizado en .py/.md/.json (`Antejard�n`, `Segǧn`, `consolidaci��n`).
3. **El canvas corre código viejo**: salida "LADOS v06.1" y "NORMATIVA v08.1" pese a
   que los .py ya son v06.2/v08.3 → re-exportar los GHPython al .gh/.ghx.
4. **Salida LADOS sin nicknames** (nombres del orquestador) → no se puede validar por
   qué la clasificación no coincide con la realidad.
5. **Clasificación errónea**: 2 lados "Frontal" (auto) vs ground-truth (1 frontal +
   1 `via_no_frontal`); `Vias:3` con ancho 41,65 m.
6. **Geometría en frame incorrecto (ROOT CAUSE del GFA)**: `ep:41.26m`, `via 41.7m`,
   Ocup 1,6 m², GFA escalonado 27,9 m² → la vía/EP/vecinos están en coordenadas
   distintas al lote (global SIRGAS vs local). El lote sí está bien (99,7 m²).
7. **Parámetros financieros por defecto** ("sin archivo específico del CHIP"): no hay
   `parametros_AAA0240ZXJH_*`; el valor del lote debe ser el primer INPUT (no output)
   y los valores de referencia de mercado deben poder editarse.
8. **Sin persistencia por CHIP**: al re-seleccionar el mismo CHIP no se restauran las
   variables de 1b-1c ni la normativa.
9. **1b-1c muestra todos los vecinos**; debe aparecer solo en "+Agregar" (y dentro,
   la opción Oriente/Sur/Occidente/Norte sobre el lote seleccionado).

## Modificaciones solicitadas
- Incluir nicknames en la salida LADOS/NORMATIVA.
- Corregir área, codificación y persistencia del orquestador.
- Validar ancho de vía y marco de coordenadas (regla de desplazamiento global).
- Parámetros financieros por CHIP (mercado editable, lote como input inicial).
- 1b-1c: lista de vecinos solo en "+Agregar" (el SVG ya resuelve la selección).
- Documentar nombres canónicos de archivos de intercambio para el canvas.

## Lecciones aprendidas
1. La consola PowerShell corrompe acentos (cp1252); escribir/editar siempre con
   `encoding="utf-8"` y no manipular tildes por shell.
2. El .gh/.ghx embebe el código Python al guardar: editar el .py NO actualiza el
   canvas → re-exportar el componente GHPython tras cada cambio.
3. `ep:`/`via:` en LADOS/NORMATIVA miden distancia en el frame de la geometría; un
   valor ~41 m delata coordenadas globales (SIRGAS) en vez de locales.
4. El valor del lote es input del análisis financiero (punto de partida), no output.

## Pendientes (orden sugerido)
1. Corregir área 450 → 99,72 en orquestador (verificar chip por defecto).
2. Decodificar entidades HTML + normalizar mojibake en labels.
3. Re-exportar F1 (LADOS v06.2, NORMATIVA v08.3) al .gh/.ghx.
4. Añadir nicknames a la salida LADOS/NORMATIVA.
5. Corregir frame de coordenadas de EP/vía/vecinos (validar en Rhino/ArchiCAD).
6. Parámetros financieros por CHIP + mercado editable + lote como input.
7. Persistencia de variables por CHIP.
8. 1b-1c: vecinos solo en "+Agregar".

## Commits
`898a50a`, `e870c49`, `3f3ff83`, `15a98b7`, `b49aa717`, `adbba01f`.
