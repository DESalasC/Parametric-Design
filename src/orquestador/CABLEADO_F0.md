# CABLEADO — F0_LOAD_PROYECTO_v01 → componentes del canvas

Versión: 2026-08-18 (v01.3) · Fuente: cabeceras ENTRADAS/SALIDAS de los scripts
vigentes (`F1_ETAPA1_CONTEXTO_v02`, `F1_ETAPA2_LADOS_v06`, `F1_ETAPA2_PATIO_v02`,
`F1_ETAPA2_NORMATIVA_v08`, `F1_OVERRIDE_USO_v01`, `F1_EXPORTAR_GFA_v02`,
`F3_DISTRIBUCION_v01`, `F3_VOLUM_GENERADOR_v07`, `F3_ACCESOS_INTEGRADOR_v02`).

## 1. Salidas de F0_LOAD_PROYECTO_v01 (v01.3)

| Salida | Tipo | Default |
|---|---|---|
| `chip` | str | `""` |
| `tipologia` | str | `"Continua"` |
| `piso_adicional` | bool | `False` |
| `tipo_bonificacion` | str | `"NINGUNO"` (normalizado) |
| `floor_height_user` | num | `3.0` |
| `antejardin_decision` | str | `"Según reglamentación"` (UI hint) |
| `antejardin_m` | num | `0.0` (0 = deriva de reglamentación) |
| `voladizo_frontal_m` | num | `0.0` (0 = deriva del perfil vial) |
| `empate_posterior_pisos` | num | `0` (independiente) |
| `empate_posterior_m` | num | `None` (independiente) |
| `empate_posterior_entrepiso_m` | num | `0.0` (derivado = m / pisos) |
| `tratamiento` | str | `"Consolidación"` |
| `caso` | str | `"A"` |
| `alineacion_nucleo` | num | `1` |
| `usos` | list | `[]` |
| `modos` | list | `[]` |
| `escenarios` | list | `[]` |
| `vecinos_por_lado_json` | str | `""` (JSON `{id_lado:[altura_m,...]}`) |
| `ok` | bool | `False` |
| `log` | str | `""` |

## 2. Cableado directo (dentro de Grasshopper)

| F0 salida | Componente destino | Input destino | Nota |
|---|---|---|---|
| `tipologia` | F1_ETAPA2_NORMATIVA_v08 | `tipologia` | directo (String) |
| `floor_height_user` | F1_ETAPA2_NORMATIVA_v08 | `floor_height_user` | directo (Number) |
| `floor_height_user` | F3_VOLUM_GENERADOR_v07 | `floor_height` | misma salida a 2 destinos |
| `piso_adicional` | F1_ETAPA2_NORMATIVA_v08 | `piso_adicional` | directo (Boolean) |
| `tipo_bonificacion` | F1_ETAPA2_NORMATIVA_v08 | `tipo_bonificacion` | ya normalizado ("NINGUNO"/"EQUIPAMIENTO"/"VIS") |
| `tratamiento` | F1_ETAPA2_NORMATIVA_v08 | `tratamiento` | directo (String) |
| `antejardin_m` | F1_ETAPA2_NORMATIVA_v08 | `antejardin_m` | directo (Number; 0 = deriva) |
| `voladizo_frontal_m` | F1_ETAPA2_NORMATIVA_v08 | `voladizo_frontal_m` | directo (Number; 0 = deriva) |
| `empate_posterior_pisos` | F1_ETAPA2_NORMATIVA_v08 | `empate_posterior_pisos` | directo (Number, ≥3 activa empate) |
| `alineacion_nucleo` | F3_VOLUM_GENERADOR_v07 | `alineacion_nucleo` | directo (0/1/2, default 1) |
| `vecinos_por_lado_json` | F1_ETAPA2_NORMATIVA_v08 | `vecinos_por_lado_json` | directo (String JSON; empate lateral por lado) |

## 3. Cableado indirecto / compuesto

| F0 salida | Destino | Cómo |
|---|---|---|
| `chip` | F1_ETAPA1_CONTEXTO_v02 → `json_path` | componer ruta `<CHIP>-contexto.json` (Path/Concat) |
| `chip` | F1_EXPORTAR_GFA_v02 → `json_path` | mismo criterio |
| `caso` | F3_DISTRIBUCION_v01 (CLI) | `python F3_DISTRIBUCION_v01.py <CASO_ID>` |

## 4. Salidas sin consumidor directo en el canvas (diagnóstico / uso futuro)

| Salida | Uso |
|---|---|
| `empate_posterior_m` | Altura total del edificio vecino posterior (independiente). No lo consume NORMATIVA; se usa para derivar `empate_posterior_entrepiso_m`. |
| `empate_posterior_entrepiso_m` | Entrepiso del vecino posterior = `empate_posterior_m / empate_posterior_pisos` (solo si se dan ambos). Reservado para validar contra NRS-10 más adelante. |
| `antejardin_decision` | Pista de UI (select); el override real es `antejardin_m`. |
| `usos` / `modos` / `escenarios` | Consumidos por F2 (CLI). En Grasshopper, informativos (Panel). |
| `ok` / `log` | Diagnóstico (Panel). |

## 5. Componentes que NO reciben salidas de F0

| Componente | Entradas reales | Origen |
|---|---|---|
| F1_ETAPA1_CONTEXTO_v02 | `json_path` | ruta derivada de `chip` |
| F1_ETAPA2_LADOS_v06 | `lot_vertices`, `vias_curves`, `ep_curves`, `vecinos_curves`, `andenes_curves`, tol/contacto | geometría |
| F1_ETAPA2_PATIO_v02 | `lot_vertices`, `sides_table_json`, `altura_max_pot` | geometría + LADOS + CONTEXTO |
| F1_EXPORTAR_GFA_v02 | `area_envelope`, `gfa_total`, `ocupacion_real`, `io_maximo`, `ic_real`, `ic_maximo`, `altura_total`, `pisos_finales`, `valido`, `mensaje`, `flag_pipeline`, `output_path`, `json_path` | salidas NORMATIVA + OVERRIDE_USO |
| F3_VOLUM_GENERADOR_v07 (resto) | `envelope_por_piso`, `envelope_curve`, `json_path`, `salida_morph` | salidas NORMATIVA + `programa-areas.json` (CLI) |
| F3_ACCESOS_INTEGRADOR_v02 | `layout_espacial.json`, `matriz_adyacencias.json`, `sides` | archivos F3_DISTRIBUCION + LADOS (CLI) |

## 6. Observaciones (resueltas en v01.2)

1. **`antejardin_decision` (select) → override numérico `antejardin_m`.** "Según
   reglamentación" = 0 (deriva); "Aumentar antejardín" = fijar `antejardin_m`;
   "Disminuir voladizo" = fijar `voladizo_frontal_m`. Ambos Number se cablean a
   NORMATIVA_v08.
2. **`empate_posterior_pisos` y `empate_posterior_m` son INDEPENDIENTES.**
   Corresponden al edificio vecino posterior (proyecto existente), sin relación
   con `floor_height_user` del proyecto actual. No se convierten entre sí; pueden
   darse uno, otro o ambos. `empate_posterior_entrepiso_m = m / pisos` (derivado)
   queda disponible para validar contra NRS-10.
3. **`tipo_bonificacion` normalizado** al vocabulario NORMATIVA
   ("Ninguno"→"NINGUNO", "Servicios"→"EQUIPAMIENTO", "VIS"→"VIS").
4. **Empate lateral por lado (v01.3):** `vecinos_por_lado_json` sale de
   `proyecto.json['vecinos_por_lado']` (lo llena el formulario del orquestador con
   la altura de cada vecino colindante por lado). Se convierte al formato
   NORMATIVA `{id_lado: [altura_m, ...]}` (id_lado = índice de segmento); NORMATIVA
   lo aplica solo a lados `Lateral`. Lados `via`/`espacio_publico`/`libre` no
   generan empate.

## 7. Resumen visual del flujo

```
F0_LOAD_PROYECTO_v01 (v01.2)
├─ tipologia ──────────────► F1_ETAPA2_NORMATIVA_v08.tipologia
├─ floor_height_user ──────► F1_ETAPA2_NORMATIVA_v08.floor_height_user
│                           └► F3_VOLUM_GENERADOR_v07.floor_height
├─ piso_adicional ─────────► F1_ETAPA2_NORMATIVA_v08.piso_adicional
├─ tipo_bonificacion ──────► F1_ETAPA2_NORMATIVA_v08.tipo_bonificacion
├─ tratamiento ────────────► F1_ETAPA2_NORMATIVA_v08.tratamiento
├─ antejardin_m ───────────► F1_ETAPA2_NORMATIVA_v08.antejardin_m
├─ voladizo_frontal_m ─────► F1_ETAPA2_NORMATIVA_v08.voladizo_frontal_m
├─ empate_posterior_pisos ─► F1_ETAPA2_NORMATIVA_v08.empate_posterior_pisos
├─ alineacion_nucleo ──────► F3_VOLUM_GENERADOR_v07.alineacion_nucleo
├─ chip ───────────────────► (ruta) F1_ETAPA1_CONTEXTO_v02.json_path
│                           └► (ruta) F1_EXPORTAR_GFA_v02.json_path
├─ caso ───────────────────► (CLI) F3_DISTRIBUCION_v01 <CASO_ID>
├─ usos / modos / escenarios► (CLI) F2 + F3_DISTRIBUCION
└─ vecinos_por_lado_json ── F1_ETAPA2_NORMATIVA_v08.vecinos_por_lado_json
├─ empate_posterior_m ─────► (deriva) empate_posterior_entrepiso_m  [NRS-10 futuro]
└─ antejardin_decision / ok / log ─► UI hint / diagnóstico
```
