

## Architect Skills Plugin

El proyecto incluye el plugin **Architect Skills** (18 skills + 7 calculadoras Python).

### Ubicación
- Skills: `.claude/skills/`
- Calculadoras: `scripts/architect-calculators/`

### Skills disponibles
- **architect-foundations** (auto-activada) - base con 50+ arquitectos/teóricos
- **design-theory** - filosofías de diseño, RIBA/AIA, precedentes
- **concept-design** - partis, massing, organización espacial
- **building-programming** - programa de espacios, adjacency matrix
- **building-typology** - tipologías (residencial, oficina, hospital, etc.)
- **spatial-planning** - circulación, núcleos, stacking, NTG
- **building-envelope** - muros, vidrios, cubiertas, puentes térmicos
- **structural-systems** - 8 sistemas estructurales, grids, luces
- **building-services** - HVAC, plomería, eléctrico, ascensores
- **daylighting-design** - iluminación natural, solar geometry
- **material-selection** - materiales, LCA, embodied carbon
- **building-codes** - IBC, ocupaciones, egress
- **accessibility-design** - ADA, universal design
- **fire-life-safety** - compartimentación, egress, sprinklers
- **acoustic-design** - STC/Rw, room acoustics, control ruido
- **building-sustainability** - LEED, Passive House, WELL, net zero
- **construction-documentation** - drawings, specs, BIM LOD, CA
- **architect-calculator** - 7 calculadoras Python

### Calculadoras Python
```powershell
# Área y FAR
python scripts/architect-calculators/area_calculator.py --site-area 5000 --far 3.0 --ntg-ratio 0.80

# U-value de muro multicapa
python scripts/architect-calculators/uvalue_calculator.py --layers '[...]'

# Egress compliance
python scripts/architect-calculators/egress_calculator.py --floor-area 2000 --occupancy-type B --sprinklered --num-stories 6
```

### Cómo usar
Las skills se activan automáticamente cuando haces preguntas de arquitectura.
No requieren slash commands. Ejemplos:
- "Calcula el área neta construible para un lote de 2000 m² con FAR 3.0"
- "Diseña el núcleo para una torre residencial de 30 pisos"
- "Especifica un muro con U-value 0.15 W/m²K para Passive House"

## Marco Teórico - Christopher Alexander

El proyecto se basa en el marco teórico de Christopher Alexander:
- **El Modo Intemporal de Construir** - cualidad sin nombre, centros vivos
- **El Lenguaje de Patrones** - 253 patrones desde ciudad hasta detalle
- **La Naturaleza del Orden** - 15 propiedades fundamentales

Documentación en vault: `30-referencia\christopher-alexander\`

Aplicar patrones en:
- Fase 2: patrones de actividad y mixtura
- Fase 3: patrones espaciales (PATIO INTERIOR, ACTIVITY POCKETS)
- Fase 4: iluminación natural (WINDOW PLACE, TALL WINDOWS)

## Subproyectos de investigación

### GhDefinitionExplorer
- Ubicación: `src\research\gh-definition-explorer\`
- Función: explorar archivos .gh/.ghx usando GH_IO.dll
- Reglas: ver `src\research\gh-definition-explorer\CLAUDE.md`
- Documentación GH_IO en vault: `30-referencia\gh-io-docs\`

### GhIoIndexGenerator
- Ubicación: `src\research\gh-io-index-generator\`
- Función: generar índice Markdown de tipos en GH_IO.dll usando Reflection
- Uso: `dotnet run` desde la carpeta

## Tapir - Conexión BIM

- Librería: `D:\WORK\LIBRARIES\bim\tapir-archicad\`
- Documentación: vault `30-referencia\tapir-api\`
- Para Fase 5: usar AC_Slab, AC_Wall, AC_Zone + Set_UserText

## Ruflo - Orquestación

- Ubicación: `D:\WORK\AI\ruflo\`
- Función: coordinación de workflows y memoria del sistema
- Repo: github.com/ruvnet/ruflo
