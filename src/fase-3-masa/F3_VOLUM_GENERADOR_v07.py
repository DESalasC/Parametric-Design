"""
================================================================================
F3_VOLUM_GENERADOR_v07.py - Masa con nucleo EXCLUIDO y circulacion/servicios
separados (geometria para elementos nativos de ArchiCAD via Live Connection)
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (componente "Script", IronPython 2.7)
================================================================================

v07 (2026-08-16): correcciones solicitadas por el operador:
  1. PERIMETRO = envelope_por_piso de F1_ETAPA2_NORMATIVA_v07 (curva POR PISO:
     ocupacion escalonada + voladizos en pisos superiores; fallback a
     envelope_curve para compatibilidad v06). El componente recibe SIEMPRE la
     lista de curvas del NORMATIVA (o la curva unica como respaldo).
  2. EXCLUSION REAL del nucleo: diferencia de curvas secuencial (caja por caja)
     con verificacion de area; fallback a boolean 3D con verificacion de
     volumen. Regla: NUNCA se entrega geometria intersectante - si la exclusion
     falla, ese piso se omite y el mensaje lo reporta (huecos excluidos n/N).
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

SALIDAS:
  volumenes_principales   (List of Brep) - Masa por piso con el hueco del
                             nucleo EXCLUIDO (no intersecta circulacion/servicios)
  volumenes_circulacion   (List of Brep) - Escaleras + ascensores (solidos)
  volumenes_servicios     (List of Brep) - Ductos/basuras/cuarto tecnico (solidos)
  volumenes_nucleo        (List of Brep) - Compat v06: circulacion + servicios
  losas                   (List of Brep)  - Losas con hueco por piso
  etiquetas               (List of String)- Usos, circulacion y servicios por piso
  mensaje                 (String)         - Diagnostico (huecos n/N, fuente)

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


def _extruir(curva, h, z):
    try:
        ext = rg.Extrusion.Create(curva.ToNurbsCurve(), h, True)
        if ext is None:
            return None
        b = ext.ToBrep()
        if b is None:
            return None
        b.Translate(rg.Vector3d(0.0, 0.0, z))
        return b
    except Exception:
        return None


def _recortar_huecos(env_crv, cajas, area_losa, hueco_m2):
    """Diferencia secuencial curva-curva (overload estable en Rhino 8) con
    verificacion de area: perfil resultante debe medir area_losa - hueco_m2.
    Devuelve (perfil, ok)."""
    perfil = env_crv
    for cc in cajas:
        try:
            dif = rg.Curve.CreateBooleanDifference(perfil, cc, 0.01)
        except Exception:
            return None, False
        if dif is None or len(dif) != 1:
            return None, False
        perfil = dif[0]
    if perfil is None:
        return None, False
    a = _area_curva(perfil)
    if a <= 0.0:
        return None, False
    esperado = area_losa - hueco_m2
    if abs(a - esperado) > 0.02 * area_losa:
        return None, False
    return perfil, True


def _excluir_3d(env_vol, cajas, h, z, area_losa, hueco_m2):
    """Boolean 3D de respaldo (Rhino 8): resta los solidos del nucleo al
    volumen del envelope. Verifica el volumen resultante. Devuelve (brep, ok)."""
    try:
        huecos = []
        for cc in cajas:
            v = _extruir(cc, h, z)
            if v is not None:
                huecos.append(v)
        if not huecos:
            return None, False
        res = rg.Brep.CreateBooleanDifference(env_vol, huecos, 0.01)
        if res is None or len(res) == 0:
            return None, False
        vol = 0.0
        for r in res:
            vol += r.GetVolume()
        esperado = (area_losa - hueco_m2) * h
        if abs(vol - esperado) > 0.03 * (area_losa * h):
            return None, False
        return res, True
    except Exception:
        return None, False


# ------------------------------------------------------------------ MAIN

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
env_crv = globals().get("envelope_curve", None)                # fallback v06
json_path_raw = globals().get("json_path", None)
floor_h_raw = globals().get("floor_height", 3.0)

json_path = str(unwrap(json_path_raw)) if json_path_raw else ""
json_path = _resolver_json(json_path)
floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0

# Normaliza la lista de curvas por piso (lista > curva suelta > vacia)
env_por_piso = []
if env_por_piso_raw is not None:
    items = env_por_piso_raw if isinstance(env_por_piso_raw, list) else [env_por_piso_raw]
    env_por_piso = [c for c in items if c is not None]

volumenes_principales = []
volumenes_circulacion = []
volumenes_servicios = []
volumenes_nucleo = []
losas = []
etiquetas = []
mensaje = ""

if not env_por_piso and env_crv is None:
    mensaje = ("VOLUM v07 | ERROR: sin curva de envelope. Cablear la salida "
               "envelope_por_piso (lista, PREFERIDA) o envelope_curve de "
               "F1_ETAPA2_NORMATIVA_v07.")
elif not json_path:
    mensaje = ("VOLUM v07 | ERROR: json_path invalido ('{}'). Cablear la ruta al "
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
            crv_ref = env_por_piso[0]
        else:
            crv_ref = env_crv
        ap = rg.AreaMassProperties.Compute(crv_ref)
        if ap is None:
            mensaje = "VOLUM v07 | ERROR: curva de envelope sin area (revisar NORMATIVA_v07)."
        else:
            area_losa_ref = ap.Area
            centroide = ap.Centroid if ap.Centroid else rg.Point3d(0, 0, 0)
            cx0, cy0 = centroide.X, centroide.Y

            cajas = []
            for c in disp:
                cajas.append(_caja_curva(cx0 + c.get("dx", 0.0), cy0 + c.get("dy", 0.0),
                                         c.get("ancho_m", 2.0), c.get("largo_m", 4.0)))

            n_pisos = 0
            n_huecos = 0
            n_omitidos = 0
            detalle_bool = "curvas"
            fuente_env = "por_piso (NORMATIVA_v07, escalonado+voladizos)" if env_por_piso \
                else "envelope_curve unica (compat)"

            for idx_piso, p in enumerate(programa):
                z = float(p.get("altura_z", 0.0) or 0.0)
                piso_num = p.get("piso", 0)
                usos = p.get("usos", [])
                h_piso = float(p.get("altura_piso", floor_h) or floor_h)
                if h_piso <= 0.0:
                    h_piso = floor_h

                # Curva del piso: la i-esima de la lista si alcanza; si no, la
                # ultima disponible; si no hay lista, la unica (fallback).
                if env_por_piso:
                    crv_piso = env_por_piso[idx_piso] if idx_piso < len(env_por_piso) \
                        else env_por_piso[-1]
                else:
                    crv_piso = env_crv
                ap_piso = rg.AreaMassProperties.Compute(crv_piso)
                if ap_piso is None:
                    n_omitidos += 1
                    continue
                area_losa = ap_piso.Area

                perfil = None
                ok = False
                if len(cajas) > 0:
                    perfil, ok = _recortar_huecos(crv_piso, cajas, area_losa, hueco_m2)
                    if ok:
                        detalle_bool = "curvas"
                if perfil is None:
                    perfil = crv_piso

                if ok:
                    # Losa con hueco
                    lb = rg.Brep.CreatePlanarBreps(perfil, 0.01)
                    losa_hueco = None
                    if lb and len(lb) > 0:
                        losa_hueco = lb[0]
                        if len(lb) > 1:
                            lu = rg.Brep.CreateBooleanUnion(lb, 0.01)
                            if lu and len(lu) > 0:
                                losa_hueco = lu[0]
                    if losa_hueco is not None:
                        losa_hueco.Translate(rg.Vector3d(0.0, 0.0, z))
                        losas.append(losa_hueco)
                    # Volumen principal perforado
                    env_vol = _extruir(perfil, h_piso, z)
                    if env_vol is not None:
                        volumenes_principales.append(env_vol)
                        n_huecos += 1
                    # Circulacion y servicios (llenan el hueco; no intersectan)
                    for cc, c in zip(cajas, disp):
                        v = _extruir(cc, h_piso, z)
                        if v is None:
                            continue
                        if c.get("tipo", "") == "servicios":
                            volumenes_servicios.append(v)
                        else:
                            volumenes_circulacion.append(v)
                else:
                    # Respaldo boolean 3D
                    env_vol = _extruir(crv_piso, h_piso, z)
                    res, ok3d = _excluir_3d(env_vol, cajas, h_piso, z,
                                            area_losa, hueco_m2)
                    if ok3d and res:
                        detalle_bool = "boolean3d"
                        env_vol = res[0]
                        for r in res[1:]:
                            volumenes_principales.append(r)
                        volumenes_principales.append(env_vol)
                        lb = rg.Brep.CreatePlanarBreps(env_vol, 0.01)
                        if lb and len(lb) > 0:
                            lb[0].Translate(rg.Vector3d(0.0, 0.0, z))
                            losas.append(lb[0])
                        n_huecos += 1
                        for cc, c in zip(cajas, disp):
                            v = _extruir(cc, h_piso, z)
                            if v is None:
                                continue
                            if c.get("tipo", "") == "servicios":
                                volumenes_servicios.append(v)
                            else:
                                volumenes_circulacion.append(v)
                    else:
                        # Regla: nunca geometria intersectante -> se omite el piso
                        n_omitidos += 1

                usos_str = ", ".join(["{}: {:.0f}m2".format(u["uso"], u["area_bruta"])
                                      for u in usos if u["uso"] != "Nucleo"])
                etiquetas.append(
                    "Piso {}: {} | Circ {:.0f}m2 | Serv {:.0f}m2 | hueco {:.0f}m2".format(
                        piso_num, usos_str, circ_m2, serv_m2, hueco_m2))
                n_pisos += 1

            volumenes_nucleo = list(volumenes_circulacion) + list(volumenes_servicios)

            if n_omitidos == 0:
                mensaje = ("VOLUM v07 | OK | {} pisos | envelope: {} | "
                           "huecos excluidos {}/{} | boolean {} | Circ {:.0f}m2 + Serv {:.0f}m2 "
                           "= nucleo {:.0f}m2/piso").format(
                    n_pisos, fuente_env, n_huecos, n_pisos, detalle_bool,
                    circ_m2, serv_m2, hueco_m2)
            else:
                mensaje = ("VOLUM v07 | ADVERTENCIA | {} pisos, {} omitidos (exclusion del "
                           "nucleo fallo; sin geometria intersectante) | huecos {}/{} | boolean {} | "
                           "envelope: {}").format(
                    n_pisos, n_omitidos, n_huecos, n_pisos, detalle_bool, fuente_env)

    except Exception as e:
        mensaje = "VOLUM v07 | ERROR: {}".format(str(e))
