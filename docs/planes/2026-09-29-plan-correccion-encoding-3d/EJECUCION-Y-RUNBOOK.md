# Ejecución y runbook — Validación viva del canvas v12 (rama 3D)

**Estado:** v12 ensamblado y validado **offline** (estructura + cableado 20/20). La corrida viva queda pendiente de agendar — instrucción del operador: *"Una vez se hayan validado los puntos anteriores, procederemos a ejecutarla"*.
**Artefacto:** `gh-definitions\F1_CONTEXTO_v12.gh` (regenerado 2026-09-29). Fallback: `F1_CONTEXTO_v11.gh` (blindado P0; backup del `.ghx` en `.bak-20260929-194159`).

---

## A. Antes de la ventana

1. **Cerrar AutoClaw** (conflicto del puerto 19723 con la Live Connection; si hace falta: `diagnostico_puerto_19723.ps1`).
2. **Habilitar logs a disco** de la sesión del canvas (con AutoClaw cerrado no hay consola visible; recomendado por el Crítico).
3. Verificar `DISENO_PARAMETRICO_ROOT` = `D:\Work\PROJECTS\DiseñoParametrico` (indicadores del canvas).
4. Iniciar el orquestador: `D:\Work\Scripts\Init-DP.cmd` (front-end 8900; no conflictúa). Chip activo: **AAA0030JKOE** (B).

## B. Pasos

1. Abrir Rhino 8 + Grasshopper → **`gh-definitions\F1_CONTEXTO_v12.gh`** (NO usar "archivos recientes" con rutas viejas).
2. Recomputar (F5) y revisar **mensajes sin rojos**:
   - `#21` → `ETAPA1 v04.3 | CHIP: …` (lector canónico; si aparece `[AVISO ENCODING]` anotar archivo).
   - Componente **3D** → `ETAPA1-3D v01 | CHIP: … | curvas: ON (lote 1 / vec N / vias N / ep N) | cintas: ON (…) | MDT pts: N`.
   - Componente **ENVOLVENTE-3D v01** → `muestras: 65 | base: … | altura: … | curva: ON | banda: ON | volumen: ON/OFF`.
   - `#48` → `… z_base −20,5–1,7 m (90 con cota)`; `#81 LADOS v06.5`; `#99 PATIO v02.5`.
3. **Exports:** pulsar "Exportar GFA" y "Exportar diagnóstico lados+patio"; recomputar si es el patrón de flags.
   - `data/fase-2-demanda/AAA0030JKOE-gfa-gh.json` nuevo (`valido=true`; revisar `pisos_finales` esperado **5**, ADR-022).
   - `data/pot-cache/AAA0030JKOE-lados.json` → `GET /api/estado?chip=AAA0030JKOE` → **F1.5 6/6**.
4. **En ArchiCAD — lo nuevo (requisito del operador):**
   - **Curvas 3D** (lote/vecinos/envolvente): visibles en vista 3D y **seleccionables** (Morph Curve no sólido).
   - **Cintas 3D** (contexto: lote+vecinos+vías+EP): Morph Solid drapeados sobre el MDT.
   - **Terreno:** malla del nodo Mesh (deja de estar huérfana).
   - **Volumen de envolvente:** si T3 está ON (default OFF) — útil para **movimiento de tierra**.
   - **Toggles:** T1 (curvas) / T2 (cintas) / T3 (volumen) deben ocultar/mostrar al recomputar.
   - **Notas:** los morphs se crean sin capa asignada (igual que el flujo vigente del #74); si se desea capa dedicada, asignar en ArchiCAD (o cablear "Morph Settings" en una ventana futura). Recomputaciones repetidas pueden **duplicar** elementos LC: verificar al final y limpiar por capa si hiciera falta.
5. **Pipeline completo** con el GFA nuevo: `f2_venta ✓`, `f3_distribucion ✓`.
6. Guardar estado del canvas (Save) y registrar evidencia (capturas + mensajes + logs).

## C. Criterios de aceptación

- [ ] Sin errores rojos en el canvas; sin `Invalid Curve value…` en las ramas LC nuevas.
- [ ] Mensajes de los componentes nuevos presentes y coherentes (números de vecinos/vías/EP).
- [ ] Curvas/cintas/terreno visibles y seleccionables en 3D; toggles operan.
- [ ] Exports OK (GFA nuevo + `6/6` de F1.5).
- [ ] Rollback probado si algo falla: reabrir `F1_CONTEXTO_v11.gh` (fallback) — la sesión sigue operativa.

## D. Rollback

1. Cerrar el canvas v12 sin guardar (o dejar v12 para diagnóstico). 2. Abrir `F1_CONTEXTO_v11.gh` (el blindaje P0 se mantiene). 3. Reportar con logs + mensajes capturados.

---

*Generado 2026-09-29 a partir del plan aprobado y de la ejecución P0/P1 (ver EJECUCION-P0-P1.md).*
