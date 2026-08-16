# -*- coding: utf-8 -*-
"""Guardian de regresion para F3_VOLUM_GENERADOR_v07.py.

Valida desde el fuente las correcciones 2026-08-16:
  1) perimetro = envelope_curve de F1_ETAPA2_NORMATIVA_v06 (ocupacion),
  2) exclusion real del nucleo por boolean (nunca geometria intersectante),
  3) circulacion vertical SEPARADA de servicios/areas tecnicas,
  4) destino ArchiCAD (Live Connection, Morphs nativos) y compatibilidad
     IronPython 2.7 (sin f-strings, sin shebang, sin type hints).
"""

import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-3-masa", "F3_VOLUM_GENERADOR_v07.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def test_salidas_circulacion_y_servicios_separadas():
    src = _fuente()
    assert "volumenes_circulacion" in src
    assert "volumenes_servicios" in src
    assert "volumenes_principales" in src
    # compat v06: nucleo = circulacion + servicios (nunca intersectante)
    assert "volumenes_nucleo = list(volumenes_circulacion) + list(volumenes_servicios)" in src


def test_perimetro_desde_normativa_v07():
    src = _fuente()
    # Entrada preferida: envelope_por_piso (lista, escalonada + voladizos)
    assert "envelope_por_piso" in src
    assert "NORMATIVA_v07" in src
    # Fallback v06: envelope_curve unica (compat)
    assert "envelope_curve" in src
    assert "fallback" in src.lower()


def test_resolucion_json_robusta():
    src = _fuente()
    assert "_resolver_json" in src
    assert "D:\\Work\\PROJECTS\\DiseñoParametrico" in src or "D:\\Work\\PROJECTS" in src
    # el mensaje de error distingue la causa (curva vs json_path)
    assert "sin curva de envelope" in src
    assert "json_path invalido" in src


def test_usa_curva_por_piso():
    src = _fuente()
    # cada piso usa su curva (escalonamiento + voladizo reales)
    assert "crv_piso = env_por_piso[idx_piso]" in src
    assert "fuente_env" in src


def test_exclusion_booleana_real():
    src = _fuente()
    assert "CreateBooleanDifference" in src
    assert "_recortar_huecos" in src
    assert "_excluir_3d" in src
    # regla: nunca entregar geometria intersectante (piso omitido si falla)
    assert "sin geometria intersectante" in src
    assert "n_omitidos" in src


def test_destino_archicad_live_connection():
    src = _fuente()
    assert "Live Connection" in src
    assert "MORPHS NATIVOS de ArchiCAD" in src


def test_ironpython_27_compatible():
    src = _fuente()
    assert 'f"' not in src.replace('"""', "")  # sin f-strings fuera de docstrings
    assert not src.lstrip().startswith("#!")
    # sin type hints en las firmas de funciones
    assert "def _caja_curva(cx, cy, ancho, largo):" in src
    assert "def _recortar_huecos(env_crv, cajas, area_losa, hueco_m2):" in src
