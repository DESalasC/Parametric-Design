---
type: project
fecha: 2026-09-28
responsable: Work
tema: lote-inclinado-candelaria-topografia-real-normativa
---

# Memoria de sesión 2026-09-28 (noche) — Lote inclinado La Candelaria (topografía real + validación normativa)

> Sesión de proyecto (evaluación + P0 + consulta normativa + reglamentación base). Continúa el hilo del cierre 2026-09-28 (lados/patio + orquestador).

## Contexto de arranque
El operador pidió evaluar el proceso completo para un **lote inclinado** en La Candelaria (caso B, `AAA0030JKOE`) con volúmenes múltiples con separaciones, dos vías, cap de altura y empate parcial con conservación; aprobó el plan y fue dando los criterios (área = geobase; **5 pisos**; BIC **2 p / ~20 m**; sur **5 p / ~25 m**; medición **desde la calle occidental**; **sin antejardín**). Al final: consulta normativa validada, reglamentación base descargada/registrada y cierre.

## Realizado (✅)
- **P0 ejecutado** (plan en `docs\planes\2026-09-28-evaluacion-lote-inclinado-candelaria\`):
  - **fetch v7** (`scripts/utilities/fetch-urban-context-v7.py`): parser MDT corregido + muestreo densificado (118 pts) + `resumen`/`perfil_lados`; referencias actualizadas; re-fetch B (Δ 16,12 m / 25,85 %; contexto50 con 90 construcciones).
  - **norma-override B**: UPZ 94, rango "4" → 5 pisos, IO 0,70, Nota Ñ (la ficha dice "Ñ"; el norma-manual decía "N").
  - **`vecinos_por_lado.py`**: ignora EP que cubren el lote (overlap > 5 m²; `eps_ignorados`) + test; suite **303/303**.
  - **F3 corrida B/B_SALUD a 5 niveles** (tolerancia `ceil` 1e-6 + huella sin redondeo; lote 931→946,45); accesos y `.3dm` regenerados.
  - **Validación normativa** (§4 del doc): empates (§1.6/§5.5.c; cumbrera N-2; 3×3 IDPC), separación entre volúmenes ≥ máx(2/5·h_prom; 6,00 m) (§1.10.b), patios 1/3·h mín 3 m (§1.12.b), piso de bonificación = escenario (sin aval IDPC).
- **Reglamentación base** en el vault: `30-referencia/pot-bogota/reglamentacion-base/` (29 archivos: PDFs originales + 8 fichas `.md` + índice; registro en el mapa; commits `d2d77de` + cierre).
- **Cierre**: acta `2026-09-28-acta-sesion-cierre-candelaria`, ADR-021/022, 4 lecciones, diario; **fix de `vault_append.py`** (slug seguro; incidente ADS del ":" detectado y resuelto, backup `vault_append.py.bak-20260928-2115`).

## Decisiones
- **ADR-021** — Topografía real en el fetch (v7): parser MDT + muestreo densificado + datum.
- **ADR-022** — Criterios normativos del caso La Candelaria (altura 5 pisos; sin antejardín; empate parcial por tramo; separaciones ≥ 6 m; piso de bonificación como escenario; corrida base 5 niveles).
- Operativas: EP-cubre-lote se ignora; tolerancias F3; lote 946,45.

## Hallazgos / lecciones
- El "0.0" por defecto escondía el bug de topografía (todos los lotes "planos").
- Capas POT "propuestas" (Pueblo Viejo) sesgan la clasificación → filtrar por overlap/estado.
- Redondeos + `ceil` = pisos fantasma (0,075 m² → un nivel extra).
- Distinguir derecho normativo vs aspiración del expediente ("piso de bonificación").
- `vault_append.py` generaba ADS por el ":" del título → parchado (slug).

## Pendientes
1. **NORMATIVA v09 (P1)**: multi-frente + antejardín 0 + empate por tramo + cap 5 pisos + salida IDPC.
2. **Validación en canvas v11 + terreno** (cerrar AutoClaw; activar chip B).
3. **UI**: overrides E/O = vías; alturas de vecinos (2p/20m; 5p/25m).
4. **P2/P3**: `F1_ETAPA4_TERRENO`, `F3_PLATAFORMAS`, `F3_MULTIVOLUMEN`; `ACCESOS v03`.
5. Verificar "Norma 3 pisos" (alzado PEMP 12F–12D) y piso de bonificación con IDPC.
6. Heredados: canvas v11 (mañana), «#113», datasets mixtos, `.venv`, `CLAUDE.md`, Morphs ArchiCAD, etc.

## Enlaces
- Vault: [[2026-09-28-acta-sesion-cierre-candelaria]] · [[adr-021-topografia-real-fetch-v7]] · [[adr-022-criterios-normativos-candelaria]] · [[00-index-reglamentacion-base]] · [[2026-09-28|Diario 2026-09-28]].
- Evidencias: `docs\planes\2026-09-28-evaluacion-lote-inclinado-candelaria\` (EVALUACION-Y-PROPUESTA §3–§4, evidencia MDT, anexos/insumos).
