# data/fase-2-demanda — Entrada del pipeline de demanda

JSON de entrada de la Fase 2 (formato del pipeline, consumido por `F2_DEMANDA_MOTOR_v01.py` y
por el motor financiero mejorado en `src\fase-2-demanda\F2_Modelo_Financiero\`).

| Archivo | GFA | Rol |
|---|---|---|
| `AAA0127AZPA-prefactibilidad.json` | 632,695 m² | **Caso actual** (Fase 1 verificada). Canónico para reproducir los KPIs del pipeline |
| `AAA0127AZPA-prefactibilidad-gfa1054.json` | 1054,49 m² | **Alternativa de curaduría**: edificabilidad ampliada que la zona está autorizando. Evaluada con `parametros_AAA0127AZPA_gfa1054_mercado2026.json` |

Historial: ambos archivos fueron duplicados entre `src\fase-2-demanda\data\` y `data\fase-2-demanda\`
hasta el 2026-08-13; se consolidaron aquí como única raíz de datos.
