---
type: project
fecha: 2026-09-28
responsable: Work
tema: post-prueba-viva-f2-v031-canvas-v042-normativa-zbase
---

# Memoria de sesión 2026-09-28 (noche 3) — Correcciones post prueba viva (F2 v03.1, canvas v04.2/NORMATIVA/z_base)

> Sesión de diagnóstico + ejecución sobre los errores de la prueba viva del canvas `F1_CONTEXTO_v11` (chip `AAA0030JKOE`, AutoClaw cerrado por el puerto 19723). Continúa los cierres del día (mañana: lados/patio + orquestador; tarde/noche: Candelaria; noche 2: contexto50/.venv).

## Contexto de arranque
El operador pidió: (1) revisar los errores aparecidos en la prueba viva (front-end + canvas); (2) establecer un plan con causas raíz; (3) **ejecutar todas las fases** (confirmó 19723 como puerto correcto; la prueba viva se corrió desde el front-end del orquestador); (4) cierre con procedimiento del vault + commit de respaldo.

## Realizado (✅)
- **P0 — Motores/pipeline**: `F2_DEMANDA_MOTOR_v03.1` (escenarios vacíos → `[AVISO]` + `escenarios_ignorados`; guard; `copy.deepcopy` de defaults — fix de contaminación), `F2_RENTA_MOTOR_v03.1` (mismo filtro), `servidor.py` (no proyecta placeholders; **aviso de GFA viejo** `_gfa_gh_estado`/`ANTIGUEDAD_GFA_DIAS=30`; payload con `f2.gfa`; front-end marca "omitido" con ⚠). **Corrida real B ✅** (A/B/C; informe); **F3 B ✅** (5 niveles, huella 663 m²; dataset mixto `resultados_AAA0030JKOE_mixto_2026-08.json`).
- **P1 — Canvas (offline)**: `patch-ghx-v11-fixes-2026-09-28.py` **anclado por GUID** (la numeración `#NN` es volátil): #21 → `F1_ETAPA1_CONTEXTO_v04.2.py` (aplanado a plano horizontal LC), #113 → `F1_ETAPA2_NORMATIVA_v08.py` (restaura envelope/GFA), #48 → `F1_CONTEXTO50_BUILD_v01b.py` v01d, rewire `#125.io_maximo` (← io_maximo). `.gh` regenerado con GH_IO (**145.779 B**); validaciones 4/4; backups `.bak-2026-09-28-2335`.
- **P2 — z_base**: `scripts/utilities/anclar_contexto50_zbase.py` (MDT REST en centroide, **marco canvas** `z_local = z_MDT − (origen_sirgas.z + ancla.z)`): B **90/90 con cota** (rango −20,51…+1,68 m; z_ref 2649,039); `contexto50-actual.json` + `<CHIP>-contexto50.json` (backups `.bak-zbase-*`); BUILD **v01d** + ETAPA3 **v01.3** (paridad) + test (perímetro intacto).
- **Docs**: `docs/planes/2026-09-28-diagnostico-prueba-viva/` (DIAGNOSTICO-Y-PLAN, EJECUCION-Y-RUNBOOK, anexos/evidencia) + lecciones vault ×2 + anexo del diario.

## Verificación
- Suites: **305/305** (raíz) · **32/32** (src fase-1) · **8/8** (F2) · **14/14** (renta) · 9/9 (orquestador).
- z_base: dry-run 3/3 → completo 90/90, 0 fallidos; `_gfa_gh_estado('AAA0030JKOE')` → `antiguo=True` (GFA ago-22) — esperado hasta el re-export vivo.
- Pendiente vivo: validación en canvas (cerrar AutoClaw) — pasos exactos en el runbook.

## Decisiones
- Tolerancia por diseño a placeholders del UI (motores) + no crear placeholders (servidor).
- Parches del canvas por **GUID** y base **canvas-fiel** (v04.2 desde el embed; el src divergía).
- z_base **en marco canvas**; `topo_mesh` queda pendiente de wiring (no hay nodo LC Mesh en v11).
- NORMATIVA v09 como sesión dedicada; dataset mixto B preservado con nombre `_mixto_2026-08`.

## Pendientes
1. Validación viva (runbook): exports GFA/lados, mensajes, `/api/estado` 6/6, morphs, malla.
2. GFA nuevo → `pisos_finales=5` (ADR-022) + re-corrida F2/F3 sin aviso de antigüedad.
3. Wiring `topo_mesh` (decisión) · datasets mix vigentes B · retirar `patch-ghx-contexto50-defensiva.py` obsoleto.
4. Heredados: NORMATIVA v09, UI overrides E/O, P2/P3 terreno/plataformas/multivolumen, ACCESOS v03, Norma 3 pisos PEMP/IDPC, LADOS v07 canvas, Morphs ArchiCAD, ítems 2026-09-11/26, Revit/AutoCAD, Dropbox/bw, discos.

## Enlaces
- Vault: [[2026-09-28-acta-sesion-cierre-post-prueba-viva]] · lecciones [[2026-09-28-leccion-f2-escenarios-vacios-pos-prueba-viva]] · [[2026-09-28-leccion-lc-curvas-horizontales-y-parches-guid]] · [[2026-09-28|Diario]].
- Código: `src/fase-2-demanda/F2_Modelo_Financiero/F2_DEMANDA_MOTOR_v03.py` (v03.1) · `F2_Modelo_Renta/F2_RENTA_MOTOR_v03.py` (v03.1) · `src/orquestador/servidor.py` · `src/orquestador/index.html` · `src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.2.py` · `F1_CONTEXTO50_BUILD_v01b.py` (v01d) · `F1_ETAPA3_CONTEXTO50_v01.1.py` (v01.3) · `scripts/utilities/patch-ghx-v11-fixes-2026-09-28.py` · `scripts/utilities/anclar_contexto50_zbase.py` · `gh-definitions/F1_CONTEXTO_v11.gh(x)`.
- Runbook: `docs/planes/2026-09-28-diagnostico-prueba-viva/EJECUCION-Y-RUNBOOK.md`.
