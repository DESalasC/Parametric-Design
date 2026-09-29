---
type: project
fecha: 2026-09-28
responsable: Work
tema: contexto50-defensiva-paridad-etapa3-builder-venv
---

# Memoria de sesión 2026-09-28 (noche 2) — Contexto50 v01.2/v01c + reparación del `.venv`

> Sesión de revisión + correcciones sobre el linaje contexto50 (ETAPA3/BUILD/canvas) y reparación del entorno. Continúa los cierres del día (mañana: lados/patio + orquestador; tarde/noche: Candelaria).

## Contexto de arranque
El operador pidió **revisar** `F1_ETAPA3_CONTEXTO50_v01.1.py` frente al esquema del lote inclinado (Candelaria `AAA0030JKOE`), **ejecutar todas las correcciones** detectadas y **reparar el `.venv`** antes del cierre.

## Realizado (✅)
- **Revisión de integración**: ETAPA3 **no está en el canvas** (el rol lo cumple `#49 F1_CONTEXTO50_BUILD_v01b`); canónico B fresco; vecinos sin cota base (brecha → encargo P2). Defectos: defensiva muerta (2 bugs), deriva ETAPA3↔builder, tests rotos por rename v01a→v01b, activos de canvas pendientes para B.
- **Correcciones (commit `a58ccf3c`)**:
  - Defensiva del template: case-insensitive + `f[:-14]` en **3 sitios** (ETAPA3 **v01.2**, BUILD **v01c**, copia embebida del canvas v11).
  - **ETAPA3 v01.2 en paridad con el builder**: antihorario, exclusiones (predio objetivo/menores), try/except por edificio, stats/mensaje, `extraer_anillos`/`_pt_xy`.
  - **Canvas v11**: `patch-ghx-contexto50-defensiva.py` (idempotente + backup) re-embebe el #49 (`embedded == src`); `.gh` regenerado con GH_IO (backups).
  - **Tests**: `test_contexto50_build.py` (sin versión; aislamiento `DISENO_PARAMETRICO_ROOT` + fixtures con/sin hermano + test defensiva); helpers v01b; nuevo `test_etapa3_contexto50.py`. **31/31**.
  - Doc: `EVALUACION-Y-PROPUESTA.md` §3 — registro + **encargo P2** (cota por edificio `z_base_m` + `z_base`).
- **`.venv` reparado (3.ª vez; commit `00fbb7f7`)**: re-creado con 3.11 sobre wheels cp312 → `py -3.12 -m venv --upgrade .venv`; lanzador bloqueado por LSPs de VS Code → renombrado en uso; guías (`SETUP_ENV.md`, `entorno_python.ps1`) → `py -3.12` + nota de reparación.

## Verificación
- Suites: raíz **303/303** (py 3.12 y `.venv`); `src/fase-1-contexto/tests` **31/31**; `test_vecinos_por_lado` 7/7; `pip check` limpio; `Init-DP` selecciona `.venv` (3.12.10).
- Pendiente vivo: validación en canvas (cerrar AutoClaw; activar chip B). Mensaje esperado #49 ≈ `Volumenes 71/90`.

## Decisiones
- ETAPA3 se **alinea** con el builder (no se deprecia) — contraparte verificable en paridad.
- Fixes sin renombrar archivos (subversión interna: v01.2 / v01c); tests sin versión en el nombre.
- Selector de intérprete se mantiene como respaldo (ya resuelve a `.venv`); su retiro queda como decisión opcional futura.

## Pendientes
1. Validación en canvas v11 con #49 v01c (activar chip B; `topo_mesh`; probar defensiva sin canónico).
2. Opcional: retirar el selector de intérprete.
3. P2: cota por edificio (`z_base_m`) + `z_base`.
4. Heredados: NORMATIVA v09, UI overrides, datasets mixtos, «#113», Morphs ArchiCAD, etc.

## Enlaces
- Vault: [[2026-09-28-acta-sesion-cierre-contexto50]] · lecciones (`contexto50-defensiva-template`, `tests-aislados-contexto50`, `venv-reparacion-lanzador-bloqueado`) · [[2026-09-28|Diario 2026-09-28]].
- Código: `src/fase-1-contexto/F1_ETAPA3_CONTEXTO50_v01.1.py` (v01.2) · `F1_CONTEXTO50_BUILD_v01b.py` (v01c) · `tests/test_contexto50_build.py` · `tests/test_etapa3_contexto50.py` · `scripts/utilities/patch-ghx-contexto50-defensiva.py`.
