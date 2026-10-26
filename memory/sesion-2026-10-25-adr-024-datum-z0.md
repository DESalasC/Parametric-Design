---
fecha: 2026-10-25
tipo: memoria_proyecto
proyecto: DiseñoParamétrico
sesion: 2026-10-25 (noche)
tags: [memoria, sesion, adr-024, datum-z0, archicad, niveles]
---

# Memoria de sesión — DiseñoParamétrico 2026-10-25 (noche)

## Situación encontrada al iniciar
- El usuario solicitó establecer como convención de construcción el punto más bajo del predio (o centro del lindero contra la vía) como cota `{z=0}` para todos los cálculos de niveles.
- Debe haber una opción en el orquestador para que el operador defina un punto `{z=0}` local arbitrario.
- En ArchiCAD, el primer nivel (Ground Floor) siempre debe ser 0.
- Se recibió como "retry" de una solicitud previa no aún respondida.

## Acciones realizadas
1. **ADR-024 registrado:** regla del datum Z0 y normalización de ArchiCAD (`Z_ac = Z_modelo − zgf_m`, GF = 0,000).
2. **Creado `scripts/utilities/calcular_z0_proyecto.py`:** cálculo del datum por modo `min_lote` / `centro_lindero_via` / `manual`.
3. **Modificado `src/orquestador/run_pipeline_v01.py`:** CLI `--z0-modo/--z0-valor/--z0-absoluto`; paso automático de cálculo y persistencia.
4. **Modificado `src/interfases-archicad/F3_StorySync_v02.py`:** `plan_stories(..., zgf_m)` con GF = 0,000; CLI `--zgf-m`; hoja del operador dinámica.
5. **Modificado `CLAUDE.md`:** sección ADR-024.
6. **Verificación:** `py_compile` OK; orquestador ejecutado con caso B → `z0_m = 0.2661` (min_lote) persistido; StorySync verificado con `zgf-m=2.92` → GF @ 0.000 m.

## Decisiones tomadas
- Datum default: `min_lote` (vértice más bajo del polígono del lote).
- `z0_m` se escribe en `data/pot-cache/<CHIP>-z0.json` y se persiste en `parametros_pipeline.json`.
- Ground Floor = 0,000 en ArchiCAD independientemente del datum de cálculo.

## Lecciones aprendidas (esta sesión)
- Al parsear stdout de subprocesos en Windows, leer el archivo JSON escrito en disco en lugar del stdout (evita bytes contaminados / codepage).
- `F3_StorySync_v02` necesita `zgf_m` como entrada explícita para normalizar stories a GF = 0.

## Puntos pendientes de esta sesión
1. Validación viva con ArchiCAD: crear niveles con `F3_StorySync_v02 --plan --zgf-m` y verificar con `--check` (0 faltantes).
2. Conectar `zgf_m` al canvas: `F3_VOLUM_GENERADOR` expone `z_gf` y aplica `−zgf_m` a morphs/zonas (ruta AC solo).
3. Front-end del orquestador: selector de datum y muestra de `z0_m`, `zgf_m`, grilla AC.

## Puntos pendientes heredados (sin resolver)
- Corrida limpia + censo 20/20 zonas en ArchiCAD.
- `F3_StorySync_v02 --check` 8/8 niveles.
- Drape o exclusión de vías/EP (opción C).
- Validación viva caso B; puerto 19723 (portproxy); estación (mantenimiento/WebView2); F4/F5; Gates PC-2/PC-3/PC-4.

## Archivos clave generados/modificados
- Creado: `scripts/utilities/calcular_z0_proyecto.py`
- Creado: `D:\Work\NOTES\obsidian-vault\10-arquitectura\decisiones-adr\adr-024-datum-z0-y-normalizacion-ac.md`
- Creado: `D:\Work\NOTES\obsidian-vault\10-arquitectura\decisiones-adr\2026-10-25-acta-sesion-cierre-adr-024.md`
- Modificado: `src/orquestador/run_pipeline_v01.py`, `src/interfases-archicad/F3_StorySync_v02.py`, `CLAUDE.md`, `60-diario\2026-10-25.md`
- Generado (datos): `data/pot-cache/AAA0030JKOE-z0.json`, `src/orquestador/parametros_pipeline.json`, `niveles_deseados.json` (prueba)
