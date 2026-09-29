# Resumen de sesión 2026-09-28

**Tema:** F1-ETAPA2 «lados/patio» (corrección + reglas nuevas), orquestador web unificado y cadena de contexto/entorno. *(La validación en canvas queda pendiente: requiere cerrar AutoClaw — puerto 19723.)*

## Qué se hizo
- **Bug crítico resuelto**: LADOS v06 llamaba `point_in_lot()` sin definirla (la rama de intersecciones vía-vía abortaba toda la clasificación con vías cruzadas) → **LADOS v06.5**.
- **Reglas del operador implementadas**: patio con **área ≥ 9 m²** y **claridad ≥ 3 m lineales** (`L = max(base, 3/sin θ)`); **simplificación** de lados con giro **< 2.5°**. Lotes: `AAA0240ZXJH` 13→4; `AAA0127AZPA` 9→4.
- **PATIO v02.3/v02.4**: garantías, dedup, anclaje, máximo 1 patio y **export del diagnóstico** (`<CHIP>-lados.json`) por flag.
- **Canvas `F1_CONTEXTO_v11`** parcheado (backups) y `.gh` regenerado; códigos embebidos = repo.
- **Orquestador unificado**: `orquestador_v01.py` (front-end 8900 + pipeline vía HTTP), `servidor.py` ampliado (pipeline completo + `/api/estado`, `/api/exportar-lados`, `/api/nuevo-chip`), **`Init-DP.ps1/.cmd`** en `D:\Work\Scripts`.
- **F1.5 ejecutado**: diagnóstico verificado 6/6 (área 9.0–10.4 m², claridad 3.0 m).
- **Front-end**: altura de vecinos bloqueada en *vía (no frontal)* / *espacio público*; **«CHIP nuevo»** como disparador del proceso.
- **F3 reparado**: prioriza el dataset del chip con mix `D_MIXTO*` (El Prado → caso A `gfa1461_cl800`); `casos/AAA0127AZPA/` regenerado (incl. `.3dm`).
- **Entorno**: `POT_*` restablecidas, defaults portables, selector de intérprete (Python 3.12).
- **Tests**: suite **289/289** (incluye 6 conductuales con stub de Rhino en CPython).

## Decisiones
- **ADR-019** — reglas de patio y simplificación de lados (F1-ETAPA2).
- **ADR-020** — orquestador web único (front-end 8900) y protocolo de activos/export F1.5.

## Pendientes
- Validación en **canvas v11** (cerrar AutoClaw): mensajes `LADOS v06.5`/`PATIO v02.4` + export nativo.
- Componente «**#113**» (¿slot NORMATIVA o duplicado?); dataset mixto nuevo y mix de `AAA0240ZXJH`.
- Reconstruir **`.venv`** (3.ª vez); documentar `CLAUDE.md` (punto de entrada único).

## Documentos
- Plan + evidencias: `docs\planes\2026-09-28-plan-correccion-lados-patio\` (PLAN.md + anexos: arnés CPython, demos F1.5/pipeline, fixes y QA de UI).
- Vault: `10-arquitectura/2026-09-28-acta-sesion-cierre.md`, `50-lecciones/2026-09-28-leccion-*.md` (3), `10-arquitectura/decisiones-adr/adr-019…/adr-020…`, `60-diario/2026-09-28.md`.
- Memoria: `D:\Work\PROJECTS\DiseñoParametrico\memory\sesion-2026-09-28.md`.

## Etiquetas
#fase-1 #lados #patio #orquestador #front-end #f3 #entorno
