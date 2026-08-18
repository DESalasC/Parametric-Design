# -*- coding: utf-8 -*-
"""
================================================================================
F3_ACCESOS_INTEGRADOR_v02.py - Accesos por uso y segregacion de flujos (Fase 3)
Proyecto: DisenoParametrico / Fase 3
Generador Python (CLI) compatible con IronPython 2.7 (componente "Script"
clasico de Grasshopper, si se cablea como GHPython).
================================================================================

PROPOSITO:
  A partir de los productos REALES de F3 (layout_espacial.json de
  F3_DISTRIBUCION_v01 y matriz_adyacencias.json), determina para CADA USO:
    - los pisos que ocupa (reparto_vertical),
    - el tipo de acceso (directo a fachada para usos publicos en planta baja;
      independiente por nucleo vertical para vivienda/usos privados),
    - el lado de acceso (Frontal por defecto; se puede afinar con sides),
    - el numero de accesos,
  y detecta las PAREJAS INCOMPATIBLES (matriz nivel 0) que exigen accesos
  segregados (NSR-10 Titulo C / POT Decreto 555 de 2021: segregacion de
  flujos residencial/comercial).

  Reemplaza a F3_ACCESOS_INTEGRADOR_v01 (referencia rota a
  OPTIMIZADOR_ADYACENCIA_v01, que no existe, + rs + type hints + f-strings).

NORMATIVA APLICABLE:
  - NSR-10 Titulo C (ocupacion y clasificacion de usos), Titulo K (evacuacion).
  - POT Decreto 555 de 2021 (usos y accesos independientes).

ENTRADAS:
  layout_espacial.json  - reparto_vertical, nucleos, niveles, poblacion_estimada
  matriz_adyacencias.json - usos, matriz (0=Incompatible..3=Requerida), escala
  sides (opcional)      - clasificacion de lados de F1_ETAPA2_LADOS (Frontal/...)

SALIDAS:
  accesos_<id>.json / .txt  - analisis de accesos por uso + segregaciones
  (GH) accesos_json (String), mensaje (String)

USO CLI:
  python F3_ACCESOS_INTEGRADOR_v02.py --caso A
  python F3_ACCESOS_INTEGRADOR_v02.py --layout <layout.json> --matriz <matriz.json>
================================================================================
"""

import json
import io
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
CASOS_DIR = os.path.join(BASE, "casos")

# Categorias de acceso por uso. Los usos PUBLICOS (atencion al publico,
# comercio, salud, educacion) exigen acceso directo desde fachada en planta
# baja. El resto (vivienda y afines) accede por nucleo/hall segregado.
USOS_PUBLICOS = set([
    "comercio", "comercial", "local", "local comercial",
    "salud", "consultorios", "consultorio",
    "institucional", "educacion", "educativo",
    "oficinas", "servicios", "hotel", "parqueadero", "estacionamiento",
])


def _normalizar(uso):
    return (uso or "").strip().lower()


def _categoria(uso):
    return "publico" if _normalizar(uso) in USOS_PUBLICOS else "privado"


def _cargar_json(ruta):
    if not ruta or not os.path.exists(ruta):
        return {}
    try:
        with io.open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _resolver(caso_id):
    """Resuelve las rutas de layout y matriz para un caso (A, B, B_SALUD, C)."""
    carpeta = os.path.join(CASOS_DIR, caso_id)
    layout = os.path.join(carpeta, "layout_espacial.json")
    matriz = os.path.join(carpeta, "matriz_adyacencias.json")
    return layout, matriz, carpeta


def _pisos_de_uso(uso, reparto, niveles):
    if uso in reparto and reparto[uso]:
        return list(reparto[uso])
    out = []
    for n in niveles:
        if uso in n.get("usos", []):
            out.append(n.get("nivel", 0))
    return out


def analizar_accesos(layout, matriz):
    """Calcula el plan de accesos por uso y las segregaciones de flujo.
    Devuelve un dict serializable a JSON."""
    reparto = layout.get("reparto_vertical", {})
    nucleos = layout.get("nucleos", {})
    niveles = layout.get("niveles", [])
    poblacion = layout.get("poblacion_estimada", {})

    usos_canonicos = list(matriz.get("usos", list(reparto.keys())))
    m = matriz.get("matriz", {})

    accesos = []
    for uso in usos_canonicos:
        pisos = _pisos_de_uso(uso, reparto, niveles)
        categoria = _categoria(uso)
        planta_baja = (1 in pisos)
        if categoria == "publico" and planta_baja:
            tipo = "directo_fachada"
            lado = "Frontal"
            n_accesos = 1
        else:
            tipo = "independiente_nucleo"
            lado = "Frontal" if planta_baja else "nucleo_vertical"
            n_accesos = 1
        accesos.append({
            "uso": uso,
            "categoria": categoria,
            "pisos": pisos,
            "planta_baja": planta_baja,
            "tipo_acceso": tipo,
            "lado": lado,
            "n_accesos": n_accesos,
        })

    # Parejas incompatibles (matriz nivel 0) -> exigen accesos segregados
    segregaciones = []
    usos_lista = list(usos_canonicos)
    for i in range(len(usos_lista)):
        for j in range(i + 1, len(usos_lista)):
            a = usos_lista[i]
            b = usos_lista[j]
            nivel = m.get(a, {}).get(b, m.get(b, {}).get(a, 0))
            if nivel == 0:
                segregaciones.append({
                    "par": [a, b],
                    "regla": "Incompatible",
                    "requiere": "accesos_segregados",
                })

    n_publicos = sum(1 for a in accesos if a["categoria"] == "publico")
    n_privados = len(accesos) - n_publicos
    resumen = {
        "total_usos": len(accesos),
        "usos_publicos": n_publicos,
        "usos_privados": n_privados,
        "total_accesos": sum(a["n_accesos"] for a in accesos),
        "pares_incompatibles": len(segregaciones),
        "nucleo_vertical_m2": nucleos.get("total_m2_piso", 0.0),
        "poblacion_total": poblacion.get("total", 0),
    }

    return {
        "metadata": {
            "version": "2.0.0",
            "modulo": "F3_ACCESOS_INTEGRADOR_v02",
            "descripcion": "Accesos por uso y segregacion de flujos (F3)",
        },
        "resumen": resumen,
        "accesos": accesos,
        "segregaciones": segregaciones,
        "nucleos": nucleos,
        "origen": "layout_espacial.json + matriz_adyacencias.json",
    }


def _reporte_txt(resultado):
    lineas = []
    lineas.append("=" * 72)
    lineas.append("F3 - ACCESOS POR USO Y SEGREGACION DE FLUJOS")
    lineas.append("=" * 72)
    r = resultado["resumen"]
    lineas.append("Usos analizados: {}".format(r["total_usos"]))
    lineas.append("Publicos (fachada): {}".format(r["usos_publicos"]))
    lineas.append("Privados (nucleo): {}".format(r["usos_privados"]))
    lineas.append("Total accesos: {}".format(r["total_accesos"]))
    lineas.append("Pares incompatibles (segregar): {}".format(r["pares_incompatibles"]))
    lineas.append("")
    lineas.append("ACCESOS POR USO:")
    lineas.append("-" * 40)
    for a in resultado["accesos"]:
        lineas.append("  {:<18} [{}] pisos={} -> {} ({})".format(
            a["uso"], a["categoria"], a["pisos"], a["tipo_acceso"], a["lado"]))
    if resultado["segregaciones"]:
        lineas.append("")
        lineas.append("SEGREGACIONES REQUERIDAS (flujos incompatibles):")
        lineas.append("-" * 40)
        for s in resultado["segregaciones"]:
            lineas.append("  {} <-> {} : {}".format(
                s["par"][0], s["par"][1], s["requiere"]))
    lineas.append("")
    return "\n".join(lineas)


def main():
    caso_id = None
    layout_path = None
    matriz_path = None
    argv = sys.argv[1:]
    i = 0
    while i < len(argv):
        if argv[i] == "--caso" and i + 1 < len(argv):
            caso_id = argv[i + 1]
            i += 2
        elif argv[i] == "--layout" and i + 1 < len(argv):
            layout_path = argv[i + 1]
            i += 2
        elif argv[i] == "--matriz" and i + 1 < len(argv):
            matriz_path = argv[i + 1]
            i += 2
        else:
            i += 1

    if caso_id:
        layout_path, matriz_path, carpeta = _resolver(caso_id)
    else:
        carpeta = os.path.dirname(layout_path) if layout_path else CASOS_DIR

    layout = _cargar_json(layout_path)
    matriz = _cargar_json(matriz_path)

    if not layout:
        print("ERROR: layout_espacial.json no encontrado o invalido: {}".format(layout_path))
        sys.exit(1)
    if not matriz:
        print("ADVERTENCIA: matriz_adyacencias.json no encontrado; se usan solo los usos del layout.")
        matriz = {"usos": list(layout.get("reparto_vertical", {}).keys()), "matriz": {}}

    resultado = analizar_accesos(layout, matriz)
    reporte = _reporte_txt(resultado)

    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)

    sufijo = caso_id if caso_id else os.path.basename(carpeta)
    ruta_json = os.path.join(carpeta, "accesos.json")
    ruta_txt = os.path.join(carpeta, "accesos_{}.txt".format(sufijo))
    with io.open(ruta_json, "w", encoding="utf-8") as f:
        f.write(json.dumps(resultado, indent=2, ensure_ascii=False))
    with io.open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(reporte)

    print(reporte)
    print("Guardado: {}".format(ruta_json))
    print("Guardado: {}".format(ruta_txt))


# ------------------------------------------------------------------ GHPython
# Si se cablea como componente "Script" (IronPython 2.7), las entradas son:
#   layout_json (String, ruta) o layout_espacial_json (String, JSON crudo)
#   matriz_json (String, ruta) o matriz_adyacencias_json (String, JSON crudo)
# Salidas: accesos_json (String), mensaje (String)

layout_json_raw = globals().get("layout_json", None)
matriz_json_raw = globals().get("matriz_json", None)
layout_crudo = globals().get("layout_espacial_json", None)
matriz_crudo = globals().get("matriz_adyacencias_json", None)


def _unwrap(v):
    if v is None:
        return ""
    if hasattr(v, "Value"):
        return v.Value
    return v


def _gh():
    layout = {}
    matriz = {}
    if layout_crudo:
        try:
            layout = json.loads(str(_unwrap(layout_crudo)))
        except Exception:
            layout = {}
    if matriz_crudo:
        try:
            matriz = json.loads(str(_unwrap(matriz_crudo)))
        except Exception:
            matriz = {}
    if not layout and layout_json_raw:
        layout = _cargar_json(str(_unwrap(layout_json_raw)))
    if not matriz and matriz_json_raw:
        matriz = _cargar_json(str(_unwrap(matriz_json_raw)))
    if not layout:
        return "", "ACCESOS v2.0 | ERROR: sin layout_espacial.json"
    if not matriz:
        matriz = {"usos": list(layout.get("reparto_vertical", {}).keys()),
                  "matriz": {}}
    resultado = analizar_accesos(layout, matriz)
    accesos_json = json.dumps(resultado, indent=2, ensure_ascii=False)
    r = resultado["resumen"]
    mensaje = ("ACCESOS v2.0 | OK | {} usos ({} publicos / {} privados) | "
               "{} accesos | {} pares incompatibles").format(
        r["total_usos"], r["usos_publicos"], r["usos_privados"],
        r["total_accesos"], r["pares_incompatibles"])
    return accesos_json, mensaje


if __name__ == "__main__":
    main()
