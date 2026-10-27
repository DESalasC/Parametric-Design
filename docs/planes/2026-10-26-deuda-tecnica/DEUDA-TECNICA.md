# Deuda técnica — DiseñoParamétrico (registro 2026-10-26)

Regla del proyecto: un fallo "preexistente" **no** se archiva para excusarlo; se
registra con causa y corrección, y se cierra. Este documento se actualiza cada vez
que se cierra un ítem.

**Estado de la suite:** inicio de la sesión **10 fallos** → cierre **0 fallos**
(`457 pasan / 0 fallan`).

---

## Cerrados en la sesión del 2026-10-26

| # | Ítem | Causa | Corrección aplicada |
|---|------|-------|---------------------|
| A1 | `run_pipeline_v01.py --checklist` lanzaba `KeyError: ' --ok'` | el CSS `:root { --ok:… }` se procesaba con `str.format()` | la plantilla se rellena por reemplazo directo (`{chip}`→valor), no con `.format()`; verificado generando `checklist.html` |
| B1 | `test_lados_v06_fuente::test_mensaje_v06` | el test fijaba «LADOS v06.5» y el componente es v06.8 | literal actualizado |
| B2 | `test_lados_v06_fuente::test_prefijo_error_v06` | idem | literal actualizado |
| B3 | `test_esquina_fuente::test_lados_esquina_anula_posterior` | exigía el comentario «CORRECCION ESQUINA» | ahora verifica el comportamiento: `idx_posterior = None` dentro del bloque `if es_esquina:` |
| B4 | `test_morph_atributos_fuente::…json_path…` | el componente pasó a `output_path` | test reescrito al contrato vigente |
| B5 | `test_normativa_v09_fuente::test_modo_potencial_sin_barras` | el test validaba `F1_ETAPA2_NORMATIVA_v09.py`, pero el canvas corre **v09.1**; además el mensaje NO VALIDADO no declaraba el modo | test apuntado a v09.1; el mensaje ahora dice `NORMATIVA v09.1 \| POTENCIAL \| NO VALIDADO …`; presupuesto esperado corregido a 596,40 m² (0,70 × 852 m² del fixture) |
| B6 | `test_orquestador::test_detectar_estado_estructura` | el set de pasos quedó viejo (v01.1 + pasos nuevos) | set actualizado a los 13 pasos reales |
| A2a | `test_storysync_v02_plan` (2) | los tests ignoraban ADR-024 (GF=0 en ArchiCAD) | reescritos al marco ADR-024: `base_z_m`=0, `zgf_m`=cota del GF, `elevation`=elevación ArchiCAD |

## Cerrado también: A2b (planificador único)
- **StorySync es canónico.** `F3_VOLUM_GENERADOR_v08._plan_stories` pasó a emitir el
  esquema ADR-024 idéntico (`elevation` en marco ArchiCAD con GF=0, `zgf_m`,
  `elevacion_modelo_m`) y el JSON exportado incluye `zgf_m`. Re-embebido #201, paridad 7/7.
- Tests: `test_paridad_plan_con_storysync_v02` y `test_export_flag_escribe_stories_y_apaga_flag`
  actualizados al marco ADR-024.
- **Consecuencia:** `niveles_deseados.json` de `casos/AAA0030JKOE` está en marco antiguo
  (base −11,565, sin `zgf_m`): **hay que regenerarlo** con `F3_StorySync_v02 --plan` tras la
  corrida del canvas con las cotas nuevas (v03.10). El alzado lo detecta y lo dice.

---

## Pendientes operativos (cierre de fase, no son tests)

1. Re-ejecutar el canvas (contexto #45, zonas #200/#201) y **censar 20/20 zonas** en ArchiCAD.
2. Re-exportar `exports/contexto50/AAA0030JKOE-contexto50.3dm` (el actual quedó con los
   71 morphs a +14,4875 m).
3. **Drape o exclusión de vías/EP** (opción C): ETAPA1 publica vías/EP/vecinos con z=0;
   el diagnóstico de cotas lo marca como FALLA.
4. `F3_StorySync_v02 --check` → 8/8 niveles; validación viva caso B.
5. Regenerar el plan de stories tras el cambio de cota de arranque de los bloques (v03.10).
6. Correr el canvas con el flag de LADOS encendido (ya dejado por el generador del alzado)
   para tener `<CHIP>-lados.json` como fuente única de linderos.
