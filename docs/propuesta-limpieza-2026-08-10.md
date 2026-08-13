# Propuesta de Limpieza — Versiones Obsoletas

**Fecha:** 2026-08-10
**Acción requerida:** Aprobación del usuario para eliminar/mover archivos

---

## Resumen

El proyecto acumula ~50 archivos de versiones antiguas que dificultan la navegación
y generan ruido en git (`??` untracked). Se propone eliminar lo obsoleto y conservar
solo las versiones vigentes documentadas.

---

## Archivos a ELIMINAR

### scripts/utilities/ — Versiones antiguas de fetch-urban-context

| Archivo | Motivo |
|---------|--------|
| `fetch-urban-context.py` | Versión original, reemplazada por v5 |
| `fetch-urban-context.py.backup` | Backup redundante |
| `fetch-urban-context-1.py` | Rama experimental |
| `fetch-urban-context-v1.py` | Obsoleta |
| `fetch-urban-context-v2.py` | Obsoleta |
| `fetch-urban-context-v3.py` | Obsoleta |
| `fetch-urban-context-v4.py` | Obsoleta |
| `fetch-urban-context-v6.py` | Obsoleta (v5 es la vigente) |
| `fetch-urban-context-v7.py` | Obsoleta |
| `fetch-urban-context-v8.py` | Obsoleta |
| `fetch-urban-context-v9.py` | Obsoleta |

### scripts/utilities/ — Versiones antiguas de normativa

| Archivo | Motivo |
|---------|--------|
| `F1_NORMATIVA_APLICAR_v01.py` al `v15.py` | La v22 en src/ es la vigente |
| `F1_NORMATIVA_APLICAR_v21.py` | Reemplazada por v22 |
| `F1_NORMATIVA_LEER_v01.py`, `v06.py`, `v08.py`, `v09.py` | La v10 en src/ es la vigente |

### scripts/utilities/ — Otras versiones obsoletas

| Archivo | Motivo |
|---------|--------|
| `gpkg-to-cache.py`, `v2.py`, `v3.py` | La v4 es la vigente |
| `fetch-aerial-photo-v1.py` al `v5.py` | La v6 es la vigente |
| `generate-archicad-layers-xml-v1.py`, `v2.py` | La v3 es la vigente |
| `setup_archicad_layers_v01.py` | Reemplazada por F0_SETUP_BIM_Layers.py |
| `test_nemotron_tooluse.py` | Test exploratorio, no del pipeline |

### gh-definitions/ — Herramientas de fix_ghx

| Archivo | Motivo |
|---------|--------|
| `fix_ghx_v3.py` al `v9.py` | Solo v10 se usa; el resto son iteraciones abandonadas |
| `_check_*.py`, `_dump_*.py`, `_find_*.py`, `_list_*.py`, `_test_*.py` | Scripts de diagnóstico puntual, ya cumplieron su propósito |

---

## Archivos a CONSERVAR

| Archivo | Versión vigente | Ubicación |
|---------|----------------|-----------|
| fetch-urban-context | **v5** | scripts/utilities/ |
| gpkg-to-cache | **v4** | scripts/utilities/ |
| fetch-aerial-photo | **v6** | scripts/utilities/ |
| generate-archicad-layers-xml | **v3** | scripts/utilities/ |
| fix_ghx | **v10** | gh-definitions/ |
| F1_CONTEXTO_POT | **v04** (sistema) | src/fase-1-contexto/ |
| F1_LADOS_CONFIGURAR | **v07** | src/fase-1-contexto/ |
| F1_NORMATIVA_APLICAR | **v22** | src/fase-1-contexto/ |
| F1_PATIO_DISCONTINUIDAD | **v02** | src/fase-1-contexto/ |

---

## Impacto

- **Archivos a eliminar:** ~50 archivos (~400 KB)
- **Archivos conservados:** ~25 scripts vigentes
- **Riesgo:** Ninguno — las versiones eliminadas son dead code confirmado
- **Recuperabilidad:** Los archivos están en git history (commiteados) o son untracked

---

## Instrucciones (tras aprobación)

```powershell
cd D:\Work\PROJECTS\DiseñoParametrico

# Eliminar versiones obsoletas de scripts/utilities/
Remove-Item scripts\utilities\fetch-urban-context.py -Force
Remove-Item scripts\utilities\fetch-urban-context.py.backup -Force
Remove-Item scripts\utilities\fetch-urban-context-1.py -Force
Remove-Item scripts\utilities\fetch-urban-context-v[1-4].py -Force
Remove-Item scripts\utilities\fetch-urban-context-v[6-9].py -Force
Remove-Item scripts\utilities\F1_NORMATIVA_APLICAR_v0[1-9].py -Force
Remove-Item scripts\utilities\F1_NORMATIVA_APLICAR_v1[0-5].py -Force
Remove-Item scripts\utilities\F1_NORMATIVA_APLICAR_v21.py -Force
Remove-Item scripts\utilities\F1_NORMATIVA_LEER_v0[1-9].py -Force
Remove-Item scripts\utilities\gpkg-to-cache.py -Force
Remove-Item scripts\utilities\gpkg-to-cache-v[2-3].py -Force
Remove-Item scripts\utilities\fetch-aerial-photo-v[1-5].py -Force
Remove-Item scripts\utilities\generate-archicad-layers-xml-v[1-2].py -Force
Remove-Item scripts\utilities\setup_archicad_layers_v01.py -Force
Remove-Item scripts\utilities\test_nemotron_tooluse.py -Force

# Eliminar fix_ghx obsoletos y scripts de diagnóstico
Remove-Item gh-definitions\fix_ghx_v[3-9].py -Force
Remove-Item gh-definitions\_check_*.py -Force
Remove-Item gh-definitions\_dump_*.py -Force
Remove-Item gh-definitions\_find_*.py -Force
Remove-Item gh-definitions\_list_*.py -Force
Remove-Item gh-definitions\_test_*.py -Force
Remove-Item gh-definitions\_compare_*.py -Force
Remove-Item gh-definitions\_extract_*.py -Force

# Commit
git add -A
git commit -m "chore: eliminar versiones obsoletas de scripts (~50 archivos)"
```
