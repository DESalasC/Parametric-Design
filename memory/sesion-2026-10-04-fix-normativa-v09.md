# Sesión 2026-10-04 — Fix error NORMATIVA v09 `float * NoneType`

## Resumen
Error reportado en componente Canvas v13 `#116-F1_ETAPA2_NORMATIVA_v09.py`: `Solution exception: unsupported operand type(s) for *: 'float' and 'NoneType'`.

## Causa raíz
En Grasshopper (IronPython), los inputs numéricos pueden llegar como:
- `None` directamente
- Listas vacías `[]`
- Listas con `None` dentro `[None]`
- Strings vacíos `""` o `"None"`

El parsing original no cubría todos estos casos para variables usadas en multiplicaciones (`area_lote * io_maximo`, `pisos_finales * floor_h`, `LATERAL_FRACCION_ALTURA * altura_total`, etc.).

## Correcciones aplicadas a `F1_ETAPA2_NORMATIVA_v09.py`

1. **Inicialización temprana de `io_maximo`** (antes del cálculo `presupuesto_ocupacion_m2`)
2. **Guarda defensiva para `floor_h`** (`if floor_h <= 0: floor_h = 3.0`)
3. **Simplificación del cálculo de `presupuesto_ocupacion_m2`** usando `io_maximo` ya inicializado

## Archivos modificados
- `D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA2_NORMATIVA_v09.py` (fix aplicado)

## Verificación
- Script compila y ejecuta offline sin error `float * NoneType`
- Tests existentes: 3/5 pasan (2 fallan por limitaciones del stub Rhino, no por el fix)
- Variables numéricas críticas ahora siempre tienen valores válidos antes de multiplicaciones

## Pendientes
1. **Patch manual canvas v13.1** en Rhino/GH (operador) — reemplazar script NORMATIVA por v09 fix
2. **Validación offline completa**: `pytest tests/ -x -q` + `run_pipeline_v01.py --run --yes`
3. **Validación viva** (bloqueada por puerto 19723)

## Bloqueador crítico
**Puerto 19723** (AutoClaw ↔ Live Connection) — sin resolver no hay validación viva posible.

## Registro en vault
- Diario: `60-diario/2026-10-04.md`
- Memoria proyecto: `memory/sesion-2026-10-04-fix-normativa-v09.md` (este archivo)