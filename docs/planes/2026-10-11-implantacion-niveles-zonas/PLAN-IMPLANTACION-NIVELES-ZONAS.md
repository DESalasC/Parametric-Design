# Plan — Implantación en el terreno, niveles (Stories) y volumetría de crujía única

- **Fecha:** 2026-10-11
- **Canvas:** `gh-definitions/F1_CONTEXTO_v13.2.ghx` (guardado 2026-10-10 13:50; 264 objetos)
- **Caso de prueba:** B — La Candelaria (`AAA0030JKOE`), 946,45 m², pendiente 25,85 % (Δ16,12 m), 5 niveles (3,6 + 3,0×4)
- **Referencias:** inventario `INVENTARIO-CANVAS-v13.2.md` (misma carpeta) · skills de arquitectura (`D:\Work\AI\skills\architect\skills\`) · skill de proyecto `disenoparametrico`
- **Estado de este documento:** propuesta para revisión del operador. **F0 ejecutado (2026-10-11)** — ver `F0-VERIFICACION-Y-SINCRONIZACION.md` (verificación en vivo + sincronización canvas→src). Fases F1–F4 por ejecutar.

---

## 1. Estado verificado (2026-10-11)

### 1.1 Cadena de implantación ya iniciada (ediciones del operador en el canvas, 2026-10-10)

| Paso | Componente | Qué hace hoy |
|---|---|---|
| Base normativa | `#199` Python 3 — `F1_ETAPA2_NORMATIVA_v10.py` | Publica `base_json` (schema `base_normativa_predio_v1`): `poligono_local`, `marco` {origen, x, y}, `retiro_frontal_m/posterior_m/lateral_m`, `pisos_limite`, `floor_h`, `presupuesto_ocupacion_m2`, `warnings`, `bloqueos`. |
| Distribución | `#116` F3_DISTRIBUCION (editado en canvas) | Franjas rectangulares en marco local (Y = hacia el fondo); recorte contra el lote (booleans, conserva piezas B{b}-R{r}); ajuste de área por **reducción centrada del ancho**; `cota_arranque_m` = **raycast al `topo_mesh`** en el centroide de cada pieza; salida `barras_json.bloques[]` con `huella_xy` (marco canvas). |
| Implantación | `#114` F3_VOLUM (editado en canvas) | Si llega `barras_implantadas_json`: reconstruye zonas por bloque×piso (perímetro a z = cota+f·h, centroide, nombre "B·usos", piso "B-Pn", altura=floor_h, atributos JSON), volúmenes y losas (áreas **brutas**, sin núcleo). |
| LC Zonas | `#197` Zone + `#189` Zone Settings | Cableados: `zonas_perimetros → P`, `zonas_centroides → SP`, `zonas_nombres → Name`, `zonas_pisos → Number`, `zonas_alturas → Height`, `#189 → S`. **Sin cablear:** Category, Subfloor Thickness, Layer, Home Story, ID, Property Settings. |
| Vecinos | `#51` F1_CONTEXTO50_BUILD v01.2 | Ya consume `z_base_m` (90/90 edificios con valor, −20,5…+1,7 en marco canvas). Falta validación en vivo. |
| Morphs | `#129` F3_MORPH_ATRIBUTOS | Salidas sin consumidores (morphs→ArchiCAD sigue pendiente, fuera de alcance de este plan salvo nota). |

### 1.2 Niveles (Stories) — capacidades disponibles

- **Live Connection:** solo **selectores** de stories ("Story Plane"); no crea.
- **Paquete `archicad` (JSON API):** revisión previa (F3_StorySync_v01, 2026-08-17) sin comando de creación → **re-verificar en F0**.
- **Tapir:** por verificar (plugin no localizado en las rutas habituales).
- **Manual (siempre posible):** Preferencias del proyecto → Configuración de pisos; luego verificar con `F3_StorySync --check`.

### 1.3 Reglas de diseño aplicables (skills de arquitectura)

| Regla | Valor | Fuente |
|---|---|---|
| Corredor de una crujía (single-loaded) | profundidad 6–9 m | `spatial-planning` §1.1 |
| Corredor de doble crujía | 12–18 m total (2×6–9 m + circulación) | `spatial-planning` §1.2 |
| Walk-up: crujía única | 6–8 m | `building-typology` §1.3 |
| Iluminación lateral: profundidad máxima | 2,0–2,5 × altura; 1 frente ≈ 2×h; 2 frentes ≈ 2,5×h por lado | `daylighting-design` §1.2 |
| Ventilación cruzada | requiere **aspecto doble** (dos frentes) | `building-typology` §3.1 |

**Conclusión operativa:** plataformas de **crujía única ≤ ~10 m de profundidad** (crujía 6–9 + circulación); los volúmenes actuales (>20 m) violan la condición → hay que **subdividir en más bloques (3–4)**, no estirar la profundidad.

---

## 2. Los 4 problemas → acciones

### P1. Primer nivel alineado con el nivel de acceso (y vecinos)

**Causa:** falta el dato «nivel de acceso»; el arranque sale del terreno en el centroide (aproximado) y el camino de compatibilidad sigue usando `altura_z` del programa (0 = esquina del lote).

**Acciones**
1. **Fetch v8:** agregar `topografia.acceso = {lado_id, z_media_m, z_min_m, z_max_m}` (cota MDT del lado frontal — el confirmado por el operador como calle de acceso; `perfil_lados` ya existe). Caso B: frente Occidente ≈ 2.635,5 m (abs).
2. **NORMATIVA v10 (`base_json`):** exponer `nivel_acceso_m` (abs y marco canvas) + `piso_alturas[]` acumuladas.
3. **#116:** política de plataformas: `B1 = nivel_acceso`; plataformas sucesivas = acceso + pasos de la grilla de niveles (P2); clamp: si el terreno local está más arriba, ajustar y avisar.
4. **#114:** ya usa `cota_arranque_m`; añadir al mensaje la cota usada ("arranque B1 = z_acceso").
5. **Vecinos (contexto50) — mecanismo anti-repetición:**
   - `z_base_m` ya viaja en datos y #51 lo consume (verificar en vivo);
   - re-ejecutar/revalidar `anclar_contexto50_zbase.py` por chip al refrescar contexto;
   - mensaje de #51 con min/max de `z_base` y aviso si todo queda en 0;
   - validación visual: bbox de vecinos vs `malla_terreno`.
6. Documentar en la skill `disenoparametrico`: «todo levantamiento vertical parte del nivel de acceso; `z_ref` solo define el marco local».

### P2. Niveles (Story Settings) — 5 niveles

**Set propuesto (caso B):** N1 = acceso (+0,00), N2 +3,60, N3 +6,60, N4 +9,60, N5 +12,60, N6/Tapa +15,60 (opcional).

**Acciones**
1. **Snap de plataformas a la grilla de niveles:** redondear las cotas de arranque de bloques a múltiplos de la grilla (corte/relleno), de modo que cada piso de cada bloque caiga en un nivel existente → evita "desfase vertical" por zona. *Variante si el operador prefiere no hacer snap:* crear 2–3 niveles específicos adicionales por plataforma (documentado).
2. **Generación:** `F3_StorySync v02` → `--plan` (escribe `niveles_deseados.json` desde base+bloques), `--check` (compara con ArchiCAD), `--crear` (si la API lo permite; si no: instrucciones manuales + `--check`).
3. **Home Story:** construir lista paralela a las zonas con el índice del nivel de su base (se deriva de bloque+planta) → conectar a `#189.Home Story`.
4. **Validación:** `--check` = 0 faltantes; en ArchiCAD: niveles a las cotas correctas; zonas/volúmenes en su nivel.

### P3. Crujía única y profundidad de zona

**Cambios en #116 (próxima versión, p.ej. v03.7; sobre la copia del canvas → src):**
1. Nuevo parámetro `crujia_max_m` (**default 10 m**; rango 9–12) — cap de profundidad de franja.
2. Si `profundidad calculada > crujia_max_m` → **subir n automáticamente** (hasta n_max=5) con aviso en mensaje; nunca profundidades > cap.
3. **Eliminar la reducción centrada del ancho** (genera huecos laterales): el área se ajusta por profundidad uniforme (≥ 6 m) o por n; el ancho se mantiene entre retiros/linderos.
4. **Orientación:** validar que `marco.x` sea paralelo al frente del lote (hoy se construye p1→p2; verificar orden del lado frontal); las zonas heredan `huella_xy` → corregir aquí corrige la orientación en ArchiCAD.
5. Mostrar recomendación: "n recomendado por crujía única: X" (la UI ya tiene `#83-Panel` para n objetivo).
6. Probar **n = 3 y n = 4** en caso B (cálculo manual del operador: ~4).

### P4. Volúmenes hasta los lados del predio (sin huecos)

1. Con P3.3 (sin shrink centrado), cada franja ocupa el **ancho útil completo** por banda Y; el recorte contra el polígono deja las piezas exactamente contra los bordes.
2. **Validaciones automáticas nuevas** (mensaje de #116):
   - (a) suma de áreas de bloques ≈ min(presupuesto, F2) ±2 %;
   - (b) por banda: la unión de piezas alcanza `xmin/xmax` del lote en esa banda (tolerancia 1 cm) o el borde es diagonal (reportar ancho efectivo);
   - (c) entre bloques: separación == `sep` sin bolsillos > 0,5 m².
3. Si quedan bolsillos por irregularidad del lote: rellenar la franja adyacente (respetando cap) o documentarlo (nunca dejar vacíos flotantes).

---

## 3. Decisiones pendientes (gates)

| ID | Decisión | Recomendación |
|---|---|---|
| D1 | Mecanismo de creación de Stories | verificar API/Tapir en F0; si no, manual + `--check` |
| D2 | Snap de plataformas a grilla de niveles | **Sí** (simplifica stories y zonas) |
| D3 | `crujia_max_m` | 10 m (ajustable 9–12) |
| D4 | Política de n_barras | auto hasta 4 + override manual |
| D5 | Categorías y capa de zonas | crear "Comercio"/"Vivienda"/"Núcleo" + capa "20-40-10_Zonas" (propuesta) y cablear Category/Layer/Subfloor(=0) |
| D6 | ID / Property Settings de zonas | opcional (documentar si se deja vacío) |

---

## 4. Fases de ejecución

| Fase | Contenido | Entregable |
|---|---|---|
| **F0** | Verificaciones (stories: API/Tapir; z_base vecinos en vivo) + **sincronizar ediciones canvas→src** (#116→`F3_DISTRIBUCION_v03.6`, #114→`F3_VOLUM v08.1`) + tests base | src actualizado, informe de verificación |
| **F1** | Multivolumen (P3 + P4): crujía_max, sin shrink centrado, n adaptativo, validaciones | v03.7 + patch canvas + tests caso B (n=3,4) |
| **F2** | Nivel de acceso (P1): fetch v8 + v10 + plataformas + vecinos | datos + componentes + prueba caso B |
| **F3** | Stories / Home Story (P2) | `niveles_deseados.json` + StorySync v02 + cableado |
| **F4** | Zonas finas (D5/D6) + validación integral en ArchiCAD + acta/vault | cierre documentado |

**Nota de riesgo:** hoy `#114` y `#116` tienen ediciones vivas en el canvas que **no** están en `src` (divergencia controlada). F0 las consolida antes de tocar código (regla del proyecto: `.py` no actualiza el canvas; y el canvas no debe quedar como única copia).

---

## 5. Punto 8 reformulado (registro del pedido 2026-10-09)

- La **limpieza del canvas** se hará **solo cuando el operador declare el canvas final** (hay elementos de apoyo en uso).
- **Inventario vivo entregado:** `INVENTARIO-CANVAS-v13.2.md` — por componente: número del macro, NickName, GUID, tipo, conexiones y clasificación (grupo / informativo-Panel / LC→ArchiCAD / lógica / entrada UI / soporte / otro) + notas (panel vacío, sin consumidores).
  - Resumen: 264 objetos — 19 lógica · 40 LC · 95 paneles · 44 UI · 39 soporte · 21 grupos · 6 por revisar.
- **Actualización:** re-ejecutar `scripts/utilities/inventario-canvas.py` tras cada guardado del canvas.
- **No eliminar** la cadena Zone (`#189`/`#197` y LC asociada) en las próximas correcciones (pedido expreso del operador).

---

## 6. Criterios de aceptación (al cerrar F4)

1. B1 de cada bloque arranca en el nivel de acceso (o plataforma de grilla inmediata superior) — verificado en ArchiCAD.
2. Vecinos de contexto50 a su cota de terreno (bbox vs malla).
3. Niveles N1…N5(+Tapa) creados; elementos y zonas en su nivel.
4. Cada volumen: crujía única (≤ crujía_max), dos frentes o patio, sin huecos laterales; n ∈ {3,4} validado.
5. Zonas con Name/Number/Height/Home Story (+ Category/Layer si D5) correctos; áreas brutas notadas hasta resta de núcleo.

---

## 7. Addendum A — Respuestas del operador (2026-10-11), profundización D1/D4 y estado F0

### 7.1 Decisiones registradas

- **D2 = SÍ** — snap de plataformas a la grilla de niveles (aprobado).
- **D3 = correcto** — `crujia_max_m` = 10 m (ajustable 9–12).
- **D4/D5 (clasificación de zonas) = usar las DOS clasificaciones** (por categoría y por nombre), alineadas a estándares internacionales. **Adoptado el marco BEP/ISO 19650** aportado por el operador: ver §7.3 y `REF-NOMENCLATURA-BEP-ISO19650.md`.
  - (La política de *n_barras* de la tabla §3 — “D4 original” — se mantiene: auto hasta 4 + override manual.)
- **D1 (nº de niveles)** — definible desde el canvas según el análisis de ocupación; especificado en §7.2.
- **F0 = ejecutado** — verificación en vivo (stories leídos: Ground Floor 0,000 / Story 3,000 / Story 6,000; API sin creación de stories) + sincronización canvas→src con backups. Detalle en `F0-VERIFICACION-Y-SINCRONIZACION.md`.

### 7.2 D1 — Número de niveles definible desde el canvas (especificación)

**Entradas del cálculo:**
- `G` = GFA objetivo (mix F2, ya en el pipeline).
- `A_i` = área de cada bloque/plataforma (#116) · `ΣA` = huella por nivel.
- `h_k` = alturas de entrepiso por piso (p. ej. [3,6, 3,0, 3,0, 3,0, 3,0]).
- `L` = `pisos_limite` (POT, v10) · `H_max` = altura máxima POT.

**Regla propuesta (pisos uniformes por bloque):**
```
p* = ceil(G / ΣA_i)
p_altura = máximo p tal que Σ(k=1..p) h_k ≤ H_max
pisos_finales = min(p*, p_altura, L)
```
- Si `p* > min(p_altura, L)` → aviso de rediseño (más plataformas / menos GFA / revisar retiros).
- Caso fino por bloque (p_i distintos) = extensión posterior; fase actual usa pisos uniformes.

**Integración en el canvas (F1):**
1. Bloque “PISOS”: `Value List` (auto | manual) + `Number Slider` (manual) + `Panel` de diagnóstico.
2. Salida `pisos_finales` + `pisos_motivo` → alimenta #116 (`bloques.pisos`; hoy fijo = `pisos_limite`) y `StorySync --plan`.
3. Mensaje #116: `p* (G/ΣA) · límite POT · altura máx → pisos finales`.

### 7.3 D4 — Nomenclatura y clasificación de zonas (marco BEP/ISO 19650 adoptado)

**Principio de tres capas (siempre separadas):**
1. **Identificador técnico** (código): `[NIVEL]-[ZONA]-[CATEGORIA]-[CONSECUTIVO]` — ej. `GF-Z1-COM-001`.
2. **Nombre descriptivo:** "Local comercial 1" (va al `Name`).
3. **Clasificación normalizada:** Uniclass/COBie (va a `Category`/Property; códigos exactos a validar contra tablas oficiales en F4).

**Catálogos adaptados al proyecto (DiseñoParamétrico):**

| Catálogo | Códigos propuestos | Nota |
|---|---|---|
| Niveles | `SIT`, `GF`, `L01`–`L04`, `RF` (+`ZZ`,`XX`) | GF = nivel de acceso (hoy B1); L01.. = plantas siguientes; RF = tapa (opcional). Los alias B1..B5 del canvas se mantienen hasta el renombre formal. |
| Zonas | `Z1`–`Zn` (plataformas/bloques) + `ZN` (núcleo, si aplica) | n según layout (3–4); lista se cierra en F1. |
| Categorías | `VIV`, `COM`, `CON`, `CIR`, `SER`, `PAR`, `EXT` | Vivienda, Local comercial, Consultorios, Circulación, Servicios, Parqueo, Exterior. Diccionario cerrado. |

**Reglas (BEP):** solo `A-Z 0-9 -`; sin espacios/acentos/`#`/`/`; sin versiones en el código; consecutivo reinicia por NIVEL+ZONA+CATEGORÍA; números no se reutilizan; códigos nuevos solo vía catálogo (operador = gestor).

**Mapeo a la cadena LC (Zonas → ArchiCAD):**
- `Zone.Number` ← **Space_Number** (código técnico; hoy "B1-R1-P2" → migrar).
- `Zone Settings.Name` ← **Space_Name** descriptivo (hoy "B1-R1 · usos" → migrar).
- `Zone Settings.ID` ← identificador único estable.
- `Zone Settings.Category` ← categoría del catálogo (pendiente cablear; requiere crear las Zone Categories en ArchiCAD).
- Property/Classification ← Uniclass/COBie (F4; el API AC dispone de `SetClassificationsOfElements`).

**QC (checklist):** 0 duplicados · 0 zonas sin número · 0 categorías fuera de catálogo · 100 % con nivel válido → script de validación en F4 sobre la lista de zonas que emite el canvas.

**Estado:** especificado; el cableado (Name/Number ajustados, Category) se ejecuta en F1/F3–F4 sobre la copia sincronizada.

### 7.4 Ajustes del operador (2026-10-11 noche) — aplicados en src v03.7

Tras la validación en vivo (volúmenes a las alturas correctas), el operador pidió:
1. **Sin antejardines en frentes públicos + eliminar el vacío posterior** → v03.7: franjas **ancladas a frente y fondo**; el remanente de área se reparte **uniformemente en las separaciones entre bloques** (aviso si la base trae retiros > 0 para revisar).
2. **Empatar con vecinos (alturas)** → mecanismo **pisos por bloque**: `pisos_por_bloque` (directo) o `limites_pisos_json` (bandas desde el frente con `max_pisos` + redistribución del sobrante al último bloque) — pensado para el caso: aligerar frentes, cargar el bloque posterior. Base reglamentaria: ADR-022 §3–4 (empates norte/sur); regla "5 m" del operador **pendiente de validar con IDPC** (parametrizable).
3. **Story Settings con alturas de piso** → F3 próximo paso: generar `niveles_deseados.json` (cotas por piso/bloque desde el nivel de acceso, snap a la grilla) + `F3_StorySync v02 (--plan/--check)`; creación manual asistida (API sin creación, ver §2 de este reporte).
4. (Diferido) Subdivisión fina de volúmenes según recomendaciones F2 — fase posterior.
