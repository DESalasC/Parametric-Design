📄 ARCHIVO 1: ADR-007

Ruta en Proyecto: docs/arquitectura/decisiones-adr/adr-007-sistema-adquisicion-contexto-urbano.md
Ruta en Vault: vault/10-arquitectura/decisiones-adr/adr-007-sistema-adquisicion-contexto-urbano.md
ADR-006: Sistema de Adquisición de Contexto Urbano y Topográfico

Fecha: 2026-08-04Estado: AceptadoContexto: El flujo manual actual (obtener coordenadas en Google Maps, transformarlas a SIRGAS y dibujar el lote en ArchiCAD) genera problemas de localización, pérdida de precisión y no contempla la topografía natural del terreno en Bogotá. Además, consume tiempo de dibujo manual que puede automatizarse consultando la geobase catastral local.

Decisión:Se descontinúa el flujo manual. Se implementa un sistema de "Origen Local Georreferenciado" mediante los siguientes pasos:

    Entrada: El usuario ingresa el CHIP o Matrícula del predio.
    Extracción (Python 3.12): Un nuevo script (fetch-urban-context.py) consultará el archivo bd_uaecd.gpkg para extraer el lote, un buffer de 75m de contexto (vecinos y vías) y calculará el Bounding Box.
    Topografía Progresiva: El script consultará un Modelo Digital de Elevación (MDE) público (IDECA) para asignar cotas Z estimadas a los vértices y generar una malla de terreno. El sistema quedará abierto para recibir futuros levantamientos topográficos reales (CSV/LandXML), cambiando el estado de los datos de "ESTIMADA" a "REAL".
    Transformación de Coordenadas: Todas las geometrías se trasladarán a un entorno local (0,0,0) restando el Min-X y Min-Y del Bounding Box. El Origen SIRGAS (X,Y,Z) y el Azimuth se guardarán como metadatos en el JSON.
    Modelado (Grasshopper/Tapir): Los scripts GHPython leerán el JSON generado y dibujarán mallas topográficas y polígonos 3D nativos en ArchiCAD, configurando el Survey Point con los metadatos SIRGAS.

Consecuencias:

    Se requiere instalar rasterio y numpy en el entorno .venv.
    El script F1_CONTEXTO_POT_v01.py debe refactorizarse para leer el nuevo JSON en lugar de coordenadas manuales.
    Se elimina el problema de escala y precisión al modelar cerca del (0,0,0) local.