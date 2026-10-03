# Sesión 2026-10-03 — Tope Ocupación IO v13 → v13.1

## Resumen
Plan aprobado para reducir ocupación al IO ≤ 0.70 en caso La Candelaria (AAA0030JKOE, 946.34 m²). Ocupación 936.56 m² (IO 0.9897) → exceso 274.12 m². 7 decisiones (D1–D7), implementación P0–P3 (código base listo). Canvas v13.1 preparado para patch manual. Validación viva bloqueada por puerto 19723.

## Decisiones aprobadas
| ID | Tema | Decisión |
|---|---|---|
| D1 | Canvas | v13.1 parche in-place |
| D2 | Entrepiso | Adaptativo 3.05/3.80 m |
| D3 | Prioridad | Profundidad → Entrepiso → Nº cuerpos |
| D4 | Margen IO | Estricto 0.70 (tol 0.0001) |
| D5 | Versionado | Homogeneizado |
| D6 | Export GFA | Solo gfa_aprobado |
| D7 | IC | Postergar |

## Código implementado (P0–P3)
- **NORMATIVA v09**: `F1_ETAPA2_NORMATIVA_v09.py` — entrada `barras_json`, presupuesto IO, salidas aprobadas, validador schema v01
- **Tests**: `test_normativa_v09_fuente.py`
- **F3_DISTRIBUCION_v03**: `F3_DISTRIBUCION_v03.py` — distribuidor con presupuesto IO, entrepiso adaptativo, prioridad D3
- **Export GFA v02.4**: `F1_EXPORTAR_GFA_v02.4.py` — modo APROBADO solo `gfa_aprobado`
- **Orquestador v01.1**: `run_pipeline_v01.py` — loop F3→NORMATIVA+barras_json→EXPORT APROBADO
- **LADOS v06.8**: `F1_ETAPA2_LADOS_v06.py` — fix altura 0 = patio confirmado en puente Orquestador
- **PATIO v03.3**: `F1_ETAPA2_PATIO_v03.py` — doc: 1 vol=patio normativo; ≥2 vol=separaciones en IO
- **Plan**: `DELIVERY/PLAN-ACCION-TOPE-OCUPACION-v13.md` + copia en `docs/planes/2026-10-03-tope-ocupacion-io/`

## Lecciones nuevas (vault 50-lecciones)
- 2026-10-03-leccion-presupuesto-io-previo-distribucion.md
- 2026-10-03-leccion-entrepiso-adaptativo-305-380.md
- 2026-10-03-leccion-altura-cero-patio-vecino.md
- 2026-10-03-leccion-patios-vs-separaciones-io.md
- 2026-10-03-leccion-canvas-v13-parche-inplace.md
- 2026-10-03-leccion-puerto-19723-bloqueador.md

## Vault actualizado
- Acta: `10-arquitectura/2026-10-03-acta-sesion-cierre-tope-ocupacion-io-v13.md`
- Diario: `60-diario/2026-10-03.md`
- Mapa: `00-index/mapa-conocimiento.md` (entrada 2026-10-03 + diario)

## Pendientes esta sesión
1. Patch manual canvas v13.1 en Rhino/GH (operador)
2. Validación offline: pytest + run_pipeline casos A/B/B_SALUD/C
3. Validación viva (bloqueada 19723)
4. Confirmar LADOS v06.8 recibe puente Orquestador
5. Verificar ancho_via_m > 0 en LADOS

## Pendientes sesiones anteriores (sin resolver)
- 2026-09-30: Validación viva par v12, v03.2 patios interiores, renombrar grupos canvas
- 2026-09-29: NORMATIVA v09 completa (ADR-022), P2/P3 Candelaria
- 2026-09-26: Puerto 19723 (estructural), retirar fcc-sanitizer
- 2026-09-11: Reset AutoClaw vs openclaw.json (ADR-015)
- 2026-08-13/14: Build-to-Rent, instalar Revit+AutoCAD
- 2026-09-20: Dropbox cuenta 5, yzarq.com, bw lock
- 2026-09-22/27: Salud disco F:/H:, MiMo-Flash-RL, ComfyUI

## Próximos pasos
1. Operador: patch canvas v13.1 → guardar timestamps sincronizados
2. Validación offline completa
3. Validación viva cuando 19723 estable
4. Sesión NORMATIVA v09 (ADR-022)
5. v03.2 patios interiores + Zonas

## Commits de respaldo
- Proyecto: `D:\Work\PROJECTS\DiseñoParametrico/` (archivos P0–P3)
- Vault: `D:\Work\NOTES\obsidian-vault/` (acta, diario, 6 lecciones, mapa)
- Workspace: `C:\Users\Dario Salas\.openclaw-autoclaw\workspace/` (plan DELIVERY, MEMORY.md)