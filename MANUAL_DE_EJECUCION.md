# MANUAL DE EJECUCIÓN — DiseñoParametrico (F0 → F3, hasta Morphs)

> Última actualización: 2026-08-23 · Equipo: i5-12600K · 64 GB RAM · RTX 4070 Ti · Win 11 Pro
> Alcance de este manual: arrancar el front-end (orquestador), recorrer F0→F1→F2→F3,
> ejecutar el **Paso Manual** Grasshopper↔ArchiCAD, y terminar con la **generación de Morphs**.
> Próximo ajuste (futuro, no bloquea): F3 emitirá **Zonas** de ArchiCAD en vez de Morphs.

---

## 0. Prerrequisitos y condiciones

Ejecutar **siempre desde la raíz** del proyecto:

```powershell
cd D:\Work\PROJECTS\DiseñoParametrico
```

- **Python del proyecto**: usar `.\.venv\Scripts\python.exe` (no el Python global). No hace falta activar el venv.
- **Rhino 8 + Grasshopper abiertos**, con el canvas maestro: `gh-definitions\F1_Contexto_Base-Editado_v02.gh`.
- **ArchiCAD abierto** con la **Live Connection** activa (plugin Graphisoft, componentes `AC_*`). Puerto CommandConnection: **19723 → 19724** en este equipo (si cambia, ver `scripts\utilities\cambiar_puerto_archicad.ps1`).
- **Unidades de Rhino en METROS** (nunca mm).
- **GHPython**: usar SIEMPRE el componente **"Script" clásico con IronPython 2.7**. **NUNCA** el componente "Python 3 Script" (bug Rhino 8: sella el componente).
- **Coordenadas locales** (0,0,0) con metadatos SIRGAS; **no** usar coordenadas globales como input directo en GH/ArchiCAD.

---

## 1. Arranque del front-end (orquestador web)

El orquestador es el formulario que centraliza las decisiones del operador y ejecuta el
pipeline F1→F2→F3 automatizable.

```powershell
cd D:\Work\PROJECTS\DiseñoParametrico
.\.venv\Scripts\python.exe src\orquestador\servidor.py --puerto 8900
```

Abrir en el navegador: **http://127.0.0.1:8900**

Qué permite:
- Seleccionar CHIP (carga identidad + contexto + vecinos por lado).
- Definir **modalidad del dueño del lote** (`modalidad_dueno_lote`: `venta_completa` /
  `participacion` / `aporte_completo` + `pago_parcial_pct`).
- Visualizar el **plano del predio (lados)** en SVG, con clic-ciclo para clasificar cada lado
  (`indefinido → vía → predio/vecino → espacio público → libre`), norte siempre arriba.
- Ejecutar **F2** (calcular) y **F1→F2→F3** (pipeline) desde un botón.
- **Guardar** → escribe `proyecto.json` (con `modalidad_dueno_lote`), consumible por el canvas GH.

Rhino.Compute (opcional, para Hops/headless; puerto 6001):

```powershell
powershell scripts\rhino-compute\start-compute.ps1
```

---

## 2. F0 — Setup BIM (capas ArchiCAD) [ya hecho]

Capas ya creadas (XML único en `src\interfases-archicad\F1_Layers_Proyecto_v01.xml`). Si
falta alguna, se crean desde Grasshopper vía Live Connection. No repetir este paso salvo
que el archivo ArchiCAD sea nuevo.

---

## 3. F1 — ETAPA 1: fetch y envío a ArchiCAD

```powershell
.\.venv\Scripts\python.exe scripts\utilities\fetch-urban-context-v6.py --chip <CHIP>
```

Genera `data\pot-cache\<CHIP>-contexto.json` (coordenadas locales + metadatos SIRGAS +
topografía). Si no existe este JSON, el pipeline se detiene y pide ejecutar el fetch.

En Grasshopper, ejecutar **`F1_ETAPA1_CONTEXTO_v02`** (GHPython IronPython 2.7). Lee el JSON
y emite `lot_curve`, `vecinos_curves`, `vias_oficiales`, `espacios_publicos`. Conectarlas a
los componentes Live Connection (`AC_*`) para **crear capas** y **enviar la geometría** a
ArchiCAD.

---

## 4. PASO MANUAL — Clasificación en ArchiCAD (ida y vuelta)

Este es el único paso que no se puede automatizar headless. Requiere sesión abierta de Rhino
+ ArchiCAD y la Live Connection.

### 4.1 Ida (Grasshopper → ArchiCAD): clasificar en capas (grupos)

En ArchiCAD, mover cada elemento a su capa (grupo) señalada:

| Capa (grupo) | Contenido |
|---|---|
| `00-00-10_Lote_proyecto` | Predio objetivo |
| `00-20-20_Elementos_entorno_urbano` | Polígonos de vías |
| `00-20-30_Ejes_vias` | Ejes de vías (líneas centrales) |
| `70-50-10_Zonas_verdes_publicas` | Parques / plazas / zonas verdes |
| `70-30-20_Andenes_preexistentes` | Andenes / espacio público peatonal |
| `70-20-20_Perimetros_vecinos` | Perímetros de predios vecinos |
| `70-20-30_Volumetrias_vecinas` | **Morphs** de construcciones existentes de vecinos (manual) |
| `00-10-20_Elementos_referencia` | Líneas de referencia / ejes auxiliares |

Reglas:
- Un borde es **Frontal** si su distancia a CUALQUIER curva de vía es < 15 m; si no, Lateral/Posterior.
- Vías = dos fuentes combinadas con **Merge** en GH: `vias_oficiales` (JSON POT) + `vias_manuales`
  (dibujadas en ArchiCAD en las capas de entorno).
- Construir **manualmente** las volumetrías existentes de vecinos como **Morph** en
  `70-20-30_Volumetrias_vecinas` (no hay modelo 3D público de Bogotá). Validar con
  `validate-neighbors.py` antes de pasar a GH.
- (Opcional) ortofoto de referencia: `fetch-aerial-photo-v6.py`, colocar en capa
  `00-20-20_Foto_Aerea_Referencia` al 50% de transparencia para verificar alineación.
- ⚠️ Curvas con arcos de la Live Connection: normalizar a curva nativa (componente Curve directo
  tras Deconstruct, o Divide Curve + Polyline). Los scripts GHPython rechazan el tipo "Planar Curve".

### 4.2 Vuelta (ArchiCAD → Grasshopper): devolver los grupos clasificados

Con componentes Live Connection **`GetElements`** (Type hint = **Curve**, **List Access** +
**Flatten**), traer las curvas clasificadas desde ArchiCAD a Grasshopper. Conectar la salida
**C** del Deconstruct DIRECTO al script GHPython (no reconstruir con Explode/PolyLine).

Encadenar en GH:

```
GetElements (ArchiCAD) → F1_ETAPA2_LADOS_v06 → F1_ETAPA2_PATIO_v02 → F1_ETAPA2_NORMATIVA_v08
                        → (F1_OVERRIDE_USO_v01 opcional) → F1_EXPORTAR_GFA_v02
```

`F1_EXPORTAR_GFA_v02` escribe automáticamente `data\fase-2-demanda\<CHIP>-gfa-gh.json`
(puente a F2, sin toggle).

---

## 5. F2 — Modelo financiero

Vía orquestador (botón "Calcular F2") o CLI:

```powershell
.\.venv\Scripts\python.exe src\fase-2-demanda\F2_Modelo_Financiero\F2_DEMANDA_MOTOR_v03.py --parametros parametros_<CHIP>_mercado2026.json
.\.venv\Scripts\python.exe src\fase-2-demanda\F2_Modelo_Renta\F2_RENTA_MOTOR_v03.py --parametros parametros_<CHIP>_renta.json
```

Los motores leen el GFA desde `data\fase-2-demanda\<CHIP>-gfa-gh.json` (si no se pasa `--gfa`).
La modalidad del dueño del lote viaja como `modalidad_dueno_lote` (el motor conserva un adaptador
interno `aporte_suelo` por retrocompatibilidad).

---

## 6. F3 — Distribución, accesos y Morphs

### 6.1 Automatizable (CLI)

```powershell
.\.venv\Scripts\python.exe src\fase-3-masa\F3_DISTRIBUCION_v01.py A          # caso A|B|B_SALUD|C
.\.venv\Scripts\python.exe src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py --caso A
```

`F3_DISTRIBUCION` emite `programa-areas.json` (balanceado, esquema GH v04/v05). Alternativa
por CHIP: `F3_DISTRIBUCION_v01.py --chip <CHIP> --escenario D_MIXTO`.

### 6.2 Manual (Rhino/GH): masa → Morphs

En Grasshopper, ejecutar **`F3_VOLUM_GENERADOR_v07.py`** (GHPython IronPython 2.7):

| Entrada | Conectar desde |
|---|---|
| `envelope_por_piso` | Salida `envelope_por_piso` de `F1_ETAPA2_NORMATIVA_v07` |
| `json_path` | `src\fase-3-masa\casos\<CASO>\programa-areas.json` |
| `floor_height` | 3.0 (default; se prefiere `altura_z` del JSON) |

| Salida (mesh) | Destino (Live Connection) |
|---|---|
| `volumenes_principales_mesh` | componente `AC_*` de creación de **Morph** |
| `volumenes_circulacion_mesh` | Morph (escaleras + ascensores) |
| `volumenes_servicios_mesh` | Morph (ductos/basuras/cuarto técnico) |
| `losas_mesh` | Morph (losa con hueco) |
| `volumenes_*` / `losas` (Brep) | Preview Rhino / F4 Ladybug |

El Morph de ArchiCAD requiere `Rhino.Geometry.Mesh` (no Brep). El destino es ArchiCAD vía
Live Connection (no se hornea en Rhino).

---

## 7. Nota: Morphs ahora → Zonas después (futuro)

Hoy F3 termina produciendo **Morphs**. El ajuste pendiente es que `F3_VOLUM_GENERADOR` +
Live Connection emitan **Zonas** de ArchiCAD (objetos con atributos de uso/ocupación), que
son mucho más útiles que un Morph simple para el round-trip de **Ladybug (F4)**. **No bloquea**:
hasta que se implemente, el flujo funciona hasta la producción de Morphs.

---

## 8. Resumen de comandos

```powershell
cd D:\Work\PROJECTS\DiseñoParametrico

# Front-end (orquestador)
.\.venv\Scripts\python.exe src\orquestador\servidor.py --puerto 8900     # http://127.0.0.1:8900

# Orquestador por consola (checklist guiado)
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --status
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --run --chip AAA0127AZPA --caso A --modo mixto --yes
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --checklist

# F1 fetch
.\.venv\Scripts\python.exe scripts\utilities\fetch-urban-context-v6.py --chip <CHIP>

# F2
.\.venv\Scripts\python.exe src\fase-2-demanda\F2_Modelo_Financiero\F2_DEMANDA_MOTOR_v03.py --parametros parametros_<CHIP>_mercado2026.json

# F3
.\.venv\Scripts\python.exe src\fase-3-masa\F3_DISTRIBUCION_v01.py A
.\.venv\Scripts\python.exe src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py --caso A

# Tests
.\.venv\Scripts\python.exe -m pytest -q

# Rhino.Compute (opcional)
powershell scripts\rhino-compute\start-compute.ps1
```

Mapa caso → chip: `A=AAA0127AZPA`, `B/B_SALUD=AAA0030JKOE`, `C=AAA0039KRMR`.
