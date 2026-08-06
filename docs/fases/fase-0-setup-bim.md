Fase 0: Configuración BIM y Plantilla Estándar

Objetivo: Establecer una plantilla de ArchiCAD (.tpl) con la clasificación GuBIMclass/Uniclass 2015 estandarizada, evitando la creación manual de cientos de capas.
Problema Resuelto

El plugin Tapir no permite la creación masiva de capas en ArchiCAD desde Grasshopper mediante strings, y la API JSON-RPC de ArchiCAD presentaba bloqueos de puerto. Además, el Administrador de Atributos de ArchiCAD exige un formato XML nativo muy estricto (<AttributeFile>) con GUIDs únicos por capa.
Solución Implementada

Se creó un script en Python 3.12 que lee el archivo CSV de GuBIMclass y genera un XML nativo con la sintaxis exacta que ArchiCAD requiere.
Scripts Producidos

    scripts/utilities/generate-archicad-layers-xml-v3.py: Lee el CSV, extrae el código, nombre y extensión, genera un GUID único para cada capa y construye el árbol XML.
    data/GuBIMclass_Layers_v3.xml: Archivo de salida importable.

Flujo de Trabajo

    Ejecutar python scripts/utilities/generate-archicad-layers-xml-v3.py.
    En ArchiCAD (plantilla limpia): Opciones > Atributos de Elemento > Administrador de Atributos > Importar.
    Seleccionar GuBIMclass_Layers_v3.xml.
    Guardar el archivo como Plantilla_DiseñoParametrico.tpl.

Estado: Completado. 503 capas estándar cargadas en la plantilla base.
