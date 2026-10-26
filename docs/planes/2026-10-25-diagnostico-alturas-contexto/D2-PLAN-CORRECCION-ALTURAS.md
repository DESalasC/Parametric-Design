# D2 — Plan de corrección de alturas contexto/lote

**Proyecto:** DiseñoParamétrico · F1/F3
**Fecha:** 2026-10-25
**Base:** `D1-DIAGNOSTICO-COTAS-CONTEXTO.md`
**Objetivo:** que el contexto 3D, las capas de referencia y los volúmenes F3 apoyen en la misma superficie de terreno que el lote, sin offsets globales ni flotaciones locales.

**Criterio de aceptación (medible):**
1. `z_origen` de #201 recibe 0,0 (no −14,488).
2. Los volúmenes vecinos no se separan del terreno más de **±0,50 m** en el 90 % de las huellas y **±1,00 m** en el 100 %.
3. Vías y espacios públicos apoyan sobre el terreno (ningún vértice a más de 0,50 m de la superficie) o se decide explícitamente que no se envían a ArchiCAD.
4. Censo ArchiCAD: 20/20 zonas y 8/8 niveles tras corrida limpia.

---

## Opción A — Verificación de cableado y corrida limpia (inmediata, sin código)

**Qué:** confirmar en Grasshopper que la entrada `z_origin` de `#201-F3_VOLUM_GENERADOR` esté cableada a la salida **`z_origen`** de `#45` (que vale 0,0) y **no** a `desplazamiento_z` (que vale −14,488).

**Condiciones:** Rhino + Grasshopper + ArchiCAD abiertos en el orden acordado; canvas v13.6 recargado.

**Limitaciones:** no corrige la flotación local de vecinos ni las vías planas; solo descarta el error de 14,5 m.

**Resultado esperado:** si el síntoma era “todo el contexto 14,5 m abajo/arriba”, desaparece al reconectar. Si el síntoma persiste, el problema es local (opciones B/C).

**Esfuerzo:** 10 min. **Riesgo:** nulo.

---

## Opción B — Muestreo MDT por huella (datos, recomendada)

**Qué:** en `scripts/utilities/anclar_contexto50_zbase.py`, muestrear el MDT en el centroide **y en los vértices de cada huella**; guardar `z_base_m` (centroide, compatibilidad), `z_base_min_m`, `z_base_max_m` y `z_base_metodo`. Usar `z_base_min_m` para apoyar el volumen (criterio “apoya en la cota más baja de su huella”).

**Condiciones:** acceso REST al MDT de Catastro (ya usado por el script); lote de ~90 edificios × 5–10 puntos.

**Limitaciones:**
- Más peticiones (≈ 450–900). Hay que respetar 429/Retry-After y ejecutar por lotes.
- El MDT es una superficie estimada; no sustituye levantamiento.
- Cambia la cota de los volúmenes existentes: requiere corrida limpia y censo.

**Resultado esperado:** residuo de vecinos dentro de ±1 m (hoy hasta 4,17 m), sin flotación visible en pendiente.

**Esfuerzo:** 1–2 h + corrida. **Riesgo:** medio (depende de red y del servicio).

---

## Opción C — Drape de vías y espacios públicos (datos + geometría)

**Qué:** muestrear el MDT en los vértices de vías/EP o recortar la referencia a un radio de 50 m y drapear solo esa ventana. Alternativa mínima: excluir vías/EP del envío a ArchiCAD y dejarlos como referencia 2D en Rhino.

**Condiciones:** si se drapea completo, hace falta MDT para ~6 200 vértices; si se recorta, se pierde la lectura de vías lejanas (Avenida de Los Cerros, etc.).

**Limitaciones:**
- La malla de ETAPA1 no sirve: cubre solo el lote + ~5 m.
- Drapear con IDW local extrapola y produce cotas falsas.

**Resultado esperado:** contexto de referencia apoyado en terreno, sin líneas atravesando el lote.

**Esfuerzo:** 2–4 h. **Riesgo:** medio-alto (volumen de datos y criterio de recorte).

---

## Secuencia recomendada

1. **A hoy:** verificar cableado `z_origen` (0,0) y hacer corrida limpia con censo 20/20 + `F3_StorySync_v02 --check` 8/8. Esto separa el error global del local.
2. **B después:** implementar muestreo por huella y re-anclar el contexto50. Repetir censo y medir residuos con `diagnosticar-cotas-contexto.py`.
3. **C al final:** decidir si vías/EP se drapean o se excluyen del envío a ArchiCAD; documentar la decisión.

## No hacer

- No volver a embeber `src` desde una copia vieja: la paridad ya está sincronizada (7/7) y `z_origen` debe quedar en 0,0.
- No cambiar el puerto de Live Connection: el work-around es el orden de arranque (AutoClaw → ArchiCAD → Rhino), que deja la conexión en 19724.
- No mover el origen del canvas ni el vértice SE: el datum cierra a 0,4 mm.
