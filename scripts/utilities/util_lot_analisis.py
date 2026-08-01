import Rhino.Geometry as rg
import math

# ============================================================
# LOT_ANALISIS_v02 - Worker puro por lado + GH Wrapper
# v02: Separado worker puro (analyze_side) + GH wrapper (solve)
#      Reutilizable por CONFIGURAR_LADOS_v02 y otros flujos
# ============================================================

def flatten_curves(input_curves):
    """Aplanar lista anidada de curvas a lista simple"""
    flat = []
    if input_curves is None:
        return flat
    if hasattr(input_curves, "__iter__") and not isinstance(input_curves, (rg.Curve, rg.Point3d, rg.Vector3d)):
        for item in input_curves:
            flat.extend(flatten_curves(item))
    else:
        flat.append(input_curves)
    return flat


def analyze_side(side_curve, side_vector, side_midpoint, north_vector, street_curves, threshold=0.5):
    """
    Analiza un lado individual del lote.

    Args:
        side_curve: rg.Curve - segmento del lote
        side_vector: rg.Vector3d - vector dirección del lado (unitario)
        side_midpoint: rg.Point3d - punto medio del lado
        north_vector: rg.Vector3d - vector Norte geográfico (unitario)
        street_curves: list[rg.Curve] - todas las curvas de calle (ejes/bordes)
        threshold: float - umbral distancia para considerar "calle" (default 0.5m)

    Returns:
        dict: {
            "dist_to_street": float,
            "ang_calle": float (grados),
            "ang_norte": float (grados),
            "es_calle": bool,
            "closest_street_vector": rg.Vector3d or None,
            "closest_street_curve": rg.Curve or None,
        }
    """
    # Normalizar Norte
    nv = rg.Vector3d(north_vector.X, north_vector.Y, north_vector.Z)
    if nv.IsTiny():
        nv = rg.Vector3d(0, 1, 0)
    nv.Unitize()

    # Vector lado ya viene unitario, pero asegurar
    ld = rg.Vector3d(side_vector.X, side_vector.Y, side_vector.Z)
    if ld.Length > 0.001:
        ld.Unitize()

    # Buscar calle más cercana
    min_dist = float('inf')
    street_dir = rg.Vector3d(0, 0, 0)
    closest_street = None

    all_streets = flatten_curves(street_curves)

    for s_crv in all_streets:
        if not isinstance(s_crv, rg.Curve):
            continue
        rc, t = s_crv.ClosestPoint(side_midpoint)
        if rc:
            cp = s_crv.PointAt(t)
            d = side_midpoint.DistanceTo(cp)
            if d < min_dist:
                min_dist = d
                street_dir = s_crv.TangentAt(t)
                closest_street = s_crv

    if street_dir.Length > 0.001:
        street_dir.Unitize()

    ang_calle = rg.Vector3d.VectorAngle(ld, street_dir) if street_dir.Length > 0.001 else 0.0
    ang_norte = rg.Vector3d.VectorAngle(ld, nv)

    return {
        "dist_to_street": round(float(min_dist), 3),
        "ang_calle": round(math.degrees(ang_calle), 1),
        "ang_norte": round(math.degrees(ang_norte), 1),
        "es_calle": min_dist < threshold,
        "closest_street_vector": street_dir if street_dir.Length > 0.001 else None,
        "closest_street_curve": closest_street,
    }


# ============================================================
# GH COMPONENT WRAPPER (para uso directo en canvas GH)
# SOLO se ejecuta cuando el archivo se usa COMO componente GhPython directamente
# No se ejecuta al importar como módulo (from Lot_analisis_v02 import ...)
# ============================================================

if __name__ == "__main__":
    # Este bloque solo corre si el archivo se ejecuta directamente en GhPython

    def solve():
        """Wrapper para componente GhPython estándar (item access)"""
        # Variables disponibles como globals en GhPython (inputs del componente)
        if 'side_curves' not in globals() or side_curves is None:
            return None

        # Convertir inputs GH items a Rhino.Geometry
        nv = rg.Vector3d(north_vector.X, north_vector.Y, north_vector.Z) if 'north_vector' in globals() and north_vector else rg.Vector3d(0,1,0)
        if nv.IsTiny(): nv = rg.Vector3d(0,1,0)
        nv.Unitize()

        # Vector lado
        if 'side_vectors' in globals() and side_vectors:
            ld = rg.Vector3d(side_vectors.X, side_vectors.Y, side_vectors.Z)
        else:
            ld = side_curves.PointAtEnd - side_curves.PointAtStart
        if ld.Length > 0.001: ld.Unitize()

        # Punto medio
        mid_pt = side_midpoints if 'side_midpoints' in globals() and side_midpoints else side_curves.PointAt(0.5)

        # Llamar worker puro
        result = analyze_side(
            side_curve=side_curves,
            side_vector=ld,
            side_midpoint=mid_pt,
            north_vector=nv,
            street_curves=street_curves if 'street_curves' in globals() else [],
            threshold=street_threshold if 'street_threshold' in globals() and street_threshold is not None else 0.5
        )

        # Agregar ID si viene
        result["id"] = int(side_indices) if 'side_indices' in globals() and side_indices is not None else 0

        return result


    # ============================================================
    # GH OUTPUT
    # ============================================================
    lado_clasificado = solve()