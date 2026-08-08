"""
Script: F1_NORMATIVA_APLICAR_v21.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote (Normativa)
Versión: 21
Descripción: 
    - Reconstrucción Topológica: Mueve el segmento posterior y alarga los laterales.
    - Cero operaciones booleanas: Evita triángulos y colapsos geométricos.
    - Altura Variable.
"""

import Rhino
import scriptcontext as sc
import json
import os
import math
import rhinoscriptsyntax as rs

# Inputs:
# lote_curve: Curve o Guid
# json_path: string
# normativa_path: string
# retiro_frontal: float
# retiro_lateral: float
# retiro_posterior: float
# sector_normativo: string

envelope_curve = None
altura_permitida = 0.0
ocupacion_real = 0.0
ic_real = 0.0
pisos_finales = 0
mensaje = "Esperando datos..."

def clean_path(p):
    if isinstance(p, list):
        if len(p) > 0: p = p[0]
        else: return ""
    return str(p).strip("[]'\" ")

j_path = clean_path(json_path) if 'json_path' in globals() else ""
n_path = clean_path(normativa_path) if 'normativa_path' in globals() else r"D:\WORK\PROJECTS\DiseñoParametrico\data\pot-bogota\normativa-upz.json"
sec_norm = str(sector_normativo).strip() if 'sector_normativo' in globals() and sector_normativo is not None else "default"

upz_lote = "default"
altura_pot = 12.0

if j_path and os.path.exists(j_path):
    try:
        with open(j_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        pot_data = data.get("pot_data", {})
        upz_lote = str(pot_data.get("upz", "default")).upper().strip()
        altura_pot = float(pot_data.get("altura_maxima_m", 12.0))
    except: pass

io_maximo = 0.70
ic_maximo = 2.0
norma_aplicada = "Default (Conservador)"

if n_path and os.path.exists(n_path):
    try:
        with open(n_path, 'r', encoding='utf-8') as f:
            normativa_db = json.load(f)
        upz_key = "UPZ_19_EL_PRADO" if "PRADO" in upz_lote else upz_lote
        if upz_key in normativa_db:
            upz_norma = normativa_db[upz_key]
            io_maximo = upz_norma.get("io_general", 0.70)
            sectores = upz_norma.get("sectores_normativos", {})
            if sec_norm in sectores:
                ic_maximo = sectores[sec_norm].get("ic_maximo", 2.0)
                norma_aplicada = "UPZ {} - Sector {}".format(upz_lote, sec_norm)
            else:
                ic_maximo = sectores.get("default", {}).get("ic_maximo", 2.0)
                norma_aplicada = "UPZ {} - Sector Default".format(upz_lote)
    except: pass

if lote_curve is not None: lote_curve = rs.coercecurve(lote_curve)

def get_inf_line_intersect(l1, l2):
    """Intersección de líneas infinitas a prueba de IronPython."""
    v1 = l1.Direction; v1.Unitize()
    c1 = Rhino.Geometry.LineCurve(l1.From - v1*1000000, l1.To + v1*1000000)
    v2 = l2.Direction; v2.Unitize()
    c2 = Rhino.Geometry.LineCurve(l2.From - v2*1000000, l2.To + v2*1000000)
    inter = Rhino.Geometry.Intersect.Intersection.CurveCurve(c1, c2, 0.01, 0.01)
    if inter and inter.Count > 0: return inter[0].PointA
    return None

if lote_curve and retiro_frontal is not None and altura_pot > 0:
    try:
        area_props = Rhino.Geometry.AreaMassProperties.Compute(lote_curve)
        area_lote_real = area_props.Area
        centroid = area_props.Centroid
        tolerancia = sc.doc.ModelAbsoluteTolerance
        
        # 1. Huella Base (Offset Uniforme)
        r_front = float(retiro_frontal)
        r_lat = float(retiro_lateral)
        r_post = float(retiro_posterior)
        retiro_base = min(r_front, r_lat, r_post)
        
        offset_curves = lote_curve.Offset(centroid, Rhino.Geometry.Vector3d.ZAxis, -retiro_base, tolerancia, Rhino.Geometry.CurveOffsetCornerStyle.Sharp)
        
        if offset_curves and len(offset_curves) > 0:
            env_curve = offset_curves[0]
            temp_area = Rhino.Geometry.AreaMassProperties.Compute(env_curve).Area
            if temp_area > area_lote_real:
                offset_curves = lote_curve.Offset(centroid, Rhino.Geometry.Vector3d.ZAxis, retiro_base, tolerancia, Rhino.Geometry.CurveOffsetCornerStyle.Sharp)
                env_curve = offset_curves[0] if offset_curves and len(offset_curves) > 0 else lote_curve
        else:
            env_curve = lote_curve
            
        area_envelope = Rhino.Geometry.AreaMassProperties.Compute(env_curve).Area
        if area_envelope <= 0: area_envelope = 1.0
        ocupacion_real = area_envelope / area_lote_real
        
        # 2. Auto-Patio por Reconstrucción Topológica
        if ocupacion_real > io_maximo:
            area_max_perm = io_maximo * area_lote_real
            delta_area = area_envelope - area_max_perm
            
            success, poly = env_curve.TryGetPolyline()
            if success and poly.Count > 3:
                n = poly.Count - 1 # Número de vértices únicos
                
                # Encontrar el segmento posterior (Max X+Y)
                max_score = -1e10
                rear_idx = 0
                for i in range(n):
                    p1 = poly[i]
                    p2 = poly[(i+1)%n]
                    mid = (p1 + p2) / 2.0
                    score = mid.X + mid.Y
                    if score > max_score:
                        max_score = score
                        rear_idx = i
                        
                rear_p1 = poly[rear_idx]
                rear_p2 = poly[(rear_idx+1)%n]
                rear_len = rear_p1.DistanceTo(rear_p2)
                
                if rear_len > 0:
                    patio_depth = (delta_area / rear_len) + 0.5 # +0.5m tolerancia
                    
                    # Vector hacia adentro (hacia el centroide)
                    rear_mid = (rear_p1 + rear_p2) / 2.0
                    vec_inward = Rhino.Geometry.Vector3d(centroid - rear_mid)
                    vec_inward.Unitize()
                    
                    # Mover línea posterior
                    p1_new = rear_p1 + vec_inward * patio_depth
                    p2_new = rear_p2 + vec_inward * patio_depth
                    moved_rear_line = Rhino.Geometry.Line(p1_new, p2_new)
                    
                    # Líneas laterales adyacentes
                    prev_idx = (rear_idx - 1 + n) % n
                    next_idx = (rear_idx + 1) % n
                    
                    prev_line = Rhino.Geometry.Line(poly[prev_idx], poly[rear_idx])
                    next_line = Rhino.Geometry.Line(poly[(rear_idx+1)%n], poly[(next_idx+1)%n])
                    
                    # Intersectar líneas laterales con la nueva línea posterior
                    inter1 = get_inf_line_intersect(prev_line, moved_rear_line)
                    inter2 = get_inf_line_intersect(next_line, moved_rear_line)
                    
                    if inter1 and inter2:
                        # Reconstruir polígono
                        new_pts = []
                        for i in range(n):
                            if i == rear_idx:
                                new_pts.append(inter1)
                                new_pts.append(inter2)
                            elif i != (rear_idx+1)%n: # No duplicar el vértice movido
                                new_pts.append(poly[i])
                                
                        new_pts.append(new_pts[0]) # Cerrar
                        env_curve = Rhino.Geometry.PolylineCurve(new_pts)
                        area_envelope = Rhino.Geometry.AreaMassProperties.Compute(env_curve).Area
                        ocupacion_real = area_envelope / area_lote_real
                        mensaje_io = "AUTO-PATIO TOPOLOGICO: Fondo empujado {:.1f}m. Lateral reconstruido.\n".format(patio_depth)
                    else:
                        mensaje_io = "ALERTA: Falló la intersección del patio.\n"
                else:
                    mensaje_io = "ALERTA: Segmento posterior sin longitud.\n"
            else:
                mensaje_io = "ALERTA: La huella no es una polilínea válida.\n"
        else:
            mensaje_io = "IO válido.\n"
            
        envelope_curve = env_curve
        
        # 3. Altura Variable
        ALTURA_MAX_ENTREPISO = 3.8
        ALTURA_MIN_ENTREPISO = 2.5
        
        pisos_max_altura = int(altura_pot / ALTURA_MIN_ENTREPISO)
        pisos_max_ic = int((ic_maximo * area_lote_real) / area_envelope)
        
        pisos_habitables = min(pisos_max_altura, pisos_max_ic)
        pisos_totales = pisos_habitables + 1
        
        if pisos_totales * ALTURA_MIN_ENTREPISO <= altura_pot:
            altura_entrepiso = min(ALTURA_MAX_ENTREPISO, altura_pot / pisos_totales)
            altura_final = altura_entrepiso * pisos_totales
        else:
            pisos_totales = pisos_habitables
            altura_entrepiso = min(ALTURA_MAX_ENTREPISO, altura_pot / pisos_totales)
            altura_final = altura_entrepiso * pisos_totales
            
        if pisos_max_ic < pisos_max_altura:
            mensaje_ic = "RESTRICCIÓN IC: {} pisos habitables.\n".format(pisos_habitables)
        else:
            mensaje_ic = "Altura POT maximizada ({} hab + 1 serv).\n".format(pisos_habitables)
            
        altura_permitida = altura_final
        pisos_finales = pisos_totales
        
        ic_real = (area_envelope * pisos_habitables) / area_lote_real
        
        mensaje = "--- RESULTADO NORMATIVO ---\n"
        mensaje += "Norma: {}\n".format(norma_aplicada)
        mensaje += mensaje_io
        mensaje += mensaje_ic
        mensaje += "Pisos: {} (Hab: {} + Serv: 1) | Entrepiso: {:.2f}m\n".format(pisos_totales, pisos_habitables, altura_entrepiso)
        mensaje += "Altura Permitida: {:.1f}m\n".format(altura_permitida)
        mensaje += "IO: {:.2f} (Max {}) | IC Real: {:.2f} (Max {})".format(ocupacion_real, io_maximo, ic_real, ic_maximo)
        print(mensaje)
    except Exception as e:
        mensaje = "Error: " + str(e)

# Salidas:
# a -> envelope_curve
# b -> altura_permitida
# c -> ocupacion_real
# d -> ic_real
# e -> mensaje
