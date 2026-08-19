# Bitácora de versiones, decisiones y pruebas — DiseñoParametrico

Cierre **2026-08-18** · 85 commits (2026-07-31 → 2026-08-18) · suite **234 passed**.

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
