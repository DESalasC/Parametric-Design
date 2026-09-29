# -*- coding: utf-8 -*-
"""Tests de lógica para F1_ETAPA3_CONTEXTO50 (contraparte GH del builder).

Ejecuta el script con los stubs de Rhino del arnés del builder y verifica
paridad de resultados (exclusiones predio/menores), orientación antihoraria,
resolución defensiva del template y compatibilidad IronPython 2.7.
Corre en CPython (no requiere Rhino ni Grasshopper).
"""

import io
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(__file__))
from test_contexto50_build import (  # noqa: E402
    JSON_BASE_REAL,
    JSON_REAL,
    _ejecutar_componente,
    _fixture_dir,
)

SRC_ETAPA3 = os.path.join(
    os.path.dirname(__file__), "..", "F1_ETAPA3_CONTEXTO50_v01.1.py"
)


def _ejecutar_etapa3(json_path):
    return _ejecutar_componente(json_path, src=SRC_ETAPA3)


def test_paridad_conteos_con_hermano():
    """Mismos números que el builder: 66/94 volúmenes; 4 predio; 24 menores."""
    d = _fixture_dir(con_hermano=True)
    ns = _ejecutar_etapa3(os.path.join(d, "AAA0240ZXJH-contexto50.json"))
    assert len(ns["volumenes"]) == 66
    assert len(ns["huellas_curvas"]) == 66
    assert "Edificios 66/94" in ns["mensaje"]
    assert "Excluidos: 4 predio objetivo, 24 andenes/menores" in ns["mensaje"]
    assert ns["ok"] is True
    assert '"excluidos_predio": 4' in ns["stats_json"]


def test_sin_hermano_no_excluye_predio():
    d = _fixture_dir(con_hermano=False)
    ns = _ejecutar_etapa3(os.path.join(d, "AAA0240ZXJH-contexto50.json"))
    assert len(ns["volumenes"]) == 68  # 94 - 26 menores
    assert "sin CHIP-contexto.json" in ns["mensaje"]


def test_anillo_horario_se_invierte_a_antihorario():
    """Anillos horarios del fetch GIS deben salir CCW (extrusión +Z)."""
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    ed = data["edificios"][0]
    data["edificios"] = [ed]
    tmp = os.path.join(tempfile.mkdtemp(prefix="dp_et3_orient_"),
                       "AAA0240ZXJH-contexto50.json")
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    ns = _ejecutar_etapa3(tmp)
    assert len(ns["huellas_curvas"]) == 1
    p3 = ns["huellas_curvas"][0].pts
    u = p3[:-1]
    s2 = 0.0
    n2 = len(u)
    for i in range(n2):
        x1, y1 = u[i][0], u[i][1]
        x2, y2 = u[(i + 1) % n2][0], u[(i + 1) % n2][1]
        s2 += x1 * y2 - x2 * y1
    assert s2 > 0, "la huella debe quedar antihoraria (normal +Z)"


def test_defensiva_template_resuelve_chip():
    """Path con template CHIP-contexto50.json -> resuelve el <CHIP>-contexto50.json."""
    d = _fixture_dir(con_hermano=True)
    shutil.copy2(JSON_BASE_REAL, os.path.join(d, "AAA0240ZXJH-contexto.json"))
    ns = _ejecutar_etapa3(os.path.join(d, "CHIP-contexto50.json"))
    assert len(ns["volumenes"]) == 66
    assert "Edificios 66/94" in ns["mensaje"]


def test_ironpython_27_compatible():
    """Sin f-strings ni walrus (IronPython 2.7)."""
    with io.open(SRC_ETAPA3, "rb") as f:
        fuente = f.read().decode("utf-8")
    assert "f'" not in fuente and 'f"' not in fuente
    assert ":=" not in fuente
