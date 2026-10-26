# Sesión 2026-10-25 — Revisión de estado y diagnóstico de alturas (DiseñoParamétrico)

## Contexto

Sesión de revisión tras el cierre del 2026-10-18/21. El operador reportó acciones no registradas
(borrado de zonas, creación manual de niveles en ArchiCAD), el work-around del puerto 19723 y la
resolución de los problemas de rendimiento. Quedaba pendiente el problema de diferencias de alturas
entre contexto y lote.

## Verificado

- Repo limpio; último commit `2cf01024` (2026-10-21).
- Canvas vivo: `F1_CONTEXTO_v13.6.ghx`.
- Paridad canvas ↔ src: **3 desfases** (#45, #81, #73) → sincronizados → **7/7**.
- Suite: **367 pasan / 7 fallan** (stale conocidos, sin fallas nuevas).
- Datum AAA0030JKOE: cierra (delta 0,4 mm); `Z_base` 0,030 m; `desplazamiento_z` −14,488 m;
  lote local 0,236…14,488 m.
- Capas planas ETAPA1: vías 4 685/4 685, EP 1 522/1 522, vecinos 2 501/2 501 con z = 0.
- Vecinos contexto50: 14 comparables dentro de la malla; residuo −4,17…+2,00 m (promedio −0,83).
- Muestreo MDT: un punto por centroide → causa estructural del residuo.

## Cambios aplicados

1. `src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01.2.py`: `z_origen = 0.0` + nota de cabecera
   (igualado al canvas v13.6).
2. `src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v02.py`: `unicode()` y `ensure_ascii=False`
   (fix 2026-10-18 que solo estaba en el canvas).
3. `src/fase-1-contexto/F1_ETAPA2_LADOS_v06.py`: perfil normativo a z = 0.
4. Herramientas nuevas:
   - `scripts/utilities/diagnosticar-cotas-contexto.py`
   - `scripts/utilities/verificar-paridad-canvas-src.py`
5. Documentos:
   - `docs/planes/2026-10-25-diagnostico-alturas-contexto/D1-DIAGNOSTICO-COTAS-CONTEXTO.md`
   - `docs/planes/2026-10-25-diagnostico-alturas-contexto/D2-PLAN-CORRECCION-ALTURAS.md`
   - evidencia en `.../evidencia/cotas-AAA0030JKOE-2026-10-25.md`

## Decisiones

- El canvas es la fuente de verdad del código embebido.
- Puerto 19723: no se toca; work-around por orden de arranque (AutoClaw → ArchiCAD → Rhino, LC 19724).
- Secuencia de corrección de alturas: A (cableado `z_origen`) → B (muestreo MDT por huella) →
  C (drape o exclusión de vías/EP).

## Ejecución 2026-10-25 20:46 — criterio A (punto más bajo)

- `anclar_contexto50_zbase.py` modificado: muestreo **centroide + 4 extremos** por huella;
  `z_base_m` = mínimo; se guardan `z_base_centroide_m`, `z_base_min_m`, `z_base_max_m`,
  `z_base_n_puntos` y `z_base_metodo`.
- Corrida REST: **450 puntos, 90 OK, 0 fallidos, 219,8 s**.
- Bajada media **1,06 m**, máxima **4,65 m**; 89/90 registros cambiaron; 9 con >2 m.
- `z_base` nuevo −21,150…−0,060 m (canvas) → −6,662…14,428 m (local).
- Contraste con malla ETAPA1 en 9 huellas completas: promedio −0,18 m, máximo 1,35 m.
- Respaldo: `AAA0030JKOE-contexto50.json.bak-zbase-20261025-2046` (el JSON no está versionado).
- Sin re-embebido: el canvas lee `z_base_m` en la próxima corrida.
- Dato: 90 registros / 45 IDs únicos.

## Pendientes actualizados

1. Verificar en GH que `z_origin` de #201 ← `z_origen` (0,0).
2. Corrida limpia del canvas con la base nueva + censo 20/20.
3. `F3_StorySync_v02 --check` → 8/8.
4. Decidir drape vs exclusión de vías/EP (opción C).
5. Documentar las acciones de rendimiento.
