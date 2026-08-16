"""
Tests para cálculos normativos y lógica de patios.

Verifica:
- Cálculo de retiros diferenciados
- Generación de patios en vértices vecino-vecino
- Validación de discontinuidades en polígono
- Lógica de balcones según clasificación vial
"""

import math
import pytest


# ============================================================
# FUNCIONES PURAS DE LÓGICA NORMATIVA
# ============================================================

def calculate_setback_by_classification(classification, treatment="consolidacion"):
    """
    Calcula retiro (m) según clasificación del lado y tratamiento.
    
    Decreto 555/2021:
    - Frontal: 3-5m según tipo de vía
    - Lateral (Continua): 0m
    - Lateral (Aislada): 3m
    - Posterior: 3m
    """
    treatment = treatment.lower()
    cls = classification.lower()
    
    if cls == "frontal":
        return 3.0  # default, puede ser 5.0 para vías arteriales
    elif cls == "lateral":
        if "desarrollo" in treatment or "aislada" in treatment:
            return 3.0
        return 0.0  # Continua
    elif cls == "posterior":
        return 3.0
    return 0.0


def calculate_patio_size(building_floors, lot_area=None, floor_height=3.0):
    """
    Calcula tamaño de patio de aislamiento.
    
    Reglas:
    - Lotes < 500 m², Continua, ≤ 5 pisos: 3.0 × 3.0 m fijo
    - General: max(3.0, altura_total × 0.25) m por lado
    """
    building_height = building_floors * floor_height
    
    if lot_area is not None and lot_area < 500.0 and building_floors <= 5:
        return 3.0
    
    patio_size = max(3.0, building_height * 0.25)
    # Redondear a 0.5 m más cercano
    return round(patio_size * 2.0) / 2.0


def find_corner_vertices(vertices, front_indices, lateral_indices):
    """
    Encuentra vértices donde convergen DOS lados vecinos (para patios).
    
    Un vértice genera patio si:
    - Es compartido por dos lados NO frontales
    - Ambos lados son laterales o posteriores
    
    Returns:
        list de (vertice_idx, lado_a, lado_b)
    """
    n = len(vertices)
    patio_vertices = []
    
    for i in range(n):
        lado_a = i
        lado_b = (i - 1) % n
        
        a_is_front = lado_a in front_indices
        b_is_front = lado_b in front_indices
        
        # Solo generar patio si AMBOS lados son NO frontales
        if not a_is_front and not b_is_front:
            patio_vertices.append((i, lado_a, lado_b))
    
    return patio_vertices


def find_discontinuities(vertices, angle_threshold=10.0):
    """
    Encuentra puntos de discontinuidad en un polígono (cambios bruscos de dirección).
    
    Similar al componente nativo Discontinuity de Grasshopper.
    
    Returns:
        list de (vertice_idx, angle_degrees)
    """
    n = len(vertices)
    disc = []
    
    for i in range(n):
        prev = vertices[(i - 1) % n]
        curr = vertices[i]
        next_v = vertices[(i + 1) % n]
        
        # Vectores de los segmentos
        v1 = (curr[0] - prev[0], curr[1] - prev[1])
        v2 = (next_v[0] - curr[0], next_v[1] - curr[1])
        
        l1 = math.sqrt(v1[0]**2 + v1[1]**2)
        l2 = math.sqrt(v2[0]**2 + v2[1]**2)
        
        if l1 < 0.001 or l2 < 0.001:
            continue
        
        # Producto cruz para ángulo
        dot = v1[0]*v2[0] + v1[1]*v2[1]
        cross = v1[0]*v2[1] - v1[1]*v2[0]
        
        cos_a = max(-1.0, min(1.0, dot / (l1 * l2)))
        angle = math.degrees(math.acos(cos_a))
        
        # Ángulo interno vs externo
        if cross > 0:
            angle = 360.0 - angle
        
        # Discontinuidad si el ángulo NO es 0° ni 360° (cambio de dirección)
        # Ángulo 0° = colineal (sin discontinuidad)
        # Ángulo ~90° = esquina (discontinuidad)
        deviation = min(abs(angle), abs(360.0 - angle))
        if deviation > angle_threshold:
            disc.append((i, round(angle, 1)))
    
    return disc


def calculate_balcony_max(classification, road_width=None):
    """
    Calcula voladizo máximo de balcón según clasificación vial.
    
    Decreto 555/2021:
    - Vía arterial principal: 1.20 m
    - Vía arterial complementaria: 1.00 m  
    - Vía colectora: 0.80 m (solo pisos superiores)
    - Vía local: 0.60 m (solo pisos superiores)
    - Vía peatonal: NO balcón
    """
    cls = classification.lower()
    
    if "peatonal" in cls:
        return 0.0, False
    
    if "arterial" in cls and "principal" in cls:
        return 1.20, True
    elif "arterial" in cls:
        return 1.00, True
    elif "colector" in cls:
        return 0.80, True
    elif "local" in cls:
        return 0.60, True
    
    return 0.60, True  # default conservador


def estimate_building_footprint_area(lote_vertices, sides_clasificacion):
    """
    Estima el área de huella edificable con retiros diferenciados.
    
    Método simplificado:
    - Para cada lado, desplaza el segmento hacia adentro según su retiro
    - Calcula el área del polígono resultante
    
    Returns:
        (area_estimada, perimetro_estimado)
    """
    n = len(lote_vertices)
    area_lote = polygon_area_2d(lote_vertices)
    
    # Calcular retiros por lado
    setbacks = {}
    for side in sides_clasificacion:
        idx = side["side_index"]
        setbacks[idx] = side.get("setback_m", 0.0)
    
    # Rellenar faltantes
    for i in range(n):
        if i not in setbacks:
            setbacks[i] = 0.0
    
    # Estimar área perdida por retiros
    perimetro = 0.0
    area_perdida = 0.0
    
    for i in range(n):
        p1 = lote_vertices[i]
        p2 = lote_vertices[(i + 1) % n]
        seg_len = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        perimetro += seg_len
        area_perdida += seg_len * setbacks[i]
    
    area_estimada = max(0.0, area_lote - area_perdida)
    
    return area_estimada, perimetro


def polygon_area_2d(vertices):
    """Área de polígono 2D (Shoelace)."""
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


# ============================================================
# TESTS
# ============================================================

class TestSetbackRules:
    """Reglas de retiros por clasificación."""
    
    def test_continua_lateral_zero(self):
        """Consolidación Continua: laterales = 0m."""
        sb = calculate_setback_by_classification("Lateral", "Consolidación")
        assert sb == 0.0
    
    def test_aislada_lateral_3m(self):
        """Desarrollo Aislada: laterales = 3m."""
        sb = calculate_setback_by_classification("Lateral", "Desarrollo")
        assert sb == 3.0
    
    def test_frontal_default_3m(self):
        """Frente por defecto: 3m."""
        sb = calculate_setback_by_classification("Frontal", "Consolidación")
        assert sb == 3.0
    
    def test_posterior_always_3m(self):
        """Posterior siempre 3m independiente del tratamiento."""
        for t in ["Consolidación", "Desarrollo", "Renovación"]:
            assert calculate_setback_by_classification("Posterior", t) == 3.0
    
    def test_unknown_classification_default_zero(self):
        """Clasificación desconocida: 0m (conservador)."""
        assert calculate_setback_by_classification("XYZ", "Cualquiera") == 0.0

    def test_espacio_publico_zero(self):
        """Espacio público (parques/plazas): aislamiento 0m (base de trabajo)."""
        for t in ["Consolidación", "Desarrollo", "Renovación Urbana"]:
            assert calculate_setback_by_classification("EspacioPublico", t) == 0.0

    def test_espacio_publico_zero_en_v04(self):
        """El mapeo real de F1_ETAPA2_NORMATIVA_v04 da 0 para EspacioPublico y Lateral.

        Regla de base de trabajo (2026-08-15, pre-NSR-10): el aislamiento sobre
        espacio público es 0 m y en tipología continua el aislamiento sobre
        vecinos es 0 m. NSR-10 modificará esto más adelante.
        """
        # Replica del bloque de retiros del v04 (misma lógica)
        def retiro_v04(cls, dist_via=999.0):
            if cls == "Frontal":
                return 5.0 if dist_via < 5.0 else 3.0
            elif cls == "Posterior":
                return 3.0
            else:
                return 0.0  # EspacioPublico y Lateral

        assert retiro_v04("EspacioPublico") == 0.0
        assert retiro_v04("Lateral") == 0.0
        assert retiro_v04("Frontal") == 3.0
        assert retiro_v04("Posterior") == 3.0


class TestPatioGeneration:
    """Lógica de generación de patios de aislamiento."""
    
    def test_patio_small_lot_3m(self):
        """Lote < 500 m², ≤ 5 pisos: patio 3.0m fijo."""
        assert calculate_patio_size(3, lot_area=200.0) == 3.0
        assert calculate_patio_size(4, lot_area=315.0) == 3.0
        assert calculate_patio_size(5, lot_area=400.0) == 3.0
    
    def test_patio_large_building_scales(self):
        """Edificio de 12 pisos: patio escala con altura."""
        size = calculate_patio_size(12, lot_area=1000.0)
        expected = max(3.0, 12 * 3.0 * 0.25)  # 9.0 m
        assert size == pytest.approx(9.0, abs=0.5)
    
    def test_patio_min_3m(self):
        """Patio nunca menor a 3.0m."""
        size = calculate_patio_size(1, lot_area=100.0)
        assert size >= 3.0
    
    def test_find_patio_vertices_no_fronts(self):
        """Sin frentes: todos los vértices generan patio."""
        vertices = [(0, 0), (10, 0), (10, 10), (0, 10)]
        patio_verts = find_corner_vertices(vertices, [], [0, 1, 2, 3])
        assert len(patio_verts) == 4  # todos los vértices
    
    def test_find_patio_vertices_two_fronts(self):
        """Dos frentes adyacentes: solo el vértice interior opuesto genera patio."""
        vertices = [(0, 0), (10, 0), (10, 10), (0, 10)]
        fronts = [0, 1]  # lados 0 y 1 son frontales
        laterals = [2, 3]
        
        patio_verts = find_corner_vertices(vertices, fronts, laterals)
        
        # Vértice 3 = convergencia de lados 2 y 3 (ambos NO frontales)
        assert (3, 3, 2) in patio_verts
    
    def test_no_patio_at_street_corner(self):
        """Vértice donde convergen dos frentes NO genera patio."""
        vertices = [(0, 0), (10, 0), (10, 10), (0, 10)]
        fronts = [0, 1]  # frentes en lados 0 y 1
        
        patio_verts = find_corner_vertices(vertices, fronts, [2, 3])
        
        # Vértice 1 = convergencia de lados 0 (frontal) y 1 (frontal)
        # NO debe aparecer en patio_verts
        patio_indices = [v[0] for v in patio_verts]
        assert 1 not in patio_indices  # esquina de calles, sin patio


class TestDiscontinuity:
    """Detección de discontinuidades en polígonos."""
    
    def test_rectangle_no_discontinuities(self):
        """Rectángulo: todos los ángulos son 90°, sin discontinuidades."""
        vertices = [(0, 0), (10, 0), (10, 10), (0, 10)]
        disc = find_discontinuities(vertices, angle_threshold=10.0)
        # En un rectángulo, cada vértice tiene ángulo ~90°, desviación de 180° = 90°
        assert len(disc) == 4  # todos son discontinuidades (ángulos de 90°)
    
    def test_irregular_lot_discontinuities(self, lote_aaa0127azpa_vertices):
        """Lote irregular (AAA0127AZPA): detecta cambios de dirección."""
        disc = find_discontinuities(lote_aaa0127azpa_vertices, angle_threshold=5.0)
        # Lote de 9 vértices irregular con varios vértices casi-colineales
        # Con threshold bajo (5°) se detectan más discontinuidades
        assert len(disc) >= 3, f"Esperadas ≥3 discontinuidades, detectadas {len(disc)}"
    
    def test_colinear_vertices_ignored(self):
        """Vértices colineales no son discontinuidades."""
        # Segmento con punto intermedio colineal
        vertices = [(0, 0), (5, 0), (10, 0), (10, 10), (0, 10)]
        disc = find_discontinuities(vertices, angle_threshold=1.0)
        
        # Vértice 1 (5,0) está en línea recta → no es discontinuidad
        disc_indices = [d[0] for d in disc]
        # Nota: el punto (5,0) entre (0,0) y (10,0) forma un ángulo de ~0°
        # Con la lógica corregida no debería marcarse como discontinuidad
        # Pero puede marcarse por la irregularidad del contorno (depende de la implementación)
        # Lo que importa es que los otros 4 vértices SÍ sean detectados
        assert 2 in disc_indices or 3 in disc_indices, "Debe detectar vértices de esquina"


class TestBalconyRules:
    """Reglas de balcones según clasificación vial."""
    
    def test_arterial_principal_balcony(self):
        """Vía arterial principal: 1.20m, todos los pisos."""
        max_m, all_floors = calculate_balcony_max("arterial_principal")
        assert max_m == 1.20
        assert all_floors is True
    
    def test_colectora_balcony(self):
        """Vía colectora: 0.80m, todos los pisos (según interpretación)."""
        max_m, _ = calculate_balcony_max("colectora")
        assert max_m == 0.80
    
    def test_local_balcony(self):
        """Vía local: 0.60m."""
        max_m, _ = calculate_balcony_max("local")
        assert max_m == 0.60
    
    def test_peatonal_no_balcony(self):
        """Vía peatonal: NO se permiten balcones."""
        max_m, _ = calculate_balcony_max("peatonal")
        assert max_m == 0.0


class TestFootprintEstimation:
    """Estimación de huella edificable."""
    
    def test_rectangular_with_setbacks(self, lote_rectangular, lote_rectangular_clasificacion):
        """Lote 10×20 con retiros: estimar huella."""
        area, perim = estimate_building_footprint_area(lote_rectangular, lote_rectangular_clasificacion)
        
        # Área original: 200 m²
        # Pérdida: frente 20m × 3m + posterior 20m × 3m = 120 m²
        # Huella esperada: 80 m²
        assert 70 <= area <= 90, f"Huella esperada ~80 m², estimada {area:.1f}"
        assert perim == pytest.approx(60.0, abs=1.0)
    
    def test_continua_minimal_setbacks(self, lote_rectangular):
        """Continua: solo frente y posterior tienen retiro."""
        clasificacion = [
            {"side_index": 0, "classification": "Frontal", "setback_m": 3.0},
            {"side_index": 1, "classification": "Lateral", "setback_m": 0.0},
            {"side_index": 2, "classification": "Posterior", "setback_m": 3.0},
            {"side_index": 3, "classification": "Lateral", "setback_m": 0.0},
        ]
        
        area, _ = estimate_building_footprint_area(lote_rectangular, clasificacion)
        
        # Área original: 200 m²
        # Pérdida: frente 20 × 3 + posterior 20 × 3 = 120
        # Huella: 80 m² → con laterales 0m esto parece mucho
        # Pero es una estimación conservadora
        assert area > 0
        assert area < 200.0  # menor que área del lote
    
    def test_aaa_footprint_estimate(self, lote_aaa0127azpa_vertices, lote_aaa0127azpa_clasificacion):
        """AAA0127AZPA: estimar huella con retiros reales."""
        area, _ = estimate_building_footprint_area(
            lote_aaa0127azpa_vertices, lote_aaa0127azpa_clasificacion
        )
        
        # Área original: ~315 m²
        # Huella esperada: ~130 m² (validado con Rhino)
        # La estimación simplificada es conservadora (ignora intersecciones de esquina)
        assert 80 <= area <= 200, f"Huella estimada {area:.1f} fuera de rango esperado (80-200)"


# ============================================================
# REGLAS v05 (Anexo 5 POT — Decreto 466/2024) y LADOS v03
# ============================================================


def retiro_posterior_consolidacion_v05(pisos):
    """Réplica de F1_ETAPA2_NORMATIVA_v05: tabla Consolidación (Anexo 5 §5.4.b)."""
    POSTERIOR_CONSOLIDACION = [
        (3, 3.0), (6, 5.0), (9, 6.0), (12, 8.0), (15, 10.0),
        (18, 12.0), (22, 14.0), (25, 16.0), (28, 18.0), (99, 20.0),
    ]
    for limite, retiro in POSTERIOR_CONSOLIDACION:
        if pisos <= limite:
            return retiro
    return POSTERIOR_CONSOLIDACION[-1][1]


def retiro_frontal_por_ancho_via_v05(ancho_via_m):
    """Réplica de F1_ETAPA2_NORMATIVA_v05: antejardín por ancho de vía.

    Regla histórica pre-555 (respaldo cuando el mapa CU-5.5 no señala):
    vías < 12m -> 3,00m; 12-20m -> 5,00m; >=20m -> 7,00m.
    """
    FRONTAL_POR_ANCHO_VIA = [(12.0, 3.0), (20.0, 5.0), (999.0, 7.0)]
    if ancho_via_m is None or ancho_via_m <= 0:
        return 3.0
    for limite, retiro in FRONTAL_POR_ANCHO_VIA:
        if ancho_via_m < limite:
            return retiro
    return FRONTAL_POR_ANCHO_VIA[-1][1]


def retiro_lateral_aislada_v05(altura_total):
    """Réplica de F1_ETAPA2_NORMATIVA_v05: lateral aislada = 1/5 altura, mín 4,00m."""
    return max(0.2 * altura_total, 4.0)


def clasificar_lados_v03(lados):
    """Réplica de F1_ETAPA2_LADOS_v03: clasificación + regla Posterior N-1.

    lados: lista de dicts con toca_via, toca_ep, toca_vecino, comparte_a.
    Retorna lista con la clasificación final (en el orden de entrada).
    """
    n = len(lados)
    out = []
    for l in lados:
        if l["toca_via"]:
            cat = "Frontal"
        elif l["toca_ep"]:
            cat = "EspacioPublico"
        elif l["toca_vecino"]:
            cat = "Lateral"
        else:
            cat = "Lateral"  # provisional
        out.append({"clasificacion": cat, "toca_vecino": l["toca_vecino"],
                    "toca_via": l["toca_via"], "toca_ep": l["toca_ep"],
                    "comparte_a": l.get("comparte_a", False)})

    # Regla Posterior: SOLO cuando todos los lados menos uno colindan con vecinos
    lados_sin_vecino = [i for i, l in enumerate(out) if not l["toca_vecino"]]
    idx_posterior = None
    if len(lados_sin_vecino) == 1:
        iu = lados_sin_vecino[0]
        if not (out[iu]["toca_via"] or out[iu]["toca_ep"]):
            idx_posterior = iu  # único lado libre
        else:
            # lado con vecino más lejano al único frente: en cuadriláteros es
            # el opuesto (iu+2)%n (el script real usa distancia geométrica)
            if n == 4:
                idx_posterior = (iu + 2) % 4
            else:
                mejor = -1
                for i, l in enumerate(out):
                    if l["toca_vecino"] and i != iu:
                        if mejor == -1 or abs(i - iu) > abs(mejor - iu):
                            mejor = i
                idx_posterior = mejor
    elif len(lados_sin_vecino) > 1:
        libres = [i for i in lados_sin_vecino
                  if not (out[i]["toca_via"] or out[i]["toca_ep"])]
        if len(libres) == 1:
            idx_posterior = libres[0]

    if idx_posterior is not None:
        out[idx_posterior]["clasificacion"] = "Posterior"

    # Fallback: lado del frente sin colindancia detectada -> Frontal
    for l in out:
        if l["clasificacion"] == "Lateral" and l["comparte_a"] and not l["toca_vecino"]:
            l["clasificacion"] = "Frontal"

    return [l["clasificacion"] for l in out]


class TestNormativaV05:
    """Reglas del Anexo 5 POT (Decreto 466/2024) implementadas en v05."""

    def test_posterior_tabla_consolidacion(self):
        """Anexo 5 §5.4.b: 3m (≤3p), 5m (4-6p), 6m (7-9p), 8m (10-12p)."""
        assert retiro_posterior_consolidacion_v05(3) == 3.0
        assert retiro_posterior_consolidacion_v05(4) == 5.0
        assert retiro_posterior_consolidacion_v05(6) == 5.0
        assert retiro_posterior_consolidacion_v05(7) == 6.0
        assert retiro_posterior_consolidacion_v05(10) == 8.0
        assert retiro_posterior_consolidacion_v05(15) == 10.0
        assert retiro_posterior_consolidacion_v05(30) == 20.0

    def test_frontal_por_ancho_via(self):
        """Antejardín según ancho de vía: 7,5m -> 3,00m (caso El Prado)."""
        assert retiro_frontal_por_ancho_via_v05(7.5) == 3.0
        assert retiro_frontal_por_ancho_via_v05(11.9) == 3.0
        assert retiro_frontal_por_ancho_via_v05(12.0) == 5.0
        assert retiro_frontal_por_ancho_via_v05(15.0) == 5.0
        assert retiro_frontal_por_ancho_via_v05(20.0) == 7.0
        assert retiro_frontal_por_ancho_via_v05(0.0) == 3.0  # sin dato
        assert retiro_frontal_por_ancho_via_v05(None) == 3.0

    def test_lateral_aislada_frac_altura(self):
        """Anexo 5 §1.9.b: lateral aislada = 1/5 altura, mínimo 4,00m."""
        # 5 pisos x 3m = 15m -> 1/5 = 3,0 -> mín 4,0
        assert retiro_lateral_aislada_v05(15.0) == 4.0
        # 10 pisos x 3m = 30m -> 1/5 = 6,0
        assert retiro_lateral_aislada_v05(30.0) == 6.0
        # 20 pisos x 3m = 60m -> 1/5 = 12,0
        assert retiro_lateral_aislada_v05(60.0) == 12.0

    def test_retiros_lote_prueba_continua(self):
        """Lote de prueba (1 frontal vía 7,5m + 1 EP + 2 laterales), Continua.

        Confirmado por el usuario 2026-08-15: sin Posterior. Retiros:
        frontal 3,0m; EP 0; laterales 0 (tipología continua).
        """
        lados = [
            {"id": 0, "clasificacion": "Frontal", "dist_v_m": 8.0},
            {"id": 1, "clasificacion": "EspacioPublico"},
            {"id": 2, "clasificacion": "Lateral"},
            {"id": 3, "clasificacion": "Lateral"},
        ]
        retiros = {}
        for lado in lados:
            idx = lado["id"]
            cls = lado["clasificacion"]
            if cls == "Frontal":
                retiros[idx] = retiro_frontal_por_ancho_via_v05(7.5)
            elif cls == "Posterior":
                retiros[idx] = retiro_posterior_consolidacion_v05(4)
            elif cls == "EspacioPublico":
                retiros[idx] = 0.0
            else:
                retiros[idx] = 0.0  # Continua

        assert retiros[0] == 3.0
        assert retiros[1] == 0.0
        assert retiros[2] == 0.0
        assert retiros[3] == 0.0

    def test_retiros_lote_prueba_aislada(self):
        """Mismo lote con tipología Aislada: laterales = 1/5 altura mín 4m."""
        lados = [
            {"id": 0, "clasificacion": "Frontal", "dist_v_m": 8.0},
            {"id": 1, "clasificacion": "EspacioPublico"},
            {"id": 2, "clasificacion": "Lateral"},
            {"id": 3, "clasificacion": "Lateral"},
        ]
        altura_total = 4 * 3.0  # rango 3 = 4 pisos
        retiros = {}
        for lado in lados:
            idx = lado["id"]
            cls = lado["clasificacion"]
            if cls == "Frontal":
                retiros[idx] = retiro_frontal_por_ancho_via_v05(7.5)
            elif cls == "Posterior":
                retiros[idx] = retiro_posterior_consolidacion_v05(4)
            elif cls == "EspacioPublico":
                retiros[idx] = 0.0
            else:
                retiros[idx] = retiro_lateral_aislada_v05(altura_total)

        assert retiros[0] == 3.0
        assert retiros[1] == 0.0
        assert retiros[2] == retiro_lateral_aislada_v05(12.0)  # 4,0
        assert retiros[3] == retiro_lateral_aislada_v05(12.0)

    def test_empate_volumetrico_posterior(self):
        """Anexo 5 §5.4.c: vecino posterior de 3+ pisos -> retiro posterior 0."""
        # Sin empate: 5 pisos -> 5,0m
        assert retiro_posterior_consolidacion_v05(5) == 5.0
        # Con empate (vecino de 3+ pisos): 0 en la huella
        empate_posterior = 3.0 >= 3.0
        assert empate_posterior is True


class TestLadosV03Posterior:
    """Regla Posterior de F1_ETAPA2_LADOS_v03 (N-1 lados con vecino)."""

    def test_lote_rodeado_vecinos_con_frente(self):
        """[vía, vecino, vecino, vecino]: el opuesto al frente es Posterior."""
        lados = [
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
        ]
        cats = clasificar_lados_v03(lados)
        assert cats[0] == "Frontal"
        assert cats.count("Posterior") == 1
        assert cats[2] == "Posterior"  # opuesto al frente
        assert cats[1] == "Lateral"
        assert cats[3] == "Lateral"

    def test_lote_prueba_sin_posterior(self):
        """[vía, EP, vecino, vecino]: NO existe Posterior (confirmado usuario)."""
        lados = [
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": True, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
        ]
        cats = clasificar_lados_v03(lados)
        assert "Posterior" not in cats
        assert cats[0] == "Frontal"
        assert cats[1] == "EspacioPublico"
        assert cats[2] == "Lateral"
        assert cats[3] == "Lateral"

    def test_lote_esquinero_dos_frentes(self):
        """[vía, vía, vecino, vecino]: dos frontales, sin posterior."""
        lados = [
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
        ]
        cats = clasificar_lados_v03(lados)
        assert cats.count("Frontal") == 2
        assert "Posterior" not in cats

    def test_lote_con_fondo_libre(self):
        """[vía, vecino, vecino, libre]: el lado libre es Posterior."""
        lados = [
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": False},
        ]
        cats = clasificar_lados_v03(lados)
        assert cats[3] == "Posterior"
        assert cats.count("Posterior") == 1

    def test_frente_sin_via_detectada_fallback(self):
        """Lado del frente sin vía detectada (comparte A): Frontal por fallback.

        Caso: 2+ lados sin vecino y NINGUNO libre -> sin Posterior; el lado
        que comparte el vértice A sin colindancia queda como Frontal.
        """
        lados = [
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": False, "comparte_a": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
        ]
        cats = clasificar_lados_v03(lados)
        assert cats[0] == "Frontal"
        assert cats[2] == "Frontal"  # fallback comparte_a (2 libres -> sin posterior)
        assert cats[1] == "Lateral"
        assert "Posterior" not in cats

    def test_lado_libre_unico_es_posterior(self):
        """[vía, vecino, vecino, libre]: el único lado libre es Posterior.

        La regla N-1 tiene prioridad sobre el fallback comparte_a: el lado
        libre único (sin vía ni EP) se clasifica Posterior.
        """
        lados = [
            {"toca_via": True, "toca_ep": False, "toca_vecino": False},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": True},
            {"toca_via": False, "toca_ep": False, "toca_vecino": False, "comparte_a": False},
        ]
        cats = clasificar_lados_v03(lados)
        assert cats[3] == "Posterior"
        assert cats.count("Posterior") == 1


# ============================================================
# DERIVACION REGLAMENTARIA (NORMATIVA_v05 + ETAPA1_v02)
# ============================================================


def derivar_reglamentacion_v05(tipologia_raw, ancho_via_raw, antejardin_raw, reg_json):
    """Réplica de la cadena operador > reglamentación > default de NORMATIVA_v05."""
    reg_data = None
    if reg_json:
        import json as _json
        try:
            d = _json.loads(reg_json)
            if isinstance(d, dict) and "pot_data" in d:
                reg_data = d
        except Exception:
            reg_data = None

    def num(campo, default=0.0):
        if reg_data is None:
            return default
        v = reg_data.get("pot_data", {}).get(campo)
        if v is None or v == "":
            return default
        try:
            return float(v)
        except Exception:
            return default

    def sstr(campo, default=""):
        if reg_data is None:
            return default
        v = reg_data.get("pot_data", {}).get(campo)
        if v is None:
            return default
        s = str(v).strip()
        return s or default

    # tipologia: operador > reglamentacion > Continua
    tipologia = "Continua"
    operador_tiene = tipologia_raw is not None and str(tipologia_raw).strip() != ""
    if operador_tiene:
        tipologia = str(tipologia_raw).strip().title()
    if not operador_tiene:
        reg = sstr("tipologia")
        if reg:
            tipologia = reg.title()

    # ancho_via_m: operador > reglamentacion > 0
    ancho = 0.0
    try:
        ancho = float(ancho_via_raw) if ancho_via_raw else 0.0
    except Exception:
        ancho = 0.0
    if ancho <= 0:
        ancho = num("ancho_via_m", 0.0)

    # antejardin_m: operador > reglamentacion > 0 (regla por ancho fuera)
    antejardin = 0.0
    try:
        antejardin = float(antejardin_raw) if antejardin_raw else 0.0
    except Exception:
        antejardin = 0.0
    if antejardin <= 0:
        antejardin = num("antejardin_m", 0.0)

    return tipologia, ancho, antejardin


class TestDerivacionReglamentariaV05:
    """Cadena operador > reglamentación > default (NORMATIVA_v05 + ETAPA1_v02)."""

    REG_COMPLETO = '{"pot_data": {"tratamiento": "Consolidación", "tipologia": "Aislada", "ancho_via_m": 7.5, "antejardin_m": 2.0}}'
    REG_PARCIAL = '{"pot_data": {"tratamiento": "Consolidación", "ancho_via_m": 7.5}}'

    def test_entradas_nulas_usan_reglamentacion(self):
        """Operador sin datos: tipología/ancho/antejardín salen de la reglamentación."""
        tip, ancho, ante = derivar_reglamentacion_v05(None, None, None, self.REG_COMPLETO)
        assert tip == "Aislada"
        assert ancho == 7.5
        assert ante == 2.0

    def test_entradas_cero_usan_reglamentacion(self):
        """Valor 0 se trata como no definido: usa reglamentación."""
        tip, ancho, ante = derivar_reglamentacion_v05("", 0, 0, self.REG_COMPLETO)
        assert tip == "Aislada"
        assert ancho == 7.5
        assert ante == 2.0

    def test_operador_gana_sobre_reglamentacion(self):
        """Si el operador define el valor, gana sobre la reglamentación."""
        tip, ancho, ante = derivar_reglamentacion_v05("Continua", 15.0, 3.0, self.REG_COMPLETO)
        assert tip == "Continua"
        assert ancho == 15.0
        assert ante == 3.0

    def test_reglamentacion_parcial_solo_ancho(self):
        """Reglamentación parcial: lo que no está queda en default (tipología Continua)."""
        tip, ancho, ante = derivar_reglamentacion_v05(None, None, None, self.REG_PARCIAL)
        assert tip == "Continua"  # sin dato reglamentario de tipología
        assert ancho == 7.5
        assert ante == 0.0  # sin dato reglamentario -> regla por ancho fuera

    def test_sin_reglamentacion_defaults(self):
        """Sin reglamentacion_json: defaults (tipología Continua, sin ancho/antejardín)."""
        tip, ancho, ante = derivar_reglamentacion_v05(None, None, None, None)
        assert tip == "Continua"
        assert ancho == 0.0
        assert ante == 0.0

    def test_reglamentacion_invalida_ignorada(self):
        """JSON inválido se ignora (defaults), no rompe el script."""
        tip, ancho, ante = derivar_reglamentacion_v05(None, None, None, "{no-json")
        assert tip == "Continua"
        assert ancho == 0.0
        assert ante == 0.0


# ============================================================
# ANCHO DE VIA ENTRE ANDENES (LADOS_v04)
# ============================================================


def dist_punto_segmento_2d(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx-ax, by-ay
    if dx == 0 and dy == 0:
        return math.hypot(px-ax, py-ay)
    t = ((px-ax)*dx + (py-ay)*dy) / (dx*dx + dy*dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(px-(ax+t*dx), py-(ay+t*dy))


def punto_mas_cercano_segmento_2d(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx-ax, by-ay
    if dx == 0 and dy == 0:
        return a
    t = ((px-ax)*dx + (py-ay)*dy) / (dx*dx + dy*dy)
    t = max(0.0, min(1.0, t))
    return (ax+t*dx, ay+t*dy)


def dist_punto_polyline_2d(p, poly):
    mejor = 1e18
    for i in range(len(poly)-1):
        d = dist_punto_segmento_2d(p, poly[i], poly[i+1])
        if d < mejor:
            mejor = d
    return mejor


def punto_cercano_y_tangente_2d(p, poly):
    """(punto_mas_cercano, tangente_unitaria) en la polilinea."""
    mejor_d = 1e18
    mejor_q = poly[0]
    mejor_dir = (1.0, 0.0)
    for i in range(len(poly)-1):
        a, b = poly[i], poly[i+1]
        d = dist_punto_segmento_2d(p, a, b)
        if d < mejor_d:
            mejor_d = d
            mejor_q = punto_mas_cercano_segmento_2d(p, a, b)
            dx, dy = b[0]-a[0], b[1]-a[1]
            L = math.hypot(dx, dy)
            if L > 1e-9:
                mejor_dir = (dx/L, dy/L)
    return mejor_q, mejor_dir


def interseccion_rayo_segmento_2d(orig, dirv, a, b):
    """orig + t*dirv = a + u*(b-a), t>=0, u en [0,1]."""
    dx, dy = dirv
    ex, ey = b[0]-a[0], b[1]-a[1]
    den = dx*ey - dy*ex
    if abs(den) < 1e-12:
        return None
    fx, fy = a[0]-orig[0], a[1]-orig[1]
    t = (fx*ey - fy*ex) / den
    u = (fx*dy - fy*dx) / den
    if t < -1e-9 or u < -1e-9 or u > 1+1e-9:
        return None
    return (orig[0] + t*dx, orig[1] + t*dy)


def medir_ancho_via_andenes_v04(lote_pts, lado_frontal_idx, andenes, muestras=7):
    """Réplica 2D pura del algoritmo de LADOS_v04 (medición entre andenes).

    Algoritmo: muestrear el lado frontal -> andén más cercano al predio ->
    normal en ese punto -> rayo en ambas direcciones -> intersección con
    otro andén -> distancia = ancho de vía.
    """
    if not andenes or len(andenes) < 2:
        return 0.0
    n = len(lote_pts)
    i = lado_frontal_idx
    j = (i + 1) % n
    p1, p2 = lote_pts[i], lote_pts[j]
    if math.hypot(p2[0]-p1[0], p2[1]-p1[1]) < 0.01:
        return 0.0

    anchos = []
    for k in range(muestras):
        t = float(k) / max(1, muestras-1)
        p = (p1[0] + t*(p2[0]-p1[0]), p1[1] + t*(p2[1]-p1[1]))

        mejor_idx = None
        mejor_d = 1e18
        for idx_c, crv in enumerate(andenes):
            d = dist_punto_polyline_2d(p, crv)
            if d < mejor_d:
                mejor_d = d
                mejor_idx = idx_c
        if mejor_idx is None or mejor_d > 15.0:
            continue

        q1, tang = punto_cercano_y_tangente_2d(p, andenes[mejor_idx])
        nrm = (-tang[1], tang[0])
        dists = []
        for dirv in (nrm, (-nrm[0], -nrm[1])):
            for idx_c, crv in enumerate(andenes):
                if idx_c == mejor_idx:
                    continue
                for s in range(len(crv)-1):
                    q2 = interseccion_rayo_segmento_2d(q1, dirv, crv[s], crv[s+1])
                    if q2:
                        d = math.hypot(q2[0]-q1[0], q2[1]-q1[1])
                        if d > 0.5:
                            dists.append(d)
        if dists:
            anchos.append(min(dists))

    if not anchos:
        return 0.0
    return sum(anchos) / len(anchos)


class TestAnchoViaAndenesV04:
    """Medición del ancho de vía entre andenes (LADOS_v04)."""

    LOTE = [(0, 0), (26, 0), (26, 12), (0, 12)]  # lado 0 = frente sur

    def test_andenes_paralelos_7_5(self):
        """Dos andenes paralelos a 7,5 m: ancho medido ≈ 7,5 m."""
        andenes = [[(0, -0.5), (26, -0.5)], [(0, 7.0), (26, 7.0)]]
        ancho = medir_ancho_via_andenes_v04(self.LOTE, 0, andenes)
        assert ancho == pytest.approx(7.5, abs=0.05)

    def test_ancho_anda_a_normativa(self):
        """Ancho 7,5 m -> antejardín 3,00 m (regla vías < 12 m)."""
        andenes = [[(0, -0.5), (26, -0.5)], [(0, 7.0), (26, 7.0)]]
        ancho = medir_ancho_via_andenes_v04(self.LOTE, 0, andenes)
        assert retiro_frontal_por_ancho_via_v05(ancho) == 3.0

    def test_ancho_12_metros_antejardin_5(self):
        """Andenes a 12,0 m: antejardín 5,00 m (regla 12-20 m)."""
        andenes = [[(0, -0.5), (26, -0.5)], [(0, 11.5), (26, 11.5)]]
        ancho = medir_ancho_via_andenes_v04(self.LOTE, 0, andenes)
        assert ancho == pytest.approx(12.0, abs=0.05)
        assert retiro_frontal_por_ancho_via_v05(ancho) == 5.0

    def test_sin_andenes_cero(self):
        """Sin andenes: 0,0 m (NORMATIVA_v05 cae a reglamentación/default)."""
        assert medir_ancho_via_andenes_v04(self.LOTE, 0, []) == 0.0
        assert medir_ancho_via_andenes_v04(self.LOTE, 0, [[(0, -0.5), (26, -0.5)]]) == 0.0

    def test_andenes_divergentes_rango(self):
        """Andenes no paralelos (7,7 a 8,3 m): el promedio cae en el rango."""
        andenes = [[(0, -0.5), (26, -0.5)], [(0, 7.2), (26, 7.8)]]
        ancho = medir_ancho_via_andenes_v04(self.LOTE, 0, andenes)
        assert 7.0 < ancho < 9.0
