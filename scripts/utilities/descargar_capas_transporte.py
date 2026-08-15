# -*- coding: utf-8 -*-
"""
================================================================================
descargar_capas_transporte.py — Descarga capas de transporte publico (Bogota)
Proyecto: DisenoParametrico / Fase 2 (N3 accesibilidad)
Python 3.8+ (requests)
================================================================================

Descarga las capas oficiales de transporte publico usadas para materializar el
nivel N3 (lejano-accesibilidad) del alcance de investigacion:

  - estaciones_tm.geojson   : 153 estaciones troncales TransMilenio (GeoJSON)
                              Fuente: TransMilenio S.A. / Datos Abiertos Bogota
                              https://datosabiertos.bogota.gov.co/dataset/estaciones-troncales-de-transmilenio
  - paraderos_sitp.geojson  : Paraderos SITP (GeoJSON)
                              Fuente: Secretaria Distrital de Movilidad
                              https://datos-abiertos-sdm-movilidadbogota.hub.arcgis.com/datasets/0df9f176a6ba4da89db428990fd9bc8b_0
  - trazados_tm.geojson     : 20 trazados (corredores) troncales TransMilenio
                              Fuente: TransMilenio S.A. / Datos Abiertos Bogota
                              https://datosabiertos.bogota.gov.co/dataset/trazados-troncales-de-transmilenio

GTFS completo (horarios/rutas): PENDIENTE de descarga manual (zip grande en
datosabiertos.bogota.gov.co/dataset/especificacion-gtfs-general-transport-feed-specification-sitp
y datos.movilidadbogota.gov.co/datasets/599751603a494051b15ac3d4f1f38ec5). La
isocrona N3 se calcula con metodo de primer orden (velocidad comercial 20 km/h)
hasta que el GTFS se incorpore.

USO:  python scripts/utilities/descargar_capas_transporte.py [--out-dir data/transporte]
"""
import argparse
import json
import os
import requests

URLS = {
    "estaciones_tm.geojson": (
        "https://gis.transmilenio.gov.co/arcgis/rest/services/Troncal/"
        "consulta_estaciones_troncales/MapServer/0/query?where=1%3D1&outFields=*&f=geojson"),
    "trazados_tm.geojson": (
        "https://gis.transmilenio.gov.co/arcgis/rest/services/Troncal/"
        "consulta_trazados_troncales/MapServer/0/query?where=1%3D1&outFields=*&f=geojson"),
    "paraderos_sitp.geojson": (
        "http://datos-abiertos-sdm-movilidadbogota.hub.arcgis.com/datasets/"
        "0df9f176a6ba4da89db428990fd9bc8b_0.geojson"),
}


def main():
    ap = argparse.ArgumentParser(description="Descarga capas de transporte Bogota")
    ap.add_argument("--out-dir", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "transporte"))
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    for name, url in URLS.items():
        try:
            r = requests.get(url, timeout=300)
            r.raise_for_status()
            data = r.json()
            path = os.path.join(args.out_dir, name)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            n = len(data.get("features", []))
            print("OK %s (%d features, %d bytes)" % (name, n, len(r.content)))
        except Exception as e:
            print("ERROR %s: %s" % (name, e))
    print("Listo. Re-ejecutar: python scripts/utilities/alcance_investigacion.py --chip <CHIP>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
