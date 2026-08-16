# gh-definitions — Definiciones Grasshopper

## Vigentes (raíz)

| Archivo | Rol |
|---|---|
| `F1_Contexto_Base-Editado_v01.gh` / `.ghx` | **Canvas maestro** de Fase 1 (renombrado de v00 por el usuario el 2026-08-15; validado 2026-08-15: `F1_ETAPA2_NORMATIVA_v04` + `F1_EXPORTAR_GFA_v02` cargados, rango de pisos corregido con Value List entre comillas) |
| `DiseñoParametrico_BaseConexiones.ghx` | Referencia de conexiones del canvas |
| `test_panel.ghx` / `.json` | Panel de prueba / referencia de componentes |

## Archivo histórico

`_archive\` conserva **todas** las versiones anteriores (F1_Contexto v00–v09, Proyecto Raven
Rev01–03B, Componentes básicos Rev00–02, Canvas_DisenoP_Rev05, backups, JSON de diagnóstico) y
`_archive\_tools\` las herramientas de conversión/fix (`fix_ghx_v10.py`, `upgrade_v06_to_v07.py`,
`compare_containers.py`, `fix_contexto_v04.py`, `Fix-Ghx.ps1`). **No usar** los archivos de
`_archive\` en definiciones nuevas; están solo como referencia e historial.

## Reglas

- Unidades en **metros**; lotes como polilíneas; GHPython con componente "Script" (IronPython 2.7).
- Pipeline del canvas: ETAPA1_CONTEXTO_v01 → ETAPA2_LADOS_v02 → ETAPA2_PATIO_v02 →
  ETAPA2_NORMATIVA_v04 → (OVERRIDE_USO_v01) → EXPORTAR_GFA_v02 → `data/fase-2-demanda/<CHIP>-gfa-gh.json`.
- Todo cambio de canvas debe versionarse y documentarse en el vault (`10-arquitectura\guia-integracion-ghx-v26.md`).
