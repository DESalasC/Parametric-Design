# Patio v03 — Bifurcación por número de volúmenes (F1 · ETAPA2)

- **Fecha:** 2026-09-30 · **Proyecto:** DiseñoParametrico · **Chip de prueba:** AAA0030JKOE (Test 07)
- **Estado:** ✅ Implementado y validado OFFLINE (fuentes + canvas v12 actualizado). ⏳ Validación viva pendiente (sesión del operador; la conexión LC se cayó durante la mañana del 30-09 — ver §5).

---

## 1. Pedido del operador (2026-09-30)

De la prueba con `F1_CONTEXTO_v12`:

> "El cálculo normativo está fallando porque en `F1_ETAPA2_PATIO_v02.py` se espera como salida **UN** polígono de patio y en este caso tenemos en realidad **varios patios** distribuidos dentro del terreno del predio. Es necesario tener una **bifurcación** entre un lote con un solo volumen que exige un solo patio, a un predio donde se pueden tener varios patios, ya sea internos o separaciones entre diferentes volúmenes."

Errores reportados (antes / después de asignar categorías en ArchiCAD): `NORMATIVA v08.1 | ERROR DE VALIDACION | Ocupacion (946.3) >= Area bruta (946.3)` · `PATIO v02.4 | Generados: 0 | fallback: patio en V0 no valida (no cabe / no interior)` · `LADOS v06.5 | ... | Esq:False | Posterior:NO`.

## 2. Diagnóstico (reproducido offline con datos reales)

- Lote AAA0030JKOE: 946.45 m²; 30 vértices crudos → **6 simplificados** (regla 2.5°).
- **V0 es una esquina ENTRANTE (reflex) del lote simplificado** (giro positivo en polígono CW; el interior queda fuera de la cuña de los dos lados). El patio anclado a V_N=V0 (paralelogramo entre los dos lados) extiende su punto interior p2 **fuera del lote** → `build_patio_desde_vertice` devuelve None → **"Generados: 0"**, exactamente como en la prueba viva.
- Consecuencia en cadena: `patios=[]` → huella = lote completo → `Ocupacion (946.3) >= Area bruta (946.3)` en NORMATIVA (valido=False) → cadena detenida.

**Reproducción (smoke real, CPython + stub):**
```
LADOS v06.5 | Verts 30->6 | A=V3 N=V0 | ... Vias:34 EP:13 Vec:90 | Ancho via: 0.00m
PATIO v03 | modo unico | ... | Generados: 0 | Motivo: fallback: patio en V0 no valida (no cabe / no interior) | Sugerencia: ...
PATIO v03 | modo MULTI (n_volumenes=2) | ... | Generados: 2/2 | Anclas: V1, V2 | Areas: 9.01, 9.00 m2 | Claridades: 3.00, 3.00 m
PATIO v03 | modo MULTI (n_volumenes=3) | ... | Generados: 3/3 | Anclas: V1, V2, V5 | Areas: 9.01, 9.00, 9.00 m2
```

## 3. Implementación

### 3.1 `F1_ETAPA2_PATIO_v03.py` (nuevo; reemplaza a v02.5 en el canvas)

- **Nuevo input `n_volumenes`** (Number; tolerante: None/0→1; tope 16).
- **Modo UNICO (n≤1):** comportamiento v02.5 **idéntico** (1 patio máx. desde V_N; puntos mejorados; garantías 9 m² / 3 m). Si no valida: mensaje con motivo + **sugerencia de modo multi**.
- **Modo MULTI (n≥2):** un patio por **esquina interior elegible** (dos lados adyacentes colindantes Lateral/Posterior), **prioridad**: V_N primero, luego por **interioridad** (mayor distancia mínima a vía/EP); hasta `n_volumenes` patios; **sin solapes** (vértices+centroides+mitades de arista+cruces); garantías idénticas por patio. Mensaje con anclas, áreas y claridades.
- Export F1.5 (`<CHIP>-lados.json`): + campos `modo`, `n_volumenes`; `patios[]` con `vertice_ancla`.
- **Regla v1 del modo MULTI sujeta a validación del operador** (¿el reparto por esquinas interiores cubre "internos vs separaciones entre volúmenes"?).

### 3.2 Canvas `F1_CONTEXTO_v12` (par .ghx/.gh actualizado)

- #99 → `#99-F1_ETAPA2_PATIO_v03.py` (código embebido = fuente; InputCount 4).
- Nuevo **`#166-Number Slider`** (Min 1, Max 8, Valor 1, entero) cableado a `n_volumenes`.
- Verificación post-parche: 331 objetos; 0 duplicados de chunk; 0 sources sin resolver; cables 3D intactos; round-trip `.gh→.ghx` OK.
- Backups: `F1_CONTEXTO_v12.ghx.bak-20260930-100421` (pre-parche) · `F1_CONTEXTO_v12.gh.bak-20260929-1942-build` (binario del build 29-09) · `.bak-20260930-0945` (estado de la mañana del operador).
- Timestamps del par sincronizados (ambos 2026-09-30 10:06:31).

### 3.3 Pruebas

- `tests/test_patio_v03_bifurcacion.py`: **9/9** (modo único idéntico a v02; V_N sin cabida → sugerencia; multi 2/4 patios; solape rechazado y continúa; tolerancia de input).
- Suites: raíz **335/335** (+9) · fase-1 **56/56**.

## 4. Cómo probar en vivo (esta ventana)

1. Abrir el par NUEVO: `gh-definitions\F1_CONTEXTO_v12.gh` (mismo nombre; timestamps 30-09 10:06). No usar "recientes" con rutas viejas.
2. Recomputar (F5). Mensajes esperados:
   - `#99` → `PATIO v03 | modo unico | ... | Generados: 0 | ... | Sugerencia: ...` (el lote real tiene V0 reflex).
   - Mover **slider #166** a **2** (o 3) → recomputar → `PATIO v03 | modo MULTI | Generados: 2/2 | Anclas: V1, V2 | ...`.
   - `#113 NORMATIVA`: con patios ≥1 debe DESAPARECER el error `Ocupacion >= Area bruta` y mostrar `Patios X m2` + GFA.
3. Exports: "Exportar GFA" + "Exportar diagnóstico lados+patio" → `GET /api/estado?chip=AAA0030JKOE` (F1.5).
4. En ArchiCAD: verificar terreno/curvas 3D (rama MC/MS/M1) — primera corrida de esa rama.
5. Evitar abrir las apps con AutoClaw ANTES que ArchiCAD (conflicto conocido del puerto 19723 — ver §5).

## 5. Incidencia de la mañana (30-09): conexión LC caída

- La sesión viva del operador se interrumpió (~09:55): Rhino y ArchiCAD ya **no estaban corriendo** al revisar; el archivo `Test 07.pln.lck` desapareció (cierre o salida abrupta).
- Al revisar: **AutoClaw escuchando en 127.0.0.1:19723** (el conflicto documentado del reporte 2026-09-13: el JSON interface de ArchiCAD / LC usa 19723 por defecto).
- Recomendación: **orden de arranque ArchiCAD → Rhino/GH → (AutoClaw)**; si la LC no conecta, cerrar AutoClaw, reconectar y reabrirlo después. Al reabrir Test 07, ArchiCAD ofrecerá recuperación si quedó algo sin guardar (existe backup `.bpn` 08:27).
- Pendiente decisión: re-enviar/actualizar el reporte del puerto 19723 al soporte del AutoClaw.

## 6. Decisiones abiertas (para el operador)

1. **Regla v1 del modo MULTI**: ¿esquinas interiores es suficiente, o se requieren reglas específicas "patios internos" / "separaciones entre volúmenes"? (parámetro y mensajes ya listos para iterar).
2. **Modo UNICO con V_N sin cabida**: hoy → 0 patios + sugerencia multi. ¿Debo además permitir "buscar otra esquina" en modo único?
3. **Renombres #45-48** (Vias/Verdes/Vecinos/andenes): en este canvas los cuatro lectores son #43–#46; ¿aplico los nombres descriptivos con nuestra numeración (#43-Vias…)?

---

*Generado 2026-09-30 a partir del pedido del operador, diagnóstico reproducido, implementación v03 y evidencia de tests/smoke.*

---

## 7. Actualización v03.1 (30-09, tarde) — Inferencia automática (mínima injerencia)

Pedido del operador: *"la decisión debe ser lo más automática posible... se debería inferir el número de volúmenes dentro del predio"* (+ preguntas de diseño: patio con volumen aislado por todos lados; patios interiores por GFA/altura/IO; futura retroalimentación de las "Zonas").

**Implementado (v03.1; canvas re-parcheado):**
- `n_volumenes` 0/vacío → **AUTO**: `n = min(esquinas interiores válidas, capacidad del lote)` con `capacidad = round(área_lote / A_REF_VOL_M2)`, `A_REF_VOL_M2 = 300 m²` (básico, ajustable).
- Ancla preferente V_N (con puntos mejorados); si no valida, AUTO puede anclar en otra esquina interior.
- Slider #166: default **0 = AUTO** (el operador no toca nada); 1 = único forzado (estricto v02.5); ≥2 = multi forzado con ese tope.
- Evidencia: AAA0030JKOE → `modo AUTO | n_volumenes inferido: 3 (esquinas validas: 3 | capacidad: 3 @ 300 m2) | Anclas: V1, V2, V5`. Tests: `test_patio_v03_bifurcacion.py` **12/12**; suite raíz **338/338**; smoke real CPython+stub.
- Backups: `F1_CONTEXTO_v12.ghx.bak-20260930-102748` (pre-v03.1). Par sincronizado: **30-09 10:27:56**.

**Respuestas de diseño (preguntas del operador):**
- **Volumen aislado por todos lados / qué recibe NORMATIVA:** el contrato ya es una **lista 0..N** que se resta de la huella. Los aislamientos de un volumen libre se resuelven con los **RETIROS** de la envolvente (no con patios de medianería); la lista de patios puede quedar **vacía** (caso válido cuando hay retiros) o contener las **separaciones entre volúmenes** como islas. Sin cambios de contrato; en la etapa de **Zonas**, esas islas se reciben/editan directamente.
- **Patios interiores (definición básica):** un patio interior por cada `A_REF_VOL` de área de piso "profunda": `n_int = max(0, ceil(A_piso / A_REF_VOL) - 1)` — disparador por **GFA/altura/IO**; garantías idénticas (≥9 m², claridad ≥3 m); distribución básica regular (v1); quedan como objetos con `id`/tipo para edición futura.
- **Interfaz "Zonas" (etapa posterior):** entrada futura de zonas de patio (p. ej. `zonas_patio_json`) que **reemplaza** la generación básica (retroalimentación del operador); NORMATIVA no cambia (mismo contrato). Implementación de interiores = **v03.2** (requiere huella/zonas — siguiente incremento).

**Decisiones pendientes actualizadas:** ② resuelta parcialmente (AUTO ya ancla alternativo si V_N no valida; único estricto queda como override); ③ renombres #45-48 sigue en pie.
