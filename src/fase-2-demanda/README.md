# Fase 2 - Demanda

Motor de viabilidad comercial y programa de áreas.

## Scripts migrados (base de referencia)

- F2_DEMANDA_MOTOR_v01.py - motor principal
- F2_OPTIMIZADOR_ADYACENCIA_v01.py - optimización adyacencia
- F2_PROG_INTERIOR_v01.py - programa interior
- F2_PROGRAMA_AREAS_v01.py - programa de áreas

## JSONs disponibles

- data/pot-bogota/edificabilidad-estructurada.json - rangos de edificabilidad
- data/pot-bogota/incentivos-670.json - incentivos urbanísticos (mezcla usos 8%→3%)

## Próximos pasos

1. Adaptar para leer área neta construible del caché Fase 1
2. Integrar incentivos del 670 (Tipo 1: reducción mezcla usos)
3. Crear tests con casos reales
