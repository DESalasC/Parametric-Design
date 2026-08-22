# Instrucciones del operador — 2026-08-21

Documento para que el operador avance en paralelo mientras el agente trabaja en el código.
Cubre: Bloque B (GFA en Rhino + validación F2) y los pasos manuales del Bloque A (canvas).

---

## BLOQUE B — Deuda de datos (parte manual del operador)

### B1. Regenerar el GFA en Rhino/Grasshopper

**Contexto del problema:** el GFA actual exportado es `826.58 m²`, pero el valor de
referencia previo es `1186.87 m²`. Además se detectaron anomalías: LADOS reportó
"0 lados / 0 vecinos", antejardín aplicado como default 3.0 m y ausencia de lado
posterior. Hay que regenerar y verificar.

**Pre-requisitos:**
1. Rhino 8 abierto, unidades en **METROS** (nunca mm).
2. Sesión de Rhino con el **lote** cargado.
3. El JSON de contexto debe existir:
   `data/pot-cache/AAA0127AZPA-contexto.json`.
   Si no existe, generarlo primero:
   ```
   python scripts\utilities\fetch-urban-context-v6.py --chip AAA0127AZPA
   ```

**Pasos (canvas maestro `gh-definitions/F1_Contexto_Base-Editado_v02.gh`):**

1. Abrir el canvas `F1_Contexto_Base-Editado_v02.gh`.
2. En `F0_LOAD_PROYECTO_v01`, verificar que `chip` = `AAA0127AZPA`
   (si usas el `proyecto.json`, revisa ese campo; si usas inputs sueltos, fíjalo a mano).
3. **ETAPA1 — `F1_ETAPA1_CONTEXTO_v02`:** confirmar que `json_path` apunta a
   `data\pot-cache\AAA0127AZPA-contexto.json` (mismo panel que alimenta ETAPA1).
   Verificar que las salidas NO están vacías: `lot_curve`, `vias_oficiales`
   (deberían ser ~42), `vecinos_curves`, `espacios_publicos` (~12).
   → **Si `vias_oficiales` o `vecinos_curves` salen vacías, aquí está la causa raíz
   de "0 lados": la geometría no llega a LADOS.**
4. **ETAPA2 — `F1_ETAPA2_LADOS_v06`:** entradas geométricas con **type hint = Curve,
   List Access, Flatten** (regla 15b del CLAUDE.md). Revisar la salida
   `sides_table_json`: debe listar **4 lados** clasificados (Frontal / Lateral / Posterior).
   → Si aparecen "0 lados", el problema es de cableado/tipo en las curvas de entrada.
5. **ETAPA2 — `F1_ETAPA2_PATIO_v02`:** verificar `patio_count` y `patios_curves`.
6. **ETAPA2 — `F1_ETAPA2_NORMATIVA_v08`:** revisar `envelope_curve`, `gfa_total`,
   `ocupacion_real`, `pisos_finales`.
7. **`F1_EXPORTAR_GFA_v02`:** conectar `json_path` al MISMO panel de ETAPA1 y las
   salidas de NORMATIVA (`gfa_total`, `ocupacion_real`, `io_maximo`, `ic_real`,
   `ic_maximo`, `altura_total`, `pisos_finales`, `valido`, `mensaje`, `flag_pipeline`).
   Al resolver, escribe automáticamente `data\fase-2-demanda\AAA0127AZPA-gfa-gh.json`
   (campo clave: `gfa_total_m2`).
8. Abrir ese JSON y comparar `gfa_total_m2` contra la referencia `1186.87 m²`.

**Anomalías a revisar (checklist):**
- **"0 lados / 0 vecinos"** → paso 3 y 4: geometría no llega a LADOS. Verificar
  type hint `Curve` + `List Access` + `Flatten` en las entradas geométricas.
- **Antejardín 3.0 m fijo** → si `antejardin_m = 0` debería derivar de reglamentación;
  si NORMATIVA aplica 3.0 fijo, es porque no hay lado `Frontal` clasificado
  (consecuencia del punto anterior). Se resuelve al corregir LADOS.
- **Sin lado posterior** → verificar que el lote tiene 4 lados y que el posterior se
  clasifica con la regla "Posterior N-1" (CLAUDE.md).

### B2. Validar `pago_parcial_pct` (F2) contra un caso real

**Motor:** `src\fase-2-demanda\F2_Modelo_Financiero\F2_DEMANDA_MOTOR_v03.py`

**Semántica:** `pago_parcial_pct` es el **% del valor del lote (CL) pagado en efectivo
al dueño**; el resto se aporta en especie con participación. Es el inverso de
`fraccion_aporte_pct`. `pago_parcial_pct = 40` ⇒ dueño recibe 40% en efectivo y aporta
el 60% en especie. Prima sobre `fraccion_aporte_pct`.

**Pasos:**
1. Definir el caso real: CHIP, valor del lote (`cl_compra`), y el % en efectivo acordado.
2. Ejecutar (flag CLI `--pago-parcial`):
   ```
   cd src\fase-2-demanda\F2_Modelo_Financiero
   python F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_mercado2026.json --pago-parcial 40
   ```
   (También puedes fijar `aporte_suelo.pago_parcial_pct` dentro del JSON de parámetros.)
3. Revisar en el resultado:
   - `pct_min` / `pct_max` / `roi_max_dev` (se recalculan sobre `ub_equity = ub_nl - cl_compra`).
   - `flujo_caja_estimado` (debe mantenerse consistente).
   - `ub_nl` vs `ub_equity`: la participación del socio debe bajar al pasar de aporte total
     a pago parcial.
4. Contrastar contra la expectativa real del negocio y reportar si es coherente.

---

## BLOQUE A — Pasos manuales en el canvas (lo que solo puede hacerse en Rhino)

El código de los scripts ya es compatible; lo que falta es el cableado visual en el canvas.
Hazlo después de B1 (sobre el mismo canvas).

### A1. Corregir type hints de #211 y #207

- **#211 (Morph Settings de `F3_MORPH_ATRIBUTOS_v01`)** y **#207 (F0_STORIES)**:
  cambiar el type hint de sus inputs de **Layer/Story a `Text`**.
  Esto resuelve el error `Data conversion failed Text→Layer / Text→Story`.
- Procedimiento: clic derecho sobre el input → `Type hint` → `Text` (String).

### A2. Cablear `layers_json` (F3) → `F1_LAYERS_XML_v02`

- Salida `layers_json` de `F3_MORPH_ATRIBUTOS_v01` (JSON de capas distintas, formato
  `[{"nombre","color","visible"},...]`) → conectar a la entrada **`json_text`** de
  `F1_LAYERS_XML_v02`.
- Alternativa: guardar `layers_json` a un archivo y apuntar la entrada **`json_path`**
  de `F1_LAYERS_XML_v02` a ese archivo.
- Resultado: `F1_LAYERS_XML_v02` genera el XML de capas (GuBIMclass) de los morphs
  ANTES de crearlos.

### A3. Cablear `usos_pisos` (F3) → `pisos` (F3_MORPH_ATRIBUTOS)

- Salida `usos_pisos` de `F3_VOLUM_GENERADOR_v08` (piso por volumen, 1:1 con
  `volumenes_por_uso`) → conectar a la entrada **`pisos`** de `F3_MORPH_ATRIBUTOS_v01`.
- Resultado: cada morph recibe el número de piso correcto para el atributo Story.
