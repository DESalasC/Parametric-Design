# DiseñoParametrico — Ecosistema BIM-GIS-AI para diseño arquitectónico paramétrico en Bogotá

**Última actualización:** 2026-08-18 · **Hardware:** i5-12600K · 64 GB RAM · RTX 4070 Ti · Win 11 Pro

Sistema que automatiza el flujo completo de prefactibilidad arquitectónica: contexto normativo
POT/NSR-10 desde geodatos oficiales, análisis de demanda y modelo financiero, generación de masa,
análisis ambiental y inyección BIM nativa en ArchiCAD vía Grasshopper.

## Fases del proyecto (estado real)

| Fase | Módulo | Estado | Contenido |
|---|---|---|---|
| **F0** | Setup BIM | ✅ Hecha | Layers ArchiCAD (GuBIMclass), plantilla XML |
| **F1** | Contexto normativo y lote | ✅ Hecha | Pipeline modular v26 (2 etapas): fetch contexto → clasificación de lados → patios → normativa/envolvente. Linaje legacy en `_legacy\` |
| **F2** | Demanda + modelo financiero | ✅ Hecha | `src\fase-2-demanda\`: 4 scripts de pipeline + `F2_Modelo_Financiero\` (motor v3.0: KPIs, alertas, sensibilidad, escenarios D/E, flujo de caja, hook GFA desde F1) + `F2_Modelo_Renta\` (motor v3.0: construir para arrendar CP/LP, TIR/VPN/cap rate, suelo soportable, hook GFA desde F1). Re-evaluado 2026-08-16 con GFA F1 v06 (1.461 m²): C_LUJO casi viable en compra, aporte/arriendo viables, BTR marginal |
| **F3** | Generación de masa | Avanzada | `src\fase-3-masa\`: `F3_DISTRIBUCION_v01` (matriz/layout/programa-areas balanceado), `F3_VOLUM_GENERADOR_v07` (v07.24: núcleo excluido, circulación/servicios separados, núcleo contra medianera, **volumetría por uso**), `F3_ACCESOS_INTEGRADOR_v02` (accesos por uso + segregación de flujos), casos A/B/B_SALUD/C regenerados, prueba real Rhino 8.33 (caso A) |
| **F4** | Análisis ambiental | 🔶 Iniciada | `src\fase-4-ambiental\`: F4_LADYBUG_ANALISIS v02 |
| **F5** | Inyección BIM nativa | ⏳ Pendiente | `src\fase-5-bim\` (solo README) |

## Estructura del proyecto

```
DiseñoParametrico/
├── README.md / CLAUDE.md        # Overview vivo + reglas del proyecto
├── config/                      # field-whitelist.json (campos POT relevantes)
├── data/                        # Única raíz de datos
│   ├── pot-cache/               # JSON por predio (<CHIP>-contexto.json) + ortofotos
│   ├── fase-2-demanda/          # JSON de entrada del pipeline (actual + alternativa GFA 1054)
│   ├── pot-bogota/ nsr-10/      # Normativa estructurada (JSON)
│   ├── ghx-samples/             # Corpus de muestras GHX (ladybug, tapir, archicad) — regenerable
│   ├── lotes-ejemplo/ clima/ ideca-cache/ neighbors/ pot-geojson/
├── gh-definitions/              # Canvas Grasshopper: F1_Contexto_Base-Editado_v02 (maestro) +
│                                # referencias de conexión/componentes; versiones viejas en _archive\
├── scripts/                     # rhino-compute/ (start-stop-health) + utilities/
├── src/                         # Código por fase (ver tabla arriba); tests en tests/ raíz
├── tests/                       # Pytest Fase 1 (test_fetch_contexto, test_normativa_calculos, test_patio_esquina)
├── exports/ logs/               # Salidas y logs automáticos (gitignored)
├── LIBRARIES/                   # Referencias externas (IDECA)
├── inventario_migracion/        # CSV de inventario de migración (histórico)
└── .venv/ pyproject.toml uv.lock requirements.txt entorno_python.ps1
```

**Decisiones de estructura (2026-08-13):**
- La documentación vive **exclusivamente** en el vault de Obsidian `D:\Work\NOTES\obsidian-vault` (única fuente de verdad). Este README es el mapa, no el detalle.
- El nombre del proyecto es **`DiseñoParametrico`** (con ñ). Se evaluó renombrar a ASCII (`DisenoParametrico`) por problemas de codificación en consolas, pero Windows/Python/Git/Obsidian lo manejan correctamente y el renombrado rompería `.venv` y ~100 referencias sin beneficio para el operador. Se mantiene el nombre y se exige consistencia textual.
- La limpieza de versiones obsoletas se aplica por linaje: vigentes a nivel raíz, anteriores en `_legacy\` o `_archive\` (nunca se borran sin respaldo git).

## Cómo ejecutar (rápido)

```powershell
# Fase 1 — contexto (genera data\pot-cache\<CHIP>-contexto.json)
python scripts\utilities\fetch-urban-context-v6.py --chip <CHIP>

# Tests
pytest tests\

# Fase 2 — modelo financiero (ver src\fase-2-demanda\F2_Modelo_Financiero\MANUAL_DE_USO.md)
cd src\fase-2-demanda\F2_Modelo_Financiero
python F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_mercado2026.json
python F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_gfa1054_mercado2026.json  # alternativa curaduría

# Fase 2 — modelo Build-to-Rent (ver src\fase-2-demanda\F2_Modelo_Renta\MANUAL_DE_USO.md)
cd ..\F2_Modelo_Renta
python F2_RENTA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_renta.json
python F2_RENTA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_renta_gfa1054.json  # alternativa curaduría
# (sin --gfa: los motores leen data\fase-2-demanda\<CHIP>-gfa-gh.json, generado por F1_EXPORTAR_GFA_v02)

# Orquestador (formulario web: pipeline F1->F2->F3 en un boton)
python src\orquestador\servidor.py --puerto 8900   # abrir http://127.0.0.1:8900
python src\orquestador\run_pipeline_v01.py --status

# Rhino.Compute
powershell scripts\rhino-compute\start-compute.ps1
```

## Documentación (vault de Obsidian)

`D:\Work\NOTES\obsidian-vault\` — índice en `00-index\mapa-conocimiento.md`. Contiene: diarios
(`60-diario\`), documentación por fase (`20-fases\`), arquitectura y ADRs (`10-arquitectura\`),
referencia normativa y de mercado (`30-referencia\`), lecciones (`50-lecciones\`).

## Reglas obligatorias

Ver `CLAUDE.md` (reglas de GHPython/IronPython, capas ArchiCAD, normativa POT/NSR-10, coordenadas
MAGNA-SIRGAS, clasificación híbrida ADR-008, estructura de datos). Resumen crítico:
- GHPython: componente "Script" clásico (IronPython 2.7), nunca "Python 3 Script" (bug Rhino 8).
- Pipeline Fase 1 vigente: modular ETAPA1/ETAPA2 (v26); normativa: `F1_ETAPA2_NORMATIVA_v08` +
  exportador `F1_EXPORTAR_GFA_v02` (puente automático `<CHIP>-gfa-gh.json` → motores F2 v03).
- Lotes como polilíneas, coordenadas locales (0,0,0), JSON del fetch como única entrada de Fase 1.
- Git: commitear al final de cada sesión (ver historial de consolidaciones 2026-08-13).
