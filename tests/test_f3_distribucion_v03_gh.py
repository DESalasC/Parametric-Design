# -*- coding: utf-8 -*-
"""F3_DISTRIBUCION_v03.6: sección GH simulada + generador crujía única (F1).

Simula el entorno Grasshopper (ghenv INYECTADO como variable — como en
Rhino 8 real — y opcionalmente como módulo importable) para verificar que la
sección GH y el generador v03.6:
  - compilan en Python 3 sin anotaciones py3 (IronPython-safe),
  - detectan el entorno GH aunque `import ghenv` falle,
  - leen entradas con los nombres reales del componente (snake_case o guiones),
  - EXIGEN base_normativa_json (no se permiten dimensiones ni pisos fijos),
  - aplican cap de crujía (crujia_max_m), suben n automáticamente y mantienen
    el ANCHO COMPLETO (sin reducción centrada — sin huecos laterales),
  - publican las 7 salidas y barras_json es consumible por NORMATIVA v09.
"""
import io
import json
import os
import sys
import types

SRC = os.path.join(os.path.dirname(__file__), "..", "src", "fase-3-masa")
sys.path.insert(0, SRC)

F3_PATH = os.path.join(SRC, "F3_DISTRIBUCION_v03.py")


def _leer_fuente():
    return io.open(F3_PATH, "r", encoding="utf-8").read()


def _base_fixture(presupuesto=662.44, lote=950.0, floor_h=3.0, pisos=5,
                  retiro_f=0.0, retiro_p=0.0, retiro_l=0.0):
    """Base normativa de prueba: rectángulo 25x38 (950 m²) en marco identidad."""
    base = {
        "schema": "base_normativa_predio_v1",
        "area_lote_m2": lote,
        "presupuesto_ocupacion_m2": presupuesto,
        "io_max": 0.70,
        "pisos_limite": pisos,
        "floor_h": floor_h,
        "gfa_techo_geometrico_m2": presupuesto * pisos,
        "frente_m": 25.0,
        "fondo_m": 38.0,
        "poligono_local": [[0.0, 0.0], [25.0, 0.0], [25.0, 38.0], [0.0, 38.0]],
        "marco": {"origen": [0.0, 0.0], "x": [1.0, 0.0], "y": [0.0, 1.0]},
        "retiro_frontal_m": retiro_f,
        "retiro_posterior_m": retiro_p,
        "retiro_lateral_m": retiro_l,
        "warnings": [],
        "bloqueos": [],
    }
    return json.dumps(base, ensure_ascii=True)


class _Goo(object):
    def __init__(self, v):
        self.Value = v


class _Tree(object):
    def __init__(self, vals):
        self._vals = vals

    def AllData(self, skip_nulls):
        return [_Goo(v) for v in self._vals]


class _Param(object):
    def __init__(self, vals):
        self.VolatileData = _Tree(vals)


class _Params(object):
    def __init__(self, inputs):
        self.Input = [_Param(v) for v in inputs]


class _Component(object):
    def __init__(self, inputs):
        self.Params = _Params(inputs)


def _ejecutar_como_gh(vars_gh, inputs_idx=None, n_inputs=13, via_modulo=False,
                      sin_ghenv=False, nombre="gh_sim"):
    """Ejecuta F3_DISTRIBUCION_v03.py simulando GHPython + ghenv."""
    inputs = [[] for _ in range(n_inputs)]
    if inputs_idx:
        for i, v in inputs_idx.items():
            inputs[i] = v if isinstance(v, (list, tuple)) else [v]
    ghenv = types.ModuleType("ghenv")
    ghenv.Component = _Component(inputs)
    sys.modules.pop("ghenv", None)
    ns = {"__name__": nombre, "__file__": F3_PATH}
    ns.update(vars_gh or {})
    if sin_ghenv:
        pass
    elif via_modulo:
        sys.modules["ghenv"] = ghenv
    else:
        ns["ghenv"] = ghenv
    try:
        code = _leer_fuente()
        exec(compile(code, F3_PATH, "exec"), ns)
        return ns
    finally:
        sys.modules.pop("ghenv", None)


def _salidas(ns):
    return {
        "barras_json": ns.get("barras_json"),
        "mensaje": ns.get("mensaje"),
        "alternativa_recomendada": ns.get("alternativa_recomendada"),
        "ocupacion_total_m2": ns.get("ocupacion_total_m2"),
        "gfa_real_m2": ns.get("gfa_real_m2"),
        "floor_h_usado": ns.get("floor_h_usado"),
        "n_barras_usado": ns.get("n_barras_usado"),
    }


def _vars_b(**kw):
    """Chip B + base normativa + kwargs extra (por encima)."""
    v = {"chip": "AAA0030JKOE", "base_normativa_json": _base_fixture()}
    v.update(kw)
    return v


def _validar_barras_json(txt, chip="AAA0030JKOE"):
    """Réplica de las exigencias de NORMATIVA v09.parsear_barras_json."""
    data = json.loads(txt)
    assert data["schema"] == "f3_barras_salida_v01"
    rec = data["recomendada"]
    assert rec
    alt = next(a for a in data["alternativas"] if a["id"] == rec)
    for campo in ("ocupacion_total_m2", "gfa_real_m2", "huellas_por_piso",
                  "altura_total_m", "floor_h"):
        assert alt.get(campo) is not None, campo
    assert alt["ocupacion_total_m2"] > 0 and alt["gfa_real_m2"] > 0
    assert len(alt["huellas_por_piso"]) >= 1
    return data, alt


# ------------------------------------------------------------------ estáticos
def test_sin_anotaciones_python3():
    """El fix del SyntaxError de IronPython: sin anotaciones en firmas."""
    txt = _leer_fuente()
    assert "def normalizar_uso(uso):" in txt
    for linea in txt.splitlines():
        ls = linea.lstrip()
        if ls.startswith("def "):
            assert ": str" not in ls, ls
            assert "->" not in ls, ls


def test_seccion_gh_presente():
    txt = _leer_fuente()
    for marcador in ("SECCIÓN GRASSHOPPER", "v03.8", "def _gh_leer",
                     "def _gh_modulo", "def _gh_input_idx",
                     "def _leer_json", "def _texto_seguro",
                     "def _json_dumps_ascii", "def _json_manual_ascii",
                     "MARGEN_DERIVACION_PCT", "barras_json = _json_dumps_ascii",
                     "v03.6", "CRUJIA_MAX_M_DEF", "def _clip_rect"):
        assert marcador in txt, marcador


def test_json_dumps_ascii_roundtrip():
    ns = _ejecutar_como_gh({})
    d = ns["_json_dumps_ascii"]({
        "mensaje": u"2 barras crujía única",
        "n": [1, 2.5, True, None],
        "nested": [[0.0, 661.85]],
    })
    assert isinstance(d, str)
    assert all(ord(c) < 128 for c in d), d[:80]
    back = json.loads(d)
    assert back["mensaje"] == u"2 barras crujía única"
    assert back["n"] == [1, 2.5, True, None]
    assert back["nested"] == [[0.0, 661.85]]


def test_json_manual_ascii_roundtrip():
    ns = _ejecutar_como_gh({})
    d = ns["_json_manual_ascii"]({u"crujía": u"ocupación 661,85 m²", u"k": [1, 2.0]})
    assert all(ord(c) < 128 for c in d), d
    back = json.loads(d)
    assert back[u"crujía"] == u"ocupación 661,85 m²"
    assert back[u"k"] == [1, 2.0]


def test_clip_rect_puro():
    """El recorte Sutherland-Hodgman funciona sin Rhino."""
    ns = _ejecutar_como_gh({})
    clip = ns["_clip_rect"]
    cuadro = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
    # recorte central
    pts = clip(cuadro, 2.0, 2.0, 8.0, 8.0)
    assert abs(ns["_area_pts"](pts) - 36.0) < 1e-9
    # recorte fuera → vacío
    assert clip(cuadro, 20.0, 20.0, 30.0, 30.0) == []
    # triángulo con rect que lo deja totalmente contenido
    tri = [(0.0, 0.0), (10.0, 0.0), (0.0, 10.0)]
    pts2 = clip(tri, 0.0, 0.0, 5.0, 5.0)
    assert abs(ns["_area_pts"](pts2) - 25.0) < 1e-9  # cuadrado ⊂ triángulo


# ------------------------------------------------------------------ GH sim
def test_gh_real_variable_no_import():
    """Regresión: en GHPython ghenv es VARIABLE inyectada; main() NO corre."""
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44),
                           nombre="__main__")
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"], out["mensaje"]
    assert out["mensaje"].startswith("F3 v03.8")
    _validar_barras_json(out["barras_json"])


def test_leer_json_con_acentos(tmp_path):
    ns = _ejecutar_como_gh({})
    p = tmp_path / "t.json"
    p.write_text(u'{"mensaje": "crujía, ocupación y diseño"}', encoding="utf-8")
    data = ns["_leer_json"](str(p))
    assert data["mensaje"] == u"crujía, ocupación y diseño"


def test_error_muestra_paso():
    ns = _ejecutar_como_gh({"chip": "ZZZZZZ"})
    msg = ns.get("mensaje") or ""
    assert "ERROR en [leer resultados F2]" in msg, msg
    assert "Sin resultados" in msg, msg


def test_gh_via_modulo_import_fallback():
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44),
                           via_modulo=True)
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"], out["mensaje"]
    _validar_barras_json(out["barras_json"])


def test_aviso_entorno_rhino_sin_ghenv(monkeypatch):
    import platform as _pl
    monkeypatch.setattr(_pl, "python_implementation", lambda: "IronPython")
    ns = _ejecutar_como_gh({}, sin_ghenv=True, nombre="__main__")
    assert "aviso" in (ns.get("mensaje") or "")


def test_gh_sin_base_normativa_reporta():
    """Sin base_normativa_json el generador v03.6 no adivina: error claro."""
    ns = _ejecutar_como_gh({"chip": "AAA0030JKOE",
                            "presupuesto_ocupacion_m2": 662.44})
    out = _salidas(ns)
    assert out["barras_json"] == ""
    assert "base_normativa_json" in (out["mensaje"] or "")
    assert "ERROR" in out["mensaje"]


# ------------------------------------------------------------------ generador
def test_gh_presupuesto_cableado():
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44,
                                   n_barras_objetivo="2,3"))
    out = _salidas(ns)
    assert out["mensaje"].startswith("F3 v03.8")
    assert "ERROR" not in out["mensaje"]
    data, alt = _validar_barras_json(out["barras_json"])
    assert data["chip"] == "AAA0030JKOE"
    assert alt["ocupacion_total_m2"] <= 662.44 + 1e-6
    assert out["alternativa_recomendada"] == data["recomendada"]
    # v03.6: n auto (2→3 por cap de crujía) y ancho COMPLETO (25 m)
    assert out["n_barras_usado"] == 3
    assert alt["n_barras"] == 3
    assert out["floor_h_usado"] == 3.0
    assert abs(out["gfa_real_m2"] - alt["gfa_real_m2"]) < 1e-6
    assert alt["profundidad_m"] <= alt["crujia_max_m"] + 1e-9
    assert abs(alt["ancho_barra_m"] - 25.0) < 1e-6


def test_crujia_cap_auto_n_ancho_completo():
    """n pedido 2 → auto 3; franjas de lado a lado (sin huecos laterales)."""
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44,
                                   n_barras_objetivo="2"))
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"]
    data, alt = _validar_barras_json(out["barras_json"])
    assert alt["n_pedido"] == 2
    assert alt["n_barras"] == 3
    assert any("n 2 -> 3" in a for a in alt["avisos"])
    assert alt["profundidad_m"] <= 10.0 + 1e-9
    assert len(alt["bloques"]) == 3
    for blk in alt["bloques"]:
        pts = blk["huella_xy"]
        assert len(pts) >= 4
        assert pts[0] == pts[-1]  # CERRADA (contrato #114)
        xs = [p[0] for p in pts]
        assert min(xs) <= 0.03 and max(xs) >= 24.97  # alcanza ambos lados
    assert all((c["izq"] is True and c["der"] is True) for c in alt["alcance_lados"])


def test_gh_presupuesto_derivado_con_margen():
    ns = _ejecutar_como_gh(_vars_b())
    out = _salidas(ns)
    assert "derivado" in out["mensaje"]
    _, alt = _validar_barras_json(out["barras_json"])
    assert alt["ocupacion_total_m2"] <= 662.44
    assert alt["ocupacion_total_m2"] > 600.0


def test_gh_nombres_con_guion():
    ns = _ejecutar_como_gh({
        "chip": "AAA0030JKOE",
        "base_normativa_json": _base_fixture(),
        "presupuesto-ocupacion": 662.44,
        "n-barras": "3",
    })
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"]
    _, alt = _validar_barras_json(out["barras_json"])
    assert alt["n_barras"] == 3
    assert out["n_barras_usado"] == 3


def test_gh_fallback_por_indice():
    ns = _ejecutar_como_gh(
        {"base_normativa_json": _base_fixture()},
        inputs_idx={0: "AAA0030JKOE", 1: 662.44, 3: [2, 3]},
    )
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"]
    data, alt = _validar_barras_json(out["barras_json"])
    assert data["chip"] == "AAA0030JKOE"


def test_gh_chip_vacio_reporta_error():
    ns = _ejecutar_como_gh({})
    out = _salidas(ns)
    assert out["barras_json"] == ""
    assert "ERROR" in out["mensaje"]
    assert "chip" in out["mensaje"]


def test_gh_salidas_siempre_definidas():
    for k in ("barras_json", "mensaje", "alternativa_recomendada",
              "ocupacion_total_m2", "gfa_real_m2", "floor_h_usado", "n_barras_usado"):
        ns = _ejecutar_como_gh({})
        assert k in ns


def test_v037_anclaje_y_pisos_por_bloque():
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44,
                                   pisos_por_bloque="4,4,6"))
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"], out["mensaje"]
    data, alt = _validar_barras_json(out["barras_json"])
    assert alt["anclaje_frentes"] is True
    ys0 = [p[1] for p in alt["bloques"][0]["huella_xy"]]
    ysL = [p[1] for p in alt["bloques"][-1]["huella_xy"]]
    assert min(ys0) <= 0.03     # frente anclado al limite
    assert max(ysL) >= 37.97    # fondo anclado al limite
    assert alt["pisos_por_bloque"] == [4, 4, 6]
    assert len(alt["huellas_por_piso"]) == 14
    assert alt["separacion_min_m"] == 6.0


def test_v037_bandas_redistribucion():
    lim = json.dumps({"bandas": [{"hasta_m": 15.0, "max_pisos": 4}],
                      "redistribuir_ultimo": True})
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44,
                                   limites_pisos_json=lim))
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"], out["mensaje"]
    data, alt = _validar_barras_json(out["barras_json"])
    assert alt["pisos_por_bloque"] == [4, 4, 7]
    assert any("redistribucion" in a for a in alt["avisos"])


def test_v038_escalonamiento_lateral_1_5():
    sep = json.dumps({"lado": "xmax", "h_vecino_m": 6.0,
                      "min_retiro_m": 0.0, "nsr_coef": 0.02})
    ns = _ejecutar_como_gh(_vars_b(presupuesto_ocupacion_m2=662.44,
                                   sep_lateral_json=sep))
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"], out["mensaje"]
    assert out["mensaje"].startswith("F3 v03.8")
    data, alt = _validar_barras_json(out["barras_json"])
    blk = alt["bloques"][0]
    ret = blk["retiros_por_piso_m"]
    assert ret == [0.0, 0.0, 0.6, 1.2, 1.8]  # floor_h=3, vecino 6 m (1/5)
    xs0 = [p[0] for p in blk["huella_xy_por_piso"][0]]
    xs2 = [p[0] for p in blk["huella_xy_por_piso"][2]]
    assert abs(max(xs0) - 25.0) < 1e-6
    assert abs(max(xs2) - 24.4) < 1e-6
    assert any("escalonamiento" in a for a in alt["avisos"])
