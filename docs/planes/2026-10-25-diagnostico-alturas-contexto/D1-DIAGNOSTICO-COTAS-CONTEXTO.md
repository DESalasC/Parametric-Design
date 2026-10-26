# D1 — Diagnóstico de cotas: contexto vs lote

**Proyecto:** DiseñoParamétrico · F1 contexto base / F3 volumetría
**Fecha:** 2026-10-25
**Caso:** AAA0030JKOE (La Candelaria, lote inclinado)
**Canvas:** `gh-definitions/F1_CONTEXTO_v13.6.ghx`
**Estado:** diagnóstico cerrado; corrección pendiente de decisión del operador

---

## 1. Tema: cadena de datum entre ETAPA1 y contexto50

### Actividades propuestas
1. Verificar que `z_ref_m` del contexto50 sea exactamente `origen_sirgas.z + ancla_canvas_local.z`.
2. Recalcular el `desplazamiento_z` que aplica `F1_CONTEXTO50_BUILD` y comprobar que deja lote, terreno y vecinos en el mismo sistema local.

### Actividades realizadas
- Lectura de `AAA0030JKOE-contexto.json` y `AAA0030JKOE-contexto50.json`.
- Réplica en Python del cálculo de `compute_dz_from_stage1_context()` y de la selección de `Z_base` de `F1_ETAPA1_CONTEXTO_v02`.

### Resultados

| Magnitud | Valor |
|---|---|
| `origen_sirgas.z` | 2634,521 m |
| `ancla_canvas_local.z` | 14,518 m |
| `z_ref_m` | 2649,039 m |
| `origen_z + ancla_z` | 2649,039 m (delta −0,0004 m) |
| Puntos de malla de terreno | 118 (1 con z = 0,000) |
| `Z_base` ETAPA1 (mín. válido) | 0,030 m |
| Z máx. de la malla | 16,125 m |
| `desplazamiento_z` | **−14,488 m** |
| Lote en Z local | **0,236 … 14,488 m** (desnivel 14,25 m) |

**Conclusión del tema 1:** el datum cierra. No hay un desplazamiento global de 13–14 m en el contexto50: `z_base_m − desplazamiento_z = z_local − Z_base`. El supuesto de que el contexto seguía “14,5 m arriba/abajo” no se sostiene con los datos actuales.

**Salvedad:** el único punto de malla en 0,000 es una cota real del punto más bajo, pero el filtro `|z| > 0,001` lo descarta y toma 0,030 m como base. El error es de 3 cm; no explica ninguna diferencia visible.

---

## 2. Tema: geometrías de contexto sin cota (planas)

### Actividades propuestas
1. Medir qué proporción de vértices de vías, espacios públicos y vecinos de ETAPA1 tiene z = 0.
2. Determinar si esas geometrías pueden drapearse con la malla disponible.

### Actividades realizadas
- Conteo de vértices y de cotas nulas en `AAA0030JKOE-contexto.json`.

### Resultados

| Capa | Registros | Vértices | Vértices con z = 0 |
|---|---:|---:|---:|
| `vias_oficiales` | 34 | 4 685 | 4 685 (100 %) |
| `espacios_publicos` | 13 | 1 522 | 1 522 (100 %) |
| `vecinos` (ETAPA1) | 90 | 2 501 | 2 501 (100 %) |

**Conclusión del tema 2:** las vías, los espacios públicos y los perímetros de vecinos de ETAPA1 son **geometría 2D a z = 0**. En un lote que sube 14,25 m, el borde alto del lote queda 14,5 m por encima de esas líneas. Si esas capas se envían a ArchiCAD, la diferencia de alturas visible es real y no proviene del datum.

**Limitación:** la malla de ETAPA1 cubre solo el lote + ~5 m (bbox 65 × 52 m); las vías se extienden cientos de metros. No se pueden drapear con IDW local sin muestrear el MDT en sus vértices.

---

## 3. Tema: cota de los volúmenes vecinos (contexto50)

### Actividades propuestas
1. Comparar la cota `z_base_m` de cada vecino con la superficie de terreno interpolada de ETAPA1.
2. Cuantificar el error en los vecinos que caen dentro de la malla.

### Actividades realizadas
- IDW con los 118 puntos de malla en el centroide de cada huella.
- Filtro a los vecinos cuyo centroide cae dentro del bbox de la malla.

### Resultados
- `z_base_m` en marco canvas: −20,510 … 1,680 m.
- `z_base` ajustado (local): **−6,022 … 16,168 m**.
- Vecinos comparables dentro de la malla: **14**.
- Residuo `z_vecino − z_terreno`: **promedio −0,83 m**, mínimo −4,17 m, máximo +2,00 m, |máx| 4,17 m.
- Ajuste plano del terreno: `z = 8,309 + 0,1766·x − 0,1887·y`, R² 0,973, desviación 0,77 m, pendiente media ≈ 26 %.

**Conclusión del tema 3:** no hay un error constante, pero sí un error local de hasta ±4 m. La causa es estructural: `z_base_m` se muestrea en **un solo punto del centroide** de la huella (`anclar_contexto50_zbase.py`). En una pendiente del 26 %, una huella de 10 m abarca 2,6 m de desnivel; el centroide deja media huella flotando y media enterrada. En bordes de terraza el error llega a 4 m.

---

## 4. Tema: paridad canvas ↔ `src`

### Actividades propuestas
1. Verificar que el código embebido en el canvas v13.6 sea idéntico al de los archivos `src` declarados vigentes.

### Actividades realizadas
- Extracción del `CodeInput` de los 7 componentes GHPython y comparación línea por línea (ignorando vacías y CR/LF).

### Resultados (antes de la sincronización)

| Componente | Archivo src | Diferencia |
|---|---|---|
| #45 CONTEXTO50_BUILD | `F1_CONTEXTO50_BUILD_v01.2.py` | 6 líneas: `z_origen = 0.0` en canvas vs `desplazamiento_z` en disco + nota de cabecera |
| #81 ETAPA1_CONTEXTO | `F1_ETAPA1_CONTEXTO_v02.py` | 27 líneas: fixes `unicode()` y `ensure_ascii=False` del 2026-10-18 solo en canvas |
| #73 ETAPA2_LADOS | `F1_ETAPA2_LADOS_v06.py` | 4 líneas: perfil normativo forzado a z = 0 en canvas |
| #80 PATIO / #131 NORMATIVA / #200 DISTRIBUCIÓN / #201 VOLUM | — | IGUAL |

**Riesgo detectado:** el commit `f4f84102` declaraba “archivo fuente en disco sincronizado con canvas”, pero no era así. Un re-embebido desde disco habría devuelto `z_origen = −14,488` (volúmenes F3 14,5 m abajo) y habría perdido el fix Unicode de ETAPA1 (rutas con “DiseñoParamétrico” y tilde).

**Corrección aplicada:** se sincronizaron los tres archivos `src` con el canvas v13.6. Paridad final: **7/7**.

---

## 5. Procedimiento reproducible

**Condiciones:** ejecución local, sin Rhino ni ArchiCAD abiertos; datos en `data/pot-cache/`.

**Comando:**
```powershell
.venv\Scripts\python.exe scripts\utilities\diagnosticar-cotas-contexto.py --chip AAA0030JKOE
.venv\Scripts\python.exe scripts\utilities\verificar-paridad-canvas-src.py
```

**Resultado esperado:** datum OK; se reportan como falla las tres capas planas; residuo de vecinos con aviso si |residuo| > 1 m; paridad 7/7.

**Limitaciones:**
- El diagnóstico no lee el `.3dm` ni el `.pln`; no prueba lo que está dibujado en ArchiCAD.
- No sustituye la verificación en vivo con el canvas recargado.
- La malla de ETAPA1 solo cubre el entorno inmediato del lote.

---

## 6. Evidencia

- Salida completa: `docs/planes/2026-10-25-diagnostico-alturas-contexto/evidencia/cotas-AAA0030JKOE-2026-10-25.md`
- Suite: **367 pasan, 7 fallan** (las 7 fallas stale ya conocidas: `test_esquina_fuente`, `test_lados_v06_fuente` ×2, `test_morph_atributos_fuente`, `test_normativa_v09_fuente`, `test_orquestador` ×2).
- Paridad: `scripts/utilities/verificar-paridad-canvas-src.py` → 7/7.

---

## 7. Actualización 2026-10-25 — criterio A ejecutado

**Decisión del operador:** el volumen apoya en el **punto más bajo de su huella**.

**Ejecutado:**
- `anclar_contexto50_zbase.py` ahora muestrea **centroide + 4 extremos** (min/max x, min/max y) por huella y guarda `z_base_m` = mínimo de las cotas válidas, más `z_base_centroide_m`, `z_base_min_m`, `z_base_max_m` y `z_base_n_puntos`.
- Corrida REST: **90 edificios, 450 puntos, 90 OK, 0 fallidos, 219,8 s**.
- Respaldo previo: `data/pot-cache/AAA0030JKOE-contexto50.json.bak-zbase-20261025-2046` (el JSON de datos no está versionado en git).

**Resultados:**

| Métrica | Valor |
|---|---|
| Bajada de la base (centroide → mínimo) | promedio **1,06 m**, máxima **4,65 m** |
| Registros modificados | 89 de 90 (> 0,01 m) |
| Con bajada > 2 m | 9 |
| Con bajada > 3 m | 2 |
| `z_base_m` nuevo | −21,150 … −0,060 m (canvas) |
| `z_base` ajustado | −6,662 … 14,428 m (local) |
| Contraste con malla (9 huellas completas dentro) | promedio **−0,18 m**, máximo **1,35 m** |

La bajada media de 1,06 m es coherente con la pendiente: una huella de ~9 m de ancho en 26 % tiene ±1,17 m entre centro y borde.

**Efecto en el canvas:** ninguno a nivel de código. `F1_CONTEXTO50_BUILD` lee `z_base_m`; la próxima corrida del canvas ya usa la base nueva, sin re-embebido.

**Observación de datos:** los 90 registros tienen solo **45 IDs catastrales únicos** (30 IDs repetidos). Son unidades/pisos del mismo edificio con registros separados; no afecta el muestreo (cada huella se consultó por separado), pero conviene no usar `id` como clave única en procesos de deduplicación.

**Evidencia:** `.../evidencia/cotas-AAA0030JKOE-2026-10-25-post-min.md`.
