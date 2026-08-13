# gh-definitions — Definiciones Grasshopper

## Vigentes (raíz)

| Archivo | Rol |
|---|---|
| `F1_Contexto_Base-Editado_v00.gh` / `.ghx` | **Canvas maestro** de Fase 1 (2026-08-13) |
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
- Todo cambio de canvas debe versionarse y documentarse en el vault (`10-arquitectura\guia-integracion-ghx-v25.md`).
