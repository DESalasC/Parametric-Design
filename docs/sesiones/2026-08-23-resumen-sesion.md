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
