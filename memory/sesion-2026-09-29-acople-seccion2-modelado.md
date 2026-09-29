# Sesión 2026-09-29 — Acople §2→§4 (usos→modelado) + multivolumen básico + diagnóstico terreno

**Tema:** ejecución de correcciones derivadas de la validación del operador (29-09, desde el orquestador).

## Contexto (hallazgos de la validación)
1. Sección 4 "Modelado (masa)" mostraba un escenario pre-generado (B) desacoplado de lo pedido en
   la sección 2 (Normativa/usos) → modelado no correspondía a lo solicitado.
2. Sin forma de definir nº de bloques, distribución en el lote ni desniveles entre bloques.
3. Polilíneas del canvas en un solo plano (no siguen el terreno); en ArchiCAD 3D no aparece el
   terreno ni los perímetros de los lotes (ni el del predio seleccionado); `topo_mesh` huérfana.

## Ejecutado (código + tests)
- **F3_DISTRIBUCION_v02.py** (nuevo): `--usos` (filtro sección 2, renormaliza pct_gfa/gfa_m2 y
  unidades), `--bloques N`, `--bloques-distribucion {longitudinal|transversal}`,
  `--bloques-separacion-m` (mín. normativo 6,00 m, Anexo 5 §1.10.b), `--bloques-desnivel-m`,
  `--bloques-azimut`; escribe **bloques.json** (franjas del lote vía OBB shapely en el marco local
  del contexto; contrato para VOLUM v09). `normalizar_uso` amplía "comercio"→Local comercial y
  "salud"→Consultorios. Defaults backward-compatible (n=1, sin filtro).
- **servidor.py**: `F3_DIST_SCRIPT`→v02; `_derivar_escenario_f3` (Salud→D_MIXTO_SALUD);
  `_generar_f3(chip, escenario, usos, bloques)` y `_pipeline(..., usos, bloques)`;
  `/api/generar-f3` y `/api/pipeline` reciben `usos`/`bloques`; 4 variables nuevas de sección
  "modelado" (bloques_num/distribucion/separacion_m/desnivel_m); label del `caso` →
  "Escenario pre-generado (referencia)".
- **index.html**: helpers `escenarioDerivado()`/`recolectarBloques()`/`actualizarModeladoDerivado()`;
  línea viva "Se modelará según §2–§3…" en la sección 4; los botones F3/Pipeline envían usos +
  bloques (ya no `escenario:'D_MIXTO'` fijo).
- **run_pipeline_v01.py**: comando F3 → v02.
- **Docs**: README raíz, fase-3 README, orquestador README (sección "Acople §2→modelado"),
  ARCHIVOS_INTERCAMBIO (fila `bloques`).
- **Tests**: `tests/test_f3_bloques_usos.py` (7) + regresión: 19/19 verdes.
  Smoke: import servidor OK; `node --check` del JS del front OK.
- **Corrida canónica**: B regenerado (5 niveles, huella 663 m²) con `bloques.json` (n=1 por
  defecto) — carpeta `casos/AAA0030JKOE` en estado limpio. Backup: `.bak-20260929-ant`.

## Decisiones
- El modelado se deriva SIEMPRE de §2/§3; el selector "pre-generado" solo sirve para VER
  resultados ya generados (no gobierna la generación).
- z_base por bloque = `i × desnivel_m` (negativo desciende) — la integración real con cotas de
  terreno queda para el canvas (VOLUM v09).
- Malla/terreno en ArchiCAD: pendiente (Fix 3) — diseño: ETAPA1 v05 con salidas drapeadas +
  nodos LC "Morph Solid" nuevos (terreno + banda del lote) en un canvas **v12** (no pisar v11).

## Pendientes (Fix 3 — siguiente)
- ETAPA1 v05 (mallas drapeadas: terreno, banda de perímetro del lote/vecinos/vías) + parche del
  canvas a `F1_CONTEXTO_v12` agregando Morphs LC (terreno → capa 10-20-10_Topografia; lote →
  00-00-10_Lote_proyecto) y regeneración .gh → validar en sesión viva (AutoClaw cerrado).
- Regenerar `casos/CASO` activo y revisar visualmente los bloques cuando el operador los use.
- Vault: registrar (diario/acta/lección) — pendiente.

## Etiquetas
#fase-3 #orquestador #multivolumen #bloques #terreno #pendiente-v12
