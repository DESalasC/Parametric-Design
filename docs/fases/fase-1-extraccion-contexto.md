Fase 1: Extracción de Contexto Urbano (Backend Python)

Objetivo: Obtener la geometría del lote, vecinos, vías y topografía de la geobase catastral y la API de Bogotá, entregando un JSON estructurado con coordenadas locales.
Problema Resuelto

    Identificadores Catastrales: El CHIP alfanumérico (AAA...) no existe en la capa Lote. Se programó un JOIN automático con la capa Predio para obtener el LotCodigo numérico.
    Topografía: La API REST de Catastro no permite descargas masivas de raster. Se implementó una consulta punto a punto (Identify) optimizada para evaluar solo esquinas, puntos medios y centroide del lote.
    Coordenadas Locales: Las coordenadas SIRGAS rompen la precisión de ArchiCAD. Se aplica un offset matemático usando la esquina Sur-Occidental global para anclar todo el contexto al (0,0,0).

Scripts Producidos

    scripts/utilities/fetch-urban-context-v5.py: Script principal de extracción.
    scripts/utilities/inspect-pot-fields.py: Script de depuración para descubrir los nombres reales de los campos en la geodatabase del POT.

Datos Extraídos (Geodatabase POT)

Se descubrió que las capas del POT no tienen nombres estándar. El script v5 mapea dinámicamente:

    UPZ: Capa Area_elevacion_maxima, Campo NOMBRE_UPI.
    Tratamiento: Capa TratamientoUrbanistico, Campo NOMBRE_TRATAMIENTO.
    Altura: Capa TratamientoUrbanistico, Campo ALTURA_MAXIMA (en pisos, multiplicado por 3.8m).

Output

Genera data/pot-cache/<CHIP>-contexto.json con metadatos SIRGAS, geometría 2D/3D local y pot_data real.
