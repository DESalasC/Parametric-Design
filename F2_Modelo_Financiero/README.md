# F2 — Modelo Financiero Inmobiliario de Prefactibilidad (Fase 2)

Modelo que determina el **producto inmobiliario óptimo** (tipología, nivel de acabados,
número de unidades) para un lote, respetando la envolvente normativa (GFA máximo de
Fase 1), evaluando 3 escenarios para el mismo GFA: **A (VIS/VIP)**, **B (Estándar)** y
**C (Lujo)**.

## Archivos

| Archivo | Propósito |
|---|---|
| `F2_DEMANDA_MOTOR_v01.py` | Motor del modelo: KPIs, alertas de viabilidad, sensibilidad ±10%, recomendación, salidas JSON/CSV/HTML |
| `parametros_entrada.json` | **Único archivo a editar**: GFA, lote, costos, precios, eficiencias, absorción, reglas y fuentes |
| `parametros_AAA0127AZPA.json` | Lote real AAA0127AZPA con datos del pipeline (reproduce sus KPIs exactamente) |
| `parametros_AAA0127AZPA_mercado2026.json` | Mismo lote con precios/costos de mercado 2026 (últimos datos) |
| `verificacion_independiente.py` | Recalcula todo con fórmulas escritas a mano y contrasta contra la salida del motor (equivalente a la hoja de cálculo independiente) |
| `MANUAL_DE_USO.md` | Manual detallado para persona no técnica: requisitos, ejecución, edición, glosario, lectura de resultados |
| `parametros_provocacion.json` | Caso de prueba: precios −10% y lote ×1,7 → dispara todas las alertas de inviabilidad |
| `parametros_zona_alta.json` | Caso alternativo: precio estándar $8,0 M/m² → cambia la recomendación (reproducibilidad) |
| `resultados/` | Salidas del caso base (JSON, 2 CSV, informe HTML) |
| `resultados_provocacion/`, `resultados_zona_alta/` | Salidas de los casos de validación |

## Cómo ejecutar

Requisito: Python 3.8+ (sin dependencias externas).

```bash
cd F2_Modelo_Financiero
python F2_DEMANDA_MOTOR_v01.py                              # caso base (GFA 1200 m2)
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_zona_alta.json --outdir resultados_zona_alta
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_provocacion.json --outdir resultados_provocacion
python F2_DEMANDA_MOTOR_v01.py --chip AAA0127AZPA --sin-informe
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_mercado2026.json --outdir resultados_AAA0127AZPA_aporte
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_mercado2026.json --pct-socio 30
```

Salidas (por defecto en `resultados/`):

- `informe_F2_prefactibilidad.html` — informe ejecutivo autocontenido (ábralo en cualquier navegador)
- `comparativo_escenarios.csv` — KPIs de los 3 escenarios (compatible con Excel, separador `;`)
- `sensibilidad.csv` — impacto ±10% por variable y escenario
- `flujo_caja_<escenario>_compra.csv` / `_aporte.csv` — flujo de caja trimestral (24 meses) de la mejor alternativa
- `resultados_completos.json` — todos los cálculos y fuentes (auditoría)

## Cómo modificar el modelo (sin tocar código)

Todo se edita en **`parametros_entrada.json`**:

| Qué quiere cambiar | Campo |
|---|---|
| Envolvente normativa (Fase 1) | `gfa_max_m2` |
| Tamaño y precio del lote | `lote.area_m2`, `lote.precio_suelo_m2`, `lote.impuestos_escritura_pct` |
| Costos blandos / marketing | `financiero.costos_blandos_pct`, `financiero.marketing_ventas_pct` |
| Por escenario: unidades, eficiencia, precio, costo, absorción | `escenarios.<ID>.unidad_m2 / eficiencia_nga / precio_venta_m2 / costo_construccion_m2 / absorcion_unid_mes` |
| Umbrales de decisión | `reglas_decision.*` |
| Amplitud de la sensibilidad | `sensibilidad.variacion_pct` |
| Participación del dueño del lote | `aporte_suelo.pct_socio` (`null` = el modelo propone el punto medio de la ventana) |
| Arriendo del lote | `arriendo_lote.mensual_pct_cl`, `arriendo_lote.meses` |
| Programa del flujo de caja | `flujo_caja.*` (listas de % por trimestre) |
| Fuentes y notas (trazabilidad) | `escenarios.<ID>.fuente_precio / fuente_costo / nota` |

Después de editar, vuelva a ejecutar el script: recalcula escenarios, alertas,
sensibilidad, recomendación e informe sin cambiar el código.

## Reglas de decisión (Bogotá, configuradas en `reglas_decision`)

- **MUB** < 18% → alto riesgo; > 25% → atractivo
- **ROI** mínimo deseable → 22%
- **CL/IT** > 25% → precaución; > 30% → inviable para desarrollo y venta (evaluar arriendo)

## Metodología (prefactibilidad estática)

```
NGA = GFA × eficiencia_NTG        (por escenario)
Unidades = floor(NGA / m² por unidad)   → área vendible real = unidades × m²
Ingresos = área vendible × precio_venta_m2
Costo duro = GFA × costo_construccion_m2
Costos blandos = 13% del costo duro      (rango 12–15%)
Marketing = 3,5% de los ingresos         (rango 3–4%)
Costo lote = área × precio_suelo × (1 + 4% impuestos)
CTD = lote + duro + blandos + marketing
UB = Ingresos − CTD ;  MUB = UB/IT ;  ROI = UB/CTD ;  CL/IT = lote/IT
```

Sensibilidad ±10% sobre: precio de venta, costo duro, eficiencia NGA, costo del lote y
absorción (unidades continuas, efecto marginal). La absorción no altera la UB estática
(afecta TIR y costos financieros, reservados para Fase 3).

## Escenario D — Participación del dueño del lote en utilidades

Cuando el lote es caro (CL/IT > 30%), el modelo explora la alternativa de que el **dueño
aporte el lote** y reciba un porcentaje de las utilidades finales en lugar del precio de
venta. Calcula la ventana de negociación por escenario:

- `pct min (dueño)`: lo necesario para recibir al menos el valor del suelo soportable por
  el mercado (CL que daría ROI mínimo comprando).
- `pct max (desarrollador)`: lo que deja al desarrollador su ROI mínimo.
- Recomendado: punto medio de la ventana (o el valor de `--pct-socio` / `aporte_suelo.pct_socio`).

Resultado lote AAA0127AZPA (mercado 2026): **B Estándar con ~30% de utilidades** → ROI
desarrollador 23,0% (antes −12,7% comprando el lote) y el dueño recibe $225,3 M. C Lujo
no tiene acuerdo posible (ROI máx. 10% < 22% ni con suelo gratis).

## Escenario E — Arriendo del lote

Alternativa recomendada por el modelo cuando CL/IT > 30%: el lote se **arrienda** durante el
ciclo (24 meses) con un canon mensual configurable (`arriendo_lote.mensual_pct_cl`, default
0,75% del valor) y vuelve al dueño al final. El análisis calcula el canon sobre el precio pedido
y sobre el valor soportable por el mercado:

| Escenario | Canon s/ pedido → ROI | Canon s/ soportable → ROI |
|---|---|---|
| A — VIS | $216 M → 18,0% | $27,2 M → 30,4% (VIABLE) |
| B — Estándar | $216 M → 21,4% | $36,5 M → 30,7% (VIABLE) |
| C — Lujo | $216 M → 3,2% | $0 M → 10,0% (no viable) |

Con canon sobre el precio pedido ningún escenario alcanza el ROI mínimo; con canon negociado
sobre el valor soportable, A y B son viables. La palanca es la base de negociación del canon.

## Flujo de caja estimado (24 meses)

El informe y los CSV incluyen el flujo de caja trimestral de la mejor alternativa en tres
modalidades: **compra** (lote al inicio), **aporte** (reparto al dueño en el trimestre 7) y
**arriendo** (canon por trimestre).
Programa por defecto: ingresos 20% preventa / 40% obra / 40% entrega; costo duro 30-40-30;
blandos 25% por trimestre el primer año; marketing sigue a los ingresos. El saldo final se
contrasta contra la UB estática (chequeo de consistencia `OK`/`INCONSISTENTE`).

## Fuentes de mercado (consultadas 2026-08-12)

| Dato | Valor | Fuente |
|---|---|---|
| SMMLV 2026 | $1.750.905 | Decreto 1469/2025 (ratificado Decreto 0159/2026) |
| Tope VIS 2026 | 135 SMMLV = $236,37 M | Ley 1537/2012 mod. Ley 2294/2023; Argos 2026 |
| Precio venta Bogotá | $6,0 M/m² promedio (50% mercado $4,5–7,9 M/m²); $7,42 M/m² apartamentos Q1-2026; premium >$11 M/m² | Terraes 2026; Ciencuadras Q1-2026; Metrocuadrado |
| Costo construcción Bogotá | Obra gris desde ~$1,3 M/m²; terminada acabados medios $2,2–3,5 M/m²; rango general $2,2–3,8 M/m² | Konstruing (07-ago-2026); Aliados de Obras 2026 |
| Suelo | Rango medio urbano (supuesto de referencia) | Catastro Bogotá (Visor Inmobiliario); IDECA |

Cada parámetro del JSON lleva su fuente y URL para auditoría.

## Alcance / fuera de alcance

- ✔ Prefactibilidad estática de 1 ciclo (~2 años), 3 escenarios, KPIs, alertas, sensibilidad, recomendación
- ✔ Escenario D (aporte del suelo con participación en utilidades) y flujo de caja trimestral estimado
- ✘ No redefine el GFA de Fase 1 (es restricción de entrada)
- ✘ No incluye financiación, TIR, VPN ni flujo de caja mensual (Fase 3); el flujo trimestral es un estimado de liquidez, no un modelo financiero completo
- ✘ No emite concepto legal, urbanístico ni de uso de suelo
- ✘ El precio de suelo del caso base es un supuesto de referencia: **reemplácelo por el dato real del lote** antes de decisiones de inversión
