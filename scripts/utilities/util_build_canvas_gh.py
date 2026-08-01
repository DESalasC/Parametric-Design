#!/usr/bin/env python3
"""
build_canvas_gh.py - Ejecutar DENTRO de Grasshopper Python Editor
Rhino → Tools → PythonScript → RunScript → Seleccionar este archivo

Crea canvas nativo completo con:
- GRUPO 0: TAPIR INPUT (ArchiCAD → GH)
- GRUPO 1: CONFIGURAR_LADOS_POT
- GRUPO 2: CONTEXTO_POT
- GRUPO 3: VOLUMEN_v02 + DISEÑO_INTERIOR_v01 + LADYBUG_v01 + WALLACEI + AC NATIVE

NOTA: Los 5 componentes Python Script requieren pegar el código manualmente
desde los archivos .py en 3-Proceso/GH_Scripts/
"""

import Grasshopper as gh
import Grasshopper.Kernel as ghk
import Grasshopper.Kernel.Data as ghkd
import Rhino.Geometry as rg
import System
import System.Drawing

# ============================================================
# HELPERS
# ============================================================

def find_component_type(name, category=None, subcategory=None):
    """Buscar tipo de componente por nombre usando GH_API correcta"""
    server = gh.Instances.ComponentServer

    # Intentar con categoría/subcategoría
    if category and subcategory:
        # En IronPython, usar FindAssemblyByName o iterar librerías
        try:
            comp_type = server.FindComponentByName(name, category, subcategory)
            if comp_type:
                return comp_type
        except:
            pass

    # Búsqueda global en todas las librerías
    for lib in server.Libraries:
        for item in lib.Items:
            if item.Name == name:
                return item
    return None

def get_server():
    """Obtener server de componentes (compatible IronPython)"""
    return gh.Instances.ComponentServer

def create_comp(doc, name, nickname, location, category=None, subcategory=None):
    """Crear componente genérico"""
    comp_type = find_component_type(name, category, subcategory)
    if comp_type is None:
        print(f"  [MISSING] {name} ({category}/{subcategory})")
        return None
    try:
        comp = comp_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        return comp
    except Exception as e:
        print(f"  [ERROR creating {name}]: {e}")
        return None

def create_py_component(doc, nickname, code_path, location):
    """Crear Python Script component vacío (pegar código después)"""
    # Python Script está en "Maths" > "Scripts"
    py_type = find_component_type("Python Script", "Maths", "Scripts")
    if py_type is None:
        print("  [MISSING] Python Script")
        return None
    try:
        comp = py_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        print(f"  [PY] {nickname} → pegar código desde: {code_path}")
        return comp
    except Exception as e:
        print(f"  [ERROR creating Python Script]: {e}")
        return None

def create_panel(doc, nickname, value, location):
    panel_type = find_component_type("Panel", "Params", "Input")
    if panel_type:
        comp = panel_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        comp.PersistentData.Clear()
        comp.PersistentData.Append(str(value))
        return comp
    return None

def create_slider(doc, nickname, min_val, max_val, value, location):
    slider_type = find_component_type("Number Slider", "Params", "Input")
    if slider_type:
        comp = slider_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        # Configurar valores
        comp.SetSliderValue(min_val, max_val, value)
        return comp
    return None

def create_gene_pool(doc, nickname, min_val, max_val, decimals, values, location):
    gp_type = find_component_type("Gene Pool", "Params", "Input")
    if gp_type:
        comp = gp_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        comp.Min = float(min_val)
        comp.Max = float(max_val)
        comp.Decimals = decimals
        comp.ValueList = [float(v) for v in values]
        return comp
    return None

def create_boolean_toggle(doc, nickname, value, location):
    bt_type = find_component_type("Boolean Toggle", "Params", "Input")
    if bt_type:
        comp = bt_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        comp.Value = value
        return comp
    return None

def create_file_path(doc, nickname, value, location):
    fp_type = find_component_type("File Path", "Params", "Input")
    if fp_type:
        comp = fp_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        comp.PersistentData.Clear()
        comp.PersistentData.Append(str(value))
        return comp
    return None

def create_vector_2pt(doc, nickname, location):
    vec_type = find_component_type("Vector 2Pt", "Vector", "Vector")
    if vec_type:
        comp = vec_type.CreateInstance()
        comp.NickName = nickname
        doc.AddObject(comp, False)
        comp.Attributes.Pivot = location
        # Los inputs A y B se configuran después o via Panels
        return comp
    return None

def create_panel_vector_a_b(doc, nickname, a_pt, b_pt, location):
    """Panel que se conecta a Vector 2Pt inputs A y B"""
    # Crear 2 Panels para A y B
    panel_a = create_panel(doc, f"{nickname}_A", f"{a_pt.X},{a_pt.Y},{a_pt.Z}", location)
    panel_b = create_panel(doc, f"{nickname}_B", f"{b_pt.X},{b_pt.Y},{b_pt.Z}",
                           System.Drawing.Point(location.X + 80, location.Y))
    return panel_a, panel_b

def connect(doc, from_comp, from_idx, to_comp, to_idx):
    """Conectar dos componentes"""
    if from_comp is None or to_comp is None:
        return False
    try:
        # Verificar índices válidos
        if from_idx >= from_comp.Params.Output.Count:
            print(f"  [CONNECT ERR] {from_comp.NickName} output idx {from_idx} >= {from_comp.Params.Output.Count}")
            return False
        if to_idx >= to_comp.Params.Input.Count:
            print(f"  [CONNECT ERR] {to_comp.NickName} input idx {to_idx} >= {to_comp.Params.Input.Count}")
            return False

        from_param = from_comp.Params.Output[from_idx]
        to_param = to_comp.Params.Input[to_idx]
        wire = ghk.GH_Wire(from_param, to_param)
        doc.Wires.Add(wire)
        return True
    except Exception as e:
        print(f"  [CONNECT ERR] {from_comp.NickName}[{from_idx}] -> {to_comp.NickName}[{to_idx}]: {e}")
        return False

def create_group(doc, name, nickname, color_hex, member_ids, location):
    try:
        group = ghk.GH_Group(doc)
        group.Name = name
        group.NickName = nickname
        group.Colour = System.Drawing.ColorTranslator.FromHtml(color_hex)
        for mid in member_ids:
            if mid:
                group.AddObject(mid)
        doc.Groups.Add(group)
        return group
    except Exception as e:
        print(f"  [GROUP ERR] {name}: {e}")
        return None

# ============================================================
# MAIN BUILD
# ============================================================

def build_canvas():
    # Obtener documento ACTIVO de Grasshopper
    doc = gh.Instances.ActiveCanvas.Document
    if doc is None:
        print("ERROR: No hay documento activo en Grasshopper")
        return

    print("=== BUILDING CANVAS: Diseño Paramétrico Rev05 ===")

    # Layout coordinates
    x0 = 100
    y0 = 100
    x_step = 280
    y_step = 100

    all_member_guids = []
    groups_data = []  # (name, nickname, color, guids, label_loc)

    # ============================================================
    # GRUPO 0: TAPIR INPUT
    # ============================================================
    g0 = []
    gy = y0

    tapir_recv = create_comp(doc, "Receive Geometry", "ArchiCAD to GH",
                              System.Drawing.Point(x0, gy), "Tapir", "Geometry")
    if tapir_recv: g0.append(tapir_recv)

    deconstruct_brep = create_comp(doc, "Deconstruct Brep", "Deconstruct Brep",
                                    System.Drawing.Point(x0 + x_step, gy))
    if deconstruct_brep: g0.append(deconstruct_brep)
    connect(doc, tapir_recv, 0, deconstruct_brep, 0)

    join_curves = create_comp(doc, "Join Curves", "Join Curves (Lote)",
                               System.Drawing.Point(x0 + 2*x_step, gy))
    if join_curves: g0.append(join_curves)
    connect(doc, deconstruct_brep, 1, join_curves, 0)  # Edges

    area_lot = create_comp(doc, "Area", "Area (Lote)",
                            System.Drawing.Point(x0 + 3*x_step, gy))
    if area_lot: g0.append(area_lot)
    connect(doc, join_curves, 0, area_lot, 0)

    # Explode para obtener segmentos del lote
    explode_lot = create_comp(doc, "Explode", "Explode Lote",
                               System.Drawing.Point(x0 + 2*x_step, gy + y_step))
    if explode_lot: g0.append(explode_lot)
    connect(doc, deconstruct_brep, 1, explode_lot, 0)  # Edges

    # Outputs Grupo 0 para Grupo 1:
    # - join_curves (curvas lote unidas)
    # - area_lot (área + centroide)
    # - explode_lot (segmentos para midpoints/tangents)

    groups_data.append(("GRUPO 0: TAPIR INPUT", "GRUPO 0: TAPIR INPUT", "#FF8C00",
                        [c.InstanceGuid for c in g0 if c],
                        System.Drawing.Point(x0 - 150, gy - 100)))
    all_member_guids.extend([c.InstanceGuid for c in g0 if c])

    # ============================================================
    # GRUPO 1: CONFIGURAR_LADOS_POT
    # ============================================================
    g1 = []
    gy1 = y0 + 350

    # Inputs desde Grupo 0
    deconstruct_2d = create_comp(doc, "Deconstruct 2D Polyline", "Deconstruct Lote 2D",
                                  System.Drawing.Point(x0, gy1))
    if deconstruct_2d: g1.append(deconstruct_2d)
    connect(doc, join_curves, 0, deconstruct_2d, 0)

    area_lot2 = create_comp(doc, "Area", "Area (Lote v2)",
                             System.Drawing.Point(x0, gy1 + y_step))
    if area_lot2: g1.append(area_lot2)
    connect(doc, join_curves, 0, area_lot2, 0)

    explode = create_comp(doc, "Explode", "Explode Lados",
                           System.Drawing.Point(x0 + x_step, gy1))
    if explode: g1.append(explode)
    connect(doc, deconstruct_2d, 1, explode, 0)  # Edges

    curve_middle = create_comp(doc, "Curve Middle", "Midpoints Lados",
                                System.Drawing.Point(x0 + 2*x_step, gy1))
    if curve_middle: g1.append(curve_middle)
    connect(doc, explode, 0, curve_middle, 0)

    curve_frame = create_comp(doc, "Curve Frame", "Frames Lados (Tangents)",
                               System.Drawing.Point(x0 + 2*x_step, gy1 + y_step))
    if curve_frame: g1.append(curve_frame)
    connect(doc, explode, 0, curve_frame, 0)
    connect(doc, curve_middle, 1, curve_frame, 1)  # Parameter

    angle = create_comp(doc, "Angle", "Ángulo vs Norte",
                         System.Drawing.Point(x0 + 3*x_step, gy1 + y_step))
    if angle: g1.append(angle)
    connect(doc, curve_frame, 1, angle, 0)  # Tangent vector

    # Vector Norte (0,1,0) - Panel conectado a Angle input B
    panel_north = create_panel(doc, "North_Vector", "0,1,0",
                                System.Drawing.Point(x0 + 3*x_step + 80, gy1 + y_step))
    if panel_north: g1.append(panel_north)
    connect(doc, panel_north, 0, angle, 1)

    # Python Script: CONFIGURAR_LADOS_v03
    py_lados = create_py_component(doc, "Python - CONFIGURAR_LADOS_POT",
                                    r"C:\Users\Dario Salas\proyectos\3-Proceso\GH_Scripts\CONFIGURAR_LADOS_v03.py",
                                    System.Drawing.Point(x0 + 4*x_step, gy1 + 30))
    if py_lados: g1.append(py_lados)
    # Entradas que espera el script:
    # 0: segments (curves from explode)
    # 1: distances (list of lengths)
    # 2: orientations (list of angles)
    connect(doc, explode, 0, py_lados, 0)

    # Length component para distances
    length = create_comp(doc, "Length", "Lengths Lados",
                          System.Drawing.Point(x0 + 4*x_step, gy1 - y_step))
    if length: g1.append(length)
    connect(doc, explode, 0, length, 0)
    connect(doc, length, 0, py_lados, 1)

    # Angles ya vienen de angle component
    connect(doc, angle, 0, py_lados, 2)

    # Inputs adicionales para Python script
    # street_curves (Panel File Path) - desde Grupo 2
    panel_street = create_panel(doc, "street_curves_file",
                                 r"C:\Users\Dario Salas\proyectos\2-Entradas\Datos_Sitio_GDB\geojson_layers\eje_vial.geojson",
                                 System.Drawing.Point(x0 + 3*x_step, gy1 + 2*y_step))
    if panel_street: g1.append(panel_street)
    # Se conectará más tarde

    # north_vector
    panel_north2 = create_panel(doc, "north_vector", "0,1,0",
                                 System.Drawing.Point(x0 + 3*x_step, gy1 + 3*y_step))
    if panel_north2: g1.append(panel_north2)
    connect(doc, panel_north2, 0, py_lados, 3)

    # building_floors (Slider/Gene Pool)
    gp_floors = create_gene_pool(doc, "building_floors (GP102)", 1, 15, 0, [5, 8, 10, 12],
                                  System.Drawing.Point(x0 + 5*x_step, gy1 + y_step))
    if gp_floors: g1.append(gp_floors)
    connect(doc, gp_floors, 0, py_lados, 4)

    # Gene Pools de optimización (outputs hacia VOLUMEN)
    gp_heights = create_gene_pool(doc, "genome_heights (GP103)", 2, 15, 0, [4, 6, 8, 10, 12],
                                   System.Drawing.Point(x0 + 6*x_step, gy1))
    if gp_heights: g1.append(gp_heights)

    gp_setbacks = create_gene_pool(doc, "genome_setbacks (GP104)", 0.5, 10, 1, [3.0, 2.5, 3.0, 2.5],
                                    System.Drawing.Point(x0 + 6*x_step, gy1 + y_step))
    if gp_setbacks: g1.append(gp_setbacks)

    gp_orientation = create_slider(doc, "genome_orientation (GP105)", 0, 360, 0,
                                    System.Drawing.Point(x0 + 6*x_step, gy1 + 2*y_step))
    if gp_orientation: g1.append(gp_orientation)

    groups_data.append(("GRUPO 1: CONFIGURAR_LADOS_POT", "GRUPO 1: CONFIGURAR_LADOS_POT", "#3881B8",
                        [c.InstanceGuid for c in g1 if c],
                        System.Drawing.Point(x0 - 150, gy1 - 100)))
    all_member_guids.extend([c.InstanceGuid for c in g1 if c])

    # ============================================================
    # GRUPO 2: CONTEXTO_POT
    # ============================================================
    g2 = []
    gy2 = gy1 + 400

    # Panel folder base
    panel_folder = create_panel(doc, "GDB_Folder",
                                 r"C:\Users\Dario Salas\proyectos\2-Entradas\Datos_Sitio_GDB\geojson_layers",
                                 System.Drawing.Point(x0, gy2))
    if panel_folder: g2.append(panel_folder)

    # Import GeoJSON components (usar custom component o File Input)
    # En GH estándar, se usa "Import" o se arrastran archivos
    # Aquí usamos Panels con paths y componentes "Import" si existen
    geojson_files = [
        ("eje_vial.geojson", "street_curves_import", "Calle/Vía"),
        ("clase_suelo_pot.geojson", "clase_suelo_import", "Clase Suelo"),
        ("tratamiento_urbanistico.geojson", "tratamiento_import", "Tratamiento"),
        ("sector_uso_residencial.geojson", "sector_residencial_import", "Sector Residencial"),
    ]

    imports = []
    for i, (fname, nick, label) in enumerate(geojson_files):
        # Panel con path
        panel_path = create_panel(doc, f"path_{nick}",
                                   r"C:\Users\Dario Salas\proyectos\2-Entradas\Datos_Sitio_GDB\geojson_layers" + "\\" + fname,
                                   System.Drawing.Point(x0, gy2 + i * 80))
        if panel_path: g2.append(panel_path)

        # Intentar componente File Import / Import
        imp = create_comp(doc, "Import", f"Import {label}",
                           System.Drawing.Point(x0 + x_step, gy2 + i * 80))
        if imp is None:
            # Fallback: Panel directo (el script Python lee el path)
            imp = create_panel(doc, f"data_{nick}", fname,
                               System.Drawing.Point(x0 + x_step, gy2 + i * 80))
        if imp: g2.append(imp)
        connect(doc, panel_path, 0, imp, 0)
        imports.append(imp)

    # north_vector
    panel_north3 = create_panel(doc, "north_vector_ctx", "0,1,0",
                                 System.Drawing.Point(x0 + 3*x_step, gy2))
    if panel_north3: g2.append(panel_north3)

    # elevation
    panel_elev = create_panel(doc, "elevation_nmm", "2600",
                               System.Drawing.Point(x0 + 3*x_step, gy2 + y_step))
    if panel_elev: g2.append(panel_elev)

    # lot_area y lot_centroid desde Grupo 0
    # area_lot outputs: A (Area), C (Centroid)
    # Se conectarán al Python script

    # Python Script: CONTEXTO_v04
    py_context = create_py_component(doc, "Python - CONTEXTO_POT_v04",
                                      r"C:\Users\Dario Salas\proyectos\3-Proceso\GH_Scripts\CONTEXTO_v04.py",
                                      System.Drawing.Point(x0 + 4*x_step, gy2 + 80))
    if py_context: g2.append(py_context)

    # Conexiones a CONTEXTO_v04:
    # 0: lot_area (number) - from area_lot.A
    # 1: lot_centroid (point) - from area_lot.C
    # 2: street_curves (curves) - from imports[0]
    # 3: clase_suelo (data) - from imports[1]
    # 4: tratamiento (data) - from imports[2]
    # 5: sector_residencial (data) - from imports[3]
    # 6: north_vector (vector) - from panel_north3
    # 7: elevation_nmm (number) - from panel_elev
    connect(doc, area_lot, 0, py_context, 0)      # Area
    connect(doc, area_lot, 1, py_context, 1)      # Centroid
    if len(imports) > 0:
        connect(doc, imports[0], 0, py_context, 2)  # street_curves
    if len(imports) > 1:
        connect(doc, imports[1], 0, py_context, 3)  # clase_suelo
    if len(imports) > 2:
        connect(doc, imports[2], 0, py_context, 4)  # tratamiento
    if len(imports) > 3:
        connect(doc, imports[3], 0, py_context, 5)  # sector
    connect(doc, panel_north3, 0, py_context, 6)
    connect(doc, panel_elev, 0, py_context, 7)

    groups_data.append(("GRUPO 2: CONTEXTO_POT", "GRUPO 2: CONTEXTO_POT", "#2E8B57",
                        [c.InstanceGuid for c in g2 if c],
                        System.Drawing.Point(x0 - 150, gy2 - 100)))
    all_member_guids.extend([c.InstanceGuid for c in g2 if c])

    # ============================================================
    # GRUPO 3: WALLACEI_FITNESS (VOLUMEN + DISEÑO + LADYBUG + WALLACEI + AC)
    # ============================================================
    g3 = []
    gy3 = gy2 + 550

    # --- GENE POOLS (desde CONFIGURAR_LADOS y propios) ---
    gp_h = create_gene_pool(doc, "genome_heights (GP103)", 2, 15, 0, [4, 6, 8, 10, 12],
                             System.Drawing.Point(x0, gy3))
    if gp_h: g3.append(gp_h)

    gp_s = create_gene_pool(doc, "genome_setbacks (GP104)", 0.5, 10, 1, [3.0, 2.5, 3.0, 2.5],
                             System.Drawing.Point(x0, gy3 + y_step))
    if gp_s: g3.append(gp_s)

    gp_o = create_slider(doc, "genome_orientation (GP105)", 0, 360, 0,
                          System.Drawing.Point(x0, gy3 + 2*y_step))
    if gp_o: g3.append(gp_o)

    # --- PANELS ---
    panel_fh = create_panel(doc, "floor_height", "3.0",
                             System.Drawing.Point(x0 + 2*x_step, gy3))
    if panel_fh: g3.append(panel_fh)

    panel_park = create_boolean_toggle(doc, "has_parking_ground", False,
                                        System.Drawing.Point(x0 + 2*x_step, gy3 + y_step))
    if panel_park: g3.append(panel_park)

    panel_comm = create_boolean_toggle(doc, "has_communal_ground", False,
                                        System.Drawing.Point(x0 + 2*x_step, gy3 + 2*y_step))
    if panel_comm: g3.append(panel_comm)

    panel_prog = create_panel(doc, "program_areas",
                               '{"1_hab": 42, "2_hab": 58, "3_hab": 75, "4_hab": 95}',
                               System.Drawing.Point(x0 + 3*x_step, gy3))
    if panel_prog: g3.append(panel_prog)

    panel_mix = create_panel(doc, "unit_mix_target",
                              '{"1_hab": 0.2, "2_hab": 0.4, "3_hab": 0.3, "4_hab": 0.1}',
                              System.Drawing.Point(x0 + 3*x_step, gy3 + y_step))
    if panel_mix: g3.append(panel_mix)

    panel_epw = create_file_path(doc, "epw_file",
                                  r"C:\Users\Dario Salas\proyectos\2-Entradas\Clima\BOGOTA_801510_IWEC.epw",
                                  System.Drawing.Point(x0 + 3*x_step, gy3 + 2*y_step))
    if panel_epw: g3.append(panel_epw)

    panel_north4 = create_panel(doc, "north_vector_wf", "0,1,0",
                                 System.Drawing.Point(x0 + 4*x_step, gy3))
    if panel_north4: g3.append(panel_north4)

    panel_period = create_panel(doc, "analysis_period", "0,1,2,3,4,5,6,7,8,9",
                                 System.Drawing.Point(x0 + 4*x_step, gy3 + y_step))
    if panel_period: g3.append(panel_period)

    # --- PYTHON SCRIPTS ---
    py_volumen = create_py_component(doc, "Python - VOLUMEN_v02",
                                      r"C:\Users\Dario Salas\proyectos\3-Proceso\GH_Scripts\VOLUMEN_v02.py",
                                      System.Drawing.Point(x0 + 5*x_step, gy3))
    if py_volumen: g3.append(py_volumen)

    py_diseno = create_py_component(doc, "Python - DISEÑO_INTERIOR_v01",
                                     r"C:\Users\Dario Salas\proyectos\3-Proceso\GH_Scripts\DISEÑO_INTERIOR_v01.py",
                                     System.Drawing.Point(x0 + 5*x_step, gy3 + 2*y_step))
    if py_diseno: g3.append(py_diseno)

    py_ladybug = create_py_component(doc, "Python - LADYBUG_v01",
                                       r"C:\Users\Dario Salas\proyectos\3-Proceso\GH_Scripts\LADYBUG_v01.py",
                                       System.Drawing.Point(x0 + 5*x_step, gy3 + 4*y_step))
    if py_ladybug: g3.append(py_ladybug)

    # Conexiones a VOLUMEN_v02 (py_volumen):
    # 0: sides_table
    # 1: pot_conclusions
    # 2: genome_heights (gp_h)
    # 3: genome_setbacks (gp_s)
    # 4: genome_orientation (gp_o)
    # 5: floor_height (panel_fh)
    # 6: has_parking_ground (panel_park)
    # 7: has_communal_ground (panel_comm)
    # 8: program_areas (panel_prog)
    # 9: unit_mix_target (panel_mix)
    # 10: sides_table also from py_lados output 0
    # 11: pot_conclusions from py_context output 0

    # Conectar Gene Pools
    connect(doc, gp_h, 0, py_volumen, 2)
    connect(doc, gp_s, 0, py_volumen, 3)
    connect(doc, gp_o, 0, py_volumen, 4)
    connect(doc, panel_fh, 0, py_volumen, 5)
    connect(doc, panel_park, 0, py_volumen, 6)
    connect(doc, panel_comm, 0, py_volumen, 7)
    connect(doc, panel_prog, 0, py_volumen, 8)
    connect(doc, panel_mix, 0, py_volumen, 9)

    # sides_table desde CONFIGURAR_LADOS (py_lados output 0)
    # pot_conclusions desde CONTEXTO (py_context output 0)
    connect(doc, py_lados, 0, py_volumen, 0)   # sides_table
    connect(doc, py_context, 0, py_volumen, 1) # pot_conclusions

    # Conexiones a DISEÑO_INTERIOR_v01 (py_diseno):
    # 0: core_positions (from py_volumen output core_positions)
    # 1: envelope_analysis (from py_volumen output envelope_analysis)
    # 1 outputs from VOLUMEN:
    #   0: building_breps
    #   1: floor_plates
    #   2: exterior_walls
    #   3: balconies
    #   4: slab_polygons
    #   5: wall_curves
    #   6: stair_polylines
    #   7: core_positions
    #   8: envelope_analysis
    #   9: nsr10_validation
    #   10: balcony_polygons
    #   11: balcony_curves

    connect(doc, py_volumen, 7, py_diseno, 0)  # core_positions
    connect(doc, py_volumen, 8, py_diseno, 1)  # envelope_analysis
    connect(doc, py_volumen, 1, py_diseno, 2)  # floor_plates
    connect(doc, py_volumen, 2, py_diseno, 3)  # exterior_walls
    connect(doc, panel_prog, 0, py_diseno, 4)  # program_areas
    connect(doc, panel_mix, 0, py_diseno, 5)   # unit_mix_target
    connect(doc, panel_fh, 0, py_diseno, 7)    # floor_height

    # Conexiones a LADYBUG_v01 (py_ladybug):
    # 0: building_envelope (py_volumen 0)
    # 1: floor_plates (py_volumen 1)
    # 2: exterior_walls (py_volumen 2)
    # 3: balconies (py_volumen 3)
    # 4: unit_polygons (py_diseno output 0)
    # 5: epw_file (panel_epw)
    # 6: north_vector (panel_north4)
    # 7: analysis_period (panel_period)
    connect(doc, py_volumen, 0, py_ladybug, 0)
    connect(doc, py_volumen, 1, py_ladybug, 1)
    connect(doc, py_volumen, 2, py_ladybug, 2)
    connect(doc, py_volumen, 3, py_ladybug, 3)
    connect(doc, py_diseno, 0, py_ladybug, 4)  # unit_polygons
    connect(doc, panel_epw, 0, py_ladybug, 5)
    connect(doc, panel_north4, 0, py_ladybug, 6)
    connect(doc, panel_period, 0, py_ladybug, 7)

    # --- LADYBUG/HONEYBEE NATIVE COMPONENTS ---
    lb_epw = create_comp(doc, "EPW File", "LB EPW File", "Ladybug", "File")
    if lb_epw: g3.append(lb_epw)
    connect(doc, panel_epw, 0, lb_epw, 0)

    lb_sky = create_comp(doc, "SkyMatrix", "LB SkyMatrix", "Ladybug", "Sun")
    # SkyMatrix está en Ladybug > Sun
    if lb_sky is None:
        lb_sky = create_comp(doc, "SkyMatrix", "LB SkyMatrix")  # búsqueda global
    if lb_sky: g3.append(lb_sky)
    connect(doc, lb_epw, 0, lb_sky, 0)
    connect(doc, panel_period, 0, lb_sky, 1)  # hoys

    lb_rad = create_comp(doc, "Radiation", "LB Radiation", "Ladybug", "Sun")
    if lb_rad is None:
        lb_rad = create_comp(doc, "Radiation", "LB Radiation")
    if lb_rad: g3.append(lb_rad)
    connect(doc, lb_sky, 0, lb_rad, 0)  # skyMatrix
    # geometry y testPoints desde py_ladybug outputs

    lb_sunpath = create_comp(doc, "SunPath", "LB SunPath", "Ladybug", "Sun")
    if lb_sunpath is None:
        lb_sunpath = create_comp(doc, "SunPath", "LB SunPath")
    if lb_sunpath: g3.append(lb_sunpath)
    connect(doc, lb_epw, 0, lb_sunpath, 0)
    connect(doc, panel_period, 0, lb_sunpath, 1)

    lb_direct = create_comp(doc, "Direct Sun Hours", "LB DirectSunHours", "Ladybug", "Sun")
    if lb_direct is None:
        lb_direct = create_comp(doc, "Direct Sun Hours", "LB DirectSunHours")
    if lb_direct: g3.append(lb_direct)
    connect(doc, lb_sunpath, 0, lb_direct, 0)  # sunPath
    # testPoints desde py_ladybug facade_sensors

    lb_utci = create_comp(doc, "UTCI", "LB UTCI", "Ladybug", "Comfort")
    if lb_utci is None:
        lb_utci = create_comp(doc, "UTCI", "LB UTCI")
    if lb_utci: g3.append(lb_utci)
    connect(doc, lb_epw, 0, lb_utci, 0)
    # testPoints desde py_ladybug facade_sensors

    # Honeybee
    hb_model = create_comp(doc, "HB Model", "HB Model", "Honeybee", "Create")
    if hb_model is None:
        hb_model = create_comp(doc, "HB Model", "HB Model")
    if hb_model: g3.append(hb_model)
    # rooms desde py_ladybug hb_rooms_data

    hb_da = create_comp(doc, "Daylight Autonomy", "HB sDA/ASE", "Honeybee", "Daylight")
    if hb_da is None:
        hb_da = create_comp(doc, "Daylight Autonomy", "HB sDA/ASE")
    if hb_da: g3.append(hb_da)
    connect(doc, hb_model, 0, hb_da, 0)
    # gridSize, hoys

    hb_df = create_comp(doc, "Daylight Factor", "HB DaylightFactor", "Honeybee", "Daylight")
    if hb_df is None:
        hb_df = create_comp(doc, "Daylight Factor", "HB DaylightFactor")
    if hb_df: g3.append(hb_df)
    connect(doc, hb_model, 0, hb_df, 0)

    # --- WALLACEI ---
    wallacei_x = create_comp(doc, "Wallacei X", "Wallacei X", "Wallacei", "Core")
    if wallacei_x is None:
        wallacei_x = create_comp(doc, "Wallacei X", "Wallacei X")
    if wallacei_x: g3.append(wallacei_x)
    connect(doc, gp_h, 0, wallacei_x, 0)
    connect(doc, gp_s, 0, wallacei_x, 1)
    connect(doc, gp_o, 0, wallacei_x, 2)

    wallacei_ctrl = create_comp(doc, "Wallacei Controller", "Wallacei Controller", "Wallacei", "Core")
    if wallacei_ctrl is None:
        wallacei_ctrl = create_comp(doc, "Wallacei Controller", "Wallacei Controller")
    if wallacei_ctrl: g3.append(wallacei_ctrl)
    connect(doc, wallacei_x, 0, wallacei_ctrl, 0)
    # Population=50, Generations=100 se configuran en el componente

    # 8 Objectives
    obj_configs = [
        ("f1: Sun Hours MAX", True),
        ("f2: Radiation MIN", False),
        ("f3: UTCI Comfort MAX", True),
        ("f4: sDA300/50% MAX", True),
        ("f5: ASE1000/250 MIN", False),
        ("f6: Daylight Factor MAX", True),
        ("f7: Balcony Shading MAX", True),
        ("f8: NSR-10 Daylight MAX", True),
    ]

    objectives = []
    for i, (nick, maximize) in enumerate(obj_configs):
        obj = create_comp(doc, "Objective", f"Obj {nick}", "Wallacei", "Core")
        if obj is None:
            obj = create_comp(doc, "Objective", f"Obj {nick}")
        if obj:
            g3.append(obj)
            objectives.append(obj)
            # Conectar desde py_ladybug fitness_inputs

    wallacei_sel = create_comp(doc, "Selection", "Wallacei Selection", "Wallacei", "Core")
    if wallacei_sel is None:
        wallacei_sel = create_comp(doc, "Selection", "Wallacei Selection")
    if wallacei_sel: g3.append(wallacei_sel)
    connect(doc, wallacei_ctrl, 0, wallacei_sel, 0)
    # Conectar objectives

    # --- ARCHICAD NATIVE COMPONENTS ---
    ac_slab_floors = create_comp(doc, "Slab", "AC Slab Floors", "Graphisoft", "Elements")
    if ac_slab_floors is None:
        ac_slab_floors = create_comp(doc, "Slab", "AC Slab Floors")
    if ac_slab_floors: g3.append(ac_slab_floors)
    # polygon desde py_volumen slab_polygons (output 4)

    ac_wall_ext = create_comp(doc, "Wall", "AC Wall Exterior", "Graphisoft", "Elements")
    if ac_wall_ext is None:
        ac_wall_ext = create_comp(doc, "Wall", "AC Wall Exterior")
    if ac_wall_ext: g3.append(ac_wall_ext)
    # baseLine desde py_volumen wall_curves (5), height desde floor_data

    ac_slab_bal = create_comp(doc, "Slab", "AC Slab Balconies", "Graphisoft", "Elements")
    if ac_slab_bal is None:
        ac_slab_bal = create_comp(doc, "Slab", "AC Slab Balconies")
    if ac_slab_bal: g3.append(ac_slab_bal)
    # polygon desde py_volumen balcony_polygons (10)

    ac_stair = create_comp(doc, "Stair", "AC Stair", "Graphisoft", "Elements")
    if ac_stair is None:
        ac_stair = create_comp(doc, "Stair", "AC Stair")
    if ac_stair: g3.append(ac_stair)
    # baseLine desde py_volumen stair_polylines (6)

    ac_wall_elev = create_comp(doc, "Wall", "AC Wall Elevator", "Graphisoft", "Elements")
    if ac_wall_elev is None:
        ac_wall_elev = create_comp(doc, "Wall", "AC Wall Elevator")
    if ac_wall_elev: g3.append(ac_wall_elev)

    ac_zone = create_comp(doc, "Zone", "AC Zone Units", "Graphisoft", "Elements")
    if ac_zone is None:
        ac_zone = create_comp(doc, "Zone", "AC Zone Units")
    if ac_zone: g3.append(ac_zone)
    # boundary desde py_diseno unit_polygons (0)

    ac_wall_part = create_comp(doc, "Wall", "AC Wall Partitions", "Graphisoft", "Elements")
    if ac_wall_part is None:
        ac_wall_part = create_comp(doc, "Wall", "AC Wall Partitions")
    if ac_wall_part: g3.append(ac_wall_part)
    # baseLine desde py_diseno partition_walls (1)

    ac_door = create_comp(doc, "Door", "AC Door", "Graphisoft", "Elements")
    if ac_door is None:
        ac_door = create_comp(doc, "Door", "AC Door")
    if ac_door: g3.append(ac_door)
    # unit_doors desde py_diseno (3)

    ac_window = create_comp(doc, "Window", "AC Window", "Graphisoft", "Elements")
    if ac_window is None:
        ac_window = create_comp(doc, "Window", "AC Window")
    if ac_window: g3.append(ac_window)
    # unit_windows desde py_diseno (4)

    # Offset Curve nativo para balcones (desde exterior_walls)
    offset_crv = create_comp(doc, "Offset Curve", "Offset Balcon Curves")
    if offset_crv is None:
        offset_crv = create_comp(doc, "Offset Curve", "Offset Balcon Curves")
    if offset_crv: g3.append(offset_crv)
    connect(doc, py_volumen, 2, offset_crv, 0)  # exterior_walls
    # Distance desde py_lados balcon_max_depth_m (output por lado)

    loft = create_comp(doc, "Loft", "Loft Balconies")
    if loft is None:
        loft = create_comp(doc, "Loft", "Loft Balconies")
    if loft: g3.append(loft)
    connect(doc, offset_crv, 0, loft, 0)
    connect(doc, py_volumen, 2, loft, 1)  # exterior_walls como rail

    # ============================================================
    # GRUPOS
    # ============================================================
    groups_data.append(("GRUPO 3: WALLACEI_FITNESS", "GRUPO 3: WALLACEI_FITNESS", "#DC143C",
                        [c.InstanceGuid for c in g3 if c],
                        System.Drawing.Point(x0 - 150, gy3 - 100)))
    all_member_guids.extend([c.InstanceGuid for c in g3 if c])

    # Crear grupos en el documento
    for name, nick, color, guids, loc in groups_data:
        create_group(doc, name, nick, color, guids, loc)

    # Forzar redibujado
    doc.ScheduleSolution(1, lambda d: gh.Instances.ActiveCanvas.Refresh())

    print("=== CANVAS BUILD COMPLETE ===")
    print("PRÓXIMOS PASOS:")
    print("1. Pegar código Python en los 5 componentes Python Script:")
    print("   - Python - CONFIGURAR_LADOS_POT  →  CONFIGURAR_LADOS_v03.py")
    print("   - Python - CONTEXTO_POT_v04      →  CONTEXTO_v04.py")
    print("   - Python - VOLUMEN_v02           →  VOLUMEN_v02.py")
    print("   - Python - DISEÑO_INTERIOR_v01   →  DISEÑO_INTERIOR_v01.py")
    print("   - Python - LADYBUG_v01           →  LADYBUG_v01.py")
    print("2. Verificar conexiones de Ladybug/Honeybee (algunas requieren setup manual)")
    print("3. Configurar Gene Pools con valores reales del proyecto")
    print("4. Configurar Wallacei Controller: Population=50, Generations=100")
    print("5. Configurar objetivos Wallacei: f1-f8 MAX/MIN según tabla")
    print("6. Guardar como .ghx (File > Save)")

if __name__ == "__main__":
    build_canvas()