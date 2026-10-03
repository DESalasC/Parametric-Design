# PLAN DE ACCIÓN — Tope de Ocupación (IO) sobre Canvas v13
**Proyecto:** DiseñoParamétrico | **Canvas base:** `F1_CONTEXTO_v13.ghx` | **Fecha:** 2026-10-03 (actualizado con progreso)
**Objetivo:** Cambiar el área de ocupación de los volúmenes generados para que quede **≤ IO reglamentario (≤ area_lote × io_maximo)**.  
**Entregable:** Plan de acción para desarrollo, **aprobado** (en ejecución).

---

## 1. RESUMEN EJECUTIVO

### 1.1 Problema
El caso **La Candelaria** (CHIP `AAA0030JKOE`, lote ≈ 946,34 m², tratamiento **Consolidación**, IO máx **0,70**) tiene una **ocupación actual de 936,56 m²** (IO real **0,9897**) frente a un techo reglamentario de **662,44 m²**. Excedente: **274,12 m²**. La validación normativa (NORMATIVA v08.5.2) **reporta** el exceso y emite `NO VALIDADO`, pero la **generación no lo impone**.

### 1.2 Dirección aprobada
Reducir la ocupación mediante **"barras por crujía"** (2–3 volúmenes/barras escalonadas de crujía única), **no** recortando patios de esquina. Separar **distribuidor** y **validador**. Devolver **GFA aprobado** a Fase 2. Mantener `normativa_confirmada=False` y exportación apagada hasta validar.

### 1.3 Reglas clave aplicadas
| Decisión | Valor |
|---|---|
| **D1** Canvas | v13.1 (parche in-place) |
| **D2** Entrepiso | Adaptativo: 3.05 m si separación → 15.25 m; 3.80 m si → 19.00 m |
| **D3** Prioridad ajuste | Profundidad → Entrepiso → Nº cuerpos |
| **D4** Margen IO | Estricto 0.70 (tolerancia técnica 0.0001) |
| **D5** Versiones | Homogeneizadas: archivo = versión interna |
| **D6** Export GFA | Solo `gfa_aprobado` |
| **D7** IC | Confrontar con decretos en etapa posterior |

---

## 2. ESTADO DE IMPLEMENTACIÓN (2026-10-03 15:10)

| Fase | Componente | Versión | Estado | Archivo |
|---|---|---|---|---|
| **P0** | NORMATIVA v09 (validador + presupuesto + barras_json) | v09.0 | ✅ **Completado** | `src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v09.py` |
| **P0** | Tests NORMATIVA v09 | — | ✅ Escritos (stub Rhino pendiente) | `tests/test_normativa_v09_fuente.py` |
| **P1** | F3_DISTRIBUCION v03 (distribuidor barras) | v03.0 | ✅ **Completado** | `src/fase-3-masa/F3_DISTRIBUCION_v03.py` |
| **P2** | F1_EXPORTAR_GFA v02.4 (solo gfa_aprobado) | v02.4 | ✅ **Completado** | `src/fase-1-contexto/F1_EXPORTAR_GFA_v02.4.py` |
| **P2** | run_pipeline v01.1 (loop barras IO) | v01.1 | ✅ **Completado** | `src/orquestador/run_pipeline_v01.py` |
| **P3** | Canvas v13.1 (parche) | v13.1 | ⏳ **Pendiente** | `gh-definitions/F1_CONTEXTO_v13.1.ghx` |
| **P3** | LADOS v06.8 (fix altura 0 confirmada) | v06.8 | ⏳ **Pendiente** | `src/fase-1-contexto/F1_ETAPA2_LADOS_v06.py` |
| **P3** | PATIO v03.3 (doc patios/separaciones) | v03.3 | ⏳ **Pendiente** | `src/fase-1-contexto/F1_ETAPA2_PATIO_v03.py` |
| **P4** | Validación offline completa | — | ⏳ **Pendiente** | Suite tests + casos A/B/B_SALUD/C |
| **P4** | Validación viva (Rhino/GH/ArchiCAD) | — | ⏳ **Pendiente** (puerto 19723 OK) | Runbook §6.3 |

---

## 3. PRÓXIMOS PASOS INMEDIATOS

### P3 — Canvas v13.1 + LADOS v06.8 + PATIO v03.3
1. **Canvas v13.1**: Parche in-place de `F1_CONTEXTO_v13.ghx` → `v13.1.ghx`/`.gh`:
   - Añadir entrada `barras_json` a NORMATIVA v09
   - Cablear salida `presupuesto_ocupacion_m2` visible
   - Slider/selector `n_barras_objetivo` (2/3/AUTO)
   - Cablear `envelope_aprobado_por_piso` → F3 (reemplaza `envelope_por_piso` potencial)
   - Homogeneizar versiones embebidas (v09.0, v03.3, v06.8, v02.4)
2. **LADOS v06.8**: Implementar fix "altura 0 confirmada (patio vecino) vs desconocida" + validar que el orquestador procese alturas 0 en linderos coincidentes con predio.
3. **PATIO v03.3**: Actualizar docstring/mensajes: patio = iluminación/ventilación (1 vol) **o** separaciones entre volúmenes (≥2 vol) que computan en IO; advertencia si `io_real > io_maximo`.

### P4 — Validación
1. **Offline**: Suite completa `pytest tests/ -x -q` + casos A/B/B_SALUD/C vía `run_pipeline_v01.py --run --yes`
2. **Viva** (puerto 19723 confirmado funcionando):
   - Cargar canvas v13.1 → Chip AAA0030JKOE → NORMATIVA v09 → capturar `presupuesto_ocupacion_m2`
   - Ejecutar F3_DISTRIBUCION_v03 `--presupuesto-ocupacion <valor> --n-barras 2,3 --entrepiso-adaptativo`
   - Re-ejecutar NORMATIVA v09 con `barras_json` → `valido=True`, `io_real ≤ 0.70`, `gfa_aprobado_m2 > 0`
   - Exportar GFA APROBADO (F1_EXPORTAR_GFA_v02.4) → verificar `modo=APROBADO`, `gfa_aprobado_m2`
   - Visualizar 3D: `envelope_aprobado_por_piso` + Morphs vecinos + `topo_mesh` + linderos 3D
   - F2 motores leen `gfa_aprobado_m2` → UI sección 2 ↔ 4 acoplada

---

## 4. ARCHIVOS CLAVE GENERADOS ESTA SESIÓN

| Archivo | Descripción |
|---|---|
| `F1_ETAPA2_NORMATIVA_v09.py` | Validador IO + presupuesto + entrada `barras_json` + salidas aprobadas |
| `F3_DISTRIBUCION_v03.py` | Distribuidor barras con presupuesto IO, entrepiso adaptativo 3.05/3.80, prioridad D3 |
| `F1_EXPORTAR_GFA_v02.4.py` | Exportador GFA APROBADO (solo `gfa_aprobado_m2` en modo APROBADO) |
| `run_pipeline_v01.py` v01.1 | Orquestador con loop barras IO (P2): F3_BARRAS → NORMATIVA v09 + barras_json → EXPORT APROBADO |
| `test_normativa_v09_fuente.py` | Tests validador (modo POTENCIAL, APROBADO, RECHAZADO, presupuesto expuesto) |
| `PLAN-ACCION-TOPE-OCUPACION-v13.md` | Este plan actualizado |

---

## 5. COMANDOS DE REFERENCIA RÁPIDA

```powershell
# Tests NORMATIVA v09 (requiere stub Rhino completo para boolean ops)
python tests/test_normativa_v09_fuente.py

# Pipeline completo La Candelaria con loop barras IO
python src/orquestador/run_pipeline_v01.py --chip AAA0030JKOE --caso B --modo mixto --run --yes

# Solo estado
python src/orquestador/run_pipeline_v01.py --status --chip AAA0030JKOE --caso B --modo mixto

# Checklist visual
python src/orquestador/run_pipeline_v01.py --checklist --chip AAA0030JKOE --caso B --modo mixto

# F3 Distribuidor barras standalone
python src/fase-3-masa/F3_DISTRIBUCION_v03.py --caso B --presupuesto-ocupacion 662.44 --n-barras 2,3 --entrepiso-adaptativo True
```

---

## 6. NOTAS TÉCNICAS PENDIENTES

1. **Stub Rhino.Geometry**: Tests unitarios fallan por `CreateBooleanUnion/Difference` no implementados en `stub_rhino_min.py`. Requiere stub completo o validación en Rhino real.
2. **Profundidad barras**: `F3_DISTRIBUCION_v03.py` usa modelo rectangular simplificado. En producción debe consumir `envelope_por_piso` real de NORMATIVA v09 y ajustar geometría al lote real (OBB/shapely).
3. **IC (índice de construcción)**: Pendiente confrontar con Decreto 466/2024 Anexo 5 §1.13; si existe tope, añadir validación `gfa_aprobado ≤ ic_maximo_m2`.
4. **Versiones internas**: Verificar que todos los scripts embebidos en canvas v13.1 tengan versión interna = nombre archivo (v09.0, v03.3, v06.8, v02.4).

---

*Plan en ejecución. P0, P1, P2 completados. Siguiente: P3 (Canvas v13.1 + LADOS v06.8 + PATIO v03.3).*