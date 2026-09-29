# Resumen de sesión 2026-09-28 (noche 2) — Contexto50: defensiva del template, paridad ETAPA3/builder y `.venv`

**Tema:** revisión de integración de `F1_ETAPA3_CONTEXTO50` con el esquema del lote inclinado (Candelaria `AAA0030JKOE`) + correcciones ejecutadas (ETAPA3 v01.2 / BUILD v01c / canvas v11 / tests) + reparación del `.venv`. *(Validación en canvas pendiente: requiere cerrar AutoClaw — puerto 19723.)*

## Qué se hizo
- **Revisión**: ETAPA3 no está embebida en canvas (rol = `#49 F1_CONTEXTO50_BUILD_v01b`); datos B frescos; vecinos sin cota base (brecha → encargo P2); defensiva del template **muerta** (case + `[:-12]`); deriva ETAPA3↔builder; tests del linaje rotos (rename `v01a`→`v01b`); activos de canvas pendientes para B.
- **Correcciones** (commit `a58ccf3c`):
  - Defensiva → `.lower()` + `f[:-14]` en ETAPA3 **v01.2**, BUILD **v01c** y copia embebida del canvas v11.
  - ETAPA3 v01.2 = **paridad con el builder** (antihorario, exclusiones predio/menores, try/except por edificio, stats/mensaje alineados).
  - Canvas: `patch-ghx-contexto50-defensiva.py` (idempotente, backup) + `.gh` regenerado con GH_IO.
  - Tests: `test_contexto50_build.py` (aislado del canónico; fixtures con/sin hermano; +defensiva) + nuevo `test_etapa3_contexto50.py` → **31/31**.
  - Doc: plan Candelaria §3 (registro + encargo P2: cota por edificio `z_base_m` + `z_base`).
- **`.venv` reparado** (3.ª vez; commit `00fbb7f7`): estaba re-creado con 3.11 sobre wheels cp312 (`shapely.lib`); fix `py -3.12 -m venv --upgrade`; lanzador bloqueado por LSPs de VS Code resuelto; guías a `py -3.12`.

## Verificación
- Raíz **303/303** (py 3.12 y `.venv`); `src/` **31/31**; `test_vecinos_por_lado` 7/7; `pip check` limpio; `Init-DP` selecciona `.venv`.
- Pendiente vivo: validación canvas (activar chip B; #49 ≈ `Volumenes 71/90`; `topo_mesh`).

## Pendientes
- Validación canvas v11 (#49 v01c + terreno); opcional retiro del selector de intérprete; P2 cota por edificio/z_base; heredados (NORMATIVA v09, UI overrides, datasets mixtos, «#113»).

## Documentos
- Vault: `10-arquitectura/2026-09-28-acta-sesion-cierre-contexto50.md`, `50-lecciones/2026-09-28-leccion-{contexto50-defensiva-template,tests-aislados-contexto50,venv-reparacion-lanzador-bloqueado}.md`, `60-diario/2026-09-28.md`, `00-index/mapa-conocimiento.md`.
- Código: `src/fase-1-contexto/F1_ETAPA3_CONTEXTO50_v01.1.py` (contenido v01.2) · `F1_CONTEXTO50_BUILD_v01b.py` (v01c) · `scripts/utilities/patch-ghx-contexto50-defensiva.py` · `gh-definitions/F1_CONTEXTO_v11.gh(x)` · `src/fase-1-contexto/tests/test_contexto50_build.py` · `test_etapa3_contexto50.py`.
- Memoria: `D:\Work\PROJECTS\DiseñoParametrico\memory\sesion-2026-09-28-contexto50.md`.

## Etiquetas
#fase-1 #contexto50 #venv #canvas #tests #candelaria
