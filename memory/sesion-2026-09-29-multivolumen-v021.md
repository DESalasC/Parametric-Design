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

## Adenda (misma sesión, 11:58) — decisiones del operador + v02.2
- **Operador (punto 1, datos):** el bloqueo de vías oficiales es manejable — al pasar los datos en bruto a ArchiCAD el operador organiza andenes/calles; la topografía fina se toma cuando llegue el momento. No cambiar el flujo por esto.
- **Operador (punto 2, circulación):** añadir opción de crujía (una/dos) y posición del núcleo por bloque (centro/lado) para mejorar la distribución en lotes grandes con desnivel (lado oriente "hundido"). Ejecutado:
  - F3 **v02.2**: `--bloques-crujia doble|unica` (doble: ancho_min = max(2×crujía + circ, núcleo); única: max(crujía + circ, núcleo)); `--bloques-nucleo centro|extremo`; `bloques.json` → `crujia {}` y `nucleo_posicion`; avisos de reducción con desglose.
  - servidor: variable `bloques_crujia`; mapeo `alineacion_nucleo` (0→centro, 1/2→extremo); paso por CLI; `bloques_resumen` ampliado.
  - index: campos nuevos; línea viva muestra núcleo (centro/extremo) y crujía con desglose del ancho.
  - **Caso B**: doble → máx 2 bloques; única → máx 4 (3 bloques: anchos 13,16 m; niveles 0,00→+13,05, paso 6,53). Con doble, 3 bloques miden 13,2 m (esquina en diagonal) < 13,4 → no caben.
  - Tests: 13 en `test_f3_bloques_usos`; suite completa **318/318**.
- **Nota 3 (re-encaje canvas):** explicada al operador en la respuesta (qué es; posibilidades y limitaciones — envolvente F1, terreno MDT/organizado en ArchiCAD, crujía/núcleo, Morphs LC).

## Adenda 2 (12:22) — skills de arquitectura revisadas; actualizaciones aprobadas
- **Inventario de skills de arquitectura** (a pedido del operador): suite AgentKit (13, en `D:\Users\Work\.openclaw-autoclaw\skills` + scripts en `D:\Work\Scripts\AgentKit`), biblioteca Architect Skills (18, enlazada en el proyecto), 4 de proyecto (disenoparametrico, normativa-bogota, construccion-colombia, alexander-patterns) y `dparam-patch-ghx` (Claude Code). Estado: no cargadas como skills activas en la sesión AutoClaw (uso por ruta). El operador aprobó todos los puntos propuestos + los 2 hallazgos extras.
- **Ejecutado:**
  - **Skill `disenoparametrico` ACTUALIZADA** (`D:\Work\AI\skills\disenoparametrico\SKILL.md`; respaldo `.bak-20260929`): versiones vigentes (ETAPA1 v05, LADOS v06, NORMATIVA v08, EXPORTAR_GFA v02, F2/F3/F4), multivolumen v02.2, orquestador, agentes dparam-*, herramientas AgentKit, docs (vault + `docs\` + `memory\`). README raíz corregido (maestro v03; operativo v11).
  - **Backup formalizado**: tareas de Windows 22:30–23:30 = vía principal (StartWhenAvailable ya activo, recuperan al encender); cron AutoClaw 23:00 **DESACTIVADO** (duplicaba D-Backup-AgentKit-H 23:15); red de seguridad 07:30 **corregida** (rutas ahora `H:\BACKUP\AgentKit\…`; antes miraba la ruta vieja `D:\Work\BACKUP`). Ojo: esa red viene fallando por 403 de auth del proxy (2 errores seguidos al 29-09).
  - **Herramientas verificadas con corridas reales**: gh-bridge sobre `F1_CONTEXTO_v11.ghx` (319 objetos, 24 GUIDs, incluye `#21-F1_ETAPA1_CONTEXTO_v04.2.py`); html-to-pdf → `exports\F3_planos_AAA0030JKOE.pdf` (68 KB); f2-excel → `exports\F2_prefactibilidad_AAA0030JKOE.xlsx`; `vault_append.py` dry-run OK.
  - **Agentes dparam-***: verificados (6 configurados y alcanzables; plan maestro v2; normativa solo-lectura con citas). Detectado que NO tenían sus skills enlazadas pese a declararlas → **12 junctions creadas** en sus `.agents\skills` (normativa-bogota, disenoparametrico, agentkit-col-data/geodata/gh-bridge, agentkit-obsidian, agentkit-f2-excel/html-to-pdf). Listos para estrenar.
  - **Contraste diseño crujías** (building-typology / spatial-planning / fire-life-safety): doble crujía residencial fondo 12–15 m ↔ nuestro 13,4 m ✓; crujía única = NTG 0,72–0,78 (menos eficiente, más luz) — consistente con lote B (doble→máx 2; única→máx 4). Núcleo en extremo ≈ "side core" (libera área; cuidar distancias de evacuación).
- Pendiente: validación del operador del orquestador → cierre con registro en vault vía `agentkit-obsidian`.

## Etiquetas
#fase-3 #orquestador #multivolumen #v02.1 #orientacion #niveles-terreno #ancho-minimo
