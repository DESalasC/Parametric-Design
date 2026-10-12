# Sesión 2026-10-11 (noche) — Implantación multivolumen como ZONAS · canvas v13.5 · limpieza

## Situación
Continuación del trabajo F3 sobre el canvas del proyecto (`F1_CONTEXTO_v13.2.ghx`, re-guardado por el operador el 10-10 13:50 y durante la noche del 10-11). El objetivo fue llevar la "implantación multivolumen" (bloques escalonados por plataformas) hasta ArchiCAD vía Live Connection, con validación en vivo del operador (puerto 19724, orden de arranque AutoClaw→ArchiCAD→Rhino).

## Problemas planteados y resolución
| # | Problema | Resolución |
|---|----------|------------|
| P1 | `Runtime error: Huella invalida B1-R1` en F3_VOLUM #114 | La huella v03.6 se emitía ABIERTA; el bloque "Implantacion" exige polilínea cerrada → **v03.6.1** (huella_xy CERRADA) + **v08.0.1** (cierre defensivo). |
| P2 | Franjas dejaban vacío posterior y no tocaban frentes; pisos fijos | **v03.7**: anclaje frente/fondo + remanente repartido en separaciones; **pisos por bloque** (`pisos_por_bloque` / `limites_pisos_json` + redistribución al último bloque). **v03.7.1**: mensajes v03.7 + 2 entradas agregadas por parche + nick. |
| P3 | Separación lateral vs vecino norte (2 pisos) no se aplicaba (norma 1/5) | **v03.8**: `sep_lateral_json` → retiro por piso `r = 0` hasta empate; luego `max(0.2·(z−h_vecino), min_retiro_m, 0.02·z)`; `huella_xy_por_piso` por bloque; **#114 v08.0.2** usa huellas por piso. Verificado en canvas: `retiros por piso 0.00, 4.00, 4.00, 4.00, 4.00` (min 4 m aplicado). |
| P4 | "Se perdieron los bloques" (volvieron los 2 volúmenes de 20 m) | Corrida de una sesión a medio actualizar; tras re-guardar/re-correr la propuesta salió OK: `F3 v03.8 | 4 barras...` + `IMPLANTACION F3 | ALT-4B-305 | 4 bloques | 20 zonas`. |
| P5 | "No cambió nada visible en ArchiCAD" | Diagnóstico: (a) **stories insuficientes** (solo 0/1/2) para las cotas del modelo; (b) **cadena de morphs F3 inexistente** (#213 sin consumidores; el único Morph es del contexto) + `salida_morph=false` + implanta emite Brep (LC Morph pide Mesh); (c) retiros frente/fondo > 0 en base; (d) aviso "no alcanza borde derecho" + margen 145 m² (borde diagonal/base). → Pendientes. |
| P6 | Versionado/limpieza | Canvas → **v13.5** (22:18; nombre interno corregido); **encabezados** recortados a las últimas 3 subversiones con "versión actual + genérica"; **limpieza**: 193 archivos desactualizados a `gh-definitions\_archive\2026-10-11\`; scratch de `scripts\utilities` → `_old\`; `__pycache__` fuera. |

## Decisiones (ver ADR-023 y acta)
- **D1 — SOLO Zonas, SIN morphs** para la propuesta de implantación (decisión del operador al cierre: más fáciles de trabajar en ArchiCAD y útiles para la fase climática). La cadena LC Morph para F3 no se construye; los volúmenes quedan en GH/Rhino para análisis.
- D2 Anclaje a frentes + separaciones ajustadas (sin huecos no válidos).
- D3 Pisos por bloque con redistribución automática al último bloque.
- D4 Escalonamiento 1/5 configurable (`min_retiro_m` 0 puro / 4 m "más generoso" BIC).
- D5 **Numeración canónica del canvas = #Fancy Names** (por posición; renumera en cada corrida; su salida `inventario` es la fuente). Referenciar componentes por nombre de script; el etiquetador toma el token `.py` de las primeras líneas.
- D6 Canvas vigente = v13.5; futuras correcciones apuntan a ese archivo.

## Estado verificado
- Parches aplicados al canvas en vivo: v03.6 (21:04) · f1fix (21:21) · v03.7 (21:48) · v03.7.1 (22:04) · v03.8+v08.0.2 (22:15); `.gh` regenerado en cada paso.
- Tests: `test_f3_distribucion_v03_gh` **21/21** (reescrito con fixtures `base_normativa_json`); `test_f3_volum_v08_fuente` 8/8.
- Toggles: `salida_zona=true`, `Zone.Sync=true`, `salida_morph=false`.
- Herramientas vivas (`inventario-canvas.py`, `sync-canvas-to-src.py`) apuntando a v13.5.
- Docs: `docs/planes/2026-10-11-implantacion-niveles-zonas/` (PLAN · F0 · INVENTARIO v13.5 · REF-NOMENCLATURA-BEP).

## Pendientes (nuevos)
1. **Stories para ArchiCAD** (bloqueador para ver zonas/geometría bien ubicadas): obtener cotas de arranque de los 4 bloques (hoverear `zonas_atributos.z_base_m` o agregar al mensaje) → `niveles_deseados.json` + `F3_StorySync v02 (--plan/--check)`; creación manual asistida (la API no crea stories).
2. **Zonas finales**: cablear Category/Layer/Subfloor/ID/Property Settings; áreas netas (descuento de núcleo hoy "BRUTAS").
3. **Base**: retiros frente/fondo = 0 (`antejardin_m=0` en v10 / override posterior).
4. **Aviso "no alcanza borde derecho" + margen 145 m²**: revisar borde diagonal del lote / retiros de base.
5. Recargar encabezados limpios en el canvas (próximo parche).
6. Re-validar en AC tras stories (correr y ver zonas).

## Pendientes (arrastre)
- Suite de tests: rojos antiguos por limpiar (patio, orquestador, lados, esquina, normativa legado).
- Validación viva caso B + prevalidación.
- Dataset mixto nuevo escala actual + mix AAA0240ZXJH.
- contexto50: verificación en vivo de `z_base_m`.
- Puerto 19723: orden de arranque "entre comillas"; falta respuesta formal de soporte; tarea programada portproxy.
- Estación: ventana de mantenimiento; discos E/F/G; reporte WebView2.
- F4/F5: salidas F3 → F4; Tapir.

## Archivos clave
- Canvas: `gh-definitions/F1_CONTEXTO_v13.5.ghx` / `.gh`
- Código: `src/fase-3-masa/F3_DISTRIBUCION_v03.py` (v03.8) · `src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py` (v08.0.2)
- Parches: `scripts/utilities/patch-ghx-v132-f3dist-v036/v037/v0371/v038*.py` · `patch-ghx-v132-f1fix-2026-10-11.py`
- Tests: `tests/test_f3_distribucion_v03_gh.py`
