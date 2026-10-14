# D1 — Diagnóstico: superposición de volúmenes (ArchiCAD / previsualización) — 2026-10-13

- **Proyecto:** DiseñoParamétrico · **Caso vivo:** B — AAA0030JKOE (Test 07.pln) · **Fecha:** 2026-10-13
- **Solicitud del operador:** revisar la mezcla de "dos volúmenes masivos" (fase anterior) con "cuatro volúmenes separados" (ocupación actual) que aparece en ArchiCAD y en la previsualización de Rhino; registrar evidencia (imagen) y establecer un plan de acción. Pendientes asociados: **separaciones laterales** (que eran perpendiculares al lado paralelo a la vía y no coincidían con los bordes del lote) y **espacio posterior** contra el borde del lote.

---

## 1. Actividades realizadas (verificación en vivo, solo lectura)

| # | Verificación | Instrumento | Resultado |
|---|--------------|-------------|-----------|
| 1 | Estado de niveles (stories) | `F3_StorySync_v02.py --list` (API JSON ac29) | **3 stories** (Ground Floor 0.000 / Story 3.000 / Story 6.000) — el plan vigente requiere **8** (GF..L07) |
| 2 | Censo de elementos vivos | `src/interfases-archicad/F0_CENSO_ELEMENTOS_v01.py` (**nuevo**, solo lectura) | **Zones 16** · Morph 71 · Mesh 1 · Slab/Wall/Column/Beam/Shell/Roof/Stair = 0 |
| 3 | Propiedades de las 16 zonas | `scripts/utilities/_tmp-zonas-propiedades.py` (**nuevo**, solo lectura) | Todas con nomenclatura **BEP v08.1** (`GF-Z1-COM-001`…): Bloques 1–3 con 5 pisos; **Bloque 4 solo Piso 1** |
| 4 | Bounding boxes por zona | `Get3DBoundingBoxes` (API) | Registradas; ver §3 y `evidencias/` |
| 5 | Morphs y su intersección con el predio | censo + CSV | 71 morphs de contexto; sin masas del edificio |
| 6 | Cableado completo del canvas v13.5 | `scripts/utilities/dump-red-canvas.py` (**nuevo**) | La cadena F3→AC viva es **solo zonas** (#198→#242/#243); morphs F3 sin consumidores (#213 en desuso); contexto→#59 Morph Solid |
| 7 | Estado de sincronía canvas↔src | `comparar-canvas-src.py` | #198 **una revisión atrás** (falta fix (d): 80.082 vs 80.433 chars); #200 sincronizado |
| 8 | Cambio de patios en el lote actual | lectura de `F1_ETAPA2_PATIO_v03.py` + slider del canvas | Slider `n_volumenes`=**0 (AUTO)** → para AAA0030JKOE generaba **3 "patios" de esquina** (regla v1 retirada; ver D2) |
| 9 | Imágenes | registro en `evidencias/` | (a) captura del operador 2026-10-13 12:15 (ArchiCAD, 16 zonas seleccionadas); (b) captura 2026-10-11 22:32 (previsualización, 2 volúmenes superpuestos) + 2 recortes ampliados |

**Nuevas herramientas dejadas en el repositorio:** `F0_CENSO_ELEMENTOS_v01.py` (censo por tipo, `--sel --bbox=...`), `dump-red-canvas.py` (red de conexiones del canvas), `_tmp-zonas-propiedades.py` (lectura de propiedades de zonas).

---

## 2. Resultados — censo en vivo de ArchiCAD (2026-10-13)

### 2.1 Zonas (16) — todas BEP v08.1

| Zona (Number) | Nombre | Área m² | BBox X[..] / Y[..] / Z[base,top] |
|---|---|---|---|
| GF-Z1-COM-001 | Local comercial · Bloque 1 · Piso 1 | 106.32 | X[-42.08,-27.22] Y[25.60,41.61] Z[-11.46,-8.41] |
| L01-Z1-COM-001 | Local comercial · Bloque 1 · Piso 2 | 287.75 | X[-21.15,2.67] Y[5.69,29.45] Z[-8.41,-5.37] |
| L02-Z1-VIV-001 | Vivienda · Bloque 1 · Piso 3 | 287.75 | idem (apilada) |
| L03-Z1-VIV-001 | Vivienda · Bloque 1 · Piso 4 | 287.75 | idem |
| L04-Z1-VIV-001 | Vivienda · Bloque 1 · Piso 5 | 287.75 | idem Z[0.73,3.79] |
| GF-Z2-COM-001 | Local comercial · Bloque 2 · Piso 1 | 105.07 | X[-31.35,-16.60] Y[18.03,33.90] Z[-8.11,-5.06] |
| L01-Z2-COM-001 … L04-Z2-VIV-001 | Bloque 2 · Pisos 2–5 | 267.32 c/u | X[-27.34,-3.46] Y[10.14,31.01] Z[-5.06…7.14] |
| GF-Z3-COM-001 | Local comercial · Bloque 3 · Piso 1 | 153.67 | X[-20.63,-1.73] Y[10.45,31.75] Z[-5.18,-2.13] |
| L01-Z3-COM-001 … L04-Z3-VIV-001 | Bloque 3 · Pisos 2–5 | 340.59 c/u | X[-33.53,-5.17] Y[11.39,35.46] Z[-2.13…10.07] |
| GF-Z4-COM-001 | Local comercial · Bloque 4 · **Piso 1 (único)** | 152.42 | X[-9.90,8.89] Y[2.88,24.03] Z[-2.47,0.58] |

**Hallazgos:**
1. **Faltan 4 zonas**: Bloque 4, Pisos 2–5. La corrida declaró "4 bloques | 20 zonas"; en AC quedaron **16**. (El estado es un **re-push incompleto/parcial**, no un mock de dos fases.)
2. **Las plataformas P1 de cada bloque no están apiladas con sus pisos superiores** (p.ej., Bloque 1: P1 en X[-42,-27] pero P2–P5 en X[-21,+3]). El conjunto se lee visualmente como "masas" superpuestas/mezcladas — el efecto que reportó el operador.
3. **Stories insuficientes (3 vs 8)**: las zonas quedan en un rango de cotas que ArchiCAD no puede organizar por niveles; refuerza la lectura "mezclada" en vistas y tablas.
4. En la captura del operador (selección = las 16 zonas, vista "3D/Selection") se ven, en efecto: plataformas + cuerpos apilados superpuestos → "dos volúmenes masivos" (lectura de las masas P1 continuas) y "cuatro volúmenes separados" (los 4 bloques) convivendo.

### 2.2 Texto/lectura de la previsualización (capturas analizadas)
- **2026-10-11 22:32 (Rhino/preview):** dos volúmenes superpuestos (uno con aristas verdes = contorno escalonado; otro azul = retícula interior ortogonal) + masas grises alrededor (contexto). Coincide con la previsualización de las salidas del canvas.
- **2026-10-13 12:15 (ArchiCAD):** objeto central seleccionado con ~4 cuerpos apilados + retícula azul interna; misma estructura que el censo (zonas + huellas desplazadas).
- **2026-10-13 13:24 (tras reabrir el canvas):** la misma situación persiste (evidencia del operador) — esperado hasta aplicar F1 (parche canvas) + F2 (corrida limpia) → `evidencias/2026-10-13-1324-canvas-misma-situacion.png`.

---

## 3. Lectura técnica (causas probables, priorizadas)

| # | Causa | Evidencia | Acción (ver D3) |
|---|-------|-----------|-----------------|
| C1 | **Re-push parcial/incompleto hacia AC** (16/20 zonas; Bloque 4 a medias) | §2.1-1 | Corrida limpia + censo de verificación |
| C2 | **#198 del canvas una revisión atrás** (sin fix (d)); mezcla de revisiones en la corrida | comparar-canvas-src | Re-embebido #198 + regen `.gh` + recarga |
| C3 | **Stories insuficientes** (3 vs 8) | §2.1-3 | Crear stories (manual asistido) + `--check` |
| C4 | **Patios AUTO/MULTI** generando 3 "patios" de esquina y restándolos al envelope (regla v1 retirada) | D2 | Corregido en src (PATIO v03.4) + re-embebido pendiente |
| C5 | **Separaciones laterales / empate posterior** sin validar contra los bordes del lote | reporte del operador | Validación en corrida limpia; ajuste si aplica |
| C6 | Posible invasión sutil del contexto al predio (morph i=35 a revisar) | CSV de morphs | Revisión visual + limpieza de contexto si aplica |

**Descartes (lo que NO es):** no hay morphs del edificio (los 71 son contexto); no hay losas/muros (0); no hay "dos versiones de zonas" BEP distintas (todas son v08.1); el terreno es 1 mesh.

## 3b. Adenda (2026-10-13, tarde) — causa raíz del «solo el piso 1 en su nivel»

**Evidencia del operador (13:27):** en la previsualización de Rhino «solamente el primer nivel de los volúmenes de una crujía está en el nivel correspondiente».

**Causa raíz encontrada (y corregida):** en `F3_DISTRIBUCION_v03.py` (bloque de escalonamiento lateral, v03.8) el recorte por piso **mezclaba marcos**: usaba el polígono del lote en **marco local** con el rango **Y de la huella en marco canvas**. Resultado: el **piso 1** (huella base) quedaba correcto y los **pisos 2..n** salían **desplazados o vacíos** (con marco rotado, directamente vacíos) — justo el síntoma reportado, y fuente de la lectura de "volúmenes mezclados" en AC/preview.

**Fix v03.9 (aplicado en src, 2026-10-13):** el recorte usa el polígono de la **franja en marco local** (`cs[_k]`) con su banda Y local; respaldo con aviso si queda degenerado. Test de regresión nuevo con **marco rotado + traslación** (`test_v039_escalonamiento_marco_rotado_sin_desplazamiento`): **22/22** en el archivo; suite **367 ✅ / 7 ✗** (stale conocidos).
**Pendiente:** re-embebido de **#200 → v03.9** en el canvas (junto a #198 fix (d) y #78 PATIO v03.4) → recarga → corrida limpia (F2). Evidencia técnica: `evidencias/2026-10-13-fix-v039-marcos.txt`.

---

## 4. Condiciones y reproducibilidad

- Todas las lecturas se hicieron con el **API JSON de ArchiCAD (solo comandos `Get*`)** con el proyecto Test 07.pln abierto — sin modificar el documento.
- Comandos reproducibles (desde la raíz del proyecto):
  - `.venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --list`
  - `.venv\Scripts\python.exe src\interfases-archicad\F0_CENSO_ELEMENTOS_v01.py --sel --bbox=Morph,Slab,Zone`
  - `.venv\Scripts\python.exe scripts\utilities\_tmp-zonas-propiedades.py`
  - `.venv\Scripts\python.exe scripts\utilities\dump-red-canvas.py` (red completa) y `comparar-canvas-src.py`
- **Limitación:** el censo refleja el estado del .pln en el instante de la lectura (12:30–12:40 del 2026-10-13). Si el operador guarda/edita después, repetir el censo antes de la corrida limpia.

## 5. Archivos de evidencia

- `evidencias/2026-10-13-archicad-seleccion-16-zonas.png` — captura del operador (12:15).
- `evidencias/2026-10-11-previsualizacion-rhino.png` — captura del 2026-10-11 22:32.
- `evidencias/2026-10-13-crop-izq-2x.png` / `-crop-arriba-2x.png` — recortes ampliados de la captura 10-13.
- `evidencias/2026-10-13-censo-morphs-ac.csv` — bboxes de los 71 morphs (censo).
- `evidencias/2026-10-13-censo-ac-vivo.txt` — texto base del censo de zonas (16 filas) y conteos.
- `evidencias/2026-10-13-1324-canvas-misma-situacion.png` — captura del operador tras reabrir el canvas (13:24; misma situación).
- `evidencias/2026-10-13-storysync-salida.txt` — salidas de `F3_StorySync` (`--list`, `--check`, hoja del operador) del 2026-10-13.
