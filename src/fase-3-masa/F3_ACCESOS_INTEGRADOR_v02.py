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

HISTORIAL DE VERSIONES:
  v02.2 (2026-10-09): Robustez de entradas + diagnostico:
    1. Parser JSON multi-forma: dict/list/string/ruta, listas anidadas y
       JSON embebido; valida que el contenido sea layout/matriz real.
    2. Si el cableado entrega otro JSON (p.ej. unidades_json) el mensaje
       lo indica en lugar de dar un error opaco.
    3. Respaldo desde disco: casos/*/layout_espacial.json y
       matriz_adyacencias.json (chip si existe) cuando el cableado no
       entrega datos validos.
    4. main() solo con __name__ == "__main__" (importable desde tests).
  v02.1 (2026-10-08): Cambio menor — FIX para lectura de entradas GH:
    1. Nueva función `_parse_json_input()`: acepta dict/list ya parseados,
       string JSON, o ruta a archivo .json (resuelve error "sin layout_espacial.json").
  v02.0 (2026-10-03): Cambio mayor — refactor completo compatible IronPython 2.7:
    - Eliminados rs, type hints, f-strings.
    - Separación CLI (`main()`) / GH (bloque final) con detección automática via `ghenv`.
    - Salidas: accesos_json (String), mensaje (String).

================================================================================
"""

import json
import io
import os
import sys

# __file__ no existe en IronPython/GH; usar cwd como fallback para modo CLI
try:
    BASE = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE = os.getcwd()
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
    """v02.2 - JSON en binario + cascada utf-8-sig/cp1252/latin-1 (IronPython-safe)."""
    if not ruta or not os.path.exists(ruta):
        return {}
    try:
        with open(ruta, "rb") as f:
            raw = f.read()
    except Exception:
        return {}
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            data = json.loads(raw.decode(enc))
            return data if isinstance(data, dict) else {}
        except Exception:
            continue
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

# Detectar modo GH: si ghenv existe o hay entradas inyectadas, NO ejecutar main()
_es_gh = False
try:
    ghenv  # noqa: F821
    _es_gh = True
except NameError:
    pass

if not _es_gh:
    # Verificar si hay entradas GH inyectadas (globals de GH)
    if globals().get("layout_json") is not None \
            or globals().get("layout_espacial_json") is not None \
            or globals().get("matriz_json") is not None \
            or globals().get("matriz_adyacencias_json") is not None:
        _es_gh = True

def _desempaquetar(v):
    """v02.2 - Desempaqueta DataTree/Goo/singleton; preserva listas multi-item."""
    if v is None:
        return None
    if hasattr(v, "Branch") and hasattr(v, "PathCount"):
        try:
            from Grasshopper.Kernel.Data import GH_Path
            path = GH_Path(0, 0)
            branch = v.Branch(path)
            if branch and branch.Count == 1:
                return _desempaquetar(branch[0])
            vals = []
            try:
                for i in range(v.PathCount):
                    b = v.get_Branch(i)
                    if b:
                        for x in b:
                            vals.append(x)
            except Exception:
                pass
            vals = [x for x in vals if x is not None]
            if len(vals) == 1:
                return _desempaquetar(vals[0])
            if vals:
                return vals
        except:
            pass
    if hasattr(v, "Value"):
        return _desempaquetar(v.Value)
    if isinstance(v, (list, tuple)):
        if len(v) == 1:
            return _desempaquetar(v[0])
        return v
    return v

def _hojas(v, out, prof=0):
    """v02.2 - Recolecta recursivamente los elementos hoja de listas/tuplas."""
    if prof > 6:
        return
    if isinstance(v, (list, tuple)):
        for x in v:
            _hojas(x, out, prof + 1)
    else:
        out.append(v)

def _s_texto(v):
    """v02.2 - Texto seguro (sin BOM ni espacios extremos)."""
    try:
        s = str(v)
    except Exception:
        return ""
    s = s.replace(u"\uFEFF", u"")
    return s.strip()

def _intenta_parse(s):
    """v02.2 - Parsea texto como JSON o lo carga desde ruta .json."""
    if not s:
        return None
    if s.endswith(".json") and os.path.exists(s):
        d = _cargar_json(s)
        return d if d else None
    try:
        return json.loads(s)
    except Exception:
        return None

def _candidatos_texto(s):
    """v02.2 - Variantes de un texto: completo y JSON embebido entre {..} / [..]."""
    if not s:
        return []
    cands = [s]
    a = s.find(u"{")
    b = s.rfind(u"}")
    if a >= 0 and b > a:
        cands.append(s[a:b + 1])
    a2 = s.find(u"[")
    b2 = s.rfind(u"]")
    if a2 >= 0 and b2 > a2:
        cands.append(s[a2:b2 + 1])
    return cands

def _parse_json_input(v):
    """v02.2 - Parsea entrada JSON: dict/list ya parseado, string JSON, ruta,
    listas anidadas (se unen) o JSON embebido."""
    v = _desempaquetar(v)
    if v is None:
        return None
    if isinstance(v, dict):
        return v
    if isinstance(v, (list, tuple)):
        hojas = []
        _hojas(v, hojas)
        for h in hojas:
            if isinstance(h, dict):
                return h
        s = u"".join([_s_texto(h) for h in hojas if h is not None])
        for cand in _candidatos_texto(s):
            r = _intenta_parse(cand)
            if r is not None:
                return r
        return None
    s = _s_texto(v)
    for cand in _candidatos_texto(s):
        r = _intenta_parse(cand)
        if r is not None:
            return r
    return None

def _es_layout(d):
    """v02.2 - Heuristica: dict que parece layout_espacial."""
    if not isinstance(d, dict):
        return False
    for k in ("reparto_vertical", "niveles", "poblacion_estimada"):
        if k in d:
            return True
    return False

def _es_matriz(d):
    """v02.2 - Heuristica: dict que parece matriz de adyacencias."""
    if not isinstance(d, dict):
        return False
    return ("matriz" in d) or ("usos" in d and "escala" in d)

def _vista_previa(v):
    """v02.2 - Resumen corto de un valor para diagnostico."""
    t = type(v).__name__
    if v is None:
        return t + ":None"
    s = _s_texto(v)
    if not s:
        try:
            s = repr(v)
        except Exception:
            s = ""
    if not s:
        s = "(vacio)"
    return t + ":" + s[:60]

def _buscar_json(claves, validador, g):
    """v02.2 - Prueba nombres conocidos/relacionados y valida el contenido.
    Devuelve (json, fuente, intentos)."""
    intentos = []
    nombres = list(claves)
    try:
        for k in list(g.keys()):
            kl = str(k).lower()
            for c in claves:
                if c in kl and k not in nombres:
                    nombres.append(k)
    except Exception:
        pass
    vistos = []
    for n in nombres:
        if n in vistos:
            continue
        vistos.append(n)
        try:
            val = g.get(n)
        except Exception:
            continue
        if val is None:
            intentos.append(n + " -> None")
            continue
        d = _parse_json_input(val)
        if d is None:
            intentos.append(n + " -> " + _vista_previa(val))
            continue
        if validador(d):
            return d, n, intentos
        claves_d = ", ".join(list(d.keys())[:6]) if isinstance(d, dict) else type(d).__name__
        intentos.append(n + " -> json sin campos esperados (" + claves_d + ")")
    return None, "", intentos

def _raiz_casos():
    """v02.2 - Localiza src/fase-3-masa/casos (archivo / entorno / cwd)."""
    raices = []
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        raices.append(os.path.join(base, "casos"))
    except Exception:
        pass
    try:
        env_root = os.environ.get("DISENO_PARAMETRICO_ROOT", "")
        if env_root:
            raices.append(os.path.join(env_root, "src", "fase-3-masa", "casos"))
    except Exception:
        pass
    p = os.getcwd()
    for _i in range(6):
        raices.append(os.path.join(p, "src", "fase-3-masa", "casos"))
        np_ = os.path.dirname(p)
        if np_ == p:
            break
        p = np_
    for r in raices:
        try:
            if r and os.path.isdir(r):
                return r
        except Exception:
            pass
    return ""

def _json_desde_disco(nombre):
    """v02.2 - Busca <casos>/<cualquiera>/<nombre> y devuelve el mas reciente."""
    casos = _raiz_casos()
    if not casos:
        return None, ""
    mejor = None
    try:
        for sub in os.listdir(casos):
            ruta = os.path.join(casos, sub, nombre)
            if os.path.isfile(ruta):
                try:
                    m = os.path.getmtime(ruta)
                except Exception:
                    m = 0
                if mejor is None or m > mejor[0]:
                    mejor = (m, ruta)
    except Exception:
        pass
    if mejor is None:
        return None, ""
    d = _cargar_json(mejor[1])
    if d:
        return d, mejor[1]
    return None, ""

def _layout_desde_disco():
    return _json_desde_disco("layout_espacial.json")

def _matriz_desde_disco():
    return _json_desde_disco("matriz_adyacencias.json")

if _es_gh:
    # v02.2: diagnostico de entradas + validacion de contenido
    try:
        gh_globals = [k for k in globals().keys() if not k.startswith('_') and k not in ['json', 'io', 'os', 'sys', '_cargar_json', '_resolver', '_pisos_de_uso', 'analizar_accesos', '_reporte_txt', 'main', '_es_gh', '_desempaquetar', '_parse_json_input', '_hojas', '_s_texto', '_intenta_parse', '_candidatos_texto', '_es_layout', '_es_matriz', '_vista_previa', '_buscar_json', '_raiz_casos', '_json_desde_disco', '_layout_desde_disco', '_matriz_desde_disco', 'USOS_PUBLICOS', '_normalizar', '_categoria']]
    except:
        gh_globals = []

    layout, fuente_layout, intentos_layout = _buscar_json(
        ["layout_espacial_json", "layout_json", "layoutespacial", "layout_espacial"],
        _es_layout, globals())
    if not layout:
        for k, v in list(globals().items()):
            if v is None or k in ('__name__',):
                continue
            d = _parse_json_input(v)
            if isinstance(d, dict) and _es_layout(d):
                layout = d
                fuente_layout = k + " (contenido)"
                break
    if not layout:
        layout, _ruta_lay = _layout_desde_disco()
        if layout:
            fuente_layout = "disco: " + _ruta_lay

    matriz, fuente_matriz, intentos_matriz = _buscar_json(
        ["matriz_adyacencias_json", "matriz_json", "matrizadyacencias", "matriz_adyacencias"],
        _es_matriz, globals())
    if not matriz:
        for k, v in list(globals().items()):
            if v is None or k in ('__name__',):
                continue
            d = _parse_json_input(v)
            if isinstance(d, dict) and _es_matriz(d):
                matriz = d
                fuente_matriz = k + " (contenido)"
                break
    if not matriz:
        matriz, _ruta_mat = _matriz_desde_disco()
        if matriz:
            fuente_matriz = "disco: " + _ruta_mat

    if not layout:
        accesos_json = ""
        mensaje = ("ACCESOS v2.0 | ERROR: sin layout_espacial.json. | layout probados: {} | "
                   "matriz probados: {} | globales: {}").format(
            "; ".join(intentos_layout[:8]) or "(ninguno)",
            "; ".join(intentos_matriz[:6]) or "(ninguno)",
            ", ".join(sorted(gh_globals)[:18]))
    else:
        if not matriz:
            matriz = {"usos": list(layout.get("reparto_vertical", {}).keys()),
                  "matriz": {}}
        resultado = analizar_accesos(layout, matriz)
        accesos_json = json.dumps(resultado, indent=2, ensure_ascii=False)
        r = resultado["resumen"]
        _src_txt = fuente_layout if fuente_layout else "cableado"
        mensaje = ("ACCESOS v2.0 | OK | {} usos ({} publicos / {} privados) | " +
               "{} accesos | {} pares incompatibles | layout: {}").format(
        r["total_usos"], r["usos_publicos"], r["usos_privados"],
        r["total_accesos"], r["pares_incompatibles"], _src_txt)
elif __name__ == "__main__":
    # MODO CLI: ejecutar main() (solo ejecucion directa; importable desde tests)
    main()
