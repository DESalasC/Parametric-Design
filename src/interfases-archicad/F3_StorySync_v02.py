# -*- coding: utf-8 -*-
"""
F3_StorySync_v02.py — Plan y verificacion de Stories (niveles) de ArchiCAD.

Nuevo en v02 (2026-10-12):
  --plan   Genera `niveles_deseados.json` a partir de:
           (a) `src/fase-3-masa/casos/<chip>/cotas-arranque.json` escrito por
               el canvas (F3_VOLUM v08.1, flag de exportacion), o
           (b) cotas explicitas: --cotas "0.2,3.35,6.85,10.15"
               [--pisos "5,5,5,5"] [--floor-h 3.05] [--tapa]
  --check  Compara el archivo de niveles deseados con los Stories existentes
           en ArchiCAD (LECTURA; paquete `archicad`, import perezoso).
  --list   Lista los Stories de ArchiCAD.

El algoritmo del plan es el MISMO del canvas (F3_VOLUM v08.1, `_plan_stories`):
  - grilla de niveles = base + j*floor_h ; base = menor cota de bloque
    (nivel de acceso definitivo: pendiente fetch v8 / NORMATIVA v10);
  - snap: cada plataforma se redondea a la grilla (corte/relleno);
  - nombres BEP: GF para el primer nivel y L01.. para los siguientes
    (RF opcional con --tapa);
  - elevaciones en marco canvas (misma referencia que zonas/LC).

Recordatorio (API ac29): la creacion de Stories NO es posible por API/LC;
este archivo es la lista para crear manualmente en ArchiCAD
(Documento > Preferencias del proyecto > Configuracion de pisos) y luego
verificar con --check.

Uso (venv del proyecto):
    .venv\\Scripts\\python.exe F3_StorySync_v02.py --list
    .venv\\Scripts\\python.exe F3_StorySync_v02.py --plan --chip AAA0030JKOE
    .venv\\Scripts\\python.exe F3_StorySync_v02.py --plan --cotas "0.2,3.35,6.85,10.15" --pisos 5,5,5,5 --floor-h 3.05
    .venv\\Scripts\\python.exe F3_StorySync_v02.py --check --json niveles_deseados.json
    .venv\\Scripts\\python.exe F3_StorySync_v02.py --puerto=19724 --list
"""
import io
import json
import os
import sys

TOL_COTA_M = 0.01
BASE_PROYECTO_DEF = r"D:\Work\PROJECTS\DiseñoParametrico"


def _raiz_proyecto():
    """env DISENO_PARAMETRICO_ROOT -> relativa al script -> ruta historica."""
    try:
        r = os.environ.get("DISENO_PARAMETRICO_ROOT", "")
        if r and os.path.isdir(r):
            return r
    except Exception:
        pass
    cand = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    if os.path.isdir(os.path.join(cand, "src")):
        return cand
    return BASE_PROYECTO_DEF


def _norm_texto_bep(s):
    """Normaliza texto (minusculas, sin acentos) para el catalogo de categorias."""
    if s is None:
        return ""
    t = s
    if not hasattr(t, "lower"):
        try:
            t = str(t)
        except Exception:
            return ""
    t = t.strip().lower()
    for a, b in ((u"\u00e1", "a"), (u"\u00e9", "e"), (u"\u00ed", "i"),
                 (u"\u00f3", "o"), (u"\u00fa", "u"), (u"\u00f1", "n")):
        t = t.replace(a, b)
    return t


def _nivel_bep(piso_1based):
    """Codigo de nivel BEP: piso 1 = GF; siguientes = L01, L02, ..."""
    try:
        n = int(round(float(piso_1based)))
    except Exception:
        n = 1
    if n <= 1:
        return "GF"
    return "L%02d" % (n - 1)


def plan_stories(bloques, floor_h, snap=True, con_tapa=False):
    """Plan de niveles (stories) desde las cotas de arranque reales.

    bloques: [{"id", "cota_arranque_m", "pisos"}] (cotas en marco canvas).
    Grilla = base + j*floor_h; base = menor cota; snap = redondeo de cada
    plataforma a la grilla (corte/relleno). Devuelve dict serializable con
    la misma estructura que F3_VOLUM v08.1 (`_plan_stories`).
    """
    if not bloques:
        return None
    try:
        h = float(floor_h)
    except Exception:
        h = 0.0
    if h <= 0.0:
        h = 3.0
    cotas = []
    for b in bloques:
        try:
            cotas.append(float(b.get("cota_arranque_m", 0.0)))
        except Exception:
            cotas.append(0.0)
    base = min(cotas)
    detalle = []
    max_j = 0
    for i, b in enumerate(bloques):
        c = cotas[i]
        try:
            p = int(b.get("pisos", 0) or 0)
        except Exception:
            p = 0
        if snap:
            o = int(round((c - base) / h))
            ajuste = round(base + o * h - c, 3)
        else:
            o = 0
            ajuste = 0.0
        detalle.append({
            "id": str(b.get("id", "B%d" % (i + 1))),
            "cota_arranque_m": round(c, 3),
            "cota_snap_m": round(base + o * h, 3),
            "offset_niveles": int(o),
            "ajuste_m": ajuste,
            "pisos": p,
        })
        if o + p > max_j:
            max_j = o + p
    stories = []
    for j in range(int(max_j)):
        d = {
            "name": ("GF" if j == 0 else "L%02d" % j),
            "elevation": round(base + j * h, 3),
            "elevacion_relativa_m": round(j * h, 3),
        }
        d["descripcion"] = "Planta baja (acceso)" if j == 0 else ("Nivel %d" % j)
        stories.append(d)
    if con_tapa:
        j = int(max_j)
        stories.append({
            "name": "RF",
            "elevation": round(base + j * h, 3),
            "elevacion_relativa_m": round(j * h, 3),
            "descripcion": "Cubierta (opcional)",
        })
    return {
        "floor_h_m": round(h, 3),
        "base_z_m": round(base, 3),
        "snap": bool(snap),
        "stories": stories,
        "bloques": detalle,
        "avisos": [
            "base = menor cota de bloque; nivel de acceso definitivo "
            "(fetch v8 / NORMATIVA v10) puede desplazar la base",
            "elevaciones en marco canvas (misma referencia que zonas/LC)",
        ],
    }


def cargar_bloques_de_casos(chip, raiz=None):
    """Lee casos/<chip>/cotas-arranque.json -> (bloques, floor_h, ruta)."""
    raiz = raiz or _raiz_proyecto()
    ruta = os.path.join(raiz, "src", "fase-3-masa", "casos", chip, "cotas-arranque.json")
    with io.open(ruta, "r", encoding="utf-8") as f:
        datos = json.loads(f.read())
    bloques = []
    for b in datos.get("bloques", []):
        bloques.append({
            "id": b.get("id", ""),
            "cota_arranque_m": float(b.get("cota_arranque_m", 0.0)),
            "pisos": int(b.get("pisos", 0) or 0),
        })
    floor_h = float(datos.get("floor_h_m") or 3.0)
    return bloques, floor_h, ruta


def leer_stories(conn):
    """Devuelve los stories de ArchiCAD ordenados por cota:
    [{'name', 'floorLevel', 'floorNumber', 'navigatorItemId'}...]."""
    def _aplanar(item, out):
        if item is None:
            return
        if getattr(item, "type", "") == "StoryItem":
            out.append(item)
        for hijo in (getattr(item, "children", None) or []):
            _aplanar(getattr(hijo, "navigatorItem", None), out)

    T = conn.types
    tree_id = T.OtherNavigatorTreeId(type="ProjectMap")
    arbol = conn.commands.GetNavigatorItemTree(tree_id)
    nodos = []
    _aplanar(arbol.rootItem, nodos)
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
    mapeo = []
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


def _leer_deseadas(ruta):
    with io.open(ruta, "r", encoding="utf-8") as f:
        return json.loads(f.read()).get("stories", [])


def _parse(args):
    opts = {
        "plan": False, "check": False, "listar": False, "tapa": False,
        "chip": None, "cotas": None, "pisos": None, "floor_h": 3.05,
        "json": None, "out": None, "puerto": None,
    }
    i = 0
    n = len(args)
    while i < n:
        a = args[i]
        if a == "--plan":
            opts["plan"] = True
        elif a == "--check":
            opts["check"] = True
        elif a == "--list":
            opts["listar"] = True
        elif a == "--tapa":
            opts["tapa"] = True
        elif a == "--chip":
            i += 1
            opts["chip"] = args[i] if i < n else None
        elif a.startswith("--chip="):
            opts["chip"] = a.split("=", 1)[1]
        elif a == "--cotas":
            i += 1
            opts["cotas"] = args[i] if i < n else None
        elif a.startswith("--cotas="):
            opts["cotas"] = a.split("=", 1)[1]
        elif a == "--pisos":
            i += 1
            opts["pisos"] = args[i] if i < n else None
        elif a.startswith("--pisos="):
            opts["pisos"] = a.split("=", 1)[1]
        elif a == "--floor-h":
            i += 1
            opts["floor_h"] = float(args[i])
        elif a.startswith("--floor-h="):
            opts["floor_h"] = float(a.split("=", 1)[1])
        elif a == "--json":
            i += 1
            opts["json"] = args[i] if i < n else None
        elif a.startswith("--json="):
            opts["json"] = a.split("=", 1)[1]
        elif a == "--out":
            i += 1
            opts["out"] = args[i] if i < n else None
        elif a.startswith("--out="):
            opts["out"] = a.split("=", 1)[1]
        elif a == "--puerto":
            i += 1
            opts["puerto"] = int(args[i])
        elif a.startswith("--puerto="):
            opts["puerto"] = int(a.split("=", 1)[1])
        i += 1
    return opts


def _bloques_de_cotas(cotas_txt, pisos_txt, n_def=5):
    cotas = [float(x) for x in cotas_txt.replace(";", ",").split(",") if x.strip()]
    if pisos_txt:
        vals = [int(round(float(x))) for x in pisos_txt.replace(";", ",").split(",") if x.strip()]
        if len(vals) == 1:
            vals = vals * len(cotas)
        if len(vals) != len(cotas):
            raise ValueError("--pisos: {} valores != {} cotas".format(len(vals), len(cotas)))
    else:
        vals = [n_def] * len(cotas)
    bloques = []
    for i, c in enumerate(cotas):
        bloques.append({"id": "B%d-R1" % (i + 1), "cota_arranque_m": c, "pisos": vals[i]})
    return bloques


def _cmd_plan(opts):
    if opts["cotas"]:
        bloques = _bloques_de_cotas(opts["cotas"], opts["pisos"])
        floor_h = opts["floor_h"]
        origen = "cotas CLI"
    elif opts["chip"]:
        bloques, floor_h, origen = cargar_bloques_de_casos(opts["chip"])
    else:
        print("--plan requiere --cotas \"a,b,c\" o --chip <CHIP> (casos/<chip>/cotas-arranque.json).")
        return 1
    plan = plan_stories(bloques, floor_h, snap=True, con_tapa=bool(opts["tapa"]))
    if not plan:
        print("Sin bloques: no hay plan.")
        return 1
    salida = {
        "schema": "f3_niveles_deseados_v01",
        "chip": opts["chip"] or "CLI",
        "generado": "manual (F3_StorySync_v02 --plan)",
        "nota": "Stories ArchiCAD (Story Settings). elevation = marco canvas; "
                "elevacion_relativa_m = acumulado desde la base.",
        "floor_h_m": plan["floor_h_m"],
        "base_z_m": plan["base_z_m"],
        "snap": plan["snap"],
        "stories": plan["stories"],
        "bloques": plan["bloques"],
        "avisos": plan["avisos"],
    }
    if opts["out"]:
        ruta_out = opts["out"]
    elif opts["chip"]:
        raiz = _raiz_proyecto()
        ruta_out = os.path.join(raiz, "src", "fase-3-masa", "casos", opts["chip"],
                                "niveles_deseados.json")
        d = os.path.dirname(ruta_out)
        if d and not os.path.isdir(d):
            os.makedirs(d)
    else:
        ruta_out = os.path.join(os.getcwd(), "niveles_deseados.json")
    txt = json.dumps(salida, ensure_ascii=True, indent=2)
    f = io.open(ruta_out, "w", encoding="utf-8")
    try:
        f.write(txt)
    finally:
        f.close()
    print("Plan de stories (fuente: {}):".format(origen))
    print("  floor_h = {:.3f} m | base = {:.3f} m | snap = {}".format(
        plan["floor_h_m"], plan["base_z_m"], plan["snap"]))
    for d in plan["bloques"]:
        print("  {}: cota {:.2f} -> snap {:.2f} (offset {} niveles, ajuste {:+.2f} m)".format(
            d["id"], d["cota_arranque_m"], d["cota_snap_m"], d["offset_niveles"], d["ajuste_m"]))
    print("  Stories ({}):".format(len(plan["stories"])))
    for s in plan["stories"]:
        print("    {} @ {:.3f} m".format(s["name"], s["elevation"]))
    print("Escrito: {}".format(ruta_out))
    return 0


def _cmd_list(opts):
    from archicad import ACConnection
    conn = ACConnection.connect(opts["puerto"])
    stories = leer_stories(conn)
    print("Stories en ArchiCAD ({}):".format(len(stories)))
    for s in stories:
        print("  N{} {}  cota={:.3f} m".format(int(s["floorNumber"]), s["name"], s["floorLevel"]))
    return 0


def _cmd_check(opts):
    ruta = opts["json"]
    if not ruta and opts["chip"]:
        ruta = os.path.join(_raiz_proyecto(), "src", "fase-3-masa", "casos",
                            opts["chip"], "niveles_deseados.json")
    if not ruta or not os.path.isfile(ruta):
        print("--check requiere --json <ruta> (o --chip con niveles_deseados.json existente).")
        return 1
    deseadas = _leer_deseadas(ruta)
    from archicad import ACConnection
    conn = ACConnection.connect(opts["puerto"])
    stories = leer_stories(conn)
    print("Stories en ArchiCAD ({}):".format(len(stories)))
    for s in stories:
        print("  N{} {}  cota={:.3f} m".format(int(s["floorNumber"]), s["name"], s["floorLevel"]))
    mapeo, faltantes = comparar(stories, deseadas)
    print("\nMapeo piso -> story:")
    for piso, name, cota in mapeo:
        print("  Piso {} -> {} (cota {:.3f} m)".format(piso, name, cota))
    if faltantes:
        print("\nNiveles FALTANTES (crear en ArchiCAD / Tapir):")
        for d in faltantes:
            print("  {} @ {:.3f} m".format(d["name"], d["elevation"]))
        return 1
    print("\nTodos los niveles deseados existen y estan alineados.")
    return 0


def main(argv=None):
    opts = _parse(argv if argv is not None else sys.argv[1:])
    if opts["plan"]:
        return _cmd_plan(opts)
    if opts["check"]:
        return _cmd_check(opts)
    if opts["listar"] or not any((opts["plan"], opts["check"], opts["json"])):
        return _cmd_list(opts)
    print("Uso: --list | --plan --chip X | --plan --cotas \"...\" | --check --json niveles_deseados.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
