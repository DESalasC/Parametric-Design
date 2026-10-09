# Sesión 2026-10-09 — Fixes salidas F1/F3 + robustez (F1 v09.2 · UNIDADES v02.2 · ACCESOS v02.2 · DISTRIBUCION v03.5)

## Contexto
Tres errores reportados tras corridas del canvas v13.1.1:
1. F3_ACCESOS_INTEGRADOR_v02: "ERROR: sin layout_espacial.json".
2. F3_UNIDADES_TIPOLOGIAS_v02: "ERROR: Precision not allowed in integer format specifier".
3. F1_ETAPA2_NORMATIVA_v09.1: salidas envelope_curve / envelope_por_piso con items "IronPython.Runtime.List".

## Causas raíz
- ACCESOS: entrada layout mal cableada a unidades_json (8f8d6966); cuando UNIDADES fallaba entregaba "" -> "sin layout". Además el parser solo tomaba el primer elemento de listas.
- UNIDADES: (a) IronPython 2.7 rechaza precisión ({:.1f}) aplicada a ENTEROS; (b) el escaneo de globales capturaba la constante USO_LAYOUT_A_OBJETIVO como "layout" (resultados basura: 0 unidades / 40 sótanos); (c) load_json usaba open(..., encoding=) — no soportado en IronPython — y no podía leer de disco.
- F1: barras_huellas llega del JSON como [piso][barra][puntos]; el aplanado previo solo bajaba un nivel y seguía publicando listas de puntos (no curvas) -> IronPython.Runtime.List.
- F3_DISTRIBUCION_v03: su salida #7 layout_espacial_json nunca se asignaba — por eso UNIDADES/ACCESOS veían vacío.

## Fixes aplicados (commit 7ddd09e + follow-up)
- F1 v09.2: helpers _huella_a_curva/_huellas_a_pisos/_aplanar_pisos/_publicar_por_piso; envelope_por_piso y envelope_aprobado_por_piso = árbol por piso (ghpythonlib.treehelpers) con respaldo lista-de-listas; envelope_curve = PolylineCurve del piso base.
- UNIDADES v02.2: float() en todos los specs {:.1f}/{:.2f}; cola de traceback en mensajes de error; respaldo de layout desde disco (casos/<chip>/ o el más reciente, validado); guard __main__.
- ACCESOS v02.2: parser JSON multi-forma con validación de contenido (layout/matriz); respaldo de disco; mensaje con candidatos probados; guard __main__ (arregla import en tests).
- F3D v03.5: publica layout_espacial_json leyendo casos/<chip>/layout_espacial.json (o el más reciente); lo indica en el mensaje.
- Canvas F1_CONTEXTO_v13.1.1.ghx (16:34): recarga de los 4 scripts; se conservó el recableado del operador (16:24) ACCESOS.layout <- UNIDADES#8 (ea77dff8), funcional con el fix F3D; revertido un swap accidental del panel #96.
- tests/test_f3_distribucion_v03_gh.py: mensajes esperados actualizados a "F3 v03.5".
- Backups: gh-definitions/F1_CONTEXTO_v13.1.1.ghx.bak-20261009-163423 (pre-parche) y copias ORIG_*.py en el tmp de AutoClaw.

## Verificación
- Simuladores con IronPython 2.7 real (DLLs de Rhino 8 + Lib): UNIDADES cableado/disco OK (idénticos, con nota de fuente); ACCESOS 6 variantes OK (incl. texto vacío, JSON equivocado, DataTree, BOM, disco); F3D publica layout válido (3134 B); F1 aprobado -> [5 pisos][2 curvas PolylineCurve], potencial sin crash.
- pytest: 70/71 (.venv). La única roja, test_modo_potencial_sin_barras, es del v09 legacy con stub y ya estaba roja sin relación (sin cambios vs HEAD en v09/stub/test).

## Pendientes
- Validación viva en canvas por el operador: reabrir F1_CONTEXTO_v13.1.1.ghx (cerrar la sesión de GH SIN guardar para no pisar el parche).
- Revisar aparte el test legacy v09 (potencial).
- Opcional: ACCESOS.layout podría cablearse directo a 2f5b4ab4 (hoy vía UNIDADES#8; ambas rutas funcionan).
