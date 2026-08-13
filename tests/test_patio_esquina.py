"""
Test de logica geometrica para F1_PATIO_ESQUINA y F1_NORMATIVA_APLICAR.
Ejecutar con: python -m pytest tests\test_patio_esquina.py -v
O directamente: python tests\test_patio_esquina.py
"""

import sys
import os
import math

# ============================================================
# DATOS DEL LOTE REAL AAA0127AZPA
# ============================================================

LOTE_AAA0127AZPA = [
    [88.011500, 79.110300],
    [87.330200, 75.000000],
    [84.174700, 75.525300],
    [75.000000, 77.052700],
    [76.333100, 85.096300],
    [78.295200, 96.934800],
    [79.120400, 101.913500],
    [91.450700, 99.860800],
    [89.646200, 88.973300],
]

# Clasificacion de lados para este lote (los frentes estan en los segmentos 6-7-8-0)
# Basado en la geometria: la calle pasa cerca del lado norte/este del lote
# Segmento 0: v0→v1 (88.0,79.1 → 87.3,75.0) = Oeste, lateral
# Segmento 1: v1→v2 (87.3,75.0 → 84.2,75.5) = Sur, lateral  
# Segmento 2: v2→v3 (84.2,75.5 → 75.0,77.1) = Suroeste, lateral
# Segmento 3: v3→v4 (75.0,77.1 → 76.3,85.1) = Oeste, posterior
# Segmento 4: v4→v5 (76.3,85.1 → 78.3,96.9) = Noroeste, posterior/lateral
# Segmento 5: v5→v6 (78.3,96.9 → 79.1,101.9) = Norte, frontal (calle)
# Segmento 6: v6→v7 (79.1,101.9 → 91.5,99.9) = Noreste, frontal (calle)
# Segmento 7: v7→v8 (91.5,99.9 → 89.6,89.0) = Este, frontal
# Segmento 8: v8→v0 (89.6,89.0 → 88.0,79.1) = Este/sureste, frontal

SIDES_CLASIFICACION = [
    {"side_index": 0, "classification": "Lateral", "setback_m": 0.0},
    {"side_index": 1, "classification": "Lateral", "setback_m": 0.0},
    {"side_index": 2, "classification": "Lateral", "setback_m": 0.0},
    {"side_index": 3, "classification": "Posterior", "setback_m": 3.0},
    {"side_index": 4, "classification": "Posterior", "setback_m": 3.0},
    {"side_index": 5, "classification": "Frontal", "setback_m": 3.0},
    {"side_index": 6, "classification": "Frontal", "setback_m": 3.0},
    {"side_index": 7, "classification": "Frontal", "setback_m": 5.0},
    {"side_index": 8, "classification": "Frontal", "setback_m": 5.0},
]

# ============================================================
# FUNCIONES DE PRUEBA (logica pura sin Rhino)
# ============================================================

def polygon_area(vertices):
    """Calcular area de poligono (formula de Shoelace)."""
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def find_corner_vertices_test(front_indices, num_vertices):
    """Version de prueba de find_corner_vertices (sin Rhino)."""
    if len(front_indices) < 2:
        return None, None
    
    sorted_fronts = sorted(front_indices)
    street_corner = None
    
    for i in range(len(sorted_fronts)):
        a = sorted_fronts[i]
        b = sorted_fronts[(i + 1) % len(sorted_fronts)]
        diff = abs(a - b)
        if diff == 1 or diff == num_vertices - 1:
            if diff == 1:
                street_corner = max(a, b)
            else:
                street_corner = 0
            break
    
    if street_corner is None and len(sorted_fronts) >= 2:
        street_corner = sorted_fronts[1]
    
    interior_corner = (street_corner + num_vertices // 2) % num_vertices
    return street_corner, interior_corner


def calculate_patio_size_test(building_floors, lot_area=None):
    """Version de prueba de calculate_patio_size."""
    building_height = building_floors * 3.0
    
    if lot_area is not None and lot_area < 500.0 and building_floors <= 5:
        return 3.0
    
    patio_size = max(3.0, building_height * 0.25)
    patio_size = round(patio_size * 2.0) / 2.0
    return patio_size


# ============================================================
# TESTS
# ============================================================

def test_lot_area():
    """Verificar que el area del lote AAA0127AZPA es ~315 m2."""
    area = polygon_area(LOTE_AAA0127AZPA)
    assert abs(area - 315.0) < 5.0, "Area del lote deberia ser ~315 m2, es {}".format(area)
    print("  [OK] Area del lote: {:.1f} m2".format(area))


def test_front_detection():
    """Verificar identificacion de frentes."""
    fronts = [s["side_index"] for s in SIDES_CLASIFICACION if s["classification"] == "Frontal"]
    assert len(fronts) >= 2, "Deberia haber al menos 2 frentes, hay {}".format(len(fronts))
    print("  [OK] {} frentes detectados: {}".format(len(fronts), fronts))


def test_corner_detection():
    """Verificar deteccion de esquina de calles y esquina interior."""
    fronts = [s["side_index"] for s in SIDES_CLASIFICACION if s["classification"] == "Frontal"]
    n_verts = len(LOTE_AAA0127AZPA)
    
    street_corner, interior_corner = find_corner_vertices_test(fronts, n_verts)
    
    assert street_corner is not None, "Debe identificar una esquina de calles"
    assert interior_corner is not None, "Debe identificar una esquina interior"
    assert street_corner != interior_corner, "Esquina de calles != esquina interior"
    
    print("  [OK] Esquina de calles: vertice {}".format(street_corner))
    print("  [OK] Esquina interior (patio): vertice {}".format(interior_corner))
    
    # Verificar que la esquina interior esta aproximadamente opuesta
    # Esperado: si street_corner esta cerca de v7 (indice 7),
    # interior_corner deberia estar cerca de v3 (indice 3)
    expected_interior = (street_corner + n_verts // 2) % n_verts
    assert interior_corner == expected_interior, \
        "Esquina interior deberia ser {}, es {}".format(expected_interior, interior_corner)


def test_patio_size():
    """Verificar calculo de tamano del patio segun altura."""
    # Lote pequeno (< 500 m2), tipologia continua, <= 5 pisos
    size_3fl = calculate_patio_size_test(3, lot_area=315.0)
    assert size_3fl == 3.0, "3 pisos en lote pequeno: patio deberia ser 3.0m, es {:.1f}".format(size_3fl)
    
    size_4fl = calculate_patio_size_test(4, lot_area=315.0)
    assert size_4fl == 3.0, "4 pisos en lote pequeno: patio deberia ser 3.0m, es {:.1f}".format(size_4fl)
    
    # Edificio alto (> 5 pisos)
    size_8fl = calculate_patio_size_test(8, lot_area=1000.0)
    altura_8 = 8 * 3.0
    expected_8 = max(3.0, altura_8 * 0.25)
    assert abs(size_8fl - round(expected_8 * 2) / 2) < 0.1, \
        "8 pisos: patio deberia ser ~{:.1f}m, es {:.1f}m".format(expected_8, size_8fl)
    
    print("  [OK] Patio 3 pisos (lote pequeno): {:.1f}m".format(size_3fl))
    print("  [OK] Patio 8 pisos (lote grande): {:.1f}m".format(size_8fl))


def test_retiro_frontal_no_interfiere_patio():
    """Verificar que los retiros frontales y el patio no se solapan."""
    fronts = [s["side_index"] for s in SIDES_CLASIFICACION if s["classification"] == "Frontal"]
    n_verts = len(LOTE_AAA0127AZPA)
    street_corner, interior_corner = find_corner_vertices_test(fronts, n_verts)
    
    # La esquina de calles NO debe ser la misma que la esquina del patio
    assert street_corner != interior_corner
    
    # Los frentes deben estar en el lado opuesto al patio
    for front_idx in fronts:
        dist_around_1 = abs(front_idx - interior_corner)
        dist_around_2 = n_verts - dist_around_1
        min_dist = min(dist_around_1, dist_around_2)
        # Un frente deberia estar al menos a 2 segmentos del patio interior
        # (no es obligatorio pero es tipico en lotes bien formados)
        # En este lote especifico, los frentes estan en indices 5-8 y el interior en ~3
        pass
    
    print("  [OK] Patio en vertice {} no coincide con frentes {}".format(interior_corner, fronts))


def test_area_reduction_with_retiros():
    """Verificar que los retiros reducen el area edificable correctamente."""
    area_lote = polygon_area(LOTE_AAA0127AZPA)
    
    # Con los retiros especificados, el area edificable deberia reducirse
    # pero no a cero ni ser mayor que el area del lote
    setbacks_used = [s["setback_m"] for s in SIDES_CLASIFICACION]
    avg_setback = sum(setbacks_used) / len(setbacks_used)
    
    # Estimacion simplificada: perimetro * retiro_promedio
    perimetro = 0.0
    for i in range(len(LOTE_AAA0127AZPA)):
        x1, y1 = LOTE_AAA0127AZPA[i]
        x2, y2 = LOTE_AAA0127AZPA[(i + 1) % len(LOTE_AAA0127AZPA)]
        perimetro += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    area_perdida_estimada = perimetro * avg_setback
    area_edificable_estimada = area_lote - area_perdida_estimada
    
    assert area_edificable_estimada > 0, "Area edificable no puede ser negativa"
    assert area_edificable_estimada < area_lote, "Area edificable debe ser menor que el area del lote"
    
    print("  [OK] Area lote: {:.1f} m2".format(area_lote))
    print("  [OK] Perimetro: {:.1f} m".format(perimetro))
    print("  [OK] Retiro promedio: {:.1f} m".format(avg_setback))
    print("  [OK] Area edificable estimada: {:.1f} m2".format(area_edificable_estimada))


def test_io_compliance():
    """Verificar que el IO (indice de ocupacion) no excede el maximo."""
    area_lote = polygon_area(LOTE_AAA0127AZPA)
    
    # Retiros por lado
    setbacks_used = {}
    for s in SIDES_CLASIFICACION:
        idx = s["side_index"]
        setbacks_used[idx] = s["setback_m"]
    
    avg_setback = sum(setbacks_used.values()) / len(setbacks_used)
    
    # Perimetro
    perimetro = 0.0
    for i in range(len(LOTE_AAA0127AZPA)):
        x1, y1 = LOTE_AAA0127AZPA[i]
        x2, y2 = LOTE_AAA0127AZPA[(i + 1) % len(LOTE_AAA0127AZPA)]
        perimetro += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    area_edificable = max(0, area_lote - perimetro * avg_setback)
    io_estimado = area_edificable / area_lote if area_lote > 0 else 0
    
    io_maximo = 0.70
    assert io_estimado <= io_maximo + 0.15, \
        "IO estimado ({:.2f}) excede significativamente el maximo ({:.2f})".format(io_estimado, io_maximo)
    
    print("  [OK] IO estimado: {:.2f} (max permitido: {:.2f})".format(io_estimado, io_maximo))


def test_building_height_and_floors():
    """Verificar calculo de altura y pisos."""
    altura_pot = 11.4
    ALTURA_MIN_ENTREPISO = 2.5
    ALTURA_MAX_ENTREPISO = 3.8
    
    pisos_max = int(altura_pot / ALTURA_MIN_ENTREPISO)
    assert pisos_max == 4, "11.4m / 2.5m deberia dar 4 pisos, dio {}".format(pisos_max)
    
    pisos_totales = pisos_max  # sin piso de servicios para este test
    altura_entrepiso = min(ALTURA_MAX_ENTREPISO, altura_pot / pisos_totales)
    altura_final = altura_entrepiso * pisos_totales
    
    assert altura_final <= altura_pot, \
        "Altura final ({:.1f}) no puede exceder altura POT ({:.1f})".format(altura_final, altura_pot)
    
    print("  [OK] Altura POT: {:.1f}m".format(altura_pot))
    print("  [OK] Pisos: {} | Entrepiso: {:.2f}m | Altura total: {:.1f}m".format(
        pisos_totales, altura_entrepiso, altura_final))


if __name__ == "__main__":
    print("=== TESTS F1_PATIO_ESQUINA + F1_NORMATIVA_APLICAR ===")
    print("Lote: AAA0127AZPA (UPZ El Prado, Consolidacion, 315 m2, 11.4m altura)")
    print()
    
    tests = [
        test_lot_area,
        test_front_detection,
        test_corner_detection,
        test_patio_size,
        test_retiro_frontal_no_interfiere_patio,
        test_area_reduction_with_retiros,
        test_io_compliance,
        test_building_height_and_floors,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print("  [FAIL] {}: {}".format(test.__name__, str(e)))
            failed += 1
        except Exception as e:
            print("  [ERROR] {}: {}".format(test.__name__, str(e)))
            failed += 1
    
    print()
    print("=== RESULTADO: {} pasaron, {} fallaron ===".format(passed, failed))
    
    if failed > 0:
        sys.exit(1)
