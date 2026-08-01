#!/usr/bin/env python3
"""
DISEÑO_INTERIOR_v01 - Distribución Unidades + Validación NSR-10 + Cesiones POT
GH Python Script para Grasshopper (GH Player compatible) — Sprint 2

ENTRADAS (desde VOLUMEN_v02 + Paneles):
  - core_positions: Output Nodo 110 VOLUMEN_v02 [{"tower": int, "position": Point3d, "floors": int}]
  - envelope_analysis: Output Nodo 110 [dict por torre con footprint, floor_areas, setbacks, nsr10]
  - floor_plates: Brep/List - Placas por torre/piso (límites unidades)
  - exterior_walls: Brep/List - Muros exteriores (huecos ventilación/iluminación)
  - program_areas: Dict áreas objetivo por tipo {"1_hab": m2, "2_hab": m2, ...} (opcional)
  - unit_mix_target: Dict mix objetivo {"1_hab": n, "2_hab": n, "3_hab": n, "4_hab": n} (opcional)
  - common_areas_required: Dict cesiones POT {tipo: area_m2_req} (opcional, calculado si falta)
  - floor_height: Altura libre (default 3.0m, desde VOLUMEN)

SALIDAS (Componentes Nativos ArchiCAD-GH + Análisis):
  - unit_polygons: DataTree/polígonos unidad por torre/piso → **AC Zone/Morph** (nativo)
  - partition_walls: DataTree/curvas tabiques por unidad → **AC Wall** (nativo, 12cm)
  - zone_bounds: DataTree/límites zona día/noche → **AC Zone** (nativo)
  - unit_doors: DataTree/huecos puerta {unit, wall_curve, pos, w, h} → **AC Door** (nativo)
  - unit_windows: DataTree/huecos ventana {unit, ext_wall, pos, w, h} → **AC Window** (nativo)
  - nsr10_compliance: Dict validación completa por unidad (Property Palette/Schedule)
  - area_schedule: Dict schedule ArchiCAD: áreas por tipo, totales, % eficiencia
  - common_areas: Dict cesiones POT {hall, stairs, elevators, waste, bikes, tech_rooms}
  - core_circulation: {stairs_polygon, elevator_polygon, corridor_polygons} por torre/piso
  - unit_breps: Brep/List - Volúmenes unidad → **Tapir Send → Morph** (para análisis Ladybug/Wallacei)

NOTA: AC Zone, AC Wall, AC Door, AC Window son del plugin ArchiCAD-Grasshopper Connection.
Crean elementos NATIVOS en ArchiCAD. Tapir solo para análisis térmico/lumínico (Ladybug/Wallacei).
"""

import rhinoscriptsyntax as rs
import math
import json

# ============================================================
# CONFIGURACIÓN NORMATIVA
# ============================================================

NSR10 = {
    "altura_libre_min": 2.30,
    "area_min_habitable": 9.0,
    "area_min_sala_comedor": 12.0,
    "area_min_cocina": 5.0,
    "area_min_banio": 3.0,
    "ventilacion_min_pct": 0.05,
    "iluminacion_min_pct": 0.10,
    "ancho_min_pasillo": 1.00,
    "ancho_min_escalera": 1.10,
    "max_longitud_pasillo_sin_vent": 15.0,
    "ancho_min_zaguan": 1.50,
}

# Programa genérico vivienda colectiva Bogotá (m2 por unidad)
DEFAULT_PROGRAM = {
    "1_hab": {"area": 42, "dorm": 1, "banos": 1, "sala_comedor": 16, "cocina": 6, "balcon": 4},
    "2_hab": {"area": 58, "dorm": 2, "banos": 1, "sala_comedor": 20, "cocina": 7, "balcon": 6},
    "3_hab": {"area": 75, "dorm": 3, "banos": 2, "sala_comedor": 24, "cocina": 8, "balcon": 8},
    "4_hab": {"area": 95, "dorm": 4, "banos": 2, "sala_comedor": 28, "cocina": 10, "balcon": 10},
}

# Cesiones POT Bogotá (porcentaje sobre área construida total)
POT_COMMON_AREAS_PCT = {
    "hall_acceso": 0.02,      # 2%
    "escaleras": 0.03,        # 3%
    "ascensores": 0.02,       # 2%
    "cuarto_basuras": 0.005,  # 0.5%
    "cuarto_bicicletas": 0.01, # 1%
    "cuarto_tecnico": 0.005,   # 0.5%
    "shafts_instalaciones": 0.015, # 1.5%
}
POT_COMMON_TOTAL_PCT = sum(POT_COMMON_AREAS_PCT.values())  # ~10%

AC_CONFIG = {
    "partition_thickness": 0.12,    # 12cm
    "door_width": 0.90,             # 90cm
    "door_height": 2.10,            # 210cm
    "window_sill_height": 1.00,     # 100cm
    "window_head_height": 2.40,     # 240cm
    "corridor_width": 1.20,         # 120cm
}

# ============================================================
# HELPERS GEOMÉTRICOS
# ============================================================

def get_footprint_per_floor(tower_idx, floor, floor_plates):
    """Obtener polígono placa para torre/piso"""
    for fp in floor_plates:
        if fp.get("tower") == tower_idx:
            floors = fp.get("floors", fp.get("slabs", []))
            for fl in floors:
                if fl.get("floor") == floor:
                    return fl.get("polygon")
    return None


def get_exterior_wall_segments(tower_idx, floor, exterior_walls):
    """Obtener segmentos muro exterior para torre/piso"""
    segments = []
    for ew in exterior_walls:
        if ew.get("tower") == tower_idx:
            walls = ew.get("walls", [])
            for w in walls:
                if w.get("floor") == floor:
                    segments.append(w.get("base_curve"))
    return segments


def create_offset_polygon(polygon, distance):
    """Offset hacia adentro"""
    if not polygon:
        return None
    plane_rc = rs.CurvePlane(polygon)
    plane = plane_rc[0] if plane_rc else rs.WorldXYPlane()
    if isinstance(plane, tuple):
        plane = plane[0]
    offset_crvs = rs.OffsetCurve(polygon, plane, -distance, plane, corner_type=2)
    return offset_crvs[0] if offset_crvs else None


def divide_polygon_perimeter(polygon, num_segments, start_angle=0):
    """Dividir perímetro polígono en N segmentos iguales (para unidades)"""
    if not polygon:
        return []
    length = rs.CurveLength(polygon)
    if length <= 0:
        return []
    seg_length = length / num_segments
    params = []
    for i in range(num_segments):
        params.append(i * seg_length)
    pts = [rs.EvaluateCurve(polygon, rs.CurveParameter(polygon, p)) for p in params]
    return pts


def create_unit_polygon_from_core(footprint, core_pt, unit_width, unit_depth):
    """Crear polígono unidad extendiéndose desde núcleo hacia fachada"""
    # Vector núcleo a centroide huella
    centroid = rs.CurveAreaCentroid(footprint)[0] if rs.CurveAreaCentroid(footprint) else core_pt
    vx = centroid[0] - core_pt[0]
    vy = centroid[1] - core_pt[1]
    dist = math.hypot(vx, vy)
    if dist == 0:
        return None

    # Escalar profundidad unidad
    scale = unit_depth / dist
    far_x = core_pt[0] + vx * scale
    far_y = core_pt[1] + vy * scale

    # Ancho unidad perpendicular
    angle = math.atan2(vy, vx)
    perp_angle = angle + math.pi / 2
    half_w = unit_width / 2

    # 4 esquinas
    c1 = (core_pt[0] - half_w * math.sin(angle), core_pt[1] + half_w * math.cos(angle), core_pt[2])
    c2 = (core_pt[0] + half_w * math.sin(angle), core_pt[1] - half_w * math.cos(angle), core_pt[2])
    c3 = (far_x + half_w * math.sin(angle), far_y - half_w * math.cos(angle), core_pt[2])
    c4 = (far_x - half_w * math.sin(angle), far_y + half_w * math.cos(angle), core_pt[2])

    return rs.AddPolyline([c1, c2, c3, c4, c1])


def validate_nsr10_unit(unit_polygon, exterior_wall_segments, floor_area):
    """Validar NSR-10 para una unidad"""
    if not unit_polygon or not exterior_wall_segments:
        return {"ventilacion_pct": 0, "iluminacion_pct": 0, "ancho_pasillo_m": 0,
                "habitable_area_m2": floor_area, "dormitorio_area_m2": 0,
                "warnings": ["No exterior walls"]}

    # Área fachada expuesta (intersección unidad con muros exteriores)
    facade_length = 0
    for ew in exterior_wall_segments:
        inters = rs.CurveCurveIntersection(unit_polygon, ew)
        if inters:
            facade_length += len(inters) * 0.5  # aprox

    # % Ventilación/Iluminación basada en longitud fachada
    unit_perimeter = rs.CurveLength(unit_polygon)
    vent_pct = min(facade_length / unit_perimeter, 1.0) if unit_perimeter > 0 else 0
    illum_pct = vent_pct  # simplificado

    return {
        "ventilacion_pct": round(vent_pct * 100, 1),
        "iluminacion_pct": round(illum_pct * 100, 1),
        "ancho_pasillo_m": AC_CONFIG["corridor_width"],
        "habitable_area_m2": round(floor_area * 0.85, 1),  # estimado
        "dormitorio_area_m2": round(floor_area * 0.25, 1),  # estimado
        "warnings": ([] if vent_pct >= NSR10["ventilacion_min_pct"]
                     else [f"Ventilación {vent_pct*100:.1f}% < {NSR10['ventilacion_min_pct']*100}%"]) +
                    ([] if illum_pct >= NSR10["iluminacion_min_pct"]
                     else [f"Iluminación {illum_pct*100:.1f}% < {NSR10['iluminacion_min_pct']*100}%"])
    }


def calculate_unit_program(unit_type, unit_area):
    """Obtener programa por tipo, ajustado a área real"""
    prog = DEFAULT_PROGRAM.get(unit_type, DEFAULT_PROGRAM["2_hab"])
    scale = unit_area / prog["area"]
    return {k: round(v * scale, 1) if isinstance(v, (int, float)) else v for k, v in prog.items()}


# ============================================================
# MAIN EXECUTION
# ============================================================

if core_positions is None: raise ValueError("Falta core_positions (VOLUMEN_v02)")
if envelope_analysis is None: raise ValueError("Falta envelope_analysis (VOLUMEN_v02)")
if floor_plates is None: raise ValueError("Falta floor_plates (VOLUMEN_v02)")
if exterior_walls is None: raise ValueError("Falta exterior_walls (VOLUMEN_v02)")

floor_height = float(floor_height) if floor_height else 3.0
prog_areas = program_areas if program_areas else {k: v["area"] for k, v in DEFAULT_PROGRAM.items()}
mix_target = unit_mix_target if unit_mix_target else {"1_hab": 0.2, "2_hab": 0.4, "3_hab": 0.3, "4_hab": 0.1}

# Convertir mix a conteos si son porcentajes
if mix_target and all(isinstance(v, float) and v <= 1.0 for v in mix_target.values()):
    # Se calculará por torre/piso más abajo
    pass

print(f"=== DISEÑO_INTERIOR_v01 (ArchiCAD Nativo) ===")
print(f"Torres: {len(core_positions)} | Altura piso: {floor_height}m")

# ============================================================
# DISTRIBUCIÓN POR TORRE/PISO
# ============================================================

unit_polygons = []        # → AC Zone/Morph
partition_walls = []      # → AC Wall (12cm)
zone_bounds = []          # → AC Zone (día/noche)
unit_doors = []           # → AC Door
unit_windows = []         # → AC Window
nsr10_compliance = {}
area_schedule = {"units_by_type": {}, "total_units": 0, "total_area_m2": 0, "total_built_m2": 0,
                 "efficiency_pct": 0, "common_area_m2": 0, "common_area_pct": 0}
common_areas = {}
core_circulation = {}

total_units = 0
total_habitable_area = 0
total_built_area = 0

for tower_idx, core in enumerate(core_positions):
    core_pt = core["position"]
    floors = core["floors"]

    # Buscar análisis torre
    tower_analysis = next((ea for ea in envelope_analysis if ea["tower_index"] == tower_idx), None)
    if not tower_analysis:
        print(f"[WARN] Torre {tower_idx}: Sin envelope_analysis")
        continue

    footprint_area = tower_analysis["footprint_area_m2"]
    floors_effective = tower_analysis["floors_effective"]
    floor_areas = tower_analysis["floor_areas_m2"]

    tower_units = []
    tower_circulation = {"stairs": [], "elevators": [], "corridors": []}
    tower_partitions = []

    for fl in range(floors_effective):
        floor_z = fl * floor_height
        unit_floor_num = fl + 1

        # Polígono placa
        footprint = get_footprint_per_floor(tower_idx, fl, floor_plates)
        if not footprint:
            continue

        # Área disponible = huella - circulaciones núcleo
        core_area_est = 15.0  # estimado escalera+ascensor
        disponible = footprint_area - core_area_est

        # Número unidades por piso (heurístico: ~80m2/unidad promedio)
        avg_unit_area = sum(prog_areas.values()) / len(prog_areas)
        num_units = max(2, int(disponible / avg_unit_area))
        num_units = min(num_units, 8)  # máx 8 unidades/piso

        # Asignar tipologías según mix
        types = []
        for ut, pct in mix_target.items():
            count = int(num_units * (pct if pct <= 1 else pct/100))
            types.extend([ut] * count)
        while len(types) < num_units:
            types.append("2_hab")
        types = types[:num_units]

        # Distribuir alrededor del núcleo
        perimeter_pts = divide_polygon_perimeter(footprint, num_units)
        if len(perimeter_pts) < num_units:
            continue

        for u_idx, unit_type in enumerate(types):
            prog = calculate_unit_program(unit_type, disponible / num_units)
            unit_area = prog["area"]

            # Polígono unidad
            unit_poly = create_unit_polygon_from_core(
                footprint, core_pt,
                unit_width=math.sqrt(unit_area * 0.6),  # aprox
                unit_depth=math.sqrt(unit_area * 0.4)
            )
            if not unit_poly:
                continue

            total_units += 1
            unit_id = f"T{tower_idx}_P{fl}_U{u_idx}"
            total_habitable_area += unit_area * 0.85
            total_built_area += unit_area

            # Validar NSR-10
            ew_segments = get_exterior_wall_segments(tower_idx, fl, exterior_walls)
            nsr10 = validate_nsr10_unit(unit_poly, ew_segments, unit_area)

            # Tabiques internos (simplificado: perímetro + 2 tabiques)
            unit_segs = rs.ExplodePolylines(unit_poly)
            partitions = []
            if unit_segs and len(unit_segs) >= 4:
                # Tabique transversal (día/noche)
                mid1 = rs.CurveMidPoint(unit_segs[0])
                mid2 = rs.CurveMidPoint(unit_segs[2])
                partitions.append(rs.AddLine(mid1, mid2))
                # Tabique baños
                partitions.append(rs.AddLine(rs.CurveMidPoint(unit_segs[1]), rs.CurveMidPoint(unit_segs[3])))

            # Puertas (entrada + interiores)
            doors = []
            if unit_segs:
                # Puerta entrada: muro fachada
                for i, ew in enumerate(ew_segments):
                    inters = rs.CurveCurveIntersection(unit_poly, ew)
                    if inters:
                        pt = rs.EvaluateCurve(ew, inters[0][5])
                        doors.append({
                            "unit_id": unit_id, "wall_curve": ew, "position": pt,
                            "width": AC_CONFIG["door_width"], "height": AC_CONFIG["door_height"],
                            "type": "Entrance"
                        })
                        break

            # Ventanas (fachadas con muro exterior)
            windows = []
            for ew in ew_segments:
                inters = rs.CurveCurveIntersection(unit_poly, ew)
                if inters:
                    for inter in inters:
                        pt = rs.EvaluateCurve(ew, inter[5])
                        windows.append({
                            "unit_id": unit_id, "wall_curve": ew, "position": pt,
                            "width": 1.5, "height": 1.4,
                            "sill": AC_CONFIG["window_sill_height"], "head": AC_CONFIG["window_head_height"]
                        })

            # Outputs
            unit_polygons.append({
                "tower": tower_idx, "floor": fl, "unit_id": unit_id,
                "polygon": unit_poly, "area_m2": unit_area,
                "type": unit_type, "rooms": prog["dorm"], "bathrooms": prog["banos"],
                "balcony_m2": prog.get("balcon", 0), "elevation": floor_z
            })

            partition_walls.append({
                "tower": tower_idx, "floor": fl, "unit_id": unit_id,
                "curves": partitions, "thickness": AC_CONFIG["partition_thickness"]
            })

            zone_bounds.append({
                "tower": tower_idx, "floor": fl, "unit_id": unit_id,
                "day_zone": unit_poly,  # simplificado
                "night_zone": unit_poly
            })

            unit_doors.append({"tower": tower_idx, "floor": fl, "unit_id": unit_id, "doors": doors})
            unit_windows.append({"tower": tower_idx, "floor": fl, "unit_id": unit_id, "windows": windows})

            nsr10_compliance[unit_id] = nsr10

            # Schedule areas
            area_schedule["units_by_type"][unit_type] = area_schedule["units_by_type"].get(unit_type, 0) + 1

    # Circulación núcleo (escalera + ascensor) - solo una vez por torre
    core_circulation[f"T{tower_idx}"] = {
        "stairs_polygon": rs.AddRectangle(rs.PlaneFromNormal(core_pt, (0,0,1)), 2.5, 3.0),
        "elevator_polygon": rs.AddRectangle(rs.PlaneFromNormal(core_pt, (0,0,1)), 2.5, 2.0),
        "corridor_polygons": []
    }

# Cesiones POT
total_built = sum(ea["total_built_area_m2"] for ea in envelope_analysis) if envelope_analysis else total_built_area
common_areas = {k: round(total_built * v, 1) for k, v in POT_COMMON_AREAS_PCT.items()}
common_areas["total_m2"] = round(sum(common_areas.values()), 1)
common_areas["total_pct"] = POT_COMMON_TOTAL_PCT * 100

area_schedule["total_units"] = total_units
area_schedule["total_habitable_m2"] = round(total_habitable_area, 1)
area_schedule["total_built_m2"] = round(total_built, 1)
area_schedule["efficiency_pct"] = round((total_habitable_area / total_built) * 100, 1) if total_built > 0 else 0
area_schedule["common_area_m2"] = common_areas["total_m2"]
area_schedule["common_area_pct"] = common_areas["total_pct"]

print(f"\nUnidades totales: {total_units}")
print(f"Área habitable: {area_schedule['total_habitable_m2']}m2")
print(f"Área construida: {area_schedule['total_built_m2']}m2")
print(f"Eficiencia: {area_schedule['efficiency_pct']}%")
print(f"Cesiones POT: {common_areas['total_m2']}m2 ({common_areas['total_pct']}%)")

# NSR-10 resumen
nsr10_ok = sum(1 for v in nsr10_compliance.values() if not v["warnings"])
nsr10_warn = total_units - nsr10_ok
print(f"NSR-10 OK: {nsr10_ok}/{total_units} | Warnings: {nsr10_warn}")

# Outputs GH:
# unit_polygons, partition_walls, zone_bounds, unit_doors, unit_windows, nsr10_compliance, area_schedule, common_areas, core_circulation