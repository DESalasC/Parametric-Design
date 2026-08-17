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


def test_salidas_mesh_para_morph_archicad():
    src = _fuente()
    # el Morph de la Live Connection de ArchiCAD requiere Mesh, no Brep
    assert "_brep_a_mesh" in src
    assert "volumenes_principales_mesh" in src
    assert "volumenes_circulacion_mesh" in src
    assert "volumenes_servicios_mesh" in src
    assert "volumenes_nucleo_mesh" in src
    assert "losas_mesh" in src
    assert "CreateFromPlanarBreps" in src
    assert "CreateFromBrep" in src


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
    assert "piezas = env_por_piso[idx_piso]" in src
    assert "fuente_env" in src


def test_normaliza_goo_y_piezas():
    src = _fuente()
    # acepta objetos Goo de Grasshopper (evita 'Type conversion failed')
    assert "_a_curvas" in src
    assert 'getattr(item, "Value", None)' in src
    # acepta curvas Rhino DIRECTAS (una PolylineCurve no tiene .Value)
    assert "isinstance(item, rg.Curve)" in src
    # acepta DataTree de GH
    assert '"Branches"' in src
    # pisos partidos en varias piezas se unen o usan la mayor
    assert "_unir_piezas" in src
    assert "CreateBooleanUnion" in src


def test_exclusion_booleana_real():
    src = _fuente()
    assert "CreateBooleanDifference" in src
    assert "_recortar_huecos" in src
    assert "_excluir_3d" in src
    # regla: nunca entregar geometria intersectante (piso omitido si falla)
    assert "sin geometria intersectante" in src
    assert "n_omitidos" in src


def test_hueco_es_el_bloque_completo():
    src = _fuente()
    # la losa se perfora con el BLOQUE del nucleo (48,6 m2), no con la suma
    # de solidos (39,8 m2): aire interior 8,76 m2 = circulacion interna
    assert "caja_bloque" in src
    assert "cajas_recorte" in src
    assert 'nucleo_info.get("bloque", {})' in src
    assert "aire_interior" in src


def test_nucleo_recentrado_por_piso():
    src = _fuente()
    # el nucleo BUSCA SU POSICION por barrido 3x3 alrededor del centroide de
    # cada piso (el centroide de una L concava puede caer en el codo);
    # si no cabe (>=95% del bloque) el piso se omite
    assert "mejor_pieza" in src
    assert "paso = 0.75" in src
    assert "cajas_piso" in src
    assert "omitidos_detalle" in src
    assert "nucleo no cabe" in src


def test_subversion_en_encabezado():
    src = _fuente()
    # sub-versionado interno: v07.x en el encabezado + mensaje con la
    # subversion en curso (la version general solo cambia con cambios mayores)
    assert "SUBVERSIONES INTERNAS" in src
    assert "v07.10" in src
    assert "VOLUM v07.10 |" in src
    assert "Regla de versionado" in src


def test_recortar_huecos_firma_estable():
    src = _fuente()
    # firma ORIGINAL de 2 retornos (compat GHPython: cualquier copia con la
    # llamada vieja sigue funcionando); el area de diagnostico via global
    assert "def _recortar_huecos(env_crv, cajas, area_losa, hueco_m2):" in src
    assert "perfil, ok = _recortar_huecos" in src
    assert "return None, False" in src
    assert "return perfil, True" in src
    assert "_area_perfil_diagnostico" in src


def test_recorte_intersecta_antes_de_restar():
    src = _fuente()
    # el hueco se construye SIN booleanos: la diferencia devuelve el contorno
    # EXTERIOR + los AGUJEROS (representacion de Rhino de una region con
    # hueco); la losa sale de CreatePlanarBreps([exterior] + agujeros)
    assert "_agujeros_global" in src
    assert "CreatePlanarBreps([perfil] + agujeros" in src
    assert "_motivo_fallo" in src


def test_recorte_mayor_pieza_y_respaldo_3d():
    src = _fuente()
    # la mayor pieza = contorno EXTERIOR; los agujeros van aparte; el volumen
    # principal = EXTRUSION de la losa con hueco; boolean 3D solo respaldo
    assert "Extrusion.Create(losa_hueco, h_piso)" in src
    assert "_excluir_3d" in src
    assert "losa-anillo" in src


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

def test_mensaje_con_contadores_de_salidas():
    src = _fuente()
    # diagnostico: contadores de salidas REALES (vol/losas/circ/serv) en el
    # mensaje OK, para distinguir fallo de generacion vs fallo de contador
    assert "salidas: vol" in src
    assert "len(volumenes_principales)" in src
    assert "len(losas)" in src
    assert "len(volumenes_circulacion)" in src
    assert "len(volumenes_servicios)" in src

def test_else_omitidos_captura_fallo_de_losa():
    src = _fuente()
    # FIX piso fantasma: 3 ifs ok encadenados con UN else final -> si la losa
    # o el volumen fallan, el piso SE OMITE (nunca llega sin generar ni omitir)
    assert src.count("if ok:") >= 3
    assert "candidatos = [agujeros]" in src
    assert "pieza_encogida" in src
    assert "CurveOffsetCornerStyle.Sharp" in src
    assert "n_omitidos += 1" in src

def test_interruptor_salida_morph():
    src = _fuente()
    # v07.9: interruptor de salida Morph/Mesh
    assert "salida_morph" in src
    assert "volumenes_principales = list(volumenes_principales_mesh)" in src
    assert "volumenes_circulacion = list(volumenes_circulacion_mesh)" in src
    assert "losas = list(losas_mesh)" in src
    assert "MORPH (mesh)" in src

def test_respaldo_3d_con_pieza_encogida():
    src = _fuente()
    # v07.10: el respaldo 3D resta la pieza ENCOGIDA 2 cm (evita la tangencia
    # del hueco contra la pared del volumen -> boolean 3D None/multipieza)
    assert "pieza_resta" in src
    assert "pieza_nucleo.Offset(" in src
    assert "-0.02" in src
    assert "CurveOffsetCornerStyle.Sharp" in src
