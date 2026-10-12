# F0 — Verificación en vivo y sincronización canvas→src

- **Fecha:** 2026-10-11 (noche)
- **Canvas:** `F1_CONTEXTO_v13.2.ghx` (2026-10-10 13:50) · **Caso:** B (AAA0030JKOE)
- **Autorización del operador:** Live Connection por 19724 viable (AutoClaw primero) · sincronizar `src/` con el canvas.

---

## 1. Verificación en vivo (Live Connection / ArchiCAD JSON API)

### 1.1 Stories actuales en ArchiCAD — LEÍDOS OK

`F3_StorySync_v01.py --list` (conexión auto-detectada):

| N | Nombre | Cota |
|---|---|---|
| N0 | Ground Floor | 0.000 m |
| N1 | Story | 3.000 m |
| N2 | Story | 6.000 m |

→ **Confirmado:** solo 3 niveles (0/3/6 m); el modelo necesita 5 (+3,6 / +6,6 / +9,6 / +12,6 según programa) + tapa opcional.

### 1.2 Capacidad de CREAR stories — NO DISPONIBLE

Catálogo de comandos del API JSON (release ac29, 73 comandos):

- Stories: **solo** `GetStoryNavigatorItems` (lectura).
- `Create*`: únicamente `CreateAttributeFolders`, `CreateLayout`, `CreateLayoutSubset`, `CreateViewMapFolder`.
- Live Connection: solo el **selector** "Story Plane" (referencia, no creación).

**Conclusión (D1):** la creación de niveles no es posible por API ni LC.
**Mecanismo adoptado:** `niveles_deseados.json` generado + creación **manual asistida** en ArchiCAD (Story Settings) + verificación automática `F3_StorySync --check`.
**Backlog:** automatización total requeriría add-on nativo (C++/API interno) — fuera de alcance.
Nota: en este proyecto "Tapir" = el API JSON (paquete `archicad`), no el plugin de terceros (ver `EJECUCION_TAPIR.md`).

---

## 2. Sincronización canvas → src (ejecutada, con backups)

Script: `scripts/utilities/sync-canvas-to-src.py --write` · Backups: `*.bak-sync-20261011-204700`

| Componente | Archivo src | Sim. previa | Acción |
|---|---|---|---|
| #114 F3_VOLUM | `src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py` | 0.9721 | **actualizado** (implanta dinámica + curvas cerradas de zona) |
| #116 F3_DISTRIBUCION | `src/fase-3-masa/F3_DISTRIBUCION_v03.py` | 0.9357 | **actualizado** (generador con base_normativa + topo + bloques) |
| #151 NORMATIVA v09.1 | `src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v09.1.py` | 0.9992 | **actualizado** (puntos 3D: `z=p[2]` en huellas) |
| #154 LAYERS XML | `src/fase-1-contexto/F1_LAYERS_XML_v02.py` | 0.9548 | **actualizado** (simplificado: se retiró fuente alternativa `json_path`) |
| #59 ETAPA1 v04.4.1 | `src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.4.1.py` | — | **creado** (no existía en esa ruta) |
| #199 NORMATIVA v10 · PATIO v03 · LADOS v06 · F0 · GFA v02.4 · UNIDADES v02 · ACCESOS v02 · OVERRIDE USO · CONTEXTO50 BUILD | (respectivos) | 1.0000 | ya iguales (sin cambios) |

**Versionado pendiente (al próximo parche de canvas):** rotular `F3_VOLUM v08.1` y `F3_DISTRIBUCION v03.6` en el encabezado interno (hoy el código quedó 1:1 con el canvas, sin tocar textos).

---

## 3. Tests post-sincronización

`pytest` (5 archivos enfocados): **37 passed / 7 failed**

| Test | Estado | Lectura |
|---|---|---|
| `test_f3_distribucion_v03_gh` (6) | ❌ nuevos | **Esperado**: el generador nuevo EXIGE `base_normativa_json` ("no se permiten dimensiones ni pisos fijos") y los tests inyectan entradas viejas. → Actualizar fixtures en F1 (añadir `base_normativa_json` + `topo_mesh` stub). |
| `test_normativa_v09_fuente::test_modo_potencial_sin_barras` | ❌ pre-existente | Ya estaba rojo desde 2026-10-09 (test legacy v09 con stub). |

Resto (volum v08, storysync, bloques usos): OK.

---

## 4. Pendientes inmediatos (entran a F1)

1. Actualizar `tests/test_f3_distribucion_v03_gh.py` con fixtures `base_normativa_json` (+ topo_mesh) — 6 casos.
2. Implementar F1 sobre la copia sincronizada: crujía única (`crujia_max_m`), sin shrink centrado, n adaptativo, validaciones de linderos.
3. Preparar `niveles_deseados.json` (caso B) + `F3_StorySync v02` (`--plan/--check`); creación manual de 5 niveles en AC cuando el operador lo indique.
4. Revisar el rojo legacy `test_modo_potencial_sin_barras` (v09/stub).

---

## 5. Actualización (misma noche, 2026-10-11) — F1 implementado en src

- **`F3_DISTRIBUCION_v03.py` → v03.6** (subversión en encabezado):
  - Cap `crujia_max_m` (def. 10 m; tope 12) con **n auto-ajustado** (≤5) y avisos.
  - **Ancho completo** (sin reducción centrada → sin huecos laterales); área ajustada por profundidad (bisección, mín. 6 m).
  - Recorte de franjas en **Python puro** (Sutherland-Hodgman) — sin depender de Rhino para el clipping.
  - Validaciones: alcance lateral por banda (`alcance_lados`), margen vs presupuesto, separaciones; avisos en el mensaje.
  - Cota de arranque tolerante: topografía opcional; cota fija con `cota_arranque_m` (para CLI/pruebas).
  - CLI: nuevos `--base-normativa-json` y `--crujia-max-m`; mensaje `F3 v03.6`.
- **Tests**: `tests/test_f3_distribucion_v03_gh.py` reescrito (fixtures base + nuevos casos cap/auto-n/ancho completo/clip puro) → **18/18 ✓**.
- **Smoke CLI (caso B, n=2,3,4)**: recomendada `ALT-3B-300` (3 barras, prof. 7.0 m, occ 630 m², GFA 3150) con avisos de auto-n/margen — mecánica F1 verificada offline.
- **Parche de canvas listo y probado sobre copia**: `scripts/utilities/patch-ghx-v132-f3dist-v036-2026-10-11.py` (re-embebe el código en #116; GH_IO relee + `.gh` regenerado OK). **Aplicar con GH cerrado** (o recargar el script manualmente en el componente).
- Pendiente de F1: **aplicado al canvas real** `F1_CONTEXTO_v13.2.ghx` (2026-10-11 21:04; backup `.bak-20261011-210427`) y `.gh` regenerado (261.737 bytes). Pendiente: validación en vivo del operador (mensaje `F3 v03.6` + n reales del caso B).
- **Fix runtime "Huella invalida B1-R1"** (2026-10-11 21:15): #116 emite `huella_xy` abierta → #114 exigía cerrada. Corregido: **#116 v03.6.1** (huella_xy CERRADA) + **#114 v08.0.1** (cierre defensivo). Parche conjunto `patch-ghx-v132-f1fix-2026-10-11.py` validado sobre copia (GH_IO relee). **Aplicado al canvas real (2026-10-11 21:21; backup `.bak-20261011-212154`) preservando la reorganización del operador (377 objetos / 134 grupos) y `.gh` regenerado (271.829 bytes).**
- **v03.7 (misma noche, ajustes operador):** (a) anclaje de franjas a frente y fondo + separaciones ajustadas uniformes (sin fondo libre; sin antejardines en frentes públicos); (b) **pisos por bloque** (`pisos_por_bloque` o `limites_pisos_json` con bandas + redistribución al último bloque). Tests **20/20**; parche `patch-ghx-v132-f3dist-v037-2026-10-11.py` validado en copia (`.gh` regen OK). **Aplicado al canvas real (2026-10-11 21:48; backup `.bak-20261011-214810`; 377 objetos preservados) y `.gh` regenerado (273.198 bytes).**
- **v03.7.1 (misma noche, 22:04):** mensajes internos `F3 v03.6 → v03.7` (3 textos que faltaban) + **2 entradas nuevas agregadas por parche al componente** (`pisos_por_bloque`, `limites_pisos_json`) + NickName actualizado a `#200-F3_DISTRIBUCION_v03.7.py`. **Aplicado al canvas real (backup `.bak-20261011-220416`) y `.gh` regenerado (273.335 bytes).**
- Reglamentación consultada: ADR-022 (sin antejardín ambos frentes; empates norte BIC ~20 m / sur 5 p; separación ≥ máx(2/5·h; 6 m)); regla "5 m" del operador pendiente validar con IDPC (parametrizable en `limites_pisos_json`).
- **v03.8 (22:15):** ESCALONAMIENTO LATERAL (norma 1/5 sobre empate): `sep_lateral_json` (retiro por piso r = max(0.2·(z−h_vecino), min, 0.02·z)); el #114 (v08.0.2) usa `huella_xy_por_piso` (volúmenes y zonas escalonan). Aplicado al canvas y `.gh` regenerado.
- **Canvas → v13.5 + limpieza (22:18):** renombrado `F1_CONTEXTO_v13.5.ghx/.gh` (nombre interno corregido, `.gh` regen); **193 archivos desactualizados** movidos a `gh-definitions\_archive\2026-10-11\` (borrable cuando se quiera; el camino queda en el Vault); scratch de `scripts\utilities` → `_old\`; `__pycache__` eliminados. Raíz de gh-definitions: v13.5 (+ README, CABLEADO_F0, data).
- **Convención de numeración (operador, 22:33):** la ficha de componentes la fija **#Fancy Names** (posición izq→der/arriba→abajo; renumera en cada corrida; su salida `inventario` es la fuente autoritativa). Referenciar componentes por **nombre de script** + número de la última corrida; el etiquetador toma el token `.py` de las primeras líneas (mantenerlo).
- **Encabezados v03.8/v08.0.2 (22:4x):** títulos con "versión actual (genérica)" y recorte a las **últimas 3 subversiones** (resto → Vault); tests 21/21 + 8/8. Pendiente: llegan al canvas con el próximo parche.
- **Diagnóstico AC (23:0x, con mensajes del operador):** la propuesta F3 está OK en canvas (4 bloques, escalonamiento 1/5, 20 zonas; mensajes v03.8/v08.0.2). Toggles verificados: **salida_zona=true · Zone.Sync=true · salida_morph=false**. Bloqueadores para que ArchiCAD cambie: (1) **stories insuficientes** (solo 0/1/2) para las cotas del modelo actual; (2) **cadena de morphs F3 inexistente** (#213 sin consumidores y el modo implanta emite Brep → plan v08.0.3: mesh cuando salida_morph + guía de cableado LC Morph); (3) **retiros frente/fondo >0 en base** (pedir antejardín 0 / override posterior en v10); (4) aviso "no alcanza borde derecho" + margen 145 m² (revisar borde diagonal del lote / base).
