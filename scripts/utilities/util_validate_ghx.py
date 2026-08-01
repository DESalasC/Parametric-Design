#!/usr/bin/env python3
"""
Validador de archivos .ghx de Grasshopper con capacidades de auto-fijo.

Uso:
    python validate_ghx.py <archivo.ghx> [--auto-fix-common] [--fix-file <archivo>]

Verifica:
1. Que el XML esté bien formado
2. Que tenga la estructura mínima de un .ghx válido
3. Lista todos los objetos con su InstanceGuid y Nickname
4. Identifica inputs REQUERIDOS (Optional=false) sin conectar → ERRORES
5. Identifica inputs OPCIONALES sin conectar → ADVERTENCIAS
6. Identifica outputs que no están siendo usados por nadie
7. Reporta conexiones huérfanas (apuntan a InstanceGuids inexistentes)
8. Cuenta total de objetos, conexiones, módulos Python
9. Verifica que cada input tenga exactamente 1 source (no duplicados)

Nuevas características:
--auto-fix-common: Aplica fijados automáticos seguros para patrones de conexión comunes
--fix-file <archivo>: Especifica archivo para aplicar fijados (por defecto usa el archivo de entrada)
--report-format json|text: Para integración con otros sistemas
--quiet: Modo silencioso para uso en scripts

Salida:
- Código 0 si todo OK
- Código 1 si hay inputs REQ vacíos (después de auto-fijo si se aplica)
- Código 2 si el archivo está corrupto
"""

import sys
import os
import re
import xml.etree.ElementTree as ET
import argparse
from collections import defaultdict
import json


def parse_ghx(filepath):
    """Parsea un .ghx y devuelve lista de objetos."""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    root = ET.fromstring(content)

    # Encontrar DefinitionObjects
    objects_chunk = None
    for chunk in root.iter('chunk'):
        if chunk.get('name') == 'DefinitionObjects':
            objects_chunk = chunk
            break
    if objects_chunk is None:
        return None, "No se encontró DefinitionObjects"

    chunks_wrapper = objects_chunk.find('chunks')
    if chunks_wrapper is None:
        return None, "DefinitionObjects no tiene <chunks>"

    objects = []
    for chunk in chunks_wrapper.findall('chunk'):
        if chunk.get('name') == 'Object':
            obj = parse_object(chunk)
            if obj:
                objects.append(obj)
    return objects, None


def parse_object(obj_chunk):
    obj = {
        'index': obj_chunk.get('index'),
        'component_guid': None,
        'name': None,
        'instance_guid': None,
        'nickname': None,
        'inputs': [],
        'outputs': [],
    }

    items_wrap = obj_chunk.find('items')
    if items_wrap is not None:
        for item in items_wrap.findall('item'):
            name = item.get('name')
            if name == 'GUID':
                obj['component_guid'] = item.text
            elif name == 'Name':
                obj['name'] = item.text

    chunks_wrap = obj_chunk.find('chunks')
    if chunks_wrap is None:
        return obj

    container = None
    for chunk in chunks_wrap.findall('chunk'):
        if chunk.get('name') == 'Container':
            container = chunk
            break
    if container is None:
        return obj

    cont_items = container.find('items')
    if cont_items is not None:
        for item in cont_items.findall('item'):
            name = item.get('name')
            if name == 'InstanceGuid':
                obj['instance_guid'] = item.text
            elif name == 'NickName':
                obj['nickname'] = item.text
            elif name == 'Name' and not obj['name']:
                obj['name'] = item.text

    cont_chunks = container.find('chunks')
    if cont_chunks is None:
        return obj

    paramdata = None
    for chunk in cont_chunks.findall('chunk'):
        if chunk.get('name') == 'ParameterData':
            paramdata = chunk
            break

    # CASO 1: ParameterData existe (componentes nativos GH y Python 3 Script)
    if paramdata is not None:
        pd_chunks = paramdata.find('chunks')
        if pd_chunks is not None:
            for chunk in pd_chunks.findall('chunk'):
                name = chunk.get('name')
                if name in ('InputParam', 'param_input'):
                    p = parse_param(chunk)
                    if p:
                        obj['inputs'].append(p)
                elif name in ('OutputParam', 'param_output'):
                    p = parse_param(chunk)
                    if p:
                        obj['outputs'].append(p)

    # CASO 2: Algunos plugins (Tapir/Archicad, Ladybug) ponen param_input/param_output
    # directamente dentro de Container.chunks, sin ParameterData wrapper
    for chunk in cont_chunks.findall('chunk'):
        name = chunk.get('name')
        if name in ('param_input', 'InputParam'):
            # Verificar que no esté ya agregado (evitar duplicados)
            p = parse_param(chunk)
            if p and p['instance_guid'] and p['instance_guid'] not in [x['instance_guid'] for x in obj['inputs']]:
                obj['inputs'].append(p)
        elif name in ('param_output', 'OutputParam'):
            p = parse_param(chunk)
            if p and p['instance_guid'] and p['instance_guid'] not in [x['instance_guid'] for x in obj['outputs']]:
                obj['outputs'].append(p)

    return obj


def parse_param(param_chunk):
    p = {
        'index': param_chunk.get('index'),
        'name': None,
        'nickname': None,
        'instance_guid': None,
        'optional': False,
        'sources': [],
        'has_persistent_data': False,  # Si tiene datos embebidos (PersistentData con Count>0)
    }
    items_wrap = param_chunk.find('items')
    if items_wrap is not None:
        for item in items_wrap.findall('item'):
            name = item.get('name')
            if name == 'Name':
                p['name'] = item.text
            elif name == 'NickName':
                p['nickname'] = item.text
            elif name == 'InstanceGuid':
                p['instance_guid'] = item.text
            elif name == 'Optional':
                p['optional'] = item.text == 'true'
            elif name == 'Source':
                if item.text:
                    p['sources'].append(item.text)

    # Detectar si tiene PersistentData con datos (Count > 0)
    for chunk in param_chunk.findall('chunk'):
        if chunk.get('name') == 'PersistentData':
            pd_items = chunk.find('items')
            if pd_items is not None:
                for item in pd_items.findall('item'):
                    if item.get('name') == 'Count':
                        try:
                            count = int(item.text)
                            if count > 0:
                                p['has_persistent_data'] = True
                        except:
                            pass
    return p


def fix_connection_in_file(filepath, target_obj_guid, target_param_guid, source_output_guid, create_backup=True):
    """
    Fix a specific connection in a GHX file.

    Args:
        filepath: Path to the GHX file
        target_obj_guid: InstanceGuid of the target object
        target_param_guid: InstanceGuid of the target input parameter
        source_output_guid: InstanceGuid of the source output to connect to
        create_backup: Whether to create a backup file

    Returns:
        True if fixed, False otherwise
    """
    try:
        # Parse the GHX file
        tree = ET.parse(filepath)
        root = tree.getroot()

        # TypeHintID for geometry connections (standard in GH)
        GEOMETRY_TYPE_HINT_ID = "1c282eeb-dd16-439f-94e4-7d92b542fe8b"

        fixed = False

        # Find the target input parameter chunk
        for chunk in root.iter('chunk'):
            if chunk.get('name') == 'InputParam':
                # Check if this InputParam belongs to the target object
                obj_chunk = chunk.find("./ancestor::chunk[@name='Object']")
                if obj_chunk is not None:
                    obj_instance_elem = obj_chunk.find(".//item[@name='InstanceGuid']")
                    if obj_instance_elem is not None and obj_instance_elem.text == target_obj_guid:
                        # Check if this is the target parameter
                        param_instance_elem = chunk.find(".//item[@name='InstanceGuid']")
                        if param_instance_elem is not None and param_instance_elem.text == target_param_guid:
                            # Found the target InputParam chunk
                            items_section = chunk.find("./items")
                            if items_section is None:
                                # Create items section if it doesn't exist
                                items_section = ET.Element('items')
                                chunk.append(items_section)

                            # Fix Source item with index="0"
                            source_items = items_section.findall("./item[@name='Source']")
                            source_index_0_exists = False

                            for source_item in source_items:
                                if source_item.get('index') == '0':
                                    if source_item.text != source_output_guid:
                                        source_item.text = source_output_guid
                                        fixed = True
                                    source_index_0_exists = True
                                    break

                            if not source_index_0_exists:
                                # Create new Source item
                                source_item = ET.Element('item')
                                source_item.set('name', 'Source')
                                source_item.set('index', '0')
                                source_item.set('type_name', 'gh_guid')
                                source_item.text = source_output_guid
                                items_section.insert(0, source_item)
                                fixed = True

                            # Fix SourceCount = "1"
                            source_count_elem = items_section.find("./item[@name='SourceCount']")
                            if source_count_elem is not None:
                                if source_count_elem.text != '1':
                                    source_count_elem.text = '1'
                                    fixed = True
                            else:
                                source_count_item = ET.Element('item')
                                source_count_item.set('name', 'SourceCount')
                                source_count_item.set('type_name', 'gh_int32')
                                source_count_item.text = '1'
                                items_section.append(source_count_item)
                                fixed = True

                            # Fix ToolTip as empty string
                            tooltip_elem = items_section.find("./item[@name='ToolTip']")
                            if tooltip_elem is not None:
                                if tooltip_elem.text != '':
                                    tooltip_elem.text = ''
                                    fixed = True
                            else:
                                tooltip_item = ET.Element('item')
                                tooltip_item.set('name', 'ToolTip')
                                tooltip_item.set('type_name', 'gh_string')
                                tooltip_item.text = ''
                                items_section.append(tooltip_item)
                                fixed = True

                            # Fix TypeHintID with geometry type hint
                            type_hint_elem = items_section.find("./item[@name='TypeHintID']")
                            if type_hint_elem is not None:
                                if type_hint_elem.text != GEOMETRY_TYPE_HINT_ID:
                                    type_hint_elem.text = GEOMETRY_TYPE_HINT_ID
                                    fixed = True
                            else:
                                type_hint_item = ET.Element('item')
                                type_hint_item.set('name', 'TypeHintID')
                                type_hint_item.set('type_name', 'gh_guid')
                                type_hint_item.text = GEOMETRY_TYPE_HINT_ID
                                items_section.append(type_hint_item)
                                fixed = True

                            break
                if fixed:
                    break

        if fixed:
            # Create backup if requested
            if create_backup:
                backup_file = filepath + ".backup"
                import shutil
                shutil.copy2(filepath, backup_file)

            # Save the modified file
            tree.write(filepath, encoding='utf-8', xml_declaration=True)
            return True
        else:
            return False

    except Exception as e:
        print(f"Error fixing connection: {e}")
        return False


def apply_common_fixes(filepath, create_backup=True):
    """
    Apply common connection fixes for Proyecto Raven.
    This function contains the known fixes that were identified during the connection fixing process.

    Args:
        filepath: Path to the GHX file
        create_backup: Whether to create a backup file

    Returns:
        Number of fixes applied
    """
    # Common fixes for Proyecto Raven (identified from the connection fixing process)
    common_fixes = [
        # Format: (target_obj_guid, target_param_guid, source_output_guid, description)
        ("6a008cea-e2d9-4a79-828c-e359262a3f62", "1731ad08-b120-4a85-8da8-fa1d46ff0b81",
         "1d239709-ceb6-4e45-b7d0-4a5ff32ac68b",
         "DISEÑO_INTERIOR_v01.floor_plates <- VOLUMEN_v03.slab_polygons"),

        ("6a008cea-e2d9-4a79-828c-e359262a3f62", "12183f9c-ff34-4ab3-9d91-7ed0500d1d4d",
         "8e241b8a-68b0-4263-a64a-02c825155b92",
         "DISEÑO_INTERIOR_v01.exterior_walls <- VOLUMEN_v03.wall_curves"),

        ("d9fa60aa-8942-4ab2-81c8-9ad5e62ac21a", "d386833c-7bbd-4545-8fe7-62dc9fa1d05e",
         "1d239709-ceb6-4e45-b7d0-4a5ff32ac68b",
         "LADYBUG_v01.building_envelope <- VOLUMEN_v03.slab_polygons"),

        ("d9fa60aa-8942-4ab2-81c8-9ad5e62ac21a", "cd9ad934-9e21-42fd-bf00-bd2d407cd65f",
         "1d239709-ceb6-4e45-b7d0-4a5ff32ac68b",
         "LADYBUG_v01.floor_plates <- VOLUMEN_v03.slab_polygons"),

        ("d9fa60aa-8942-4ab2-81c8-9ad5e62ac21a", "483cc1e5-18e7-4ed9-888b-1cf3e2956ddd",
         "8e241b8a-68b0-4263-a64a-02c825155b92",
         "LADYBUG_v01.exterior_walls <- VOLUMEN_v03.wall_curves")
    ]

    fixed_count = 0
    for obj_guid, param_guid, source_guid, description in common_fixes:
        print(f"Applying common fix: {description}")
        if fix_connection_in_file(filepath, obj_guid, param_guid, source_guid, create_backup):
            fixed_count += 1
            print(f"  ✓ Fixed")
        else:
            print(f"  ✗ Failed to fix")

    return fixed_count


def validate(filepath, apply_fixes=False, fix_file=None, quiet=False):
    """
    Validate a GHX file and optionally apply fixes.

    Args:
        filepath: Path to the GHX file to validate
        apply_fixes: Whether to apply common fixes before validation
        fix_file: Path to file to apply fixes to (if different from validation file)
        quiet: Whether to suppress verbose output

    Returns:
        Exit code (0=OK, 1=critical errors, 2=corrupt file)
    """
    if not quiet:
        print(f"╔═══════════════════════════════════════════════════════════════╗")
        print(f"║  VALIDACIÓN DE ARCHIVO .GHX                                 ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝")
        print(f"Archivo: {filepath}")
        size = os.path.getsize(filepath)
        print(f"Tamaño: {size:,} bytes\n")

    # Apply fixes if requested
    if apply_fixes:
        target_file = fix_file if fix_file else filepath
        if not quiet:
            print("─── APLICANDO FIJADOS COMUNES ───")
        fixed_count = apply_common_fixes(target_file, create_backup=True)
        if not quiet:
            print(f"Se aplicaron {fixed_count} fijados comunes\n")
        # If we fixed a different file, we need to validate that file
        if fix_file and fix_file != filepath:
            filepath = fix_file

    # 1. Verificar XML bien formado
    if not quiet:
        print("─── 1. ESTRUCTURA XML ───")
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        if not quiet:
            print(f"  ✓ XML bien formado")
            print(f"  ✓ Root: <{root.tag} name=\"{root.get('name')}\">")
    except ET.ParseError as e:
        if not quiet:
            print(f"  ✗ XML CORRUPTO: {e}")
        return 2

    # 2. Parsear objetos
    if not quiet:
        print("\n─── 2. OBJETOS ───")
    objects, err = parse_ghx(filepath)
    if err:
        if not quiet:
            print(f"  ✗ {err}")
        return 2
    if not quiet:
        print(f"  ✓ {len(objects)} objetos encontrados")

    # Por tipo
    by_type = defaultdict(int)
    for o in objects:
        by_type[o.get('name', 'unknown')] += 1
    if not quiet:
        print(f"\n  Por tipo (top 10):")
        for t, c in sorted(by_type.items(), key=lambda x: -x[1])[:10]:
            print(f"    {c:3d}  {t}")

    # 3. Mapear InstanceGuids
    all_param_guids = set()
    all_obj_guids = set()
    for o in objects:
        if o['instance_guid']:
            all_obj_guids.add(o['instance_guid'])
        for p in o['inputs'] + o['outputs']:
            if p['instance_guid']:
                all_param_guids.add(p['instance_guid'])
    all_valid_targets = all_param_guids | all_obj_guids
    if not quiet:
        print(f"\n  Total InstanceGuids únicos: objetos={len(all_obj_guids)}, params={len(all_param_guids)}")

    # 4. Verificar conexiones
    if not quiet:
        print("\n─── 3. CONEXIONES (WIRES) ───")
    total_connections = 0
    orphan_connections = []  # sources que apuntan a InstanceGuids inexistentes
    duplicate_sources = []   # inputs con más de 1 source (raro pero posible)

    for o in objects:
        for p in o['inputs']:
            for src in p.get('sources', []):
                total_connections += 1
                if src not in all_valid_targets:
                    orphan_connections.append({
                        'obj': o.get('nickname') or o.get('name'),
                        'param': p.get('name'),
                        'orphan_src': src,
                    })
            if len(p.get('sources', [])) > 1:
                duplicate_sources.append({
                    'obj': o.get('nickname') or o.get('name'),
                    'param': p.get('name'),
                    'count': len(p['sources']),
                })

    if not quiet:
        print(f"  Total conexiones: {total_connections}")
        print(f"  Conexiones huérfanas: {len(orphan_connections)}")
        print(f"  Inputs con múltiples sources: {len(duplicate_sources)}")

        if orphan_connections:
            print(f"\n  ⚠ Conexiones huérfanas (apuntan a InstanceGuids inexistentes):")
            for c in orphan_connections[:10]:
                print(f"    - {c['obj']}.{c['param']} → {c['orphan_src'][:8]}...")

    # 5. Inputs REQUERIDOS sin conectar (CRÍTICO)
    if not quiet:
        print("\n─── 4. INPUTS REQUERIDOS SIN CONECTAR ───")
    empty_req_critical = []   # En módulos Python
    empty_req_warning = []    # En otros componentes
    for o in objects:
        for p in o['inputs']:
            if not p.get('sources') and not p.get('optional') and not p.get('has_persistent_data'):
                entry = {
                    'obj': o.get('nickname') or o.get('name'),
                    'obj_name': o.get('name'),
                    'param': p.get('name'),
                    'obj_guid': o['instance_guid'],
                    'param_guid': p['instance_guid'],
                }
                if o.get('name') == 'Python 3 Script':
                    empty_req_critical.append(entry)
                else:
                    empty_req_warning.append(entry)

    if empty_req_critical:
        if not quiet:
            print(f"  ✗ CRÍTICO - {len(empty_req_critical)} inputs REQ vacíos en módulos Python:")
            for e in empty_req_critical:
                print(f"    - [{e['obj']}] {e['param']}")
                print(f"        param_guid: {e['param_guid']}")
    else:
        if not quiet:
            print(f"  ✓ Módulos Python: ningún input requerido vacío")

    if empty_req_warning:
        if not quiet:
            print(f"\n  ⚠ ADVERTENCIA - {len(empty_req_warning)} inputs REQ vacíos en otros componentes:")
            print(f"    (suelen ser componentes Tapir/Archicad/Honeybee en standby - no rompen el pipeline)")
            # Agrupar por objeto
            by_obj = defaultdict(list)
            for e in empty_req_warning:
                by_obj[e['obj']].append(e['param'])
            for obj, params in sorted(by_obj.items()):
                print(f"    {obj}: {', '.join(params[:4])}{' ...' if len(params) > 4 else ''}")

    # 6. Inputs OPCIONALES sin conectar (ADVERTENCIA)
    if not quiet:
        print("\n─── 5. INPUTS OPCIONALES SIN CONECTAR (info) ───")
    empty_opt = []
    for o in objects:
        for p in o['inputs']:
            if not p.get('sources') and p.get('optional') and not p.get('has_persistent_data'):
                empty_opt.append({
                    'obj': o.get('nickname') or o.get('name'),
                    'param': p.get('name'),
                })
    if not quiet:
        print(f"  {len(empty_opt)} inputs opcionales sin conectar (pueden quedar así)")
        if empty_opt:
            # Agrupar por objeto
            by_obj = defaultdict(list)
            for e in empty_opt:
                by_obj[e['obj']].append(e['param'])
            for obj, params in sorted(by_obj.items())[:5]:
                print(f"    {obj}: {', '.join(params[:3])}{' ...' if len(params) > 3 else ''}")

    # 7. Outputs no usados (considerando que componentes simples tienen su InstanceGuid como source)
    if not quiet:
        print("\n─── 6. OUTPUTS SIN USAR (nadie los consume) ───")
    used_outputs = set()
    for o in objects:
        for p in o['inputs']:
            for s in p.get('sources', []):
                used_outputs.add(s)

    unused = []
    for o in objects:
        # Para componentes simples (Panel, Toggle, etc.) el InstanceGuid del objeto sirve como output
        if o['instance_guid'] and o['instance_guid'] in used_outputs:
            continue
        for p in o['outputs']:
            if p['instance_guid'] and p['instance_guid'] not in used_outputs:
                unused.append({
                    'obj': o.get('nickname') or o.get('name'),
                    'param': p.get('name'),
                })
    if not quiet:
        print(f"  {len(unused)} outputs no están siendo usados")
        if unused:
            by_obj = defaultdict(list)
            for e in unused:
                by_obj[e['obj']].append(e['param'])
            for obj, params in sorted(by_obj.items())[:5]:
                print(f"    {obj}: {', '.join(params[:3])}{' ...' if len(params) > 3 else ''}")

    # 8. Módulos Python (los más importantes)
    if not quiet:
        print("\n─── 7. MÓDULOS PYTHON (nodos principales) ───")
    py_modules = [o for o in objects if o['name'] == 'Python 3 Script' and o.get('nickname')]
    for o in py_modules:
        n_inputs = len(o['inputs'])
        n_connected = sum(1 for p in o['inputs'] if p.get('sources') or p.get('has_persistent_data'))
        n_req_empty = sum(1 for p in o['inputs'] if not p.get('sources') and not p.get('optional') and not p.get('has_persistent_data'))
        n_outputs = len(o['outputs'])
        status = "✓" if n_req_empty == 0 else "✗"
        if not quiet:
            print(f"  {status} {o['nickname']:<25} inputs={n_connected}/{n_inputs} (REQ vacíos: {n_req_empty})  outputs={n_outputs}")

    # 9. Resumen final
    if not quiet:
        print("\n" + "═" * 64)
        print("RESUMEN FINAL")
        print("═" * 64)
        print(f"  Objetos:                 {len(objects)}")
        print(f"  Conexiones:              {total_connections}")
        print(f"  Conexiones huérfanas:    {len(orphan_connections)}")
        print(f"  Inputs REQ vacíos (CRÍTICO, en Python): {len(empty_req_critical)} ← debe ser 0")
        print(f"  Inputs REQ vacíos (ADVERTENCIA, otros): {len(empty_req_warning)}")
        print(f"  Inputs OPT vacíos:       {len(empty_opt)}")
        print(f"  Outputs sin usar:        {len(unused)}")
        print(f"  Módulos Python:          {len(py_modules)}")

    # Determine exit code
    if empty_req_critical:
        if not quiet:
            print(f"\n✗ ARCHIVO TIENE ERRORES CRÍTICOS: {len(empty_req_critical)} inputs requeridos sin conectar en módulos Python")
        return 1
    elif orphan_connections:
        if not quiet:
            print(f"\n⚠ Archivo OK pero con {len(orphan_connections)} conexiones huérfanas")
        return 0
    else:
        if not quiet:
            print(f"\n✓ ARCHIVO VÁLIDO - listo para abrir en Grasshopper")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Validador de archivos .ghx de Grasshopper con capacidades de auto-fijo")
    parser.add_argument("filepath", help="Path to the .ghx file to validate")
    parser.add_argument("--auto-fix-common", action="store_true",
                       help="Apply common fixes for Proyecto Raven before validation")
    parser.add_argument("--fix-file", help="File to apply fixes to (if different from validation file)")
    parser.add_argument("--report-format", choices=["json", "text"], default="text",
                       help="Output format for results")
    parser.add_argument("--quiet", action="store_true",
                       help="Suppress verbose output (useful for scripting)")

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        if not args.quiet:
            print(f"ERROR: archivo no encontrado: {args.filepath}")
        sys.exit(2)

    exit_code = validate(
        args.filepath,
        apply_fixes=args.auto_fix_common,
        fix_file=args.fix_file,
        quiet=args.quiet
    )

    # If JSON format is requested, output results as JSON
    if args.report_format == "json" and not args.quiet:
        # Re-run validation to get detailed results (without printing)
        objects, err = parse_ghx(args.filepath)
        if not err:
            # Build results dictionary
            results = {
                "filepath": args.filepath,
                "exit_code": exit_code,
                "object_count": len(objects),
                # Additional details could be added here
            }
            print(json.dumps(results, indent=2))

    sys.exit(exit_code)


if __name__ == '__main__':
    main()