Fase 3: Motor Normativo y Prisma Edificable (Resumen de Sesión)

Objetivo: Aplicar automáticamente la normativa POT (Retiros, Alturas, IC, IO) sobre la geometría del lote para generar el volumen máximo edificable.
1. Logros Alcanzados (Lo que funciona perfectamente)

    Base de Conocimiento Normativa (normativa-upz.json):
        Se creó un JSON que unifica el Decreto 555/2021 con normativas de ultraactividad (Decreto 299/2002 y Resolución 1673/2010).
        El sistema distingue entre UPZs y Sectores Normativos. Si el lote está en el Sector 5 de la UPZ El Prado, el IC máximo sube a 5.5; de lo contrario, se usa 2.5.
    Cálculo de Ocupación (IO):
        El script calcula el IO real (Área huella / Área lote) y verifica que no supere el límite (ej: 0.60).
    Altura Variable y Maximización de Rentabilidad:
        El script respeta estrictamente la altura máxima del POT (ej: 11.4m).
        Calcula cuántos pisos habitables + 1 piso de servicio caben dentro de esa altura, usando la altura mínima reglamentaria de entrepiso (2.5m) para maximizar el número de pisos (ej: 4 pisos a 2.85m en lugar de 3 pisos a 3.8m).
        Verifica que el IC real no supere el máximo permitido; si lo hace, reduce el número de pisos automáticamente.
    Piso de Servicios:
        Se implementó la reglamentación de Bogotá que permite 1 piso adicional no computable para servicios.

2. El Problema Pendiente (Lo que falló)

El Offset Direccional y el Auto-Patio Posterior.

    Síntoma: Al intentar aplicar retiros diferentes (Frontal, Lateral, Posterior), el script deforma la geometría original. Al intentar crear un "Auto-Patio" restando un rectángulo o moviendo líneas, el script se confunde y hace los cortes en el lado incorrecto (ej: corta la esquina frontal en lugar del fondo).
    Causa Raíz: El script intenta adivinar qué lado es el "frente" y cuál es el "fondo" usando matemáticas puras (ej: Min X+Y o Max X+Y, o distancia al centroide). Sin embargo, debido a la rotación y forma del lote local, estas heurísticas fallan y el script mueve el lado equivocado.
    Soluciones Intentadas (Fallidas):
        Offset uniforme y escala (deforma el lote).
        Intersección de líneas infinitas (falla por dirección horaria/antihoraria en IronPython).
        Resta booleana de rectángulos de corte (crea triángulos por colapso de precisión).
        Reconstrucción topológica moviendo el segmento de "Max X+Y" (corta el lado frontal porque la rotación engaña al algoritmo).

3. La Solución Definitiva (Para la próxima sesión)

Para resolver el problema del patio posterior sin fallos, el script F1_NORMATIVA_APLICAR no debe adivinar la orientación del lote. Debe recibir información espacial explícita.

Plan de Acción:

    El script F1_NORMATIVA_APLICAR debe tener una nueva entrada: public_space_curve (la curva de las vías que ya generamos en Fase 1).
    Identificar el Frente: El script medirá la distancia de cada segmento del lote hacia la curva de la vía. El segmento más cercano se etiqueta como "Frente".
    Identificar el Fondo: El segmento paralelo opuesto (o el más alejado de la vía) se etiqueta como "Fondo/Posterior".
    Generar Patio: Una vez identificado el segmento posterior con certeza espacial, se aplica el retiro posterior y, si el IO se excede, se empuja ese segmento específico hacia adentro.

4. Scripts Producidos en esta Fase

    src/fase-1-contexto/F1_NORMATIVA_LEER_v09.py: Lee el JSON del POT y extrae retiros base.
    src/fase-1-contexto/F1_NORMATIVA_APLICAR_v21.py: Motor normativo actual (cálculos de IO/IC/Altura funcionan; offset direccional pendiente de fix espacial).
    data/pot-bogota/normativa-upz.json: Base de datos de normativas por UPZ y Sector.