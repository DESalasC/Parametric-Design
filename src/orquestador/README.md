# Orquestador + Checklist — DiseñoParametrico (Parte 1: F1 → F3)

Punto de entrada único para reducir errores en las ejecuciones manuales.
Recoge las variables una vez, ejecuta lo automatizable validando cada salida,
guía los pasos manuales (Rhino/Grasshopper/ArchiCAD) y genera un checklist HTML.

## Requisitos

- Entorno de Python del proyecto: `.venv` (creado con `entorno_python.ps1`).
- Ejecutar desde la raíz del proyecto `D:\Work\PROJECTS\DiseñoParametrico`.

## Cómo usar

```powershell
# 1) Ver el estado sin ejecutar nada (seguro)
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --status

# 2) Ejecutar el flujo guiado (interactivo, pide confirmaciones)
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --run

# 3) Ejecutar sin preguntar (no interactivo, para automatización)
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --run --chip AAA0127AZPA --caso A --modo mixto --yes

# 4) Generar el checklist HTML visual
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --checklist
```

El checklist se genera en `src\orquestador\checklist.html` y se abre con doble clic.

## Variables (fuente única: `parametros_pipeline.json`)

| Variable | Significado | Default |
|---|---|---|
| `chip` | CHIP del predio | `AAA0127AZPA` |
| `caso` | Caso F3 (`A`/`B`/`B_SALUD`/`C`) | `A` |
| `modo` | `venta` / `renta` / `mixto` | `mixto` |
| `gfa_m2` | Override de GFA (null = usa export F1) | `null` |
| `costo_lote_cop` | Override costo de lote (null = default F2) | `null` |

**Mapa caso → chip:** `A=AAA0127AZPA`, `B/B_SALUD=AAA0030JKOE`, `C=AAA0039KRMR`.

## Pasos que cubre (Parte 1)

| # | Paso | Tipo | Script |
|---|---|---|---|
| 1.1 | Fetch contexto normativo | auto | `scripts/utilities/fetch-urban-context-v7.py` |
| 1.2 | Exportar GFA | manual (Rhino) | `F1_EXPORTAR_GFA_v02` |
| 2.1 | Modelo financiero venta | auto | `F2_DEMANDA_MOTOR_v03.py` |
| 2.2 | Modelo Build-to-Rent | auto | `F2_RENTA_MOTOR_v03.py` |
| 3.1 | Distribución espacial | auto | `F3_DISTRIBUCION_v02.py` |
| 3.2 | Accesos por uso | auto | `F3_ACCESOS_INTEGRADOR_v02.py` |
| 3.3 | Masa en Rhino + Morphs | manual (Rhino/ArchiCAD) | `F3_VOLUM_GENERADOR_v07.py` |

### Acople §2 → modelado (2026-09-29)

La generación de masa del front-end ya **no depende de un caso pre-generado**: al pulsar
"Generar masa (F3)" / "Pipeline completo" se envían los **usos marcados en la sección 2** y
los parámetros de **bloques** (sección 4); el servidor deriva el escenario F2 (`D_MIXTO` /
`D_MIXTO_SALUD` según usos) y `F3_DISTRIBUCION_v02` filtra/renormaliza el mix y escribe
`bloques.json` (multivolumen). El selector "Escenario pre-generado" queda solo como
referencia para ver resultados ya generados.

## Límite honesto

Los pasos **manuales** (exportar GFA en Rhino, masa + Morphs en ArchiCAD) **no se
pueden automatizar headless** (necesitan la sesión abierta de Rhino y la Live
Connection de ArchiCAD). El orquestador los convierte en checklist guiado con
verificación del artefacto, en vez de pasos a ciegas.

## Parte 2 (F4 → F5)

Se desarrollará aparte, bajo los mismos estándares. Incluirá F4 (Ladybug + EPW
Bogotá) y F5 (inyección BIM vía Tapir). El enlace está en el checklist HTML.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_orquestador.py -q
```


## Canvas parametrizado (carga de `proyecto.json`)

El canvas de Grasshopper hoy usa ~12 inputs sueltos (tipología, piso adicional,
bonificación, altura de placa, antejardín/voladizo, empate posterior, tratamiento,
caso, alineación del núcleo, usos, modos, escenarios). Para reducirlos a un único
punto de entrada se agregó:

- **`F0_LOAD_PROYECTO_v01.py`** — componente GHPython (IronPython 2.7) que lee un
  `proyecto.json` y expone todas esas variables como salidas. Validación:

  ```powershell
  .\.venv\Scripts\python.exe -m pytest tests\test_f0_load_proyecto.py -q
  ```

- **Esquema canónico** de `proyecto.json` (el mismo que guarda el formulario
  `POST /api/proyecto`):

  ```json
  {
    "nombre": "proyecto-01",
    "chip": "AAA0127AZPA",
    "variables": {
      "tipologia": "Continua",
      "piso_adicional": false,
      "tipo_bonificacion": "Ninguno",
      "floor_height_user": 3.0,
      "antejardin_decision": "Según reglamentación",
      "empate_posterior_pisos": 0,
      "empate_posterior_m": null,
      "tratamiento": "Consolidación",
      "caso": "A",
      "alineacion_nucleo": 1
    },
    "usos": ["Vivienda", "Comercio"],
    "modos": ["venta"],
    "escenarios": ["A_VIS", "B_ESTANDAR", "C_LUJO"]
  }
  ```

### Cableado (paso manual en Rhino)

El loader reemplaza los inputs sueltos, pero el cableado del canvas es **manual**
(requiere sesión de Rhino/Grasshopper abierta):

1. Crear el componente **"Script"** (clásico, NO "Python 3 Script") y pegar el
   contenido de `F0_LOAD_PROYECTO_v01.py`; seleccionar **IronPython 2.7**.
2. Añadir dos inputs: `ruta_json` (string, Item Access) y `caso_default` (string,
   Item Access).
3. Conectar `ruta_json` a un panel con la ruta del `proyecto.json` generado por el
   formulario (`data/activo/proyecto.json`, espejo reescrito en cada
   guardado por `POST /api/proyecto`).
4. Conectar las salidas (`tipologia`, `caso`, `usos`, etc.) a los componentes que
   antes recibían los inputs sueltos (F1_LADOS, F1_NORMATIVA, F3_VOLUM, F3_ACCESOS).
5. Ejecución **por clic o Tapir**: se re-escribe el `proyecto.json` (formulario o
   Tapir) y se dispara la solución; no hay que re-cablear nada.
