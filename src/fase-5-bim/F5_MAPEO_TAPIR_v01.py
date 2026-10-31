# -*- coding: utf-8 -*-
"""
================================================================================
F5_MAPEO_TAPIR_v01.py — Fase 5: mapeo GH → ArchiCAD vía protocolo Tapir
================================================================================

Propósito:
  Mapear geometría de Fase 1/3 (lotes, vías, volúmenes, zonas) a elementos
  nativos de ArchiCAD (AC_Slab, AC_Wall, AC_Zone) usando el protocolo JSON-RPC
  Tapir (paquete Python `archicad` de Graphisoft, puerto CommandConnection
  19724 para API JSON/Python; 19723 solo para Live Connection del canvas GH).

Normativa aplicable:
  - POT Decreto 555/2021 (clasificación de suelos, tratamientos).
  - ADR-024: datum Z0 configurable; ArchiCAD GF = 0,000; Z_ac = Z_modelo - z_gf_m.
  - Capas de clasificación de entorno (ArchiCAD Layers, CLAUDE.md proyecto).

Historial de versiones:
  v01.0 - Creación inicial. Esqueleto de mapeo Tapir (sin conexión viva aún).

Entradas (JSON, No Type Hint + Item Access):
  - chip (str): CHIP del predio (ej. "AAA0030JKOE").
  - zgf_m (float): cota del Ground Floor (de <CHIP>-z0.json, ADR-024).
  - elementos (list[dict]): lista de elementos a mapear con llaves:
      tipo ("slab"|"wall"|"zone"), vertices ([x,y] o [[x,y],...]), altura (m),
      capa (nombre de capa ArchiCAD), material (opcional).

Salidas:
  - resultado (dict): {"ok": bool, "elementos_mapeados": int, "errores": [str],
      "detalle": [{"tipo":, "element_id":, "capa":}]}.

Funciones internas:
  - conectar_tapir(): abre CommandConnection a ArchiCAD (puerto 19724).
  - mapear_elemento(tipo, vertices, altura, capa): crea AC_Slab/AC_Wall/AC_Zone.
  - ejecutar_mapa(elementos, chip, zgf_m): recorre la lista y mapea cada uno.
================================================================================
"""

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
POT_CACHE = os.path.join(ROOT, "data", "pot-cache")

# Puerto Tapir para API JSON/Python (ArchiCAD auto-escanea 19723-19743).
TAPIR_PUERTO = 19724


def _z0_ruta(chip):
    return os.path.join(POT_CACHE, chip + "-z0.json")


def leer_z0(chip):
    """Lee <CHIP>-z0.json y devuelve z0_m (float) o None si no existe."""
    ruta = _z0_ruta(chip)
    if not os.path.exists(ruta):
        return None
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            d = json.load(f)
        return float(d.get("z0_m"))
    except Exception:
        return None


def conectar_tapir(puerto=TAPIR_PUERTO):
    """Abre la CommandConnection Tapir a ArchiCAD. Devuelve el objeto connection
    o None si no hay ArchiCAD escuchando."""
    try:
        from archicad import ACConnection
        conn = ACConnection.connect(puerto=puerto)
        return conn
    except Exception:
        return None


def mapear_elemento(conn, tipo, vertices, altura_m, capa, material=None):
    """Crea un elemento nativo en ArchiCAD vía Tapir.

    tipo: "slab" | "wall" | "zone"
    vertices: lista de [x, y] en marco local (0,0,0).
    altura_m: altura en metros.
    capa: nombre de capa ArchiCAD (debe existir).
    material: nombre opcional de material de superficie.
    Devuelve dict con element_id o None si falla."""
    try:
        commands = conn.commands
        # Normalizar vértices aplicando desfase Z0 (ADR-024): GF=0 en ArchiCAD.
        z_base = 0.0
        z_top = float(altura_m)

        if tipo == "slab":
            result = commands.CreateSlab(
                polygon=vertices,
                thickness=z_top - z_base,
                layer=capa,
                material=material,
            )
        elif tipo == "wall":
            result = commands.CreateWall(
                polygon=vertices,
                height=z_top - z_base,
                layer=capa,
                material=material,
            )
        elif tipo == "zone":
            result = commands.CreateZone(
                polygon=vertices,
                layer=capa,
            )
        else:
            return {"ok": False, "error": "tipo no soportado: " + str(tipo)}

        return {"ok": True, "tipo": tipo, "element_id": result,
                "capa": capa, "altura_m": altura_m}
    except Exception as e:
        return {"ok": False, "tipo": tipo, "error": str(e)}


def ejecutar_mapa(elementos, chip, zgf_m=None):
    """Mapea una lista de elementos a ArchiCAD.

    elementos: lista de dict con llaves tipo, vertices, altura_m, capa, material.
    chip: CHIP del predio (para leer z0 si zgf_m no se pasa).
    zgf_m: cota Ground Floor (si None, se lee de <chip>-z0.json).
    Devuelve dict resumen."""
    if zgf_m is None:
        zgf_m = leer_z0(chip)
    if zgf_m is None:
        zgf_m = 0.0

    conn = conectar_tapir()
    if conn is None:
        return {"ok": False, "error": "No se pudo conectar a ArchiCAD (Tapir puerto {})".format(TAPIR_PUERTO),
                "elementos_mapeados": 0, "detalle": []}

    detalle = []
    mapeados = 0
    errores = 0
    for el in elementos:
        res = mapear_elemento(
            conn,
            tipo=el.get("tipo"),
            vertices=el.get("vertices", []),
            altura_m=float(el.get("altura_m", 0.0)),
            capa=el.get("capa", "00-10-20_Elementos_referencia"),
            material=el.get("material"),
        )
        detalle.append(res)
        if res.get("ok"):
            mapeados += 1
        else:
            errores += 1

    return {
        "ok": errores == 0,
        "chip": chip,
        "zgf_m": zgf_m,
        "elementos_mapeados": mapeados,
        "errores": errores,
        "detalle": detalle,
    }


if __name__ == "__main__":
    # Autocomprobación mínima (sin ArchiCAD): verificar que se lee z0 si existe.
    chip = sys.argv[1] if len(sys.argv) > 1 else "AAA0030JKOE"
    z0 = leer_z0(chip)
    print("chip={} z0_m={}".format(chip, z0))
    print("F5_MAPEO_TAPIR_v01: esqueleto listo (conexión viva requiere ArchiCAD abierto).")
