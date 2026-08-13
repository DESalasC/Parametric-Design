# Manual de Uso — Modelo Financiero de Prefactibilidad (Fase 2)

**Versión:** 2.1 (agosto 2026) · **Proyecto:** DiseñoParamétrico · **Lote de referencia:** AAA0127AZPA

Este manual está escrito para una persona **sin conocimientos técnicos** de programación ni de
modelos financieros. Si usted puede abrir una carpeta y copiar un texto, puede usar este modelo.
Cada sección explica *qué hace*, *cómo se hace* y *qué significa lo que ve*.

---

## 1. ¿Qué es esto y para qué sirve?

Es un **modelo de prefactibilidad inmobiliaria**: una calculadora grande y organizada que responde
una sola pregunta:

> **"Dado un lote con un área máxima construible (GFA), ¿qué tipo de edificio conviene construir
> (vivienda de interés social, estándar o lujo) y cuánta utilidad deja?"**

El modelo compara **3 escenarios** (A = VIS/VIP, B = Estándar, C = Lujo) para **el mismo edificio**,
calcula los ingresos, los costos y la utilidad de cada uno, revisa si cumplen las reglas mínimas de
rentabilidad de Bogotá, y le dice **cuál conviene y por qué**. También calcula:

- **Cuánto riesgo** tiene cada alternativa (sensibilidad ±10%).
- **Qué pasa si el dueño del lote participa con su terreno** en las utilidades finales, en vez de
  venderlo (escenario D).
- **La opción de arrendar el lote** en lugar de comprarlo (escenario E), con el canon calculado
  sobre el precio pedido y sobre el valor que el mercado realmente soporta.
- **El flujo de caja estimado** (cuánto dinero entra y sale cada trimestre durante 24 meses) de la
  mejor alternativa, en tres modalidades: compra, aporte o arriendo del lote.

**Qué NO hace** (por ahora): no incluye financiación bancaria, ni TIR/VPN (eso es la Fase 3), ni
conceptos legales o urbanísticos. Es una herramienta de decisión preliminar.

---

## 2. Requisitos previos

Necesita tres cosas, en este orden:

| # | Requisito | Qué es | Cómo verificarlo |
|---|---|---|---|
| 1 | Un computador con **Windows** | Cualquier PC con Windows 10 o 11 | El modelo se creó y probó en Windows |
| 2 | **Python** instalado (versión 3.8 o superior) | El "motor" que ejecuta el modelo | Abra el símbolo del sistema (tecla Windows, escriba `cmd`, Enter) y escriba `python --version`. Si aparece algo como `Python 3.12.x`, listo. Si dice "no se reconoce", instale Python desde <https://www.python.org/downloads/> (marque la casilla *"Add Python to PATH"* al instalar) |
| 3 | La carpeta del modelo | `D:\Work\PROJECTS\DiseñoParametrico\src\fase-2-demanda\F2_Modelo_Financiero` | Abra el Explorador de Windows y verifique que exista esa ruta |

**No necesita** instalar nada más: el modelo usa únicamente funciones que vienen con Python.
Tampoco necesita internet para ejecutarlo (solo para consultar las fuentes de datos citadas).

### ¿Qué hay dentro de la carpeta?

| Archivo / carpeta | Qué es |
|---|---|
| `F2_DEMANDA_MOTOR_v01.py` | **El programa.** No lo modifique (a menos que sepa programar) |
| `parametros_entrada.json` | **Los datos de entrada del caso de referencia** (edítele aquí los números) |
| `parametros_AAA0127AZPA.json` | Datos del lote real AAA0127AZPA según el pipeline de demanda |
| `parametros_AAA0127AZPA_mercado2026.json` | El mismo lote con precios y costos de mercado 2026 (GFA 633 m², los más recientes) |
| `parametros_AAA0127AZPA_gfa1054_mercado2026.json` | **Alternativa de curaduría**: mismo lote con GFA 1054,49 m² (la zona está autorizando mayor edificabilidad) |
| `verificacion_independiente.py` | Programa de verificación (control de calidad; no necesita tocarlo) |
| `README.md` | Ficha técnica rápida |
| `resultados\` y `resultados_AAA0127AZPA*\` | Carpetas donde el modelo guarda sus resultados |

---

## 3. Cómo ejecutar el modelo (paso a paso)

1. Presione la tecla **Windows**, escriba `cmd` y presione **Enter**. Se abre la "ventana negra"
   (símbolo del sistema).
2. Escriba esta línea y presione Enter (cámbiela si su ruta es otra):

   ```
   cd /d D:\Work\PROJECTS\DiseñoParametrico\src\fase-2-demanda\F2_Modelo_Financiero
   ```

3. Ejecute el modelo. **Opción recomendada** (lote real con datos de mercado 2026):

   ```
   python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_mercado2026.json --outdir resultados_AAA0127AZPA_aporte
   ```

4. Espere unos segundos. Al final verá una tabla con los 3 escenarios y las líneas de resumen
   (sección 5 de este manual le enseña a leerla).
5. Abra el informe: en el Explorador vaya a la carpeta
   `resultados_AAA0127AZPA_aporte` y abra el archivo `informe_F2_prefactibilidad.html`
   (doble clic; se abre en su navegador).

**Variantes útiles:**

```bash
# Caso de referencia (sin lote real): usa parametros_entrada.json
python F2_DEMANDA_MOTOR_v01.py

# Reproducir exactamente los números del pipeline de demanda (datos originales)
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA.json --outdir resultados_AAA0127AZPA

# Forma compatible con el pipeline (--chip --gfa --costo-lote)
python F2_DEMANDA_MOTOR_v01.py --chip AAA0127AZPA --gfa 632.695061 --costo-lote 1200000000

# Ejecutar la alternativa de curaduría (GFA 1054,49 m2)
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_gfa1054_mercado2026.json

# Fijar el porcentaje de utilidades para el dueño del lote (escenario D)
python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_mercado2026.json --pct-socio 30
```

Cada ejecución genera 5 archivos en la carpeta `--outdir` (o `resultados` si no la indica):
`resultados_completos.json` (todos los números), `comparativo_escenarios.csv`,
`sensibilidad.csv`, `flujo_caja_<escenario>_compra.csv`, `flujo_caja_<escenario>_aporte.csv`
y el informe `informe_F2_prefactibilidad.html`.

---

## 4. Cómo cambiar los datos

Los datos se cambian en el archivo **`parametros_AAA0127AZPA_mercado2026.json`** (o el que quiera
usar), **nunca en el programa**. Ábralo con el Bloc de notas (clic derecho → *Abrir con* → *Bloc de
notas*). Respete el formato: cada dato va entre comillas y después de dos puntos.

**Consejo:** antes de editar, haga una copia del archivo (por ejemplo
`parametros_prueba.json`) y ejecute `python F2_DEMANDA_MOTOR_v01.py --parametros parametros_prueba.json`.
Si rompe el formato, el modelo le dirá cuál línea tiene el error.

Los campos que más le interesarán:

| Campo (en el JSON) | Qué significa | Dónde conseguir el valor |
|---|---|---|
| `gfa_max_m2` | Área máxima construible (m²) que permite la norma. **No lo cambie por su cuenta**: viene de la Fase 1 | Documento de Fase 1 / curaduría |
| `lote.area_m2` | Área del lote (m²) | Certificado de tradición / catastro |
| `lote.precio_suelo_m2` | Precio del suelo por m² (COP) | Negociación / avalúo. Si conoce el valor total, use `costo_lote_total_cop` |
| `lote.costo_lote_total_cop` | Valor total del lote incluido impuestos (COP). **Si está presente, manda sobre el precio por m²** | Escritura / oferta del dueño |
| `escenarios.A/B/C.precio_venta_m2` | Precio de venta por m² de cada producto (COP) | Comparables de la zona (ver sección 9) |
| `escenarios.A/B/C.costo_construccion_m2` | Costo de construcción por m² (COP) | Cotizaciones de constructoras |
| `financiero.costos_blandos_pct` | Costos de diseño, permisos, gerencia (%), sobre el costo duro | Práctica de mercado: 12–15% |
| `financiero.marketing_ventas_pct` | Comercialización (%), sobre los ingresos | Práctica de mercado: 3–4% |
| `escenarios.*.eficiencia_ntg_pct` | Porcentaje del GFA que se puede vender (el resto son zonas comunes) | Diseño preliminar: 0,68–0,80 |
| `reglas_decision` | Los umbrales de decisión (MUB 18–25%, ROI 22%, CL/IT 25–30%) | Reglas internas del estudio; se pueden ajustar aquí |
| `aporte_suelo.pct_socio` | Porcentaje de utilidades para el dueño del lote (escenario D). Si lo deja en `null`, el modelo propone el punto medio de la ventana de negociación | Negociación |
| `arriendo_lote.mensual_pct_cl` / `meses` | Canon de arriendo del lote: % mensual del valor y duración en meses (escenario E) | Contrato de arrendamiento / negociación |
| `flujo_caja.*` | El programa de ingresos y costos por trimestre (avanzado; los valores por defecto son razonables) | Solo si quiere afinar |

Después de editar, vuelva a ejecutar (sección 3). **No hay que recompilar nada.**

---

## 5. Qué significan las cifras (léalo con calma)

El modelo usa 8 cifras principales. Todas están en pesos colombianos (COP) y en millones (M$)
en las tablas. Usamos los números del lote AAA0127AZPA para que vea ejemplos reales.

| Sigla | Nombre | Qué es, en palabras simples | Fórmula (para curiosos) | Ejemplo (escenario B, mercado 2026) |
|---|---|---|---|---|
| **GFA** | Área máxima construible | Cuántos m² de construcción permite la norma | Viene de la Fase 1 | 633 m² |
| **NGA** | Área neta vendible | Del GFA, cuánto se puede **vender** (lo demás son pasillos, escaleras, zonas comunes) | GFA × eficiencia | 633 × 0,75 = 475 m² |
| **Unidades** | Apartamentos | Cuántas unidades salen, según el tamaño de cada una | NGA ÷ m² por unidad (se redondea hacia abajo) | 5 unidades de 85 m² |
| **IT** | Ingresos totales | Todo el dinero que entra por vender todo | NGA vendible × precio por m² | $3.060 M |
| **CD** | Costo duro | Lo que cuesta **construir** (materiales y mano de obra) | GFA × costo por m² | $1.898 M |
| **CB** | Costos blandos | Diseño, licencias, gerencia del proyecto | 15% del CD | $285 M |
| **CMV** | Comercialización | Publicidad y comisiones de venta | 4% del IT | $122 M |
| **CL** | Costo del lote | Lo que cuesta el terreno (incluido impuestos) | área × precio/m² × (1 + 4%) | $1.200 M |
| **CTD** | Costo total del desarrollo | Todo lo que se gasta | CL + CD + CB + CMV | $3.505 M |
| **UB** | Utilidad bruta | Lo que queda al final | IT − CTD | **−$445 M** (¡pierde!) |
| **MUB** | Margen sobre ventas | Qué porcentaje de cada peso vendido es ganancia | UB ÷ IT × 100 | −14,6% |
| **ROI** | Retorno sobre la inversión | Cuánto gana por cada peso invertido | UB ÷ CTD × 100 | −12,7% |
| **CL/IT** | Peso del suelo | Qué porcentaje de las ventas se lo come el lote | CL ÷ IT × 100 | 39,2% |

**Reglas de decisión que usa el modelo** (estándar para Bogotá):

- **MUB < 18%** → margen de alto riesgo. **> 25%** → atractivo.
- **ROI < 22%** → no conviene desarrollar (no compensa el riesgo).
- **CL/IT > 25%** → el suelo pesa mucho, precaución. **> 30%** → el lote es demasiado caro para
  desarrollar y vender: la recomendación automática es **evaluar arrendar el lote** o renegociar.

---

## 6. Cómo leer la recomendación final

Al final de la ejecución, el modelo imprime un bloque que empieza con **`RECOMENDACION:`** y
después `[NO VIABLE]` o `[VIABLE]`. Ejemplo real del lote AAA0127AZPA:

```
RECOMENDACION:
  [NO VIABLE] Ningun escenario cumple las reglas de viabilidad (MUB >= 18%, ROI >= 22%, CL/IT <= 30%).
  Conclusion: con los parametros actuales el lote no soporta desarrollo y venta bajo las reglas de
  Bogota. Opciones: (1) renegociar el precio del suelo, (2) validar precios de venta reales con
  comparables de radio 5 km, (3) evaluar alternativa de arriendo del lote.
```

**Cómo interpretarlo:**

1. Mire el **estado**: si dice `NO VIABLE`, ningún producto funciona como está planteado. No es un
   fracaso del modelo: es la información más valiosa que puede obtener antes de gastar dinero.
2. Mire **por qué**: las líneas `[CRITICA]` debajo de la tabla le dicen exactamente qué regla se
   incumple (ej.: `CL/IT 39.2% > 30.0%`). En nuestro caso el problema es **el precio del lote**,
   no el diseño.
3. Mire la **sensibilidad** (sección 4 del informe): dice qué variable mueve más la utilidad.
   Aquí: *precio de venta* (impacto 9,6%) y *costo duro* (6,4%) — es decir, si los precios reales
   de la zona son mejores de lo asumido, el proyecto cambia; por eso conviene validarlos con
   comparables antes de decidir.
4. Si el estado es `NO VIABLE`, las opciones del texto son su plan de acción.

---

## 7. Escenario D: el dueño del lote participa en las utilidades

**Idea:** en vez de que el desarrollador compre el lote (pagar $1.200 M por adelantado), el **dueño
entrega el lote al proyecto** y, al final, recibe un **porcentaje de las utilidades**. El
desarrollador no desembolsa el lote, por lo que su rentabilidad sube; el dueño apuesta a que el
proyecto gane más de lo que le pagarían hoy.

El modelo calcula la **ventana de negociación** para cada escenario:

- **pct mínimo (dueño):** el porcentaje con el que el dueño recibe al menos lo que el mercado
  pagaría por su lote (el "CL soportable": lo máximo que un comprador desarrollador pagaría
  dejando ROI 22%).
- **pct máximo (desarrollador):** el porcentaje que deja al desarrollador su ROI mínimo (22%).
- **Recomendado:** el punto medio de esa ventana (o el valor de `--pct-socio` si lo fijó).

Resultado real del lote AAA0127AZPA (datos de mercado 2026):

| Escenario | Utilidad sin suelo | ROI máx. desarrollador | Ventana | pct recomendado | ROI desarrollador | Dueño recibe |
|---|---|---|---|---|---|---|
| A — VIS | $573,0 M | 32,4% | 26,4% – 32,2% | 29,3% | 22,9% | $167,6 M |
| **B — Estándar** | **$754,8 M** | **32,7%** | **26,9% – 32,8%** | **29,9% ≈ 30%** | **23,0%** | **$225,3 M** |
| C — Lujo | $327,3 M | 10,0% | sin acuerdo | — | — | — |

**Lectura:** con la compra del lote, **todos** los escenarios pierden dinero (ROI −12,7% a −21,1%).
Pero si el dueño **aporta el lote a cambio de ~30% de las utilidades**, el escenario B (Estándar)
pasa a ser **viable**: el desarrollador obtiene ROI 23% y el dueño recibe **$225,3 M** al final del
proyecto. El escenario C nunca funciona, ni siquiera con el lote gratis, porque sus costos de lujo
se comen la utilidad.

**Dato clave para negociar:** los $225,3 M que recibiría el dueño equivalen al **18,8%** del precio
que pide por el lote ($1.200 M). En otras palabras, el mercado (y el modelo) dicen que ese lote
"soporta" unos **$204 M** para un desarrollo; el precio pedido está **~6 veces por encima** de lo
que el proyecto puede pagar. Si el dueño quiere más, los precios de venta de la zona deben ser
mayores — valídelos con comparables.

---

## 8. El flujo de caja estimado (24 meses)

El modelo calcula **cuánto dinero entra y sale cada trimestre** (8 trimestres = 24 meses) para la
mejor alternativa, en tres modalidades:

- **A — Compra:** el lote se paga al inicio (trimestre 0). Saldo final = utilidad del escenario.
- **B — Aporte:** el lote no se paga; el dueño recibe su porcentaje al cierre (trimestre 7).
- **C — Arriendo:** el lote no se paga; se paga un canon por trimestre y el lote vuelve al dueño al final.

**Supuestos del programa** (editables en el JSON, campo `flujo_caja`):

- **Ingresos:** 20% se recibe al apartar (meses 1–6), 40% durante la obra (meses 7–18) y 40%
  contra la entrega (meses 19–24).
- **Costo duro:** 30% en los trimestres 1–2, 40% en 3–4, 30% en 5–6.
- **Blandos:** 25% por trimestre durante el primer año.
- **Comercialización:** se paga a medida que entran los ingresos.
- **Cierre:** al trimestre 7, en modalidad B, se paga al dueño su participación.

Resultado real para el escenario B (mejor alternativa) del lote AAA0127AZPA:

| Trimestre | Meses | Ingresos | Lote | Costo duro | Blandos | Mkt | Reparto dueño | Flujo neto | Acumulado |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 00-03 | $0 | $1.200 M | $0 | $71 M | $0 | — | −$1.271 M | −$1.271 M |
| 1 | 03-06 | $306 M | $0 | $285 M | $71 M | $12 M | — | −$62 M | −$1.333 M |
| 2 | 06-09 | $306 M | $0 | $285 M | $71 M | $12 M | — | −$62 M | −$1.395 M |
| 3 | 09-12 | $306 M | $0 | $379 M | $71 M | $12 M | — | −$157 M | −$1.552 M |
| 4 | 12-15 | $306 M | $0 | $379 M | $0 | $12 M | — | −$86 M | −$1.638 M |
| 5 | 15-18 | $306 M | $0 | $285 M | $0 | $12 M | — | $9 M | −$1.629 M |
| 6 | 18-21 | $306 M | $0 | $285 M | $0 | $12 M | — | $9 M | −$1.620 M |
| 7 | 21-24 | $1.224 M | $0 | $0 | $0 | $49 M | — | $1.175 M | **−$445 M** |

*(En la modalidad B —aporte—, la fila 0 no paga el lote y la fila 7 incluye el reparto al dueño;
el saldo final es +$529 M. En la modalidad C —arriendo—, en vez del lote se paga un canon de
$27 M/trimestre y el saldo final es +$538,8 M.)*

**Cómo leerlo:** el saldo acumulado se hunde los primeros trimestres (se construye antes de que
entren las ventas) y se recupera al final. El último número de la columna "Acumulado" **debe
coincidir con la utilidad bruta** del escenario; el modelo lo verifica e imprime `chequeo OK`.
Si ve `INCONSISTENTE`, avise al responsable del modelo: algo se cambió mal en el JSON.

---

## 9. Escenario E: arriendo del lote (cuando el lote es demasiado caro para comprarlo)

**Idea:** en lugar de comprar el lote (o de que el dueño participe en las utilidades), el
desarrollador **arrienda el lote durante el ciclo** (24 meses), paga un **canon mensual** y al
final el lote vuelve al dueño. Es la alternativa que el modelo sugiere automáticamente cuando
CL/IT > 30% (el suelo se come más del 30% de las ventas).

El canon por defecto es **0,75% mensual del valor del lote** (editable en `arriendo_lote` del
JSON). El modelo lo calcula sobre **dos bases**: el precio pedido ($1.200 M) y el **valor que el
mercado soporta** (el CL que daría ROI 22% comprando).

Resultado real del lote AAA0127AZPA (mercado 2026):

| Escenario | Canon s/ pedido (24 meses) | ROI | Canon s/ valor soportable | ROI | Estado |
|---|---|---|---|---|---|
| A — VIS | $216,0 M | 18,0% | $27,2 M | 30,4% | viable s/ soportable |
| **B — Estándar** | **$216,0 M** | **21,4%** | **$36,5 M** | **30,7%** | **viable s/ soportable** |
| C — Lujo | $216,0 M | 3,2% | $0,0 M | 10,0% | no viable |

**Lectura:** con el canon calculado sobre el **precio pedido**, ningún escenario alcanza el ROI
mínimo (el B queda en 21,4%, apenas por debajo del 22%). Pero si el canon se negocia sobre el
**valor soportable** (~$200 M), A y B son **viables** (ROI 30%+). La palanca real no es el
producto sino **sobre qué valor se negocia el canon**.

**Diferencia con el escenario D (aporte):** en el aporte, el dueño recibe un porcentaje de las
utilidades al cierre (apuesta a que el proyecto gane) y no recupera el lote durante el ciclo; en
el arriendo, el dueño recibe un canon periódico garantizado y recupera el lote al final. El
arriendo es más conservador para el dueño; el aporte le da mayor potencial de ganancia.

## 10. Preguntas frecuentes

- **¿El modelo "decide" por mí?** No. Le da números y reglas; la decisión final es suya (con su
  equipo técnico y jurídico).
- **¿Puedo confiar en los precios de venta?** Son referencias de mercado 2026 (fuentes citadas en
  la sección 8 del informe), pero **deben validarse con comparables reales del sector** (radio 5 km).
  El modelo le dice cuánto le duele un error: ±10% en precio = ±9,6% de los ingresos.
- **¿Por qué todos los escenarios salen NO VIABLES?** Porque el lote cuesta $1.200 M y el proyecto
  solo "soporta" ~$204 M de suelo. El problema es el precio del lote, no el diseño.
- **¿Qué hago si quiero cambiar solo el precio de venta?** Edite
  `escenarios.B.precio_venta_m2` en el JSON y vuelva a ejecutar (sección 3).
- **¿Qué es un "comparables de radio 5 km"?** Precios reales de apartamentos en venta en un radio
  de 5 km alrededor del lote. Se consiguen en Ciencuadras, Metrocuadrado, Finca Raíz, o con
  corredores de la zona.
- **¿Puedo abrir los resultados en Excel?** Sí: los archivos `.csv` se abren con doble clic.
- **¿Y si no tengo Python?** Instálelo desde <https://www.python.org/downloads/> marcando
  *"Add Python to PATH"*. Es gratuito.

---

## 11. Solución de problemas

| Síntoma | Causa probable | Solución |
|---|---|---|
| `'python' no se reconoce` | Python no está instalado o no quedó en el PATH | Reinstale Python marcando *"Add Python to PATH"* y **abra una ventana cmd nueva** |
| `No existe el archivo de parametros: ...` | Escribió mal el nombre del JSON o está en otra carpeta | Verifique que el archivo esté en `D:\Work\PROJECTS\DiseñoParametrico\src\fase-2-demanda\F2_Modelo_Financiero` y el nombre exacto |
| `JSONDecodeError` / "caracter inesperado" | Se rompió el formato del JSON al editarlo (comilla o coma de más) | Compare con una copia original; recuerde: comas entre campos, ninguna después del último |
| El informe HTML sale en blanco o cortado | El archivo se abrió mientras el modelo lo escribía | Espere a que termine la ejecución (`chequeo OK` en pantalla) y ábralo de nuevo |
| Los números no coinciden con otra corrida | Se usó otro archivo de parámetros o los datos cambiaron | Mire la línea `Fecha de datos` y el nombre del JSON en la salida |
| `flujo_caja: las listas ... deben sumar > 0` | Se editó el campo `flujo_caja` y las listas quedaron mal | Restaure los valores por defecto de la sección 8 |

---

## 12. Guía rápida de una sola página

```
1. Abrir cmd → cd /d D:\Work\PROJECTS\DiseñoParametrico\src\fase-2-demanda\F2_Modelo_Financiero
2. Ejecutar → python F2_DEMANDA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_mercado2026.json
3. Ver la tabla de escenarios → ¿VIABLE o NO VIABLE? ¿por qué (alertas CRITICA)?
4. Ver ESCENARIO D (aporte) y ESCENARIO E (arriendo) → ¿existe ventana de acuerdo? ¿pct / canon viable?
5. Ver FLUJO DE CAJA → ¿chequeo OK? saldo final = utilidad bruta (3 modalidades)
6. Abrir informe_F2_prefactibilidad.html en el navegador para el detalle completo
```

Si algo no cuadra o aparece un error que no está en esta tabla, guarde el texto de la ventana negra
y envíelo al responsable del modelo junto con el archivo JSON que usó.
