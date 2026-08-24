# Bitácora de versiones, decisiones y pruebas — DiseñoParametrico

Cierre de fase **F1–F3** · **2026-08-18** · 85 commits · suite **234 passed**.

## 1. Versiones vigentes por fase

| Fase | Script vigente | Versión | Estado |
|---|---|---|---|
| F0 | `F0_LOAD_PROYECTO_v01.py` | v01.3 | Estable (IronPython 2.7) |
| F1 contexto | `F1_ETAPA1_CONTEXTO_v02.py` | v02 | Estable |
| F1 lados | `F1_ETAPA2_LADOS_v06.py` | v06 | Estable |
| F1 patio | `F1_ETAPA2_PATIO_v02.py` | v02 | Estable |
| F1 normativa | `F1_ETAPA2_NORMATIVA_v08.py` | v08 | Estable |
| F1 GFA | `F1_EXPORTAR_GFA_v02.py` | v02 | Estable |
| F2 venta | `F2_DEMANDA_MOTOR_v03.py` | v03 | Estable |
| F2 renta | `F2_RENTA_MOTOR_v03.py` | v03 | Estable |
| F3 distribución | `F3_DISTRIBUCION_v01.py` | v01 | Estable |
| F3 volumen | `F3_VOLUM_GENERADOR_v07.py` | v07 | Estable (Rhino 8) |
| F3 accesos | `F3_ACCESOS_INTEGRADOR_v02.py` | v02 | Estable |
| F4 ambiental | `F4_LADYBUG_ANALISIS_v02.py` | v02 | No validado en Rhino |
| F5 BIM | — | — | Documentación |

## 2. Decisiones (ADR)

| ADR | Decisión |
|---|---|
| ADR-002 | Catastro vs POT: POT como fuente normativa primaria |
| ADR-004 | Postergar MCPs; solo componentes nativos GH/ArchiCAD |
| ADR-005 | Corrección de interpretación de altura POT |
| ADR-006 | Integración climática transversal (EPW + Ladybug) |
| ADR-007 | Sistema de adquisición de contexto urbano |
| ADR-008 | Clasificación espacial híbrida (oficial + manual) |
| ADR-010 | Optimización topográfica + plantilla BIM |

## 3. Pruebas

- **Suite pytest: 234 passed**, última ejecución 2026-08-18.
- Archivos de test (22): F0 load, F1 (fetch, lados v04/v05/v06, normativa v06/v07/v08, patio), F2 (venta, renta), F3 (distribución/núcleo, volumen v07, accesos v02), orquestador, servidor, vecinos por lado.
- **Casos límite cubiertos**: vecino `via` vs `predio` (Muzú occidente), empate posterior independiente, aporte parcial (`pago_parcial_pct`), usos base vs sector, alineación de núcleo.

## 4. Hitos por fecha

- **2026-07-31** — init + Decreto 555/670 + NSR-10.
- **2026-08-01/09** — Fase 1: contexto, lados, normativa, patios.
- **2026-08-12/14** — Fase 2: financiero, Build-to-Rent, sensibilidad, 3 casos.
- **2026-08-14/17** — Fase 3: distribución, volumen, accesos, prueba real de masa en Rhino 8.
- **2026-08-17/18** — Orquestador: formulario, servidor, F0 load, vecinos por lado.
- **2026-08-18** — Área de actividad (geobase) + cableado del canvas commiteado.
- **2026-08-18 (tarde)** — Sector de uso por UPL (geobase) extraído e integrado + validación `pago_parcial_pct` 70/30 con AAA0127AZPA.


## Sesión 2026-08-18 (tarde) — Interfaz + F2/F3 ejecutables desde el formulario

### Cambios
- **Interfaz**: `caso` → "Escenario de modelado" atado al CHIP (sección 4 ya no cambia de lote).
- **Aporte del lote (venta)**: variables `aporte_lote` + `pago_parcial_pct`; helper `_aporte_a_pago_parcial()`.
- **F2 desde el form**: `POST /api/calcular-f2` (corre F2 con `--pago-parcial`) + botón.
- **F3 para cualquier CHIP**: `F3_DISTRIBUCION_v01.py` acepta `--chip`/`--escenario` (`buscar_resultados`, `leer_programa_chip`, fallback `mix_usos`); `POST /api/generar-f3` + botón.
- **Pipeline**: `POST /api/pipeline` (F1→F2→F3) + botón "Ejecutar pipeline"; `_calcular_f2` escribe `resultados_<CHIP>.json` canónico.
- **Suite**: 234 → 239 passed.

### Decisiones
- `aporte_lote` → `pago_parcial_pct`: venta_completa=100, participacion=% (default 30), aporte_completo=0 (inverso de `fraccion_aporte_pct`).
- El selector de escenario no re-selecciona el CHIP: `syncCasoConChip()` filtra por `CASO_CHIP`.
- F3 con error claro + fallback a escenario `mix_usos` cuando falta D_MIXTO.

### Pendientes
- F1 GFA manual en Rhino (verificar GFA 826.58 vs 1186.87 tras regeneración del operador).
- Listas definitivas de usos por sector (Sinupot / CU-5.4.x).
- F3 masa Rhino → Morphs ArchiCAD (manual). F4/F5 pendientes.


## Sesión 2026-08-23 — Regla de esquina + puente frente_override

### Cambios
- **Normativa F1 (esquina)**: `LADOS_v06` anula `idx_posterior` en esquina;
  `PATIO_v02.1` genera el patio 3×3 sobre lados colindantes (Lateral o Posterior);
  `NORMATIVA_v08.2` fuerza `retiro_posterior = 0` en esquina.
- **Puente orquestador→canvas**: `F0_LOAD_PROYECTO_v01.4` emite `frente_override_json`
  `{cardinal: frente}`; `NORMATIVA_v08.2` lo aplica a los retiros por cardinal
  (normal saliente, `azimut = atan2(nx,ny) % 360`, misma convención de
  `vecinos_por_lado.py`).
- **Orquestador (A/B/C)**: mensaje de éxito en normativa (JSON solo en "Copiar");
  quitados `empate_posterior_pisos/m` duplicados; `_financiero` con fallback a
  `parametros_entrada.json` + campo "Valor del lote (COP)" → `costo_lote_cop`.
- **`modalidad_dueno_lote`** consolidada como única fuente (servidor + F2 + front).

### Pruebas
- **Suite: 267 passed** (nuevos `test_esquina_fuente.py`, `test_frente_override_fuente.py`).
- Sintaxis Python OK en los tres scripts F1 y en F0 (IronPython 2.7).

### Decisiones
- Lote de esquina: sin aislamiento posterior; solo antejardín frontal + patio 3×3
  en la esquina interior.
- Vocabulario de frentes (Continua): `via`, `predio` (lateral), `espacio_publico`
  (zona verde); `indefinido`/`libre` → ignorar; `servidumbre` reservado a futuro.
- Matching de lados por **cardinal** (no por índice) entre orquestador y canvas.


## Sesión 2026-08-23 (tarde) — Override de norma + GFA

### Cambios
- `data/pot-bogota/norma-override.json` (clave por CHIP): completa rango, altura,
  IO, IC, antejardín y tipología que la geobase POT no trae.
- `fetch-urban-context-v6.py`: fusiona el override en `pot_data` (gana sobre la
  geobase; solo campos faltantes/incorrectos).
- `servidor.py` + `index.html`: `GET/POST /api/norma-override` + panel "Completar
  norma (datos faltantes de la geobase)".
- `scripts/utilities/verificar-gfa.py`: chequeo post-run del GFA.
- Reconciliación `tratamiento` (`data/predios/AAA0240ZXJH/proyecto.json`) y
  proyecto `EdificioDeysy` renombrado + chip/tratamiento/antejardín completados.

### Pruebas
- **Suite: 267 passed** (sin cambios en tests; cambios son de datos + orquestador).
- Fetch verificado en vivo: override aplicado, `pot_data` con `rango "3"`,
  `altura_maxima_pisos 4`, `io_maximo 0.7`, `ic_maximo 3.0`, `antejardin_m 3.5`.
- `verificar-gfa.py` smoke-tested: detecta `io_maximo 4.0` y huella 46,3 m².

### Decisiones
- Override **por CHIP** (no por UPZ), **gana sobre la geobase**.
- `upz`/`tratamiento` fuera del override (la geobase ya los trae bien).
- Fuente exacta (ficha `041 EDIFICABILIDAD-FIRMA.pdf` + resolución 00865/2006)
  sin OCR por ahora (el operador considera que la curaduría aún no lo exige).


## Sesión 2026-08-23 (noche) — cardinal, via_no_frontal, puerto 19723

### Cambios
- **LADOS v06.2**: nomenclatura cardinal por lado (normal saliente,
  `azimut = atan2(nx,ny) % 360`, bandas N/O/S/Occ) — misma convención en
  NORMATIVA_v08 y `vecinos_por_lado.py`; guard `MAX_ANCHO_VIA_M = 100.0`.
- **Frente `via_no_frontal`** (vía sin antejardín): `FRENTE_A_CLASIFICACION` →
  "EspacioPublico" en NORMATIVA; UI del orquestador (FRENTES/CICLO/COLORES/ETIQUETA).
- **`via_no_frontal` cuenta como vía en esquina** (v08.3): `_n_vias` suma
  `v in ("via", "via_no_frontal")` → el lote es esquina con 2+ lados de calle aunque
  uno no sea el frente principal (evita patio posterior espurio).
- **Docs puerto 19723** (CLAUDE.md, MANUAL, scripts): la Live Connection de GH solo
  conecta por 19723; mover ArchiCAD a 19724 solo sirve para la JSON/Python API.
- **`diagnostico_puerto_19723.ps1 -Liberar`**: comprueba `$LASTEXITCODE` de taskkill
  (ya no dice "liberado" en falso), fallback `Stop-Process -Force`, y guía a cerrar
  AutoClaw o ejecutar como Administrador (AutoClaw corre elevado → acceso denegado).

### Pruebas
- Suite: **272 passed** (267 → 272; nuevos tests cardinal v06.2, via_no_frontal ×3,
  esquina cuenta via_no_frontal).

### Decisiones
- `via_no_frontal` = vía funcional sin aislamiento (mapea a EspacioPublico), pero
  **sí cuenta como calle** para la regla de esquina.
- AutoClaw hardcodea 127.0.0.1:19723 y lo reclama; no hay config → depende del
  soporte de AutoClaw (ticket abierto); workaround real = cerrar/reabrir en orden.

### Pendientes (diagnosticados, NO resueltos)
- Área orquestador 450 vs 99,72; entidades HTML sin decodificar; mojibake en labels.
- Re-exportar F1 al .gh (canvas aún corre v06.1/v08.1); nicknames en salida LADOS.
- Frame de coordenadas EP/vía/vecinos (ROOT CAUSE: ancho via 41,7 m, Ocup 1,6 m²).
- Parámetros financieros por CHIP + persistencia de variables + 1b-1c vecinos.
