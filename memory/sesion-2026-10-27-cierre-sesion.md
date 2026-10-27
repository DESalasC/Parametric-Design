# Memoria de sesión — 2026-10-27 (DiseñoParametrico)

## Sesión de trabajo

**Fecha:** 2026-10-27  
**Proyecto:** DiseñoParametrico  
**Tipo:** Cierre de sesión  
**Estado:** Cerrado ordenadamente

## Situación encontrada

El proyecto DiseñoParametrico tiene el pipeline modular F1 (ETAPA1/ETAPA2) vigente, F2 completado, y F3 en desarrollo avanzado. El chip objetivo para pruebas es AAA0030JKOE (La Candelaria, caso B, modo mixto). El estado de avance vigente es el corte 2026-10-12.

## Estado del pipeline (AAA0030JKOE, caso B, mixto)

Ejecutado `run_pipeline_v01.py --status`:

- [OK] F1 Contexto normativo (fetch) — CHIP-contexto.json activo
- [OK] F1 Alzado vía frontal (z=0)
- [OK] F1 Contexto 50 m (fetch)
- [OK] F1 Cotas MDT vecinos (z_base_m, 90/90)
- [OK] F1 Exportar GFA (manual Rhino)
- [ ] F3 Distribuidor barras — barras.json FALTA
- [??] F1 NORMATIVA v09 + barras_json — manual canvas v13.1
- [??] F1 Exportar GFA APROBADO — manual
- [OK] F2 Modelo financiero (venta)
- [OK] F2 Modelo Build-to-Rent (renta)
- [OK] F3 Distribución espacial (v02) — programa-areas.json
- [OK] F3 Accesos por uso — accesos.json
- [??] F3 Masa en Rhino + Morphs ArchiCAD — manual

## Variables de nuevas acciones del Orquestador (faltantes de conectar)

| Variable | Origen | Dónde conectar |
|---|---|---|
| presupuesto_ocupacion_m2 | Panel NORMATIVA v09 | F3_DISTRIBUCION --presupuesto-ocupacion |
| barras_json | F3_DISTRIBUCION_v03 | NORMATIVA v09 re-ejecutada |
| gfa_aprobado_m2 | NORMATIVA v09 | F1_EXPORTAR_GFA_v02.4 |
| z0_m, z0_abs_m, origen_z_m | calcular_z0_proyecto.py (ADR-024) | F3_VOLUM_GENERADOR / niveles AC |
| zgf_m | F3_StorySync_v02 | F3_VOLUM_GENERADOR (−zgf_m a morphs/zonas) |

## Problemas planteados

- Type hints Python 3 en F3_DISTRIBUCION_v03.py incompatibles con IronPython 2.7.
- Canvas v13.5 nodo #198 una revisión atrás (fix Z-BASE (d) pendiente).
- Validación viva con ArchiCAD pendiente desde múltiples sesiones.

## Decisiones tomadas

- Cerrar sesión siguiendo el procedimiento del vault (mapa-conocimiento.md).
- No ejecutar cambios de código en esta sesión; solo registro y consolidación.

## Cómo se resolvieron los problemas

- No se resolvieron problemas de código esta sesión; se documentaron todos los pendientes para la próxima sesión.

## Lecciones aprendidas

- El procedimiento de cierre del vault requiere: diario (60-diario/), lecciones (50-lecciones/), memoria de proyecto (memory/), y backup final (backup_projects.ps1 -Real).
- Siempre documentar variables de nuevas acciones del Orquestador para no perder trazabilidad entre sesiones.

## Pendientes de esta sesión

- Ninguno.

## Pendientes de sesiones anteriores (no resueltos)

Ver lista completa en 60-diario/2026-10-27.md. Incluye: conectar 9 entradas v10, corregir type hints F3_DISTRIBUCION_v03.py, re-embebido #198 canvas v13.5, validación viva ArchiCAD, crear 8 stories + StorySync --check, limpieza tests desactualizados.

## Próxima sesión

Reanudar con: corregir type hints en F3_DISTRIBUCION_v03.py, conectar entradas v10 al canvas, ejecutar validación viva con ArchiCAD (F3_StorySync_v02.py --plan --chip AAA0030JKOE).
