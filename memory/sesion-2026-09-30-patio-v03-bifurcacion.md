# Sesión 2026-09-30 — PATIO v03 (bifurcación multi-volumen) + restauración del par v12

**Contexto:** prueba viva de la mañana con `F1_CONTEXTO_v12` (Test 07, chip AAA0030JKOE); el operador reportó: (a) el cálculo normativo falla porque PATIO espera UN patio y el caso requiere varios (bifurcación un-volumen/multi-volumen); (b) el terreno/linderos/vecinos no aparecen en 3D.

**Intervenciones del agente:**

1. **Restauración del par v12:** el `F1_CONTEXTO_v12.ghx` de la carpeta había sido sobrescrito por la sesión de la mañana (sin rama 3D, código pre-P0). Instrucción del operador: usar el .ghx con la misma fecha/hora que `F1_CONTEXTO_v12.gh` (build 29-09 19:42, sin abrir). Se restauró desde HEAD (hash `fc6628fc…`), timestamps sincronizados; la versión de la mañana quedó en `.bak-20260930-0945`.

2. **PATIO v03.0** (`src/fase-1-contexto/F1_ETAPA2_PATIO_v03.py`): bifurcación por `n_volumenes` — modo único = v02.5 exacto; modo MULTI = un patio por esquina interior elegible (V_N primero, luego interioridad), sin solapes, hasta N. Export F1.5 ampliado (modo/n_volumenes/vertice_ancla). Regla v1 sujeta a validación.

3. **Canvas v12 parcheado:** #99 → PATIO v03 + slider `#166-Number Slider` (1..8) cableado; 331 objetos; verificación OK (0 duplicados, 0 sources sin resolver, cables 3D intactos, round-trip .gh→.ghx OK). Backups pre-parche en la carpeta.

4. **Diagnóstico reproducido offline:** V0 del lote AAA0030JKOE es **esquina reflex** → el patio no valida en V_N (mensaje idéntico al de la prueba viva); modo MULTI genera 2/2 (V1,V2) y 3/3 (V1,V2,V5) con garantías 9 m² / 3 m.

5. **Pruebas:** `tests/test_patio_v03_bifurcacion.py` 9/9; suite raíz 335/335; fase-1 56/56; smoke real (LADOS+PATIO v03, CPython+stub, datos AAA0030JKOE).

**Incidencia paralela:** la conexión GH–AC se cayó durante la mañana; Rhino/ArchiCAD cerrados; **AutoClaw escuchando en 127.0.0.1:19723** (conflicto conocido, reporte 2026-09-13). Ruta: arrancar ArchiCAD antes que AutoClaw; si falla, cerrar AutoClaw → reconectar → reabrir.

**Decisiones abiertas (operador):** (1) regla de reparto del modo MULTI (¿esquinas interiores basta?); (2) modo único con V_N sin cabida: ¿buscar otra esquina o 0+sugerencia (actual)?; (3) renombres de los cuatro lectores de polígonos (#45-48 en su canvas vs #43-46 en el canónico).

**Artifacts:** docs/planes/2026-09-30-patio-v03-bifurcacion/PLAN-Y-EJECUCION.md; commit de la sesión.

---

## Addendum (tarde del 30-09) — PATIO v03.1 AUTO

- Pedido del operador: inferencia automática del número de volúmenes (mínima injerencia) + diseño básico de patios interiores con futura retroalimentación de "Zonas".
- Implementado v03.1: `n_volumenes` 0/vacío = **AUTO** → `n = min(esquinas válidas, capacidad)` con `capacidad = round(área_lote/300 m²)`; slider #166 default 0; 1 = único forzado; ≥2 = multi forzado. AUTO puede anclar fuera de V_N si V_N no valida.
- Evidencia: AUTO en AAA0030JKOE → 3 patios (V1,V2,V5) sin intervención; tests 12/12; suite 338/338; par v12 sincronizado (30-09 10:27:56); backup pre-v03.1 en gh-definitions.
- Diseño documentado: volumen aislado → retiros + lista de patios posiblemente vacía / separaciones; patios interiores básicos `n_int = max(0, ceil(A_piso/300)-1)` (v03.2 con Zonas).

## Cierre de sesión (30-09, mediodía)

- **Renombres de lectores ArchiCAD aplicados** al canvas v12: `#36-Predio`, `#43-Vias`, `#44-Verdes`, `#45-Vecinos`, `#46-andenes` (mapeo verificado por GUID; commit `026b851f`). Par re-sincronizado 30-09 10:33.
- **Cierre por procedimiento del vault**: acta `10-arquitectura/2026-09-30-acta-sesion-cierre-patio-v03-bifurcacion.md`, diario `60-diario/2026-09-30.md`, 3 lecciones (`2026-09-30-leccion-*`), mapa actualizado; resumen del proyecto: `docs/sesiones/2026-09-30-resumen-sesion-patio-v03.md`.
- **Pendientes clave**: validación viva del par v12 (AUTO/NORMATIVA/3D/exports); v03.2 interiores + interfaz Zonas; confirmar staleness de `KeyError 'eficiencia_nga'` y `Invalid Curve value… horizontal plane` con el par nuevo; decisión reporte 19723.
- Commit de respaldo de cierre: proyecto + vault.
