# -*- coding: utf-8 -*-
"""
F3_PRUEBA_MASA_A_rhino.py — Prueba REAL de F3_VOLUM_GENERADOR_v05 dentro de Rhino 8.

Ejecucion (Rhino abre su ventana y se cierra solo):
  "C:\Program Files\Rhino 8\System\Rhino.exe" /nosplash /runscript="_-RunPythonScript D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_PRUEBA_MASA_A_rhino.py"

Inyecta las mismas entradas que Grasshopper (envelope_curve <- vertice del lote del
contexto F1; json_path <- programa-areas.json del caso A; floor_height <- 3.0),
ejecuta el cuerpo del v05 tal cual y guarda:
  - casos/A/F3_A_masa_rhino.3dm   (losas + volumenes principales + nucleo, por capas)
  - casos/A/f3_prueba_rhino.log   (mensaje, etiquetas, conteos, volumen)
"""
import io
import json
import os

import scriptcontext as sc  # noqa: F401
import Rhino  # noqa: F401
import rhinoscriptsyntax as rs  # noqa: F401

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, "..", ".."))
CASO = os.path.join(BASE, "casos", "A")
LOG = os.path.join(CASO, "f3_prueba_rhino.log")


def log(linea):
    with io.open(LOG, "a", encoding="utf-8") as f:
        f.write(linea + "\n")


def run():
    if os.path.exists(LOG):
        os.remove(LOG)
    doc = sc.doc

    # 1. Envelope curve desde el lote objetivo (contexto F1)
    with io.open(os.path.join(ROOT, "data", "pot-cache", "AAA0127AZPA-contexto.json"),
                 encoding="utf-8") as f:
        ctx = json.load(f)
    verts = [tuple(v[:2]) for v in ctx["lote_objetivo"]["vertices_3d_local"]]
    pts = [Rhino.Geometry.Point3d(x, y, 0.0) for x, y in verts]
    pts.append(pts[0])
    envelope_curve = Rhino.Geometry.PolylineCurve(pts)

    def AreaPoly(vs):
        return sum(vs[i][0] * vs[(i + 1) % len(vs)][1] - vs[(i + 1) % len(vs)][0] * vs[i][1]
                   for i in range(len(vs))) / 2.0

    # 2. Entradas iguales a Grasshopper
    json_path = os.path.join(CASO, "programa-areas.json")
    floor_height = 3.0
    g = globals()
    g["envelope_curve"] = envelope_curve
    g["json_path"] = json_path
    g["floor_height"] = floor_height

    # 3. Ejecutar el cuerpo del v06 (Rhino.Geometry completo)
    src = io.open(os.path.join(BASE, "F3_VOLUM_GENERADOR_v06.py"),
                  encoding="utf-8").read()
    # En IronPython, el 'import ... as rg' dentro de exec no resuelve bien:
    # se inyecta rg directamente y se retira la linea de import del fuente.
    g["rg"] = Rhino.Geometry
    g["json"] = json
    g["math"] = __import__("math")
    src = src.replace("import Rhino.Geometry as rg\n", "")
    exec(compile(src, "F3_VOLUM_GENERADOR_v06.py", "exec"), g)

    mensaje = g.get("mensaje", "?")
    losas = g.get("losas", [])
    vol_princ = g.get("volumenes_principales", [])
    vol_nuc = g.get("volumenes_nucleo", [])
    etiquetas = g.get("etiquetas", [])

    log("MENSAJE: " + mensaje)
    log("Losas: {} | Vol. principales: {} | Vol. nucleo: {}".format(
        len(losas), len(vol_princ), len(vol_nuc)))
    for e in etiquetas:
        log("  " + e)

    # 4. Agregar al documento por capas (Layers.Add espera objeto Layer en Rhino 8)
    def add_layer(nombre):
        layer = Rhino.DocObjects.Layer()
        layer.Name = nombre
        return doc.Layers.Add(layer)

    try:
        for i, b in enumerate(losas):
            add_layer("LOSA_{}".format(i + 1))
            doc.Objects.AddBrep(b)
        for i, b in enumerate(vol_princ):
            add_layer("VOL_PRINCIPAL_{}".format(i + 1))
            doc.Objects.AddBrep(b)
        for i, b in enumerate(vol_nuc):
            add_layer("VOL_NUCLEO_{}".format(i + 1))
            doc.Objects.AddBrep(b)
        log("Objetos agregados al documento: {}".format(
            len(losas) + len(vol_princ) + len(vol_nuc)))
    except Exception as e:
        log("ERROR agregando objetos: {}".format(e))

    # 5. Guardar .3dm y log de volumen
    try:
        out = os.path.join(CASO, "F3_A_masa_rhino.3dm")
        ok = doc.SaveAs(out)
        log("SAVE: {} -> {}".format(out, "OK" if ok else "ERROR"))
    except Exception as e:
        log("ERROR SaveAs: {}".format(e))

    vol_total = sum(b.GetVolume() for b in vol_princ) + sum(b.GetVolume() for b in vol_nuc)
    with io.open(json_path, encoding="utf-8") as f:
        prog = json.load(f)
    alt = sum(float(p.get("altura_piso", 3.0)) for p in prog["programa_pisos"])
    area_env = abs(AreaPoly(verts))  # huella real usada en la prueba
    log("Volumen total: {:.1f} m3 | esperado envelope x alturas: {:.1f} m3 | desv {:.1f}%".format(
        vol_total, area_env * alt,
        100 * abs(vol_total - area_env * alt) / (area_env * alt)))
    log("Nota: la masa usa la huella real ({} m2); el GFA del layout ({} m2) corresponde a la "
        "ocupacion POT aplicada en F1 (envelope con retiros).".format(area_env, prog["gfa_total"]))
    log("DONE")

    # Cerrar esta instancia de Rhino (solo la lanzada por la prueba)
    doc.Close(False)
    Rhino.Application.Exit()


if __name__ == "__main__":
    run()
