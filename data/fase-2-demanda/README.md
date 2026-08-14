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
El lote 002407033006 (Venecia, Tunjuelito) fue **EXCLUIDO** del ejercicio el 2026-08-14 por
decisión del usuario; su lugar lo ocupa AAA0039KRMR (Muzu, Puente Aranda).

| Archivo | Lote | GFA | CL | Situación de prueba |
|---|---|---|---|---|
| `AAA0127AZPA-prefactibilidad-gfa1053-cl550.json` | AAA0127AZPA (El Prado, Suba) | 1.053 m² | $550 M | Norte medio: suelo renegociado para resolver el caso |
| `AAA0030JKOE-prefactibilidad.json` | AAA0030JKOE (La Candelaria, UPZ 94) | 3.312,6 m² | $1.420 M | Centro histórico: escala grande, turismo, restauración |
| `AAA0039KRMR-prefactibilidad.json` | AAA0039KRMR (Muzu, Puente Aranda) | 1.100 m² | $700 M | Occidente: lote pequeño (357 m²), suelo caro (caso de estrés) |

Nota: en los tres casos los precios/costos/cánones de los escenarios están documentados como
"supuestos de ejercicio" en los JSON de parámetros de cada motor (fuente `nota`), salvo los del
caso A que usan los precios validados con comparables 2026-08-13. Todos los casos incluyen el
escenario `D_MIXTO` (USO-MULTIPLE, override de usuario fuera de reglamentación) para la
validación de hipótesis de construcción y prefactibilidad.

## Áreas de influencia de la investigación (multi-nivel)

`alcance-investigacion.json` define los tres niveles del estudio de demanda:

| Nivel | Alcance | Enfoque |
|---|---|---|
| `N1-CERCANO` | Radio 2.000 m desde el lote | Vecindario directo: precios/cánones/competencia local |
| `N2-INTERMEDIO` | Radio 5.000 m desde el lote | Área de mercado actual: comparables UPZ, oferta nueva |
| `N3-LEJANO-ACCESIBILIDAD` | Sin radio fijo: estaciones TransMilenio/paraderos SITP < 500 m; isocrona 20 min en transporte público; malla vial arterial (privado) | Preferencias de localización por acceso a la red principal de transporte |

Anillos por lote (círculos SIRGAS): `exports/alcance/<CHIP>-alcance.json`, generados con
`scripts\utilities\alcance_investigacion.py`. El nivel N3 reporta estado de datos: la malla vial
del POT ya viene en el contexto F1; las capas de estaciones/paraderos/GTFS se incorporan desde
datos abiertos de Bogotá (IDECA/TransMilenio) como paso siguiente.

Historial: los dos primeros archivos fueron duplicados entre `src\fase-2-demanda\data\` y
`data\fase-2-demanda\` hasta el 2026-08-13; se consolidaron aquí como única raíz de datos.
