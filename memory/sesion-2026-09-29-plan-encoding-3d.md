# Sesión 2026-09-29 — Plan de corrección de raíz: encoding + 3D vecinos/envolvente

## Encargo del operador (post corrida canvas v11, GH+ArchiCAD)
1. `#21` ETAPA1 v04.2: `UnicodeDecodeError` ('ó' = 0xF3 cp1252) leyendo `data/pot-cache/CHIP-contexto.json`.
2. Polilíneas de predios vecinos y envolvente del lote solo visibles/utilizables a nivel 0.0 (nodos 2D de la Live Connection).
3. Autoriza canvas nuevo "si es necesario"; pide **plan de raíz** desarrollado/presentado con el esquema del skill `council` (marketplace ECC; el operador lo llama "claude-council").

## Hallazgos verificados (2026-09-29)
- `CHIP-contexto.json`: UTF-8 válido, sin byte 0xF3, mtime 09-28 20:22; escaneo de `data/` (123 JSON): **0 problemas**. Error no reproducible en frío → clase de fallo latente (decodes estrictos fragmentarios; mezcla de codepages en el toolchain).
- **Evidencia viva de fragilidad**: la extracción de hoy falló al imprimir '→' (U+2192) con consola cp1252 → `UnicodeEncodeError: 'charmap' …`.
- Código embebido del canvas == src `F1_ETAPA1_CONTEXTO_v04.2.py` (byte-idéntico, len 16 709). Canvas v11: 319 objetos.
- **Live Connection**: NO existe nodo "3D Polyline"; SÍ existen **"Morph Curve"** (morph no sólido desde curva 3D), **"Morph Solid"** (mesh → sólido) y **"Mesh"** (fuente: `C:\Program Files\Rhino 8\Plug-ins\Grasshopper\ArchicadConnection.gha`). Restricción 2D: "It must be a planar curve"/"horizontal plane".
- `F1_ETAPA1_CONTEXTO_v05` (bandas drapeadas) test 6/6 re-corrido OK; `z_base` v01d embebido en v11; NORMATIVA v08 embebida.
- Anclas GUID para parches: `#21 0d986a36-a41a-429c-8f29-9e2658659e25`; `#113 d4aab682-ad94-40e9-a5b5-eaf20b3350c7`; `#48 ad270c61-3268-4dcc-b9e8-dd6e9711f5c8`; rewire `#125 cb180da5-4884-4861-9c9f-a5a74020ed62`. Plantilla: `scripts/utilities/patch-ghx-v11-fixes-2026-09-28.py`; regenera `.gh` con `scripts/utilities/ghx-to-gh.ps1`.
- Inventario lectores/escritores de JSON en componentes embebidos: ETAPA1 (ReadAllText UTF8→Default), CONTEXTO50_BUILD (utf-8→latin-1), EXPORTAR_GFA (utf-8-sig; escribe utf-8 `ensure_ascii=False`), PATIO (`_escribir_json_utf8`), LAYERS (io.open utf-8), F0 (utf-8), fetch v7 (`ensure_ascii=False`). → escritores/lectores heterogéneos (raíz del riesgo).

## Consejo
- Convocado: voces escéptica / pragmática / crítica (subagentes `consejo-esceptico`, `consejo-pragmatico`, `consejo-critico`) + Arquitecto (posición inicial en anexos). **Síntesis pendiente.**

## Entregables en curso
- `docs/planes/2026-09-29-plan-correccion-encoding-3d/` → `DIAGNOSTICO-Y-PLAN.md` + `anexos/` (componentes v11, scripts embebidos, ETAPA1 embebido, nodos LC disponibles, posición del Arquitecto).

## Cierre 2026-09-29 (ejecución P0+P1 offline, mismo día)

- **P0 ejecutado**: lector canónico (utf-8 estricto → cp1252 → latin-1, avisos ruidosos) en `v04.3` / `v01e` / `v02.5` / `v01.5` / `v02.3` + política de escritura ASCII-safe + utilidad `verificar-codificacion-json.py` (tests 8/8; scan `data` 123 archivos / 0 problemas). Embebido en `F1_CONTEXTO_v11.ghx` (5 CodeInput anclados por nickname/GUID; validación 5/5; backup `.bak-20260929-194159`; `.gh` regenerado).
- **P1 ejecutado**: `F1_CONTEXTO_v12.ghx/.gh` = v11 parcheado + rama 3D: comps `F1_ETAPA1_CONTEXTO_3D_v01` (bandas + curvas 3D + terreno + toggles) y `F1_ETAPA2_ENVOLVENTE_3D_v01` (curva/banda/**volumen** para movimiento de tierra); nodos LC `MC1/MC2/MC3` (Morph Curve), `MS1/MS2` (Morph Solid), `M1` (Mesh), toggles `T1/T2/T3`. Verificación: 330 objetos, 0 duplicados de chunk, 0 GUIDs duplicados, 0 fuentes sin resolver, 20/20 cables OK, conversión y round-trip GH_IO OK. Scripts: `patch-ghx-v11-encoding-2026-09-29.py`, `build-ghx-v12-2026-09-29.py`, plantillas en `scripts/utilities/lc_templates/`.
- **Evidencia raíz**: error del operador **reproducido exacto** bajo IronPython 2.7 de Rhino 8 (decode estricto de cp1252 `Consolidación`: `'unknown' codec … byte 0xf3 … at index 11`).
- **Docs**: `docs/planes/2026-09-29-plan-correccion-encoding-3d/` → `DIAGNOSTICO-Y-PLAN.md`, `EJECUCION-P0-P1.md`, `EJECUCION-Y-RUNBOOK.md`, anexos (consejo, verificación v12, guids, componentes, scan).
- **Pendiente**: ventana viva (cerrar AutoClaw; runbook listo) + cola P3 (NORMATIVA v09, datasets mix B, aviso GFA, barrido ETAPA3/LADOS/LAYERS, binding de capas de morphs).
- Suites finales: raíz **326/326** · fase-1 **56/56** · utilidad **8/8**.
