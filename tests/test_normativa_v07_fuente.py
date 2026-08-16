# -*- coding: utf-8 -*-
"""Guardian de regresion para F1_ETAPA2_NORMATIVA_v07.py.

Valida desde el fuente (2026-08-16):
  - Envelope ESCALONADO por pisos superiores: empate volumetrico lateral
    (Anexo 5 POT, SECCION 1.9.c) + separacion sismica NSR-10 A.6.5 (mayor),
    aplicado solo a lados Lateral (vecino), no a via/espacio publico.
  - Salidas nuevas: envelope_por_piso, retiros_por_piso, GFA escalonado.
"""

import ast
import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v07.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def _extraer_funcion(nombre):
    """Extrae y ejecuta una funcion pura del fuente (sin dependencias de Rhino),
    inyectando las constantes numericas del modulo (p. ej. LATERAL_FRACCION_ALTURA)."""
    src_completo = _fuente()
    tree = ast.parse(src_completo)
    ns = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if getattr(t, "id", "").isupper():
                    try:
                        ns[t.id] = ast.literal_eval(node.value)
                    except Exception:
                        pass
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == nombre:
            src = ast.get_source_segment(src_completo, node)
            exec(src, ns)
            return ns[nombre]
    raise AssertionError("funcion %s no encontrada" % nombre)


def test_sintaxis_valida():
    ast.parse(_fuente())


def test_referencias_normativas():
    src = _fuente()
    assert "SECCION 1.9.c" in src or "1.9.c" in src
    assert "NSR-10 A.6.5" in src or "A.6.5" in src


def test_salidas_nuevas():
    src = _fuente()
    assert "envelope_por_piso" in src
    assert "retiros_por_piso" in src
    assert "GFA escalonado" in src
    assert "escalonados" in src


def test_entradas_nuevas():
    src = _fuente()
    assert "altura_vecinos_m" in src
    assert "empate_lateral_min_m" in src
    assert "nsr10_separacion_coef" in src


def test_no_escalona_via_ni_ep():
    # El retiro por piso solo toca lados clasificados Lateral (vecino);
    # Frontal (via) y EspacioPublico quedan con el retiro base (excepcion A.6.5)
    src = _fuente()
    assert 'lado.get("clasificacion", "Lateral") == "Lateral"' in src


def test_retiro_lateral_empate():
    f = _extraer_funcion("retiro_lateral_empate")
    # Caso A: vecino de 2 pisos (6,0 m); piso 3 a 9,6 m -> 1/5 x 3,6 = 0,72
    # -> minimo 3,0 m
    assert f(9.6, 6.0, 3.0) == 3.0
    # Sin excedente -> 0
    assert f(5.0, 6.0, 3.0) == 0.0
    # Excedente grande -> 1/5 (0,2) de la altura desde el empate
    assert abs(f(30.0, 6.0, 3.0) - 4.8) < 1e-9
    # Sin vecino informado -> 0 (sin escalonamiento + aviso)
    assert f(9.6, 0.0, 3.0) == 0.0


def test_separacion_sismica():
    f = _extraer_funcion("separacion_sismica_piso")
    # NSR-10 A.6.5, Tabla A.6.5-1 (>3 pisos, losas coincidentes 2%): s = 0,02 x h
    assert abs(f(22.8, 0.02) - 0.456) < 1e-9
    assert f(22.8, 0.0) == 0.0


def test_se_toma_el_mayor_pot_vs_nsr():
    src = _fuente()
    # En el bucle de pisos: r_lat = max(empate, sismica)
    assert "r_lat = max(r_empate, r_sismica)" in src


def test_voladizos_referencias():
    src = _fuente()
    # Anexo 5 SECCION 1.13: tabla, entrada, aplicacion en pisos != 1
    assert "SECCION 1.13" in src
    assert "VOLADIZO_POR_ANCHO_VIA" in src
    assert "voladizo_frontal_m" in src
    assert "voladizo_por_perfil_vial" in src


def test_voladizo_por_perfil_vial():
    f = _extraer_funcion("voladizo_por_perfil_vial")
    # SECCION 1.13.b, columna con antejardin/APAUP
    assert f(6.0) == 0.0          # <= 6,00 m: no se permite
    assert f(8.0) == 0.60         # >6-10 m
    assert f(12.9) == 0.80        # caso A: via 12,9 m -> 0,80 m
    assert f(15.0) == 0.80        # >10-15 m
    assert f(20.0) == 1.00        # >15-22 m
    assert f(30.0) == 1.50        # >22 m / malla arterial
    assert f(0.0) == 0.0          # sin via: sin voladizo


def test_voladizo_solo_pisos_no_primero_y_solo_frontal():
    src = _fuente()
    # se aplica en pisos != 1 y solo en lados Frontal
    assert "if nv > 1 and voladizo_frontal > 0:" in src
    assert '"Frontal"' in src
    # EspacioPublico (parques/EEP) y Lateral (aislamientos) NO se tocan
    assert "EspacioPublico" in src


def test_voladizo_en_mensaje_y_json():
    src = _fuente()
    assert "Voladizo frontal" in src
    assert "voladizo_frontal_m" in src
