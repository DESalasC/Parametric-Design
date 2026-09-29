# Resumen de sesión 2026-09-28 (noche 3) — Correcciones post prueba viva: F2 v03.1, canvas (curvas LC + NORMATIVA + z_base) y runbook

**Tema:** diagnóstico y ejecución de las correcciones a los errores de la **prueba viva** del canvas `F1_CONTEXTO_v11` (chip B `AAA0030JKOE`; AutoClaw cerrado — puerto 19723). Aprobado por el operador "ejecutar todas las fases según la propuesta". *(La validación final en canvas queda con runbook para la próxima sesión.)*

## Qué se hizo
- **Plan**: `docs/planes/2026-09-28-diagnostico-prueba-viva/` — DIAGNOSTICO-Y-PLAN + EJECUCION-Y-RUNBOOK + anexo de evidencia (trazas, reproducciones, flags, referencias LC).
- **P0 (F2/pipeline)** — commit `3e5ba33f`:
  - Motor `F2_DEMANDA_MOTOR_v03.1`: escenarios vacíos tolerados (`[AVISO]` + `escenarios_ignorados`), guard, `copy.deepcopy` de defaults (bug de contaminación); `F2_RENTA_MOTOR_v03.1` igual.
  - `servidor.py`: no proyecta placeholders; aviso de GFA viejo (`_gfa_gh_estado`, 30 días); `f2.gfa` en el payload.
  - **Corrida real B OK**; **F3 B** → 5 niveles, huella 663 m²; dataset mixto preservado (`resultados_AAA0030JKOE_mixto_2026-08.json`); `parametros_AAA0030JKOE_mercado2026.json` limpio (bak).
- **P1 (canvas, offline)** — commit `895dd4e2`: parche **por GUID** (`patch-ghx-v11-fixes-2026-09-28.py`): #21 → **v04.2** (curvas aplanadas a plano horizontal LC), #113 → **NORMATIVA v08** (restaura envelope/GFA), #48 → **v01d** (z_base), rewire `#125.io_maximo`; `.gh` regenerado con GH_IO (145.779 B) + backups.
- **P2 (z_base)** — `anclar_contexto50_zbase.py` (MDT en centroide, marco canvas): B **90/90** (−20,51…+1,68 m; z_ref 2649,039); BUILD v01d + ETAPA3 **v01.3**; test nuevo.
- **Extras**: front-end marca "omitido" con ⚠ (commit `f4e270cd`); docs (commit `db5eeb52`); lecciones vault ×2; anexo del diario.

## Verificación
- Suites: raíz **305/305**; `src/fase-1-contexto/tests` **32/32**; F2 **8/8**; renta **14/14**; orquestador 9/9.
- z_base: dry-run 3/3 → completo 90/90 (0 fallidos). Canvas: parche validado 4/4.
- Pendiente vivo: validación en canvas (cerrar AutoClaw; runbook paso a paso).

## Pendientes
- Validación viva (runbook) → exports GFA/lados; `pisos_finales=5` (ADR-022); re-corrida F2/F3; `/api/estado` 6/6; morphs; malla.
- Wiring `topo_mesh`; datasets mix vigentes B; retirar parche `#49` obsoleto; NORMATIVA v09 (sesión dedicada); heredados (UI overrides, P2/P3 multivolumen, IDPC, LADOS v07, etc.).

## Documentos
- Vault: `10-arquitectura/2026-09-28-acta-sesion-cierre-post-prueba-viva.md`, lecciones `50-lecciones/2026-09-28-leccion-{f2-escenarios-vacios-pos-prueba-viva,lc-curvas-horizontales-y-parches-guid}.md`, `60-diario/2026-09-28.md`, `00-index/mapa-conocimiento.md`.
- Proyecto: `docs/planes/2026-09-28-diagnostico-prueba-viva/` · `memory/sesion-2026-09-28-post-prueba-viva.md` · código citado arriba.
- Memoria: `D:\Work\PROJECTS\DiseñoParametrico\memory\sesion-2026-09-28-post-prueba-viva.md`.

## Etiquetas
#fase-1 #fase-2 #canvas #live-connection #z-base #prueba-viva #candelaria
