# Resumen de sesión 2026-09-28 (noche) — Lote inclinado La Candelaria

**Tema:** evaluación + P0 (topografía real, fetch v7), validación normativa (empates/separaciones/altura) y reglamentación base registrada en el vault. *(Validación en canvas pendiente: requiere cerrar AutoClaw — puerto 19723.)*

## Qué se hizo
- **Evaluación + propuesta** del lote inclinado (4 capas: terreno → envolvente multi-frente → fragmentación → masa/flujos; plan P0–P3) — `docs\planes\2026-09-28-evaluacion-lote-inclinado-candelaria\`.
- **Fetch v7**: parser MDT corregido (`attributes["Stretch.Pixel Value"]`) + muestreo densificado; re-fetch B (Δ 16,12 m / 25,85 %; 118/118 cotas; `contexto50` con 90 construcciones).
- **Norma B al override** (Decreto 492/07: 5 pisos, IO 0,70, Nota Ñ; 10 m como referencia).
- **Clasificador de vecinos**: filtra EP que cubren el lote ("Pueblo Viejo", propuesto); test de regresión; suite **303/303**.
- **Corrida B/B_SALUD a 5 niveles** (fix `ceil` + huella sin redondeo; lote 946,45); accesos y `.3dm` regenerados.
- **Validación normativa** (§4 del doc): empate parcial por tramo (cumbrera N-2; + 3×3 solicitado por IDPC); separación entre volúmenes ≥ máx(2/5·h_prom; 6,00 m); patios 1/3·h mín 3 m; **piso de bonificación = escenario** (sin aval IDPC) → corrida base 5.
- **Reglamentación base** descargada y registrada en el vault (`30-referencia/pot-bogota/reglamentacion-base/`; 29 archivos; originales + fichas). Fix de `vault_append.py` (slug seguro).

## Decisiones
- **ADR-021** — Topografía real en el fetch (v7).
- **ADR-022** — Criterios normativos del caso La Candelaria (altura/empates/separaciones/bonificación).

## Pendientes
- **NORMATIVA v09 (P1)** con los criterios validados; UI (overrides E/O = vías; alturas de vecinos); validación canvas + terreno; P2 terreno/plataformas/multivolumen.

## Documentos
- Plan + evidencias: `docs\planes\2026-09-28-evaluacion-lote-inclinado-candelaria\` (EVALUACION-Y-PROPUESTA §3–§4.4, evidencia MDT, anexos/insumos).
- Vault: `10-arquitectura/2026-09-28-acta-sesion-cierre-candelaria.md`, `decisiones-adr/adr-021…`/`adr-022…`, `50-lecciones/2026-09-28-leccion-{parser-mdt-fetch-z0,ep-cubren-lote,precision-numerica-f3,norma-vs-expediente}…`, `30-referencia/pot-bogota/reglamentacion-base/`, `60-diario/2026-09-28.md`.
- Memoria: `D:\Work\PROJECTS\DiseñoParametrico\memory\sesion-2026-09-28-candelaria.md`.

## Etiquetas
#fase-1 #topografia #normativa #candelaria #fetch #vault
