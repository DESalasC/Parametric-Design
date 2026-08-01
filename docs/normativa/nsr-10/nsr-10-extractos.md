---
fecha: 2026-08-01
tipo: referencia
fase: transversal
estado: activo
tags: [nsr-10, sismo-resistente, bogota, normativa, separacion-sismica]
---

# NSR-10 - Extractos Relevantes para Pipeline Paramétrico

**Fuente:** Reglamento Colombiano de Construcción Sismo Resistente NSR-10
**Fecha de expedición:** 26 de marzo de 2010 (Diario Oficial 47.663)
**Entidad:** Ministerio de Ambiente, Vivienda y Desarrollo Territorial

## Estructura del NSR-10

El reglamento está organizado en 11 títulos:

| Título | Tema | Relevancia para pipeline |
|--------|------|---------------------------|
| **A** | Requisitos generales de diseño y construcción sismo resistente | ⭐⭐⭐ CRÍTICO |
| B | Cargas | ⭐⭐ |
| C | Concreto estructural | ⭐ |
| D | Mampostería estructural | ⭐ |
| E | Casas de uno y dos pisos | ⭐⭐ |
| F | Estructuras metálicas | ⭐ |
| G | Estructuras de madera y guadua | ⭐ |
| H | Estudios geotécnicos | ⭐⭐ |
| I | Supervisión técnica | ⭐ |
| J | Requisitos de protección contra incendios | ⭐⭐ |
| K | Requisitos complementarios | ⭐ |

## Bogotá D.C. - Valores NSR-10

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| **Aa** (aceleración pico efectiva) | **0.15** | Tabla A.2.3-2 |
| **Av** (velocidad pico efectiva) | **0.20** | Tabla A.2.3-2 |
| **Zona de amenaza sísmica** | **Intermedia** | A.2.3.2 |
| **Microzonificación** | Sí (Decreto 523/2010, compilado en 670/2025) | A.2.1.2.1 |

## Aplicabilidad para el pipeline

### En Bogotá D.C. SÍ aplican:
- ✅ Requisitos de separación sísmica entre edificaciones vecinas (A.6.5)
- ✅ Para edificaciones > 2 pisos aéreos en colindancia
- ✅ Microzonificación sísmica propia (más detallada que NSR-10 genérico)

### En Bogotá D.C. NO aplican (excepciones):
- ❌ Casas de 1-2 pisos (no requieren separación sísmica)
- ❌ Edificaciones con paramento colindante con vía pública o zona verde pública
- ❌ Edificaciones de Reconocimiento (legalización)

## Para ANALISIS_VECINOS.py

La función principal del NSR-10 en el pipeline es el cálculo de **separaciones sísmicas**
entre la edificación nueva y los vecinos. Esto se suma a los retiros urbanísticos del POT.

### Regla de aplicación
```
separación_final = MÁXIMO(retiro_urbano_POT, separación_sísmica_NSR)
```

### Tabla A.6.5-1 (resumen)

| Pisos aéreos en colindancia | Vecina no se separó | Losas coinciden | Losas no coinciden | Sin vecina |
|------------------------------|---------------------|-----------------|--------------------|-------------|
| 1-2 pisos | no requiere | no requiere | no requiere | no requiere |
| 3 pisos | no requiere | no requiere | **1% de hn** | no requiere |
| >3 pisos | n/a | **2% de hn** | **3% de hn** | **1% de hn** |

Donde `hn` = altura de la edificación nueva en la colindancia.

## Extractos completos

## A.1.2 - Objeto y organización del Reglamento

```
TÍTULO K — Otros requisitos complementarios

A.1.2.2 — OBJETO — El presente Reglamento de Construcciones Sismo Resistentes, NSR-10, tiene por objeto:

A.1.2.2.1 — Reducir a un mínimo el riesgo de la pérdida de vidas humanas, y defender en lo posible el
patrimonio del Estado y de los ciudadanos.

A-1

Edición 47.663
Viernes 26 de marzo de 2010

D I A R I O O F I C I A L

15

A.1.2.2.2 — Una edificación diseñada siguiendo los requisitos de este Reglamento, debe ser capaz de
resistir, además de las fuerzas que le impone su uso, temblores de poca intensidad sin daño, temblores
moderados sin daño estructural, pero posiblemente con algún daño a los elementos no estructurales y un
temblor fuerte con daños a elementos estructurales y no estructurales pero sin colapso.

A.1.2.2.3 — Además de la defensa de la vida, con el cumplimiento de los niveles prescritos por el presente
Reglamento para los movimientos sísmicos de diseño, los cuales corresponden a requisitos mínimos
establecidos para el diseño de elementos estructurales y elementos no estructurales, se permite proteger en
alguna medida el patrimonio.

A.1.2.2.4 — Los movimientos sísmicos de diseño prescritos en el presente Reglamento corresponden a los
que afectarían las edificaciones de presentarse un sismo fuerte. Ante la ocurrencia, en el territorio nacional,
de un sismo fuerte que induzca movimientos de características similares a los movimientos sísmicos de
diseño prescritos en el presente Reglamento deben esperarse, en las edificaciones construidas cumpliendo
con el Reglamento, daños estructurales y no estructurales reparables, aunque en algunos casos pueda que
no sea económicamente factible su reparación.
```

---

## A.2.2 - Movimientos sísmicos de diseño (Aa, Av)

```
aA o

A.2.2 — MOVIMIENTOS SÍSMICOS DE DISEÑO

A.2.2.1 — Los movimientos sísmicos de diseño se definen en función de la aceleración pico efectiva, representada
por el parámetro
vA , para una probabilidad del
diez por ciento de ser excedidos en un lapso de cincuenta años. Los valores de estos coeficientes, para efectos de
este Reglamento, deben determinarse de acuerdo con A.2.2.2 y A.2.2.3.

aA , y de la velocidad pico efectiva, representada por el parámetro

A.2.2.2 — Se determina el número de la región en donde está localizada la edificación usando para
figura A.2.3-2 y el número de la región donde está localizada la edificación para

aA el mapa de la
vA , en el mapa de la figura A.2.3-3.

vA se obtienen de la tabla A.2.2-1, en función del número de la región determinado
A.2.2.3 — Los valores de
en A.2.2.2. Para las ciudades capitales de departamento del país los valores se presentan en la tabla A.2.3-2 y para
todos los municipios del país en el Apéndice A-4 incluido al final del presente Título.

aA y

Tabla A.2.2-1

vA , según las regiones
Valores de
De los mapas de las figuras A.2.3-2 Y A.2.3-3

aA y de

Región Nº

10
9
8
7
6
5
4
3
2
1

Valor de
vA

aA o de
0.50
0.45
```

---

## A.2.3 - Zonas de Amenaza Sísmica (Baja, Intermedia, Alta)

```
0.05

A.2.3 — ZONAS DE AMENAZA SÍSMICA

La edificación debe localizarse dentro de una de las zonas de amenaza sísmica que se definen en esta sección y que
están presentadas en el Mapa de la figura A.2.3-1.

A.2.3.1 — ZONA DE AMENAZA SÍSMICA BAJA — Es el conjunto de lugares en donde tanto
menores o iguales a 0.10. Véase la tabla A.2.3-1.

aA como

vA son

A.2.3.2 — ZONA DE AMENAZA SÍSMICA INTERMEDIA — Es el conjunto de lugares en donde
son mayores de 0.10 y ninguno de los dos excede 0.20. Véase la tabla A.2.3-1.

aA o

vA , o ambos,

A.2.3.3 — ZONA DE AMENAZA SÍSMICA ALTA — Es el conjunto de lugares en donde
mayores que 0.20. Véase la tabla A.2.3-1.

aA o

vA , o ambos, son

Nivel de amenaza sísmica según valores de

aA y de

vA

Tabla A.2.3-1

Mayor valor entre

aA y

vA

0.50
0.45
0.40
0.35
0.30
0.25
0.20
0.15
0.10
0.05

Asociado en mapas
de las figuras A.2.3-2
y A.2.3-3 a Región Nº
10
9
8
7
6
5
```

---

## A.2.4 - Efectos locales (perfiles de suelo)

```
A-19

A.2.4 — EFECTOS LOCALES

En esta sección se dan los tipos de perfil de suelo y los valores de los coeficientes de sitio. El perfil de suelo debe ser
determinado por el ingeniero geotecnista a partir de unos datos geotécnicos debidamente sustentados.

A.2.4.1 — GENERAL — Se prescriben dos factores de amplificación del espectro por efectos de sitio, aF y vF , los
cuales afectan la zona del espectro de períodos cortos y períodos intermedios, respectivamente. Los efectos locales
de la respuesta sísmica de la edificación deben evaluarse con base en los perfiles de suelo dados a continuación,
independientemente del tipo de cimentación empleado. La identificación del perfil de suelo se realiza a partir de la
superficie del terreno. Cuando existan sótanos, o en edificio en ladera, el ingeniero geotecnista, de acuerdo con el tipo
de cimentación propuesta, puede variar el punto a partir del cual se inicia la definición del perfil, por medio de un
estudio acerca de la interacción que pueda existir entre la estructura de contención y el suelo circundante; pero en
ningún caso este punto puede estar por debajo de la losa sobre el terreno del sótano inferior.

A.2.4.1.1 — Estabilidad del depósito de suelo — Los perfiles de suelo presentados en esta sección A.2.4
hacen referencia a depósitos estables de suelo. Cuando exista la posibilidad de que el depósito no sea
estable, especialmente ante la ocurrencia de un sismo, como puede ser en sitios en ladera o en sitios con
suelos potencialmente licuables, no deben utilizarse las definiciones dadas y hay necesidad de realizar una
investigación geotécnica que identifique la estabilidad del depósito, además de las medidas correctivas, si son
posibles, que se deben tomar para poder adelantar una construcción en el lugar. El estudio geotécnico debe
indicar claramente las medidas correctivas y los coeficientes de sitio que se debe utilizar en el diseño, dado
que se lleven a cabo las medidas correctivas planteadas. La construcción de edificaciones en el sitio no
puede adelantarse sin tomar medidas correctivas, cuando éstas sean necesarias.

A.2.4.1.2 — Procedimientos alternos — Cuando según A.2.1.2 se permitan procedimientos alternos para
definir los efectos locales, se debe cumplir con lo requerido allí en vez de lo presentado en esta sección.

A.2.4.2 — TIPOS DE PERFIL DE SUELO — Se definen seis tipos de perfil de suelo los cuales se presentan en la
tabla A.2.4-1. Los parámetros utilizados en la clasificación son los correspondientes a los 30 m superiores del perfil
para los perfiles tipo A a E. Aquellos perfiles que tengan estratos claramente diferenciables deben subdividirse,
asignándoles un subíndice i que va desde 1 en la superficie, hasta n en la parte inferior de los 30 m superiores del
perfil. Para el perfil tipo F se aplican otros criterios y la respuesta no debe limitarse a los 30 m superiores del perfil en
los casos de perfiles con espesor de suelo significativo.

A.2.4.3 — PARÁMETROS EMPLEADOS EN LA DEFINICIÓN DEL TIPO DE PERFIL DE SUELO — A continuación
se definen los parámetros que se utilizan para definir el tipo de perfil de suelo con base en los 30 m superiores del
mismo y considerando ensayos realizados en muestras tomadas al menos cada 1.50 m de espesor del suelo. Estos
sv , en m/s, (b) el número medio de golpes del ensayo
parámetros son (a) la velocidad media de la onda de cortante,
de penetración estándar, N , en golpes/píe a lo largo de todo el perfil, o, (c) cuando se trate de considerar por
separado los estratos no cohesivos y los cohesivos del perfil, para los estratos de suelos no cohesivos se determinará
chN , en golpes/píe, y para los cohesivos la
el número medio de golpes del ensayo de penetración estándar,
resistencia media al corte obtenida del ensayo para determinar su resistencia no drenada, us , en kPa. Además se
(cid:7)IP , y el contenido de agua en porcentaje, w .
emplean el Índice de Plasticidad (cid:6)

A.2.4.3.1 — Velocidad media de la onda de cortante — La velocidad media de la onda de cortante se
obtiene por medio de:

(cid:8)

v

s

n
(cid:10)
(cid:8)
i 1
n
(cid:10)
(cid:8)
i 1

d

i

d
v

si

i

(A.2.4-1)

donde:
siv
```

---

## A.2.5 - Coeficiente de Importancia (Grupos de Uso I-IV)

```
geotecnista de la edificación, debidamente sustentados.

A.2.5 — COEFICIENTE DE IMPORTANCIA

En esta sección se definen los grupos de tipo de uso y los valores del coeficiente de importancia.

A.2.5.1 — GRUPOS DE USO — Todas las edificaciones deben clasificarse dentro de uno de los siguientes Grupos
de Uso:

A.2.5.1.1 — Grupo IV — Edificaciones indispensables — Son aquellas edificaciones de atención a la
comunidad que deben funcionar durante y después de un sismo, y cuya operación no puede ser trasladada
rápidamente a un lugar alterno. Este grupo debe incluir:

(a) Todas las edificaciones que componen hospitales clínicas y centros de salud que dispongan de
servicios de cirugía, salas de cuidados intensivos, salas de neonatos y/o atención de urgencias,
(b) Todas las edificaciones que componen aeropuertos, estaciones ferroviarias y de sistemas

masivos de transporte, centrales telefónicas, de telecomunicación y de radiodifusión,

(c) Edificaciones designadas como refugios para emergencias, centrales de aeronavegación,

hangares de aeronaves de servicios de emergencia,

(d) Edificaciones de centrales de operación y control de líneas vitales de energía eléctrica, agua,

combustibles, información y transporte de personas y productos,

(e) Edificaciones que contengan agentes explosivos, tóxicos y dañinos para el público, y
(f) En el grupo IV deben incluirse las estructuras que alberguen plantas de generación eléctrica de
emergencia, los tanques y estructuras que formen parte de sus sistemas contra incendio, y los
accesos, peatonales y vehiculares de las edificaciones tipificadas en los literales a, b, c, d y e del
presente numeral.

A-24

A-25

Edición 47.663
Viernes 26 de marzo de 2010

D I A R I O O F I C I A L

21

A.2.5.1.2 — Grupo III — Edificaciones de atención a la comunidad — Este grupo comprende aquellas
edificaciones, y sus accesos, que son indispensables después de un temblor para atender la emergencia y
preservar la salud y la seguridad de las personas, exceptuando las incluidas en el grupo IV. Este grupo debe
incluir:

(a) Estaciones de bomberos, defensa civil, policía, cuarteles de las fuerzas armadas, y sedes de las

oficinas de prevención y atención de desastres,

(b) Garajes de vehículos de emergencia,
(c) Estructuras y equipos de centros de atención de emergencias,
(d) Guarderías, escuelas, colegios, universidades y otros centros de enseñanza,
(e) Aquellas del grupo II para las que el propietario desee contar con seguridad adicional, y
(f) Aquellas otras que la administración municipal, distrital, departamental o nacional designe como

tales.

A.2.5.1.3 — Grupo II — Estructuras de ocupación especial — Cubre las siguientes estructuras:

(a) Edificaciones en donde se puedan reunir más de 200 personas en un mismo salón,
(b) Graderías al aire libre donde pueda haber más de 2000 personas a la vez,
(c) Almacenes y centros comerciales con más de 500 m² por piso,
(d) Edificaciones de hospitales, clínicas y centros de salud, no cubiertas en A.2.5.1.1.
(e) Edificaciones donde trabajen o residan más de 3000 personas, y
(f) Edificios gubernamentales.

A.2.5.1.4 — Grupo I — Estructuras de ocupación normal — Todas la edificaciones cubiertas por el
alcance de este Reglamento, pero que no se han incluido en los Grupos II, III y IV.

A.2.5.2 — COEFICIENTE DE IMPORTANCIA — El Coeficiente de Importancia, I , modifica el espectro, y con ello las
fuerzas de diseño, de acuerdo con el grupo de uso a que esté asignada la edificación para tomar en cuenta que para
edificaciones de los grupos II, III y IV deben considerarse valores de aceleración con una probabilidad menor de ser
excedidos que aquella del diez por ciento en un lapso de cincuenta años considerada en el numeral A.2.2.1. Los
valores de I se dan en la tabla A.2.5-1.

(cid:8)

S

a

Tabla A.2.5-1
Valores del coeficiente de importancia, I

Grupo de Uso

IV
III
II
I

Coeficiente de
Importancia, I
1.50
1.25
1.10
1.00
```

---

## A.2.5.1 - Grupos de Uso (I, II, III, IV)

```
En esta sección se definen los grupos de tipo de uso y los valores del coeficiente de importancia.

A.2.5.1 — GRUPOS DE USO — Todas las edificaciones deben clasificarse dentro de uno de los siguientes Grupos
de Uso:

A.2.5.1.1 — Grupo IV — Edificaciones indispensables — Son aquellas edificaciones de atención a la
comunidad que deben funcionar durante y después de un sismo, y cuya operación no puede ser trasladada
rápidamente a un lugar alterno. Este grupo debe incluir:

(a) Todas las edificaciones que componen hospitales clínicas y centros de salud que dispongan de
servicios de cirugía, salas de cuidados intensivos, salas de neonatos y/o atención de urgencias,
(b) Todas las edificaciones que componen aeropuertos, estaciones ferroviarias y de sistemas

masivos de transporte, centrales telefónicas, de telecomunicación y de radiodifusión,

(c) Edificaciones designadas como refugios para emergencias, centrales de aeronavegación,

hangares de aeronaves de servicios de emergencia,

(d) Edificaciones de centrales de operación y control de líneas vitales de energía eléctrica, agua,

combustibles, información y transporte de personas y productos,

(e) Edificaciones que contengan agentes explosivos, tóxicos y dañinos para el público, y
(f) En el grupo IV deben incluirse las estructuras que alberguen plantas de generación eléctrica de
emergencia, los tanques y estructuras que formen parte de sus sistemas contra incendio, y los
accesos, peatonales y vehiculares de las edificaciones tipificadas en los literales a, b, c, d y e del
presente numeral.

A-24

A-25

Edición 47.663
Viernes 26 de marzo de 2010

D I A R I O O F I C I A L

21

A.2.5.1.2 — Grupo III — Edificaciones de atención a la comunidad — Este grupo comprende aquellas
edificaciones, y sus accesos, que son indispensables después de un temblor para atender la emergencia y
preservar la salud y la seguridad de las personas, exceptuando las incluidas en el grupo IV. Este grupo debe
incluir:

(a) Estaciones de bomberos, defensa civil, policía, cuarteles de las fuerzas armadas, y sedes de las

oficinas de prevención y atención de desastres,

(b) Garajes de vehículos de emergencia,
(c) Estructuras y equipos de centros de atención de emergencias,
(d) Guarderías, escuelas, colegios, universidades y otros centros de enseñanza,
(e) Aquellas del grupo II para las que el propietario desee contar con seguridad adicional, y
(f) Aquellas otras que la administración municipal, distrital, departamental o nacional designe como

tales.

A.2.5.1.3 — Grupo II — Estructuras de ocupación especial — Cubre las siguientes estructuras:

(a) Edificaciones en donde se puedan reunir más de 200 personas en un mismo salón,
(b) Graderías al aire libre donde pueda haber más de 2000 personas a la vez,
(c) Almacenes y centros comerciales con más de 500 m² por piso,
(d) Edificaciones de hospitales, clínicas y centros de salud, no cubiertas en A.2.5.1.1.
(e) Edificaciones donde trabajen o residan más de 3000 personas, y
(f) Edificios gubernamentales.

A.2.5.1.4 — Grupo I — Estructuras de ocupación normal — Todas la edificaciones cubiertas por el
alcance de este Reglamento, pero que no se han incluido en los Grupos II, III y IV.

A.2.5.2 — COEFICIENTE DE IMPORTANCIA — El Coeficiente de Importancia, I , modifica el espectro, y con ello las
fuerzas de diseño, de acuerdo con el grupo de uso a que esté asignada la edificación para tomar en cuenta que para
edificaciones de los grupos II, III y IV deben considerarse valores de aceleración con una probabilidad menor de ser
excedidos que aquella del diez por ciento en un lapso de cincuenta años considerada en el numeral A.2.2.1. Los
valores de I se dan en la tabla A.2.5-1.

(cid:8)

S

a

Tabla A.2.5-1
```

---

## A.6.5 - Separación entre estructuras adyacentes (CRÍTICO)

```
interiores y exteriores así como los cielorrasos se diseñen para acomodar las derivas del piso.

A.6.5 — SEPARACIÓN ENTRE ESTRUCTURAS ADYACENTES POR CONSIDERACIONES
SÍSMICAS

A.6.5.1 — DENTRO DE LA MISMA CONSTRUCCIÓN — Todas las partes de la estructura deben diseñarse y
construirse para que actúen como una unidad integral para efectos de resistir las fuerzas sísmicas, a menos que se
separen una distancia suficiente para evitar la colisión nociva entre las partes. Para determinar la distancia mínima de
separación debe sumarse el valor absoluto de los desplazamientos horizontales totales obtenidos en A.6.2.1 para
cada una de las porciones de la edificación en la dirección perpendicular a la junta que las separe, a menos que se
tomen medidas para que no se presente daño a la estructura al utilizar una distancia menor.

A.6.5.2 — ENTRE EDIFICACIONES VECINAS QUE NO HAGAN PARTE DE LA MISMA CONSTRUCCIÓN — La
separación entre edificaciones vecinas, para evitar efectos nocivos ante la ocurrencia de un sismo, debe cumplir los
siguientes requisitos:

A.6.5.2.1 — Alcance — La presente reglamentación es aplicable en los siguientes casos:

(a) En municipios localizados en Zonas de Amenaza Sísmica Baja según lo dispone el presente
Reglamento en su Capítulo A.2 no se requieren consideraciones de separación sísmica entre
edificaciones vecinas.

(b) Solo aplica para la obtención de licencias de construcción de edificaciones nuevas que se

soliciten por primera vez con posterioridad a la adopción del presente Reglamento.

(c) No aplica para el caso de edificaciones que sean objeto del trámite de Reconocimiento.

(d) Para el caso de rehabilitaciones sísmicas de edificaciones existentes aplican los requisitos

especiales que se indican en A.10.7.

(e) Los requisitos de esta sección del Reglamento pueden ser modificados por la administración
municipal o distrital, siempre y cuando los requisitos de la separación sísmica que resulten de la
aplicación de la reglamentación municipal o distrital no sean menores que los dados aquí.

A.6.5.2.2 — Definiciones — En el Capítulo A.13 deben consultarse las siguientes definiciones: altura del
piso, altura de la edificación en la colindancia, cerramiento, coincidencia de las losas de entrepiso en la
colindancia, nivel (medido desde la base) de un piso en la colindancia, número de pisos aéreos de la
edificación, número de pisos aéreos en la colindancia, y separación sísmica en la colindancia. Además debe
tenerse en cuenta cuando el terreno es inclinado en la colindancia, o haya diferentes alturas de piso en la
colindancia, o exista un número diferente de pisos aéreos en la colindancia, que debe utilizarse la altura de
piso, o el número de pisos aéreos que conduzca a la mayor separación sísmica.

A.6.5.2.3 — Requisitos de separación sísmica con respecto al paramento del lote para edificaciones
nuevas — Deben cumplirse los siguientes requisitos para efectos de determinar la separación sísmica con
respecto al paramento del lote en edificaciones nuevas cubiertas por el alcance dado en A.6.5.2.1:

(a) Cuando el paramento del lote sea colindante con vía pública o zona verde pública no requiere
separación sísmica con respecto al paramento en ese costado o costados. Ello no exime cumplir
los requisitos urbanísticos de las normas municipales para la edificación en lo referente a
retrocesos.

(b) Cuando en la colindancia haya un cerramiento, y la edificación nueva esté separada de este
cerramiento en una distancia que supera la señalada para el piso crítico en la Tabla A.6.5-1 no se

A-76

A-77

34

D I A R I O O F I C I A L

Edición 47.663
Viernes 26 de marzo de 2010

requiere separación sísmica del cerramiento de la edificación nueva con respecto al paramento
del lote.

(c) Las edificaciones con uno o dos pisos aéreos en la colindancia no requieren separación sísmica

(véase también la Tabla A.6.5-1).

(d) Las edificaciones de más de dos pisos aéreos en la colindancia deben separarse del paramento

en la colindancia así (véase también la Tabla A.6.5-1 y la Figura A.6.5-1):

(i) Edificaciones hasta de tres pisos aéreos en la colindancia — No se requiere
separación sísmica de la edificación nueva con respecto al paramento cuando no haya
edificación vecina existente, o cuando las losas de la edificación nueva coinciden en la
colindancia (véanse las definiciones) con las de la edificación vecina existente en la
misma colindancia. Si las losas de entrepiso de la edificación nueva no coinciden con las
de la edificación existente se requiere una separación sísmica de la edificación nueva con
respecto al paramento igual al 1% (uno por ciento) de la altura de la edificación nueva en
la colindancia.

(ii) Edificaciones de más de tres pisos aéreos en la colindancia — Cuando las losas de
la edificación nueva coinciden en la colindancia (véanse las definiciones) con las de la
edificación vecina existente en la misma colindancia la edificación nueva debe retirarse
del paramento en la colindancia una distancia de separación sísmica igual al 2% (dos por
ciento) de la altura de la edificación nueva en la colindancia. Cuando las losas de
entrepiso de la edificación nueva no coincidan con las de la edificación existente en la
colindancia, esta separación sísmica debe ser del 3% (tres por ciento) de la altura de la
edificación nueva en la colindancia. Si no existe edificación vecina en la colindancia
(cubre además el caso de que sea solo un cerramiento), esta separación sísmica debe
ser del 1% (uno por ciento) de la altura de la edificación nueva en la colindancia.

(e) Cuando se requiera separación sísmica, la separación en cualquier piso en particular
corresponde a la distancia horizontal en dirección perpendicular al plano vertical levantado sobre
el lindero entre los dos lotes de terreno, medida desde la losa de entrepiso de la edificación hasta
este plano, calculada utilizando la altura sobre el nivel del terreno del piso en particular
multiplicada por el coeficiente que indique la Tabla A.6.5-1 para ese caso. Véase también la
Figura A.6.5-1.

(f) Deben tomarse precauciones para que no se depositen materiales extraños dentro de la
separación sísmica entre edificaciones. Así mismo debe colocarse un protección de humedad
apropiada para que el agua lluvia no entre dentro de la abertura de la separación sísmica.

(g) Para el caso de edificaciones objeto de reforzamiento y rehabilitación sísmica el ingeniero
diseñador de la rehabilitación debe dejar constancia de que estudió el potencial efecto nocivo de
la interacción con las edificaciones vecinas colindantes y que tomó las medidas apropiadas según
su mejor criterio dentro de lo requerido en A.10.1.7.

(h) El paramento del lote y la separación sísmica requerida deben quedar claramente indicados en
los planos arquitectónicos que se presentan a la autoridad competente o curaduría para la
obtención de la licencia de construcción.

Tabla A.6.5-1
Separación sísmica mínima en la cubierta entre
edificaciones colindantes que no hagan parte de la misma construcción

Altura de la
edificación nueva

Tipo de Colindancia
Existe edificación vecina que no ha dejado
la separación sísmica requerida

Coinciden las losas
de entrepiso

No coinciden las
losas de entrepiso

1 y 2 pisos

3 pisos

no requiere
separación

no requiere
separación

Más de 3 pisos

0.02 veces la altura
de la edificación
nueva (2% de hn)

no requiere
separación
0.01 veces la altura
de la edificación
nueva (1% de hn)
0.03 veces la altura
de la edificación
nueva (3% de hn)

No existe
edificación vecina
o la que existe ha
dejado la
separación sísmica
requerida
no requiere
separación

no requiere
separación

0.01 veces la altura
de la edificación
nueva (1% de hn)

Notas:
1. Para obtener la separación sísmica en pisos diferentes a la cubierta se aplicará el coeficiente

indicado en la Tabla multiplicado por la altura sobre el terreno del piso en particular.

2. Cuando el terreno en la colindancia sea inclinado en el sentido del paramento, o haya
diferentes alturas de piso o diferentes números de pisos aéreos en la colindancia, se tomará
en la edificación nueva la altura de piso, o el número de pisos aéreos que conduzca a la
mayor separación sísmica.

Cubierta

Piso aéreo i

Piso aéreo 2

hn

hi

Separación sísmica para cualquier
piso, es como mínimo la distancia que
se obtiene al multiplicar el coeficiente
indicado en la Tabla A.6.5-1 por el
correspondiente hi.

Piso aéreo 1

h2

h1

Paramento

Nivel del terreno

Edificación nueva

Edificación existente

Figura A.6.5-1 — Medición de la separación sísmica (vista en elevación)

$

A-78

Notas:

A-79

CAPÍTULO A.7
INTERACCIÓN SUELO-ESTRUCTURA

A.7.1 — GENERAL

A.7.1.1 — DEFINICIÓN — La respuesta sísmica de la estructura está íntimamente ligada a la forma como los
movimientos sísmicos del terreno afectan la estructura a través de su cimentación. Las características dinámicas del
suelo subyacente, la rigidez y disposición de la cimentación y el tipo de sistema estructural de la edificación
interactúan entre sí para caracterizar los efectos sísmicos sobre ella. El hecho de que no se tome en cuenta la rigidez
de la cimentación y las características dinámicas del suelo subyacente en el análisis sísmico de la edificación puede
conducir a variaciones apreciables entre la respuesta sísmica estimada y la respuesta real de la estructura. Por las
razones anotadas es conveniente incluir los efectos de la interacción suelo-estructura en el análisis sísmico de la
edificación.

A.7.1.2 — EFECTOS ASOCIADOS CON LA INTERACCIÓN SUELO-ESTRUCTURA — Dependiendo de las
características de la estructura, de su cimentación y del suelo subyacente, la respuesta de la estructura ante
solicitaciones estáticas verticales y dinámicas (sismo) puede variar con respecto al estimativo que se realiza sin tener
en cuenta la interacción suelo-estructura, en los siguientes aspectos:

(a) La presencia de suelos blandos y compresibles en las distribución de esfuerzos y deformaciones bajo

losas de fundación, tanto ante solicitaciones de cargas verticales como de fuerzas horizontales,

(b) Aumento en el periodo del sistema suelo-estructura que considera la flexibilidad del suelo, respecto a la
evaluación de los períodos de vibración de la edificación considerando un modelo de base empotrada,
```

---

## Tabla A.2.3-2 - Valores Aa y Av para ciudades capitales

```
Reglamento NSR-10 lo siguiente:
" Tabla A.2.3-2 — Valor de Aa y de Av para las ciudades capitales de departamento.

3

4

" Figura A.2.3-1 — Zonas de Amenaza Sísmica aplicable a edificaciones para la NSR-10

Capítulo A.3 — Requisitos generales de diseño sismo resistente

en función de Aa y Av.

" Figura A.2.3-2 — Mapa de valores de Aa
" Figura A.2.3-3 — Mapa de valores de Av
" Tabla A.10.3-2 — Valor de Ae para las ciudades capitales de departamento.
" Figura A.10.3-1 — Mapa de valores de Ae
" Tabla A.12.2-2 — Valores de Ad para las ciudades capitales de departamento
" Figura A.12.2-1 — Mapa de valores de Ad
" Apéndice A-4 — Valores de Aa, Av, Ae y Ad y definición de la zona de amenaza sísmica

de los municipios colombianos

(cid:3) La sección A.2.4 — Efectos locales, que trata sobre la amplificación de las ondas sísmica debida
al suelo subyacente de la edificación fue actualizada y modernizada para el Reglamente
NSR-10. Los efectos de sitio se definen ahora por medio de coeficientes, Fa y Fv, que afectan
la zona de períodos cortos (0.1 s) y períodos medios del espectro (1 s) respectivamente.
(cid:3) En la sección A.2.5 — Coeficiente de importancia, donde se prescribe un mayor grado de
conservatismo en el diseño sismo
resistente de aquellas edificaciones que son
indispensables para la atención de la emergencia y la recuperación de la comunidad con
posterioridad a la ocurrencia de un sismo fuerte se actualizaron y modernizaron los grupos de
uso (I, II, III y IV), incluyéndose ahora las edificaciones escolares dentro del Grupo de Uso
III de edificaciones de atención a la comunidad siguiendo las tendencias mundiales al
respecto. Los valores del coeficiente de importancia, I, fueron actualizados también (Tabla
A.2.5-1).

(cid:3) La definición del espectro de diseño (A.2.6 — Espectro de diseño) se ajustó para tener en cuenta
los parámetros Aa y Av tal como se definen ahora. A diferencia del Reglamento NSR-98,
ahora se presentan también, además del espectro de aceleraciones, los espectros de
velocidades y de desplazamientos.

(cid:3) Los requisitos para el uso de familias de acelerogramas como alternativa de diseño sismo
resistente a los espectros, A.2.7 — Familias de acelerogramas, se actualizó y modernizó para
que sea compatible con la definición de la amenaza sísmica que se prescribe en el
Reglamento NSR-10.

(cid:3)

 Se actualizaron y ajustaron los requisitos de A.2.9 — Estudios de microzonificación sísmica de
acuerdo con las experiencias nacionales en la realización de estos estudios y los registros
acelerográficos registrados en suelo blando en ciudades colombianas. En A.2.9.3.7(e) se
trascribe lo requerido en el Artículo 2° del Decreto 2809 de 2000 respecto a la necesidad de
recurrir a un concepto por parte de la Comisión Asesora Permanente del Régimen de
Construcciones Sismo Resistentes de los estudios de microzonificación cuando en su
elaboración se han utilizado fondos de entidades de la Nación y en A.2.9.5 se sugiere
armonizar los estudios de microzonificación existentes al nuevo Reglamento NSR-10.
(cid:3) Se incluye una nueva sección A.2.10 — Estudios sísmicos particulares de sitio que regula la
elaboración de estudios de sitio particulares para determinar los efectos de amplificación en
edificaciones cuya importancia o tamaño así lo ameriten.

(cid:3) La filosofía general de este capítulo se ha mantenido igual a la del Reglamento NSR-98. Se

hicieron ajustes y actualizaciones en los siguientes aspectos:

(cid:3) En A.3.3 — Configuración estructural de la edificación, se hizo una actualización de los sistemas
estructurales permitidos y del manejo de las irregularidades con más casos de los
contemplados anteriormente. Ahora se incluye un factor de castigo por falta de redundancia
del sistema estructural para evitar el diseño de estructuras vulnerables sísmicamente debido
a ausencia de redundancia estructural (A.3.3.8 — Ausencia de redundancia en el sistema
estructural de resistencia sísmica).

(cid:3) En A.3.3.9 — Uso del coeficiente de sobrerresistencia (cid:2)0, se introduce un nuevo parámetro para
tratar adecuadamente elementos estructurales que no están en capacidad de disipar energía
en el rango de respuesta inelástico como vienen haciéndolo las normas base desde hace
algunos años.
(cid:3) Se modernizan

incluyendo
procedimientos no-lineales (A.3.4 — Métodos de análisis), teniendo en cuenta de esta
manera los enormes avances que han ocurrido en las ciencias de la computación en la última
década.

tanto estático como dinámico,

los requisitos de análisis,

(cid:3) En A.3.6.8 — Diafragmas, se modernizó la forma como se calculan las fuerzas inerciales que

actúan en los diafragmas.

(cid:3) Se permite el uso de aisladores en la base (A.3.8 — Estructuras aisladas sísmicamente en su
base) y disipadores de energía (A.3.9 — Uso de elementos disipadores de energía) y se fijan
los parámetros y requisitos para su uso, abriendo de esta manera la posibilidad de utilizar en
el país estas técnicas muy modernas, pero haciendo referencia a los documentos apropiados
para que su empleo se realice con todas las garantías del caso.

(cid:3) Las Tablas A.3-1 a A.3-4 donde se regulan los sistemas estructurales permitidos, las alturas
según la zona de amenaza sísmica y los grupos de uso donde pueden utilizarse, fueron
actualizadas teniendo en cuenta la amplia experiencia nacional al respecto y buscando, en
varios casos, la forma de reducir costos en los sistemas estructurales que se utilizan
```

---

## Referencias cruzadas

- [[decreto-555-extractos]] - POT Bogotá
- [[decreto-670-extractos]] - Compilación POT
- [[03-retiros-obligatorios]] - Retiros POT
- [[04-edificabilidad-y-ocupacion]] - Edificabilidad POT

## JSONs estructurados generados

- `data/nsr-10/separaciones-sismicas.json` - Tabla A.6.5-1 estructurada
- `data/nsr-10/grupos-uso-coef-importancia.json` - Grupos I-IV con coeficientes
- `data/nsr-10/amenaza-sismica-bogota.json` - Valores Aa/Av para Bogotá

## Notas de implementación

### Para CONTEXTO_v09.py
- Cargar `amenaza-sismica-bogota.json` para verificar si aplican separaciones
- Bogotá está en Zona Intermedia → SÍ aplican requisitos A.6.5

### Para ANALISIS_VECINOS.py
- Cargar `separaciones-sismicas.json` para tabla A.6.5-1
- Calcular separación según número de pisos del proyecto (parámetro de entrada)
- Comparar con retiros urbanísticos del POT (tomar el mayor)

### Para VOLUMEN_v04.py
- Considerar coeficiente de importancia según grupo de uso
- Edificaciones residenciales normales: Grupo I, I=1.00
- Si el proyecto incluye >200 personas en un salón: Grupo II, I=1.10
