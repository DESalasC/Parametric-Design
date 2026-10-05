# -*- coding: utf-8 -*-
"""F3_DISTRIBUCION_v03.1: fix IronPython 2.7 + sección GH (simulada).

Simula el entorno Grasshopper (módulo ghenv falso + variables inyectadas)
para verificar que la sección GH:
  - compila en Python 3 sin anotaciones py3 (fix del SyntaxError de IronPython),
  - lee entradas con los nombres reales del componente (snake_case o guiones),
  - cae al fallback por índice (ghenv) cuando el nombre no está en globals,
  - deriva presupuesto = lote × io_max (con margen) cuando no está cableado,
  - publica las 7 salidas, y barras_json es consumible por NORMATIVA v09
    (schema f3_barras_salida_v01 + campos del validador).
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


def _ejecutar_como_gh(vars_gh, inputs_idx=None, n_inputs=11):
    """Ejecuta F3_DISTRIBUCION_v03.py simulando GHPython + ghenv."""
    inputs = [[] for _ in range(n_inputs)]
    if inputs_idx:
        for i, v in inputs_idx.items():
            inputs[i] = v if isinstance(v, (list, tuple)) else [v]
    ghenv = types.ModuleType("ghenv")
    ghenv.Component = _Component(inputs)
    sys.modules["ghenv"] = ghenv
    try:
        ns = {"__name__": "gh_sim", "__file__": F3_PATH}
        ns.update(vars_gh or {})
        code = _leer_fuente()
        exec(compile(code, F3_PATH, "exec"), ns)
        return ns
    finally:
        del sys.modules["ghenv"]


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
    # Ninguna FIRMA de función (línea que empieza con 'def ') puede llevar
    # anotaciones de tipo Python 3 ('x: str', '-> str'): IronPython 2.7 no las
    # soporta y provocan SyntaxErrorException en el componente GHPython.
    for linea in txt.splitlines():
        ls = linea.lstrip()
        if ls.startswith("def "):
            assert ": str" not in ls, ls
            assert "->" not in ls, ls


def test_seccion_gh_presente():
    txt = _leer_fuente()
    for marcador in ("SECCIÓN GRASSHOPPER", "v03.1", "def _gh_leer",
                     "def _gh_input_idx", "MARGEN_DERIVACION_PCT",
                     "barras_json = json.dumps"):
        assert marcador in txt, marcador


# ------------------------------------------------------------------ GH sim
def test_gh_presupuesto_cableado():
    """Con presupuesto explícito: salidas completas y JSON válido."""
    ns = _ejecutar_como_gh({
        "chip": "AAA0030JKOE",
        "presupuesto_ocupacion_m2": 662.44,
        "n_barras_objetivo": "2,3",
    })
    out = _salidas(ns)
    assert out["mensaje"].startswith("F3 v03.1")
    assert "ERROR" not in out["mensaje"]
    data, alt = _validar_barras_json(out["barras_json"])
    assert data["chip"] == "AAA0030JKOE"
    assert alt["ocupacion_total_m2"] <= 662.44 + 1e-6
    assert out["alternativa_recomendada"] == data["recomendada"]
    assert out["n_barras_usado"] in (2, 3)
    assert out["floor_h_usado"] in (3.05, 3.80)
    assert abs(out["gfa_real_m2"] - alt["gfa_real_m2"]) < 1e-6


def test_gh_presupuesto_derivado_con_margen():
    """Sin presupuesto: se deriva lote×IO - margen y queda por debajo del
    presupuesto normativo esperado (662.44 de NORMATIVA para el caso B)."""
    ns = _ejecutar_como_gh({"chip": "AAA0030JKOE"})
    out = _salidas(ns)
    assert "derivado" in out["mensaje"]
    _, alt = _validar_barras_json(out["barras_json"])
    # lote F2 = 946.45; IO 0.70 -> base 662.515; margen 0.6625 -> 661.852
    assert alt["ocupacion_total_m2"] <= 662.44, "el derivado debe caber en el presupuesto de NORMATIVA"
    assert alt["ocupacion_total_m2"] > 655.0


def test_gh_nombres_con_guion():
    """Acepta los nombres antiguos con guion (normalización "-" ↔ "_")."""
    ns = _ejecutar_como_gh({
        "chip": "AAA0030JKOE",
        "presupuesto-ocupacion": 662.44,
        "n-barras": "3",
    })
    out = _salidas(ns)
    assert "ERROR" not in out["mensaje"]
    _, alt = _validar_barras_json(out["barras_json"])
    assert alt["n_barras"] == 3
    assert out["n_barras_usado"] == 3


def test_gh_fallback_por_indice():
    """Si los nombres no están en globals(), lee por índice vía ghenv."""
    ns = _ejecutar_como_gh(
        {},  # sin variables inyectadas
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
    """Aun sin ejecución GH válida, las 7 salidas existen (no NameError)."""
    for k in ("barras_json", "mensaje", "alternativa_recomendada",
              "ocupacion_total_m2", "gfa_real_m2", "floor_h_usado", "n_barras_usado"):
        ns = _ejecutar_como_gh({})
        assert k in ns
