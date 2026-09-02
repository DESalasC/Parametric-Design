"""
================================================================================
F1_ETAPA2_PATIO_v02.py — Patio desde el Vertice N
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

ALGORITMO (2026-08-12):
  El patio se origina en el VERTICE N (el vertice del lote simplificado
  mas alejado de las vias del frente, segun F1_ETAPA2_LADOS_v02).

  Se desarrolla sobre los lados simplificados clasificados "Lateral"
  que comparten el vertice N, con dimensiones que al multiplicarse
  entre si dan el area del patio exigido:

    lado_patio = max(3.0m, pisos * 0.25m)   [reglamentacion POT]
    area_patio = lado_patio^2

  El rectangulo del patio se proyecta hacia el interior del lote
  desde el vertice N, alineado a las direcciones de los dos lados
  laterales que lo comparten.

SUBVERSIONES INTERNAS (v02.x: iteraciones sin cambio de version general):
  v02.0 (2026-08-12) - Algoritmo original: patio cuadrado desde el
         Vertice N sobre los dos lados laterales que lo comparten.
  v02.1 (2026-08-23) - El patio de esquina se ancla en el Vertice N
         cuando los DOS lados que lo comparten son colindantes (Lateral
         o Posterior); antes solo "Lateral" dejaba el patio sin generar.
  v02.2 (2026-08-25) - Consume vertice_n_points de F1_ETAPA2_LADOS_v06.3
         (puntos mejorados del Vertice N por intersecciones reales con
         vias) y genera un patio por cada punto disponible.
Regla de versionado: la version general (v02 -> v03) SOLO cambia con
cambios mayores (contrato de entradas/salidas o algoritmo central); las
iteraciones internas se registran como subversiones v02.x en este
encabezado. Historial reconstruido desde git el 2026-09-01.

ENTRADAS:
  lot_vertices (Point3d[])     — 4 vertices desde Discontinuity
  sides_table_json (String)    — Clasificacion desde F1_ETAPA2_LADOS_v06
  altura_max_pot (Number)      — Altura maxima [m]

SALIDAS:
  patios_curves   (Curve[])   — Rectangulo(s) de patio desde vertice N
  patio_count     (int)       — Numero de patios (0 o 1)
  mensaje         (String)    — Diagnostico
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

PATIO_MINIMO_M = 3.0
ALTURA_ENTREPISO = 3.0


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def point_in_lot(pt, vertices):
    """Ray casting + deteccion de punto sobre el borde (tol 0.1m)."""
    n = len(vertices)
    if n < 3: return False
    px, py = pt.X, pt.Y
    # 1) Ray casting estandar
    count = 0
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            if (v2.Y - v1.Y) != 0:
                x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
                if px < x_int:
                    count += 1
    if (count % 2) == 1:
        return True
    # 2) Punto sobre el borde (distancia al segmento < 0.1m)
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        dx = v2.X - v1.X
        dy = v2.Y - v1.Y
        l2 = dx * dx + dy * dy
        if l2 < 1e-12:
            continue
        t = ((px - v1.X) * dx + (py - v1.Y) * dy) / l2
        t = max(0.0, min(1.0, t))
        cx = v1.X + t * dx
        cy = v1.Y + t * dy
        dist = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
        if dist < 0.1:
            return True
    return False


def centroide_pts(vertices):
    sx = sum(v.X for v in vertices)
    sy = sum(v.Y for v in vertices)
    n = len(vertices)
    return rg.Point3d(sx / n, sy / n, 0)


def normal_interior(p1, p2, centro):
    """Normal unitaria hacia el INTERIOR del lote para el borde (p1->p2)."""
    e = rg.Vector3d(p2.X - p1.X, p2.Y - p1.Y, 0)
    n1 = rg.Vector3d(-e.Y, e.X, 0)   # rotacion CCW
    n2 = rg.Vector3d(e.Y, -e.X, 0)   # rotacion CW
    mid = rg.Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, 0)
    to_c = rg.Vector3d(centro.X - mid.X, centro.Y - mid.Y, 0)
    if n1.X * to_c.X + n1.Y * to_c.Y > 0:
        n1.Unitize()
        return n1 if n1.Length > 0 else rg.Vector3d(1, 0, 0)
    else:
        n2.Unitize()
        return n2 if n2.Length > 0 else rg.Vector3d(1, 0, 0)


def build_patio_desde_vertice(corner_pt, borde_a_p1, borde_a_p2, borde_b_p1, borde_b_p2, size, lot_vertices):
    """
    Rectangulo de patio anclado en corner_pt (vertice N), proyectado hacia
    el interior del lote usando las NORMALES INTERIORES de los dos bordes
    laterales que comparten el vertice.
    """
    ctr = centroide_pts(lot_vertices)
    na = normal_interior(borde_a_p1, borde_a_p2, ctr)  # normal del borde A
    nb = normal_interior(borde_b_p1, borde_b_p2, ctr)  # normal del borde B

    p0 = rg.Point3d(corner_pt)
    p1 = rg.Point3d(p0.X + na.X * size, p0.Y + na.Y * size, p0.Z)
    p3 = rg.Point3d(p0.X + nb.X * size, p0.Y + nb.Y * size, p0.Z)
    p2 = rg.Point3d(p1.X + nb.X * size, p1.Y + nb.Y * size, p0.Z)

    # Validar interioridad: los puntos p1/p3 caen EXACTAMENTE sobre los
    # bordes del lote (el patio se alinea a ellos), y el ray casting los
    # clasifica como fuera. Se desplazan ligeramente hacia adentro (eps)
    # para la validacion.
    EPS = 0.05
    pts_check = [
        rg.Point3d(p1.X + na.X * EPS, p1.Y + na.Y * EPS, p1.Z),
        rg.Point3d(p2.X + (na.X + nb.X) * EPS, p2.Y + (na.Y + nb.Y) * EPS, p2.Z),
        rg.Point3d(p3.X + nb.X * EPS, p3.Y + nb.Y * EPS, p3.Z),
    ]
    inside = sum(1 for p in pts_check if point_in_lot(p, lot_vertices))
    if inside < 2:
        return None

    poly = rg.Polyline()
    poly.Add(p0); poly.Add(p1); poly.Add(p2); poly.Add(p3); poly.Add(p0)
    return rg.PolylineCurve(poly)


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
sides_raw = globals().get("sides_table_json", None)
altura_raw = globals().get("altura_max_pot", None)

lot_vertices = safe_list(lot_vertices_raw)

sides_data = None
if sides_raw is not None:
    try:
        if isinstance(sides_raw, list) and sides_raw:
            s = str(sides_raw[0])
        else:
            s = str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

try:
    altura_max = float(unwrap(altura_raw)) if altura_raw else 11.4
except:
    altura_max = 11.4

patios_curves = []
patio_count = 0

if sides_data is None or len(lot_vertices) < 4:
    mensaje = "PATIO v02 | ERROR: vertices={} sides={}".format(
        len(lot_vertices), "OK" if sides_data else "FALTA")
else:
    try:
        lados = sides_data.get("lados", [])
        vertice_n = sides_data.get("vertice_n", None)
        n = len(lot_vertices)

        if vertice_n is None:
            mensaje = "PATIO v02 | ERROR: sides_table_json sin vertice_n (usar F1_ETAPA2_LADOS_v06)"
        else:
            # NUEVO: Intentar usar los puntos mejorados de Vertice N si están disponibles
            vertice_n_points_data = sides_data.get("vertice_n_points")
            usar_puntos_mejorados = vertice_n_points_data is not None and len(vertice_n_points_data) > 0

            # Tamano del patio segun altura
            pisos = max(1, int(math.ceil(altura_max / ALTURA_ENTREPISO)))
            patio_lado = max(PATIO_MINIMO_M, pisos * 0.25)
            area_patio = patio_lado * patio_lado

            patios_curves_generados = []

            if usar_puntos_mejorados:
                # Usar los puntos mejorados de Vertice N
                for punto_coords in vertice_n_points_data:
                    vi = rg.Point3d(punto_coords[0], punto_coords[1], punto_coords[2] if len(punto_coords) > 2 else 0)

                    # Encontrar el índice del vértice más cercano para determinar los lados
                    min_dist = float('inf')
                    vertice_n_idx = 0
                    for i, v in enumerate(lot_vertices):
                        dist = v.DistanceTo(vi)
                        if dist < min_dist:
                            min_dist = dist
                            vertice_n_idx = i

                    # Verificar que los dos lados que comparten el vertice N son Laterales
                    if len(lados) >= n and n > 0:
                        lado1 = lados[vertice_n_idx]
                        lado2 = lados[(vertice_n_idx + n - 1) % n]
                    else:
                        lado1 = {}
                        lado2 = {}
                    cat1 = lado1.get("clasificacion", "Desconocido")
                    cat2 = lado2.get("clasificacion", "Desconocido")

                    # v02.1 (2026-08-23): el patio de esquina se ancla en la
                    # esquina interior (vertice N) cuando los DOS lados que la
                    # comparten son COLINDANTES (Lateral o Posterior). Antes solo
                    # "Lateral", por lo que un lado "Posterior" o un vecino cuyo
                    # vertice no coincide exactamente dejaba el patio sin generar.
                    if cat1 in ("Lateral", "Posterior") and cat2 in ("Lateral", "Posterior"):
                        # Borde A: (V_n -> V_next)
                        va1 = vi
                        va2 = lot_vertices[(vertice_n_idx + 1) % n]
                        # Borde B: (V_prev -> V_n)
                        vb1 = lot_vertices[(vertice_n_idx + n - 1) % n]
                        vb2 = vi

                        patio_crv = build_patio_desde_vertice(
                            vi, va1, va2, vb1, vb2, patio_lado, lot_vertices)
                        if patio_crv:
                            patios_curves_generados.append(patio_crv)
            else:
                # FALLBACK: Usar el método tradicional de vertice_n índice
                # Tamano del patio segun altura
                pisos = max(1, int(math.ceil(altura_max / ALTURA_ENTREPISO)))
                patio_lado = max(PATIO_MINIMO_M, pisos * 0.25)
                area_patio = patio_lado * patio_lado

                # Verificar que los dos lados que comparten el vertice N son Laterales
                if len(lados) >= n and n > 0:
                    lado1 = lados[vertice_n]
                    lado2 = lados[(vertice_n + n - 1) % n]
                else:
                    lado1 = {}
                    lado2 = {}
                cat1 = lado1.get("clasificacion", "Desconocido")
                cat2 = lado2.get("clasificacion", "Desconocido")

                # v02.1 (2026-08-23): el patio de esquina se ancla en la
                # esquina interior (vertice N) cuando los DOS lados que la
                # comparten son COLINDANTES (Lateral o Posterior). Antes solo
                # "Lateral", por lo que un lado "Posterior" o un vecino cuyo
                # vertice no coincide exactamente dejaba el patio sin generar.
                if cat1 in ("Lateral", "Posterior") and cat2 in ("Lateral", "Posterior"):
                    vi = lot_vertices[vertice_n]
                    # Borde A: (V_n -> V_next)
                    va1 = vi
                    va2 = lot_vertices[(vertice_n + 1) % n]
                    # Borde B: (V_prev -> V_n)
                    vb1 = lot_vertices[(vertice_n + n - 1) % n]
                    vb2 = vi

                    patio_crv = build_patio_desde_vertice(
                        vi, va1, va2, vb1, vb2, patio_lado, lot_vertices)
                    if patio_crv:
                        patios_curves_generados.append(patio_crv)

            patio_count = len(patios_curves_generados)
            patios_curves = patios_curves_generados
            cats = [l.get("clasificacion", "?") for l in lados]

            if usar_puntos_mejorados:
                mensaje = "PATIO v02.2 | V_N_Puntos={} | Lados: {} | Patio={:.2f}x{:.2f}m ({} m2) | Generados: {}".format(
                    len(vertice_n_points_data), ", ".join(cats), patio_lado, patio_lado,
                    area_patio, patio_count)
            else:
                mensaje = "PATIO v02.1 | V_N={} | Lados: {} | Patio={:.2f}x{:.2f}m ({} m2) | Generados: {}".format(
                    vertice_n, ", ".join(cats), patio_lado, patio_lado,
                    area_patio, patio_count)

    except Exception as e:
        mensaje = "PATIO v02 | ERROR: {}".format(str(e))
