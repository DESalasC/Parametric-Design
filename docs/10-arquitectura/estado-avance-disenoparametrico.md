# Estado de Avance - DiseñoParametrico

## Tabla Única de Versiones Vigentes (T-14)

| Componente | Versión Vigente | Estado | Última Actualización |
|------------|----------------|--------|----------------------|
| Canvas Base Editado | F1_Contexto_Base-Editado_v03.ghx | Vigente | 2026-09-01 |
| Script F1 Etapa 1 - Contexto | F1_ETAPA1_CONTEXTO_v02.py | Vigente | 2026-08-24 |
| Script F1 Etapa 2 - Lados | F1_ETAPA2_LADOS_v06.py | Vigente | 2026-08-16 |
| Script F1 Etapa 2 - Patio | F1_ETAPA2_PATIO_v02.py | Vigente | 2026-08-15 |
| Script F1 Etapa 2 - Normativa | F1_ETAPA2_NORMATIVA_v08.py | Vigente | 2026-08-23 |
| Script F1 Override Uso (Opcional) | F1_OVERRIDE_USO_v01.py | Vigente | 2026-08-10 |
| Script F1 Exportar GFA | F1_EXPORTAR_GFA_v02.py | Vigente | 2026-08-18 |
| Script F2 Motor de Demanda | F2_DEMANDA_MOTOR_v03.py | Vigente | 2026-08-20 |
| Script F2 Modelo Financiero | F2_MODELO_FINANCIERO_v03.py | Vigente | 2026-08-21 |
| Script F2 Modelo Renta | F2_MODELO_RENTA_v03.py | Vigente | 2026-08-22 |
| Script F3 Volumen Generador | VOLUM_GENERADOR_v08.py | Vigente (Fase 3 en desarrollo) | 2026-08-19 |
| Script F3 Accesos Integrador | ACCESOS_INTEGRADOR_v02.py | Vigente (Fase 3 en desarrollo) | 2026-08-18 |
| Script F4 Ladybug Análisis | F4_LADYBUG_ANALISIS_v02.py | Vigente (Fase 4 en desarrollo) | 2026-08-25 |
| Interfaz ArchiCAD Capas | F1_Layers_Proyecto_v01.xml | Vigente | 2026-07-31 |

## Crónica 08-25 → 09-05

- **2026-08-25**: Inicio de revisión de normsativa NSR-10 A.2.5 y actualización de cuestas.
- **2026-08-26**: Corrección de manejo de capas en F1_LAYERS_XML_v02.py para garantizar capa 00-00-10_Lote_proyecto.
- **2026-08-27**: Actualización de tabla de retiros por vía según Decreto 466/2024.
- **2026-08-28**: Pruebas de integración entre F1_ETAPA2_LADOS_v06 y F1_ETAPA2_PATIO_v02.
- **2026-08-29**: Validación de umbrales de ocupación frente a COS_norma en zona Chapinero.
- **2026-08-30**: Sincronización de manifest de runs con versiones de schemas.
- **2026-08-31**: Preparación de entorno para pruebas de Rhino.Compute headless.
- **2026-09-01**: Declaración de canvas v03 como maestro tras revisión de drift.
- **2026-09-02**: Limpieza de artefactos de test y saneamiento de repositorio (A1).
- **2026-09-03**: Aprobación de manual único estable y tabla única de vigentes.
- **2026-09-04**: Inicio de diagnóstico de puerto 19723 (A5).
- **2026-09-05**: Ejecución de primer ciclo de tests de lógica pura en CPython 3.12.

## Corte del Estado de Avance

**Fecha de corte:** 2026-09-07

A esta fecha, el proyecto se encuentra en la siguiente situación:
- Fase 1 (Contexto POT + retiros + vecinos): Completada con pipeline modular v26.
- Fase 2 (Motor de demanda + modelos financieros): En desarrollo, con hook GFA desde F1 operativo.
- Fase 3 (Generación de masa): En desarrollo, volumetría por uso implementada.
- Fase 4 (Análisis ambiental): Pendiente de primera corrida con EPW real.
- Fase 5 (Inyección BIM nativa): Pendiente de resolución de bloqueo de puerto 19723.

Los puntos de control PC-0 y PC-1 están activos con criterios de aceptación definidos.
El bloqueador A5 (puerto 19723) está en diagnóstico y es prerequisite para PC-4 y partes de S3.

