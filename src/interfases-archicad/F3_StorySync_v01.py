# -*- coding: utf-8 -*-
"""
F3_StorySync_v01.py — Lee y sincroniza los Stories (niveles) de ArchiCAD.

Propósito: mapear cada piso del F3_VOLUM_GENERADOR a su Story de ArchiCAD para
crear cada elemento (Morph) en el nivel correspondiente, leyendo los stories del
proyecto SECUENCIALMENTE (por cota floorLevel).

Uso (con el venv del proyecto y ArchiCAD abierto con el Python API activo,
puerto auto-detectado 19723-19743 (suele ser 19724 porque AutoClaw ocupa 19723)):
    .venv\\Scripts\\python.exe F3_StorySync_v01.py --list
    .venv\\Scripts\\python.exe F3_StorySync_v01.py --json niveles_deseados.json
    .venv\\Scripts\\python.exe F3_StorySync_v01.py --puerto=19724 --list

Limitación verificada (2026-08-17): el paquete `archicad` (API JSON, release
ac29) expone LECTURA de stories (GetStoryNavigatorItems) pero NO un comando para
CREAR stories — `CreateStory` / `CreateElement` / `CreateMorph` no existen en el
paquete (se inspeccionó b3000commands.py). Por eso:

  * LECTURA + mapeo piso->story: este script (funciona si ArchiCAD está abierto).
  * CREACIÓN de niveles: Tapir, un Add-On C++ o creación manual en ArchiCAD
    (Documento > Preferencias del proyecto > Configuración de pisos). No hay
    importación XML de stories equivalente al XML de layers (AttributeFile
    solo cubre atributos, no la estructura de niveles).

Formato del JSON de niveles deseados (nombres y cotas según norma/operador):
    {
      "stories": [
        {"name": "Nivel 1", "elevation": 0.0},
        {"name": "Nivel 2", "elevation": 3.2}
      ]
    }
La comparación usa nombre + cota (con tolerancia), NO el índice, porque el índice
cambia al insertar/eliminar stories.
"""
import json
import sys

from archicad import ACConnection

TOL_COTA_M = 0.01


def _aplanar_stories(item, out):
    """Recorre el árbol del navegador y recoge los nodos StoryItem (niveles)."""
    if item is None:
        return
    if getattr(item, "type", "") == "StoryItem":
        out.append(item)
    for hijo in (getattr(item, "children", None) or []):
        _aplanar_stories(getattr(hijo, "navigatorItem", None), out)


def leer_stories(conn):
    """Devuelve la lista de stories ordenada por cota:
    [{'name', 'floorLevel', 'floorNumber', 'navigatorItemId'}...]."""
    T = conn.types
    tree_id = T.OtherNavigatorTreeId(type="ProjectMap")
    arbol = conn.commands.GetNavigatorItemTree(tree_id)
    nodos = []
    _aplanar_stories(arbol.rootItem, nodos)
    if not nodos:
        return []
    ids = [T.NavigatorItemIdWrapper(n.navigatorItemId) for n in nodos]
    detalles = conn.commands.GetStoryNavigatorItems(ids)
    stories = []
    for d in detalles:
        s = getattr(d, "storyNavigatorItem", None)
        if s is None:
            continue
        stories.append({
            "name": s.name,
            "floorLevel": s.floorLevel,
            "floorNumber": s.floorNumber,
            "navigatorItemId": s.navigatorItemId,
        })
    stories.sort(key=lambda x: x["floorLevel"])
    return stories


def comparar(stories, deseadas):
    """Compara stories existentes vs deseadas. Devuelve (mapeo, faltantes)."""
    faltantes = []
    mapeo = []  # (piso_index, story_name, floorLevel)
    for i, d in enumerate(deseadas):
        coinc = next(
            (s for s in stories if abs(s["floorLevel"] - d["elevation"]) <= TOL_COTA_M),
            None,
        )
        if coinc is None:
            faltantes.append(d)
        else:
            mapeo.append((i + 1, coinc["name"], coinc["floorLevel"]))
    return mapeo, faltantes


def main():
    puerto = None  # auto-detecta 19723-19743 (19724 si AutoClaw ocupa 19723)
    json_path = None
    listar = False
    for a in sys.argv[1:]:
        if a.startswith("--puerto="):
            puerto = int(a.split("=", 1)[1])
        elif a.startswith("--json="):
            json_path = a.split("=", 1)[1]
        elif a == "--list":
            listar = True

    conn = ACConnection.connect(puerto)
    stories = leer_stories(conn)
    print("Stories en ArchiCAD ({}):".format(len(stories)))
    for s in stories:
        print("  N{} {}  cota={:.3f} m".format(
            int(s["floorNumber"]), s["name"], s["floorLevel"]))

    if json_path:
        with open(json_path, "r", encoding="utf-8") as f:
            deseadas = json.load(f).get("stories", [])
        mapeo, faltantes = comparar(stories, deseadas)
        print("\nMapeo piso -> story:")
        for piso, name, cota in mapeo:
            print("  Piso {} -> {} (cota {:.3f} m)".format(piso, name, cota))
        if faltantes:
            print("\nNiveles FALTANTES (crear en ArchiCAD / Tapir):")
            for d in faltantes:
                print("  {} @ {:.3f} m".format(d["name"], d["elevation"]))
        else:
            print("\nTodos los niveles deseados existen y están alineados.")
    elif not listar:
        print("\nUso: --list  |  --json niveles_deseados.json  |  --puerto=<N> (default: auto)")


if __name__ == "__main__":
    main()
