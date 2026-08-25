# MANUAL DE EJECUCIÓN — DiseñoParametrico (F0 → F3, hasta Zonas de ArchiCAD)

> Última actualización: 2026-08-24 · Equipo: i5-12600K · 64 GB RAM · RTX 4070 Ti · Win 11 Pro
> Alcance de este manual: arrancar el front-end (orquestador), recorrer F0→F1→F2→F3,
> ejecutar el **Paso Manual** Grasshopper↔ArchiCAD, y terminar con la **generación de Zonas** de ArchiCAD (cuando se activa la salida de Zona) o Morphs (modo compatibilidad).
> Próximo ajuste (futuro): afinar atributos de Zona para Ladybug (F4).

---

## 0. Prerrequisitos y condiciones

Ejecutar **siempre desde la raíz** del proyecto:

```powershell
cd D:\Work\PROJECTS\DiseñoParametrico
```

- **Python del proyecto**: usar `.\.venv\Scripts\python.exe` (no el Python global). No hace falta activar el venv.
- **Rhino 8 + Grasshopper abiertos**, con el canvas maestro: `gh-definitions\F1_Contexto_Base-Editado_v02.ghx`.
- **ArchiCAD abierto** con la **Live Connection** activa (plugin Graphisoft, componentes `AC_*`). Puerto CommandConnection: **19723** (la Live Connection de GH solo conecta por 19723; mover ArchiCAD a 19724 solo sirve para la JSON/Python API). Si se bloquea, ver `scripts\utilities\diagnostico_puerto_19723.ps1 -Liberar`.
- **Unidades de Rhino en METROS** (nunca mm).
- **GHPython**: usar SIEMPRE el componente **"Script" clásico con IronPython 2.7**. **NUNCA** el componente "Python 3 Script" (bug Rhino 8: sella el componente).
- **Coordenadas locales** (0,0,0) con metadatos SIRGAS; **no** usar coordenadas globales como input directo en GH/ArchiCAD.

---

## 1. Arranque del front-end (orquestador)

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
| `00-30-10_Zonas_ArchiCAD` | **Zonas** de ArchiCAD (cuando se activa la salida de Zona en F3) |

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

## 6. F3 — Distribución, accesos y generación de Zonas o Morphs

### 6.1 Automatizable (CLI)

```powershell
.\.venv\Scripts\python.exe src\fase-3-masa\F3_DISTRIBUCION_v01.py A          # caso A|B|B_SALUD|C
.\.venv\Scripts\python.exe src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py --caso A
```

`F3_DISTRIBUCION` emite `programa-areas.json` (balanceado, esquema GH v04/v05). Alternativa
por CHIP: `F3_DISTRIBUCION_v01.py --chip <CHIP> --escenario D_MIXTO`.

### 6.2 Manual (Rhino/GH): masa → Zonas o Morphs

En Grasshopper, ejecutar **`F3_VOLUM_GENERADOR_v08.py`** (GHPython IronPython 2.7):

#### Entradas

| Entrada | Descripción | Conectar desde |
|---|---|---|
| `envelope_por_piso` | Sobrevolumen por piso (Brep o Mesh) | Salida `envelope_por_piso` de `F1_ETAPA2_NORMATIVA_v08` |
| `json_path` | Ruta al archivo `programa-areas.json` generado por F3_DISTRIBUCION | `src\fase-3-masa\casos\<CASO>\programa-areas.json` |
| `floor_height` | Altura típica de piso (metros) | 3.0 (default; se prefiere `altura_z` del JSON) |
| `salida_zona` | **Bandera booleana**: `True` para emitir Zonas, `False` para emitir Morphs (compatibilidad) | Valor fijo (`True` o `False`) o fuente de datos |

#### Salidas (dependen de `salida_zona`)

Cuando `salida_zona = False` (modo Morphs, compatibilidad):

| Salida (mesh) | Descripción | Destino (Live Connection) |
|---|---|---|
| `volumenes_principales_mesh` | Volúmenes de usos principales | componente `AC_*` de creación de **Morph** |
| `volumenes_circulacion_mesh` | Volúmenes de circulación (escaleras + ascensores) | Morph |
| `volumenes_servicios_mesh` | Volúmenes de servicios (ductos/basuras/cuarto técnico) | Morph |
| `losas_mesh` | Losas con hueco | Morph |
| `volumenes_*` / `losas` (Brep) | Preview Rhino / F4 Ladybug | — |

Cuando `salida_zona = True` (modo Zonas, nuevo):

| Salida | Descripción | Destino (Live Connection) |
|---|---|---|
| `zonas_perimetros` | Lista de listas de puntos 3D que definen el perímetro 2D de cada zona (por piso) | componente `AC_Zona` (input de contorno) |
| `zonas_pisos` | Lista de enteros indicando el número de piso (0 = planta baja, 1 = primer piso, etc.) para cada zona | componente `AC_Zona` (input de historia/nivel) |
| `zonas_atributos` | Lista de cadenas JSON con atributos de zona (uso, área, etc.) | componente `AC_Zona` (input de User Text) |
| `zonas_alturas` | Lista de alturas (en metros desde Z=0) del centro de cada zona | componente `AC_Zona` (input de altura de referencia opcional) |

> **Nota**: En modo Zona, los outputs de Morphs (`volumenes_*_mesh`, `losas_mesh`) siguen estando disponibles pero se recomiendan dejar sin conectar para evitar duplicados.

#### Flujo de datos para Zona

1. `F3_VOLUM_GENERADOR_v08.py` procesa el `programa-areas.json` y el `envelope_por_piso`.
2. Para cada uso definido en el programa-areas, genera una zona por piso donde ese uso está presente.
3. Calcula el perímetro 2D de la zona (extruido del envelope) y lo simplifica a un polígono válido.
4. Asigna el número de piso (historia) basado en la altura del envelope.
5. Crea un atributo JSON para cada zona con:
   - `uso`: nombre del uso (ej. "residencial", "comercial")
   - `area_m2`: área del perímetro en metros cuadrados
   - `piso`: número de piso (entero)
   - `altura_base_m`: altura inferior de la zona (metros desde Z=0)
   - `altura_centro_m`: altura del centro de la zona (metros desde Z=0)
6. Emite los cuatro outputs de Zona listados arriba.

#### Conexión en Grasshopper al componente Zona de ArchiCAD (Live Connection)

- `zonas_perimetros` → **Contorno** (Curve, List Access) del componente `AC_Zona`
- `zonas_pisos` → **Historia** (Integer, List Access) del componente `AC_Zona`
- `zonas_atributos` → **User Text** (String, List Access) del componente `AC_Zona` (se espera una cadena JSON por zona)
- `zonas_alturas` → **Referencia de Altura** (Number, List Access) opcional del componente `AC_Zona`

> **Importante**: El componente `AC_Zona` de ArchiCAD Live Connection espera los perímetros como curvas planas en el sistema de coordenadas local (metros). Asegúrese de que la geometría esté en el mismo sistema que el proyecto ArchiCAD (origen local 0,0,0).

---

## 7. Nota: Compatibilidad y migración

El cambio de Morphs a Zonas es **opcional y reversible** mediante la bandera `salida_zona` en el componente `F3_VOLUM_GENERADOR_v08`.
- Para mantener compatibilidad con flujos existentes que dependen de Morphs, establezca `salida_zona = False`.
- Para aprovechar los beneficios de Zonas (atributos de uso, integración directa con Ladybug F4), establezca `salida_zona = True`.

El canvas maestro `F1_Contexto_Base-Editado_v02.ghx` ha sido actualizado para incluir los cuatro nuevos outputs de Zona (índices 19-22) y el `OutputCount` se actualizó a 27.

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

# F3 (Distribución y Accesos)
.\.venv\Scripts\python.exe src\fase-3-masa\F3_DISTRIBUCION_v01.py A
.\.venv\Scripts\python.exe src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py --caso A

# F3 (Volumen → Zonas o Morphs)
# En Grasshopper, ejecutar F3_VOLUM_GENERADOR_v08.py con la bandera salida_zona según se desee.

# Tests
.\.venv\Scripts\python.exe -m pytest -q

# Rhino.Compute (opcional)
powershell scripts\rhino-compute\start-compute.ps1
```

Mapa caso → chip: `A=AAA0127AZPA`, `B/B_SALUD=AAA0030JKOE`, `C=AAA0039KRMR`.

---

## 9. Archivos modificados para la producción de Zonas

| Archivo | Modificación | Propósito |
|---|---|---|
| `src/fase-3-masa\F3_VOLUM_GENERADOR_v08.py` | - Añadida entrada booleana `salida_zona`. <br> - Refactorizada lógica para generar datos de Zona cuando `salida_zona = True`. <br> - Mantiene salida de Morphs cuando `salida_zona = False` (compatibilidad). | Permite cambiar entre Morphs y Zonas mediante una bandera. |
| `gh-definitions\F1_Contexto_Base-Editado_v02.ghx` | - Añadidos cuatro `OutputParam` para Zona: `zonas_perimetros` (índice 19), `zonas_pisos` (20), `zonas_atributos` (21), `zonas_alturas` (22). <br> - Actualizado `OutputCount` de 23 a 27. | Expande los outputs disponibles del canvas para conectar a componentes Zona de ArchiCAD. |

---

## 10. Próximos pasos

- Validar la generación de Zonas con datos de caso de prueba.
- Ejecutar tests unitarios para la nueva lógica de Zona en `F3_VOLUM_GENERADOR_v08.py`.
- Documentar en el vault de Obsidian las decisiones de diseño para los atributos de Zona.
- Estudiar el uso de las Zonas generadas en el flujo de Ladybug (F4) para análisis de energía solar y luminosidad.