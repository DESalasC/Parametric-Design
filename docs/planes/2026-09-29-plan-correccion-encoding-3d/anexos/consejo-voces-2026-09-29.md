# Consejo — posiciones crudas (2026-09-29)

Esquema: skill `council` (marketplace ECC). Cuatro voces; síntesis en [../DIAGNOSTICO-Y-PLAN.md](../DIAGNOSTICO-Y-PLAN.md) §1. (Posición del Arquitecto redactada ANTES de leer las voces externas: ver `arquitecto-posicion-inicial.md`.)

---

## Arquitecto (posición inicial, en sesión)

**Posición:** canvas **v12 incremental** desde v11 (preservar lo validado; añadir 3D + lecturas robustas; NO reformulación total; NO parche mínimo dentro del v11). Para (A): doble blindaje — escritores seguros + lectores con cascada sobre bytes (y utilidad de reparación/tests). Para (B): bandas → Morph Solid; envolvente 3D; `topo_mesh` al nodo Mesh; cadenas 2D intactas.
**Razones:** (1) v11 a medio validar; (2) material para v12 ya probado offline (v05 bandas 6/6); (3) la reformulación total reintroduce riesgo sin ganancia.
**Riesgo principal:** coexistencia temporal de dos canvases → mitigación con nomenclatura, un runbook y v11 congelado como fallback.

---

## Voz Escéptica (subagente: `consejo-esceptico`)

**Posición:** un canvas, sin bifurcar. Hacer A) robusto y ruidoso en v11; B) como refactor ADITIVO en v11 con contrato nulo y fixtures.
**Razonamiento:**
- Un canvas nuevo no protege un byte; el bug de encoding es de E/S (lectores/escritores), no de topología.
- .ghx + anclaje por GUID + bak convierten la reformulación en algo barato de hacer *in situ*; "canvas nuevo" suena más limpio que "in situ", no demuestra serlo.
- Snapshot del archivo no captura el entorno que produjo el archivo (locale, PowerShell, hooks)…
**Riesgo:** releer solo `Consolidación` normalizado con un fixture nunca demuestra la desnormalización real (el bug era de *escritura*, no de lectura).
**Sorprendente:** el error del operador (byte `0xF3` pos. 11) es *fragmentario*, no de archivo completo: cazar primero si algún valor corto (p. ej. `tratamiento`) se codifica en cp1252 al escribirse — y hacer que el fallback **jamás sea silencioso** (mojibake peor que crash).

## Voz Pragmática (subagente: `consejo-pragmatico`)

**Posición:** do it now: A) parche en v11 (corregir lectores con fallback + avisos y estandarizar escritores) **ya**; B) en paralelo, script nuevo v12 SOLO con la rama 3D (curvas + bandas + toggles), importando lo ya probado.
**Razonamiento:**
- Editar `CodeInput` no mueve GUIDs ni layout: cero riesgo de topología para v11. Añadir nodos allí sí mueve numeración → mantener el ábol 3D en v12 y re-anclar con GUIDs.
- Vuelca v05 (bandas 6/6) como comp 3D slim + envolvente v08.1 + `topo_mesh`; conserva 2D intacto. Meshes pesados por toggles; envío por lotes.
- **Una sola corrida viva**: junta la re-validación de v11+A y B en un único recomputo con checklist y rollback ya probado.
**Riesgo:** dos canvases derivan en silencio si no congelas YA v11 (solo fixes de encoding) y no difunde un runbook único **y** las pruebas clave deben ser del REP de la LC: que 65 muestras drapeadas + malla + morph no escalen en tiempo/peso → medir con el chip B.
**Sorprendente:** el byte `0xF3` es una `ó` en **cp1252**, no UTF-8: haz la caza del residuo ya (offline) con una utilidad `verify-json-encoding` que recorra `data/pot-cache` y **escriba log** — probablemente ya no hay residuo, y el fallback de lectura lo esté tapando.

## Voz Crítica (subagente: `consejo-critico`)

**Posición:** v12 = copia de v11 (post-A) + rama 3D; ejecutable, con validaciones intermedias y rollback probado; **A antes que B**.
**Razonamiento:**
- v11 a medias: un canvas nuevo permite construir/validar offline; pero ensambla EDITANDO el .ghx y **preservando GUIDs de parámetros**; verifica en el diff y regenera `.gh`.
- El fallo de encoding no está reproducible (¿algún **PowerShell 5.1** `Set-Content/Out-File` escribió ANSI?): trampa típica PS5.1 → `Set-Content` ANSI (por eso "funciona" hoy y falla mañana). En A: escritura con `[IO.File]::WriteAllText(... UTF8)` o `-Encoding utf8` en PS7; y "conversión" de legados con log.
- IDW en bordes de lote inclinado puede extrapolar (no hay muestras): clampa z al rango de muestras cercanas o añade ε de margen; y valida que 65 muestras + 90 vecinos no degraden LC: si pesa, throttling.
**Riesgo:** que el error de encoding no esté — y el fix "cure" un síntoma equivocado: mete un **modo verbose con log a disco** durante la sesión viva (sin AutoClaw no hay consola) y reproduce con un fixture de línea cp1252 antes de dar A por cerrado.
**Sorprendente:** el toque de "reformular todos los componentes" es una trampa de alcance/riesgo: si el problema de A) es del **escritor**, reescribir todo el canvas no lo arregla pero multiplica la superficie de fallos.

---

## Síntesis del consejo (veredicto)

- **Consenso:** A offline ya, in-place en v11 (solo CodeInput); cascada ruidosa + escritor único + utilidad + fixture; UNA sesión viva con checklist/rollback; no reformular todo.
- **Disidencia más fuerte:** Escéptico (no abrir canvas nuevo); adoptada en parte (A sin bifurcar; B con v12 MÍNIMO por seguridad del fallback).
- **Premisas cuestionadas:** "el canvas nuevo no protege un byte" ✓; "el bug puede ser del escritor (PS5.1)" → adoptado (política de escritura + búsqueda de residuos offline con utilidad).
- **Cambio de recomendación del Arquitecto:** sí — "v12 incremental amplio" → "A in-place en v11 + v12 mínimo solo-3D + única sesión viva" (convergencia Pragmático/Crítico).
