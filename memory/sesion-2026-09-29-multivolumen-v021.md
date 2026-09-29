# Sesión 2026-09-29 — Multivolumen v02.1: orientación referida al predio, niveles Entrada→Salida y ancho mínimo por programa

**Tema:** ajustes al acople §2→§4 del orquestador tras la validación del operador (reinició con `Init-DP.ps1` y reportó: la línea de §4 seguía débil — "solo aparece Se modelará según §2–§3…" —, las opciones "a lo ancho/a lo largo" no eran claras, y faltaban niveles por bloque y ancho mínimo compatible con el programa). El operador aclaró que aún **no** inicia la revisión del canvas; esta parte (orquestador) es la inicial.

## Ejecutado (código + tests)
- **F3_DISTRIBUCION_v02.py (v02.1)**:
  - Orientación **referida al predio**: `--bloques-distribucion automatico|paralelo_calle_acceso|perpendicular_calle_acceso|paralelo_lindero|angulo` (+ `--bloques-lindero`, `--bloques-angulo-ref`, `--bloques-angulo-grados`). La dirección de las franjas sale de los **lados reales** del predio (override del operador si existe) y del azimut de la vía; los modos v02 (`longitudinal`/`transversal`/`--bloques-azimut`) siguen aceptándose (compat).
  - **Niveles automáticos**: `--bloques-desnivel auto` (default). Entrada = calle de acceso (`frente_override="via"`), Salida = vía posterior (`via_no_frontal` opuesta) o extremo opuesto del lote; cotas desde `topografia.perfil_lados` (MDT). B1 = ±0,00; BN = nivel final; intermedios uniformes. Manual disponible (`--bloques-desnivel-m`). Cada bloque reporta `z_terreno_medio_m` (MDT absoluto) desde la malla.
  - **Ancho mínimo por programa**: `ancho_min = núcleo (6,4) + 2×circulación (1,2) + crujía (unidad mayor/9,0)`; si el N pedido no cabe, se **reduce** con aviso y `n_max_recomendado`. Bloques con `ancho_m` y `unidades_estimadas` (mín-máx por uso según el GFA del bloque).
  - Franjas ordenadas **desde la entrada** (ancla en la calle) hacia el interior; `--dry-run`/`--json` para propuestas sin escribir archivos.
  - Caso B (AAA0030JKOE): 3 bloques → **2** (franja más angosta 13,2 m < mín 14,9 m); orientación "franjas paralelas a la calle de acceso (Occidente-2)"; niveles **0,00 → +13,05 m** (Entrada 2635,52 → Salida 2648,57 MDT; vía posterior = Oriente). Convención verificada: `azimut` de lados = atan2(nx,ny) local, con +y como norte de la proyección; conversión local↔azimut: θ = 90° − az.
  - Nota vía: la calle real de acceso **no** está digitalizada en `vias_oficiales` (más cercana: KR 2 E a 45,5 m); el nombre de vía solo se muestra si queda a ≤15 m.
- **servidor.py**: variables §4 nuevas (orientación, lindero, ángulo ref/grados, `bloques_desnivel_auto`); `_cmd_f3_dist` compartido; `_proponer_bloques` (F3 `--dry-run --json`, con caché) y endpoint `POST /api/proponer-bloques`; `/api/generar-f3` devuelve `bloques_resumen` (sin polígonos).
- **index.html**: `recolectarBloques()` ampliado; línea viva §4 con **propuesta real** (orientación, niveles B1→BN, ancho mínimo con desglose, avisos, ajuste de N) consultando el endpoint con debounce; mensaje de "Generar masa (F3)" con el resumen. Subtítulo de §4 actualizado. `node --check` OK.
- **Tests**: `test_f3_bloques_usos.py` actualizado y ampliado (12 tests). Suite completa: **317/317**.
- **Docs**: README fase-3 (v02.1 + tabla de salidas), orquestador README (acope §2→modelado), ARCHIVOS_INTERCAMBIO (fila `bloques`).
- **Caso**: `casos/AAA0030JKOE` regenerado con defaults v02.1 (n=1); respaldo previo en `casos/AAA0030JKOE.bak-20260929-pre-v021`.

## Decisiones
- El desfase reportado se ataca desde la **línea viva**: §4 ya no muestra un texto estático, sino la propuesta real de F3 (misma ruta que la generación), con avisos visibles (p. ej. N ajustado).
- La cota de **Entrada** es la calle de acceso confirmada por el operador (frente_override), no la vía oficial más cercana (capa incompleta).
- `z_base_m` queda **relativo a la entrada** (B1 = 0,00); el encaje definitivo a cotas de canvas/terreno es tarea del canvas (VOLUM v09 / v12), fuera de esta parte.

## Pendientes
- Validación viva del operador en el front-end (reiniciar: `Init-DP.ps1 -Stop` y luego `.\Init-DP.ps1`; recargar la pestaña).
- Canvas (parte que el operador aún no inicia): v12 (bandas 3D), wiring de `topo_mesh`, NORMATIVA v09, datasets mix; re-encaje de `bloques.json` en la envolvente (VOLUM v09).
- Vault: registrar cierre (diario/acta/lección) cuando concluya la validación.

## Etiquetas
#fase-3 #orquestador #multivolumen #v02.1 #orientacion #niveles-terreno #ancho-minimo
