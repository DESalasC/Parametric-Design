# Diagnóstico y plan — Prueba viva del canvas (Grasshopper ↔ ArchiCAD), chip B `AAA0030JKOE`

- **Fecha del diagnóstico:** 2026-09-28 (noche, post-prueba viva)
- **Ámbito:** errores aparecidos al ejecutar la prueba en vivo del canvas `F1_CONTEXTO_v11` con el chip B (La Candelaria), realizada con AutoClaw cerrado por el conflicto del puerto de la Live Connection (documentado: **19723**).
- **Estado:** ✅ Ejecutado en la noche del 2026-09-28 (P0, P1-offline y P2); validación viva del canvas pendiente (requiere cerrar AutoClaw — puerto 19723). Ver [EJECUCION-Y-RUNBOOK.md](EJECUCION-Y-RUNBOOK.md).
- **Fuente:** última entrada del vault (diario 2026-09-28) + reproducción local + inspección de código y artefactos del 28/09 22:32–22:56.

---

## 0. Resumen ejecutivo

La prueba viva expuso **4 errores visibles** y **2 causas de fondo**:

| # | Error observado | Causa raíz (verificada) |
|---|---|---|
| 1 | Front-end F2: `KeyError: 'eficiencia_nga'` (L244, GFA 1845,35 m²) | Escenarios **`D_MIXTO*` vacíos** (`{}`) en `parametros_AAA0030JKOE_mercado2026.json`, inyectados por la proyección del override financiero; el motor v03 no tolera escenarios vacíos. **Reproducido** con B y con El Prado. |
| 2 | Pipeline: `f3_distribucion` ✗ y `f1_lados_patio (canvas)` ✗ | F3 = **cascada** ("omitido: F2 fallo"); F1.5 = **no existe `AAA0030JKOE-lados.json`**: el flag de exportación quedó **sin consumir** por el canvas (no se completó el export). |
| 3 | Canvas: `Invalid Curve value. It must be in a horizontal plane.` al generar la polilínea del lote | El lote es **inclinado** (fetch v7: z por vértice, Δ16,12 m) y el canvas emite **curvas 3D**; los nodos de la Live Connection exigen curvas **cerradas y en plano horizontal** (2D Polyline / Mesh). |
| 4 | Vecinos todos a **z=0.0**; no se ve la **malla del terreno** | Vecinos: el builder extrude **desde z=0** (pendiente P2 ya registrado: cota por edificio). Malla: depende del tramo de exportación (falla 3) y de sus toggles. |

**Causas de fondo:**
- **GFA obsoleto:** F2 corrió con `AAA0030JKOE-gfa-gh.json` de **ago-22** (1845,35 m² / **7 pisos**) porque el componente `#113` del canvas tiene **contrato de NORMATIVA pero código de ETAPA1** → `valido=False` → `F1_EXPORTAR_GFA_v02` nunca escribió (el flag sigue en `true`). Pendiente ya registrado ("#113: decidir NORMATIVA en construcción vs duplicado").
- **Numeración `#NN` volátil:** el componente "Escáner y Etiquetador" **renombra los componentes** (`#1..#N` por posición); los parches por número dejan de calzar (p. ej. el patch de contexto50 apuntaba a `#49` y el canvas quedó en `#48`). Los parches deben anclarse por **GUID/nombre de archivo**.

**Quick win P0:** blindar el motor F2 (ignorar escenarios vacíos) + no proyectar vacíos desde el servidor + tests + re-corrida del pipeline.

---

## 1. Cronología y evidencia de la prueba viva (2026-09-28)

| Hora | Artefacto / acción |
|---|---|
| 22:32:49 | `data/lotes-ejemplo/Test 07.pln` — archivo ArchiCAD tocado en la prueba |
| 22:42:03 | "Guardar financiero" B → `parametros_AAA0030JKOE_mercado2026.json` + `financiero-override.json` (ultima_edicion 22:42) |
| 22:42:36 | `gfa-export-flag.json` → `{"exportar": true}` |
| 22:42:38 | `lados-export-flag.json` → `{exportar: true, chip: AAA0030JKOE, origen_solicitud: servidor}` |
| 22:42:58 | F3 regenera `casos/AAA0030JKOE/*` (programa, accesos, planos, `.3dm`) — corrida D_MIXTO de agosto |
| 22:43:01 | Archivos activos (`CHIP-vecinos-por-lado.json`, `f2_entrada.json`, `proyecto.json`) + arranque F2 (falla) |
| 22:51:23 | `src/interfases-archicad/F1_Layers_Proyecto_v01.xml` (9 capas) — export de capas del canvas |
| 22:51:30–42 | Canvas guardado: `gh-definitions/F1_CONTEXTO_v11.ghx/.gh` |
| 22:56 | Commit `c6657b54` "backup diario 2026-09-28" (incluye el canvas; repo limpio) |

**Notas de estado:**
- Los dos flags quedaron **en `true`** ⇒ ninguna de las dos exportaciones (GFA y lados/patio) se completó. Solo ocurre eso cuando el export nunca corre (el patrón de ambos componentes devuelve el flag a `false` al terminar bien).
- `data/pot-cache/AAA0030JKOE-lados.json` **no existe** (sí existen los de `AAA0127AZPA` y `AAA0240ZXJH`, de la revisión de cierre).
- `DISENO_PARAMETRICO_ROOT` (User) = `D:\Work\PROJECTS\DiseñoParametrico` ✓ definida (no fue la causa del no-export; el canvas requiere recomputar con el flag puesto).

---

## 2. Temas (diagnóstico)

### T1 — F2 `KeyError: 'eficiencia_nga'` (front-end)

**Síntoma.** Al correr el paso F2 del pipeline para el chip B: `[INFO] GFA desde Grasshopper F1 (…AAA0030JKOE-gfa-gh.json): 1845.35 m2` y traza con `KeyError: 'eficiencia_nga'` en `F2_DEMANDA_MOTOR_v03.py` L244 (`nga = gfa * esc["eficiencia_nga"]`), invocado desde L1426 (`main`).

**Causa raíz (verificada).** El archivo de parámetros `src/fase-2-demanda/F2_Modelo_Financiero/parametros_AAA0030JKOE_mercado2026.json` contiene:
```
"D_MIXTO": {}, "D_MIXTO_SALUD": {}, "D_MIXTO_OFICINAS": {}
```
Son **placeholders vacíos** (sin `mix_usos` ni `eficiencia_nga`). `run_scenario` toma la rama simple (`esc.get("mix_usos")` falso) → `esc["eficiencia_nga"]` → `KeyError`.

**Origen de los vacíos.** La proyección del override financiero (`servidor.py / _financiero_override_guardar`) recorre `escenarios` del override y hace `base["escenarios"].setdefault(eid, {})`, sin descartar los escenarios sin datos; el override de B (guardado 22:42 desde el front-end) traía `precio_venta_m2: null, costo_construccion_m2: null` para esos tres. El motor los escribe tal cual.

**Reproducción (realizada).**
- Chip B → `KeyError` idéntico (exit 1).
- Chip El Prado con `parametros_AAA0127AZPA_mercado2026.json` → **mismo `KeyError`** (su archivo también tiene `D_MIXTO: {}`). El Prado no falló en la noche porque el servidor **prioriza** `data/fase-2-demanda/mercado/parametros_AAA0127AZPA_f2mercado_2026-09.json` (sin placeholders); B no tiene archivo `f2mercado`.

**Actividades propuestas (fix en 3 capas):**
1. **Motor** → `F2_DEMANDA_MOTOR_v03.1` (subversión interna del mismo archivo): filtrar escenarios sin `eficiencia_nga` ni `mix_usos` antes de `run_scenario`/sensibilidad/alertas; dejar constancia en el informe ("escenarios ignorados: …"); tests nuevos (escenario vacío; mix normal intacto; suite vigente).
2. **Servidor** → `_financiero_override_guardar`: no proyectar escenarios vacíos/solo-nulos (skip); opcional: sanear el archivo generado.
3. **Datos** → cuando el operador defina el contenido real de `D_MIXTO*` de B (mix general / salud / oficinas), volver a guardar el financiero; mientras tanto, el motor los ignora con aviso.

- **Condiciones:** no cambia KPIs de A/B/C; no altera esquema de sensibilidad.
- **Límites:** el UI seguirá mostrando las filas `D_MIXTO*`; el fix no inventa datos.
- **Resultado esperado:** `python F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0030JKOE_mercado2026.json --chip AAA0030JKOE --pago-parcial 30` → exit 0; informe con A/B/C; pipeline `f2_venta` ✓.

### T2 — Pipeline: `f3_distribucion` ✗ y `f1_lados_patio (canvas)` ✗

**f3_distribucion ✗ = cascada.** `servidor.py / _pipeline`: si F2 falla → `"omitido: F2 fallo"`. No es un defecto propio de F3: la corrida standalone de F3 **sí funciona** para B (evidencia: `casos/AAA0030JKOE/programa.json` 22:42:58; usa `resultados_AAA0030JKOE.json` → escenario `D_MIXTO` "Local comercial turístico 30% + Vivienda 70%", GFA 3.312,575). Tras T1, el pipeline lo correrá; queda decidir la **"corrida vigente"** del caso B (dataset con mix a escala actual + variante SALUD — pendiente de la sesión anterior).

**f1_lados_patio ✗ = sin diagnóstico exportado.** `_verificar_lados → estado_lados_patio(chip)`: exige `data/pot-cache/AAA0030JKOE-lados.json` con checks: chip, `lados>=3`, `patio>=1`, `area>=9 m²`, `claridad>=3 m`, sin `ERROR` en mensajes. No existe porque el canvas no completó el export (flag sin consumir, ver §1).

**Causas probables a verificar en la re-prueba (P1):**
- la corrida del canvas tenía errores en ramas de geometría (T3) que pudieron impedir el cómputo/export del tramo LADOS/PATIO;
- la exportación depende de **recomputar** el canvas con el flag en `true` (y el botón/toggle correspondiente activo).
- `DISENO_PARAMETRICO_ROOT` ya está definida (descartada como causa).

**Propuestas:** tras T3, recomputar canvas → verificar export + `/api/estado` 6/6; mejora `PATIO v02.5`: mensajes explícitos cuando no exporta (sin flag / sin raíz / excepción) y verificación de que el chip del canvas coincide con el del flag.

### T3 — Canvas: `Invalid Curve value. It must be in a horizontal plane.`

**Mecanismo (verificado a nivel de código + documentación LC).**
- El contexto B trae `lote_objetivo.vertices_3d_local` (z por vértice) y `topografia.malla_terreno` (118 puntos; z_local de relieve; Δ16,12 m; La Candelaria en pendiente).
- El componente `#21 F1_ETAPA1_CONTEXTO_v04.1` construye las curvas **en 3D** (`polyline_from_coords` conserva `c[2]`) y las convierte a NURBS para la Live Connection.
- Los nodos LC involucrados exigen: **2D Polyline** = "Create a planar curve in an Archicad document"; **Mesh (terreno)** = "3D points and a closed planar 2D curve for boundary", con validación adicional (foro McNeel): *"…It must be in a horizontal plane and closed"*.
- Con z variable (lote inclinado), la curva no es horizontal ⇒ el nodo rechaza: `1. Invalid Curve value. It must be in a horizontal plane.`

**Estrategia:** separar **3D (Rhino/uso general)** de **2D horizontal (Live Connection)**:
- En `#21` (y `#113` tras T5) emitir **copias aplanadas** (`*_h`, z constante = ancla/z_base) para los inputs de los nodos LC; conservar las 3D para lo demás.
- Para la malla del terreno: boundary **cerrado y horizontal** (contorno proyectado) + puntos 3D por separado (requisito del nodo Mesh/terreno).
- Validar cierre (`IsClosed`) y horizontalidad antes de emitir.

- **Condiciones:** es solo presentación/dibujo; no altera cálculos (normativa/GFA usan datos 2D del JSON).
- **Límites:** la LC no admite plano inclinado para esos inputs; el relieve se representa con el Mesh (puntos 3D), no con la boundary.
- **Resultado esperado:** al recomputar, sin mensajes de error en esas ramas; polilíneas dibujadas en ArchiCAD; malla creada.

### T4 — Vecinos a z=0.0 y malla del terreno no visible

**Vecinos (confirmado).** `F1_CONTEXTO50_BUILD_v01b/v01c` documenta y ejecuta la extrusión **desde Z=0** (`Extrusion.Create(crv, h, True)`), y `contexto50-actual.json` **no trae cota base por edificio** (90 registros con `pisos`/`altura_m`, sin `z_base`). Está registrado como encargo **P2** ("cota por edificio (z_base_m vía MDT) + z_base de extrusión en ETAPA3/BUILD"). En lote inclinado el efecto es notorio (todo al 0.0, incluidos los Morphs que se envían a ArchiCAD).

**Malla del terreno.** `#21` la construye bien desde `topografia.malla_terreno` (IDW, grilla 5 m); que no se vea se atribuye al tramo de exportación (T3) y/o a los toggles `bake`/`exportar` del canvas. A verificar en la re-prueba; si aplica, explicitar el boundary horizontal del Mesh (T3).

**Propuestas:**
1. `z_base_m` por edificio: muestrear el MDT v7 en centroide/huella; añadir a `<CHIP>-contexto50.json` y `contexto50-actual.json` (y paridad `F1_ETAPA3_CONTEXTO50` v01.3).
2. `F1_CONTEXTO50_BUILD` v01d: levantar huella a `z_base_m` y extruir desde ahí; opción de anclar al "Level" LC para Morphs; mensaje con rango de cotas.
3. Tests: terreno plano (z_base=0 → comportamiento actual), edificio en pendiente, exclusiones intactas (lote objetivo / construcciones <15 m²).
4. Malla: verificación visual (Rhino + ArchiCAD) y de toggles.

- **Límites:** MDT puntual es estimado (documentar tolerancia ±0,5 m; permitir override manual por edificio).

### T5 — `#113` (envelope/GFA sin fuente) y GFA obsoleto

**Hallazgo.** En el canvas, el componente rotulado `#113-F1_ETAPA1_CONTEXTO_v04.py` tiene **contrato de NORMATIVA** (entradas: `lot_polygon, sides_table_json, patio_curves, altura_max_pot, tratamiento, …, empate_posterior_pisos`; salidas: `envelope_curve, gfa_total, ocupacion_real, io_maximo, ic_real, ic_maximo, altura_total, pisos_finales, valido, mensaje`) pero su **CodeInput contiene el código de ETAPA1 v04** (no calcula envolvente). Resultado: `envelope/GFA sin fuente` (ya detectado en la sesión anterior como decisión pendiente).

**Consecuencias medidas.**
- `F1_EXPORTAR_GFA_v02` exige `flag.exportar=true` **y** `valido=True`; con `valido=False` no escribe (y no devuelve el flag a false) → el flag quedó en `true`.
- F2 leyó el GFA viejo: `data/fase-2-demanda/AAA0030JKOE-gfa-gh.json` → `generado: 2026-08-22`, `gfa_total_m2: 1845.3473`, **7 pisos** (previo a las definiciones de La Candelaria: 5 pisos, empates por tramo, etc. del ADR-022).

**Propuestas (P3):**
1. Re-encajar **NORMATIVA** en `#113` (mismo contrato; código `F1_ETAPA2_NORMATIVA_v08` mientras llega la **v09** de la fase candelaria) o retirar el duplicado según decisión; el cableado existente no cambia.
2. Exportar GFA de B con la norma vigente (5 pisos, multi-frente/empate por tramo) → nuevo `AAA0030JKOE-gfa-gh.json`; re-correr F2/F3.
3. Añadir **aviso de antigüedad** en el motor F2 (si `generado` > N días o chip distinto → warning, sin bloquear).

### T6 — Operativos y de proceso

- **Puerto:** el conflicto documentado es **19723** (AutoClaw vs Live Connection); no hay referencias a "16723" en proyecto/vault — confirmar con el operador (posible errata). Workaround vigente: cerrar AutoClaw para pruebas vivas / `diagnostico_puerto_19723.ps1 -Liberar` / orden de arranque ArchiCAD→Grasshopper→AutoClaw.
- **Numeración `#NN` volátil** (Escáner/Bifocals renumera por posición): los scripts de parche deben anclarse por **GUID** o marcadores únicos de código, nunca por `#NN`.
- **Front-end:** `f3` muestra ✗ cuando en realidad es "omitido"; distinguir "omitido" de "fallo" (cosmético).
- **UI financiero:** evita crear placeholders vacíos (complemento de T1-capa-2).

---

## 3. Plan de ejecución propuesto (P0–P4)

### P0 — Quick win (inmediato, bajo riesgo) — motor F2 + servidor + re-corrida
- **Tareas:** (1) `F2_DEMANDA_MOTOR_v03.1` (skip de escenarios vacíos + informe + tests); (2) `servidor.py`: skip en proyección de financiero; (3) re-correr F2 B (real) y pipeline; (4) commit.
- **Archivos:** `src/fase-2-demanda/F2_Modelo_Financiero/F2_DEMANDA_MOTOR_v03.py`, `src/orquestador/servidor.py`, `tests/test_f2_venta.py` (+ caso nuevo).
- **Aceptación:** F2 exit 0 con informe; pipeline `f2_venta` ✓; `f3_distribucion` ✓ (con dataset actual); suite de tests verde.
- **Nota:** no requiere canvas ni ArchiCAD; se puede hacer de inmediato.

### P1 — Canvas: curvas horizontales para LC + re-exportaciones (requiere cerrar AutoClaw)
- **Tareas:** (1) patch al canvas (anclado por GUID): salidas aplanadas `*_h` para LC en `#21`/`#113`; boundary horizontal para el Mesh; (2) re-encaje NORMATIVA en `#113` (o decisión de retiro); (3) regenerar `.gh` (`ghx-to-gh.ps1`) con backups; (4) recomputar canvas con flags → exportar **GFA** y **lados/patio**; (5) verificar mensajes, malla y polilíneas; (6) `/api/estado` 6/6.
- **Aceptación:** sin errores LC; `AAA0030JKOE-lados.json` con 6/6; `AAA0030JKOE-gfa-gh.json` nuevo (5 pisos, conforme ADR-022); capturas de evidencia.

### P2 — Vecinos anclados al terreno (z_base)
- **Tareas:** `z_base_m` (MDT) en contexto50/actual; `BUILD v01d` + paridad `ETAPA3 v01.3`; Level LC para Morphs; tests; validación visual inclinada.
- **Aceptación:** vecinos a su cota (tolerancia ±0,5 m); terreno plano sin cambios; mensajes con rango de cotas.

### P3 — NORMATIVA v09 + GFA real + corridas F2/F3
- **Tareas:** NORMATIVA v09 (multi-frente, antejardín 0, empate por tramo, cap 5 pisos, salida IDPC); embed en canvas; export GFA; re-corridas; decidir datasets `D_MIXTO*` vigentes de B (incl. SALUD); aviso de antigüedad en F2.

### P4 — Higiene, docs y registro
- `CLAUDE.md`: parches por GUID, protocolo del canvas/flags, env var; front-end "omitido"; `PATIO v02.5` mensajes; registrar en vault (lecciones + ADR si aplica).

---

## 4. Verificación (procedimientos)

| Fase | Comando / acción | Resultado esperado |
|---|---|---|
| P0 | `py -3.12 .venv\Scripts\python.exe src\fase-2-demanda\F2_Modelo_Financiero\F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0030JKOE_mercado2026.json --chip AAA0030JKOE --pago-parcial 30` | exit 0; informe con A/B/C; "escenarios ignorados: D_MIXTO…" |
| P0 | Pipeline front-end B (o `servidor`) | `f2_venta` ✓ · `f3_distribucion` ✓ |
| P1 | Canvas v11 (AutoClaw cerrado) + recomputo con flags | Sin `Invalid Curve…`; export GFA + lados | 
| P1 | `GET /api/estado?chip=AAA0030JKOE` | F1.5 6/6 OK |
| P2 | Canvas + revisión de cotas | Vecinos sobre el terreno; Morphs en nivel correcto |
| P3 | Export GFA + F2/F3 | GFA 5 pisos; KPIs frescos |

---

## 5. Decisiones pendientes del operador

1. **¿Se aprueba ejecutar P0 ahora?** (sin canvas; no interfiere con nada abierto).
2. Contenido real de `D_MIXTO` / `D_MIXTO_SALUD` / `D_MIXTO_OFICINAS` para B (cuando se defina el mix).
3. Confirmar puerto (¿19723?; "16723" no aparece en ninguna parte).
4. `#113`: ¿re-encaje de NORMATIVA (recomendado) o retiro del duplicado?
5. "Corrida vigente" del caso B para F3 (canónico vs dataset con mix actual).
