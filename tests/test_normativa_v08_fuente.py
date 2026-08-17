# -*- coding: utf-8 -*-
"""Guardian de regresion para F1_ETAPA2_NORMATIVA_v08.py.

Valida desde el fuente (2026-08-16):
  - Vecinos con alturas VARIABLES por lateral (SECCION 1.9.c por segmento):
    entrada vecinos_por_lado_json, subdivision del lado, retiro por vecino.
  - Recorte de la huella por SEMIPLANOS (cajas exteriores + BooleanDifference),
    robusto en poligonos concavos.
  - Compatibilidad: sin la entrada, comportamiento identico al v07
    (altura_vecinos_m global + voladizos SECCION 1.13).
"""

import ast
import json
import math
import os
import re

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v08.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def _extraer_funcion(nombre):
    """Extrae y ejecuta una funcion pura del fuente (sin dependencias de Rhino),
    inyectando las constantes numericas del modulo."""
    src_completo = _fuente()
    tree = ast.parse(src_completo)
    ns = {}
    ns["json"] = json
    ns["math"] = math
    ns["re"] = re
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


def test_entrada_vecinos_por_lado():
    src = _fuente()
    assert "vecinos_por_lado_json" in src
    assert "parsear_vecinos_por_lado" in src


def test_funciones_semiplanos():
    src = _fuente()
    assert "_recortar_puntos" in src
    assert "_subdividir_lado" in src
    assert "_subsegmentos_piso" in src
    assert "_poligono_ccw" in src
    assert "_area_signada_puntos" in src
    assert "_curva_desde_puntos" in src
    # recorte por PUNTOS (Sutherland-Hodgman): sin cajas gigantes que parten
    # el poligono concavo (causa de los Curve[] por piso)
    assert "_caja_semiplano" not in src
    # los patios siguen con boolean (envelope_final)
    assert "CreateBooleanDifference" in src
    assert "JoinCurves" in src


def test_mensaje_v08():
    src = _fuente()
    assert "NORMATIVA v08" in src
    assert "Vecinos por lado" in src


def test_compat_v07_sin_vecinos():
    src = _fuente()
    # la global sigue funcionando para laterales sin vecinos informados
    assert "altura_vecinos_m" in src
    assert "modo v07" in src
    # voladizos SECCION 1.13 se mantienen
    assert "voladizo_frontal" in src


def test_parsear_vecinos_formato_a():
    f = _extraer_funcion("parsear_vecinos_por_lado")
    r = f('{"4": [6.0, 9.0], "5": [6.0]}')
    assert r == {4: [(6.0, None), (9.0, None)], 5: [(6.0, None)]}


def test_parsear_vecinos_formato_b():
    f = _extraer_funcion("parsear_vecinos_por_lado")
    r = f(json.dumps({"lados": [
        {"id": 4, "vecinos": [{"altura_m": 6.0, "longitud_m": 12.0},
                              {"altura_m": 9.0}]},
        {"id": 7, "vecinos": [{"altura_m": 3.0}]}]}))
    assert r[4] == [(6.0, 12.0), (9.0, None)]
    assert r[7] == [(3.0, None)]


def test_parsear_vecinos_invalido():
    f = _extraer_funcion("parsear_vecinos_por_lado")
    assert f(None) == {}
    assert f("no-json") == {}
    assert f("{}") == {}

def test_empate_1_9_c_solo_con_lado_posterior():
    src = _fuente()
    # Anexo 5 SECCION 1.9.c: el empate volumetrico lateral aplica SOLO a
    # predios con lado POSTERIOR; sin el, rige solo la sismica NSR-10 A.6.5
    assert "aplica_empate_lateral" in src
    assert "empate_activo" in src
    assert "posterior" in src.lower()
    assert "solo sismica" in src.lower()
    assert "NORMATIVA v08.1" in src

def test_subsegmentos_recibe_empate_activo():
    src = _fuente()
    assert "empate_activo=True" in src
    assert "if empate_activo:" in src

def test_subversion_interna_en_encabezado():
    src = _fuente()
    assert "SUBVERSIONES INTERNAS" in src
    assert "v08.1" in src
    assert "Regla de versionado" in src
