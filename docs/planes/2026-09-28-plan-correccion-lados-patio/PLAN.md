# Plan de corrección - "definición de lados" y patio (F1 · ETAPA2)

**Fecha:** 2026-09-28 · **Proyecto:** DiseñoParametrico · **Estado:** ✅ Ejecutado (fases 0-3) el 2026-09-28; pendiente verificación visual del operador y cierre (vault/backup/commit).

**Alcance revisado:** `src/fase-1-contexto/F1_ETAPA2_PATIO_v02.py`, `F1_ETAPA2_LADOS_v06.py`, canvas `gh-definitions/F1_CONTEXTO_v11.ghx` (código embebido), orquestador `src/orquestador/run_pipeline_v01.py`, y el flujo de datos real del chip activo **AAA0240ZXJH**.

---

## 0. Estado de ejecución (2026-09-28, tarde)

**Decisiones del operador (registradas):**
- **(a) Patio:** la forma no es crítica; garantías obligatorias: **área ≥ 9 m2** y **≥ 3 metros lineales** entre cada lado del predio y el borde opuesto del patio (claridad/profundidad desde cada lado).
- **(b) Lados:** simplificar colineales o con variación de ángulo **< 2.5°**; si el ángulo es **≥ 2.5°** el vértice se mantiene, sin importar el número final de lados.

**Ejecutado:**

| Fase | Estado | Entregable |
|---|---|---|
| F0 hotfix | ✅ | `point_in_lot` definida en LADOS **v06.5** (subversión); canvas v11 parcheado (backup `.ghx.bak-2026-09-28-1831`) y `.gh` regenerado (122.693 B); validado: código embebido **idéntico** a los fuentes del repo |
| F1 V_N/patio | ✅ | PATIO **v02.3**: dedup de puntos mejorados (≤0.30 m), uso solo si coincide con vértice del lote (±0.15 m), máximo **1** patio, motivos de descarte en el mensaje |
| F2 simplificación | ✅ | Regla 2.5° implementada en LADOS v06.5 **y** PATIO v02.3 (misma función, mismo input → índices consistentes). AAA0240ZXJH: **13→4 lados**, coincide con la agrupación del operador |
| F2 NORMATIVA | ✅ (chequeo) | NORMATIVA v08 consume lados genéricamente y los overrides `frente_override` van por *cardinal* → compatible con 4 lados |
| F3 orquestador | ✅ | 4 defectos corregidos (`shutil`, `post_comando` en rama de éxito, estado por **frescura de chip**, arranque en frío) + fetch unificado (`fetch-contexto-completo_v01.py --solo-base/--solo-50`) + estado del paso 50 m en el display |
| Tests | ✅ | +12 tests nuevos (conductuales con stub CPython: vías cruzadas, simplificación, garantías en esquina 60°, dedup, chip real) - **suite completa 286/286 en verde** |
| Extra higiene tests | ✅ | `tests/test_servidor.py` escribía/borraba el espejo real `data/activo/proyecto.json` en cada corrida; ahora todas las rutas de escritura se aíslan en `tmp_path` (monkeypatch). Archivo real restaurado desde git y verificado pos-suite |
| F4 cierre | ⏳ | Verificación visual del operador en canvas; diario/lección, backup y commit (los cambios están **sin commitear**) |

**Evidencia (anexos):** `harness_out_precorreccion.txt` (error original), `harness_out_postcorreccion.txt` (corrida post-fix: `LADOS v06.5 | Verts 13->4 | A=V1 N=V3 | ...`, `PATIO v02.3 | Patio 3.00x3.00 m (area 9.00 m2; claridad 3.00 m) | Generados: 1`), `verificacion_tests.txt`.

**Pendientes / notas:**
- **Verificación operador:** reabrir `F1_CONTEXTO_v11` en Rhino; mensajes esperados: LADOS v06.5 sin ERROR (Verts 13->4) y PATIO v02.3 con `Generados: 1`. Verificar también el chip del mensaje ETAPA1 (panel #2; `CHIP-contexto.json` estaba desactualizado).
- **T3.3** (export diagnóstico `<CHIP>-lados.json` para el orquestador): propuesta, no implementada.
- Con vías tipo *Eje_vial* (JSON) ningún lado queda "Frontal" por contacto (>0.5 m); en canvas con capas clasificadas de ArchiCAD (lotes de vía) sí. No afecta al patio del vértice N (lados colindantes).

---

## 1. Resumen ejecutivo

1. **Causa raíz principal (bloqueante):** `F1_ETAPA2_LADOS_v06.py` llama a `point_in_lot()` en la **línea 683** pero la función **no está definida en el archivo**. Cuando existe al menos un cruce vía-vía (lo normal con ≥2 vías), la ejecución lanza `NameError`, el `try/except` general la captura y **se aborta toda la clasificación de lados**: `sides_table_json` queda vacío; `F1_ETAPA2_PATIO_v02` recibe "sides=FALTA" y el patio no se genera. Eso es exactamente "la definición de lados no está trabajando".
2. **Reproducido offline** con los datos reales de `AAA0240ZXJH` (arlés de stubs en CPython, ver Anexo A): mensaje exacto `LADOS v06.2 | ERROR: name 'point_in_lot' is not defined`.
3. El defecto está **vivo en el canvas v11**: el `CodeInput` del componente LADOS es idéntico al del repo (solo difiere en 6 líneas del encabezado v06.4). Aplica la regla: *editar el `.py` no actualiza el canvas* → el hotfix requiere parchear `.ghx` + regenerar `.gh` (GH_IO).
4. Se identificaron además **5 hallazgos** (V_N mejorado inerte, fragmentación de lados con lotes multi-quiebre, duplicados latentes en el patio, 4 defectos en el orquestador, y desalineación de archivos "activos" del fetch) que conviene resolver en el mismo ciclo para dejar la cadena F1 estable.

---

## 2. Evidencia verificada (2026-09-28)

| Hecho | Evidencia |
|---|---|
| LADOS llama `point_in_lot` sin definirla | `F1_ETAPA2_LADOS_v06.py:683` (1 sola mención; los legacy `F1_PATIO_DISCONTINUIDAD_*` sí la definen; v04/v05 no la usan) |
| Error reproducido con datos reales | Arnés CPython + `AAA0240ZXJH-contexto.json` → `LADOS v06.2 \| ERROR: name 'point_in_lot' is not defined` (caso A0, Anexo A) |
| Canvas v11 embebe el mismo defecto | `F1_CONTEXTO_v11.ghx`: `point_in_lot` ×3 = 2 del PATIO (def + uso) + 1 del LADOS (uso); `def` solo 1 (PATIO) |
| LADOS del canvas DIFIERE solo en encabezado | diff ratio 0.9972, únicamente líneas del changelog v06.4 |
| El lote activo tiene 13 vértices y micro-segmentos | `AAA0240ZXJH-contexto.json` → `lote_objetivo.vertices_3d_local` (14 pts, cierre dup.; segmentos de 0.06-0.07 m; área 99.7 m2) |
| Con la función inyectada, la cadena completa | LADOS clasifica (13 "Lateral") y PATIO genera 1 patio 3.00×3.00 m = 9.0 m2 dentro del lote (caso A, Anexo A) |
| `vertice_n_points` quedó **vacío** (0 pts) | Se activa el *fallback* tradicional: V_N = vértice más lejano por distancia; `vertice_n_method = None`. El mecanismo v02.2 quedó inerte para este lote |
| Orquestador: 4 defectos | ver H5 |
| Archivo activo base desactualizado | `data/pot-cache/CHIP-contexto.json` contiene **AAA0127AZPA** (mtime 2026-08-10). El panel #2 del canvas apunta a ese archivo; verificar qué leyó ETAPA1 en la última corrida |

---

## 3. Hallazgos detallados

### H1 - CRÍTICO · `point_in_lot` no definida en LADOS v06 (bloquea lados + patio)

- **Qué pasa:** el bloque "Calcular Vertice A como intersección de vías" (nuevo en v06, reparado el 2026-09-01 en v06.3) pasó de ser una *rama muerta* a ejecutarse de verdad. Al activarse, quedó expuesto que `point_in_lot(pt, lot_vertices)` (línea 683) **nunca fue copiada del patio legacy**.
- **Disparador:** cualquier par de vías con intersección (calles que se cruzan). Con 2+ vías que se cruzan → `intersections` no vacío → `NameError` → toda la clasificación se aborta.
- **Por qué "a veces funciona":** antes del fix del 2026-09-01 el filtro `IntersectionType == Point` era rama muerta → nunca se llegaba a la línea 683. En corridas con vías que no se cruzan tampoco se dispara. Por eso el fallo es intermitente y apareció ahora.
- **Efecto en producción:** `sides_table_json = ""` → PATIO → "ERROR: sides=FALTA" → sin patio, sin aislamientos por lado (NORMATIVA), sin diagnóstico útil.

**Fix propuesto (hotfix):** añadir la función al inicio del script (misma semántica que el legacy/PATIO: ray casting + tolerancia de borde 0.1 m), p. ej. copiada de `F1_ETAPA2_PATIO_v02.py`. Solo cambia el script (subversión v06.5) sin tocar el contrato de entradas/salidas. Después: parche idempotente del `.ghx` + regenerar `.gh` con GH_IO (flujo ya establecido en `scripts/utilities/patch-ghx-*.py`).

**Test de regresión (nuevo):** caso "2 vías que se cruzan" → mensaje sin `ERROR`, `sides_table_json` no vacío y sin excepción. Integrar el arnés del Anexo A como `tests/test_lados_patio_conductual.py` (skip si no hay fixtures).

### H2 - Vertice N mejorado (v02.2) inerte en el lote real; anclaje del patio no garantizado por construcción

- `vertice_n_points` = **0 puntos** para `AAA0240ZXJH`: la condición "coincidencia <0.10 m con vértices de vecinos" no se cumple en la esquina lejana (los vértices de los vecinos están a otras distancias sobre la calle).
- Se cae al *fallback* tradicional `idx_n = argmax(dist_vertices)` → V_N = vértice más lejano **por distancia** (en esta corrida V7, que casualmente coincide con la esquina deseada). No hay garantía de que el anclaje sea la "esquina interior" entre los dos lados colindantes.
- Riesgo colateral: si V_N cae del lado de una vía (frente/sur), el gate de patio (`Lateral`/`Posterior` en ambos lados adyacentes) puede fallar sin explicación clara.

**Acciones:** (a) anclar por construcción: exigir que los dos lados adyacentes sean colindantes (sin vía/EP) y, si el punto mejorado no existe, elegir la unión de los lados colindantes dominantes (con ayuda de `vecinos_por_lado`/fracciones de contacto); (b) ampliar tolerancia de coincidencia o evaluar coincidencia con *vérties de la manzana*; (c) mensaje diagnóstica del porqué cuando no haya esquina válida.

### H3 - Fragmentación de lados con lotes multi-quiebre (13 lados vs 4 lógicos)

- El lote de `AAA0240ZXJH` tiene 13 vértices; los archivos de trabajo del operador (`AAA0240ZXJH-vecinos-por-lado*.json`) lo agrupan en **4 lados lógicos**: `[0]`, `[1,2]`, `[3..6]`, `[7..12]` (2 predios colindantes en el norte).
- LADOS v06 clasifica 13 lados; micro-segmentos de 6 cm aparecen como lados independientes ("sin contacto mínimo" / "vértices coincidentes"). El patio se ancla usando índices adyacentes concretos (p. ej. L6/L7), sin noción de "lado lógico".
- Además, con las vías tipo *Eje_vial* (líneas de eje) ninguna quedó "Frontal" (distancias 5.8-13.5 m ≫ tolerancia 0.5 m): en canvas real las vías vienen de capas clasificadas (lotes de vía), pero refuerza la necesidad de robustez.

**Decisión pendiente (con el operador):**
- **(a)** simplificar el lote a esquinas lógicas (4 lados) antes de LADOS/PATIO (reusar el agrupamiento de `vecinos_por_lado.py`), o
- **(b)** hacer LADOS/PATIO robustos a N lados (colapsar micro-segmentos ≤0.3 m como alias del lado vecino, agregar "lado lógico" al JSON).
Recomendación técnica: **(a)** alinea con la semántica del pipeline ("lote simplificado") y con los archivos del operador; (b) como refuerzo adicional.

### H4 - Patio v02.2: duplicados latentes y contrato desalineado

- `vertice_n_points` sin deduplicar: muestreo cada 0.1 m puede producir varios puntos válidos en la misma esquina → **un patio por punto** → solapes duplicados. (No se disparó aquí porque la lista quedó vacía; queda latente.)
- Encabezado dice `patio_count (0 o 1)`, pero v02.2 puede generar N. Alinear contrato (deduplicar por clustering ≤0.25 m, o documentar N y ajustar consumidores).
- Regla geométrica: el "cuadrado" se construye sobre las **normales** de los dos lados → en esquinas no perpendiculares es un paralelogramo (área ≠ lado2). Decidir y documentar (paralelogramo vs rectángulo inscrito).

### H5 - Orquestador `run_pipeline_v01.py`: 4 defectos (verificados)

1. **`shutil` no importado** (líneas 40-46) pero `_copy_file` usa `shutil.copy2` (línea 104) → la copia falla en silencio (lint atrapado por try/except).
2. **Bloque `post_comando` mal ubicado** (líneas 461-466): quedó dentro del `else` de fallo y protegido por `if ok and ...` (ok=False ahí) → **nunca ejecuta** → `contexto-actual.json` / `contexto50-actual.json` jamás se refrescan desde `<CHIP>-*.json`. Mover a la rama de éxito (tras línea 449).
3. **Init de archivos en blanco antes de detectar estado** (líneas 388-413): en arranque frío marca los pasos como "hecho" y los salta (requiere `--refresh` para forzar). Inicializar en blanco **después** de `detectar_estado`, o no contarla como "hecho" si el chip del archivo no corresponde (usar `_validar_contexto_fresco`, hoy definida pero sin uso).
4. **No hay paso/verificación de la etapa canvas ETAPA2** (LADOS/PATIO/NORMATIVA): la "definición de lados" no deja artefacto verificable. Propuesta: que el canvas exporte un diagnóstico (`<CHIP>-lados.json` + `patio` en el JSON) y el orquestador lo liste/verifique.

**Además (alineación):**
- Conviven dos orquestadores: el nuevo `scripts/utilities/fetch-contexto-completo_v01.py` (crea solo el canónico `contexto50-actual.json`) y `run_pipeline_v01.py` (espera `contexto-actual.json`, que **no existe** en `data/pot-cache/`). Definir convención única:
  - Base: `<CHIP>-contexto.json` (chip) + **crear/actualizar el activo literal que el canvas consume** (hoy el panel apunta a `CHIP-contexto.json`, actualmente con contenido viejo de AAA0127AZPA).
  - 50 m: `contexto50-actual.json` (ya funciona).
- Verificar en el próximo arranque del canvas el **mensaje de ETAPA1** (muestra chip y `json_path`): debe decir `AAA0240ZXJH`.
- ETAPA1 no tiene resolución defensiva de plantilla (ETAPA3 v01.1 sí, vía `contexto50-actual.json`).

### H6 - Drift menor (encabezados/versiones)

- Canvas LADOS sin las 6 líneas del changelog v06.4 del repo (solo encabezado; sin efecto funcional).
- Al aplicar fixes: subir subversiones (`LADOS v06.5`, `PATIO v02.3`) y actualizar encabezados ENTRADAS/SALIDAS/cambios (regla del proyecto #25).

---

## 4. Plan de trabajo

> Orden recomendado. Fase 0 desbloquea todo lo demás; Fase 1-2 consolidan la semántica; Fase 3 deja el pipeline verificable; Fase 4 cierra según procedimiento.

### Fase 0 - Hotfix bloqueante (≈1 h)

| # | Tarea | Archivos | Criterio de done |
|---|---|---|---|
| T0.1 | Añadir `point_in_lot` a LADOS v06 (copiada del patio legacy, misma semántica) | `src/fase-1-contexto/F1_ETAPA2_LADOS_v06.py` | Script ejecuta; mensaje sin `ERROR` con ≥2 vías cruzadas |
| T0.2 | Parchear canvas: `.ghx` (idempotente + backup) y regenerar `.gh` con GH_IO | `gh-definitions/F1_CONTEXTO_v11.ghx/.gh` + script en `scripts/utilities/` | Canvas embebe v06.5; reabrir en GH: mensaje LADOS sin ERROR |
| T0.3 | Test de regresión "vías cruzadas" + integrar arnés conductual (Anexo A) | `tests/test_lados_patio_conductual.py` (nuevo), `tests/` | Test rojo→verde con la corrección; corre en CI local (`pytest`) |
| T0.4 | Correr suite completa | - | Verde (base actual: "261 tests") |

**Nota:** antes de tocar, backup según flujo estándar (`AgentKit/04-backup`) y verificación visual del operador en canvas (mensajes ETAPA1/LADOS/PATIO).

### Fase 1 - Robustez del Vertice N y del patio (≈2-4 h)

| # | Tarea | Criterio |
|---|---|---|
| T1.1 | Deduplicar `vertice_n_points` (clustering ≤0.25 m) y limitar a 1 patio por esquina; alinear docstring/contrato | Sin patios duplicados en clustering de prueba |
| T1.2 | Anclaje por construcción: verificar adyacencia colindante (sin vía/EP) y preferir la unión de lados colindantes; usar `vertice_n_points` solo si coincide con vértice del lote (±0.15 m) | Patio en la esquina interior correcta en 4 lotes de prueba (incl. AAA0240ZXJH) |
| T1.3 | Decisión + documentación de la forma en esquinas no perpendiculares | Nota de decisión en encabezado + caso de prueba |
| T1.4 | Mensajes diagnósticos cuando NO se genere patio (motivo: sin V_N válido / lados no colindantes / fuera de lote) | Mensaje claro en los 3 escenarios |

### Fase 2 - Lote multi-quiebre: simplificado vs robusto (decisión + impl., ≈3-6 h)

| # | Tarea | Criterio |
|---|---|---|
| T2.1 | Reunión corta de decisión con evidencia (esta nota): (a) simplificar a 4 lados lógicos, o (b) robustez N-lados | Decisión registrada |
| T2.2 | Si (a): agrupar segmentos por dirección dominante (reusar enfoque `vecinos_por_lado.py`) antes de LADOS; verificar en 4 chips | 4 lados estables; mensajes legibles |
| T2.3 | Si (b): colapsar micro-segmentos ≤0.3 m como alias del vecino; etiqueta de "lado lógico" | Sin lados de 6 cm en el JSON |
| T2.4 | Revisar consumo de N lados en NORMATIVA v08 (retiros por lado) | NORMATIVA estable con 4 y con N lados |

### Fase 3 - Orquestador (≈1-2 h)

| # | Tarea | Criterio |
|---|---|---|
| T3.1 | Corregir H5.1-H5.3 (`import shutil`; mover `post_comando` a la rama de éxito; init en blanco después de detectar / usar `_validar_contexto_fresco`) | `--run` refresca canónicos; arranque frío NO salta fetch |
| T3.2 | Unificar con `fetch-contexto-completo_v01.py`; crear/refrescar también el activo base que consume el canvas | Un solo comando de contexto; archivos activos al día |
| T3.3 | Paso F1.5 "Canvas ETAPA2": export de diagnóstico (`<CHIP>-lados.json` propuesto: clasificaciones + patio) y chequeo en el orquestador | `--status` muestra estado de lados/patio; detecta `sides_table_json` vacío |
| T3.4 | Tests `test_orquestador.py` (post_comando, canónicos, refresh, chip en archivo) | Verde |

### Fase 4 - Cierre (≈1 h)

- Subversiones y encabezados actualizados (LADOS v06.5 / PATIO v02.3 / nota canvas).
- Suite completa + nuevo arnés en verde; verificación visual del operador en canvas (AAA0240ZXJH y otro chip de control).
- Documento de sesión + lección en vault; backup `backup_projects.ps1 -Real` y commit (procedimiento de cierre).

---

## 5. Criterios de aceptación globales

1. **Canvas (chip AAA0240ZXJH):** mensaje LADOS sin `ERROR`; clasificación de lados visible; PATIO genera **1 patio 3×3 m (9 m2)** en la esquina interior de los lados colindantes (Norte/Occidente para este lote según archivos del operador); mensajes claros si no aplica.
2. **Regresión:** suite completa verde + nuevos tests (vías cruzadas, dedup, esquina, orquestador).
3. **Orquestador:** `--status`/`--run` refrescan los canónicos y los archivos activos del canvas; arranque en frío consistente; sin pasos saltados.
4. **Trazabilidad:** artefacto diagnóstico de lados/patio verificable por el orquestador.

---

## 6. Anexos

### A. Reproducción offline (arnés CPython, sin Rhino)

Archivos (copia en `anexos/`):
- `anexos/stub_rg.py` - stub mínimo de `Rhino.Geometry` para polilíneas (Point3d, Vector3d, Polyline, PolylineCurve, Line, intersecciones).
- `anexos/run_harness.py` - ejecuta LADOS v06 + PATIO v02 con `data/pot-cache/AAA0240ZXJH-contexto.json` (casos A0/A/B/C).
- `anexos/harness_out_precorreccion.txt` - salida **antes** de la corrección (reproduce el `NameError`).
- `anexos/harness_out_postcorreccion.txt` - salida **después** de la corrección (v06.5 / v02.3).
- `anexos/verificacion_tests.txt` - captura de los tests focales (32).
- Tests de producción añadidos: `tests/test_lados_patio_conductual.py` + `tests/stub_rhino_min.py`.

### B. Referencias internas

- Cambio que activó la rama: commit `cdc03688` (2026-09-01, "enum Intersection desde rg.Intersect... rama muerta silenciosa").
- Regla canvas: *editar un `.py` NO actualiza el canvas*; parchear `.ghx` + GH_IO (§ memoria del proyecto).
- Archivos del operador usados como referencia de "4 lados lógicos": `data/pot-cache/AAA0240ZXJH-vecinos-por-lado.json` y `...-override.json`.
- Código embebido del canvas verificado hoy: `F1_CONTEXTO_v11.ghx` (mtime 13:53), LADOS 47081 chars (diff 0.9972 vs repo), PATIO 12595 chars (idéntico).

---

*Nota: este documento es una propuesta de trabajo. La fase 0 es autónoma y recomendable de inmediato; las fases 1-2 requieren una decisión breve del operador (forma del patio y estrategia de simplificación).*

---

## 7. Segunda pasada (2026-09-28, tarde-noche): front-end unificado, Init-DP y export F1.5

**Solicitud:** un solo archivo que sirva el front-end (127.0.0.1:8900) y ejecute allí todo el pipeline; lanzador `Init-DP` en `D:\Work\Scripts`; ejecutar el paso opcional (diagnóstico lados/patio). Restricción vigente: la validación en canvas queda bloqueada mientras AutoClaw esté abierto (puerto 19723).

**Implementado:**

| Entregable | Detalle |
|---|---|
| `src/orquestador/orquestador_v01.py` | **Archivo único de entrada**: sirve el front-end (reutiliza `servidor.py`) y ejecuta el pipeline completo A TRAVÉS del front-end por HTTP (`--run`, `--status`, `--checklist`, `--stop`, `--abrir`). Auto-arranca el servidor si falta. |
| `servidor.py` ampliado | Pipeline completo: activar chip/caso → F1 base → F1 50 m → F2 venta (+ renta según modo) → F3 → **F1.5 lados/patio**; endpoints nuevos `GET /api/estado` y `POST /api/exportar-lados`; guardas de error (no reportar OK si la salida trae Traceback / “Sin escenario de uso mixto”). |
| `index.html` | Botón “Exportar diagnóstico lados+patio (canvas)” + línea F1.5 en el resultado del pipeline. |
| `D:\Work\Scripts\Init-DP.ps1` + `Init-DP.cmd` | Lanzador: se ubica en el proyecto, arranca orquestador+front-end, abre navegador; soporta `-Status`, `-Pipeline -Chip -Caso -Modo`, `-Stop`. |
| `F1_ETAPA2_PATIO_v02.py` v02.4 | Export del diagnóstico: con flag `lados-export-flag.json {exportar:true}` escribe `data/pot-cache/<CHIP>-lados.json` y resetea el flag (patrón GFA). Canvas v11 parcheado + `.gh` regenerado (123.903 B). |
| `run_pipeline_v01.py` | `estado_lados_patio(chip)` (verificación F1.5); frescura del contexto alineada a los activos reales del canvas (`CHIP-contexto.json` / `<CHIP>-contexto.json`); post_comando refresca el activo base. |

**Evidencia (anexo `demo_f1_5_pipeline_web.txt`):** flag → PATIO v02.4 → `<CHIP>-lados.json` (área 9.0004 m², claridad 3.0 m) → `/api/estado` `ok:true` con 6/6 checks; pipeline completo vía front-end con pasos OK (F3 chip-mode queda pendiente por el escenario D_MIXTO del chip nuevo — ver abajo). Suite: **288/288**.

**Hallazgos nuevos de esta pasada:**
1. **F3 chip-mode y D_MIXTO:** para `AAA0240ZXJH` el motor F2 produce A/B/C; F3 requiere un escenario `D_MIXTO*`. Los casos A/B/C usan archivos dedicados (`resultados_AAA0127AZPA_gfa1461_cl800.json`, etc.). Para el chip nuevo: generar su mixto (equivalente a `generar_caso_f3_gfa1461.py`) o usar modo caso. Guarda de error corregida.
2. **Componente “#113” del canvas v11:** apodado `#113-F1_ETAPA1_CONTEXTO_v04.py` pero con **parámetros de familia NORMATIVA** (recibe `sides_table_json`, `patio_curves`; emite `envelope_curve`, `gfa_total`…) y **código embebido de ETAPA1 v04** → en su estado actual no puede calcular envelope/GFA (salidas nulas). Se requiere decisión/limpieza al validar el canvas (¿slot NORMATIVA en construcción? ¿duplicado obsoleto?).
3. `data/activo/proyecto.json`, `CHIP-contexto.json`, `CHIP-vecinos-por-lado.json` quedaron apuntando a `AAA0240ZXJH` (activación del flujo web). `data/pot-bogota/norma-override.json` ganó un bloque `AAA0127AZPA` a las 18:55 (¿guardado desde la UI? — verificar si no lo hizo el operador).

**Pendientes:** validación en canvas (bloqueada por 19723/AutoClaw); D_MIXTO del chip nuevo (o uso en modo caso); reconstruir `.venv` (hoy roto para numpy/geopandas: 432 binarios cp312 sobre 3.11 — mitigado con selector de intérprete); cierre (vault/backup/commit).

**Ajustes post-prueba del operador (2026-09-28, Prado 18:58):** (1) geobase portable + `--gpkg` explícito + env vars restablecidas → `f1_contexto50` OK; (2) selector de intérprete en servidor/run_pipeline/Init-DP (F2/F3 no dependen de numpy; el fetch sí); (3) diagnóstico F1.5 generado para `AAA0127AZPA` (lados=4, patio 9.0 m² / claridad 3.0 m); (4) F3: resumen chip→caso y fallo claro de D_MIXTO (ya no “OK” vacío). Evidencia: `anexos/fixes_pipeline_2026-09-28_noche.txt`.

**Front-end (pedido 19:15, ejecutado):** (5) altura de vecinos **bloqueada** en lados `vía (no frontal)` / `espacio público` (inputs deshabilitados y limpiados, marca en la fila, etiqueta “(sin altura)” en el plano + leyenda, y limpieza al guardar en servidor); (6) campo **“CHIP nuevo”** en la sección 1 como disparador de un proceso nuevo (fetch base + 50 m + activación + refresco completo; endpoint `/api/nuevo-chip` con validación de formato). Evidencia: `anexos/front-ui-2026-09-28.txt`.

**F3 / D_MIXTO (19:29, ejecutado):** `buscar_resultados` en F3 ahora prioriza el dataset del chip que **contiene** escenario mixto (`mix_usos_detalle`); para El Prado usa `resultados_AAA0127AZPA_gfa1461_cl800.json` (caso A) y genera `casos/AAA0127AZPA/` completo (incl. `F3_AAA0127AZPA.3dm` — rhino3dm instalado en el intérprete del pipeline; F2/F3 también usan el selector de intérprete). Verificado por el mismo camino del botón (`/api/generar-f3` → ok). Evidencia: `anexos/f3-dmixto-fix-2026-09-28.txt`. Pendiente/opcional: dataset mixto nuevo a la escala actual (GFA 1265.39) y mix para AAA0240ZXJH.
