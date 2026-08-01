# Architect Skills - Referencia

**Plugin:** Architect Skills v1.0.0
**Autor:** Abhinav Bhardwaj
**Licencia:** MIT
**Instalado:** $(Get-Date -Format 'yyyy-MM-dd')

## Ubicación

- **Skills:** `.claude/skills/` (18 carpetas)
- **Calculadoras:** `scripts/architect-calculators/` (7 scripts Python)
- **Origen:** `C:\Users\Dario Salas\proyectos\Skills-Architects-main`

## Skills por categoría

### 1. Foundation (Auto-activada)
- `architect-foundations` - base con 50+ arquitectos/teóricos, 50+ métricas

### 2. Design & Theory
- `design-theory` - 8 filosofías, RIBA/AIA, precedentes
- `concept-design` - 12 partis, massing, organización

### 3. Program & Typology
- `building-programming` - Peña method, area standards, adjacency
- `building-typology` - residencial, oficina, hospital, educación

### 4. Spatial & Envelope
- `spatial-planning` - 10 plan types, circulación, núcleos
- `building-envelope` - 10 wall systems, glazing, roofs

### 5. Structure & Services
- `structural-systems` - 8 sistemas, grids, luces
- `building-services` - 9 HVAC types, plomería, eléctrico

### 6. Environment & Materials
- `daylighting-design` - DF, sDA, ASE, UDI, glare
- `material-selection` - 7 categorías, LCA, embodied carbon

### 7. Codes & Compliance
- `building-codes` - IBC, ocupaciones, egress
- `accessibility-design` - ADA, universal design
- `fire-life-safety` - compartimentación, sprinklers
- `acoustic-design` - STC/Rw, room acoustics

### 8. Sustainability & Production
- `building-sustainability` - LEED, Passive House, WELL
- `construction-documentation` - drawings, specs, BIM LOD
- `architect-calculator` - 7 calculadoras Python

## Calculadoras Python

| Calculadora | Función | Ejemplo |
|-------------|---------|---------|
| `area_calculator.py` | GFA, NGA, unidades, parking | `--site-area 5000 --far 3.0 --ntg-ratio 0.80` |
| `uvalue_calculator.py` | U-value multicapa | `--layers '[{...}]'` |
| `daylight_calculator.py` | Daylight factor | geometría + ventana |
| `egress_calculator.py` | Egress compliance | `--floor-area 2000 --occupancy-type B` |
| `structural_load_calculator.py` | Cargas gravitacionales | tributary area |
| `energy_calculator.py` | Demanda heating/cooling | degree-day method |
| `cost_calculator.py` | Costo construcción | por tipo y región |

## Cómo usar con Claude Code

Las skills se activan automáticamente. Ejemplos de prompts:

### Para Fase 2 (Demanda)
```
> Usando architect-calculator, calcula el área neta construible para un lote de 2000 m² con FAR 3.0
> Crea un adjacency matrix para un edificio residencial de 50 unidades
> ¿Qué NTG ratio debo apuntar para un edificio de oficinas?
```

### Para Fase 3 (Masa)
```
> Diseña el núcleo para una torre residencial de 30 pisos
> Selecciona un sistema estructural para un edificio de 12 pisos en timber
> Compara chilled beams vs VAV para una oficina de 20000 m²
```

### Para Fase 4 (Ambiental)
```
> Estima el daylight factor para una oficina de 6m de profundidad
> Diseña una estrategia de sombreado para fachada oeste a latitud 4.7°N (Bogotá)
> Compara embodied carbon de CLT vs RC frame para 6 pisos
```

### Para Fase 5 (BIM)
```
> Genera un door schedule para un edificio de 20 unidades
> ¿Qué LOD necesito para elementos estructurales en BIM?
> Especifica un muro con U-value 0.15 W/m²K para Passive House
```

## Integración con pipeline DiseñoParametrico

### Flujo de trabajo sugerido

```
1. [F1_CONTEXTO_POT] obtiene datos del lote (POT + catastro)
   ↓
2. [architect-calculator: area_calculator.py] calcula GFA, NGA
   ↓
3. [F2_DEMANDA_MOTOR] distribuye usos (incentivos 670)
   ↓
4. [building-programming skill] genera adjacency matrix
   ↓
5. [F3_VOLUM_GENERADOR] genera masa
   ↓
6. [spatial-planning skill] diseña núcleo y circulación
   ↓
7. [F4_LADYBUG_ANALISIS] análisis ambiental
   ↓
8. [daylighting-design skill] optimiza daylight
   ↓
9. [F5_MAPEO_TAPIR] inyección BIM
   ↓
10. [construction-documentation skill] genera schedules y specs
```

### Bogotá-specific considerations

- **Latitud:** 4.7°N (tropical, sin estaciones marcadas)
- **Altitud:** 2640 msnm (menor densidad aire, mayor radiación solar)
- **Clima:** Clima templado sin calefacción ni refrigeración mecánica significativa
- **Sísmico:** Zona Intermedia (Aa=0.15, Av=0.20 según NSR-10)
- **Normativa local:** POT Decreto 555/2021 + NSR-10 (no IBC, no ASHRAE)
