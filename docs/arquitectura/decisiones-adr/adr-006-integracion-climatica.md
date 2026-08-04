# ADR-006: Integración Climática Transversal en el Pipeline DiseñoParametrico

**Fecha:** 2026-08-03
**Estado:** Propuesto

## Contexto

El pipeline actual considera normativa (POT, NSR-10) y contexto urbano (catastro), pero ignora el contexto ambiental hasta la Fase 4 (Ladybug). Bogotá tiene un clima tropical de altura único (4.7°N, 2640 msnm) con:
- Radiación solar intensa (menor atmósfera que filtra UV)
- Sin estaciones marcadas (12°C-20°C todo el año)
- Regímenes de lluvia bimodales (abril-mayo, octubre-noviembre)
- Vientos dominantes del NE y SW

El usuario requiere que el clima informe **todas las fases** del diseño, no solo el análisis final.

## Decisión

Integrar datos climáticos (EPW) de forma transversal en todo el pipeline, con dos niveles de granularidad:
- **Mensual** (F1-F3): para decisiones rápidas de diseño temprano
- **Horario** (F4): para análisis detallado con Ladybug y optimización con Wallacei

### Arquitectura propuesta

```
NUEVA CAPA: data/clima/
├── bogota_epw/                        # Archivos EPW
│   ├── bogota_skbo.epw                # EPW principal (Aeropuerto El Dorado)
│   └── bogota_ideam.epw               # EPW alternativo (estación IDEAM)
├── clima-mensual.json                 # Resúmenes mensuales precalculados
├── rosa-vientos.json                  # Frecuencia direcciones viento
├── solar-path-bogota.json             # Carta solar para latitud 4.7°N
└── confort-termico.json              # Rangos confort adaptativo Bogotá
```

### Integración por fase

#### F1 — CONTEXTO (nuevo: contexto climático)
```
Script nuevo: F1_CONTEXTO_CLIMA_v01.py

Función:
- Cargar archivo EPW de Bogotá
- Generar resúmenes mensuales (temp media/max/min, humedad, radiación, viento)
- Calbrar rosa de vientos dominantes
- Generar carta solar para latitud 4.7°N
- Identificar orientaciones críticas (norte = sombra permanente, sur = sol todo el año)
- Salida: JSON con datos climáticos mensuales + recomendaciones de orientación

Entradas:
- Ruta al archivo EPW
- Coordenadas del lote (ya disponibles en caché POT)

Salidas:
- clima_context: JSON con:
  - temp_mensual: {media, max, min} por mes
  - humedad_mensual: {media, max, min} por mes
  - radiacion_solar_mensual: W/m² por mes (suma diaria)
  - viento_dominante: {direccion, velocidad_media} por mes
  - precipitacion_mensual: mm por mes
  - orientacion_recomendada: grados desde norte
  - orientacion_evitar: grados desde norte
  - estaciones_lluvia: ["abril", "mayo", "octubre", "noviembre"]
```

#### F2 — DEMANDA (clima influye en programa)
```
Modificación: F2_DEMANDA_MOTOR_v01.py

Función nueva:
- Usar datos de radiación solar mensual para priorizar usos:
  - Fachadas con mayor radiación → residencial (mejor daylight)
  - Fachadas con menor radiación → comercial/oficinas (menor ganancia térmica)
- Usar precipitación para dimensionar captación de agua lluvia (áreas de cubierta)
- Usar viento dominante para ubicar ventilación natural en áreas comunes

Salidas adicionales:
- clima_programa_sugerencia: {orientacion_residencial, orientacion_comercial, captacion_agua_m2}
```

#### F3 — MASA (clima define volumetría)
```
Modificaciones a F3_VOLUM_GENERADOR_v01.py y F3_ACCESOS_INTEGRADOR_v01.py:

Nuevas restricciones climáticas:
1. Orientación:
   - Eje mayor del edificio a 15° NE (mejor balance solar/viento)
   - Evitar fachadas puras al occidente (ganancia térmica tarde)

2. Patios (Alexander Pattern 163):
   - Dimensionar patios según ángulo solar de latitud 4.7°N
   - Patio mínimo: H/2 (relación altura/profundidad para daylight)
   - Ubicar patios barlovento-sotavento según viento dominante NE

3. Sombras (aleros y quiebrasoles):
   - Calcular ángulo solar solsticio de verano (21 jun, altitud solar 65°)
   - Calcular ángulo solar solsticio de invierno (21 dic, altitud solar 61°)
   - Dimensionar alero: L = H / tan(65°) para sombra verano
   - Bogotá: ángulos muy similares todo el año (diferencia solo 4°)

4. Envelope:
   - WWR máximo por orientación:
     * Norte: 40% (sombra permanente, menos vidrio)
     * Sur: 60% (sol filtrado, más daylight)
     * Oriente: 30% (sol directo mañana, proteger)
     * Occidente: 20% (sol directo tarde, máximo protección)
   - U-values sugeridos para Bogotá (sin calefacción/refrigeración mecánica):
     * Muros: U < 2.0 W/m²K
     * Cubierta: U < 1.5 W/m²K (ganancia térmica por radiación)
     * Vidrios: U < 3.0 W/m²K, SHGC < 0.6

Script nuevo: F3_SOMBREADO_v01.py
- Genera geometría de aleros/quiebrasoles según orientación
- Calcula factor de sombra proyectada
```

#### F4 — AMBIENTAL (análisis detallado + optimización)
```
Mejoras a F4_LADYBUG_ANALISIS_v01.py:

1. Análisis con datos horarios EPW (8760 registros):
   - Daylight autónomo (sDA) por espacio
   - Ganancia térmica solar anual
   - Ventilación natural potencial (horas/año con viento útil)
   - Confort térmico adaptativo (ASHRAE 55)

2. Optimización con Wallacei:
   Objetivos evolutivos:
   - Maximizar sDA (daylight autónomo > 300 lux, 50% del tiempo)
   - Minimizar ganancia térmica solar (kWh/m²/año)
   - Maximizar horas de confort térmico natural
   - Maximizar área construible (restricción POT)
   - Minimizar costo de envelope (U-value vs material)

   Genotipo Wallacei:
   - Orientación del edificio (0°-360°)
   - Profundidad de planta (4m-12m)
   - Dimensiones de patio (ancho x largo)
   - WWR por orientación (20%-60%)
   - Altura de aleros (0.5m-2.0m)
```

#### F5 — BIM (propiedades climáticas en Archicad)
```
Mejoras a F5_MAPEO_TAPIR_v01.py:

Properties adicionales (Set_UserText):
- CLIMA_ORIENTACION_OPTIMA: grados desde norte
- CLIMA_WWR_NORTE: porcentaje
- CLIMA_WWR_SUR: porcentaje
- CLIMA_WWR_ORIENTE: porcentaje
- CLIMA_WWR_OCCIDENTE: porcentaje
- CLIMA_U_VALUE_MURO: W/m²K
- CLIMA_U_VALUE_CUBIERTA: W/m²K
- CLIMA_SDA_ESPERADO: porcentaje
- CLIMA_VENTILACION_NATURAL: horas/año
- CLIMA_AGUA_LLUVIA_CAPTAR: m³/año
```

### Script de carga de EPW

```
Script nuevo: scripts/utilities/load-epw-bogota.py

Función:
- Descarga automáticamente EPW de Bogotá desde Ladybug EPW Map
- O usa archivo local si ya existe
- Genera resúmenes mensuales (clima-mensual.json)
- Genera rosa de vientos (rosa-vientos.json)
- Genera carta solar (solar-path-bogota.json)
- Genera rangos de confort (confort-termico.json)

Fuentes EPW confirmadas:
- EPW Map (Ladybug Tools): https://www.ladybug.tools/epwmap/
- Climate.OneBuilding Colombia: https://climate.onebuilding.org/WMO_Region_3_South_America/COL_Colombia/
- Ladybug built-in: ladybug.epw.EPW.download_from_energyplus()
```

### Bogotá — Parámetros climáticos clave

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| Latitud | 4.7°N | EPW |
| Longitud | -74.15°W | EPW |
| Altitud | 2640 msnm | EPW |
| Zona climática Köppen | Cfb (templado oceanico) | EPW |
| Temp media anual | 13.5°C | EPW |
| Temp max media | 20°C | EPW |
| Temp min media | 7°C | EPW |
| Humedad relativa media | 80% | EPW |
| Radiación solar global | 4.5 kWh/m²/día | EPW |
| Precipitación anual | 1010 mm | EPW |
| Viento dominante | NE (5-8 nudos) | EPW |
| Altura solar solsticio verano | 65° (21 jun) | Calculado |
| Altura solar solsticio invierno | 61° (21 dic) | Calculado |
| Altura solar equinoccio | 85° (21 mar/sep) | Calculado |

### Carta solar Bogotá (latitud 4.7°N)

```
Bogotá está muy cerca del ecuador (4.7°N):
- Solsticio de verano (jun): sol pasa casi por el zenit (85° altitud al mediodía)
- Solsticio de invierno (dic): sol sigue alto (61° altitud al mediodía)
- Diferencia verano-invierno: solo 4° (mínima variación estacional)
- El sol sale ~6am y se pone ~6pm todo el año (12h luz constante)

Implicaciones de diseño:
1. Fachada norte: recibe sombra propia del edificio todo el año
2. Fachada sur: recibe sol directo todo el año
3. Fachada oriente: sol directo 6am-12pm (mañana)
4. Fachada occidente: sol directo 12pm-6pm (tarde, más calor acumulado)
5. Aleros horizontales efectivos todo el año (ángulo solar siempre >60°)
6. Quiebrasoles verticales más efectivos en oriente/occidente
```

## Consecuencias

### Positivas
- Pipeline completo que integra normativa + clima + teoría arquitectónica
- Optimización evolutiva con objetivos múltiples (POT + clima + áreas)
- Decisiones de diseño basadas en datos reales de Bogotá
- Propiedades climáticas en BIM nativo (Archicad)
- Cumple con objetivo de Alexander: "edificios vivos" adaptados al lugar

### Negativas
- Mayor complejidad del pipeline (2 scripts nuevos + modificaciones en 5)
- Wallacei con objetivos climáticos requiere más tiempo de cómputo
- Dependencia de archivo EPW (debe actualizarse periódicamente)
- Mayor consumo de VRAM si Rhino.Compute + Ladybug corren en paralelo con Ollama

### Neutrales
- Ladybug ya está instalado como plugin de Grasshopper
- EPW es estándar internacional, fácil de conseguir y mantener
- Los datos mensuales son suficientes para F1-F3 (no requieren cómputo pesado)

## Implementación propuesta

### Fase 1: Cargar datos climáticos (1 día)
1. Crear `scripts/utilities/load-epw-bogota.py`
2. Descargar EPW de Bogotá
3. Generar JSONs estructurados (mensual, vientos, solar, confort)
4. Integrar al caché POT existente

### Fase 2: F1_CONTEXTO_CLIMA (1 día)
1. Crear script que lee JSONs climáticos
2. Genera recomendaciones de orientación
3. Integra con caché POT existente

### Fase 3: Modificar F2 y F3 (2 días)
1. F2: usar radiación solar para sugerir mixtura de usos
2. F3: restringir orientación, dimensionar patios y sombras
3. F3: nuevo script F3_SOMBREADO_v01.py

### Fase 4: Mejorar F4 Ladybug (2 días)
1. Análisis con datos horarios EPW
2. Configurar Wallacei con objetivos climáticos
3. Definir genotipo evolutivo

### Fase 5: F5 BIM con propiedades climáticas (1 día)
1. Agregar User Text climático a elementos Archicad
2. Sincronizar con análisis de F4

## Referencias

- [[adr-001-uso-tapir]] - Tapir para BIM
- [[adr-003-elementos-bim-nativos-vs-morphs]] - Elementos nativos
- [[adr-005-correccion-altura-pot]] - Corrección de datos POT
- EPW Map: https://www.ladybug.tools/epwmap/
- Climate.OneBuilding Colombia: https://climate.onebuilding.org/WMO_Region_3_South_America/COL_Colombia/
- Ladybug Tools: https://www.ladybug.tools/
- Alexander Pattern 163: PATIO INTERIOR
