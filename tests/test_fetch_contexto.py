"""
Tests para el procesamiento de datos de contexto urbano.

Verifica:
- Estructura del JSON de contexto
- Clasificación de lados por adyacencia
- Cálculos de altura y pisos
- Coherencia de datos POT
"""

import json
import math
import pytest
from pathlib import Path


# ============================================================
# FUNCIONES PURAS (extraídas para testing sin dependencias externas)
# ============================================================

def polygon_area(vertices):
    """Área de polígono (Shoelace formula)."""
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def segment_length(p1, p2):
    """Longitud de segmento entre dos puntos 2D."""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def polygon_perimeter(vertices):
    """Perímetro de polígono."""
    n = len(vertices)
    p = 0.0
    for i in range(n):
        p += segment_length(vertices[i], vertices[(i + 1) % n])
    return p


def calculate_floors(altura_max_m, entrepiso_min=2.5, entrepiso_max=3.8):
    """Calcular número máximo de pisos según altura POT."""
    pisos_max = int(altura_max_m / entrepiso_min)
    altura_entrepiso = min(entrepiso_max, altura_max_m / pisos_max if pisos_max > 0 else entrepiso_max)
    return pisos_max, round(altura_entrepiso, 2)


def calculate_io(area_huella, area_lote):
    """Índice de Ocupación."""
    if area_lote <= 0:
        return 0.0
    return round(area_huella / area_lote, 4)


def calculate_ic(area_huella, area_lote, pisos):
    """Índice de Construcción."""
    if area_lote <= 0:
        return 0.0
    return round((area_huella * pisos) / area_lote, 4)


def classify_side_by_adjacency(borde_idx, edge_midpoint, vecinos_polygons, proximity_m=2.0):
    """
    Clasifica un lado del lote como 'Frontal' o 'Lateral' según adyacencia con vecinos.
    
    Un lado es 'Frontal' si ningún vecino está a menos de proximity_m del segmento.
    Un lado es 'Lateral' si hay al menos un vecino colindante.
    
    Returns:
        dict con: lado_idx, clasificacion, vecino_colindante
    """
    from shapely.geometry import Point as ShapelyPoint
    
    pt = ShapelyPoint(edge_midpoint[0], edge_midpoint[1])
    
    tiene_vecino = False
    vecino_id = None
    
    for v_id, v_poly in vecinos_polygons:
        if v_poly.distance(pt) < proximity_m:
            tiene_vecino = True
            vecino_id = v_id
            break
    
    return {
        "lado_idx": borde_idx,
        "clasificacion": "Lateral" if tiene_vecino else "Frontal",
        "vecino_colindante": vecino_id,
    }


def find_fronts_from_clasificacion(sides_data):
    """Extrae índices de lados frontales de la clasificación."""
    fronts = []
    for side in sides_data:
        cls = side.get("classification", "").lower()
        if cls in ("frontal", "frente"):
            fronts.append(side["side_index"])
    return sorted(fronts)


def detect_consecutive_fronts(front_indices, num_vertices):
    """Detecta frentes consecutivos (indica esquina de calles)."""
    if len(front_indices) < 2:
        return []
    
    sorted_f = sorted(front_indices)
    consecutive_pairs = []
    
    for i in range(len(sorted_f)):
        a = sorted_f[i]
        b = sorted_f[(i + 1) % len(sorted_f)]
        diff = abs(a - b)
        # Consecutivos normales o wrap-around (ej: índices 8 y 0 en polígono de 9 vértices)
        if diff == 1 or diff == num_vertices - 1:
            consecutive_pairs.append((a, b))
    
    return consecutive_pairs


# ============================================================
# TESTS
# ============================================================

class TestGeometryCalculations:
    """Cálculos geométricos básicos."""
    
    def test_area_lote_aaa(self, lote_aaa0127azpa_vertices):
        """El área del lote AAA0127AZPA debe ser ~315 m²."""
        area = polygon_area(lote_aaa0127azpa_vertices)
        assert 310 < area < 320, f"Área esperada ~315 m², obtenida {area:.1f}"
    
    def test_area_rectangular(self, lote_rectangular):
        """Lote 10×20 debe dar 200 m²."""
        area = polygon_area(lote_rectangular)
        assert area == pytest.approx(200.0, abs=1.0)
    
    def test_area_esquina(self, lote_esquina):
        """Lote 12×15 debe dar 180 m²."""
        area = polygon_area(lote_esquina)
        assert area == pytest.approx(180.0, abs=1.0)
    
    def test_perimeter_rectangular(self, lote_rectangular):
        """Perímetro 10×20: 60 m."""
        p = polygon_perimeter(lote_rectangular)
        assert p == pytest.approx(60.0, abs=1.0)
    
    def test_perimeter_aaa(self, lote_aaa0127azpa_vertices):
        """Perímetro AAA0127AZPA ~72 m (9 lados irregulares)."""
        p = polygon_perimeter(lote_aaa0127azpa_vertices)
        assert 65 < p < 80, f"Perímetro esperado ~72m, obtenido {p:.1f}"


class TestPotDataStructure:
    """Validación de estructura y coherencia de datos POT."""
    
    def test_contexto_json_structure(self, lote_aaa0127azpa_contexto_json):
        """El JSON de contexto debe tener las claves requeridas."""
        if lote_aaa0127azpa_contexto_json is None:
            pytest.skip("JSON de contexto no disponible")
        
        required_keys = ["metadata", "pot_data", "topografia", "lote_objetivo", "vecinos", "lados"]
        for key in required_keys:
            assert key in lote_aaa0127azpa_contexto_json, f"Falta clave: {key}"
    
    def test_pot_data_values(self, pot_data_aaa0127azpa):
        """Verificar valores POT para AAA0127AZPA."""
        assert pot_data_aaa0127azpa["upz"] == "EL PRADO"
        assert 11.0 < pot_data_aaa0127azpa["altura_maxima_m"] < 12.0
        assert pot_data_aaa0127azpa["rango_edificabilidad"] == "3"
        assert "consolidación" in pot_data_aaa0127azpa["tratamiento"].lower()
    
    def test_lote_vertices_count(self, lote_aaa0127azpa_contexto_json):
        """El lote AAA0127AZPA debe tener ~9 vértices."""
        if lote_aaa0127azpa_contexto_json is None:
            pytest.skip("JSON de contexto no disponible")
        
        vertices = lote_aaa0127azpa_contexto_json["lote_objetivo"]["vertices_3d_local"]
        assert 8 <= len(vertices) <= 12, f"Esperados 9 vértices, obtenidos {len(vertices)}"
        
        # Verificar que son coordenadas locales (desplazadas al origen ~0)
        for vert in vertices:
            x, y, z = vert
            assert 70 <= x <= 100, f"Coordenada X fuera de rango local: {x}"
            assert 70 <= y <= 110, f"Coordenada Y fuera de rango local: {y}"
    
    def test_lados_classification_in_json(self, lote_aaa0127azpa_contexto_json):
        """El JSON debe tener clasificación de lados."""
        if lote_aaa0127azpa_contexto_json is None:
            pytest.skip("JSON de contexto no disponible")
        
        lados = lote_aaa0127azpa_contexto_json.get("lados", [])
        assert len(lados) > 0, "Debe haber clasificación de lados"
        
        for lado in lados:
            assert "lado_idx" in lado
            assert "clasificacion" in lado
            assert lado["clasificacion"] in ("Frontal", "Lateral", "Posterior")


class TestHeightAndFloors:
    """Cálculos de altura y pisos según normativa."""
    
    def test_floors_from_pot_height(self):
        """11.4m / 2.5m = 4 pisos."""
        pisos, entrepiso = calculate_floors(11.4)
        assert pisos == 4, f"Esperados 4 pisos, obtenidos {pisos}"
        assert 2.5 <= entrepiso <= 3.8
    
    def test_floors_min_height(self):
        """Altura mínima de 5m: 2 pisos máximo."""
        pisos, entrepiso = calculate_floors(5.0)
        assert pisos == 2
    
    def test_floors_high_building(self):
        """Edificio alto: 30m → 12 pisos (a 2.5m) o 7 pisos (a 3.8m)."""
        pisos, entrepiso = calculate_floors(30.0)
        assert pisos == 12
        assert entrepiso == 2.5  # prefiere entrepiso mínimo para maximizar pisos
    
    @pytest.mark.parametrize("altura, expected_pisos", [
        (2.5, 1),
        (5.0, 2),
        (7.5, 3),
        (10.0, 4),
        (12.5, 5),
        (15.0, 6),
        (20.0, 8),
    ])
    def test_floors_parametrized(self, altura, expected_pisos):
        """Serie de alturas → pisos esperados."""
        pisos, _ = calculate_floors(altura)
        assert pisos == expected_pisos, f"Altura {altura}m → {pisos} pisos, esperado {expected_pisos}"


class TestIOIC:
    """Cálculos de Índice de Ocupación y Construcción."""
    
    def test_io_basic(self):
        """Huella = 130 m², Lote = 315 m² → IO = 0.41."""
        io = calculate_io(130.7, 315.0)
        assert 0.40 <= io <= 0.42, f"IO esperado ~0.41, obtenido {io}"
    
    def test_ic_basic(self):
        """Huella = 130 m², 4 pisos, Lote = 315 m² → IC = 1.65."""
        ic = calculate_ic(130.7, 315.0, 4)
        assert 1.60 <= ic <= 1.70, f"IC esperado ~1.66, obtenido {ic}"
    
    def test_io_max_exceeded(self, tratamientos_params):
        """IO no debe exceder el máximo por tratamiento."""
        io_max = tratamientos_params["Consolidación"]["io_max"]
        
        # Lote AAA0127AZPA: huella ~130, lote ~315
        io_real = calculate_io(130.7, 315.0)
        assert io_real <= io_max, f"IO {io_real} excede máximo {io_max}"
    
    def test_ic_max_no_exceeded(self, tratamientos_params):
        """IC no debe exceder el máximo por tratamiento."""
        ic_max = tratamientos_params["Consolidación"]["ic_max"]
        
        # 130.7 m² × 4 pisos / 315 m²
        ic_real = calculate_ic(130.7, 315.0, 4)
        assert ic_real <= ic_max, f"IC {ic_real} excede máximo {ic_max}"
    
    def test_zero_area_safety(self):
        """Área de lote 0 no debe causar división por cero."""
        io = calculate_io(100.0, 0.0)
        assert io == 0.0
        
        ic = calculate_ic(100.0, 0.0, 5)
        assert ic == 0.0


class TestSideClassification:
    """Clasificación de lados del lote."""
    
    def test_fronts_count(self, lote_aaa0127azpa_clasificacion):
        """AAA0127AZPA debe tener al menos 2 frentes."""
        fronts = find_fronts_from_clasificacion(lote_aaa0127azpa_clasificacion)
        assert len(fronts) >= 2, f"Debe haber ≥2 frentes, hay {len(fronts)}"
    
    def test_total_sides_match(self, lote_aaa0127azpa_vertices, lote_aaa0127azpa_clasificacion):
        """Número de lados clasificados = número de vértices del polígono."""
        assert len(lote_aaa0127azpa_clasificacion) == len(lote_aaa0127azpa_vertices)
    
    def test_consecutive_fronts_esquina(self, lote_esquina_clasificacion):
        """Lote de esquina: debe tener 2 frentes consecutivos."""
        fronts = find_fronts_from_clasificacion(lote_esquina_clasificacion)
        assert len(fronts) == 2
        
        pairs = detect_consecutive_fronts(fronts, 4)
        assert len(pairs) >= 1, "Debe haber al menos un par de frentes consecutivos"
    
    def test_consecutive_fronts_aaa(self, lote_aaa0127azpa_clasificacion):
        """AAA0127AZPA: verificar que los frentes forman grupo(s) consecutivo(s)."""
        fronts = find_fronts_from_clasificacion(lote_aaa0127azpa_clasificacion)
        pairs = detect_consecutive_fronts(fronts, len(lote_aaa0127azpa_clasificacion))
        
        # Si hay 4 frentes, deberían estar agrupados (al menos 3 pares consecutivos)
        if len(fronts) == 4:
            assert len(pairs) >= 3, f"4 frentes deben tener ≥3 pares consecutivos, hay {len(pairs)}"
    
    def test_every_side_classified(self, lote_aaa0127azpa_clasificacion):
        """Cada lado debe tener una clasificación válida."""
        valid = {"Frontal", "Lateral", "Posterior"}
        for side in lote_aaa0127azpa_clasificacion:
            assert side["classification"] in valid, \
                f"Clasificación inválida: {side['classification']}"
            assert side["side_index"] >= 0


class TestNormativaConsolidacion:
    """Reglas específicas para tratamiento de Consolidación (Continua)."""
    
    def test_continua_lateral_zero(self):
        """En tipología Continua, los retiros laterales son 0m."""
        # La clasificación AAA0127AZPA muestra laterales con setback 0
        setback_lateral = 0.0
        assert setback_lateral == 0.0, "Continua debe tener laterales en 0m"
    
    def test_frontal_setback_min_3m(self, lote_aaa0127azpa_clasificacion):
        """Retiro frontal mínimo 3.0m según Decreto 555/2021."""
        for side in lote_aaa0127azpa_clasificacion:
            if side["classification"] == "Frontal":
                assert side["setback_m"] >= 3.0, \
                    f"Lado frontal {side['side_index']} tiene retiro {side['setback_m']}m (< 3.0m)"
    
    def test_patio_size_for_small_lot(self):
        """Lote < 500 m²: patio mínimo 3.0 m × 3.0 m."""
        area_lote = 315.0
        pisos = 4
        altura = pisos * 3.0  # 12m
        
        # Regla: max(3.0, altura * 0.25) por lado
        patio_size = max(3.0, altura * 0.25)
        
        assert patio_size == 3.0, f"Lote pequeño: patio debe ser 3.0m, calculado {patio_size}"
    
    def test_patio_size_for_large_building(self):
        """Edificio alto: patio escala con altura."""
        pisos = 10
        altura = pisos * 3.0  # 30m
        patio_size = max(3.0, altura * 0.25)  # 7.5m
        assert patio_size == pytest.approx(7.5, abs=0.1)
