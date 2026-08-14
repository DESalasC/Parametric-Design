# Manual de uso — Modelo Build-to-Rent (F2 Renta)

Guía para persona no técnica. Si ya usó el manual del modelo de venta
(`F2_Modelo_Financiero\MANUAL_DE_USO.md`), este es su equivalente para la
estrategia de **construir para arrendar**.

---

## 1. ¿Qué hace este modelo?

El modelo de venta (F2) calculaba cuánto ganaría construyendo y **vendiendo**
apartamentos. Cuando el lote es caro (CL/IT > 30%), el F2 recomendaba "evaluar
arriendo". Este modelo desarrolla esa idea:

> **Construir el edificio y NO venderlo: arrendarlo.**

Compara dos formas de arrendar, para 3 productos (VIS, Estándar, Lujo):

- **Corto plazo (CP)**: apartamentos **amoblados** arrendados por días/semanas/meses
  (estilo apartahotel). Se cobra más por m², pero hay más desocupación y gastos de
  gestión y limpieza. Requiere invertir en muebles.
- **Largo plazo (LP)**: arriendo tradicional de 12 meses o más. Se cobra el canon de
  mercado, la ocupación es alta y los gastos son los normales.

El modelo proyecta **10 años** de ingresos y gastos, calcula el **valor de reventa**
del edificio al final (por el método de capitalización) y responde:

- ¿Cuánto rinde mi inversión? → **TIR** (retorno anual compuesto) y **VPN** (valor
  creado, en pesos de hoy).
- ¿Qué % del año está ocupado? ¿Cuánto debo cobrar? → supuestos editables.
- ¿Cuánto puedo pagar por el lote? → **suelo soportable** (clave de negociación).

---

## 2. Requisitos

- Python 3.8 o superior (cualquier sistema). No instala nada extra.
- Una carpeta con el modelo: `D:\Work\PROJECTS\DiseñoParametrico\src\fase-2-demanda\F2_Modelo_Renta\`

---

## 3. Cómo ejecutarlo (paso a paso)

**Paso 1.** Abra una terminal (PowerShell) en la carpeta del modelo:

```powershell
cd D:\Work\PROJECTS\DiseñoParametrico\src\fase-2-demanda\F2_Modelo_Renta
```

**Paso 2.** Ejecute con el lote real (el caso que ya viene configurado):

```powershell
python F2_RENTA_MOTOR_v02.py --parametros parametros_AAA0127AZPA_renta.json
```

**Paso 3.** Abra el informe:

```
resultados_AAA0127AZPA_renta\informe_F2_renta.html
```

(doble clic; se abre en el navegador).

Otras ejecuciones útiles:

```powershell
# Alternativa de curaduría (GFA 1054)
python F2_RENTA_MOTOR_v02.py --parametros parametros_AAA0127AZPA_renta_gfa1054.json

# Solo largo plazo
python F2_RENTA_MOTOR_v02.py --parametros parametros_AAA0127AZPA_renta.json --estrategia LP

# Caso de referencia (GFA 1200, lote genérico)
python F2_RENTA_MOTOR_v02.py
```

---

## 4. Cómo cambiar los datos (sin tocar código)

Todo se edita en el archivo **`parametros_AAA0127AZPA_renta.json`**
(para el caso de referencia, `parametros_entrada.json`). Ábralo con el Bloc de
notas o VS Code. Los campos principales:

| Quiero cambiar... | Busco el campo... | Ejemplo |
|---|---|---|
| El GFA (m² construibles de Fase 1) | `"gfa_max_m2"` | `"gfa_max_m2": 632.695061` |
| El precio del lote | `"lote"` → `"costo_lote_total_cop"` | `"costo_lote_total_cop": 1200000000` |
| El canon de arriendo | `"escenarios"` → `"B_ESTANDAR"` → `"canon_m2_mes"` | `"LP": 38000` = $38.000/m²/mes |
| La ocupación promedio | `"estrategias"` → `"LP"` → `"ocupacion_pct"` | `"ocupacion_pct": 95.0` |
| Los gastos de operación | `"estrategias"` → `"LP"` → `"gastos_operativos_pct_egi"` | `"gastos_operativos_pct_egi": 12.0` |
| El número de años | `"renta"` → `"horizonte_anios"` | `"horizonte_anios": 10` |
| La tasa exigida (qué quiero ganar) | `"reglas_renta"` → `"tasa_descuento_pct"` y `"tir_minima_pct"` | `"tasa_descuento_pct": 10.0` |

Después de guardar, vuelva a ejecutar el paso 2: todo se recalcula.

> ⚠️ Respete las comas y comillas (formato JSON). Si algo se rompe, el modelo le
> dirá qué línea tiene el error.

---

## 5. Glosario de las cifras del informe

| Sigla | Qué significa | Cómo se lee |
|---|---|---|
| **GFA** | Área total construible (Fase 1) | Restricción normativa |
| **NGA** | Área neta útil después de circulaciones | Parte del GFA que se puede arrendar |
| **GPI** | Ingreso bruto potencial (todo ocupado, todo el año) | El techo de ingresos |
| **EGI** | Ingreso efectivo (GPI × ocupación) | Lo que realmente entra |
| **NOI** | Ingreso neto operativo (EGI − administración − gastos) | El "sueldo" anual del edificio |
| **Cap rate entrada** | NOI del año 1 ÷ inversión total | Rentabilidad anual del primer año (%). Si es < 5%, no cubre el costo del dinero |
| **TIR** | Retorno anual compuesto de todo el proyecto (10 años + reventa) | El KPI principal: ¿cuánto rindo al año? |
| **VPN** | Valor presente neto (todo descontado a hoy, menos la inversión) | ¿Cuántos pesos crea el proyecto? Positivo = crea valor |
| **Payback** | Años que tarda en recuperarse la inversión | Liquidez |
| **Suelo soportable** | Máximo que el proyecto puede pagar por el lote (VPN = 0) | Su vara de negociación con el dueño |
| **Ocupación de equilibrio** | Ocupación mínima para no perder dinero en operación | Si la ocupación real cae por debajo, el edificio pierde |

---

## 6. Cómo leer la recomendación

El informe empieza con un veredicto:

- **VIABLE** (verde): la combinación cumple TIR ≥ 10%, cap rate ≥ 5% y VPN > 0.
- **NO VIABLE** (rojo): ninguna combinación cumple las reglas. El informe muestra la
  mejor alternativa y las palancas. En los resultados actuales del lote
  AAA0127AZPA, la conclusión es **NO VIABLE con el lote a $1.200 M** (igual que en
  venta) y la palanca principal es el precio del suelo: el modelo reporta cuánto
  sería soportable (hasta $817 M con la curaduría GFA 1054 y arriendo largo plazo
  en producto VIS).

Lea siempre la tabla **"Suelo soportable por combinación"**: es la respuesta a
"¿cuánto puedo ofrecer por el lote?".

---

## 7. Preguntas frecuentes

**¿Por qué sale NO VIABLE si los arriendos en Bogotá están caros?**
Porque el modelo compara contra el **costo de construir nuevo + el lote**. Con el
lote a $1.200 M y la construcción a ~$3 M/m², el cap rate del primer año queda en
~4-5%, por debajo del 5% mínimo y de lo que paga un CDT/leasing. El problema no es
el canon: es el costo total del activo.

**¿El corto plazo (amoblado) es mejor?**
Cobra más por m², pero tiene más vacancia (25%), más gastos (gestión, limpieza,
mobiliario) y más capex. En los resultados actuales, **el largo plazo gana** en
TIR y suelo soportable. El CP solo conviene con operadores especializados que
garanticen ocupación alta.

**¿Y si pido un crédito para construir?**
La deuda (apalancamiento) mejora el retorno sobre el patrimonio (ROE) pero añade
riesgo de tasa y exige que el NOI cubra el servicio de la deuda. Está fuera del
alcance de esta versión; se modelará en Fase 3. Con las tasas de 2026, no cambia
la conclusión de fondo: el suelo debe bajar de $1.200 M.

**¿Cómo sé si mis cánones son realistas?**
El modelo incluye cánones de mercado 2026 (Ciencuadras Q1-2026: promedio Bogotá
$47.821/m²/mes; FincaRaíz Prado Veraniego ~$1,84 M/mes promedio). Antes de decidir,
valide con 5-10 anuncios de arriendo en un radio de 5 km del lote y ajuste
`canon_m2_mes` por escenario.

---

## 8. Solución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| `FileNotFoundError` | Ejecutó desde otra carpeta | Ejecute con `cd` a la carpeta del modelo (paso 1) |
| Error de JSON al abrir | Coma o comilla mal puesta | Revise la línea indicada; valide en https://jsonlint.com |
| El informe no se ve bien | Archivo abierto con editor de texto | Ábralo con doble clic (navegador) |
| Quiere borrar resultados | — | Borre la carpeta `resultados_*`; se regenera al ejecutar |
