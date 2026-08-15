# F3 — Distribución espacial del USO-MULTIPLE (Fase 3, primera parte)

Motor que convierte el programa del escenario **D_MIXTO** (override de uso múltiple) de cada
caso F2 en una **distribución espacial** verificable: matriz de adyacencias, layout con
núcleos de servicios y transporte vertical, planos esquemáticos y masa 3D.

## Qué genera (`F3_DISTRIBUCION_v01.py <CASO_ID>`)

| Salida | Contenido |
|---|---|
| `programa.json` | Usos del D_MIXTO con % GFA, área, unidades y unidad tipo |
| `matriz_adyacencias.json` | Matriz de relaciones entre usos (3 Requerida / 2 Deseable / 1 Indiferente / 0 Incompatible) con justificación funcional y normativa (NSR-10 Título C y K, habilitación IPS, accesibilidad) |
| `layout_espacial.json` | Huella (ocupación POT × lote), niveles, reparto vertical de usos, núcleos (escaleras según altura — presurizada > 6 pisos NSR-10 K.3.6 —, ascensores según población ~1/40 unid, ductos/basuras/cuarto técnico), población estimada |
| `planos_<id>.html` | Planos esquemáticos SVG por nivel (losa, núcleo, unidades por uso coloreadas) |
| `F3_<id>.3dm` | Masa 3D: cajas por nivel (capas N1..Nn) + volumen del núcleo (capa NUCLEO), con rhino3dm (sin abrir Rhino) |

## Casos

| ID | Caso | Escenario F2 | Resultado |
|---|---|---|---|
| A | El Prado (Suba) | D_MIXTO (local 20% + vivienda 80%) | 5 niveles, huella 220 m², 1 ascensor, núcleo ~40 m²/piso |
| B | La Candelaria | D_MIXTO (local turístico 30% + vivienda 70%) | 6 niveles, huella 652 m², 2 ascensores, núcleo ~45 m²/piso |
| B_SALUD | La Candelaria (variante) | D_MIXTO_SALUD (consultorios 25% + vivienda 75%) | 6 niveles; consultorios en N1-2, vivienda N3-6 |
| C | Muzú (Puente Aranda) | D_MIXTO (local 35% + vivienda VIS 65%) | 5 niveles, huella 250 m², 1 ascensor, núcleo ~40 m²/piso |

## Reglas incorporadas (primera instancia)

- **Ocupación**: huella = 70% del área del lote (tratamiento Consolidación); niveles = GFA/huella.
- **Verticalidad**: usos públicos y de salud en los primeros niveles (evacuación y accesos
  independientes); vivienda arriba.
- **Adyacencias clave**: salud ↔ salud requerida (cluster); vivienda ↔ institucional/geriátrico
  incompatible en el mismo piso; local ↔ institucional requerida (farmacia/insumos).
- **Núcleo**: 2 módulos de escalera (13,5 m²) + ascensores (1 por ~40 unidades) + 8 m² de
  ductos/basuras/cuarto técnico por piso.

## Siguientes pasos (F3 completo)

- Volumetría detallada por uso en Grasshopper (VOLUM_GENERADOR) consumiendo `layout_espacial.json`.
- F4 ambiental (Ladybug) y F5 inyección BIM (ArchiCAD live connection, puerto 19723).
