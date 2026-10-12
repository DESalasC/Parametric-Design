"""
================================================================================
F3_VOLUM_GENERADOR_v08.py - Masa con nucleo EXCLUIDO y circulacion/servicios
separados (geometria para elementos nativos de ArchiCAD via Live Connection)
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (componente "Script", IronPython 2.7)
================================================================================

SUBVERSIONES INTERNAS (politica: solo se documentan las 1-2 sub-versiones
  inmediatamente anteriores; el historial completo vive en el archivo v07
  archivado en _legacy):

  v08.0: salidas nuevas `circulacion_pisos`, `servicios_pisos`, `losas_pisos`
         y `nucleo_pisos` (numero de piso por geometria, paralelas 1:1 a sus
         respectivas salidas de geometria), para alimentar F3_MORPH_ATRIBUTOS
         y asignar el Story en ArchiCAD sin adivinar el piso.

  v07.25 (previa): salida `usos_pisos` (piso por volumen en volumenes_por_uso).
  v07.24 (previa): salidas `volumenes_por_uso` + `usos_etiquetas` (paralelas).
cambios mayores (contrato de entradas/salidas o algoritmo central); las
iteraciones internas se registran como subversiones v07.x en este encabezado
(el mensaje del componente reporta la subversion en curso).

v07 (2026-08-16): correcciones solicitadas por el operador:
  1. PERIMETRO = envelope_por_piso de F1_ETAPA2_NORMATIVA_v07 (curva POR PISO:
     ocupacion escalonada + voladizos en pisos superiores; fallback a
     envelope_curve para compatibilidad v06). El componente recibe SIEMPRE la
     lista de curvas del NORMATIVA (o la curva unica como respaldo).
  2. EXCLUSION REAL del nucleo: la losa se perfora con el BLOQUE COMPLETO
     del nucleo (nucleo.bloque del programa-areas.json: 5,4x9,0 m = 48,6 m2
     en el caso A), UBICADO POR BARRIDO 3x3 (paso 0,75 m) alrededor del
     centroide de cada piso (el centroide de una L concava puede caer en el
     codo y partir la interseccion; el barrido ubica el bloque donde cabe
     completo, >=95% del area - posicion indicativa del layout, la
     definitiva es del diseno arquitectonico). El hueco se construye SIN
     booleanos: la diferencia de curvas devuelve el contorno EXTERIOR + los
     AGUJEROS como curvas separadas (representacion de Rhino de una region
     con hueco); la losa sale de CreatePlanarBreps([exterior] + agujeros)
     y el volumen principal es la EXTRUSION de esa losa con hueco
     (verificacion de area tol 2%); boolean 3D (verificacion de volumen
     tol 3%) solo como respaldo. Los SOLIDOS del nucleo
     (circulacion + servicios, 39,8 m2) se generan aparte y rellenan parte
     del hueco; el aire interior del bloque (8,8 m2) queda vacio (circulacion
     interna del nucleo). Regla: NUNCA se entrega geometria intersectante - si
     la exclusion falla, ese piso se omite y el mensaje lo reporta (huecos
     excluidos n/N + detalle por piso).
  3. CIRCULACION VERTICAL (escaleras + ascensores) SEPARADA de SERVICIOS y
     areas tecnicas (ductos/basuras/cuarto tecnico): salidas independientes
     volumenes_circulacion y volumenes_servicios, con la disposicion real de
     nucleo.disposicion del programa-areas.json (F3_DISTRIBUCION_v01).
  4. DESTINO = ArchiCAD: las salidas de geometria se cablean a los componentes
     de la Live Connection (AC_*) que crean MORPHS NATIVOS de ArchiCAD - no se
     hornea en Rhino. Los elementos viajan a ArchiCAD y pueden volver
     modificados por decisiones del operador (GetElements) o por sugerencias de
     Ladybug (F4) y Wallacei (optimizacion) dentro de Grasshopper.

Normativa aplicable: NSR-10 Titulo K (escaleras de evacuacion), C.2.3
(ocupacion); POT Decreto 555/2021 (ocupacion del envelope F1).

ENTRADAS (contrato GH):
  envelope_por_piso (List)     - [v07+] Curvas de ocupacion POR PISO (salida
                             envelope_por_piso de F1_ETAPA2_NORMATIVA_v07:
                             escalonada + voladizos en pisos superiores).
                             Se usa curva[i] para el piso i. PREFERIDA.
  envelope_curve (Curve)   - Fallback: si envelope_por_piso no llega o llega
                             con menos curvas que pisos, se usa esta curva
                             para todos los pisos (compat v06).
  json_path (String)       - Ruta al programa-areas.json (F3_DISTRIBUCION_v01).
                             Acepta ruta absoluta o relativa al proyecto
                             (se resuelve contra D:\Work\PROJECTS\DiseñoParametrico).
  floor_height (Number)    - Altura de entrepiso [m] (default 3.0; se prefiere
                             la altura_z del JSON por piso)
  salida_morph (Boolean)   - [v07.9] Interruptor de salida. True: las salidas
                             principales (volumenes_principales, circulacion,
                             servicios, nucleo, losas) emiten MESH, listas
                             para cablear directo al componente Morph de
                             ArchiCAD (exige Rhino.Geometry.Mesh). False
                             (default): Brep en las principales + *_mesh
                             por separado.
  salida_zona (Boolean)    - [v08.0] Interruptor de salida. True: las salidas
                             principales emiten datos para componentes Zona de
                             ArchiCAD (perimetros 2D, atributos de uso y piso).
                             False (default): comportamiento compatible con
                             versiones anteriores (Morph o Brep segun salida_morph).

SALIDAS:
  volumenes_principales   (List of Brep) - Masa por piso con el hueco del
                             nucleo EXCLUIDO (no intersecta circulacion/servicios)
  volumenes_circulacion   (List of Brep) - Escaleras + ascensores (solidos)
  volumenes_servicios     (List of Brep) - Ductos/basuras/cuarto tecnico (solidos)
  volumenes_nucleo        (List of Brep) - Compat v06: circulacion + servicios
  losas                   (List of Brep)  - Losas con hueco por piso
  etiquetas               (List of String)- Usos, circulacion y servicios por piso
  volumenes_por_uso       (List of Brep)  - [v07.24] Masa POR USO, paralela a
                             usos_etiquetas: piso simple = el volumen principal
                             etiquetado; piso mixto = sub-volumenes por uso.
  usos_etiquetas          (List of String)- [v07.24] Nombre del uso de cada
                             volumen en volumenes_por_uso (paralelo 1:1).
  usos_pisos              (List of int)    - [v07.25] Numero de piso de cada
                             volumen en volumenes_por_uso (paralelo 1:1), para
                             asignar el Story (nivel) en ArchiCAD.
  circulacion_pisos       (List of int)    - [v08.0] Numero de piso de cada
                             volumen en volumenes_circulacion (paralelo 1:1).
  servicios_pisos         (List of int)    - [v08.0] Numero de piso de cada
                             volumen en volumenes_servicios (paralelo 1:1).
  losas_pisos             (List of int)    - [v08.0] Numero de piso de cada
                             losa en losas (paralelo 1:1).
  nucleo_pisos            (List of int)    - [v08.0] circulacion_pisos + servicios_pisos.
  mensaje                 (String)         - Diagnostico (huecos n/N, fuente)

  SALIDAS ZONA (cuando salida_zona=True):
  zonas_perimetros        (List of List of Point3d) - Perimetros 2D de zonas por uso
                                                      (lista de listas de puntos, una lista por zona)
  zonas_pisos             (List of int)             - Numero de piso de cada zona (paralelo 1:1)
  zonas_atributos         (List of String)          - Atributos de zona en formato JSON (uso, area, etc.)
  zonas_alturas           (List of float)           - Altura de cada zona (acumulada desde Z=0)

SALIDAS MESH (para el componente Morph de la Live Connection de ArchiCAD,
que requiere Rhino.Geometry.Mesh, no Brep):
  volumenes_principales_mesh / volumenes_circulacion_mesh /
  volumenes_servicios_mesh / volumenes_nucleo_mesh / losas_mesh
  (mismo contenido que las Brep, convertido con Mesh.CreateFromBrep /
  CreateFromPlanarBreps; las losas salen como superficie abierta).

FUNCIONES INTERNAS:
  _caja_curva(cx, cy, ancho, largo) - Polilinea cerrada de una caja centrada
  _area_curva(curva)                - Area plana de una curva (AreaMassProperties)
  _extruir(curva, h, z)             - Extrusion a Brep trasladada a z
  _recortar_huecos(env, cajas, area_losa, hueco_m2) - Diferencia secuencial
                             curva-curva con verificacion de area; devuelve
                             (perfil, ok)
  _excluir_3d(env_vol, cajas, h, z, area_losa, hueco_m2) - Boolean 3D de
                             respaldo con verificacion de volumen
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import io
import math

# ------------------------------------------------------------------ helpers

def unwrap(val):
    if val is None:
        return None
    if isinstance(val, list):
        return val[0] if len(val) > 0 else None
    return val


def _caja_curva(cx, cy, ancho, largo):
    a2 = ancho / 2.0
    l2 = largo / 2.0
    pts = [rg.Point3d(cx - a2, cy - l2, 0.0), rg.Point3d(cx + a2, cy - l2, 0.0),
           rg.Point3d(cx + a2, cy + l2, 0.0), rg.Point3d(cx - a2, cy + l2, 0.0),
           rg.Point3d(cx - a2, cy - l2, 0.0)]
    return rg.PolylineCurve(pts)


def _area_curva(curva):
    try:
        ap = rg.AreaMassProperties.Compute(curva)
        return ap.Area if ap else 0.0
    except Exception:
        return 0.0


def _subir_si_negativo(brep):
    """Si la extrusion quedo hacia -Z (normal de la curva/cara invertida),
    la desplaza a [0, +h] antes de subirla a su nivel. Los morphs SUBEN, no
    bajan (FIX 2026-08-17: arrancaban en el nivel y terminaban en -altura)."""
    try:
        bb = brep.GetBoundingBox(True)
        if bb is not None and bb.Min.Z < -1e-9:
            brep.Translate(rg.Vector3d(0.0, 0.0, -bb.Min.Z))
    except Exception:
        pass
    return brep


def _extruir(curva, h, z):
    try:
        ext = rg.Extrusion.Create(curva.ToNurbsCurve(), h, True)
        if ext is None:
            return None
        b = ext.ToBrep()
        if b is None:
            return None
        _subir_si_negativo(b)
        b.Translate(rg.Vector3d(0.0, 0.0, z))
        return b
    except Exception:
        return None


def _brep_a_mesh(brep):
    """Convierte un Brep a Mesh para el componente Morph de ArchiCAD (la Live
    Connection requiere Rhino.Geometry.Mesh). Usa presets estaticos de Rhino;
    para planos cae a CreateFromPlanarBreps. Devuelve Mesh o None."""
    if brep is None:
        return None
    try:
        mp = rg.MeshingParameters.Coarse
    except Exception:
        mp = None
    if mp is None:
        try:
            mp = rg.MeshingParameters.Default
        except Exception:
            mp = None
    # Superficies planas (losas con hueco): mesh de la region plana
    try:
        ms = rg.Mesh.CreateFromPlanarBreps(brep, mp)
        if ms and len(ms) > 0:
            m = rg.Mesh()
            for x in ms:
                m.Append(x)
            return m
    except Exception:
        pass
    # Solidos 3D
    try:
        ms = rg.Mesh.CreateFromBrep(brep, mp)
        if ms and len(ms) > 0:
            m = rg.Mesh()
            for x in ms:
                m.Append(x)
            return m
    except Exception:
        pass
    return None


def _recortar_huecos(env_crv, cajas, area_losa, hueco_m2):
    """Diferencia curva-curva: Rhino representa una region CON AGUJERO como
    varias curvas (el contorno exterior + los contornos de los agujeros) -
    "2 piezas" NO es un roce ni un error. Esta funcion devuelve (perfil, ok)
    con el contorno EXTERIOR en perfil y los contornos de los AGUJEROS en la
    global _agujeros_global; la losa con hueco se construye luego con
    rg.Brep.CreatePlanarBreps([perfil] + agujeros) SIN booleanos."""
    global _area_perfil_diagnostico, _motivo_fallo, _agujeros_global
    _area_perfil_diagnostico = 0.0
    _motivo_fallo = ""
    _agujeros_global = []
    perfil = env_crv
    for cc in cajas:
        try:
            dif = rg.Curve.CreateBooleanDifference(perfil, cc, 0.01)
        except Exception as ex:
            _motivo_fallo = "diferencia excepcion: {}".format(str(ex))
            return None, False
        if dif is None or len(dif) == 0:
            _motivo_fallo = "diferencia sin resultado"
            return None, False
        amax = -1.0
        pmax = dif[0]
        for d in dif:
            aa = _area_curva(d)
            if aa > amax:
                amax = aa
                pmax = d
        perfil = pmax
        _agujeros_global = [d for d in dif if d is not pmax]
    if perfil is None:
        return None, False
    a = _area_curva(perfil)
    _area_perfil_diagnostico = a
    if a <= 0.0:
        _motivo_fallo = "area nula"
        return None, False
    return perfil, True


def _excluir_3d(env_vol, cajas, h, z, area_losa, hueco_m2):
    """Boolean 3D de respaldo (Rhino 8): resta los solidos del nucleo al
    volumen del envelope. Verifica el volumen resultante. Devuelve (brep, ok);
    el motivo del fallo queda en la global _motivo_3d (v07.12)."""
    global _motivo_3d
    _motivo_3d = ""
    try:
        if env_vol is None:
            _motivo_3d = "volumen base None"
            return None, False
        huecos = []
        for cc in cajas:
            v = _extruir(cc, h, z)
            if v is not None:
                huecos.append(v)
        if not huecos:
            _motivo_3d = "extrucion del hueco fallo"
            return None, False
        # v07.12: resta los huecos UNO A UNO con la firma (Brep, Brep, tol).
        # Pasar (Brep, [Brep]) resuelve en Rhino 8 la sobrecarga IEnumerable y
        # falla con "expected IEnumerable[Brep], got Brep".
        piezas = [env_vol]
        try:
            for hh in huecos:
                nuevos = []
                for p in piezas:
                    d = rg.Brep.CreateBooleanDifference(p, hh, 0.01)
                    if d is None or len(d) == 0:
                        _motivo_3d = "boolean sin resultado"
                        return None, False
                    nuevos.extend(d)
                piezas = nuevos
                if not piezas:
                    _motivo_3d = "boolean sin resultado"
                    return None, False
            res = piezas
        except Exception as ex:
            _motivo_3d = "boolean excepcion: {}".format(str(ex))
            return None, False
        vol = 0.0
        for r in res:
            vol += r.GetVolume()
        esperado = (area_losa - hueco_m2) * h
        if abs(vol - esperado) > 0.03 * (area_losa * h):
            _motivo_3d = "volumen {:.1f} vs {:.1f}".format(vol, esperado)
            return None, False
        return res, True
    except Exception as ex:
        _motivo_3d = "excepcion: {}".format(str(ex))
        return None, False


def _vertices_de_curva(crv):
    """Vertices (Point3d) de una curva plana. ToPolyline + fallback
    TryGetPolyline (mismo patron que LADOS_v06)."""
    if crv is None:
        return []
    pts = []
    try:
        poly = crv.ToPolyline(0.05)
        if poly is not None:
            for i in range(poly.Count):
                pts.append(poly[i])
    except Exception:
        pts = []
    if not pts:
        try:
            ok, poly = crv.TryGetPolyline()
            if ok and poly is not None:
                for i in range(poly.Count):
                    pts.append(poly[i])
        except Exception:
            pts = []
    return pts


def _a_puntos(item):
    """Normaliza una entrada GH a lista de Point3d (lista/DataTree/Goo/Curve)."""
    if item is None:
        return []
    if isinstance(item, (list, tuple)):
        out = []
        for x in item:
            out.extend(_a_puntos(x))
        return out
    if isinstance(item, rg.Point3d):
        return [item]
    if isinstance(item, rg.Curve):
        return _vertices_de_curva(item)
    branches = getattr(item, "Branches", None)
    if branches is not None:
        out = []
        for br in branches:
            out.extend(_a_puntos(list(br)))
        return out
    v = getattr(item, "Value", None)
    if v is None:
        v = getattr(item, "Point", None)
    if v is None:
        return []
    return _a_puntos(v)


def _medianeira_info(lote_vertices, lados_info):
    """Medianera mas larga (Lateral/Posterior; evita Frontal y EspacioPublico).
    Usa dx/dy/mx/my del lado (LADOS_v06.1+) para NO depender del orden de
    lote_vertices; si no estan, cae a lote_vertices[id] (legacy).
    Devuelve dict {ang, nx, ny, long, mx, my, id} o None.
      ang = angulo del borde (rad)
      (nx, ny) = normal interior (hacia el centroide del lote)
      (mx, my) = punto medio del borde"""
    n = len(lote_vertices)
    if n < 3:
        return None
    medianeras = [l for l in lados_info
                  if l.get("clasificacion") in ("Lateral", "Posterior")]
    if not medianeras:
        return None
    mejor = None
    mejor_long = -1.0
    for l in medianeras:
        i = int(l.get("id", -1))
        dx = l.get("dx")
        dy = l.get("dy")
        if dx is None or dy is None:
            if i < 0 or i >= n:
                continue
            p1 = lote_vertices[i]
            p2 = lote_vertices[(i + 1) % n]
            dx = p2.X - p1.X
            dy = p2.Y - p1.Y
            src = "vertices"
        else:
            src = "lados"
        L = math.hypot(dx, dy)
        if L > mejor_long:
            mejor_long = L
            mejor = {"id": i, "dx": dx, "dy": dy,
                     "mx": l.get("mx"), "my": l.get("my"), "src": src}
    if mejor is None:
        return None
    dx = mejor["dx"]
    dy = mejor["dy"]
    ang = math.atan2(dy, dx)
    mx = mejor["mx"]
    my = mejor["my"]
    if mx is None or my is None:
        i = mejor["id"]
        p1 = lote_vertices[i]
        p2 = lote_vertices[(i + 1) % n]
        mx = (p1.X + p2.X) / 2.0
        my = (p1.Y + p2.Y) / 2.0
    cx = sum(v.X for v in lote_vertices) / n
    cy = sum(v.Y for v in lote_vertices) / n
    nx = -math.sin(ang)
    ny = math.cos(ang)
    if (cx - mx) * nx + (cy - my) * ny < 0.0:
        nx = -nx
        ny = -ny
    return {"ang": ang, "nx": nx, "ny": ny,
            "long": mejor_long, "mx": mx, "my": my, "id": mejor["id"],
            "src": mejor.get("src", "vertices")}


def _caja_rotada(cx, cy, ancho, largo, ang):
    """Rectangulo 2D con 'ancho' (lado corto) paralelo al angulo 'ang' (rad)."""
    a2 = ancho / 2.0
    l2 = largo / 2.0
    cosA = math.cos(ang)
    sinA = math.sin(ang)
    base = [(-a2, -l2), (a2, -l2), (a2, l2), (-a2, l2), (-a2, -l2)]
    pts = []
    for bx, by in base:
        rx = bx * cosA - by * sinA
        ry = bx * sinA + by * cosA
        pts.append(rg.Point3d(cx + rx, cy + ry, 0.0))
    return rg.PolylineCurve(pts)


def _caja_solido_rot(cx, cy, dx, dy, ancho_m, largo_m, ang):
    """Solido de la disposicion (dx/dy en el marco local del bloque) rotado
    por 'ang'. En el marco local, local X = lado corto, local Y = lado largo."""
    cosA = math.cos(ang)
    sinA = math.sin(ang)
    wx = cx + dx * cosA - dy * sinA
    wy = cy + dx * sinA + dy * cosA
    return _caja_rotada(wx, wy, ancho_m, largo_m, ang)


def _mejor_posicion(crv_piso, candidatos):
    """candidatos: lista de (caja, cx, cy, ang). Devuelve la de mayor area de
    interseccion: (piezas_interseccion, area, cx, cy, ang) o None."""
    mejor = None
    mejor_area = -1.0
    for caja, cx, cy, ang in candidatos:
        try:
            inter = rg.Curve.CreateBooleanIntersection(crv_piso, caja, 0.01)
        except Exception:
            inter = None
        if inter is None or len(inter) == 0:
            continue
        aa = 0.0
        for it in inter:
            aa += _area_curva(it)
        if aa > mejor_area:
            mejor_area = aa
            mejor = (inter, aa, cx, cy, ang)
    return mejor


# ------------------------------------------------------------------ MAIN

def _usos_no_nucleo(usos):
    """Usos de un piso SIN el pseudo-uso 'Nucleo' (dicts con 'uso' y
    'area_bruta'). El Nucleo es circulacion/servicios, no un uso de area."""
    out = []
    for u in usos:
        if u.get("uso", "") != "Nucleo":
            out.append(u)
    return out


def _rect_curva(x0, y0, x1, y1):
    """Polilinea cerrada de un rectangulo (x0,y0)-(x1,y1) en Z=0, para
    recortes booleanos. Se evita rg.Rectangle3d (no expuesto al namespace
    Python de Rhino 8, igual que rg.Rectangle)."""
    pts = [rg.Point3d(x0, y0, 0.0), rg.Point3d(x1, y0, 0.0),
           rg.Point3d(x1, y1, 0.0), rg.Point3d(x0, y1, 0.0),
           rg.Point3d(x0, y0, 0.0)]
    return rg.PolylineCurve(pts)


def _repartir_usos(crv_piso, usos_ok, area_losa):
    """Reparte la huella de un piso mixto en sub-regiones por uso, cortando a
    lo largo del eje dominante del bounding box (proporcional al area_bruta).
    Devuelve lista de (uso, curva_pieza). Best-effort: si un recorte falla, la
    pieza restante va al uso siguiente (nunca deja geometria duplicada)."""
    total = 0.0
    for u in usos_ok:
        total += float(u.get("area_bruta", 0.0) or 0.0)
    if total <= 0.0:
        return [(u.get("uso", ""), crv_piso) for u in usos_ok]
    usos_ord = sorted(usos_ok,
                      key=lambda u: -float(u.get("area_bruta", 0.0) or 0.0))
    bbox = crv_piso.GetBoundingBox(True)
    minx, miny = bbox.Min.X, bbox.Min.Y
    maxx, maxy = bbox.Max.X, bbox.Max.Y
    dx = maxx - minx
    dy = maxy - miny
    eje_x = (dx >= dy)
    lo = minx if eje_x else miny
    span = dx if eje_x else dy
    if span <= 1e-9:
        return [(usos_ord[0].get("uso", ""), crv_piso)]
    resultado = []
    acum = 0.0
    resto = crv_piso
    for i, u in enumerate(usos_ord[:-1]):
        acum += float(u.get("area_bruta", 0.0) or 0.0)
        corte = lo + span * (acum / total)
        if eje_x:
            clip = _rect_curva(minx, miny, corte, maxy)
        else:
            clip = _rect_curva(minx, miny, maxx, corte)
        pieza = None
        try:
            inter = rg.Curve.CreateBooleanIntersection(resto, clip, 0.01)
        except Exception:
            inter = None
        if inter and len(inter) > 0:
            pieza = _unir_piezas(inter)
        if pieza is None:
            pieza = resto
        resultado.append((u.get("uso", ""), pieza))
        try:
            dif = rg.Curve.CreateBooleanDifference(resto, clip, 0.01)
        except Exception:
            dif = None
        if dif and len(dif) > 0:
            resto = _unir_piezas(dif)
        else:
            resto = pieza
    resultado.append((usos_ord[-1].get("uso", ""), resto))
    return resultado


def _a_curvas(item):
    """Normaliza una entrada GH a lista de curvas Rhino. Acepta:
    - curvas Rhino directas (PolylineCurve, Curve)
    - listas/tuplas (aplanadas recursivamente)
    - DataTree de Grasshopper (.Branches)
    - objetos Goo (GH_Curve / GH_ObjectWrapper: .Value / .Curve)
    Evita el 'Type conversion failed from Goo to Curve'."""
    if item is None:
        return []
    if isinstance(item, (list, tuple)):
        out = []
        for x in item:
            out.extend(_a_curvas(x))
        return out
    if isinstance(item, rg.Curve):
        return [item]
    branches = getattr(item, "Branches", None)
    if branches is not None:
        out = []
        for br in branches:
            out.extend(_a_curvas(list(br)))
        return out
    v = getattr(item, "Value", None)
    if v is None:
        v = getattr(item, "Curve", None)
    if v is None:
        return []
    return _a_curvas(v)


def _unir_piezas(piezas):
    """Une las piezas de un piso (si quedo partido) en una curva; si no se
    pueden unir, devuelve la pieza de mayor area. Nunca intersectante."""
    if not piezas:
        return None
    if len(piezas) == 1:
        return piezas[0]
    try:
        un = rg.Curve.CreateBooleanUnion(piezas, 0.01)
        if un and len(un) == 1:
            return un[0]
    except:
        pass
    mejor = piezas[0]
    ma = -1.0
    for c in piezas:
        ap = rg.AreaMassProperties.Compute(c)
        a = ap.Area if ap else 0.0
        if a > ma:
            ma = a
            mejor = c
    return mejor


def _resolver_json(ruta):
    """Resuelve la ruta del JSON: absoluta > relativa al proyecto > busqueda
    del basename bajo src/fase-3-masa. Devuelve ruta existente o ''."""
    if not ruta:
        return ""
    if os.path.exists(ruta):
        return ruta
    base_proyecto = r"D:\Work\PROJECTS\DiseñoParametrico"
    for cand in (os.path.join(base_proyecto, ruta),
                 os.path.join(base_proyecto, "src", "fase-3-masa", ruta)):
        if os.path.exists(cand):
            return cand
    nombre = os.path.basename(ruta)
    for raiz, _, archivos in os.walk(os.path.join(base_proyecto, "src", "fase-3-masa", "casos")):
        if nombre in archivos:
            return os.path.join(raiz, nombre)
    return ""


env_por_piso_raw = globals().get("envelope_por_piso", None)   # v07+ preferida
env_crv_raw = globals().get("envelope_curve", None)            # fallback v06
json_path_raw = globals().get("json_path", None)
floor_h_raw = globals().get("floor_height", 3.0)
salida_morph_raw = globals().get("salida_morph", False)        # v07.9
sides_json_raw = globals().get("sides_table_json", None)       # v07.14
lote_vertices_raw = globals().get("lote_vertices", None)       # v07.14
alineacion_nucleo_raw = globals().get("alineacion_nucleo", 1)  # v07.18
salida_zona_raw = globals().get("salida_zona", False)

json_path = str(unwrap(json_path_raw)) if json_path_raw else ""
json_path = _resolver_json(json_path)
floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0

# v07.9: interruptor de salida. True -> las salidas principales emiten MESH
# (listas para el componente Morph de ArchiCAD, que exige Mesh);
# False (default) -> Brep en las salidas principales + *_mesh por separado.
sm = salida_morph_raw
if isinstance(sm, bool):
    salida_morph = sm
else:
    txt = str(unwrap(sm)).strip().lower()
    salida_morph = txt in ("true", "1", "si", "yes")

# v08.0: interruptor de salida para Zonas de ArchiCAD
# True -> las salidas principales emiten datos para componentes Zona (perimetros 2D, atributos)
# False (default) -> comportamiento compatible con versiones anteriores (Morph o Brep segun salida_morph)
sz = salida_zona_raw
if isinstance(sz, bool):
    salida_zona = sz
else:
    txt = str(unwrap(sz)).strip().lower()
    salida_zona = txt in ("true", "1", "si", "yes")

# Normaliza: env_por_piso = lista de PISOS; cada piso = lista de curvas
# (piezas). Acepta lista, DataTree, Goo y Curve[] (pisos partidos).
env_por_piso = []
if env_por_piso_raw is not None:
    _branches = getattr(env_por_piso_raw, "Branches", None)
    if _branches is not None:
        items = [list(br) for br in _branches]
    elif isinstance(env_por_piso_raw, (list, tuple)):
        items = env_por_piso_raw
    else:
        items = [env_por_piso_raw]
    for it in items:
        cs = _a_curvas(it)
        if cs:
            env_por_piso.append(cs)
env_fb = _a_curvas(env_crv_raw)  # fallback: piezas de la curva unica

# v07.14: medianera (Lateral/Posterior) desde LADOS_v06 + vertices del lote
lados_info = []
if sides_json_raw:
    try:
        _sd = json.loads(str(unwrap(sides_json_raw)))
        if isinstance(_sd, dict):
            lados_info = _sd.get("lados", [])
    except Exception:
        lados_info = []
lote_vertices = _a_puntos(lote_vertices_raw)
med_info = _medianeira_info(lote_vertices, lados_info)
if med_info is None:
    if len(lote_vertices) < 3:
        med_desc = "medianera NO detectada (vertices {}<3: revisar List Access)".format(len(lote_vertices))
    elif not lados_info:
        med_desc = "medianera NO detectada (sin sides_table_json)"
    else:
        med_desc = "medianera NO detectada (sin lado Lateral/Posterior)"
else:
    med_desc = "med ang {:.1f}deg L{:.1f}m id{} n{}/{} [{}]".format(
        math.degrees(med_info["ang"]), med_info["long"],
        med_info["id"], len(lote_vertices), len(lados_info),
        med_info.get("src", "vertices"))
    if len(lote_vertices) != len(lados_info):
        med_desc += " [WARN cableado lote_vertices != LADOS_v06]"

# v07.18: selector de alineacion (preferencia de diseno)
#   0 = centro (barrido 3x3, version actual)
#   1 = medianera (Lateral/Posterior, lado corto paralelo) — default
#   2 = opuesta (lado contrario a la medianera; contradice 0 y 1)
try:
    modo = int(unwrap(alineacion_nucleo_raw))
except Exception:
    modo = 1
if modo < 0:
    modo = 0
elif modo > 2:
    modo = 2
modo_desc = {0: "centro", 1: "medianera", 2: "opuesta"}.get(modo, "centro")
med_debug = ""  # diagnostico de colocacion medianera (primer piso)

volumenes_principales = []
volumenes_circulacion = []
volumenes_servicios = []
volumenes_nucleo = []
losas = []
etiquetas = []
volumenes_principales_mesh = []
volumenes_circulacion_mesh = []
volumenes_servicios_mesh = []
volumenes_nucleo_mesh = []
losas_mesh = []
volumenes_por_uso = []
usos_etiquetas = []
usos_pisos = []
volumenes_por_uso_mesh = []
circulacion_pisos = []
servicios_pisos = []
losas_pisos = []
nucleo_pisos = []
# Zona outputs
zonas_perimetros = []      # List of List[Point3d] - 2D perimeters of zones
zonas_pisos = []           # List[int] - floor number for each zone
zonas_atributos = []       # List[str] - JSON attributes for each zone
zonas_alturas = []         # List[float] - height of each zone
mensaje = ""

if not env_por_piso and not env_fb:
    mensaje = ("VOLUM v08.0 | ERROR: sin curva de envelope. Cablear la salida "
               "envelope_por_piso (lista, PREFERIDA) o envelope_curve de "
               "F1_ETAPA2_NORMATIVA_v07.")
elif not json_path:
    mensaje = ("VOLUM v08.0 | ERROR: json_path invalido ('{}'). Cablear la ruta al "
               "programa-areas.json (absoluta o relativa al proyecto)").format(
        str(unwrap(json_path_raw)) if json_path_raw else "")
else:
    try:
        with io.open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        programa = data.get("programa_pisos", [])
        nucleo_info = data.get("nucleo", {})
        disp = nucleo_info.get("disposicion", [])
        hueco_m2 = float(nucleo_info.get("hueco_m2_piso", 0.0) or 0.0)
        circ_m2 = float(nucleo_info.get("circulacion_m2", 0.0) or 0.0)
        serv_m2 = float(nucleo_info.get("servicios_m2", 0.0) or 0.0)

        # Curva de referencia para el nucleo: PISO 1 (el layout se diseno
        # contra el envelope base; el nucleo sube vertical).
        if env_por_piso:
            crv_ref = env_por_piso[0][0]
        else:
            crv_ref = env_fb[0]
        ap = rg.AreaMassProperties.Compute(crv_ref)
        if ap is None:
            mensaje = "VOLUM v08.0 | ERROR: curva de envelope sin area (revisar NORMATIVA_v07)."
        else:
            area_losa_ref = ap.Area
            centroide = ap.Centroid if ap.Centroid else rg.Point3d(0, 0, 0)
            cx0, cy0 = centroide.X, centroide.Y

            # Solidos del nucleo (circulacion + servicios): extrusiones que
            # rellenan el hueco. Se generan aparte; NO se usan para recortar.
            cajas = []
            for c in disp:
                cajas.append(_caja_curva(cx0 + c.get("dx", 0.0), cy0 + c.get("dy", 0.0),
                                         c.get("ancho_m", 2.0), c.get("largo_m", 4.0)))

            # BLOQUE del nucleo (el hueco REAL de la losa): nucleo.bloque del
            # JSON (ancho x largo, centrado en el centroide). Si no esta,
            # se deriva del bounding box de la disposicion. La losa se perfora
            # con el BLOQUE COMPLETO (incluye el aire interior de 8,76 m2:
            # circulacion interna del nucleo), no con la suma de solidos
            # (39,8 m2) — esa inconsistencia hacia fallar la validacion 2%.
            bloque_info = nucleo_info.get("bloque", {})
            try:
                b_ancho = float(bloque_info.get("ancho_m", 0.0) or 0.0)
                b_largo = float(bloque_info.get("largo_m", 0.0) or 0.0)
                b_dx = float(bloque_info.get("dx", 0.0) or 0.0)
                b_dy = float(bloque_info.get("dy", 0.0) or 0.0)
            except Exception:
                b_ancho = b_largo = b_dx = b_dy = 0.0
            if b_ancho <= 0 or b_largo <= 0:
                xs = []
                ys = []
                for c in disp:
                    xs.append(c.get("dx", 0.0) - c.get("ancho_m", 2.0) / 2.0)
                    xs.append(c.get("dx", 0.0) + c.get("ancho_m", 2.0) / 2.0)
                    ys.append(c.get("dy", 0.0) - c.get("largo_m", 4.0) / 2.0)
                    ys.append(c.get("dy", 0.0) + c.get("largo_m", 4.0) / 2.0)
                b_ancho = max(xs) - min(xs)
                b_largo = max(ys) - min(ys)
            caja_bloque = _caja_curva(cx0 + b_dx, cy0 + b_dy, b_ancho, b_largo)
            cajas_recorte = [caja_bloque]
            solidos_m2 = circ_m2 + serv_m2
            aire_interior = max(0.0, hueco_m2 - solidos_m2)

            n_pisos = 0
            n_huecos = 0
            n_omitidos = 0
            n_medianeira = 0
            mejor_area_med = -1.0
            omitidos_detalle = []
            _area_perfil_diagnostico = 0.0
            _motivo_fallo = ""
            _motivo_3d = ""
            _agujeros_global = []
            detalle_bool = "curvas"
            fuente_env = "por_piso (escalonado+voladizos)" if env_por_piso \
                else "envelope_curve unica (compat)"

            for idx_piso, p in enumerate(programa):
                z = float(p.get("altura_z", 0.0) or 0.0)
                piso_num = p.get("piso", 0)
                usos = p.get("usos", [])
                h_piso = float(p.get("altura_piso", floor_h) or floor_h)
                if h_piso <= 0.0:
                    h_piso = floor_h

                # Piezas del piso: la i-esima de la lista si alcanza; si no, la
                # ultima; si no hay lista, el fallback. Union para el perfil.
                if env_por_piso:
                    piezas = env_por_piso[idx_piso] if idx_piso < len(env_por_piso) \
                        else env_por_piso[-1]
                else:
                    piezas = env_fb
                crv_piso = _unir_piezas(piezas)
                if crv_piso is None:
                    n_omitidos += 1
                    omitidos_detalle.append("P{} sin curva".format(piso_num))
                    continue
                ap_piso = rg.AreaMassProperties.Compute(crv_piso)
                if ap_piso is None:
                    n_omitidos += 1
                    omitidos_detalle.append("P{} sin area".format(piso_num))
                    continue
                area_losa = ap_piso.Area

                # Nucleo: v07.18 con SELECTOR de alineacion (alineacion_nucleo):
                #   0 = centro (barrido 3x3, version actual)
                #   1 = medianera (Lateral/Posterior, lado corto paralelo) — default
                #   2 = opuesta (lado contrario a la medianera; contradice 0 y 1)
                # ROTACION real del borde (lotes diagonales). Si no cabe
                # (>=95%), barrido 3x3 alrededor del centroide como respaldo.
                cxp = ap_piso.Centroid.X if ap_piso.Centroid else cx0
                cyp = ap_piso.Centroid.Y if ap_piso.Centroid else cy0
                area_bloque_m2 = b_ancho * b_largo
                paso = 0.75
                mejor_pieza = None
                mejor_area = -1.0
                mejor_cx = cxp + b_dx
                mejor_cy = cyp + b_dy
                ang_nucleo = 0.0

                # candidatos contra un borde (medianera u opuesta)
                cand_med = []
                if modo in (1, 2) and med_info is not None:
                    _ang = med_info["ang"]
                    _nx = med_info["nx"]
                    _ny = med_info["ny"]
                    _mx = med_info["mx"]
                    _my = med_info["my"]
                    fv = _vertices_de_curva(crv_piso)
                    # bordes de la losa paralelos a la medianera: modo 1 usa el
                    # mas cercano a ella, modo 2 el mas lejano (lado opuesto)
                    best_edge = None
                    best_d = 1e18 if modo == 1 else -1.0
                    for i in range(len(fv)):
                        q1 = fv[i]
                        q2 = fv[(i + 1) % len(fv)]
                        ddx = q2.X - q1.X
                        ddy = q2.Y - q1.Y
                        L = math.hypot(ddx, ddy)
                        if L < 1e-6:
                            continue
                        par = abs(ddx * math.cos(_ang) + ddy * math.sin(_ang)) / L
                        if par < 0.90:
                            continue
                        qmx = (q1.X + q2.X) / 2.0
                        qmy = (q1.Y + q2.Y) / 2.0
                        dperp = abs((qmx - _mx) * math.sin(_ang)
                                    - (qmy - _my) * math.cos(_ang))
                        if modo == 1:
                            if dperp < best_d:
                                best_d = dperp
                                best_edge = (q1, q2)
                        else:
                            if dperp > best_d:
                                best_d = dperp
                                best_edge = (q1, q2)
                    if best_edge is not None:
                        q1, q2 = best_edge
                        emx = (q1.X + q2.X) / 2.0
                        emy = (q1.Y + q2.Y) / 2.0
                        edx = q2.X - q1.X
                        edy = q2.Y - q1.Y
                        eL = math.hypot(edx, edy)
                        if eL < 1e-6:
                            eL = 1.0
                        # v07.22: rotacion y normal desde el BORDE DE LA LOSA
                        # (no desde la medianera del lote), mas robusto.
                        ang_edge = math.atan2(edy, edx)
                        if modo == 1:
                            _ix = -edy / eL
                            _iy = edx / eL
                        else:
                            _ix = edy / eL
                            _iy = -edx / eL
                        if (cxp - emx) * _ix + (cyp - emy) * _iy < 0.0:
                            _ix = -_ix
                            _iy = -_iy
                        if not med_debug:
                            _bcx0 = emx + _ix * (b_largo / 2.0)
                            _bcy0 = emy + _iy * (b_largo / 2.0)
                            med_debug = (" | fv{} edge1 dperp{:.2f} "
                                         "bc({:.1f},{:.1f}) fc({:.1f},{:.1f})").format(
                                len(fv), best_d, _bcx0, _bcy0, cxp, cyp)
                        for _t in (-1, 0, 1):
                            _cx = emx + (edx / eL) * (_t * paso) + _ix * (b_largo / 2.0)
                            _cy = emy + (edy / eL) * (_t * paso) + _iy * (b_largo / 2.0)
                            cand_med.append(
                                (_caja_rotada(_cx, _cy, b_ancho, b_largo, ang_edge),
                                 _cx, _cy, ang_edge))
                    elif not med_debug:
                        med_debug = " | fv{} edge0 tipo{}".format(
                            len(fv), type(crv_piso).__name__)

                if cand_med:
                    _mejor = _mejor_posicion(crv_piso, cand_med)
                    if _mejor is not None:
                        if _mejor[1] > mejor_area_med:
                            mejor_area_med = _mejor[1]
                        if _mejor[1] >= 0.95 * area_bloque_m2:
                            mejor_pieza, mejor_area, mejor_cx, mejor_cy, ang_nucleo = _mejor
                            n_medianeira += 1

                # centro (modo 0) o respaldo: barrido 3x3 alrededor del centroide
                if mejor_pieza is None or mejor_area < 0.95 * area_bloque_m2:
                    cand_cen = []
                    for ix in (-1, 0, 1):
                        for iy in (-1, 0, 1):
                            _cx = cxp + b_dx + ix * paso
                            _cy = cyp + b_dy + iy * paso
                            cand_cen.append(
                                (_caja_curva(_cx, _cy, b_ancho, b_largo),
                                 _cx, _cy, 0.0))
                    _mejor = _mejor_posicion(crv_piso, cand_cen)
                    if _mejor is not None:
                        mejor_pieza, mejor_area, mejor_cx, mejor_cy, ang_nucleo = _mejor

                if mejor_pieza is None or mejor_area < 0.95 * area_bloque_m2:
                    n_omitidos += 1
                    omitidos_detalle.append(
                        "P{} nucleo no cabe (max interseccion {:.1f} m2 de {:.1f})".format(
                            piso_num, mejor_area, area_bloque_m2))
                    continue
                pieza_nucleo = mejor_pieza[0]
                if len(mejor_pieza) > 1:
                    u = rg.Curve.CreateBooleanUnion(mejor_pieza, 0.01)
                    if u and len(u) > 0:
                        pieza_nucleo = u[0]
                    else:
                        amax = -1.0
                        for it in mejor_pieza:
                            aa = _area_curva(it)
                            if aa > amax:
                                amax = aa
                                pieza_nucleo = it
                cajas_recorte = [pieza_nucleo]
                cajas_piso = []
                for c in disp:
                    cajas_piso.append(_caja_solido_rot(
                        mejor_cx, mejor_cy,
                        c.get("dx", 0.0), c.get("dy", 0.0),
                        c.get("ancho_m", 2.0), c.get("largo_m", 4.0),
                        ang_nucleo))

                # --- Hueco del nucleo SIN booleanos (v07.6) ---
                # La diferencia devuelve el contorno EXTERIOR + los AGUJEROS
                # como curvas separadas (la representacion de Rhino de una
                # region con hueco). La losa se construye con
                # CreatePlanarBreps([exterior] + agujeros) y el volumen
                # principal es la EXTRUSION de esa losa con hueco.
                perfil = None
                ok = False
                area_perfil = 0.0
                agujeros = []
                if cajas_recorte:
                    perfil, ok = _recortar_huecos(
                        crv_piso, cajas_recorte, area_losa, hueco_m2)
                    area_perfil = _area_perfil_diagnostico
                    agujeros = _agujeros_global
                    if ok:
                        detalle_bool = "curvas"
                if perfil is None:
                    perfil = crv_piso

                losa_hueco = None
                if ok:
                    # Losa con hueco SIN booleanos: contorno + agujeros.
                    # Si el agujero TOCA el borde (inner loop tangente), Rhino
                    # puede no crear la superficie: se reintenta con el agujero
                    # ENCOGIDO 2 cm (offset negativo) y con el perfil de la
                    # diferencia (que ya trae el mordisco si aplica).
                    candidatos = [agujeros]
                    if agujeros:
                        pieza_encogida = None
                        try:
                            pieza_encogida = agujeros[0].Offset(
                                -0.02, 0.01, rg.CurveOffsetCornerStyle.Sharp)
                        except Exception:
                            pieza_encogida = None
                        if pieza_encogida is not None:
                            candidatos.append([pieza_encogida])
                    candidatos.append([])
                    for ag in candidatos:
                        try:
                            lb = rg.Brep.CreatePlanarBreps([perfil] + ag, 0.01)
                        except Exception:
                            lb = None
                        if not lb or len(lb) == 0:
                            continue
                        ap_l = rg.AreaMassProperties.Compute(lb[0])
                        if ap_l is None:
                            continue
                        area_losa_h = ap_l.Area
                        esperado = area_losa - hueco_m2
                        if abs(area_losa_h - esperado) <= 0.02 * area_losa:
                            losa_hueco = lb[0]
                            _motivo_fallo = ""
                            break
                        _motivo_fallo = "losa-anillo area {:.1f} vs {:.1f}".format(
                            area_losa_h, esperado)
                    if losa_hueco is None:
                        if not _motivo_fallo:
                            _motivo_fallo = "losa-anillo no creo superficie"
                        ok = False

                if ok:
                    # Volumen principal: extrusion de la losa con hueco.
                    # v07.12: Extrusion.Create espera Curve o Surface — pasar
                    # el Brep (losa_hueco) devuelve None en Rhino 8; se extruye
                    # la CARA plana (que ya trae el hueco como inner loop) y se
                    # convierte a Brep.
                    env_vol = None
                    if losa_hueco is not None and losa_hueco.Faces.Count > 0:
                        try:
                            ext = rg.Extrusion.Create(losa_hueco.Faces[0], h_piso, True)
                            if ext is not None:
                                env_vol = ext.ToBrep()
                                if env_vol is not None:
                                    _subir_si_negativo(env_vol)
                        except Exception:
                            env_vol = None
                    if env_vol is not None:
                        env_vol.Translate(rg.Vector3d(0.0, 0.0, z))
                        losa_hueco.Translate(rg.Vector3d(0.0, 0.0, z))
                        losas.append(losa_hueco)

                        losas_pisos.append(piso_num)
                        m = _brep_a_mesh(losa_hueco)
                        if m is not None:
                            losas_mesh.append(m)
                        volumenes_principales.append(env_vol)
                        m = _brep_a_mesh(env_vol)
                        if m is not None:
                            volumenes_principales_mesh.append(m)
                        n_huecos += 1
                    else:
                        # Extrusion fallo: respaldo boolean 3D del volumen.
                        # La pieza se ENCOGE 2 cm (offset negativo): si el
                        # bloque toca el borde del piso, la extrucion del
                        # agujero toca la pared del volumen y el boolean 3D
                        # falla (None/multipieza); encogida, resta siempre
                        # (el hueco queda 2 cm menor, dentro de la tol).
                        pieza_resta = None
                        try:
                            pieza_resta = pieza_nucleo.Offset(
                                -0.02, 0.01, rg.CurveOffsetCornerStyle.Sharp)
                        except Exception:
                            pieza_resta = None
                        if pieza_resta is None:
                            pieza_resta = pieza_nucleo
                        env_vol = _extruir(perfil, h_piso, z)
                        res, ok3d = _excluir_3d(env_vol, [pieza_resta], h_piso, z,
                                                area_losa, hueco_m2)
                        if ok3d and res:
                            detalle_bool = "boolean3d"
                            env_vol = res[0]
                            for r in res[1:]:
                                volumenes_principales.append(r)
                                m = _brep_a_mesh(r)
                                if m is not None:
                                    volumenes_principales_mesh.append(m)
                            volumenes_principales.append(env_vol)
                            m = _brep_a_mesh(env_vol)
                            if m is not None:
                                volumenes_principales_mesh.append(m)
                            # v07.13: la losa con hueco YA existe (losa_hueco).
                            # No se reconstruye con CreatePlanarBreps sobre el
                            # volumen (esa firma espera IEnumerable[Curve], no
                            # un Brep -> "expected IEnumerable[Curve], got Brep").
                            losa_hueco.Translate(rg.Vector3d(0.0, 0.0, z))
                            losas.append(losa_hueco)

                            losas_pisos.append(piso_num)
                            m2 = _brep_a_mesh(losa_hueco)
                            if m2 is not None:
                                losas_mesh.append(m2)
                            n_huecos += 1
                        else:
                            ok = False
                            if not _motivo_fallo:
                                if _motivo_3d:
                                    _motivo_fallo = "extrusion + respaldo 3D fallo ({})".format(_motivo_3d)
                                else:
                                    _motivo_fallo = "extrusion + respaldo 3D fallo"

                if ok:
                    # Circulacion y servicios (llenan el hueco; no intersectan)
                    for cc, c in zip(cajas_piso, disp):
                        v = _extruir(cc, h_piso, z)
                        if v is None:
                            continue
                        m = _brep_a_mesh(v)
                        if c.get("tipo", "") == "servicios":
                            volumenes_servicios.append(v)

                            servicios_pisos.append(piso_num)
                            if m is not None:
                                volumenes_servicios_mesh.append(m)
                        else:
                            volumenes_circulacion.append(v)

                            circulacion_pisos.append(piso_num)
                            if m is not None:
                                volumenes_circulacion_mesh.append(m)

                    # --- Volumetria por uso (v07.24) ---
                    usos_ok = _usos_no_nucleo(usos)
                    if len(usos_ok) == 1:
                        nombre_uso = usos_ok[0].get("uso", "")
                        volumenes_por_uso.append(env_vol)
                        usos_etiquetas.append(nombre_uso)
                        usos_pisos.append(piso_num)
                        m_uso = _brep_a_mesh(env_vol)
                        if m_uso is not None:
                            volumenes_por_uso_mesh.append(m_uso)
                    elif len(usos_ok) > 1:
                        partes = _repartir_usos(crv_piso, usos_ok, area_losa)
                        for _nombre, _curva in partes:
                            _perfil_u = _curva
                            _aguj_u = []
                            if pieza_nucleo is not None:
                                try:
                                    _perfil_u, _ok_u = _recortar_huecos(
                                        _curva, [pieza_nucleo], area_losa, hueco_m2)
                                    if _perfil_u is None:
                                        _perfil_u = _curva
                                        _aguj_u = []
                                    else:
                                        _aguj_u = _agujeros_global
                                except Exception:
                                    _perfil_u = _curva
                                    _aguj_u = []
                            _vol_u = None
                            try:
                                _lb = rg.Brep.CreatePlanarBreps(
                                    [_perfil_u] + _aguj_u, 0.01)
                                if _lb and len(_lb) > 0 and _lb[0].Faces.Count > 0:
                                    _ext2 = rg.Extrusion.Create(
                                        _lb[0].Faces[0], h_piso, True)
                                    if _ext2 is not None:
                                        _vol_u = _ext2.ToBrep()
                            except Exception:
                                _vol_u = None
                            if _vol_u is not None:
                                _subir_si_negativo(_vol_u)
                                _vol_u.Translate(rg.Vector3d(0.0, 0.0, z))
                            else:
                                _vol_u = _extruir(_perfil_u, h_piso, z)
                            if _vol_u is None:
                                continue
                            volumenes_por_uso.append(_vol_u)
                            usos_etiquetas.append(_nombre)
                            usos_pisos.append(piso_num)
                            _m_u = _brep_a_mesh(_vol_u)
                            if _m_u is not None:
                                volumenes_por_uso_mesh.append(_m_u)
                    else:
                        volumenes_por_uso.append(env_vol)
                        usos_etiquetas.append("")
                        usos_pisos.append(piso_num)
                else:
                    # Regla: nunca geometria intersectante -> se omite el piso
                    n_omitidos += 1
                    if _motivo_fallo:
                        omitidos_detalle.append(
                            "P{} {}".format(piso_num, _motivo_fallo))
                    elif area_perfil > 0.0:
                        omitidos_detalle.append(
                            "P{} area {:.1f} vs {:.1f}".format(
                                piso_num, area_perfil, area_losa - hueco_m2))
                    else:
                        omitidos_detalle.append(
                            "P{} sin detalle".format(piso_num))

                usos_str = ", ".join(["{}: {:.0f}m2".format(u["uso"], u["area_bruta"])
                                      for u in usos if u["uso"] != "Nucleo"])
                etiquetas.append(
                    "Piso {}: {} | Circ {:.0f}m2 | Serv {:.0f}m2 | hueco {:.0f}m2".format(
                        piso_num, usos_str, circ_m2, serv_m2, hueco_m2))
                n_pisos += 1

            conteo_usos = {}
            for _u in usos_etiquetas:
                if _u:
                    conteo_usos[_u] = conteo_usos.get(_u, 0) + 1
            usos_resumen = ", ".join(["{}:{}".format(k, v)
                                      for k, v in conteo_usos.items()])
            if not usos_resumen:
                usos_resumen = "sin-usos"

            volumenes_nucleo = list(volumenes_circulacion) + list(volumenes_servicios)
            nucleo_pisos = list(circulacion_pisos) + list(servicios_pisos)
            volumenes_nucleo_mesh = (list(volumenes_circulacion_mesh) +
                                     list(volumenes_servicios_mesh))
            med_desc = med_desc + med_debug

            if n_omitidos == 0:
                mensaje = ("VOLUM v08.0 | OK | {} pisos | envelope: {} | "
                           "huecos excluidos {}/{} | boolean {} | "
                           "salidas: vol {}/{} losas {}/{} circ {}/{} serv {}/{} | "
                           "Circ {:.0f}m2 + Serv {:.0f}m2 = nucleo {:.0f}m2/piso | "
                           "nucleo[{}]: {} {}/{} medmax{:.1f}m2 | "
                           "usos: {} | salida: {}").format(
                    n_pisos, fuente_env, n_huecos, n_pisos, detalle_bool,
                    len(volumenes_principales), n_pisos, len(losas), n_pisos,
                    len(volumenes_circulacion), n_pisos, len(volumenes_servicios), n_pisos,
                    circ_m2, serv_m2, hueco_m2,
                    modo_desc, med_desc, n_medianeira, n_pisos,
                    mejor_area_med if mejor_area_med >= 0.0 else 0.0,
                    usos_resumen,
                    "MORPH (mesh)" if salida_morph else "BREP + mesh")
            else:
                mensaje = ("VOLUM v08.0 | ADVERTENCIA | {} pisos, {} omitidos (exclusion del "
                           "nucleo fallo; sin geometria intersectante) | huecos {}/{} | boolean {} | "
                           "envelope: {} | nucleo: bloque {:.0f}m2, solidos {:.0f}m2 "
                           "(aire interior {:.0f}m2) | nucleo[{}]: {} {}/{} medmax{:.1f}m2 | omitidos: {} | salida: {}").format(
                    n_pisos, n_omitidos, n_huecos, n_pisos, detalle_bool, fuente_env,
                    hueco_m2, solidos_m2, aire_interior,
                    modo_desc, med_desc, n_medianeira, n_pisos,
                    mejor_area_med if mejor_area_med >= 0.0 else 0.0,
                    "; ".join(omitidos_detalle),
                    "MORPH (mesh)" if salida_morph else "BREP + mesh")

            # v07.9: interruptor de salida -> las principales emiten MESH
            if salida_morph:
                volumenes_principales = list(volumenes_principales_mesh)
                volumenes_circulacion = list(volumenes_circulacion_mesh)
                volumenes_servicios = list(volumenes_servicios_mesh)
                volumenes_nucleo = list(volumenes_nucleo_mesh)
                losas = list(losas_mesh)
                volumenes_por_uso = list(volumenes_por_uso_mesh)

            # v08.0: interruptor de salida -> las principales emiten datos para Zonas de ArchiCAD
            if salida_zona:
                # Preparar datos de zonas basados en volumetria por uso
                zonas_perimetros = []
                zonas_pisos = []
                zonas_atributos = []
                zonas_alturas = []

                # Re-procesar piso por piso para obtener perímetros 2D precisos de cada zona
                try:
                    altura_acumulada = 0.0  # Altura acumulada desde Z=0

                    for piso_idx, piso_data in enumerate(programa):
                        z = float(piso_data.get("altura_z", 0.0) or 0.0)
                        piso_num = piso_data.get("piso", piso_idx)
                        h_piso = float(piso_data.get("altura_piso", floor_h) or floor_h)
                        if h_piso <= 0.0:
                            h_piso = floor_h

                        # Obtener curva del piso (de envelope_por_piso o fallback)
                        if env_por_piso:
                            piezas_piso = env_por_piso[piso_idx] if piso_idx < len(env_por_piso) else env_por_piso[-1]
                        else:
                            piezas_piso = env_fb

                        # Unir piezas del piso
                        crv_piso = _unir_piezas(piezas_piso)
                        if crv_piso is None:
                            continue

                        # Calcular área del piso
                        ap_piso = rg.AreaMassProperties.Compute(crv_piso)
                        if ap_piso is None:
                            continue
                        area_losa = ap_piso.Area

                        # Preparar exclusión del núcleo (similar al procesamiento principal)
                        usos = piso_data.get("usos", [])
                        usos_ok = _usos_no_nucleo(usos)

                        # Si no hay usos (solo núcleo), continuar
                        if not usos_ok:
                            altura_acumulada += h_piso
                            continue

                        # Preparar datos del núcleo para exclusión
                        nucleo_info = data.get("nucleo", {})
                        disp = nucleo_info.get("disposicion", [])
                        hueco_m2 = float(nucleo_info.get("hueco_m2_piso", 0.0) or 0.0)

                        # Preparar cajas del núcleo (misma lógica que en procesamiento principal)
                        cajas = []
                        bloque_info = nucleo_info.get("bloque", {})
                        try:
                            b_ancho = float(bloque_info.get("ancho_m", 0.0) or 0.0)
                            b_largo = float(bloque_info.get("largo_m", 0.0) or 0.0)
                            b_dx = float(bloque_info.get("dx", 0.0) or 0.0)
                            b_dy = float(bloque_info.get("dy", 0.0) or 0.0)
                        except Exception:
                            b_ancho = b_largo = b_dx = b_dy = 0.0
                        if b_ancho <= 0 or b_largo <= 0:
                            xs = []
                            ys = []
                            for c in disp:
                                xs.append(c.get("dx", 0.0) - c.get("ancho_m", 2.0) / 2.0)
                                xs.append(c.get("dx", 0.0) + c.get("ancho_m", 2.0) / 2.0)
                                ys.append(c.get("dy", 0.0) - c.get("largo_m", 4.0) / 2.0)
                                ys.append(c.get("dy", 0.0) + c.get("largo_m", 4.0) / 2.0)
                            b_ancho = max(xs) - min(xs)
                            b_largo = max(ys) - min(ys)
                        caja_bloque = _caja_curva(cx0 + b_dx, cy0 + b_dy, b_ancho, b_largo)
                        cajas_recorte = [caja_bloque]

                        # Aplicar exclusión del núcleo al piso
                        perfil_piso = None
                        ok_piso = False
                        if cajas_recorte:
                            perfil_piso, ok_piso = _recortar_huecos(
                                crv_piso, cajas_recorte, area_losa, hueco_m2)
                            if perfil_piso is None:
                                perfil_piso = crv_piso

                        # Si la exclusión falló, usar el piso completo
                        if not ok_piso:
                            perfil_piso = crv_piso

                        # Dividir el piso por usos (usando la misma lógica que en procesamiento principal)
                        if len(usos_ok) == 1:
                            # Un solo uso: todo el piso (menos núcleo)
                            partes = [(usos_ok[0].get("uso", ""), perfil_piso)]
                        elif len(usos_ok) > 1:
                            # Múltiplos usos: repartir proporcionalmente
                            partes = _repartir_usos(perfil_piso, usos_ok, area_losa)
                        else:
                            # No debería ocurrir por el filtro anterior, pero por seguridad
                            continue

                        # Procesar cada zona (uso) del piso
                        for uso_nombre, curva_zona in partes:
                            if curva_zona is None:
                                continue

                            # Calcular área de la zona (2D)
                            area_zona = _area_curva(curva_zona)

                            # Obtener vértices del perímetro 2D
                            puntos_perimetro = _vertices_de_curva(curva_zona)
                            # Asegurar que esté cerrado (primer punto = último punto)
                            if puntos_perimetro and len(puntos_perimetro) > 0:
                                if puntos_perimetro[0].DistanceTo(puntos_perimetro[-1]) > 0.001:
                                    puntos_perimetro.append(puntos_perimetro[0])

                            # Calcular altura de la zona
                            zona_altura_base = altura_acumulada
                            zona_altura_centro = altura_acumulada + (h_piso / 2.0)

                            # Preparar atributos como JSON
                            import json as py_json
                            atributos = {
                                "uso": uso_nombre if uso_nombre else "desconocido",
                                "area_m2": round(area_zona, 2),
                                "piso": piso_num,
                                "altura_base_m": round(zona_altura_base, 2),
                                "altura_centro_m": round(zona_altura_centro, 2)
                            }

                            # Agregar datos a las listas de salida
                            zonas_perimetros.append(puntos_perimetro)
                            zonas_pisos.append(piso_num)
                            zonas_alturas.append(zona_altura_centro)
                            zonas_atributos.append(py_json.dumps(atributos, ensure_ascii=False))

                        # Incrementar altura acumulada para el siguiente piso
                        altura_acumulada += h_piso
                except Exception as e:
                    # En caso de error general, asegurar que las listas estén inicializadas vacías
                    zonas_perimetros = []
                    zonas_pisos = []
                    zonas_atributos = []
                    zonas_alturas = []

                
    except Exception as e:
        mensaje = "VOLUM v08.0 | ERROR: {}".format(str(e))

