# Bitácora de versiones, decisiones y pruebas — DiseñoParametrico

Cierre de fase **F1–F3** · **2026-08-18** · 85 commits · suite **234 passed**.

## 1. Versiones vigentes por fase

| Fase | Script vigente | Versión | Estado |
|---|---|---|---|
| F0 | `F0_LOAD_PROYECTO_v01.py` | v01.3 | Estable (IronPython 2.7) |
| F1 contexto | `F1_ETAPA1_CONTEXTO_v02.py` | v02 | Estable |
| F1 lados | `F1_ETAPA2_LADOS_v06.py` | v06 | Estable |
| F1 patio | `F1_ETAPA2_PATIO_v02.py` | v02 | Estable |
| F1 normativa | `F1_ETAPA2_NORMATIVA_v08.py` | v08 | Estable |
| F1 GFA | `F1_EXPORTAR_GFA_v02.py` | v02 | Estable |
| F2 venta | `F2_DEMANDA_MOTOR_v03.py` | v03 | Estable |
| F2 renta | `F2_RENTA_MOTOR_v03.py` | v03 | Estable |
| F3 distribución | `F3_DISTRIBUCION_v01.py` | v01 | Estable |
| F3 volumen | `F3_VOLUM_GENERADOR_v07.py` | v07 | Estable (Rhino 8) |
| F3 accesos | `F3_ACCESOS_INTEGRADOR_v02.py` | v02 | Estable |
| F4 ambiental | `F4_LADYBUG_ANALISIS_v02.py` | v02 | No validado en Rhino |
| F5 BIM | — | — | Documentación |

## 2. Decisiones (ADR)

| ADR | Decisión |
|---|---|
| ADR-002 | Catastro vs POT: POT como fuente normativa primaria |
| ADR-004 | Postergar MCPs; solo componentes nativos GH/ArchiCAD |
| ADR-005 | Corrección de interpretación de altura POT |
| ADR-006 | Integración climática transversal (EPW + Ladybug) |
| ADR-007 | Sistema de adquisición de contexto urbano |
| ADR-008 | Clasificación espacial híbrida (oficial + manual) |
| ADR-010 | Optimización topográfica + plantilla BIM |

## 3. Pruebas

- **Suite pytest: 234 passed**, última ejecución 2026-08-18.
- Archivos de test (22): F0 load, F1 (fetch, lados v04/v05/v06, normativa v06/v07/v08, patio), F2 (venta, renta), F3 (distribución/núcleo, volumen v07, accesos v02), orquestador, servidor, vecinos por lado.
- **Casos límite cubiertos**: vecino `via` vs `predio` (Muzú occidente), empate posterior independiente, aporte parcial (`pago_parcial_pct`), usos base vs sector, alineación de núcleo.

## 4. Hitos por fecha

- **2026-07-31** — init + Decreto 555/670 + NSR-10.
- **2026-08-01/09** — Fase 1: contexto, lados, normativa, patios.
- **2026-08-12/14** — Fase 2: financiero, Build-to-Rent, sensibilidad, 3 casos.
- **2026-08-14/17** — Fase 3: distribución, volumen, accesos, prueba real de masa en Rhino 8.
- **2026-08-17/18** — Orquestador: formulario, servidor, F0 load, vecinos por lado.
- **2026-08-18** — Área de actividad (geobase) + cableado del canvas commiteado.
- **2026-08-18 (tarde)** — Sector de uso por UPL (geobase) extraído e integrado + validación `pago_parcial_pct` 70/30 con AAA0127AZPA.


## Sesión 2026-08-18 (tarde) — Interfaz + F2/F3 ejecutables desde el formulario

### Cambios
- **Interfaz**: `caso` → "Escenario de modelado" atado al CHIP (sección 4 ya no cambia de lote).
- **Aporte del lote (venta)**: variables `aporte_lote` + `pago_parcial_pct`; helper `_aporte_a_pago_parcial()`.
- **F2 desde el form**: `POST /api/calcular-f2` (corre F2 con `--pago-parcial`) + botón.
- **F3 para cualquier CHIP**: `F3_DISTRIBUCION_v01.py` acepta `--chip`/`--escenario` (`buscar_resultados`, `leer_programa_chip`, fallback `mix_usos`); `POST /api/generar-f3` + botón.
- **Pipeline**: `POST /api/pipeline` (F1→F2→F3) + botón "Ejecutar pipeline"; `_calcular_f2` escribe `resultados_<CHIP>.json` canónico.
- **Suite**: 234 → 239 passed.

### Decisiones
- `aporte_lote` → `pago_parcial_pct`: venta_completa=100, participacion=% (default 30), aporte_completo=0 (inverso de `fraccion_aporte_pct`).
- El selector de escenario no re-selecciona el CHIP: `syncCasoConChip()` filtra por `CASO_CHIP`.
- F3 con error claro + fallback a escenario `mix_usos` cuando falta D_MIXTO.

### Pendientes
- F1 GFA manual en Rhino (verificar GFA 826.58 vs 1186.87 tras regeneración del operador).
- Listas definitivas de usos por sector (Sinupot / CU-5.4.x).
- F3 masa Rhino → Morphs ArchiCAD (manual). F4/F5 pendientes.
