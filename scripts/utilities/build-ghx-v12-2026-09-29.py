# -*- coding: utf-8 -*-
"""Ensambla F1_CONTEXTO_v12.ghx (rama 3D minima) desde el v11 parcheado.

Parte de `gh-definitions/F1_CONTEXTO_v11.ghx` (YA parcheado con P0) y agrega
SOLO la rama 3D acordada (2026-09-29):

  - F1_ETAPA1_CONTEXTO_3D_v01.py    (json_path + 2 toggles -> 12 salidas)
  - F1_ETAPA2_ENVOLVENTE_3D_v01.py  (envelope #113 + topo -> curva/banda/volumen)
  - 3x "Morph Curve"  (lote, vecinos, envolvente)
  - 2x "Morph Solid"  (bandas de contexto, volumen de envolvente)
  - 1x "Mesh"         (terreno: topo_pts + topo_boundary)
  - 3x "Boolean Toggle" (T1 curvas=ON, T2 cintas=ON, T3 volumen=OFF)

Plantillas serializadas (extraidas del canvas v11 y del corpus LC el
2026-09-29) en scripts/utilities/lc_templates/. Todos los GUIDs de instancia
de los nodos nuevos se regeneran; se validan colisiones y que cada Source
nuevo apunte a un GUID existente. NO toca el v11.

Salida: gh-definitions/F1_CONTEXTO_v12.ghx (+ reporte). Regenerar .gh:
  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 `
    -InputGhx gh-definitions/F1_CONTEXTO_v12.ghx -OutputGh gh-definitions/F1_CONTEXTO_v12.gh
"""
import copy
import io
import os
import shutil
import sys
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TPL = os.path.join(BASE, "scripts", "utilities", "lc_templates")
PAR = os.path.join(TPL, "params")
V11 = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v11.ghx")
V12 = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v12.ghx")

SRC_3D = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_3D_v01.py")
SRC_ENV = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_ENVOLVENTE_3D_v01.py")

new_guids = []


def nu():
    g = str(uuid.uuid4())
    new_guids.append(g)
    return g


def load(path):
    return ET.parse(path).getroot()


def parse_str(xml_text):
    return ET.fromstring(xml_text)


def load_param(fname):
    with io.open(os.path.join(PAR, fname), "r", encoding="utf-8") as f:
        return ET.fromstring(f.read())


def nick_of(obj):
    for i in obj.iter('item'):
        if i.get('name') == 'NickName' and i.text:
            return i.text.strip()
    return ''


def find_obj(root, prefix):
    hits = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        nick = nick_of(o)
        if nick.startswith(prefix):
            hits.append(o)
    return hits


def find_obj_exact(root, name):
    hits = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        if nick_of(o) == name:
            hits.append(o)
    return hits


def container(obj):
    for c in obj.iter('chunk'):
        if c.get('name') == 'Container':
            return c
    return None


def cont_wrapper(cont):
    for w in cont:
        if w.tag == 'items':
            return w
    return None


def cont_get(obj, name):
    cont = container(obj)
    w = cont_wrapper(cont)
    if w is None:
        return None
    for i in w:
        if i.tag == 'item' and i.get('name') == name:
            return i
    return None


def cont_set(obj, name, value):
    i = cont_get(obj, name)
    if i is None:
        w = cont_wrapper(container(obj))
        i = ET.SubElement(w, 'item', {'name': name, 'type_name': 'gh_string', 'type_code': '10'})
    i.text = value
    return i


def set_item_first(obj, name, value):
    for i in obj.iter('item'):
        if i.get('name') == name:
            i.text = value
            return i
    return None


def set_pivot(obj, x, y):
    for it in obj.iter('item'):
        if it.get('name') == 'Pivot':
            for c in it:
                if c.tag == 'X':
                    c.text = str(x)
                if c.tag == 'Y':
                    c.text = str(y)
            break
    for it in obj.iter('item'):
        if it.get('name') == 'Bounds':
            for c in it:
                if c.tag == 'X':
                    c.text = str(x - 90)
                if c.tag == 'Y':
                    c.text = str(y - 40)
            break


def regen_guids(obj):
    for i in obj.iter('item'):
        if i.get('name') == 'InstanceGuid':
            i.text = nu()


def clear_sources(obj):
    par = {c: p for p in obj.iter() for c in p}
    for it in list(obj.iter('item')):
        if it.get('name') == 'Source':
            p = par.get(it)
            if p is not None:
                p.remove(it)
    for it in obj.iter('item'):
        if it.get('name') == 'SourceCount':
            it.text = '0'


def param_chunks(obj, kinds=('param_input', 'InputParam', 'param_output', 'OutputParam')):
    out = []
    for ch in obj.iter('chunk'):
        if ch.get('name') in kinds:
            out.append(ch)
    return out


def param_name(ch):
    for i in ch.iter('item'):
        if i.get('name') == 'Name':
            return (i.text or '').strip()
    return ''


def param_guid(ch):
    for i in ch.iter('item'):
        if i.get('name') == 'InstanceGuid':
            return (i.text or '').strip()
    return ''


def par_map(obj):
    ins = {}
    outs = {}
    for ch in param_chunks(obj):
        nm = param_name(ch)
        if not nm:
            continue
        if ch.get('name') in ('param_input', 'InputParam'):
            ins[nm] = ch
        else:
            outs[nm] = ch
    return ins, outs


def set_source(ch, source_guid):
    sc = None
    src = None
    for i in ch.iter('item'):
        if i.get('name') == 'SourceCount':
            sc = i
        if i.get('name') == 'Source':
            src = i
    if sc is None:
        # insertar SourceCount junto a Name/NickName si falta
        w = None
        for ww in ch.iter():
            if ww.tag == 'items' and any(x.get('name') == 'Name' for x in ww):
                w = ww
                break
        sc = ET.SubElement(w, 'item', {'name': 'SourceCount', 'type_name': 'gh_int32', 'type_code': '3'})
    sc.text = '1'
    if src is None:
        w = None
        for ww in ch.iter():
            if ww.tag == 'items' and any(x.get('name') == 'SourceCount' for x in ww):
                w = ww
                break
        src = ET.SubElement(w, 'item', {'name': 'Source', 'type_name': 'gh_guid', 'type_code': '9'})
    src.text = source_guid


def wire_param(obj, param_name_, source_guid):
    for ch in param_chunks(obj):
        if param_name(ch) == param_name_:
            set_source(ch, source_guid)
            return True
    return False


def fix_counts(root):
    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))


def make_python_comp(template, nick, code_text, inputs_spec, outputs_spec, pivot):
    """inputs_spec/outputs_spec: [(name, param_template_filename), ...]"""
    obj = copy.deepcopy(template)
    params = param_chunks(obj)
    in_chunks = [c for c in params if c.get('name') in ('param_input', 'InputParam')]
    out_chunks = [c for c in params if c.get('name') in ('param_output', 'OutputParam')]
    par = {c: p for p in obj.iter() for c in p}
    in_parent = par.get(in_chunks[0]) if in_chunks else None
    out_parent = par.get(out_chunks[0]) if out_chunks else None
    if in_parent is None or out_parent is None:
        raise RuntimeError('plantilla sin parametros esperados')
    for c in params:
        par[c].remove(c)

    def add(tpl_file, name, dest_parent):
        ch = load_param(tpl_file)
        for i in ch.iter('item'):
            if i.get('name') == 'Name':
                i.text = name
            if i.get('name') == 'NickName':
                i.text = name
        for i in ch.iter('item'):
            if i.get('name') == 'InstanceGuid':
                i.text = nu()
        # limpiar fuentes heredadas
        p2 = {c: p for p in ch.iter() for c in p}
        for it in list(ch.iter('item')):
            if it.get('name') == 'Source':
                p2[it].remove(it)
        for it in ch.iter('item'):
            if it.get('name') == 'SourceCount':
                it.text = '0'
        # indice secuencial dentro del padre (evita colisiones GH_IO)
        idx = len([c for c in list(dest_parent) if c.tag == 'chunk'])
        ch.set('index', str(idx))
        dest_parent.append(ch)
        return ch

    for name, tpl_file in inputs_spec:
        add(tpl_file, name, in_parent)
    for name, tpl_file in outputs_spec:
        add(tpl_file, name, out_parent)

    cont_set(obj, 'NickName', nick)
    cont_set(obj, 'InstanceGuid', nu())
    cont_set(obj, 'CodeInput', code_text)
    set_item_first(obj, 'InputCount', str(len(inputs_spec)))
    set_item_first(obj, 'OutputCount', str(len(outputs_spec)))
    set_pivot(obj, pivot[0], pivot[1])
    return obj


def clone_lc(template, nick, wiring, pivot, toggle_value=None):
    obj = copy.deepcopy(template)
    regen_guids(obj)
    cont_set(obj, 'NickName', nick)
    clear_sources(obj)
    for pname, src in wiring.items():
        if not wire_param(obj, pname, src):
            raise RuntimeError('no se pudo cablear {0} en {1}'.format(pname, nick))
    set_pivot(obj, pivot[0], pivot[1])
    if toggle_value is not None:
        i = cont_get(obj, 'ToggleValue')
        if i is not None:
            i.text = 'true' if toggle_value else 'false'
    return obj


def main():
    with io.open(SRC_3D, 'r', encoding='utf-8') as f:
        code_3d = f.read()
    with io.open(SRC_ENV, 'r', encoding='utf-8') as f:
        code_env = f.read()

    tree = ET.parse(V11)
    root = tree.getroot()

    # --- localizar referencias del canvas vigente ---
    o21 = find_obj(root, '#21-')
    o113 = find_obj(root, '#113-')
    o60 = find_obj(root, '#60-')
    if not (o21 and o113 and o60):
        print('ERROR: no se localizaron #21/#113/#60 en v11')
        sys.exit(1)
    obj21, obj113, obj60 = o21[0], o113[0], o60[0]

    ins21, _ = par_map(obj21)
    _, outs113 = par_map(obj113)

    def src_of(ch):
        for i in ch.iter('item'):
            if i.get('name') == 'Source':
                return (i.text or '').strip()
        return None

    guid21_json = src_of(ins21['json_path'])
    guid113_env = param_guid(outs113['envelope_curve'])
    guid113_alt = param_guid(outs113['altura_total'])
    guid60 = cont_get(obj60, 'InstanceGuid').text.strip()
    if not (guid21_json and guid113_env and guid113_alt and guid60):
        print('ERROR: faltan referencias (json_path/envelope/altura/sync): {0} {1} {2} {3}'.format(
            guid21_json, guid113_env, guid113_alt, guid60))
        sys.exit(1)
    print('refs: json_path<- {0} | envelope {1} | altura {2} | sync {3}'.format(
        guid21_json[:8], guid113_env[:8], guid113_alt[:8], guid60[:8]))

    # --- plantillas ---
    tpl_py = copy.deepcopy(obj21)          # componente GhPython base
    tpl_mc = load(os.path.join(TPL, 'lcchunk_Morph_Curve.xml'))
    tpl_ms = load(os.path.join(TPL, 'chunk_74.xml'))          # Morph Solid (canvas)
    tpl_mesh = load(os.path.join(TPL, 'lcchunk_Mesh.xml'))
    tpl_tog = load(os.path.join(TPL, 'chunk_130.xml'))

    # --- componentes nuevos ---
    inputs_3d = [
        ('json_path', 'v21in_json_path.xml'),
        ('mostrar_curvas', 'v48in_bake.xml'),
        ('mostrar_cintas', 'v48in_exportar.xml'),
    ]
    outputs_3d = [
        ('bandas_lote', 'v21out_topo_mesh.xml'),
        ('bandas_vecinos', 'v21out_vecinos_curves.xml'),
        ('bandas_vias', 'v21out_vecinos_curves.xml'),
        ('bandas_ep', 'v21out_vecinos_curves.xml'),
        ('bandas_todas', 'v21out_vecinos_curves.xml'),
        ('curvas_lote', 'v21out_lot_curve.xml'),
        ('curvas_vecinos', 'v21out_vecinos_curves.xml'),
        ('curvas_vias', 'v21out_vecinos_curves.xml'),
        ('curvas_ep', 'v21out_vecinos_curves.xml'),
        ('topo_pts', 'v21out_vecinos_curves.xml'),
        ('topo_boundary', 'v21out_lot_curve.xml'),
        ('mensaje', 'v21out_mensaje.xml'),
    ]
    c3d = make_python_comp(tpl_py, 'F1_ETAPA1_CONTEXTO_3D_v01.py', code_3d, inputs_3d, outputs_3d, (9200, 320))

    inputs_env = [
        ('envelope_curve', 'v113in_lot_polygon.xml'),
        ('altura_total', 'v113in_altura_max_pot.xml'),
        ('topo_pts', 'v99in_lot_vertices.xml'),
        ('mostrar_curva', 'v48in_bake.xml'),
        ('mostrar_banda', 'v48in_exportar.xml'),
        ('mostrar_volumen', 'v48in_bake.xml'),
    ]
    outputs_env = [
        ('curva_3d', 'v21out_lot_curve.xml'),
        ('banda_3d', 'v21out_topo_mesh.xml'),
        ('volumen_3d', 'v21out_topo_mesh.xml'),
        ('mensaje', 'v21out_mensaje.xml'),
    ]
    cenv = make_python_comp(copy.deepcopy(tpl_py), 'F1_ETAPA2_ENVOLVENTE_3D_v01.py', code_env,
                            inputs_env, outputs_env, (9200, 1400))

    # guids de salidas/inputs de los componentes nuevos
    _, out3d = par_map(c3d)
    in3d, _ = par_map(c3d)
    _, outenv = par_map(cenv)
    inenv, _ = par_map(cenv)

    def og(map_, name):
        return param_guid(map_[name])

    # --- toggles ---
    t1 = clone_lc(tpl_tog, 'T1-mostrar_curvas', {}, (9000, 2500), toggle_value=True)
    t2 = clone_lc(tpl_tog, 'T2-mostrar_cintas', {}, (9000, 2580), toggle_value=True)
    t3 = clone_lc(tpl_tog, 'T3-mostrar_volumen', {}, (9000, 2660), toggle_value=False)
    g_t1 = cont_get(t1, 'InstanceGuid').text.strip()
    g_t2 = cont_get(t2, 'InstanceGuid').text.strip()
    g_t3 = cont_get(t3, 'InstanceGuid').text.strip()

    # --- morfos / malla ---
    mc1 = clone_lc(tpl_mc, 'MC1-lote_3D', {'Synchronize': guid60, 'Curve': og(out3d, 'curvas_lote')}, (10100, 300))
    mc2 = clone_lc(tpl_mc, 'MC2-vecinos_3D', {'Synchronize': guid60, 'Curve': og(out3d, 'curvas_vecinos')}, (10100, 620))
    mc3 = clone_lc(tpl_mc, 'MC3-envolvente_3D', {'Synchronize': guid60, 'Curve': og(outenv, 'curva_3d')}, (10100, 940))
    ms1 = clone_lc(tpl_ms, 'MS1-contexto_3D', {'Synchronize': guid60, 'Mesh': og(out3d, 'bandas_todas')}, (10100, 1500))
    ms2 = clone_lc(tpl_ms, 'MS2-volumen_3D', {'Synchronize': guid60, 'Mesh': og(outenv, 'volumen_3d')}, (10100, 1820))
    m1 = clone_lc(tpl_mesh, 'M1-terreno_3D', {'Synchronize': guid60, 'Points': og(out3d, 'topo_pts'),
                                              'Boundary': og(out3d, 'topo_boundary')}, (10100, 2140))

    # --- cablear entradas de los componentes nuevos ---
    wire_param(c3d, 'json_path', guid21_json)
    wire_param(c3d, 'mostrar_curvas', g_t1)
    wire_param(c3d, 'mostrar_cintas', g_t2)
    wire_param(cenv, 'envelope_curve', guid113_env)
    wire_param(cenv, 'altura_total', guid113_alt)
    wire_param(cenv, 'topo_pts', og(out3d, 'topo_pts'))
    wire_param(cenv, 'mostrar_curva', g_t1)
    wire_param(cenv, 'mostrar_banda', g_t2)
    wire_param(cenv, 'mostrar_volumen', g_t3)

    # --- insertar en el contenedor de objetos ---
    def_objs = None
    wrapper = None
    for c in root.iter('chunk'):
        if c.get('name') == 'DefinitionObjects':
            def_objs = c
            break
    if def_objs is None:
        print('ERROR: sin DefinitionObjects')
        sys.exit(1)
    for w in def_objs.iter():
        if w.tag == 'chunks' and any(x.get('name') == 'Object' for x in w):
            wrapper = w
            break
    if wrapper is None:
        print('ERROR: sin wrapper de objetos')
        sys.exit(1)
    base_count = len([x for x in wrapper if x.tag == 'chunk' and x.get('name') == 'Object'])
    nuevos = [c3d, cenv, t1, t2, t3, mc1, mc2, mc3, ms1, ms2, m1]
    for k, obj in enumerate(nuevos):
        obj.set('index', str(base_count + k))
        wrapper.append(obj)

    fix_counts(root)

    # --- validaciones ---
    root2 = ET.fromstring(ET.tostring(root, encoding='utf-8'))
    new_count = len([x for x in wrapper if x.tag == 'chunk' and x.get('name') == 'Object'])
    # colisiones de InstanceGuid
    seen = {}
    dups = 0
    for i in root2.iter('item'):
        if i.get('name') == 'InstanceGuid' and i.text:
            g = i.text.strip()
            if g in seen:
                dups += 1
            seen[g] = True
    # sources nuevos resueltos
    unresolved = 0
    for i in root2.iter('item'):
        if i.get('name') == 'Source' and i.text:
            g = i.text.strip()
            if g not in seen and g not in set(new_guids):
                unresolved += 1
    print('objetos base:', base_count, '| tras insertar:', new_count)
    print('instanceguids unicos:', len(seen), '| duplicados:', dups, '| sources sin resolver:', unresolved)

    # duplicados hermano: SOLO chunk (name+index) es fatal para GH_IO;
    # los duplicados de item (ID/InputId/OutputId) existen en el documento
    # base y GH los tolera (se reportan como informacion).
    def count_sibling_dups(rt):
        bad_c = 0
        bad_i = 0
        for w in rt.iter():
            if w.tag == 'chunks':
                s = {}
                for c in w:
                    if c.tag != 'chunk':
                        continue
                    key = (c.get('name'), c.get('index'))
                    if key in s:
                        bad_c += 1
                    s[key] = 1
            elif w.tag == 'items':
                s2 = set()
                for i2 in w:
                    if i2.tag != 'item':
                        continue
                    nm2 = i2.get('name')
                    if nm2 in s2:
                        bad_i += 1
                    s2.add(nm2)
        return bad_c, bad_i

    dups_chunk, dups_item = count_sibling_dups(root2)

    ok = (new_count == base_count + len(nuevos)) and dups == 0 and dups_chunk == 0
    print('duplicados hermano v12 -> chunks:', dups_chunk, '| items (tolerados):', dups_item)
    # marcadores
    txt = ET.tostring(root2, encoding='unicode')
    for marker in ('bandas_todas', 'F1_ETAPA1_CONTEXTO_3D_v01.py', 'F1_ETAPA2_ENVOLVENTE_3D_v01.py',
                   'MC1-lote_3D', 'MC2-vecinos_3D', 'MC3-envolvente_3D', 'MS1-contexto_3D',
                   'MS2-volumen_3D', 'M1-terreno_3D', 'T1-mostrar_curvas', 'T2-mostrar_cintas',
                   'T3-mostrar_volumen'):
        res = marker in txt
        ok = ok and res
        if not res:
            print('FALTA marcador:', marker)
    if not ok:
        print('VALIDACION FALLIDA')
        sys.exit(1)

    if os.path.exists(V12):
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(V12, V12 + ".bak-" + ts)
        print('backup v12 previo')
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(V12, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('escrito:', V12)
    print('OK v12: {0} objetos nuevos, 0 duplicados'.format(len(nuevos)))


if __name__ == '__main__':
    main()
