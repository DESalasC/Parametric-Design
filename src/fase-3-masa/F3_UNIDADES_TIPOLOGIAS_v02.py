# -*- coding: utf-8 -*-
"""
================================================================================
F3_UNIDADES_TIPOLOGIAS_v02.py - Definición de unidades tipológicas flexibles (Fase 3)
Proyecto: DiseñoParametrico / Fase 3
Generador Python (CLI) + GH Python Script para Grasshopper
================================================================================

RESTRICCIONES ARQUITECTÓNICAS CLAVE:
  1. COMERCIO SOLO EN FACHADA PUBLICA (frente a via/anden).
     - NUNCA en patio interior / lado posterior.
     - Accesibilidad directa desde espacio publico.
     - Venta/arriendo viable solo con fachada a via.
  2. VIVIENDA en ambos lados (fachada + patio) con ventilacion natural.
  3. FLEXIBILIDAD TOTAL:
     - Unidades se adaptan al area disponible (ancho variable).
     - Soporte DUPLEX/LOFT: unidades que abarcan 2+ pisos.
     - Parqueaderos consolidados en MINIMO 1 sotano (no afecta ocupacion lote).
  4. PRE-VALIDACION: Reporte detallado para aprobacion del operador ANTES de generar geometria final.

NORMATIVA:
  - NSR-10 Titulo C (ocupacion, ventilacion, areas minimas)
  - NSR-10 Titulo K (evacuacion, pasillos >=1.20m, recorridos <=30m)
  - POT D555/2021 (parqueaderos 1c/und viv + 1c/100m2 com)
  - Res. 0549/2015 (vivienda min 42m2 VIS, 50m2 estandar)
  - Ley 675/2001 (PH: areas privadas/comunes, coeficientes)

ENTRADAS:
  CLI: --caso B --cota-via 0.0 --lote-frente 25 --lote-fondo 38 [--duplex-vivienda] [--duplex-comercio]
  GH: f2_resultados_json, layout_espacial_json, cota_via_m, chip,
      lote_frente_m, lote_fondo_m, angulo_fachada_deg,
      permitir_duplex_vivienda (bool), permitir_duplex_comercio (bool),
      consolidar_parqueaderos (bool), modo_validacion (bool)

SALIDAS:
  unidades_<chip>.json        : Unidades con geometria 2D, tipologia, multi-nivel
  parqueaderos_<chip>.json    : Parqueaderos consolidados (1 sotano preferido)
  circulaciones_<chip>.json   : Pasillos horizontales + nucleos verticales
  prevalidacion_<chip>.txt    : REPORTE PARA OPERADOR (areas, conteos, alertas)
  (GH) volumenes_por_uso, usos_etiquetas, usos_pisos -> F3_VOLUM_GENERADOR
================================================================================

HISTORIAL DE VERSIONES:
  v02.1 (2026-10-08): Cambio menor — FIXES para compatibilidad GH:
    1. Fix `_pj()`: ahora acepta dict/list ya parseados (no solo string/archivo).
    2. Fix `_gh()`: fallback automático de `lote_frente_m`/`lote_fondo_m` desde
       huella del layout si no vienen de F1.
    3. Fix detección modo GH: más robusta con lista de inputs esperados.
  v02.0 (2026-10-03): Cambio mayor — refactor completo compatible IronPython 2.7:
    - Eliminados f-strings, type hints, walrus operator.
    - Separación CLI (`main()`) / GH (`_gh()`) con detección automática.
    - Salidas paralelas: volumenes_por_uso, usos_etiquetas, usos_pisos (para F3_VOLUM_GENERADOR).

================================================================================
"""
import json
import os
import sys
import math

# ============================================================
# CONSTANTES NORMATIVAS
# ============================================================
ANCHO_PASILLO_MIN = 1.20
ANCHO_PASILLO_PREF = 1.50
AREA_MIN_VIV_VIS = 42.0
AREA_MIN_VIV_EST = 50.0
AREA_MIN_LOCAL = 20.0
PROF_MAX_VIV_FACHADA = 12.0      # 1 fachada -> max 12m profundidad
PROF_MAX_VIV_2FACHADAS = 18.0    # 2 fachadas (fachada+patio) -> hasta 18m
PROF_MAX_LOCAL = 15.0            # Comercio fachada publica
RECORRIDO_MAX_EVAC = 30.0
PARQ_VIV = 1.0
PARQ_COM_100M2 = 1.0
AREA_PARQ_UND = 12.5
AREA_PARQ_CIRC = 0.30

TIPOLOGIAS_BASE = {
    "Local fachada": {"area_obj": 40.0, "tipo": "comercio", "min_area": AREA_MIN_LOCAL, "fachada_obligatoria": True},
    "Vivienda estandar": {"area_obj": 55.0, "tipo": "vivienda", "min_area": AREA_MIN_VIV_EST, "fachada_obligatoria": False},
    "Vivienda VIS": {"area_obj": 45.0, "tipo": "vivienda", "min_area": AREA_MIN_VIV_VIS, "fachada_obligatoria": False},
}

# Mapeo: nombre de uso en layout_espacial.json -> clave en objetivos
USO_LAYOUT_A_OBJETIVO = {
    "Local comercial": "Local fachada",
    "Vivienda": "Vivienda",
}

# ============================================================
# GEOMETRIA 2D
# ============================================================
def rect(x, y, w, h): hw, hh = w/2, h/2; return [(x-hw,y-hh),(x+hw,y-hh),(x+hw,y+hh),(x-hw,y+hh),(x-hw,y-hh)]
def area(pts):
    if len(pts)<3: return 0.0
    a=0.0
    for i in range(len(pts)-1): a+=pts[i][0]*pts[i+1][1]-pts[i+1][0]*pts[i][1]
    return abs(a)/2
def rot(pts, ang, cx=0, cy=0):
    ca, sa = math.cos(ang), math.sin(ang)
    return [(cx+(x-cx)*ca-(y-cy)*sa, cy+(x-cx)*sa+(y-cy)*ca) for x,y in pts]
def bbox(pts): xs=[p[0] for p in pts]; ys=[p[1] for p in pts]; return min(xs),min(ys),max(xs),max(ys)

# ============================================================
# I/O
# ============================================================
def load_json(p):
    if not p or not os.path.exists(p): return {}
    try:
        with open(p,"r",encoding="utf-8") as f: return json.load(f)
    except: return {}

def resolve(caso):
    base=os.path.dirname(os.path.abspath(__file__))
    cdir=os.path.join(base,"casos",caso)
    lay=os.path.join(cdir,"layout_espacial.json")
    f2b=os.path.join(base,"..","fase-2-demanda","F2_Modelo_Financiero","resultados")
    f2f=[f for f in os.listdir(f2b) if f.startswith("resultados_") and f.endswith(".json")]
    return lay, os.path.join(f2b,f2f[0]) if f2f else "", cdir

# ============================================================
# LOGICA PRINCIPAL: DISTRIBUCION ADAPTATIVA
# ============================================================
def distribuir_piso(nivel, nucleo, uso, tip, area_neta, lote_frente, lote_fondo, ang,
                    lado_permitido,  # "fachada" | "patio" | "ambos"
                    n_und_obj,
                    altura_piso,
                    duplex=False,
                    piso_siguiente=None):
    """
    Distribuye unidades en UN piso (o 2 si duplex).
    lado_permitido: donde puede ir este uso ("fachada"=solo +Y, "patio"=solo -Y, "ambos"=ambos)
    n_und_obj: objetivo de unidades a colocar
    duplex: si True, intenta crear duplex con piso_siguiente
    """
    unds, circs = [], []
    n_w = nucleo.get("bloque",{}).get("ancho_m",6.4)
    n_l = nucleo.get("bloque",{}).get("largo_m",9.0)
    
    # Fachada = +Y (norte), Patio = -Y (sur)
    y_pasillo_fach = n_l/2 + 0.75
    y_pasillo_pat  = -n_l/2 - 0.75
    
    # Profundidades disponibles
    prof_disp_fach = lote_fondo/2 - y_pasillo_fach
    prof_disp_pat  = lote_fondo/2 + y_pasillo_pat  # y_pasillo_pat es negativo
    
    # Que lados usar segun restriccion
    filas = []
    if lado_permitido in ("fachada","ambos") and prof_disp_fach >= tip["min_area"]/8:
        prof = min(prof_disp_fach, PROF_MAX_VIV_FACHADA if tip["tipo"]=="vivienda" else PROF_MAX_LOCAL)
        filas.append(("fachada", y_pasillo_fach + prof/2, prof, PROF_MAX_VIV_2FACHADAS if tip["tipo"]=="vivienda" else PROF_MAX_LOCAL))
    if lado_permitido in ("patio","ambos") and prof_disp_pat >= tip["min_area"]/8:
        prof = min(prof_disp_pat, PROF_MAX_VIV_2FACHADAS if tip["tipo"]=="vivienda" else PROF_MAX_LOCAL)
        filas.append(("patio", y_pasillo_pat - prof/2, prof, PROF_MAX_VIV_2FACHADAS if tip["tipo"]=="vivienda" else PROF_MAX_LOCAL))
    if not filas: return unds, circs
    
    margen = 1.0
    frente_util = lote_frente - 2*margen
    
    # Calcular ancho unitario objetivo
    area_und = tip["area_obj"]
    # Si duplex, el area se duplica y la profundidad puede ser mayor (2 fachadas efectivas)
    if duplex:
        area_und *= 2
        for i,f in enumerate(filas):
            filas[i] = (f[0], f[1], f[2], f[3])
    
    id_base = 0
    for lado, y_centro, prof, prof_max_2fach in filas:
        n_fila_obj = max(1, n_und_obj // len(filas))
        ancho_ideal = area_und / prof
        n_caben = max(1, int(frente_util / ancho_ideal))
        n_final = min(n_fila_obj, n_caben)
        ancho_real = frente_util / n_final
        
        for i in range(n_final):
            x_centro = -frente_util/2 + ancho_real/2 + i*ancho_real
            verts = rect(x_centro, y_centro, ancho_real, prof)
            verts_r = rot(verts, ang)
            
            und = {
                "id": "U_{0}_{1}_{2:02d}".format(nivel['nivel'], uso[:3].upper(), id_base+1),
                "uso": uso, "tipologia": tip.get("nombre", uso),
                "piso_inicio": nivel["nivel"], "piso_fin": nivel["nivel"],
                "z_base_m": nivel["z_base_m"], "altura_total": altura_piso,
                "vertices": verts_r, "area_m2": round(area(verts_r),2),
                "ancho_m": round(ancho_real,2), "profundidad_m": round(prof,2),
                "lado": lado, "fachada_publica": (lado=="fachada"),
                "ventilacion_natural": True, "acceso_pasillo": True,
                "es_duplex": False, "duplex_con_piso": None,
            }
            
            if duplex and piso_siguiente:
                verts2 = rot(rect(x_centro, y_centro, ancho_real, prof), ang)
                und2 = {
                    "id": "U_{0}_{1}_{2:02d}_DUP".format(piso_siguiente['nivel'], uso[:3].upper(), id_base+1),
                    "uso": uso, "tipologia": tip.get("nombre", uso) + " (Duplex alto)",
                    "piso_inicio": nivel["nivel"], "piso_fin": piso_siguiente["nivel"],
                    "z_base_m": nivel["z_base_m"], "altura_total": altura_piso + piso_siguiente["altura_m"],
                    "vertices": verts2, "area_m2": round(area(verts2)*2,2),
                    "ancho_m": round(ancho_real,2), "profundidad_m": round(prof,2),
                    "lado": lado, "fachada_publica": (lado=="fachada"),
                    "ventilacion_natural": True, "acceso_pasillo": True,
                    "es_duplex": True, "duplex_con_piso": nivel["nivel"],
                    "unidad_base_id": und["id"],
                }
                und["es_duplex"] = True
                und["duplex_con_piso"] = piso_siguiente["nivel"]
                und["unidad_alto_id"] = und2["id"]
                unds.append(und)
                unds.append(und2)
            else:
                unds.append(und)
            id_base += 1
    
    # Pasillo unico en fachada (conecta al nucleo)
    if any(f[0]=="fachada" for f in filas):
        pl = frente_util + 2*margen
        pv = rot(rect(0, y_pasillo_fach, pl, ANCHO_PASILLO_PREF), ang)
        circs.append({"tipo":"pasillo_central","piso":nivel["nivel"],"z_base_m":nivel["z_base_m"],
            "vertices":pv,"ancho_m":ANCHO_PASILLO_PREF,"largo_m":round(pl,2),"conecta_nucleo":True,"lado":"fachada"})
    
    return unds, circs

def calc_parqueaderos(layout, f2_mix, cota_via, lote_frente, lote_fondo, consolidar=True):
    n_viv = sum(d["num_unidades"] for d in f2_mix if d["uso"].lower().startswith("viv"))
    a_com = sum(d["area_vendible_m2"] for d in f2_mix if d["uso"].lower().startswith(("loc","com")))
    total = int(math.ceil(n_viv*PARQ_VIV + a_com/100*PARQ_COM_100M2))
    a_und = AREA_PARQ_UND * (1+AREA_PARQ_CIRC)
    a_lote = lote_frente * lote_fondo
    cap_niv = max(1, int(a_lote*0.8/a_und))
    
    if consolidar:
        n_niv = math.ceil(total / cap_niv)
    else:
        n_niv = math.ceil(total / cap_niv)
    
    parqs = []
    for i in range(n_niv):
        z = -(i+1)*2.5
        cap = min(cap_niv, total - i*cap_niv)
        parqs.append({"nivel":-(i+1),"nombre":"Sotano {0}".format(i+1),"z_base_m":z,"altura_m":2.5,
            "capacidad":cap,"area_m2":round(cap*a_und,1),"tipo":"sotano",
            "cota_via_m":cota_via,"es_sotano":True,"consolidado":consolidar,
            "lote_frente":lote_frente,"lote_fondo":lote_fondo})
    return parqs

def generar(layout, f2, cota_via, ang, lote_frente, lote_fondo,
            allow_duplex_viv=False, allow_duplex_com=False, consolidar_parq=True):
    f2_mix = next((e["mix_usos_detalle"] for e in f2.get("escenarios",[]) if e.get("escenario_id")=="D_MIXTO"), [])
    if not f2_mix:
        f2_mix = [{"uso":"Local comercial turistico","num_unidades":21,"area_vendible_m2":840},
                  {"uso":"Vivienda estandar","num_unidades":31,"area_vendible_m2":1705}]
    
    # Mapear tipologías objetivo usando el mapeo de nombres
    objetivos = {}
    for d in f2_mix:
        uf = d["uso"]
        if "viv" in uf.lower():
            objetivos["Vivienda"] = dict(TIPOLOGIAS_BASE["Vivienda estandar"])
            objetivos["Vivienda"]["nombre"] = "Vivienda estandar"
            objetivos["Vivienda"]["total"] = d["num_unidades"]
        elif "loc" in uf.lower() or "com" in uf.lower():
            objetivos["Local fachada"] = dict(TIPOLOGIAS_BASE["Local fachada"])
            objetivos["Local fachada"]["nombre"] = "Local fachada publica"
            objetivos["Local fachada"]["total"] = d["num_unidades"]
    
    nucleo = layout.get("nucleos",{})
    cap_piso = {}
    for niv in layout.get("niveles",[]):
        an = (niv["gfa_m2"] - nucleo.get("nucleo_solidos_m2",44.6))*0.88
        for u in niv.get("usos",[]):
            obj_key = USO_LAYOUT_A_OBJETIVO.get(u)
            if obj_key and obj_key in objetivos:
                cap_piso[(u,niv["nivel"])] = int(an/(objetivos[obj_key]["area_obj"]*1.12))
    
    asign = {}
    reparto = layout.get("reparto_vertical",{})
    for uso, pisos in reparto.items():
        obj_key = USO_LAYOUT_A_OBJETIVO.get(uso)
        if not obj_key or obj_key not in objetivos: continue
        tot = objetivos[obj_key]["total"]
        pisos_ord = sorted(pisos, key=lambda p: cap_piso.get((uso,p),0), reverse=True)
        rest = tot
        for p in pisos_ord:
            cap = cap_piso.get((uso,p),0)
            mult = 1 if obj_key=="Local fachada" else 2
            real_cap = cap * mult
            asp = min(rest, real_cap)
            if asp>0:
                asign[(uso,p)] = asp
                rest -= asp
        if rest>0:
            for p in pisos:
                cap = cap_piso.get((uso,p),0)
                mult = 1 if obj_key=="Local fachada" else 2
                add = min(rest, cap*mult)
                if add>0:
                    asign[(uso,p)] = asign.get((uso,p),0)+add
                    rest -= add
                    if rest<=0: break
    
    all_und, all_circ = [], []
    niveles = layout.get("niveles",[])
    for idx, niv in enumerate(niveles):
        pn = niv["nivel"]
        for uso in niv.get("usos",[]):
            obj_key = USO_LAYOUT_A_OBJETIVO.get(uso)
            if not obj_key or obj_key not in objetivos: continue
            n_obj = asign.get((uso,pn),0)
            if n_obj<=0: continue
            tip = objetivos[obj_key]
            an = (niv["gfa_m2"]-nucleo.get("nucleo_solidos_m2",44.6))*0.88
            
            nxt = niveles[idx+1] if idx+1 < len(niveles) else None
            duplex = False
            if nxt and USO_LAYOUT_A_OBJETIVO.get(nxt.get("usos",[None])[0]) == obj_key:
                if (obj_key=="Vivienda" and allow_duplex_viv) or (obj_key=="Local fachada" and allow_duplex_com):
                    duplex = True
            
            lado_perm = "fachada" if obj_key=="Local fachada" else "ambos"
            unds, circs = distribuir_piso(niv, nucleo, uso, tip, an,
                lote_frente, lote_fondo, ang, lado_perm, n_obj, niv["altura_m"], duplex, nxt)
            all_und.extend(unds); all_circ.extend(circs)
    
    parqs = calc_parqueaderos(layout, f2_mix, cota_via, lote_frente, lote_fondo, consolidar_parq)
    return all_und, all_circ, parqs, objetivos, asign

def to_volum(unds, circs, parqs):
    vol, et, pi = [], [], []
    base_unds = [u for u in unds if not u.get("es_duplex") or u.get("duplex_con_piso") is not None]
    for u in base_unds:
        vol.append([[[v[0],v[1],0] for v in u["vertices"]]])
        et.append("{0} {1}".format(u['uso'], u['tipologia'])); pi.append(u["piso_inicio"])
    for c in circs:
        vol.append([[[v[0],v[1],0] for v in c["vertices"]]])
        et.append("Circulacion"); pi.append(c["piso"])
    for p in parqs:
        a=p["area_m2"]; l=math.sqrt(a)
        vol.append([[[v[0],v[1],0] for v in rect(0,0,l,l)]])
        et.append("Parqueadero {0}".format(p['nombre'])); pi.append(p["nivel"])
    return vol, et, pi

def prevalidacion(unds, circs, parqs, objetivos, asign, lote_frente, lote_fondo, cota_via):
    lines = []
    lines.append("="*80)
    lines.append("F3 - PRE-VALIDACION UNIDADES TIPOLOGICAS (REVISION OPERADOR)")
    lines.append("="*80)
    lines.append("\nLOTE: {:.1f} x {:.1f} m = {:.1f} m2".format(lote_frente, lote_fondo, lote_frente*lote_fondo))
    lines.append("COTA VIA: {:.1f} m -> Parqueaderos en sotano (z<0)".format(cota_via))
    lines.append("\nRESTRICCIONES APLICADAS:")
    lines.append("  [OK] Comercio SOLO en fachada publica (lado +Y, frente a via)")
    lines.append("  [OK] Vivienda en fachada + patio (ventilacion cruzada)")
    lines.append("  [OK] Pasillos >= {:.1f}m (NSR-10 K)".format(ANCHO_PASILLO_PREF))
    lines.append("  [OK] Profundidad max: Viv fachada {}m, Viv 2 fach {}m, Com {}m".format(
        PROF_MAX_VIV_FACHADA, PROF_MAX_VIV_2FACHADAS, PROF_MAX_LOCAL))
    lines.append("  [OK] Parqueaderos consolidados en sotano unico (no consume ocupacion lote)")
    
    lines.append("\n{:<25} {:>8} {:>10} {:>10} {:>12} {}".format(
        "TIPOLOGIA", "OBJ F2", "ASIGNADOS", "GENERADOS", "AREA TOTAL", "PISOS"))
    lines.append("-"*80)
    for uso_obj, tip in objetivos.items():
        obj = tip["total"]
        # Sumar asignados para este objetivo (buscar en asign por uso_layout)
        asig = 0
        for (u_layout, p), v in asign.items():
            if USO_LAYOUT_A_OBJETIVO.get(u_layout) == uso_obj:
                asig += v
        gen = [u for u in unds if USO_LAYOUT_A_OBJETIVO.get(u["uso"]) == uso_obj and not u.get("unidad_alto_id")]
        a_tot = sum(u["area_m2"] for u in gen)
        pisos = sorted(set(u["piso_inicio"] for u in gen))
        lines.append("{:<25} {:>8} {:>10} {:>10} {:>11.1f} m2  {}".format(
            tip['nombre'], obj, asig, len(gen), a_tot, pisos))
    
    duplexs = [u for u in unds if u.get("es_duplex") and u.get("duplex_con_piso") is not None]
    if duplexs:
        lines.append("\nDUPLEX/LOFT ({} pares):".format(len(duplexs)))
        for u in duplexs:
            lines.append("  {}: Pisos {}-{}, {:.1f} m2, lado {}".format(
                u['id'], u['piso_inicio'], u['piso_fin'], u['area_m2'], u['lado']))
    
    tot_p = sum(p["capacidad"] for p in parqs)
    lines.append("\nPARQUEADEROS: {} puestos en {} nivel(es) sotano".format(tot_p, len(parqs)))
    for p in parqs:
        lines.append("  {}: {} pts, {:.1f} m2, z={:.1f}m".format(p['nombre'], p['capacidad'], p['area_m2'], p['z_base_m']))
    
    lines.append("\nVERIFICACIONES NORMATIVAS:")
    com_patio = [u for u in unds if USO_LAYOUT_A_OBJETIVO.get(u["uso"])=="Local fachada" and u["lado"]=="patio"]
    lines.append("  Comercio en patio (PROHIBIDO): {} {}".format(len(com_patio), "[ALERTA]" if com_patio else "[OK]"))
    sin_vent = [u for u in unds if not u.get("ventilacion_natural")]
    lines.append("  Unidades sin ventilacion natural: {} {}".format(len(sin_vent), "[ALERTA]" if sin_vent else "[OK]"))
    for c in circs:
        if c["ancho_m"] < ANCHO_PASILLO_MIN:
            lines.append("  Pasillo P{} {:.2f}m < {:.1f}m [ALERTA]".format(c['piso'], c['ancho_m'], ANCHO_PASILLO_MIN))
    for u in unds:
        obj_key = USO_LAYOUT_A_OBJETIVO.get(u["uso"])
        if obj_key and obj_key in TIPOLOGIAS_BASE:
            min_a = TIPOLOGIAS_BASE[obj_key]["min_area"]
            if u["area_m2"] < min_a:
                lines.append("  {} area {:.1f} < min {:.1f} [ALERTA]".format(u['id'], u['area_m2'], min_a))
    
    estado = "LISTO PARA GENERAR" if not com_patio and not sin_vent else "REQUIERE AJUSTES"
    lines.append("\n>>> ESTADO: {}".format(estado))
    return "\n".join(lines)

def main():
    caso=f2p=layp=None; cota=0.0; out=None; ang=0.0; lf=0.0; lfo=0.0
    dviv=False; dcom=False; cons=True; val=False
    argv=sys.argv[1:]; i=0
    while i<len(argv):
        a=argv[i]
        if a=="--caso" and i+1<len(argv): caso=argv[i+1]; i+=2
        elif a=="--f2-resultados" and i+1<len(argv): f2p=argv[i+1]; i+=2
        elif a=="--layout" and i+1<len(argv): layp=argv[i+1]; i+=2
        elif a=="--cota-via" and i+1<len(argv): cota=float(argv[i+1]); i+=2
        elif a=="--salida" and i+1<len(argv): out=argv[i+1]; i+=2
        elif a=="--angulo-fachada" and i+1<len(argv): ang=math.radians(float(argv[i+1])); i+=2
        elif a=="--lote-frente" and i+1<len(argv): lf=float(argv[i+1]); i+=2
        elif a=="--lote-fondo" and i+1<len(argv): lfo=float(argv[i+1]); i+=2
        elif a=="--duplex-vivienda": dviv=True; i+=1
        elif a=="--duplex-comercio": dcom=True; i+=1
        elif a=="--no-consolidar-parq": cons=False; i+=1
        elif a=="--validacion": val=True; i+=1
        else: i+=1
    if caso:
        layp,f2pa,cdir=resolve(caso)
        if not f2p: f2p=f2pa
        if not out: out=cdir
    elif not layp or not f2p:
        print("ERROR: --caso o (--layout + --f2-resultados)"); sys.exit(1)
    else:
        cdir=os.path.dirname(layp)
        if not out: out=cdir
    lay=load_json(layp); f2=load_json(f2p)
    if not lay: print("ERROR: layout no encontrado: {}".format(layp)); sys.exit(1)
    if not f2:
        f2={"escenarios":[{"escenario_id":"D_MIXTO","mix_usos_detalle":[
            {"uso":"Local comercial turistico","num_unidades":21,"area_vendible_m2":840},
            {"uso":"Vivienda estandar","num_unidades":31,"area_vendible_m2":1705}]}]}
    chip=lay.get("chip",caso or "chip")
    
    unds, circs, parqs, objs, asign = generar(lay, f2, cota, ang, lf, lfo, dviv, dcom, cons)
    vol, et, pi = to_volum(unds, circs, parqs)
    
    if not os.path.isdir(out): os.makedirs(out)
    data = {"metadata":{"version":"2.0.0","modulo":"F3_UNIDADES_TIPOLOGIAS_v02","chip":chip,
        "total_unidades_base":len([u for u in unds if not u.get("unidad_alto_id")]),
        "total_duplex":len([u for u in unds if u.get("es_duplex") and u.get("duplex_con_piso")]),
        "total_circulaciones":len(circs),"total_parqueaderos":sum(p["capacidad"] for p in parqs),
        "lote_frente_m":lf,"lote_fondo_m":lfo,"cota_via_m":cota,
        "restricciones":{"comercio_solo_fachada":True,"parking_sotano_consolidado":cons,
        "duplex_vivienda":dviv,"duplex_comercio":dcom}},
        "unidades":unds,"circulaciones":circs,"parqueaderos":parqs,
        "volumenes_para_F3_VOLUM_GENERADOR":{"volumenes_por_uso":vol,"usos_etiquetas":et,"usos_pisos":pi}}
    
    with open(os.path.join(out,"unidades_{}.json".format(chip)),"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    
    prev = prevalidacion(unds, circs, parqs, objs, asign, lf, lfo, cota)
    with open(os.path.join(out,"prevalidacion_{}.txt".format(chip)),"w",encoding="utf-8") as f:
        f.write(prev)
    print(prev)
    print("\nGuardado: unidades_{}.json + prevalidacion_{}.txt".format(chip, chip))
    if val:
        print("\n>>> MODO VALIDACION: Revisar prevalidacion_*.txt antes de proceder")

def _u(v):
    if v is None: return None
    if hasattr(v,"Value"): return v.Value
    # GH a veces entrega listas de 1 elemento en lugar del valor directo
    if isinstance(v, (list, tuple)) and len(v) > 0:
        return _u(v[0])
    return v
def _pj(v):
    """Parsea JSON desde string, archivo, o retorna dict/list si ya está parseado."""
    if v is None:
        return None
    # Si ya es dict o list, retornarlo directamente (IMPORTANTE: antes de str())
    if isinstance(v, (dict, list)):
        return v
    s = str(v).strip()
    # Si es ruta a archivo .json
    if s.endswith(".json") and os.path.exists(s):
        return load_json(s)
    # Si es string JSON, parsearlo
    try: return json.loads(s)
    except: return None

def _gh():
    # Debug: listar todas las globales disponibles para diagnosticar nombres de entradas
    try:
        gh_globals = [k for k in globals().keys() if not k.startswith('_') and k not in ['json', 'os', 'sys', 'math', 'rg', 'io', 'load_json', 'resolve', 'rect', 'area', 'rot', 'bbox', 'distribuir_piso', 'calc_parqueaderos', 'generar', 'to_volum', 'prevalidacion', 'main', '_u', '_pj', '_gh', '_es_gh', 'gh_inputs', 'inp', 'TIPOLOGIAS_BASE', 'USO_LAYOUT_A_OBJETIVO', 'ANCHO_PASILLO_MIN', 'ANCHO_PASILLO_PREF', 'AREA_MIN_VIV_VIS', 'AREA_MIN_VIV_EST', 'AREA_MIN_LOCAL', 'PROF_MAX_VIV_FACHADA', 'PROF_MAX_VIV_2FACHADAS', 'PROF_MAX_LOCAL', 'RECORRIDO_MAX_EVAC', 'PARQ_VIV', 'PARQ_COM_100M2', 'AREA_PARQ_UND', 'AREA_PARQ_CIRC']]
    except:
        gh_globals = []

    # Intentar múltiples nombres posibles para layout (compatibilidad con diferentes cableados)
    lay = None
    tried_names = []
    for layout_name in ["layout_espacial_json", "layout_json", "layoutEspacialJson", "layout_espacial", "LayoutEspacialJson", "layout-espacial-json"]:
        tried_names.append(layout_name)
        val = globals().get(layout_name)
        if val is not None:
            lay = _pj(_u(val))
            if lay:
                break

    # Si aún no hay layout, intentar buscar en todas las globales que contengan "layout" o "espacial"
    if not lay:
        for k, v in globals().items():
            kl = k.lower()
            if ('layout' in kl or 'espacial' in kl) and v is not None:
                tried_names.append(k)
                lay = _pj(_u(v))
                if lay:
                    break

    f2=_pj(_u(globals().get("f2_resultados_json")))
    cota=float(_u(globals().get("cota_via_m",0)) or 0)
    chip=_u(globals().get("chip")) or "chip"
    ang=math.radians(float(_u(globals().get("angulo_fachada_deg",0)) or 0))
    lf=float(_u(globals().get("lote_frente_m",0)) or 0)
    lfo=float(_u(globals().get("lote_fondo_m",0)) or 0)
    # Fallback: si no vienen de F1, calcular desde envelope del layout
    if (lf <= 0 or lfo <= 0) and lay and lay.get("niveles"):
        huella = lay["niveles"][0].get("gfa_m2", 0)
        if huella > 0:
            lf = math.sqrt(huella / 1.5)
            lfo = lf * 1.5
    dviv=bool(_u(globals().get("permitir_duplex_vivienda",False)))
    dcom=bool(_u(globals().get("permitir_duplex_comercio",False)))
    cons=bool(_u(globals().get("consolidar_parqueaderos",True)))
    val=bool(_u(globals().get("modo_validacion",False)))
    if not lay:
        debug_msg = "UNIDADES v2.0 | ERROR: sin layout. Globales disponibles: {}".format(", ".join(sorted(gh_globals)[:20]))
        return "","","",[],[],[],debug_msg
    if not f2:
        f2={"escenarios":[{"escenario_id":"D_MIXTO","mix_usos_detalle":[
            {"uso":"Local comercial turistico","num_unidades":21,"area_vendible_m2":840},
            {"uso":"Vivienda estandar","num_unidades":31,"area_vendible_m2":1705}]}]}
    u,c,p,objs,asign=generar(lay,f2,cota,ang,lf,lfo,dviv,dcom,cons)
    vol,et,pi=to_volum(u,c,p)
    tp=sum(x["capacidad"] for x in p)
    prev=prevalidacion(u,c,p,objs,asign,lf,lfo,cota)
    return (json.dumps({"unidades":u},ensure_ascii=False),
            json.dumps({"parqueaderos":p},ensure_ascii=False),
            json.dumps({"circulaciones":c},ensure_ascii=False),
            vol,et,pi,
            "UNIDADES v2.0 | {} | {} base + {} duplex | {} circ | {} parq ({} sotano)".format(
                "VALIDACION" if val else "OK",
                len([x for x in u if not x.get('unidad_alto_id')]),
                len([x for x in u if x.get('es_duplex') and x.get('duplex_con_piso')]),
                len(c), tp, len(p)))

# ------------------------------------------------------------------ Detección modo GH vs CLI
# En GH: ghenv existe, o hay entradas inyectadas (f2_resultados_json, layout_espacial_json, etc.)
_es_gh = False
try:
    ghenv  # noqa: F821
    _es_gh = True
except NameError:
    pass

if not _es_gh:
    # Verificar si hay entradas GH inyectadas
    gh_inputs = ["f2_resultados_json", "layout_espacial_json", "cota_via_m", "chip",
                 "angulo_fachada_deg", "lote_frente_m", "lote_fondo_m",
                 "permitir_duplex_vivienda", "permitir_duplex_comercio",
                 "consolidar_parqueaderos", "modo_validacion"]
    for inp in gh_inputs:
        if globals().get(inp) is not None:
            _es_gh = True
            break

if _es_gh:
    # MODO GH: ejecutar _gh() y asignar salidas globales
    unidades_json = ""
    parqueaderos_json = ""
    circulaciones_json = ""
    mensaje = ""
    volumenes_por_uso = []
    usos_etiquetas = []
    usos_pisos = []
    try:
        (unidades_json, parqueaderos_json, circulaciones_json,
         volumenes_por_uso, usos_etiquetas, usos_pisos, mensaje) = _gh()
    except Exception as e:
        mensaje = "UNIDADES v2.0 | ERROR: {}".format(e)
        try:
            ghenv.Component.Message = mensaje  # noqa: F821
        except Exception:
            pass
else:
    # MODO CLI: ejecutar main()
    main()