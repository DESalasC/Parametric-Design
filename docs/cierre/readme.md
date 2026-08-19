# Paquete de entrega — DiseñoParametrico (cierre 2026-08-18)

Contenido del paquete de cierre:

| Archivo | Propósito |
|---|---|
| `01-estado-y-alcance.md` | Alcance, qué está completo, qué falta, qué se considera terminado |
| `02-bitacora.md` | Versiones, decisiones (ADR) y pruebas |
| `03-informe-final.html` | Informe final consolidado (Precisión suiza) |
| `README.md` | Índice + instrucciones de uso y transferencia (este archivo) |

## Cómo abrir, operar y mantener

### Requisitos
- Python 3.12 con entorno virtual `.venv` (creado con `entorno_python.ps1`).
- Dependencias: `fiona`, `geopandas`, `shapely`, `pytest` (ver `requirements.txt`).
- Rhino 8 + Grasshopper (para F1/F3 geométrico) y ArchiCAD (para capas y Morphs).

### Ejecutar desde la raíz `D:\Work\PROJECTS\DiseñoParametrico`

```powershell
# 1) Ver estado del pipeline (seguro, no ejecuta nada)
.\.venv\Scripts\python.exe src\orquestador\run_pipeline_v01.py --status

# 2) Clasificar vecinos por lado de un lote
.\.venv\Scripts\python.exe src\orquestador\vecinos_por_lado.py AAA0127AZPA

# 3) Modelo financiero (venta) por chip
.\.venv\Scripts\python.exe src\fase-2-demanda\F2_Modelo_Financiero\F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_mercado2026_validado.json --chip AAA0127AZPA

# 4) Distribución espacial por caso (A|B|B_SALUD|C)
.\.venv\Scripts\python.exe src\fase-3-masa\F3_DISTRIBUCION_v01.py A

# 5) Formulario interactivo (interfaz web)
.\.venv\Scripts\python.exe src\orquestador\servidor.py --puerto 8900
# abrir http://127.0.0.1:8900

# 6) Suite de pruebas
.\.venv\Scripts\python.exe -m pytest -q
```

### Dónde modificar cada cosa

| Qué cambias | Archivo |
|---|---|
| Variables de decisión del lote | `proyectos/_provisional/proyecto.json` |
| Usos permitidos por sector | `data/pot-bogota/usos-por-sector.json` |
| Área de actividad por lote | `data/pot-bogota/areas-actividad.json` |
| Parámetros financieros por chip | `src/fase-2-demanda/F2_Modelo_Financiero/parametros_<CHIP>_venta.json` |
| Catálogo base de usos | `src/orquestador/servidor.py` (constante `USOS_CATALOGO`) |
| Normativa / retiros / empates | `src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v08.py` |

### Transferencia

El repositorio es la fuente de verdad y está versionado en git (83 commits). Para transferir a otro equipo: clonar el repo, recrear el entorno con `entorno_python.ps1`, y copiar la geobase `POT_Decreto_555_2021_Bogota_D_C.gdb` (no versionada, en `D:\Work\LIBRARIES\POT_Bogota\`) porque los `data/pot-cache/*-contexto.json` se regeneran desde ella.
