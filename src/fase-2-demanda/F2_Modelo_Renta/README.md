# F2 — Modelo Financiero Build-to-Rent (Fase 2)

Ampliación del [F2_Modelo_Financiero](../F2_Modelo_Financiero/README.md): cuando el
F2 concluye que **CL/IT > 30% hace inviable construir para vender**, este modelo
desarrolla la alternativa recomendada: **construir para arrendar (Build-to-Rent)**
— el edificio se construye y se conserva como activo generador de renta, con dos
estrategias de explotación:

| Estrategia | Descripción | Canon | Ocupación | Gastos | Inversión extra |
|---|---|---|---|---|---|
| **CP — Corto plazo** | Arriendo temporal **amoblado** (apartahotel/coliving), días/semanas/meses | LP × 1,7 | 75% (vacancia 25%) | Gestión intensiva: 25% EGI + capex 3% | Mobiliario $500.000/m² |
| **LP — Largo plazo** | Arriendo residencial **tradicional**, contratos 12+ meses | De mercado | 95% (vacancia 5%) | Estándar: 12% EGI + capex 1% | Ninguna |

## Archivos

| Archivo | Propósito |
|---|---|
| `F2_RENTA_MOTOR_v01.py` | Motor: flujo descontado 10 años, KPIs de renta (yield, cap rate, TIR, VPN, payback, múltiplo), suelo soportable, sensibilidad ±10%, salidas JSON/CSV/HTML |
| `parametros_entrada.json` | **Único archivo a editar** en el caso de referencia (GFA 1200, lote genérico) |
| `parametros_AAA0127AZPA_renta.json` | Lote real AAA0127AZPA (GFA 632,7 m²; CL $1.200 M; cánones de la zona; referencia de venta del F2 validado) |
| `parametros_AAA0127AZPA_renta_gfa1054.json` | Alternativa de curaduría (GFA 1054,49 m²) |
| `parametros_AAA0127AZPA_renta_cl_soportable.json` | Validación de la mecánica: CL al valor soportable ($817 M) → TIR 10,0% |
| `verificacion_independiente.py` | Recalcula todo con fórmulas manuales (TIR por Newton, el motor usa bisección) y contrasta: **PASS** |
| `resultados/` | Salidas del caso de referencia |
| `resultados_AAA0127AZPA_renta/`, `resultados_AAA0127AZPA_renta_gfa1054/`, `resultados_AAA0127AZPA_renta_cl_soportable/` | Salidas por caso (JSON, 2 CSV, flujo CSV, informe HTML) |

## Cómo ejecutar

Requisito: Python 3.8+ (sin dependencias externas).

```bash
cd src\fase-2-demanda\F2_Modelo_Renta
python F2_RENTA_MOTOR_v01.py                                                          # caso de referencia
python F2_RENTA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_renta.json           # lote real
python F2_RENTA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_renta_gfa1054.json   # curaduría
python F2_RENTA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_renta.json --estrategia LP
python F2_RENTA_MOTOR_v01.py --chip AAA0127AZPA --gfa 632.695061 --costo-lote 1200000000
python F2_RENTA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_renta.json --outdir resultados_prueba --sin-informe
```

Verificación independiente (PASS):

```bash
python verificacion_independiente.py --parametros parametros_AAA0127AZPA_renta.json --resultados resultados_AAA0127AZPA_renta/resultados_completos.json
```

Tests: `pytest tests\test_f2_renta.py -v` desde la raíz del proyecto (11 tests; suite total 73 PASS).

Salidas (por defecto en `resultados/`):

- `informe_F2_renta.html` — informe ejecutivo autocontenido (ábralo en cualquier navegador)
- `comparativo_renta.csv` — KPIs por estrategia × escenario (separador `;`)
- `sensibilidad.csv` — impacto ±10% por variable y combinación
- `flujo_caja_<ESTRATEGIA>_<ESCENARIO>.csv` — flujo anual del mejor caso
- `resultados_completos.json` — todos los cálculos y fuentes (auditoría)

## Cómo modificar el modelo (sin tocar código)

| Qué quiere cambiar | Campo |
|---|---|
| Envolvente normativa (Fase 1) | `gfa_max_m2` |
| Tamaño y precio del lote | `lote.area_m2`, `lote.precio_suelo_m2`, `lote.impuestos_escritura_pct` o `lote.costo_lote_total_cop` (CL directo, compatible con el pipeline) |
| Costos blandos / leasing | `financiero.costos_blandos_pct`, `financiero.marketing_leasing_pct` |
| Horizonte, IPC, cap rate de salida | `renta.horizonte_anios`, `renta.incremento_canon_pct`, `renta.incremento_gastos_pct`, `renta.cap_rate_salida_pct` |
| Reglas de decisión | `reglas_renta.tasa_descuento_pct / tir_minima_pct / cap_rate_entrada_min_pct / payback_max_anios / cl_inversion_*` |
| Por escenario: unidades, eficiencia, costo, cánones | `escenarios.<ID>.unidad_m2 / eficiencia_nga / costo_construccion_m2 / canon_m2_mes.{CP,LP}` |
| Por estrategia: ocupación, administración, gastos, mobiliario | `estrategias.<CP|LP>.*` |
| Amplitud de la sensibilidad | `sensibilidad.variacion_pct` |
| Comparación contra venta (F2) | `referencia_venta.escenarios.<ID>.*` |
| Fuentes y notas (trazabilidad) | `escenarios.<ID>.fuente_canon / fuente_costo / nota` |

## Metodología (flujo descontado, 10 años)

```
NGA = GFA × eficiencia_NTG      → unidades enteras → área arrendable = unidades × m²
Inversión₀ = CL + CD + CB + MKT + Mobiliario(CP)
  CD = GFA × costo_construccion_m2 ; CB = 15% CD ; MKT = 2% GPI₁
Año t:  GPI = área × canon_m2_mes × 12 × (1+IPC)^(t−1)
        EGI = GPI × ocupación
        NOI = EGI − administración − (gastos + capex)%·EGI
Salida(H) = NOI_H × (1+IPC) / cap_rate_salida
KPIs: yield bruto = GPI₁/Inv ; cap rate entrada = NOI₁/Inv ; TIR ; VPN @ tasa ;
      payback simple/descontado ; múltiplo ; CL/Inv ; suelo soportable ; ocup. de equilibrio
```

**Suelo soportable**: máximo CL que deja VPN ≥ 0 a la tasa exigida — la vara de
negociación con el dueño del lote (análogo al CL soportable del F2).

## Resultados lote real AAA0127AZPA (GFA 632,7 m²; CL $1.200 M; cánones de zona 2026)

| Estrategia × Producto | Cap rate entrada | TIR | VPN (M$) | Suelo soportable |
|---|---|---|---|---|
| LP × A VIS | 4,2% | 6,2% | −710 | **$490 M** |
| CP × A VIS | 4,1% | 5,7% | −875 | $325 M |
| LP × B Estándar | 3,8% | 5,0% | −1.065 | $135 M |
| CP × B Estándar | 3,8% | 4,9% | −1.156 | $44 M |
| C Lujo (CP/LP) | 2,6–2,7% | 0,4–0,7% | −2.3 mil M | $0 (inviable ni con suelo gratis) |

**Conclusión**: con el CL de $1.200 M, construir para arrendar **tampoco es viable**
(TIR máx. 6,2% vs 10% exigido) — consistente con el F2, que ya lo era para venta.
El suelo soportable máximo es **$490 M** (LP × A VIS), ~59% por debajo del precio
pedido: la negociación del lote (o el arriendo del mismo) sigue siendo la palanca #1.

## Resultados alternativa de curaduría (GFA 1054,49 m²; CL $1.200 M)

| Estrategia × Producto | Cap rate entrada | TIR | VPN (M$) | Suelo soportable |
|---|---|---|---|---|
| **LP × A VIS** | **5,1%** | **8,6%** | −383 | **$817 M** |
| CP × A VIS | 4,8% | 7,8% | −658 | $542 M |
| LP × B Estándar | 4,8% | 8,0% | −667 | $533 M |
| CP × B Estándar | 4,7% | 7,7% | −830 | $370 M |
| C Lujo (CP/LP) | 3,5–3,6% | 4,0–4,1% | −2,4 mil M | $0 |

**Conclusión**: con la mayor edificabilidad el proyecto de renta mejora (cap rate de
entrada de A supera el 5% exigido) pero la TIR se queda en 8,6%: el CL de $1.200 M
sigue ~47% por encima de lo soportable. Si la curaduría prospera **y** el suelo se
negocia a ~$817 M, LP × A VIS alcanza exactamente TIR 10,0% (caso
`parametros_AAA0127AZPA_renta_cl_soportable.json`).

## Sensibilidad ±10% (prioridad de fetch)

1. **Ocupación** (impacto promedio VPN 289–610 M$) — crítica: gestión comercial (CP) / mercado (LP)
2. **Canon m²** (289–609 M$) — crítica: dato de mercado por zona y tipología
3. **Costo duro** (233–442 M$) — crítica: define la inversión; CAMACOL proyecta +15% en 2026
4. **Cap rate de salida** — alta: define el valor residual
5. **Incremento del canon (IPC)** — media: protección contra inflación, palanca estructural
6. **Tasa de descuento** — media: política del inversionista
7. **Gastos operativos** — media: controlable por gestión

## Fuentes de mercado (consultadas 2026-08-13)

| Dato | Valor | Fuente |
|---|---|---|
| Canon promedio Bogotá (apartamentos) | $3.761.958/mes en 79 m² = **$47.821/m²/mes** | Ciencuadras Q1-2026 |
| Canon promedio Prado Veraniego-Canódromo | **$1.841.565/mes** | FincaRaíz (zona del lote) |
| Comparables zona (usados en el modelo) | 80 m² @ $3,0 M ($37.500/m²/mes); 47 m² @ $2,7 M; 2 hab @ $2,3 M | Properati; MercadoLibre; Mitula |
| Vacancia Bogotá | **1,9%** (el modelo usa 5% LP conservador) | Inversionistas 2026 |
| Cap rates vivienda Colombia | **5,4–6,0%** (salida del modelo 6,2% conservador) | Tinsa; inversionistas 2026 |
| IPC 2026 | **5,56%** | DANE (IPVN Q1-2026) |
| Regla de mercado | Canon mensual ≈ 1% del valor del inmueble | PADS 2025 |
| Costo construcción | $2,3–4,3 M/m² según acabados | Konstruing (07-ago-2026); Aliados de Obras 2026 |

Cada parámetro del JSON lleva su fuente y URL para auditoría.

## Alcance / fuera de alcance

- ✔ Flujo descontado anual a 10 años con valor de salida (cap rate)
- ✔ KPIs de inversión en renta (yield, cap rate, TIR, VPN, payback, múltiplo)
- ✔ Suelo soportable (vara de negociación) y punto de equilibrio de ocupación
- ✔ Sensibilidad ±10% y comparación con la alternativa de venta (F2)
- ✘ No incluye deuda/apalancamiento (el ROE con financiación se reserva para Fase 3)
- ✘ No modela rampa de leasing del año 1 (ocupación promedio constante; conservador)
- ✘ No redefine el GFA de Fase 1 (es restricción de entrada)
- ✘ No emite concepto legal, urbanístico, tributario ni de uso de suelo
- ✘ Los cánones del modelo son de mercado abierto 2026; **valídelos con comparables de radio 5 km** antes de decisiones de inversión
