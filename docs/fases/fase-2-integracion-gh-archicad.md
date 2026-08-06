Fase 2: Integración Grasshopper - ArchiCAD (Frontend)

Objetivo: Leer el JSON de contexto, dibujar la geometría en Rhino/Grasshopper e inyectarla en ArchiCAD usando Tapir, respetando capas y origen.
Problema Resuelto

    Separación de Espacio Público: El catastro trae los lotes pegados. Se usó Rhino.Geometry.Curve.CreateBooleanDifference restando los lotes privados del Bounding Box de 75m para obtener las vías limpias.
    Offset Invertido: La función Offset de RhinoCommon expande la curva si fue dibujada en sentido horario. Se añadió una validación de área: si el área resultante es mayor al lote, invierte la distancia del offset.
    Desplazamiento en ArchiCAD (Bug del Puente): Tapir desplazaba la geometría ~265m del origen debido a conflictos con el Survey Point interno. Se solucionó aplicando un componente Move en Grasshopper usando un vector desde la esquina inferior del Bounding Box hacia el (0,0,0) absoluto.

Scripts Producidos

    src/fase-1-contexto/F1_CONTEXTO_POT_v04.py: Lee JSON, genera curvas 2D cerradas, separa vías y malla topográfica (Delaunay).

Configuración en Grasshopper

    Las salidas se conectan a componentes Tapir Element Settings (para asignar capas GuBIMclass) y luego a Tapir Polyline / Tapir Mesh.
    Type Hints configurados como "No Type Hint" o "Curve" para evitar errores de conversión de IronPython.

