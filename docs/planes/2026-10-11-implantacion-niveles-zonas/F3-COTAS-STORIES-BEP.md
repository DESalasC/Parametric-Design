# F3 — Parche cotas + Stories + Zonas BEP (v08.1) — 2026-10-12

- **Canvas:** `gh-definitions/F1_CONTEXTO_v13.5.ghx/.gh` (parche aplicado 2026-10-12 12:57;
  backup `.bak-20261012-125713` y `.gh.bak-20261012-1257` al lado).
- **Código:** `F3_VOLUM_GENERADOR_v08.py` → **v08.1** · `F3_DISTRIBUCION_v03.py` → **v03.8 (genérica v03)**
  (resincronización de cabecera, cuerpo ya 1:1).
- **Herramientas nuevas:** `src/interfases-archicad/F3_StorySync_v02.py` · parche
  `scripts/utilities/patch-ghx-v135-cotas-stories-2026-10-12.py` · utilitarios
  `scripts/utilities/comparar-canvas-src.py` y `dump-nodo-ghx.py`.
- **Tests:** `test_f3_volum_v081_zonas_stories.py` (conductual, ejecuta el componente completo),
  `test_storysync_v02_plan.py`; guardas ampliadas en `test_f3_volum_v08_fuente.py`.

---

## 1. Lo que pide el corto plazo (a) — Stories: flujo de la corrida de esta noche

1. **Flag ya activo**: `data/fase-3-masa/stories-export-flag.json` = `{"exportar": true}`.
2. Correr el canvas **en el orden habitual** (AutoClaw cerrado → ArchiCAD/GH según protocolo).
3. En el mensaje de **#198-F3_VOLUM_GENERADOR_v08.1** saldrá, además del resumen de siempre:

   ```text
   IMPLANTACION F3 | ALT-4B-305 | 4 bloques | 20 zonas | cotas B1..B4: <c1> / <c2> / <c3> / <c4> m |
   stories: <N> niveles (GF..L0X, snap ajuste max <a> m) | … | niveles: casos/<CHIP>/niveles_deseados.json
   ```

   — Las **4 cotas de arranque reales** quedan a la vista en la corrida; el flag queda en `false`
   tras exportar (una vez).
4. La misma corrida escribe en `src/fase-3-masa/casos/<CHIP>/`:
   - `cotas-arranque.json` — cotas crudas por bloque, `floor_h`, plan de stories (datos de la corrida).
   - `niveles_deseados.json` — **lista para Story Settings** (nombre + elevación + relativo).
5. **Crear los niveles en ArchiCAD** (manual asistido — la API ac29 no crea stories):
   Documento → Preferencias del proyecto → Configuración de pisos → ingresar la tabla.
6. **Verificar** (ArchiCAD abierto, puerto auto):

   ```powershell
   .venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --list
   .venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --check --chip AAA0030JKOE
   ```

   Alternativa sin canvas (repeticiones):

   ```powershell
   .venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --plan --chip AAA0030JKOE
   .venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --plan --cotas "0.2,3.35,6.85,10.15" --pisos 5,5,5,5 --floor-h 3.05
   ```

> Si hay que re-exportar tras cambiar geometría: volver a poner el flag en `true` y correr de nuevo.

### Criterio del plan (snap, decisión D2 aprobada)

- Grilla de niveles = `base + j·floor_h`; **base = menor cota de bloque**
  (el nivel de acceso definitivo — fetch v8 / NORMATIVA v10 — puede desplazar la base; el JSON lo advierte).
- Cada plataforma se **redondea a la grilla** (corte/relleno acotado a ±h/2); se reporta el ajuste por bloque.
- Nombres BEP: **GF** (acceso) y **L01…** siguientes; `RF` opcional (`--tapa`).
- Elevaciones en **marco canvas** (la misma referencia con la que la LC posiciona zones/volúmenes);
  `elevacion_relativa_m` = acumulado desde la base.

## 2. Lo que pide (b) — Zonas y categorías al estándar (BEP/ISO 19650)

Emisión v08.1 (aplica a la ruta clásica **y** a la implantación):

| Campo LC | Antes | Ahora (v08.1) |
|---|---|---|
| `Zone.Number` (`zonas_pisos`) | `B1-R1-P2` | **`L01-Z1-COM-001`** (`[NIVEL]-[ZONA]-[CATEGORIA]-[CONSECUTIVO]`) |
| `Zone Settings.Name` (`zonas_nombres`) | `B1-R1 · Local comercial` | **`Local comercial · Bloque 1 · Piso 2`** |
| `zonas_atributos` (JSON) | uso/piso/z_base | + `number`, `name`, `nivel`, `zona`, `categoria`, `consecutivo`, `usos` |

Catálogos (plan 2026-10-11 §7.3 + extensión propuesta a validar):

- **Niveles:** `GF`, `L01…`, `RF` (opcional).
- **Zonas:** `Z1…Zn` = bloques/plataformas (`ZN` reservado para núcleo si luego se emite).
- **Categorías:** `VIV` (Vivienda) · `COM` (Local comercial) · `CON` (Consultorios) ·
  `CIR` · `SER` · `PAR` · `EXT` + **extensiones propuestas**: `OFI` (Oficinas),
  `INS` (Institucional salud), `GER` (Hogar geriátrico); fallback `ZZ` + revisar.
- Reglas: solo `A-Z 0-9 -` en códigos; consecutivo reinicia por NIVEL+ZONA+CATEGORÍA; sin versiones.

**Pendiente F4 (cadena LC):** cablear `Category` (crear Zone Categories en AC) y
`Subfloor Thickness`/`Layer`/`ID`/`Property Settings` (hoy sin cablear); áreas netas (descuento de núcleo).

## 3. Recordatorio — Morphs

**La entrega de F3 es SOLO Zonas (ADR-023).** Los *Morphs* quedan reservados
**exclusivamente al contexto/vecinos** (F1). El toggle `salida_morph` sigue disponible para
análisis, pero la cadena F3 no construye morphs ni consume `F3_MORPH_ATRIBUTOS` (queda sin consumidores).

## 4. Archivos tocados en esta iteración

| Archivo | Cambio |
|---|---|
| `src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py` | v08.1: cotas en mensaje · zonas BEP · `_plan_stories` · export por flag |
| `src/interfases-archicad/F3_StorySync_v02.py` | **nuevo**: `--plan`/`--check`/`--list` (import perezoso de `archicad`) |
| `tests/test_f3_volum_v081_zonas_stories.py` | **nuevo**: conductual (stubs Rhino/GH) — 4 tests |
| `tests/test_storysync_v02_plan.py` | **nuevo**: función + CLI — 3 tests |
| `tests/stub_rhino_min.py` | + `Centroid`, `DuplicateCurve`, `Translate`, bbox, `CreatePlanarBreps` curva única |
| `tests/test_f3_volum_v08_fuente.py` | guardas v08.1 |
| `scripts/utilities/patch-ghx-v135-cotas-stories-2026-10-12.py` | parche del canvas (aplicado) |
| `gh-definitions/F1_CONTEXTO_v13.5.ghx/.gh` | re-embed #198 (v08.1) + #200 (cabecera); `.gh` regen |

## 5. Pendientes inmediatos (para la sesión)

1. Corrida real del canvas → leer cotas y confirmar `niveles_deseados.json` (revisar ajustes de snap).
2. Crear stories en AC + `--check` (0 faltantes) y re-correr para ver zones con Name/Number BEP.
3. D5 restante: Zone **Categories** en AC + cableado de `Category`; Subfloor=0; áreas netas (F4).
4. Retiros frente/fondo=0 en base (antejardín 0) + aviso "no alcanza borde derecho"/margen 145 m².
5. Botón/endpoint de orquestador para el flag de stories (como lados/GFA) — opcional.
