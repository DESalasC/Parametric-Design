# Documento de estado y alcance — DiseñoParametrico

Fecha de corte: **2026-08-18** · Cierre de fase: **F1–F3 (v1.0)** · Repositorio: `D:\Work\PROJECTS\DiseñoParametrico`

> **Alcance del cierre**: este documento registra el cierre de la fase **F1→F3** (contexto normativo → demanda → masa). El proyecto tiene **6 fases (F0–F5)**; F4 (ambiental) y F5 (BIM) son fases posteriores y quedan fuera de este cierre.

## 1. Qué abarca el proyecto

DiseñoParametrico es un ecosistema **BIM-GIS-AI** para el diseño arquitectónico paramétrico en Bogotá. Toma un lote (CHIP), extrae su contexto urbano y normativo (POT Decreto 555/2021 + geobase), calcula la envolvente edificable (retiros, empates, escalonamiento, GFA/IO/IC), evalúa la demanda financiera (venta y renta) y genera la masa volumétrica por uso.

Pipeline por fases:

| Fase | Responsabilidad | Estado |
|---|---|---|
| F0 | Orquestación: carga `proyecto.json` y expone variables del canvas | ✅ Estable (v01.3) |
| F1 | Contexto normativo y lote (fetch, lados, patio, normativa, GFA) | ✅ Estable (v08) |
| F2 | Demanda y modelo financiero (venta + Build-to-Rent) | ✅ Estable (v03) |
| F3 | Generación de masa (distribución, volumen, accesos) | ✅ Automático · ⚠️ Rhino manual |
| F4 | Análisis ambiental (Ladybug/EPW) | ⚠️ Scripts v02, no validado en Rhino |
| F5 | Integración BIM (ArchiCAD) | 📋 Documentación |

## 2. Qué se ha completado

- **F1**: extracción de contexto (3 capas viales + vecinos + espacios públicos), clasificación de lados (regla 15 m + paralelismo), patios, motor normativo v08 (retiros, empate lateral por lado, escalonamiento, IO/IC/altura), exportador GFA.
- **F2**: motor de venta v03 (escenarios A_VIS/B_ESTANDAR/C_LUJO/D_MIXTO, sensibilidad, aporte parcial `pago_parcial_pct`) y motor de renta v03 (CP/LP).
- **F3**: distribución espacial por uso, generador volumétrico v07 (escalonado, núcleo contra medianera) y accesos por uso. Prueba real de masa en Rhino 8 (caso A: 15 objetos `.3dm`).
- **Orquestador**: formulario interactivo + servidor local (F1→F3), `F0_LOAD_PROYECTO_v01`, clasificación de vecinos por lado, integración de área de actividad.
- **Validación**: suite pytest **234 passed** (22 archivos).

## 3. Qué falta (pendientes al cierre)

1. **F3 masa en Rhino**: cableado del canvas ya commiteado; falta la ejecución manual final de Morphs en ArchiCAD.
2. **Usos por sector (definitivo)**: sector UPL extraído de la geobase (`sectores-uso-lotes.json`); la lista final predio a predio requiere Sinupot / CU-5.4.x o el cuadro del Decreto 555 Art. 243.
3. **F4 ambiental**: ejecutar Ladybug/EPW en Rhino (scripts listos, sin corrida validada).
4. **F5 BIM**: materializar la integración ArchiCAD (capas y story-sync preparados).

## 4. Qué se considera "terminado"

- **Terminado (automatizable)**: F0, F1, F2 y F3 — reproducibles por CLI con salidas deterministas y 234 tests verdes.
- **Terminado (manual, requiere Rhino)**: cableado del canvas y generación de masa; validación visual del operador.
- **No terminado**: usos por sector definitivo (Sinupot / CU-5.4.x), F4/F5 en ejecución.

## 5. Supuestos

- La geobase POT es imperfecta (vías incompletas, zonas verdes como "vecinos"); la clasificación automática es **sugerencia**, el operador confirma/override.
- La lógica de mapeo se mantiene en 3 lugares (Python + IronPython + JS); exige tests unitarios para no divergir.
- Los derivados (`data/pot-cache/*`, `resultados/*.csv`, `.3dm`) se regeneran y no son fuente de verdad.
