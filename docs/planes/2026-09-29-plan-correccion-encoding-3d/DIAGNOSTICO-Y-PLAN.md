# Diagnóstico y plan — Corrección de raíz: codificación JSON + 3D de contexto

- **Fecha:** 2026-09-29
- **Ámbito:** canvas `F1_CONTEXTO` (v11 → v12), proyecto DiseñoParametrico; chip de trabajo B (`AAA0030JKOE`).
- **Estado:** ✅ **P0 (blindaje de codificación) y P1 (canvas v12, rama 3D) ejecutados OFFLINE y validados**. ⏳ Validación viva pendiente (requiere cerrar AutoClaw — conflicto del puerto 19723).
- **Esquema de decisión:** skill `council` (marketplace ECC; el operador lo refirió como "claude-council"): cuatro voces (Arquitecto + Escéptico + Pragmático + Crítico).
- **Ejecución detallada:** [EJECUCION-P0-P1.md](EJECUCION-P0-P1.md) · **Ventana viva:** [EJECUCION-Y-RUNBOOK.md](EJECUCION-Y-RUNBOOK.md) · **Voces crudas:** [anexos/consejo-voces-2026-09-29.md](anexos/consejo-voces-2026-09-29.md).

---

## 0. Resumen ejecutivo

| # | Problema observado | Causa raíz verificada | Solución ejecutada |
|---|---|---|---|
| 1 | `#21 ETAPA1 | ERROR al leer JSON: [UnicodeDecodeError] 'unknown' codec can't decode byte 0xf3 in position 11 …` leyendo `data/pot-cache/CHIP-contexto.json` | Decodificación **estricta UTF-8** aplicada a contenido **cp1252** (la 'ó' = byte `0xF3` en posición 11) dentro de la cadena IronPython/.NET; toolchain con escritores/lectores de codificación heterogénea. **Error reproducido exactamente** bajo el IronPython 2.7 de Rhino 8 (ver §2.1). | **Lector canónico** (cascada `utf-8 → cp1252 → latin-1`, avisos ruidosos, error con hex) en todos los componentes de E/S + política de escritura (UTF-8 explícito / ASCII-safe) + utilidad de verificación/reparación + tests con fixture `0xF3`. Embebido en el canvas v11 (P0). |
| 2 | Las polilíneas de predios vecinos y la envolvente **solo se ven a nivel 0.0** en ArchiCAD (solo en planta) | Los nodos **"2D Polyline"** de la Live Connection solo admiten curvas **planas horizontales**; no existía ninguna representación 3D (y la malla del terreno quedaba huérfana). | **Canvas v12 (rama 3D mínima):** curvas 3D drapeadas → **Morph Curve**; bandas drapeadas → **Morph Solid**; terreno → nodo **Mesh**; envolvente → curva + banda + **volumen** (movimiento de tierra) con **toggles**. Verificado contra la biblioteca LC: **no existe** nodo "3D Polyline"; **sí** existen "Morph Curve", "Morph Solid" y "Mesh". |

> **Dato de raíz:** una corrida de este mismo turno reprodujo la **misma familia de fallo en vivo** (un `print` de `→` con consola cp1252 lanzó `UnicodeEncodeError: 'charmap'`). El blindaje cubre ambos sentidos (lectura y escritura/impresión).

---

## 1. Consejo — veredicto (resumen; voces crudas en anexos)

- **Arquitecto (sesión):** v12 incremental + doble blindaje de codificación + bandas → Morphs. *Preservar lo validado y convertir trabajo ya probado en valor.*
- **Escéptico:** un solo canvas, sin bifurcar. *"Un canvas nuevo no protege un byte": el bug es de E/S, no de topología.*
- **Pragmático:** A en v11 **in-place** (editar CodeInput no mueve GUIDs) + **v12 mínimo solo-3D**; **una única** corrida viva combinada. *Tres corridas = tres interrupciones del operador.*
- **Crítico:** v12 incremental con **v11 congelado**; A antes que B; avisos ruidosos; vigilar escritores PowerShell, bordes del IDW y peso de Morphs; **logs a disco** en la ventana viva; rollback probado.

**Veredicto:**
- **Consenso:** (1) blindaje de codificación ya, offline, en v11 (solo CodeInput; sin cambios de topología); (2) cascada de lectura **ruidosa** + escritor único con UTF-8 explícito + utilidad de verificación/reparación + tests con fixture 0xF3; (3) **una sola** sesión viva con checklist y rollback; (4) cazar residuos offline, nunca en la validación; (5) **no** reformular todo.
- **Disidencia más fuerte (Escéptico):** no abrir canvas nuevo. Adoptada en parte: para (A) nada se bifurca — todo va en v11. Para (B) se mantiene un **v12 mínimo** porque añadir nodos a un canvas a medio validar mezcla regresiones con lo nuevo y degrada el fallback.
- **Chequeo de premisas:** "un canvas nuevo no protege un byte" — correcto; por eso (A) va en v11. "¿Hace falta canvas nuevo?" — no para reformular; sí uno mínimo para la rama 3D que la LC 2D no puede representar.
- **Cambio de recomendación (explícito):** de "v12 incremental con varios frentes" → **"A in-place en v11 + v12 mínimo solo-rama-3D + una única sesión viva"** (convergencia Pragmático/Crítico; el Escéptico forzó que A no espere al canvas nuevo).

**Decisiones del operador (2026-09-29):** ① ejecutar P0 ya — SÍ; ② ruta v12 mínimo — SÍ; ③ ambas representaciones 3D **con toggles** — SÍ; ④ **volumen** de envolvente útil para movimiento de tierra — incluido; ⑤ ventana viva: cuando P0/P1 estén validados offline.

---

## 2. T1 — Codificación (raíz)

### 2.1 Evidencia (reproducción exacta)

Bajo el runtime IronPython 2.7 de Rhino 8 (ensamblados `IronPython.dll` / `netcore`, 2026-09-29), decodificar en **UTF-8 estricto** los bytes cp1252 del valor `"Consolidación"` (ó en índice 11):

```text
bb = System.Text.Encoding.GetEncoding(1252).GetBytes(u"Consolidación"); bb[11] -> 0xF3
System.Text.UTF8Encoding(False, True).GetString(bb)
=> UnicodeDecodeError: 'unknown' codec can't decode byte 0xf3 in position 11:
   Unable to translate bytes [F3] at index 11 from specified code page to Unicode.
```

Firma **idéntica** al error del operador (incluido el formato híbrido `'unknown' codec` propio de IronPython/.NET). El archivo actual ya está en UTF-8 válido: **residuo latente** de desnormalización, no corrupción actual.

### 2.2 Inventario (pre-fix)

- **Lectores:** ETAPA1 (`ReadAllText` UTF8→Default), CONTEXTO50_BUILD/ETAPA3 (`utf-8 → latin-1`), PATIO (flag con `json.load` binario), GFA (`utf-8-sig`), F0 (`open(..., encoding="utf-8")` estricto), LAYERS (string de entrada).
- **Escritores:** mezcla de `ensure_ascii=False` (fetch v7, servidor, GFA, PATIO) + PowerShell + copias manuales ⇒ riesgo cruzado.

### 2.3 Solución implementada (P0)

1. **Lector canónico** `_leer_json_canonico(ruta)`: bytes → `utf-8 estricto (con/sin BOM)` → `cp1252` → `latin-1`; **aviso ruidoso** `[AVISO ENCODING]` si no fue UTF-8; si todo falla, error con **primeros 24 bytes en hex**. Aplicado a: `F1_ETAPA1_CONTEXTO_v04.3`, `F1_CONTEXTO50_BUILD_v01e`, `F1_ETAPA2_PATIO_v02` (v02.5), `F0_LOAD_PROYECTO_v01` (v01.5), `F1_EXPORTAR_GFA_v02.3`.
2. **Política de escritura:** un solo escritor por archivo; `encoding="utf-8"` explícito en cada apertura; JSON de `pot-cache`/pipeline en **ASCII-safe** (`ensure_ascii=True`, equivalentes); nunca defaults ANSI.
3. **Utilidad** `scripts/utilities/verificar-codificacion-json.py` (escaneo + `--aplicar` con backup y reescritura atómica; `--ascii` opcional) + reporte en anexos. Corrida real: **123 archivos `data/`, 0 problemas** (guardián permanente).
4. **Tests** `test_lector_canonico.py`: fixture cp1252 con `0xF3` (valores tipo "Consolidación"/"Clasificación"), BOM, basura con error hex, inexistente, y **aviso obligatorio** en el fallback.

> Nota: ETAPA3, LADOS y LAYERS quedan **sin cambios** (no leen archivos críticos / contrato estable); pasan a la cola P3 del barrido.

---

## 3. T2 — 3D (raíz)

### 3.1 Hechos verificados de la Live Connection (fuente: `ArchicadConnection.gha` + canvas v11)

- **No existe** el nodo "3D Polyline" (0 coincidencias en la biblioteca).
- **Sí existen:** **"Morph Curve"** (*non-solid Morph defined by a 3D Curve*), **"Morph Solid"** (*solid Morph defined by a mesh*), **"Mesh"** (terreno por puntos + boundary) y el resto de la familia Morph/Settings/Layer.
- Restricciones 2D confirmadas en los binarios: *"Invalid Curve value. It must be a planar curve / horizontal plane"*.

### 3.2 Canvas v12 — rama 3D mínima (11 nodos nuevos)

| Nodo nuevo | Función | Cableado |
|---|---|---|
| `F1_ETAPA1_CONTEXTO_3D_v01.py` | Lee el mismo JSON; emite bandas + **curvas 3D drapeadas** + terreno (topo_pts/boundary) | `json_path ←` mismo File Path del #21; los 2 toggles |
| `F1_ETAPA2_ENVOLVENTE_3D_v01.py` | Envolvente → curva 3D + banda + **volumen** (movimiento de tierra) | `envelope_curve`/`altura_total ← #113`; `topo_pts ←` comp. 3D; 3 toggles |
| `MC1/2/3` Morph Curve | Perímetro 3D de **lote / vecinos / envolvente** | ← curvas del comp. 3D y de ENVOLVENTE |
| `MS1` Morph Solid | Cintas drapeadas de contexto (lote+vecinos+vías+EP) | ← `bandas_todas` |
| `MS2` Morph Solid | Volumen de envolvente | ← `volumen_3d` |
| `M1` Mesh | Malla de terreno (deja de estar huérfana) | ← `topo_pts` + `topo_boundary` |
| `T1/T2/T3` Boolean Toggles | **mostrar curvas (ON) / cintas (ON) / volumen (OFF)** | → gates de ambos componentes |

- Componentes existentes (#21/#48/#99/#89/#10) **conservan contrato**; las cadenas 2D quedan intactas (clasificación manual).
- **Capa de los Morphs:** en v12.0 se crean sin `Morph Settings` cableado (igual que el flujo vigente del #74); la asignación fina de capa por nodo requiere referencia viva de ArchiCAD y queda para la ventana viva (1 min) o después.

---

## 4. Ejecución (resumen; detalle y comandos en EJECUCION-P0-P1.md)

- **Canvas v11 (P0):** parche por GUID/ancla → CodeInput de 5 componentes al día (`#21 v04.3`, `#48 v01e`, `#99 v02.5`, `#89 v01.5`, `#10 v02.3`), validación de marcadores **5/5 OK**, backup `F1_CONTEXTO_v11.ghx.bak-20260929-194159`, `.gh` regenerado (159.696 B).
- **Canvas v12 (P1):** ensamblado por script desde el v11 parcheado con **11 nodos nuevos** → **330 objetos**, **0 duplicados de chunk**, **0 GUIDs duplicados**, **0 fuentes sin resolver**, **verificación de cableado 20/20 OK**, conversión `.ghx→.gh` **OK** (177.378 B) y **round-trip `.gh→.ghx` OK** (GH_IO lee el resultado).
- **Suites:** raíz **326/326**, fase-1 **56/56**, utilidad **8/8**.
- **Artefactos:** `gh-definitions/F1_CONTEXTO_v11.ghx/.gh` (blindado) · `gh-definitions/F1_CONTEXTO_v12.ghx/.gh` (rama 3D) · scripts de parche/ensamblado en `scripts/utilities/` · plantillas LC en `scripts/utilities/lc_templates/`.

---

## 5. Verificación viva (P2) — pendiente

Sigue el runbook [EJECUCION-Y-RUNBOOK.md](EJECUCION-Y-RUNBOOK.md): **cerrar AutoClaw**, abrir `F1_CONTEXTO_v12.gh`, recomputar con flags, verificar mensajes sin rojos, exports (GFA + lados/patio) → `6/6`, y en ArchiCAD: curvas 3D / cintas / terreno visibles y seleccionables, toggles funcionando, volumen según T3. Logs a disco durante la sesión; rollback = volver a v11 (backup listo).

## 6. Cola (P3)

- NORMATIVA v09 (Candelaria) · datasets mix vigentes de B · aviso de antigüedad GFA en F2 · barrido de codificación en ETAPA3/LADOS/LAYERS · retirar parche viejo (`patch-ghx-contexto50-defensiva.py`) · binding de capas para los morphs 3D en vivo.
