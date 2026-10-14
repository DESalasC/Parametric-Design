# D2 — Precisión: regla patio / separaciones + corrección del script

- **Fecha:** 2026-10-13 · **Proyecto:** DiseñoParamétrico · **Caso:** AAA0030JKOE (lote actual)
- **Origen:** precisión del operador sobre el documento `estado-avance-disenoparametrico.md` (ítem "Resta de patio geométrica") y "corrección del script".

---

## 1. Texto del pedido (operador, 2026-10-13)

> «…es necesario una aclaración y corrección del script debido a que existe un “patio” con dimensiones mínimas de 9 m2 y lado menor de 3 ml, pero esos solo aplica en el caso de un lote donde no haya la posibilidad de un solo “bloque” constructivo, en el caso particular del lote actual, no existen patios sino separaciones entre los diferentes volúmenes.»

## 2. Regla vigente (confirmada)

Concordante con las **reglas aprobadas 2026-10-03** (encabezado de `F1_ETAPA2_PATIO_v03.py` y nota de cálculo de `F1_ETAPA2_NORMATIVA_v09.x`):

| Caso | Regla |
|---|---|
| **1 volumen** (lote resuelto con un solo bloque constructivo) | Patio normativo Anexo 5 §1.12.b: **H/3, ≥ 9 m², lado ≥ 3 ml** (resta booleana sobre la envolvente cuando aplique) |
| **≥ 2 volúmenes** | **NO se generan patios independientes**: rigen las **separaciones entre volúmenes** (separación mínima entre cuerpos = máx(6,0 m; 0,2·altura; 2 %·h NSR-10)) y **computan en IO** |
| **Lote actual (4 volúmenes)** | **Separaciones** entre los cuerpos; **sin patios** |

**Nota de interpretación (para confirmar):** la frase «esos solo aplica en el caso de un lote donde no haya la posibilidad de un solo bloque constructivo» se registra textual. La implementación sigue la concordancia 10-03/10-13: el patio con mínimos 9 m²/3 ml es del régimen de **un solo volumen**; el lote actual (multivolumen) queda con separaciones y sin patios. Si la intención fuese otra para algún caso futuro de lote, se parametriza en una nueva subversión.

## 3. Corrección aplicada (código fuente, sin tocar el canvas)

**`F1_ETAPA2_PATIO_v03.py` → v03.4** (subversión registrada en encabezado):

1. **Modo MULTI (n ≥ 2 forzado): `patios_curves = []`** — retirada la "regla v1" de patios por esquina interior (v03.0–v03.3, que estaba *sujeta a validación del operador*). Mensaje: «Regla v03.4 (2026-10-13): con >=2 volumenes rigen las separaciones entre volumenes (computan en IO); sin patios independientes».
2. **Modo AUTO con n inferido ≥ 2: `patios_curves = []`** — mismo criterio; el mensaje informa «modo AUTO | n_volumenes inferido: N (esquinas validas / capacidad)».
3. **Modo UNICO (n = 1): intacto** (v02.5 estricto: 1 patio máx. desde V_N, garantías 9 m²/3 ml).
4. **Fix de robustez (modo único):** inicialización de `aceptados = []` — el bloque de diagnóstico de IO referenciaba la variable y podía lanzar `NameError` en modo único (bug latente detectado por los tests).
5. **Mensajes/versión:** todas las salidas pasan a `PATIO v03.4`; sugerencia del modo único actualizada («n_volumenes=0 (AUTO)…»).
6. **Export F1.5** (`data/pot-cache/<CHIP>-lados.json`): `generado_por = F1_ETAPA2_PATIO_v03.4`; en multi el bloque `patio` queda con `count: 0` y el mensaje de la regla.

**Tests** — `tests/test_patio_v03_bifurcacion.py` actualizado a la semántica v03.4 y **corregido el stub** (inyección idempotente y completa de `Curve/Brep/AreaMassProperties`; antes quedaba "contaminado" por otros módulos y los casos daban falsos negativos):
- `12/12` en aislamiento · `38/38` junto al resto de pruebas "patio" de la carpeta.

**Precisión en el documento de estado** (`estado-avance-disenoparametrico.md`):
- Ítem 2 de "Bloqueantes resueltos (Corte de Sesión)": se añadió la nota **Precisión (2026-10-13)** con la regla 1 vol / ≥2 vol.
- Se agregó el corte **2026-10-13** (superposición de volúmenes + esta precisión, con enlaces).

## 4. Condiciones · limitaciones · resultado esperado

- **Condición:** el código `src` es la fuente; el canvas se actualiza por parche + recarga del operador (protocolo: GH cerrado; no pisar ediciones vivas). **El re-embebido de #78 (PATIO → v03.4) queda PENDIENTE** para la próxima ventana de parche (junto con #198 fix (d)).
- **Limitación:** hasta que el canvas no tenga v03.4, una corrida seguiría generando los 3 "patios" de esquina del modo AUTO para este lote (y restándolos al envelope en NORMATIVA). Para la próxima corrida: aplicar parches o poner el slider `n_volumenes` en **1** sólo si se quisiera forzar el régimen único (no recomendado para este lote).
- **Resultado esperado (tras el parche):** mensaje `PATIO v03.4 | modo AUTO | n_volumenes inferido: 3 … Generados: 0 | Regla v03.4…`; `env` sin recortes de patio; separaciones gobernando el diseño en F3.
