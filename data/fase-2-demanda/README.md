# data/fase-2-demanda — Entrada del pipeline de demanda

JSON de entrada de la Fase 2 (formato del pipeline, consumido por `F2_DEMANDA_MOTOR_v01.py` y
por los motores financieros en `src\fase-2-demanda\F2_Modelo_Financiero\` y
`src\fase-2-demanda\F2_Modelo_Renta\`).

## Casos históricos

| Archivo | GFA | Rol |
|---|---|---|
| `AAA0127AZPA-prefactibilidad.json` | 632,695 m² | **Caso actual** (Fase 1 verificada). Canónico para reproducir los KPIs del pipeline |
| `AAA0127AZPA-prefactibilidad-gfa1054.json` | 1054,49 m² | **Alternativa de curaduría**: edificabilidad ampliada que la zona está autorizando |

## Casos de estudio del ejercicio (2026-08-14)

Generados con `scripts\utilities\generar_casos_pipeline.py` (mismas fórmulas del pipeline).

| Archivo | Lote | GFA | CL | Situación de prueba |
|---|---|---|---|---|
| `AAA0127AZPA-prefactibilidad-gfa1053-cl550.json` | AAA0127AZPA (El Prado, Suba) | 1.053 m² | $550 M | Norte medio: suelo renegociado para resolver el caso |
| `AAA0030JKOE-prefactibilidad.json` | AAA0030JKOE (La Candelaria, UPZ 94) | 3.312,6 m² | $1.420 M | Centro histórico: escala grande, turismo, restauración |
| `002407033006-prefactibilidad.json` | 002407033006 (Venecia, Tunjuelito) | 650 m² | $192 M | Sur: lote pequeño, valores bajos (caso de estrés) |

Nota: en los tres casos los precios/costos/cánones de los escenarios están documentados como
"supuestos de ejercicio" en los JSON de parámetros de cada motor (fuente `nota`), salvo los del
caso A que usan los precios validados con comparables 2026-08-13.

Historial: los dos primeros archivos fueron duplicados entre `src\fase-2-demanda\data\` y
`data\fase-2-demanda\` hasta el 2026-08-13; se consolidaron aquí como única raíz de datos.
