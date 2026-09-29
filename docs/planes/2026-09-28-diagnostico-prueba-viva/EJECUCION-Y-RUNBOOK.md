# Ejecución y runbook — Correcciones post prueba viva (noche 2026-09-28)

Documento de ejecución del plan `DIAGNOSTICO-Y-PLAN.md`.
**Estado:** P0 ✅ · P1 (offline) ✅ · P2 (código+datos) ✅ · validación viva del canvas **pendiente** (requiere cerrar AutoClaw — puerto 19723).

---

## A. Ejecutado (con evidencia)

### A1. P0 — Motor F2 / servidor / re-corrida
- `F2_DEMANDA_MOTOR_v03.py` → v03.1: escenarios sin datos se ignoran con `[AVISO]` y quedan en
  `resultados_completos.json → escenarios_ignorados`; guard "sin escenarios"; `copy.deepcopy`
  de `_DEFAULT_PARAMS` (fix de contaminación entre llamadas en un mismo proceso).
- `F2_RENTA_MOTOR_v03.py` → v03.1: mismo filtro.
- `servidor.py`: `_financiero_override_guardar` no proyecta escenarios solo-nulos;
  `_calcular_f2` agrega `[AVISO]` de GFA antiguo/ausente (helper `_gfa_gh_estado`); el
  payload del pipeline incluye `f2.gfa`.
- **Corrida real F2 B** (`AAA0030JKOE`): exit 0; informe + CSV generados; canónico
  `resultados/resultados_AAA0030JKOE.json` actualizado; dataset mixto preservado como
  `resultados_AAA0030JKOE_mixto_2026-08.json` (lo usa F3).
- **F3 B**: `OK AAA0030JKOE: 5 niveles, huella 663 m², ascensores 2, núcleo 45 m²/piso`
  + accesos regenerados (usa el dataset mixto). Cascada F2→F3 reparada.
- Tests: `tests/test_f2_escenarios_vacios.py` (nuevo) + `test_f3_chip_generico.py`
  actualizado (contrato "archivo con mix").
- Limpieza: `parametros_AAA0030JKOE_mercado2026.json` sin placeholders
  (backup `.bak-empties-2026-09-28`).

### A2. P1 — Canvas (offline)
Parche `scripts/utilities/patch-ghx-v11-fixes-2026-09-28.py` (anclado por **GUID**;
la numeración `#NN` es volátil porque el Escáner la reasigna por posición):
| Fix | Componente | Resultado |
|---|---|---|
| Curvas aplanadas a plano horizontal (LC) | #21 (guid `0d986a36…`) ← `F1_ETAPA1_CONTEXTO_v04.2.py` (copia canvas-fiel) | CodeInput 15.655 → 16.322 chars |
| Re-encaje NORMATIVA (envelope/GFA) | #113 ← `F1_ETAPA2_NORMATIVA_v08.py` | 14.139 → 50.484 chars |
| z_base por edificio | #48 ← `F1_CONTEXTO50_BUILD_v01b.py` (v01d) | 24.031 → 24.892 chars |
| Rewire `#125.io_maximo` (iba a `ic_maximo`) | chunk `cb180da5…` | Source → `86d781d0…` (OK) |
- `.gh` regenerado con `ghx-to-gh.ps1` (GH_IO): **145.779 B**; backups
  `*.bak-2026-09-28-2335`. Validación de markers: 4/4 OK.

### A3. P2 — z_base de vecinos (datos + código)
- `scripts/utilities/anclar_contexto50_zbase.py`: muestrea el MDT (REST Catastro,
  reutiliza fetch v7) en el centroide de cada huella y escribe `z_base_m`
  **en el marco del canvas** (`z_local = z_MDT − z_ref`, `z_ref = origen_sirgas.z + ancla.z`).
- Corrida B: **90/90 edificios con cota, 0 fallidos**; rango **−20,51 … +1,68 m**
  (z_ref = 2649,039; ancla del lote = 0). Actualizados `<CHIP>-contexto50.json` y
  `contexto50-actual.json` (backups `.bak-zbase-*`).
- `F1_CONTEXTO50_BUILD` v01d + `F1_ETAPA3_CONTEXTO50` v01.3 (paridad): huella y extrusión
  desde `z_base_m`; mensaje incluye rango; sin `z_base_m` → comportamiento previo (z=0).
- Tests: `test_z_base_v01d_mueve_y_conserva_perimetro` (perímetro XY intacto).

### A4. Suites
- Raíz: **305/305** · contexto50/ETAPA3: **32/32** (+ z_base) · F2: **8/8** · renta: **14/14**.

### A5. Registro
- Lecciones vault: `2026-09-28-leccion-f2-escenarios-vacios-pos-prueba-viva.md`,
  `2026-09-28-leccion-lc-curvas-horizontales-y-parches-guid.md`.
- Anexo en el diario del vault con los commits.

---

## B. RUNBOOK — Validación viva (cerrar AutoClaw primero)

> El conflicto de puerto es **19723** (AutoClaw vs Live Connection). Cerrar AutoClaw antes
> del paso 2 (si hace falta: `diagnostico_puerto_19723.ps1`).

1. **Cerrar AutoClaw.**
2. Abrir Rhino 8 + Grasshopper → `gh-definitions\F1_CONTEXTO_v11.gh` (regenerado 28-09 23:35).
   - Verificar `DISENO_PARAMETRICO_ROOT` con los indicadores del canvas (#3/#19/#67 muestran el valor).
3. Iniciar el orquestador: `D:\Work\Scripts\Init-DP.cmd` (front-end 8900; no conflictúa).
   - Seleccionar/activar chip **AAA0030JKOE** (activa contexto, vecinos y caso).
4. Pulsar **"Exportar GFA"** y **"Exportar diagnóstico lados+patio"** y **recomputar el canvas (F5)**:
   - Debe escribirse `data/fase-2-demanda/AAA0030JKOE-gfa-gh.json` (nuevo) con
     `valido=true`; **revisar `pisos_finales` (esperado 5 — ADR-022)** y `gfa_total_m2`.
   - Debe escribirse `data/pot-cache/AAA0030JKOE-lados.json`; luego
     `GET /api/estado?chip=AAA0030JKOE` → **F1.5 6/6**.
   - Los dos flags vuelven a `false` (patrón de exportación).
5. Mensajes esperados en el canvas (sin rojos):
   - #21 `ETAPA1 v04.2 | CHIP: AAA0030JKOE | …`; #81 `LADOS v06.5 …`;
     #99 `PATIO v02.4 … (área ≥ 9 m², claridad ≥ 3 m)`; #48
     `CONTEXTO50_BUILD | … | z_base −20,5–1,7 m (90 con cota)`;
     sin `Invalid Curve value…` en #161/#162/#163/#71; `#74 Morph Solid` con volúmenes.
6. **Vecinos en ArchiCAD**: verificar que los Morphs de volumetrías ya no quedan todos a
   nivel 0.0 (cota del terreno). Si el Morph necesita Story/Level distinto, anotar para P2b.
7. **Malla del terreno** (`topo_mesh`): en v11 quedó **huérfana** (no existe nodo LC "Mesh").
   Opciones: (a) verla en Rhino (preview de la salida de #21), o (b) cablearla a mano con un
   nodo **Mesh** de la Live Connection: `Pts` ← vértices de `topo_mesh` (Deconstruct Mesh → V),
   `Boundary` ← curva cerrada **horizontal** (rectángulo envolvente en Z=0 del área muestreada);
   validar que no dispare el error de plano horizontal. Registrar la decisión.
8. Con el GFA nuevo: re-correr **pipeline completo** del front-end (F2→F3) y revisar
   `f2_venta ✓`, `f3_distribucion ✓` y el bloque `f2.gfa` (sin aviso de antigüedad).
9. Si se hacen cambios manuales al canvas: `Save As` a `F1_CONTEXTO_v12.ghx` (no pisar el
   `.ghx` regenerado; los parches dejan `.bak-*` de todos modos).
10. Cierre: commit del repo (ya hay 3 commits de esta ejecución como base) + registrar en el
    vault (anexo + lecciones ya creados).

---

## C. Apéndice — comandos usados (verificación reproducible)

```powershell
# F2 venta (B)
.\.venv\Scripts\python.exe src\fase-2-demanda\F2_Modelo_Financiero\F2_DEMANDA_MOTOR_v03.py `
  --parametros parametros_AAA0030JKOE_mercado2026.json --chip AAA0030JKOE --pago-parcial 30
# F3 (B)
.\.venv\Scripts\python.exe src\fase-3-masa\F3_DISTRIBUCION_v01.py --chip AAA0030JKOE --escenario D_MIXTO
.\.venv\Scripts\python.exe src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py --caso AAA0030JKOE
# z_base (MDT) — probar sin escribir primero
.\.venv\Scripts\python.exe scripts\utilities\anclar_contexto50_zbase.py --chip AAA0030JKOE --dry-run --limite 3
# Parche del canvas + regeneración .gh
.\.venv\Scripts\python.exe scripts\utilities\patch-ghx-v11-fixes-2026-09-28.py
pwsh -NoProfile -File scripts\utilities\ghx-to-gh.ps1 -InputGhx gh-definitions/F1_CONTEXTO_v11.ghx -OutputGh gh-definitions/F1_CONTEXTO_v11.gh
# Suites
.\.venv\Scripts\python.exe -m pytest tests -q
.\.venv\Scripts\python.exe -m pytest src\fase-1-contexto\tests -q
```

## D. Pendientes / decisiones
- **NORMATIVA v09** (multi-frente, antejardín 0, empate por tramo, cap, salida IDPC) — fase P3, dedicada.
- **Datasets mix vigentes de B** (D_MIXTO / SALUD a escala actual) — hoy F3 usa `_mixto_2026-08`.
- **Mesh wiring** (paso 7b) — decisión del operador.
- Retirar/actualizar el viejo `patch-ghx-contexto50-defensiva.py` (nickname `#49` stale):
  el parche GUID nuevo lo reemplaza para el canvas v11.
- Al re-exportar GFA: confirmar `pisos_finales=5` y `gfa_total` coherente con ADR-022
  (si no, es la primera tarea de la sesión de NORMATIVA v09).
