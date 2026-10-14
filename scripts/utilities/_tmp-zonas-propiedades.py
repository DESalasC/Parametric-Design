# -*- coding: utf-8 -*-
"""_tmp-zonas-propiedades.py — Diagnostico (SOLO LECTURA): propiedades de las Zones del proyecto AC abierto.

Flujo: nombres built-in -> GetPropertyIds (guid) -> GetPropertyValuesOfElements.
Lee para cada Zone: nombre, numero, categoria, capa, area calculada y perímetro.

Uso: .venv\\Scripts\\python.exe scripts\\utilities\\_tmp-zonas-propiedades.py
"""
import sys

from archicad import ACConnection

PROPS = [
    'Zone_ZoneName',
    'Zone_ZoneNumber',
    'Zone_ZoneCategoryCode',
    'IdAndCategories_ZoneStampName',
    'ModelView_LayerName',
    'Zone_CalculatedArea',
    'Zone_NetArea',
    'Zone_Perimeter',
]


def _d(x):
    try:
        return x.to_dict()
    except Exception:
        return x if isinstance(x, dict) else {'repr': repr(x)}


def main():
    conn = ACConnection.connect(None)
    T = conn.types

    zones = conn.commands.GetElementsByType('Zone')
    print('Zones: {}'.format(len(zones)))

    user_ids = [T.PropertyUserId(type='BuiltIn', nonLocalizedName=p) for p in PROPS]
    ids = conn.commands.GetPropertyIds(user_ids)
    kept = []
    prop_items = []
    for nm, item in zip(PROPS, ids):
        d = _d(item)
        pid = d.get('propertyId') or {}
        guid = pid.get('guid')
        if guid:
            kept.append(nm)
            prop_items.append(T.PropertyIdArrayItem(propertyId=T.PropertyId(guid=guid)))
        else:
            print('prop no disponible: {} -> {}'.format(nm, d))

    vals = conn.commands.GetPropertyValuesOfElements(zones, prop_items)
    print('=' * 120)
    for k, item in enumerate(vals):
        d = _d(item)
        if 'error' in d and d['error']:
            print('Z{:02d}: ERROR {}'.format(k, d['error']))
            continue
        row = []
        for nm, pv in zip(kept, d.get('propertyValues', [])):
            pvd = _d(pv)
            v = pvd.get('propertyValue') or {}
            val = v.get('displayValue', v.get('value'))
            row.append('{}={}'.format(nm.replace('Zone_', '').replace('ModelView_', ''), val))
        print('Z{:02d} | {}'.format(k, ' | '.join(row)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
