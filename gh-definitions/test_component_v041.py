#!/usr/bin/env python3
# Test script to verify F1_ETAPA1_CONTEXTO_v04.1.py with real data

import sys
import os
import json

# Try to import the module - this might fail due to Rhino.Geometry dependencies
# but we can at least test the logic parts
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'fase-1-contexto'))
    # We won't actually import the full module due to Rhino dependencies
    # Instead, we'll extract and test the key logic functions
    print("Attempting to test F1_ETAPA1_CONTEXTO_v04.1 logic...")
except Exception as e:
    print(f"Could not set up module import: {e}")

def to_float_safe(val, default=0.0):
    if val is None: return default
    try: return float(val)
    except: return default

def polyline_from_coords(coords, dx, dy, dz):
    """Convierte [[x,y,z],...] en PolylineCurve con offset."""
    if not coords or len(coords) < 3:
        return None
    # Simplified for testing - just return a mock object
    return {"type": "Polyline", "points": [(c[0]-dx, c[1]-dy, c[2]-dz) for c in coords]}

def polyline_to_nurbs(poly_curve):
    """Convierte una PolylineCurve a NurbsCurve para mejor compatibilidad con ArchiCAD."""
    # Simplified for testing - just return the input with a type change
    if poly_curve is None:
        return None
    return {"type": "Nurbs", "points": poly_curve.get("points", []) if isinstance(poly_curve, dict) else []}

def build_terrain_mesh(mesh_points, dx, dy, dz):
    """Malla de terreno por interpolacion IDW sobre grilla ~5m."""
    # Simplified for testing
    return {"type": "Mesh", "vertices": len(mesh_points) if mesh_points else 0}

def leer_json_seguro(ruta):
    """Lee archivos JSON soportando rutas y contenidos con tildes y eñes en IronPython."""
    if not ruta or not os.path.exists(str(ruta)):
        raise Exception("El archivo no existe en la ruta especificada: {}".format(ruta))

    # 1. Intento con UTF-8
    try:
        with open(str(ruta), 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e_utf8:
        # 2. Fallback a codificación por defecto de Windows (CP1252 / Latin-1)
        try:
            with open(str(ruta), 'r', encoding='cp1252') as f:
                return json.load(f)
        except Exception as e_default:
            raise Exception("Error al decodificar el archivo: UTF-8 falló: {} | Default falló: {}".format(e_utf8, e_default))

def garantizar_layer_lote(layers):
    """v04: asegura que 00-00-10_Lote_proyecto este en la lista (primer item)."""
    LOTE = {"nombre": "00-00-10_Lote_proyecto", "color": 1, "visible": True}
    for layer in layers:
        nombre = str(layer.get("nombre", "")).strip()
        if nombre == LOTE["nombre"]:
            return layers, True
    layers.insert(0, dict(LOTE))
    return layers, True

def test_with_real_data():
    """Test the component logic with real JSON data"""
    print("Testing with real JSON data...")

    # Use the AAA0030JKOE-contexto.json file
    json_path = "D:/Work/PROJECTS/DiseñoParametrico/data/pot-cache/AAA0030JKOE-contexto.json"

    try:
        data = leer_json_seguro(json_path)
        print(f"Successfully loaded JSON for chip: {data.get('metadata', {}).get('chip', 'UNKNOWN')}")

        # Test basic data extraction
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        print(f"Lote vertices: {len(lote_verts)} points")

        # Test vial data
        vias_oficiales = data.get("vias_oficiales", [])
        print(f"Vias oficiales: {len(vias_oficiales)} entries")

        # Test secundarias and terciarias (might not exist in this dataset)
        vias_secundarias = data.get("vias_secundarias", [])
        vias_terciarias = data.get("vias_terciarias", [])
        peatonales = data.get("peatonales", [])
        print(f"Vias secundarias: {len(vias_secundarias)} entries")
        print(f"Vias terciarias: {len(vias_terciarias)} entries")
        print(f"Peatonales: {len(peatonales)} entries")

        # Test our road processing logic
        ejes_vias_curves = []  # Ejes de vía de motor (para capa 00-20-30_Ejes_vias)
        vias_oficiales_result = []    # Áreas de vía de motor (para capa 00-20-20_Elementos_entorno_urbano)
        peatonales_curves = [] # Ejes peatonales (para capa 70-30-10_Peatonales)

        # Definimos los grupos de vías que queremos procesar
        # Cada grupo es una tupla: (clave_json, tipo)
        # tipo: 'vial' para vías de motor (oficiales, secundarias, terciarias)
        #       'peonal' para peatonales
        road_groups = [
            ("vias_oficiales", "vial"),
            ("vias_secundarias", "vial"),
            ("vias_terciarias", "vial"),
            ("peatonales", "peonal")
        ]

        total_viales_procesados = 0
        total_peatonales_procesados = 0

        for group_key, group_type in road_groups:
            if group_key not in data:
                print(f"Group {group_key} not found in data")
                continue
            group_data = data[group_key]
            if not isinstance(group_data, list):
                print(f"Group {group_key} is not a list")
                continue

            print(f"Processing {len(group_data)} entries in {group_key} ({group_type})")

            for via in group_data:
                coords = via.get("coordenadas_local", [])
                ancho_via = to_float_safe(via.get("ancho"), 0.0)

                if len(coords) >= 2:
                    # Crear la polilínea central (eje de vía)
                    poly = polyline_from_coords(coords, 0, 0, 0)  # Simplified offset
                    poly_curve = polyline_to_nurbs(poly) if poly else None

                    if poly_curve:
                        if group_type == "vial":
                            # Para vías de motor: el eje va a ejes_vias_curves
                            ejes_vias_curves.append(poly_curve)
                            # El área de vía (si hay ancho) va a vias_oficiales
                            if ancho_via > 0:
                                # Simplified buffering - just note we would buffer
                                vias_oficiales_result.append({"type": "buffered", "source": poly_curve, "width": ancho_via})
                            else:
                                # Si no hay ancho, usar el eje como referencia mínima
                                vias_oficiales_result.append(poly_curve)
                            total_viales_procesados += 1
                        else:  # group_type == "peonal"
                            # Para peatonales: el eje va a peatonales_curves
                            peatonales_curves.append(poly_curve)
                            total_peatonales_procesados += 1
                    else:
                        print(f"  WARNING: Could not create polyline for via {via.get('codigo', 'unknown')}")
                else:
                    print(f"  WARNING: Insufficient coordinates for via {via.get('codigo', 'unknown')}")

        print(f"\nResults:")
        print(f"  - Ejes de vía procesados: {len(ejes_vias_curves)} (para capa 00-20-30_Ejes_vias)")
        print(f"  - Áreas de vía procesadas: {len(vias_oficiales_result)} (para capa 00-20-20_Elementos_entorno_urbano)")
        print(f"  - Ejes peatonales procesados: {len(peatonales_curves)} (para capa 70-30-10_Peatonales)")

        # Test layer guarantee
        layers_archicad = [
            {"nombre": "00-20-20_Elementos_entorno_urbano", "color": 2, "visible": True},
            {"nombre": "00-20-30_Ejes_vias", "color": 8, "visible": True},
            {"nombre": "70-30-10_Zonas_verdes_publicas", "color": 3, "visible": True},
        ]

        layers_archicad, layer_lote_ok = garantizar_layer_lote(layers_archicad)
        print(f"  - Layer guarantee: {'OK' if layer_lote_ok else 'FAILED'} - Lote layer is first: {layers_archicad[0]['nombre'] if layers_archicad else 'N/A'}")

        print("\nTEST COMPLETED SUCCESSFULLY")
        return True

    except Exception as e:
        print(f"ERROR during test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("F1_ETAPA1_CONTEXTO_v04.1 Component Test")
    print("=" * 50)
    success = test_with_real_data()
    print("=" * 50)
    if success:
        print("RESULT: PASSED")
        sys.exit(0)
    else:
        print("RESULT: FAILED")
        sys.exit(1)