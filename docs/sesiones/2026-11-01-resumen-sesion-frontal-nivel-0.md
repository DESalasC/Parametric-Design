# Sesión 2026-11-01 — Vista FRONTAL y nivel 0,00 del orquestador web

**Proyecto:** DiseñoParamétrico · **Alcance:** orquestador web (`src/orquestador`), Fase 1 (contexto) y enlace con F3/Stories.
**Estado:** implementado y verificado en local; pendiente la validación en ArchiCAD del L 01.

## 1. Objetivo

Completar la presentación del orquestador web con una vista **FRONTAL desde la calle** que permita decidir el **nivel 0,00 (L 01 en ArchiCAD)** con criterio, no a ciegas sobre la planta:

- predio y volumen de los vecinos inmediatos;
- curvas de nivel en MSNM;
- nivel de la calle;
- cotas de las esquinas del polígono;
- alturas en metros de los predios vecinos;
- perímetro del lote con los mismos colores de la planta;
- planta en miniatura con hasta **5 puntos** que se reflejan en el alzado con su identificador;
- línea vertical de **altura máxima permitida** en cada punto;
- fijación del **0,00** por clic en el alzado o por cota MSNM;
- banda gris de altura permitida medida **sobre el nivel del terreno**, no sobre el 0,00.

## 2. Decisiones de diseño

| Tema | Decisión | Razón |
|---|---|---|
| Lado frontal | `lado_id` de `vecinos-por-lado`; por defecto la calle de acceso de `bloques.json` o el lado clasificado como `via` | El operador ya clasifica la calle FRONTAL en la planta; no se inventa una arista |
| Sentido de la vista | Proyección ortogonal con **espejo automático** para mirar desde la calle | Una fachada se dibuja desde el observador, no desde el lote |
| Ancho de la vista | Rango de todo el predio proyectado (`x_rango`), no solo el frente | El lote es irregular: el resto del polígono también debe verse |
| Curvas de nivel | *Marching squares* sobre grilla IDW del MDT, proyectadas como líneas horizontales con cota MSNM | En una elevación las curvas de nivel son horizontales; dan la lectura topográfica sin falsa 3D |
| Vecinos | `contexto50` filtrado a los que tocan el lote (≤ 4 m) o cruzan la calle (≤ 15 m) | "Inmediatos" evita los 90 edificios del contexto |
| Puntos | Máx. 5, ids P1…P5 estables, color por id, persistidos por CHIP | Identificador único planta ↔ fachada y resistencia a borrados |
| Altura por punto | H global de la norma, editable por punto | La norma puede cambiar por tramo; el valor manual queda marcado con `*` |
| Datum | `POST /api/z0` guarda `z0_m`, `z0_abs_m` y `presentacion.x_frente_m` / `punto_id` | El 0,00 no es solo una cota: también es un punto de la fachada |
| Banda de altura | Base = terreno en el punto del datum; opción "sobre el perfil" | La norma habla de "sobre el nivel del terreno", no del 0,00 |
| Cotas de calle | `mdt=malla` por defecto; botón **Actualizar cotas MDT** lee Catastro y cachea | La malla ETAPA1 no cubre bien la calle (diferencia detectada de ~1,8 m) |

## 3. Actividades realizadas

### 3.1 Backend

- Nuevo `scripts/utilities/F1_FRONTAL_NIVEL_v01.py`:
  - construye el payload `frente / lindero / calle / perfil / esquinas / curvas / silueta / vecinos / lados / altura / datum / banda / puntos / plano`;
  - selecciona el lado frontal y aplica el espejo "desde la calle";
  - calcula curvas de nivel MSNM por *marching squares*;
  - proyecta los puntos de planta a la fachada y calcula su altura permitida;
  - cachea las cotas REST del MDT en `<CHIP>-frontal-mdt.json` (por lado y número de muestras).
- `src/orquestador/servidor.py`:
  - `GET /api/frontal?chip=&lado=&mdt=` (cache en memoria por chip/lado/mdt/firma);
  - `GET|POST /api/frontal/puntos` (máx. 5, ids P1…P5, solo dentro del lote);
  - `GET /frontal?chip=` (página independiente) y estáticos `/frontal.js`, `/frontal.css`;
  - `POST /api/z0` acepta `x_frente_m` y `punto_id` y los guarda en `presentacion`.

### 3.2 Interfaz

- `src/orquestador/frontal.js` (nuevo): planta en miniatura clicable, alzado SVG, puntos P1…P5, banda de altura, datum, curvas, vecinos, esquinas, leyenda y notas; lectura de cotas al pasar el cursor y clic para fijar el 0,00.
- `src/orquestador/frontal.css` (nuevo): estilo de la sección, responsive y página independiente.
- `src/orquestador/index.html`: sección **1d. Frontal (nivel 0,00)** entre 1b–1c y 2; el bloque rompe el ancho del formulario para dar espacio al dibujo; enlace directo `/?chip=AAA...`.

### 3.3 Documentación

- `docs/manual/MANUAL_USUARIO_ORQUESTADOR_WEB.html` **v1.1**: bloque 1d en el mapa, paso nuevo del flujo, filas de controles, sección 6.5 con la figura, archivos canónicos, API y límites actualizados.
- `docs/manual/assets/frontal-nivel-0.png`: captura de la vista con P1–P3.
- `src/orquestador/ARCHIVOS_INTERCAMBIO.md` y `README.md`: archivos y API de la vista.

### 3.4 Pruebas

- `tests/test_frontal_nivel_v01.py` (nuevo): 11 pruebas del payload (lado, perfil, espejo, curvas, esquinas, vecinos, colores, puntos, máximo 5, banda, plano).
- `tests/test_servidor.py`: prueba del payload y la página independiente.
- Verificación de interacción real con CDP (Edge headless): el clic en la planta añade P1, **Reiniciar** lo borra, el clic en el alzado fija el 0,00 y no hay errores JS.

## 4. Resultados verificables (chip AAA0030JKOE)

- Lado frontal detectado: **25 · Occidente-2**, longitud 14,98 m, vía KR 2 E (calle de acceso del modelado).
- Perfil del lindero (MDT Catastro en caché): **2.634,79 a 2.636,47 msnm**; calle **2.634,53 a 2.634,71 msnm**.
- Curvas de nivel: 26 niveles entre 2.636,00 y 2.648,50 msnm.
- Esquinas del polígono: 6 cotas (2.634,79 … 2.649,04 msnm), incluida la mínima del lote.
- Vecinos inmediatos: 10 volúmenes con altura (2 laterales izquierdos, 2 laterales derechos, 6 de fondo); el propio predio se excluye.
- Altura reglamentaria: **H = 10,00 m** (IDPC, Decreto 492/07 PZCB); referencia PZCB 7,00 m.
- 0,00 por defecto: **2.634,79 msnm** (mínimo del lote); terreno en el punto del datum: **2.636,07 msnm** → **Δ 1,29 m**; banda gris 2.636,07 → 2.646,07 msnm.
- Pruebas: `pytest tests/test_frontal_nivel_v01.py tests/test_servidor.py -q` → **33 passed**.
- Captura de referencia: `docs/manual/assets/frontal-nivel-0.png`.

## 5. Procedimiento de uso

1. Abrir `http://127.0.0.1:8900` (o el puerto elegido) y seleccionar el CHIP.
2. En **1d**, confirmar el **lado frontal** en el selector.
3. Hacer clic dentro del lote para marcar P1…P5 (máx. 5). Cada punto aparece en el alzado con su cota y su línea de altura.
4. Si la norma tiene alturas distintas por tramo, editar **H (m)** en la tabla de puntos; el valor manual se marca con `*`.
5. Fijar el **0,00**: clic en el alzado a la cota deseada, o escribir la MSNM y pulsar **Fijar**. **Mín. lote** restaura el criterio por defecto.
6. Revisar la **banda gris** y la nota de Δ. Activar **Banda sobre el perfil** para ver la altura permitida siguiendo el terreno.
7. Si la calle quedó estimada, pulsar **Actualizar cotas MDT** (Catastro, ~20-30 s) y revisar de nuevo.
8. Al cambiar el 0,00, regenerar el plan de stories (`F3_StorySync_v02.py --plan`) y verificar en ArchiCAD que el Ground Floor es 0,000.

## 6. Condiciones, limitaciones y resultados esperados

- **Curvas de nivel**: son una proyección horizontal de las cotas del MDT; no sustituyen un modelo 3D. La lectura correcta es "a esta cota, el terreno ocupa este tramo del frente".
- **MDT**: la malla ETAPA1 solo cubre el lote + ~5 m. La calle se estima; por eso existe **Actualizar cotas MDT** y el caché por lado. Si se cambia de lado frontal, hay que volver a actualizar.
- **Vecinos**: `contexto50` puede traer varias partes del mismo edificio y alturas distintas; se dibujan todas y la más alta manda visualmente. Los vecinos sin altura no se dibujan (se informa el conteo).
- **Puntos**: deben quedar dentro del lote; un clic sobre el borde puede rechazarse (el polígono se evalúa con *ray casting*). Los puntos se persisten por CHIP y se pueden reiniciar en cualquier momento.
- **Datum**: el 0,00 y la base de la banda son conceptos distintos. La banda se mide sobre el terreno; el 0,00 es el Ground Floor del proyecto. La vista muestra ambos y el Δ.
- **ArchiCAD**: la vista no crea stories; solo fija el datum. La creación/verificación sigue siendo manual asistida.

## 7. Archivos tocados

- `scripts/utilities/F1_FRONTAL_NIVEL_v01.py` (nuevo)
- `src/orquestador/servidor.py`
- `src/orquestador/frontal.js` (nuevo)
- `src/orquestador/frontal.css` (nuevo)
- `src/orquestador/index.html`
- `tests/test_frontal_nivel_v01.py` (nuevo)
- `tests/test_servidor.py`
- `docs/manual/MANUAL_USUARIO_ORQUESTADOR_WEB.html` + `assets/frontal-nivel-0.png`
- `src/orquestador/ARCHIVOS_INTERCAMBIO.md`, `src/orquestador/README.md`

## 8. Pendientes

1. Validar el **L 01 en ArchiCAD** con el datum fijado desde la vista (StorySync `--plan` y `--check`).
2. Decidir si la banda debe abrir por defecto en **"sobre el perfil"** o en base horizontal (hoy: horizontal).
3. Revisar con el operador si la **altura por punto** debe derivarse de la norma por tramos (hoy es H global editable).
4. Limpiar la documentación antigua del alzado estático (`/alzado`) o marcarlo como vista heredada.
5. Evaluar un `H` por punto persistido en `norma-override.json` si se repite entre sesiones.

## 9. Referencias

- Manual del orquestador v1.1: `docs/manual/MANUAL_USUARIO_ORQUESTADOR_WEB.html`.
- Payload/modelo: `scripts/utilities/F1_FRONTAL_NIVEL_v01.py`.
- Pruebas: `tests/test_frontal_nivel_v01.py`, `tests/test_servidor.py`.
