# F3 — Distribución espacial del USO-MULTIPLE (Fase 3, primera parte)

Motor que convierte el programa del escenario **D_MIXTO** (override de uso múltiple) de cada
caso F2 en una **distribución espacial** verificable: matriz de adyacencias, layout con
núcleos de servicios y transporte vertical, planos esquemáticos y masa 3D.

## Generador v07 (2026-08-16, v07.24 2026-08-17): nucleo EXCLUIDO + circulacion/servicios separados + volumetria por uso

`F3_VOLUM_GENERADOR_v07.py` (IronPython 2.7, componente "Script" clásico) reemplaza al v06
con las correcciones del operador. **Sub-versiones internas** (la versión general solo cambia
con cambios mayores de contrato o algoritmo; el mensaje del componente reporta la subversión
en curso, p. ej. "VOLUM v07.5 |"):

- **v07.1** — hueco = BLOQUE COMPLETO del núcleo (48,6 m²), no la suma de sólidos (39,8 m²):
  el aire interior del bloque (8,8 m²) rompía la validación en todos los pisos.
- **v07.2** — núcleo centrado en el centroide de CADA piso (el bloque fijo al piso 1
  sobresalía en los pisos escalonados).
- **v07.3** — recorte por INTERSECCIÓN primero (la diferencia directa perfil − caja fallaba
  en Rhino al rozar el borde: None/multipieza).
- **v07.4** — diferencia multipieza → tomar la MAYOR pieza validada; respaldo 3D resta la
  pieza intersección, no la caja completa.
- **v07.5** — núcleo BUSCA SU POSICIÓN (barrido 3×3, paso 0,75 m alrededor del centroide de
  cada piso): el centroide de una L cóncava puede caer en el codo y partir la intersección;
  el barrido ubica el bloque donde cabe completo (≥95%). Diagnóstico numérico (áreas) en el
  detalle de omitidos.

1. **Perímetro = envelope_por_piso de F1_ETAPA2_NORMATIVA_v07** (lista de curvas
   POR PISO: ocupación escalonada por empates laterales + voladizos frontales
   en pisos 2+; fallback a `envelope_curve` para compat v06): la masa coincide
   con la envolvente normativa piso a piso, no con el lote completo.
2. **Exclusión booleana real del núcleo**: diferencia de curvas secuencial (caja por caja,
   overload estable curva-curva) con verificación de área (tol 2%); respaldo boolean 3D con
   verificación de volumen (tol 3%). **Regla: nunca se entrega geometría intersectante** — si
   la exclusión falla, el piso se omite y el mensaje reporta `huecos excluidos n/N`.
3. **Circulación vertical SEPARADA de servicios/áreas técnicas**: salidas
   `volumenes_circulacion` (escaleras + ascensores) y `volumenes_servicios` (ductos/basuras/
   cuarto técnico), con la disposición real de `nucleo.disposicion` del programa-areas.json
   (bloque 5,4×9,0 m para el caso A; 2 escaleras 2,7×5,0 + ascensor 2,2×2,2 + servicios 2,0×4,0).
4. **Destino = ArchiCAD (Live Connection)**: las salidas se cablean a los componentes AC_*
   que crean **Morphs nativos de ArchiCAD** (no se hornea en Rhino). Los elementos viajan a
   ArchiCAD y pueden volver modificados por decisiones del operador (GetElements) o por
   sugerencias de Ladybug (F4) y Wallacei (optimización) dentro de Grasshopper.

### Cableado en el canvas (sesión abierta de Rhino)

| Entrada del GHPython | Conectar desde |
|---|---|
| `envelope_por_piso` (PREFERIDA) | Salida `envelope_por_piso` (lista) de `F1_ETAPA2_NORMATIVA_v07` |
| `envelope_curve` (fallback) | Salida `envelope_curve` de `F1_ETAPA2_NORMATIVA_v07` |
| `json_path` | Ruta a `src/fase-3-masa/casos/A/programa-areas.json` (absoluta o relativa al proyecto; el script la resuelve y busca el archivo) |
| `floor_height` | 3,0 (default; se prefiere `altura_z` del JSON) |

| Salida | Destino (Live Connection AC_*) |
|---|---|
| `volumenes_principales_mesh` | Componente AC de creación de **Morph** (el Morph de ArchiCAD requiere `Rhino.Geometry.Mesh`, no Brep) |
| `volumenes_circulacion_mesh` | Morph (escaleras + ascensores) |
| `volumenes_servicios_mesh` | Morph (ductos/basuras/cuarto técnico) |
| `volumenes_nucleo_mesh` | Morph (compat: circulación + servicios) |
| `losas_mesh` | Morph (superficie abierta de la losa con hueco) |
| `volumenes_*` / `losas` (Brep) | Preview en Rhino / F4 (Ladybug) / otros consumidores |
| `etiquetas` / `mensaje` | Paneles / texto del canvas |

## Prueba real en Rhino 8 (2026-08-14, caso A)

`F3_PRUEBA_MASA_A_rhino.py` ejecuta el cuerpo del `F3_VOLUM_GENERADOR_v06` DENTRO de Rhino 8.33
(API completa, no rhino3dm) con la huella real del lote (contexto F1) y el `programa-areas.json`
del caso A. Resultado: **5 losas, 5 volúmenes principales, 5 volúmenes de núcleo, etiquetas
correctas y .3dm guardado (15 objetos)** — valida el contrato GH y el balance del programa.

Hallazgos de la prueba (ya corregidos en v06):
- `rg.Extrude.Create` no existe en Rhino 8.33 → `Extrusion.Create(...).ToBrep()`.
- `rg.Rectangle` no se expone al namespace Python → contorno del núcleo con `PolylineCurve`.
- `doc.Layers.Add(nombre, tupla)` espera objeto Layer en Rhino 8 (solo nombre).

Pendiente documentado: la **resta booleana del núcleo** (2D y 3D) cayó al fallback en esta
huella de catastro (volumen = envelope completo + núcleo; el v06 reporta `huecos aplicados n/N`
para detectarlo en GH). Con el envelope cerrado de F1 el boolean 2D suele funcionar; si no, la
masa con núcleo superpuesto es geométricamente válida para la prueba de distribución.

## Integración con el flujo GH existente (2026-08-14)

El motor **emite `programa-areas.json` balanceado** (esquema compatible con
`F3_VOLUM_GENERADOR_v04/v05`) en cada carpeta de caso. Diagnóstico de las piezas preexistentes:

| Archivo | Estado | Diagnóstico |
|---|---|---|
| `F3_PROGRAMA_AREAS_v01.py` | ⚠️ bug de balance | Con GFA 1.053 m² generaba solo **382,6 m²** construidos (déficit 670 m²): la vivienda se dividía entre (pisos−2) sin re-multiplicar, el piso 1 solo cubría el 30% de la losa y el núcleo se contaba mal. Mix limitado a Comercio/Salud/Vivienda sin integrar F2 |
| `F3_VOLUM_GENERADOR_v04.py` | ✅ base sólida, 4 mejoras | Núcleo heurístico 10% (sin NSR-10); Z fijas 3,0 m; `open()` sin encoding; `CreatePlanarBreps` tomaba solo el primer brep (patio perdido) |
| `F3_VOLUM_GENERADOR_v05.py` (nuevo) | ✅ | Mismo contrato GH (envelope_curve, json_path, floor_height → losas, volumenes_principales, volumenes_nucleo, etiquetas, mensaje) con: núcleo real del JSON (lado por componentes NSR-10), `altura_piso` por nivel (primer piso 3,6 m), lectura UTF-8 y unión de losas con patio |
| `F3_ACCESOS_INTEGRADOR_v01.py` | ⚠️ referencia rota | Consume `OPTIMIZADOR_ADYACENCIA_v01.py`, que no existe en la carpeta |
| `F3_PREP_LADYBUG_v01.py` | ✅ | Consume salidas de VOLUMEN_v03 → F4 |

El `programa-areas.json` de F3_DISTRIBUCION incluye: `programa_pisos` (piso, `altura_z` real,
`altura_piso`, usos con `area_bruta`/`area_neta` balanceadas — suma = GFA exacto — y `Nucleo`),
`matriz_adyacencia` proyectada a la escala −1/0/1 del v04, y `nucleo` con la dimensión real.

## Qué genera (`F3_DISTRIBUCION_v01.py <CASO_ID>`)

| Salida | Contenido |
|---|---|
| `programa.json` | Usos del D_MIXTO con % GFA, área, unidades y unidad tipo |
| `matriz_adyacencias.json` | Matriz 0-3 (Requerida/Deseable/Indiferente/Incompatible) con justificación funcional y normativa |
| `layout_espacial.json` | Huella, niveles, reparto vertical, núcleos (escaleras/ascensores NSR-10), población |
| `programa-areas.json` | **Esquema GH v04/v05 balanceado** (losas + volúmenes por piso) |
| `planos_<id>.html` | Planos esquemáticos SVG por nivel |
| `F3_<id>.3dm` | Masa 3D (capas N1..Nn + NUCLEO), rhino3dm |

## Casos

| ID | Caso | Escenario F2 | Resultado |
|---|---|---|---|
| A | El Prado (Suba) | D_MIXTO (local 20% + vivienda 80%) | **6 niveles, huella 243,5 m² (real F1 v06), GFA 1.461,1 m² balanceado, núcleo descompuesto: circulación 31,8 m² (2 esc + 1 asc) + servicios 8,0 m², hueco real 48,6 m²/piso (5,4×9,0), disposición para v07** (regenerado 2026-08-16; D_MIXTO ROI 25,6% con CL $800 M) |
| B | La Candelaria | D_MIXTO (local turístico 30% + vivienda 70%) | 5 niveles, huella 662,5 m², 2 ascensores, núcleo ~45 m²/piso (corrida actualizada 2026-09-28; lote 946,45 m²) |
| B_SALUD | La Candelaria (variante) | D_MIXTO_SALUD (consultorios 25% + vivienda 75%) | 5 niveles; consultorios en N1-2, vivienda en niveles superiores (corrida actualizada 2026-09-28) |
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

- ✅ Volumetría por uso en Grasshopper (v07.24: `volumenes_por_uso` + `usos_etiquetas`).
- ✅ Accesos por uso + segregación de flujos (`F3_ACCESOS_INTEGRADOR_v02`).
- F4 ambiental (Ladybug) y F5 inyección BIM (ArchiCAD live connection, puerto 19723).
