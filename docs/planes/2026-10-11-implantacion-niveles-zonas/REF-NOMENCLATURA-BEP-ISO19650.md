# Referencia — Nomenclatura y clasificación BEP (ISO 19650)

- **Origen:** documento aportado por el operador (2026-10-11) como base para la decisión D4
  (clasificación de zonas por categoría y por nombre, con estándares internacionales).
- **Uso:** marco normativo para la nomenclatura de espacios/zonas en F1–F4 del plan
  `PLAN-IMPLANTACION-NIVELES-ZONAS.md` (ver Addendum A §7.3).

---

El BEP debe tratar la nomenclatura como una **regla contractual y verificable**, no como una sugerencia. Estructúrala en una sección dedicada que defina el formato, los catálogos de valores permitidos, los parámetros obligatorios, los ejemplos y el método de control de calidad. ISO 19650-2 exige un BEP del equipo designado y vincula la identificación de información con la estructura de contenedores de información.

## Estructura sugerida del BEP

### 1. Objetivo y alcance

Declara qué se nombra y por qué:

- Archivos, vistas, hojas, familias, tipos, materiales, sistemas, fases y espacios.
- Niveles, zonas, habitaciones/espacios, elementos y atributos.
- Entregables IFC, COBie, planos y documentación del CDE.

Indica que la convención aplica a **todos los participantes** y prevalece sobre convenciones internas de cada firma, salvo excepciones aprobadas por el Gestor de Información.

### 2. Normas aplicables

Enumera la jerarquía normativa:

- ISO 19650 y anexo nacional aplicable.
- Requisitos del cliente: EIR, AIR, PIR y protocolo de información.
- Sistema de clasificación elegido: Uniclass, OmniClass, CoClass u otro.
- COBie, si se requiere entrega para operación.
- Estándares internos del proyecto, como plantillas Revit, IFC y CDE.

El BEP debe indicar qué norma prevalece cuando haya conflicto.

### 3. Estructura de identificación

Define una fórmula única por tipo de objeto. Por ejemplo:

```text
[PROYECTO]-[AUTOR]-[VOLUMEN]-[NIVEL]-[TIPO]-[ROL]-[NUMERO]
```

Para espacios:

```text
[NIVEL]-[ZONA]-[CATEGORIA]-[NOMBRE]-[CONSECUTIVO]
```

Ejemplo:

```text
L02-ZA-SAL-SALA-REUNION-001
```

Establece explícitamente:

- Separador: guion para campos, sin espacios dentro de códigos.
- Mayúsculas/minúsculas.
- Longitud máxima.
- Caracteres permitidos: idealmente A-Z, 0-9 y guion.
- Idioma de los nombres.
- Prohibición de acentos, tildes, espacios, `#`, `/`, `\` y caracteres especiales.

COBie, por ejemplo, requiere nombres únicos y establece reglas de formato para nombres; además organiza los espacios como descomposición horizontal de los niveles.

### 4. Catálogo de niveles

Incluye una tabla obligatoria de niveles. No dejes que cada disciplina invente códigos.

| Código | Nombre del nivel | Elevación base | Uso |
|---|---|---:|---|
| `SIT` | Site | 0.00 | Terreno y urbanización |
| `B01` | Sótano 1 | -4.50 | Estacionamiento |
| `GF` | Planta baja | 0.00 | Acceso y recepción |
| `L01` | Nivel 1 | 4.20 | Oficinas |
| `L02` | Nivel 2 | 8.40 | Oficinas |
| `RF` | Cubierta | 24.00 | Cuartos técnicos |

Define también códigos para casos especiales: `ZZ` varios niveles, `XX` no aplica, `M01` mezzanine, etc.

### 5. Catálogo de zonas

Define zonas físicas o funcionales:

| Código | Zona |
|---|---|
| `ZA` | Ala A |
| `ZB` | Ala B |
| `ZN` | Núcleo |
| `ZP` | Público |
| `ZS` | Servicios |
| `ZT` | Técnica |

Si el proyecto es pequeño, puedes omitir zona; pero decláralo formalmente para evitar interpretaciones distintas.

### 6. Catálogo de categorías de espacio

Crea un diccionario cerrado de categorías y abreviaturas:

| Código | Categoría | Ejemplos |
|---|---|---|
| `ACC` | Acceso | Vestíbulo, recepción |
| `CIR` | Circulación | Pasillo, escalera, ascensor |
| `OFI` | Oficina | Oficina, sala de reuniones |
| `SAL` | Sala | Sala de usos múltiples, auditorio |
| `SER` | Servicio | Baño, depósito, limpieza |
| `TEC` | Técnico | Cuarto eléctrico, cuarto de datos |
| `EXT` | Exterior | Terraza, balcón |

Cada categoría debe corresponderse, cuando aplique, con un código de clasificación externo como Uniclass `SL_`. Uniclass tiene una tabla específica de *Spaces/locations* para clasificar espacios donde se realizan actividades.

### 7. Parámetros obligatorios del espacio

Especifica los campos que deben completarse en el modelo, no solo en el nombre:

| Parámetro | Obligatorio | Formato | Ejemplo |
|---|---|---|---|
| `Space_Number` | Sí | Código único | `L02-ZA-SAL-001` |
| `Space_Name` | Sí | Texto legible | `Sala de reuniones 1` |
| `Level` | Sí | Del catálogo | `L02` |
| `Zone` | Sí/No según proyecto | Del catálogo | `ZA` |
| `Space_Category` | Sí | Del catálogo | `SAL` |
| `Classification_Code` | Sí | Uniclass/COBie | Código aplicable |
| `Department` | Según AIR | Texto o código | `Finanzas` |
| `Occupancy_Type` | Según AIR | Catálogo | `Reunión` |
| `COBie_External_ID` | Si hay COBie | GUID o ID | UUID |

COBie requiere una fila por espacio funcional y que los valores de identificación sean únicos; por eso conviene separar el identificador técnico del nombre descriptivo.

### 8. Reglas de numeración

Define sin ambigüedad:

- El consecutivo se reinicia por `nivel + zona + categoría`, por ejemplo `L02-ZA-SAL-001`.
- No se reutilizan números eliminados.
- Los espacios nuevos usan el siguiente número disponible.
- Si un espacio se divide, los nuevos reciben números nuevos; no se reutilizan parcialmente.
- Si un espacio cambia de uso, mantiene su número si su función y ubicación no cambian; si cambia de categoría, se evalúa si requiere recodificación.

### 9. Ejemplos aprobados y no aprobados

Incluye ejemplos visuales; reducen errores más que las reglas abstractas.

| Estado | Nombre | Motivo |
|---|---|---|
| Aprobado | `L02-ZA-SAL-001` | Cumple estructura y catálogo |
| Aprobado | `L01-ZP-ACC-003` | Nivel, zona y categoría válidos |
| Rechazado | `Sala reuniones final 2` | Sin código, con espacios y ambiguo |
| Rechazado | `L2_A_SALA_01` | Separadores y formato no autorizados |
| Rechazado | `L02-ZA-SAL-001 v2` | No debe incorporarse versión en el nombre del espacio |

### 10. Control de calidad

Define quién valida y en qué momento:

- **Gestor BIM / Gestor de Información:** aprueba catálogos y excepciones.
- **Coordinador BIM por disciplina:** verifica cumplimiento antes de cada entrega.
- **Responsable arquitectónico:** crea y mantiene espacios.
- **Validación automática:** comprobación de duplicados, campos vacíos, códigos inválidos y formato.
- **Validación manual:** revisión funcional de nombres y clasificación antes de emisión.

Puedes usar un *model auditing checklist* con reglas como: "0 espacios sin `Space_Number`", "0 duplicados", "0 categorías fuera del catálogo" y "100% de espacios con nivel válido".

### 11. Gestión de cambios

Establece un procedimiento para añadir códigos nuevos:

1. El equipo solicita el código mediante formulario o issue en el CDE.
2. El Gestor de Información valida que no exista equivalente.
3. Se actualiza el catálogo del BEP y la plantilla.
4. Se notifica a todos los equipos.
5. Se registra la versión del BEP.

No permitas que cada disciplina cree abreviaturas nuevas de forma local.

## Plantilla breve para insertar en el BEP

```text
7. NOMENCLATURA Y CLASIFICACIÓN

7.1 Alcance
Esta convención aplica a espacios, niveles, zonas, archivos, vistas,
hojas, familias, tipos, sistemas y entregables del proyecto.

7.2 Formato de espacios
[NIVEL]-[ZONA]-[CATEGORIA]-[CONSECUTIVO]
Ejemplo: L02-ZA-SAL-001

7.3 Reglas
- Identificadores únicos en todo el proyecto.
- Solo mayúsculas, números y guiones.
- Sin espacios, acentos ni caracteres especiales.
- Niveles, zonas y categorías provenientes exclusivamente de los catálogos 7.4 a 7.6.
- El nombre descriptivo se registra en el parámetro Space_Name.
- El código no incorpora versiones ni estados.

7.4 Catálogo de niveles
SIT, B01, GF, L01, L02, RF, ZZ, XX.

7.5 Catálogo de zonas
ZA, ZB, ZN, ZP, ZS, ZT.

7.6 Catálogo de categorías
ACC, CIR, OFI, SAL, SER, TEC, EXT.

7.7 Clasificación
Todos los espacios deberán tener clasificación Uniclass/COBie
según la tabla de espacios aplicable.

7.8 Control
El Coordinador BIM validará duplicados, campos vacíos y códigos
fuera de catálogo antes de cada entrega.
```

## Principio clave

Separa siempre tres cosas:

1. **Identificador técnico:** `L02-ZA-SAL-001`.
2. **Nombre descriptivo:** `Sala de reuniones 1`.
3. **Clasificación normalizada:** código Uniclass/COBie.

Así el modelo permanece ordenado, es exportable a IFC/COBie y no depende de que las personas interpreten libremente los nombres. La estructura BEP debe recoger explícitamente nomenclatura, clasificación, procesos de control y entorno común de datos.
