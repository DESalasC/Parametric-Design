# -*- coding: utf-8 -*-
"""
================================================================================
alcance_investigacion.py — Areas de influencia multi-nivel (Fase 2)
Proyecto: DisenoParametrico / Fase 2
Python 3.8+ Standalone (sin dependencias externas)
================================================================================

OBJETIVO:
  Definir y materializar las areas de influencia del estudio de demanda para un
  lote dado:

    N1-CERCANO            : radio 2.000 m  (vecindario directo)
    N2-INTERMEDIO         : radio 5.000 m  (area de mercado actual)
    N3-LEJANO-ACCESIBILIDAD: sin radio fijo; criterios de accesibilidad:
                             estaciones TransMilenio / paraderos SITP a < 500 m
                             del lote, e isocrona de 20 minutos en transporte
                             publico (preferencias sobre rutas principales de
                             transporte publico y privado).

USO:
  python alcance_investigacion.py --chip AAA0039KRMR [--config <json>]

SALIDAS (exports/alcance/<CHIP>-alcance.json):
  - Anillos N1/N2 (circulo SIRGAS: centro + radio) listos para GIS/Grasshopper.
  - Estado de datos del nivel N3 (malla vial disponible; estaciones/GTFS
    pendientes de capa) y la lista de indicadores a medir en cada nivel.
  - Las consultas de investigacion por nivel (lo que se debe buscar/validar).

NOTA:
  La isocrona de 20 min requiere el GTFS oficial de TransMilenio/SITP; hasta que
  la capa se incorpore, el nivel N3 reporta estado PENDIENTE sin inventar datos.
================================================================================
"""

import argparse
import io
import json
import math
import os

DEFAULT_CONFIG = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..",
    "data", "fase-2-demanda", "alcance-investigacion.json")
POT_CACHE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "pot-cache")
OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..",
    "exports", "alcance")


def _cargar(path):
    with io.open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def circulo(origen_x, origen_y, radio_m, pasos=48):
    """Poligono del anillo (SIRGAS, metros) para GIS/Grasshopper."""
    pts = []
    for i in range(pasos):
        a = 2.0 * math.pi * i / pasos
        pts.append([round(origen_x + radio_m * math.cos(a), 2),
                    round(origen_y + radio_m * math.sin(a), 2)])
    pts.append(pts[0])
    return pts


def nivel_indicadores(niveles, nid):
    for n in niveles.values():
        if n.get("id") == nid:
            return n
    return None


def construir_alcance(chip, config_path):
    config = _cargar(config_path)
    ctx_path = os.path.join(POT_CACHE, chip + "-contexto.json")
    if not os.path.exists(ctx_path):
        raise SystemExit("Contexto no encontrado: %s" % ctx_path)
    ctx = _cargar(ctx_path)

    origen = ctx["metadata"]["origen_sirgas"]
    ox, oy = float(origen["x"]), float(origen["y"])

    niveles = config["niveles"]
    cercano = nivel_indicadores(niveles, "N1-CERCANO")
    intermedio = nivel_indicadores(niveles, "N2-INTERMEDIO")
    lejano = nivel_indicadores(niveles, "N3-LEJANO-ACCESIBILIDAD")

    vias = ctx.get("vias_oficiales", []) or []
    n_vias = len(vias)
    n_por_fuente = {}
    for v in vias:
        f = v.get("fuente", "?")
        n_por_fuente[f] = n_por_fuente.get(f, 0) + 1

    doc = {
        "chip": chip,
        "origen_sirgas": {"crs": origen["crs"], "x": ox, "y": oy},
        "area_lote_m2": ctx["lote_objetivo"]["area_m2"],
        "niveles": [
            {
                "id": cercano["id"],
                "etiqueta": cercano["etiqueta"],
                "radio_m": cercano["radio_m"],
                "circulo_sirgas": circulo(ox, oy, cercano["radio_m"]),
                "enfoque": cercano["enfoque"],
                "indicadores": cercano["indicadores"],
            },
            {
                "id": intermedio["id"],
                "etiqueta": intermedio["etiqueta"],
                "radio_m": intermedio["radio_m"],
                "circulo_sirgas": circulo(ox, oy, intermedio["radio_m"]),
                "enfoque": intermedio["enfoque"],
                "indicadores": intermedio["indicadores"],
            },
            {
                "id": lejano["id"],
                "etiqueta": lejano["etiqueta"],
                "radio_m": None,
                "criterios": lejano["criterios"],
                "estado_datos": config["estado_datos"],
                "accesibilidad": {
                    "distancia_estacion_tm_m": "PENDIENTE (capa estaciones TransMilenio)",
                    "distancia_paradero_sitp_m": "PENDIENTE (capa paraderos SITP)",
                    "isocrona_20min_tp": "PENDIENTE (GTFS TransMilenio/SITP)",
                    "red_principal_privado": {
                        "malla_vial_disponible": True,
                        "vias_en_contexto_f1": n_vias,
                        "vias_por_fuente": n_por_fuente,
                        "criterio": "Malla vial arterial e intermedia del POT",
                    },
                },
                "enfoque": lejano["enfoque"],
                "indicadores": lejano["indicadores"],
            },
        ],
        "consultas_investigacion": {
            "N1-CERCANO": [
                "Precios y canones de oferta activa a <=2 km (portales: Ciencuadras, FincaRaiz, Properati).",
                "Vacancia y absorcion del sector inmediato.",
                "Equipamientos y usos del primer anillo.",
            ],
            "N2-INTERMEDIO": [
                "Comparables de la UPZ y UPZ vecinas dentro de 5 km.",
                "Oferta nueva en construccion (licencias) en el anillo intermedio.",
                "Tendencia poblacional y capacidad de compra de la zona.",
            ],
            "N3-LEJANO-ACCESIBILIDAD": [
                "Distancia al corredor/estacion TransMilenio mas cercano (<500 m).",
                "Cobertura de paraderos SITP a <500 m.",
                "Isocrona de 20 min en transporte publico (GTFS) -> demanda capturable.",
                "Acceso a la malla vial arterial (transporte privado).",
            ],
        },
        "nota": "Los radios se miden desde el origen SIRGAS del lote. N3 usa accesibilidad en lugar de radio fijo, segun config alcance-investigacion.json.",
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    salida = os.path.join(OUT_DIR, chip + "-alcance.json")
    with io.open(salida, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    return salida, doc


def main():
    ap = argparse.ArgumentParser(description="Areas de influencia multi-nivel")
    ap.add_argument("--chip", required=True, help="CHIP del lote")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    args = ap.parse_args()

    salida, doc = construir_alcance(args.chip, args.config)
    print("OK alcance de investigacion: %s" % salida)
    print("  N1-CERCANO    : radio 2.000 m")
    print("  N2-INTERMEDIO : radio 5.000 m")
    n3 = doc["niveles"][2]
    print("  N3-ACCESIBILIDAD: %s" % n3["accesibilidad"]["distancia_estacion_tm_m"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
