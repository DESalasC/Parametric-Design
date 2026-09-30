# Ejecución P0 + P1 — 2026-09-29 (offline)

Ejecuta el plan [DIAGNOSTICO-Y-PLAN.md](DIAGNOSTICO-Y-PLAN.md) aprobado por el operador (respuestas 1–5 del 2026-09-29). Todo corrido **offline** (sin Rhino/ArchiCAD abiertos, sin tocar la ventana viva).

---

## A. Entregables técnicos

### A1. Código fuente (nuevo / actualizado)

| Archivo | Cambio | Evidencia |
|---|---|---|
| `src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.3.py` | Lector canónico + BOM + avisos; salidas idénticas a v04.2 | incluido en canvas v11 ✓ |
| `src/fase-1-contexto/F1_ETAPA1_CONTEXTO_3D_v01.py` | **Nuevo**: bandas + curvas 3D drapeadas (IDW) + terreno + toggles | tests `test_etapa1_3d_v01.py` |
| `src/fase-1-contexto/F1_ETAPA2_ENVOLVENTE_3D_v01.py` | **Nuevo**: envolvente → curva/banda/volumen (prisma por malla, sin `rg.Extrusion`) | tests `test_envolvente_3d_v01.py` |
| `src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01e.py` | Lector canónico (cascada) | suite contexto50 ✓ |
| `src/fase-1-contexto/F1_ETAPA2_PATIO_v02.py` (v02.5) | Lectura de flag con cascada + escritura ASCII-safe | suite fase-1 ✓ |
| `src/fase-1-contexto/F1_EXPORTAR_GFA_v02.3.py` | Cascada en `leer_flag`/`derivar_chip` + escritura ASCII-safe | suite raíz ✓ |
| `src/orquestador/F0_LOAD_PROYECTO_v01.py` (v01.5) | Lector canónico **dual** (IronPython/CPython) | tests F0 ✓ |

### A2. Utilidad + gobernanza

- `scripts/utilities/verificar-codificacion-json.py` (escaneo/reparación; `--aplicar`, `--ascii`, `--reporte`) + `tests/test_verificar_codificacion_json.py` (**8/8**).
- Corrida real: `data` + `docs` → **125 archivos JSON, 0 problemas** (reporte en `anexos/scan-codificacion-2026-09-29.txt`).
- Tests del lector: `src/fase-1-contexto/tests/test_lector_canonico.py` (fixture `0xF3`, BOM, basura→hex, inexistente).

### A3. Canvas

- `gh-definitions/F1_CONTEXTO_v11.ghx/.gh` — **P0**: CodeInput de `#21/#48/#99/#89/#10` actualizados (validación de marcadores 5/5 OK; backup `.bak-20260929-194159`; `.gh` regenerado 159.696 B).
- `gh-definitions/F1_CONTEXTO_v12.ghx/.gh` — **P1**: 11 nodos nuevos (comps 3D/ENVOLVENTE + 3 Morph Curve + 2 Morph Solid + 1 Mesh + 3 toggles). Verificación: **330 objetos**, **0 duplicados de chunk**, **0 GUIDs duplicados**, **0 fuentes sin resolver**, **20/20 cables OK**, conversiones `.ghx→.gh` y round-trip `.gh→.ghx` **OK**.
- Scripts: `scripts/utilities/patch-ghx-v11-encoding-2026-09-29.py` · `scripts/utilities/build-ghx-v12-2026-09-29.py` · plantillas serializadas en `scripts/utilities/lc_templates/`.

---

## B. Comandos (reproducibles)

```powershell
# P0: parche v11 + regeneración
.\.venv\Scripts\python.exe scripts\utilities\patch-ghx-v11-encoding-2026-09-29.py
pwsh -NoProfile -File scripts\utilities\ghx-to-gh.ps1 -InputGhx gh-definitions/F1_CONTEXTO_v11.ghx -OutputGh gh-definitions/F1_CONTEXTO_v11.gh -Force

# P1: ensamblado v12 + regeneración
.\.venv\Scripts\python.exe scripts\utilities\build-ghx-v12-2026-09-29.py
pwsh -NoProfile -File scripts\utilities\ghx-to-gh.ps1 -InputGhx gh-definitions/F1_CONTEXTO_v12.ghx -OutputGh gh-definitions/F1_CONTEXTO_v12.gh -Force

# Suites
.\.venv\Scripts\python.exe -m pytest tests -q                    # 326/326
.\.venv\Scripts\python.exe -m pytest src\fase-1-contexto\tests -q  # 56/56

# Guardián de codificación
.\.venv\Scripts\python.exe scripts\utilities\verificar-codificacion-json.py --roots data docs
```

---

## C. Desviaciones (con justificación)

1. **Envolvente:** componente dedicado `F1_ETAPA2_ENVOLVENTE_3D_v01` en lugar de "NORMATIVA v08.1" — no toca el contrato validado de NORMATIVA v08 y aísla el código nuevo testeable.
2. **Contexto 3D:** componente slim `F1_ETAPA1_CONTEXTO_3D_v01` en lugar de reemplazar `#21` por v05 (completa) — preserva el contrato del #21 validado; `v05` queda como referencia offline-testeada.
3. **GFA** quedó como `v02.3` (subversión interna; antes de la corrida el nombre era `_v02.py`). Refs actualizables en docs menores.
4. **Morphs sin `Morph Settings` cableado** (capa fina) — igual que el flujo vigente (`#74`); la asignación de capa requiere referencia viva de ArchiCAD → ventana viva/manual.
5. **`duplicados hermano` de tipo item** (ID/InputId/OutputId): presentes también en el documento base (322) y tolerados por GH_IO; el criterio de aceptación usa solo duplicados de **chunk** (0).

## D. Pendientes / siguiente

- **Ventana viva (P2)** según [EJECUCION-Y-RUNBOOK.md](EJECUCION-Y-RUNBOOK.md).
- Cola P3 (NORMATIVA v09, datasets mix, aviso GFA, barrido ETAPA3/LADOS/LAYERS, retirar parche viejo, binding de capas).
- Actualizar referencias a `F1_EXPORTAR_GFA_v02` → `v02.3` donde aplique.
