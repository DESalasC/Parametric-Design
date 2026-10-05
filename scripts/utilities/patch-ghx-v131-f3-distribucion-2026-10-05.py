# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.1.ghx: F3_DISTRIBUCION v03 -> v03.2 (sección GH + detección ghenv).

Cambios (2026-10-05):
  1. Componente #61-F3_DISTRIBUCION_v03.py -> embebe el
     src/fase-3-masa/F3_DISTRIBUCION_v03.py corregido (v03.3):
       - FIX IronPython 2.7: sin anotación de tipo py3 en normalizar_uso()
         (provocaba SyntaxErrorException "unexpected token ':'" en GHPython);
       - SECCIÓN GRASSHOPPER completa (lee entradas del canvas y publica las
         7 salidas GH: barras_json, mensaje, alternativa_recomendada,
         ocupacion_total_m2, gfa_real_m2, floor_h_usado, n_barras_usado);
       - v03.2: detección de entorno GH vía `"ghenv" in globals()` (en Rhino 8
         `import ghenv` FALLA: se inyecta como variable; main() ya no corre
         dentro de Grasshopper) + guard CLI con detección IronPython/clr;
       - v03.3: lectura JSON con patrón canónico (rb + cascada utf-8-sig →
         cp1252 → latin-1; evita el codec "unknown" de IronPython) y pasos de
         diagnóstico en el mensaje; barras_json/JSON en ensure_ascii=True.
  2. Renombra las entradas con guion a snake_case (convención del proyecto):
       presupuesto-ocupacion -> presupuesto_ocupacion_m2
       io-max                -> io_max
       n-barras              -> n_barras_objetivo
       entrepiso-adaptativo  -> entrepiso_adaptativo
       prioridad-ajuste      -> prioridad_ajuste
       bloques-separacion-m  -> bloques_separacion_m
       bloques-crujia        -> bloques_crujia
       bloques-nucleo        -> bloques_nucleo
       output-json           -> output_json
     (chip y usos no cambian; los cables se conservan: el único cable de
     entrada es chip -> F0_LOAD_PROYECTO_v01.chip.)
  3. Actualiza la Description del componente (cableado resumido).
  4. Backup .bak-<ts>, validaciones y escritura con BOM (misma técnica que
     patch-ghx-v12-patio-v031-2026-09-30.py, con comentarios preservados).

Uso: .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v131-f3-distribucion-2026-10-05.py
"""
import io
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.1.ghx")
SRC = os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py")

INSTANCE_GUID = "6eaf2956-f649-4540-a900-4b32a10deee4"

RENOMBRES = {
    "presupuesto-ocupacion": "presupuesto_ocupacion_m2",
    "io-max": "io_max",
    "n-barras": "n_barras_objetivo",
    "entrepiso-adaptativo": "entrepiso_adaptativo",
    "prioridad-ajuste": "prioridad_ajuste",
    "bloques-separacion-m": "bloques_separacion_m",
    "bloques-crujia": "bloques_crujia",
    "bloques-nucleo": "bloques_nucleo",
    "output-json": "output_json",
}

DESCRIPCION = (
    "F3_DISTRIBUCION v03.3 - Distribuidor de barras por crujia (presupuesto IO). "
    "ENTRADAS (Item salvo indicacion): chip <- F0_LOAD_PROYECTO_v01.chip | "
    "presupuesto_ocupacion_m2 (Number; si vacio se deriva = lote x io_max con margen) | "
    "io_max (0.70) | n_barras_objetivo (2 | 3 | '2,3') | entrepiso_adaptativo (Boolean) | "
    "prioridad_ajuste (List; reservado) | usos (List; filtra mix, p.ej. 'Vivienda,Local comercial') | "
    "bloques_separacion_m (6.0) | bloques_crujia ('unica'|'doble') | bloques_nucleo ('centro'|'extremo') | "
    "output_json (ruta opcional). SALIDAS: barras_json -> NORMATIVA v09.barras_json | mensaje | "
    "alternativa_recomendada | ocupacion_total_m2 | gfa_real_m2 | floor_h_usado | n_barras_usado. "
    "Doc: encabezado del script + docs/planes/2026-10-03-tope-ocupacion-io/PLAN-ACCION.md"
)


def nick_of(obj):
    for i in obj.iter('item'):
        if i.get('name') == 'NickName' and i.text:
            return i.text.strip()
    return ''


def container_items(obj):
    for c in obj.iter('chunk'):
        if c.get('name') == 'Container':
            return c
    return None


def cont_get(obj, name):
    c = container_items(obj)
    if c is None:
        return None
    for w in c:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item' and i.get('name') == name:
                    return i
    return None


def find_component(root):
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        c = container_items(o)
        if c is None:
            continue
        for w in c:
            if w.tag == 'items':
                for i in w:
                    if i.tag == 'item' and i.get('name') == 'InstanceGuid' \
                       and (i.text or '').strip() == INSTANCE_GUID:
                        return o
    # Fallback por nickname
    for o in root.iter('chunk'):
        if o.get('name') == 'Object' and 'F3_DISTRIBUCION_v03' in nick_of(o):
            return o
    return None


def param_names(obj):
    """Nombres de los InputParam del componente."""
    names = []
    for ch in obj.iter('chunk'):
        if ch.get('name') != 'InputParam':
            continue
        for w in ch:
            if w.tag == 'items':
                for i in w:
                    if i.tag == 'item' and i.get('name') == 'Name':
                        names.append((i.text or '').strip())
    return names


def count_sibling_dups(rt):
    bad_c = 0
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
    return bad_c


def main():
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(GHX, parser=parser)
    root = tree.getroot()

    obj = find_component(root)
    if obj is None:
        print('ERROR: no se encontro el componente F3_DISTRIBUCION_v03 en', GHX)
        sys.exit(1)
    print('Componente:', nick_of(obj))

    # --- 1. CodeInput ---
    code_new = io.open(SRC, 'r', encoding='utf-8').read().replace('\r\n', '\n')
    ci = cont_get(obj, 'CodeInput')
    print('CodeInput previo: {} chars | nuevo: {} chars'.format(len(ci.text or ''), len(code_new)))
    ci.text = code_new

    # --- 2. Renombres de entradas (Name y NickName) ---
    renombrados = 0
    for ch in obj.iter('chunk'):
        if ch.get('name') != 'InputParam':
            continue
        for w in ch:
            if w.tag != 'items':
                continue
            for i in w:
                if i.tag != 'item':
                    continue
                if i.get('name') in ('Name', 'NickName'):
                    viejo = (i.text or '').strip()
                    if viejo in RENOMBRES:
                        i.text = RENOMBRES[viejo]
                        renombrados += 1
    print('Renombres aplicados (items Name/NickName):', renombrados)

    # --- 3. Description ---
    de = cont_get(obj, 'Description')
    print('Description previa: {} chars | nueva: {} chars'.format(
        len(de.text or ''), len(DESCRIPCION)))
    de.text = DESCRIPCION

    # --- 4. Counts ---
    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    # --- 5. Validaciones ---
    txt = ET.tostring(root, encoding='unicode')

    try:
        ET.fromstring(txt)
        xml_ok = True
    except Exception:
        xml_ok = False

    obj2 = find_component(root)
    names2 = param_names(obj2)
    esperados = {
        'chip', 'presupuesto_ocupacion_m2', 'io_max', 'n_barras_objetivo',
        'entrepiso_adaptativo', 'prioridad_ajuste', 'usos',
        'bloques_separacion_m', 'bloques_crujia', 'bloques_nucleo', 'output_json',
    }
    viejos = set(RENOMBRES.keys())

    # chip conserva su cable (Source presente)
    chip_items = None
    for ch in obj2.iter('chunk'):
        if ch.get('name') != 'InputParam':
            continue
        es_chip = False
        for w in ch:
            if w.tag == 'items':
                for i in w:
                    if i.tag == 'item' and i.get('name') == 'Name' and (i.text or '').strip() == 'chip':
                        es_chip = True
        if es_chip:
            chip_items = []
            for w in ch:
                if w.tag == 'items':
                    for i in w:
                        if i.tag == 'item':
                            chip_items.append((i.get('name'), (i.text or '').strip()))
    chip_src = any(n == 'Source' for n, _v in chip_items or [])
    chip_src_count = any(n == 'SourceCount' and v == '1' for n, v in chip_items or [])

    dups_chunk = count_sibling_dups(root)
    seen = {}
    dups_guid = 0
    for i in root.iter('item'):
        if i.get('name') == 'InstanceGuid' and i.text:
            g = i.text.strip()
            if g in seen:
                dups_guid += 1
            seen[g] = True

    checks = [
        ('XML serializado re-parseable', xml_ok),
        ('code con seccion GH', 'SECCIÓN GRASSHOPPER' in (ci.text or '') or 'SECCION GRASSHOPPER' in (ci.text or '')),
        ('code v03.3', 'v03.3' in (ci.text or '')),
        ('code con _gh_leer', 'def _gh_leer' in (ci.text or '')),
        ('code con _gh_modulo', 'def _gh_modulo' in (ci.text or '')),
        ('code con _leer_json', 'def _leer_json' in (ci.text or '')),
        ('code con _texto_seguro', 'def _texto_seguro' in (ci.text or '')),
        ('code con ghdoc (2a senal)', 'ghdoc' in (ci.text or '')),
        ('code con barras_json json.dumps', 'barras_json = json.dumps' in (ci.text or '')),
        ('entradas renombradas == esperados', set(names2) == esperados),
        ('sin nombres viejos con guion', not (set(names2) & viejos)),
        ('chip conserva Source (cable F0)', chip_src and chip_src_count),
        ('sin duplicados de chunk', dups_chunk == 0),
        ('sin InstanceGuid duplicados', dups_guid == 0),
    ]
    ok = True
    for nm, okc in checks:
        print('  [{}] {}'.format('OK' if okc else 'FAIL', nm))
        ok = ok and okc
    if not ok:
        print('VALIDACION FALLIDA - no se escribe'); sys.exit(1)

    # --- 6. Escritura con backup ---
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = GHX + '.bak-' + ts
    shutil.copy2(GHX, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(GHX, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup:', bak)
    print('escrito:', GHX)
    print('OK PATCH F3_DISTRIBUCION v03.3 aplicado')


if __name__ == '__main__':
    main()
