# Condiciones de diseño — Emplazamiento del núcleo (F3)

Documento de condiciones que rige la posición/orientación del núcleo
(escaleras + ascensor + servicios) dentro de la masa por piso. Combina los
patrones de C. Alexander, las reglas de iluminación natural y la decisión del
operador. Se incorpora como regla suave en `F3_VOLUM_GENERADOR_v07` (no sustituye
la normativa NSR-10 ni el POT).

## 1. Patrones de C. Alexander aplicables

Fuente: skill `alexander-patterns` del proyecto (vault `30-referencia\christopher-alexander\`).

| Patrón | Nombre | Aplicación al núcleo |
|---|---|---|
| 159 | Light on Two Sides of Every Room | Todo espacio habitable debe recibir luz por ≥2 lados; el núcleo (servicio) no debe ocupar los frentes de luz. |
| 107 | Wings of Light | La masa se despliega en alas estrechas para maximizar perímetro iluminado; el núcleo se retira del frente iluminable. |
| 133 | Staircase as a Stage | La escalera (parte del núcleo) es espacio de circulación y puede ocupar la posición menos favorable a la luz. |
| 163 | Courtyards that Breathe (Patio Interior) | La ventilación/luz se garantiza dejando libres las fachadas exteriores y vacíos que "respiren". |
| 236 | Window Place (Ventanas Altas) | La luz profunda se logra sin ganancia solar; el núcleo no debe taponar la penetración de luz. |
| 98 | Circulation Realms | El núcleo vertical organiza la circulación y conecta el acceso; se apoya contra la medianera. |
| 110 | Main Entrance | El acceso y el núcleo se resuelven juntos, sin sacrificar fachada de vivienda/local. |

## 2. Reglas de iluminación natural

Fuente: skill `daylighting-design` del proyecto.

- **Zonas de servicio como tampón**: escaleras, ascensores, ductos y baños se
  colocan en la fachada menos favorable (medianera u orientación E/O), liberando
  las fachadas N/S para espacios habitables ("place service spaces ... as buffer
  zones").
- **Objetivos DF (vivienda)**: sala ≥ 2,0 %, alcoba ≥ 1,5 %; profundidad iluminada
  útil = 2,0–2,5 × altura de dintel.
- **Bogotá (clima tropical de altura)**: la crítica es el asoleamiento E/O; el
  núcleo contra la medianera evita fachadas ciegas hacia el frente y maximiza el
  perímetro con luz útil.

## 3. Regla de emplazamiento (decisión del operador, 2026-08-17)

> El núcleo se emplaza con su **lado corto paralelo al lado largo posterior o
> lateral del lote** (la medianera de mayor longitud), **evitando el lado
> frontal y la zona verde / espacio público** del predio.

Consecuencias operativas (caso A: bloque de núcleo 5,4 × 9,0 m):

1. Ocupa la **mínima longitud de fachada ciega** (5,4 m, su lado corto) sobre
   la medianera.
2. Su dimensión larga (9,0 m) **penetra hacia el interior**, sin taponar frentes de luz.
3. Las fachadas exteriores (frente, laterales iluminables y el espacio público)
   quedan **libres para vivienda/local → máxima luz**, consistente con los
   patrones 159 y 107.

## 4. Condiciones de validación (regla "nunca geometría intersectante")

- El bloque debe caber íntegro contra el borde requerido: intersección ≥ 95 % del
  área del bloque dentro del piso.
- Si no cabe en ese lado, se intenta **barrido a lo largo de ese mismo borde**
  (no alrededor del centroide) antes de omitir el piso.
- Si ningún desplazamiento cabe, el piso se omite y el mensaje reporta el motivo
  numérico (áreas), igual que en v07.5+.

## 5. Implementación en `F3_VOLUM_GENERADOR_v07` (v07.14)

**Implementado** en v07.14:

1. Entradas opcionales `sides_table_json` (JSON de `F1_ETAPA2_LADOS_v06`, con la
   clasificación por lado: Frontal / EspacioPublico / Lateral / Posterior) y
   `lote_vertices` (vértices del predio).
2. `_medianeira_eje()` elige el **lado medianero (Lateral/Posterior) más largo**,
   descartando Frontal y EspacioPúblico, y devuelve su eje dominante (X/Y) y
   signo (sur/norte u oeste/este).
3. El bloque se apoya contra ese borde con el **lado corto paralelo** y barre a lo
   largo del borde (paso 0,75 m); si no cabe (≥95 %), **fallback** al barrido
   3×3 centrado (comportamiento v07.5).
4. `_caja_orientada()` y `_caja_solido()` reorientan el bloque y los sólidos de
   circulación/servicios según el eje detectado.

Limitación conocida: alineación por **eje dominante** (X/Y) para lotes
ortogonales; la rotación exacta para lotes diagonales queda como mejora futura.

## 6. Trazabilidad

Cada regla se referencia con su número de patrón (Alexander), su fuente
(daylighting-design) o la decisión del operador (fecha), para trazabilidad en la
memoria de diseño.
