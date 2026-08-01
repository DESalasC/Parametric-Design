#!/usr/bin/env python3
"""
Mapeo GuBIMclass v1.2 ES → Uniclass 2015
Para vincular elementos ArchiCAD a base de costos via Classification System
"""

import pandas as pd
import json

GUBIMCLASS_CLEAN = r"C:\Users\Dario Salas\proyectos\2-Entradas\Plantillas_ArchiCAD\GuBIMclass_v12_ES_clean.csv"
OUTPUT_MAPPING = r"C:\Users\Dario Salas\proyectos\2-Entradas\Plantillas_ArchiCAD\GuBIMclass_to_Uniclass2015_mapping.csv"
OUTPUT_JSON = r"C:\Users\Dario Salas\proyectos\2-Entradas\Plantillas_ArchiCAD\GuBIMclass_to_Uniclass2015_mapping.json"

# Uniclass 2015 Tablas principales
# Pr_Products (products), Ss_Systems (systems), EF_Elements (elements),
# Co_Complexes (complexes), Ac_Activities (activities), PM_ProjectManagement

# Mapeo manual GuBIMclass (principales grupos) → Uniclass 2015
UNICLASS_MAPPING = {
    # 00 - Trabajos previos y replanteo
    "00": {
        "uniclass_table": "Ac_Activities",
        "uniclass_code": "Ac_10",
        "uniclass_name": "Pre-construction activities"
    },
    "00.10": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_10_20", "uniclass_name": "Setting out"},
    "00.20": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_10_30", "uniclass_name": "Existing conditions surveys"},
    "00.30": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_10_40", "uniclass_name": "Testing and investigation"},

    # 10 - Actuaciones provisionales y movimiento de tierras
    "10": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_20", "uniclass_name": "Temporary works and earthworks"},
    "10.10": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_20_10", "uniclass_name": "Temporary works"},
    "10.20": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_20_20", "uniclass_name": "Earthworks"},
    "10.30": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_20_30", "uniclass_name": "Groundwater control"},

    # 20 - Sistema estructural
    "20": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20", "uniclass_name": "Structural frame"},
    "20.10": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_10", "uniclass_name": "Substructure"},
    "20.10.10": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_10_10", "uniclass_name": "Foundations"},
    "20.10.20": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_10_20", "uniclass_name": "Deep foundations"},
    "20.10.30": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_10_30", "uniclass_name": "Earth retaining structures"},
    "20.10.40": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_10_40", "uniclass_name": "Basement structure"},
    "20.20": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_20", "uniclass_name": "Superstructure"},
    "20.20.10": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_20_10", "uniclass_name": "Columns and walls"},
    "20.20.20": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_20_20", "uniclass_name": "Floors and roofs structure"},
    "20.20.30": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_20_20_30", "uniclass_name": "3D structural systems"},

    # 30 - Envolvente y acabados exteriores
    "30": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_30", "uniclass_name": "External envelope"},
    "30.10": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_30_10", "uniclass_name": "External walls"},
    "30.10.10": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_30", "uniclass_name": "Wall systems"},
    "30.10.20": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_70", "uniclass_name": "Windows and external doors"},
    "30.20": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_30_20", "uniclass_name": "Roofs"},
    "30.20.10": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_50", "uniclass_name": "Roof systems"},
    "30.20.20": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_70", "uniclass_name": "Roof lights and openings"},
    "30.30": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_30_30", "uniclass_name": "External horizontal enclosures"},
    "30.40": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_30_40", "uniclass_name": "External stairs and ramps"},

    # 40 - Compartimentación y acabados interiores
    "40": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_40", "uniclass_name": "Internal elements and finishes"},
    "40.10": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_40_10", "uniclass_name": "Internal walls and partitions"},
    "40.10.10": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_40", "uniclass_name": "Partition systems"},
    "40.10.20": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_90", "uniclass_name": "Wall finishes"},
    "40.20": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_40_20", "uniclass_name": "Internal floors and ceilings"},
    "40.20.10": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_25_10", "uniclass_name": "Ceiling systems"},
    "40.20.20": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_25_30", "uniclass_name": "Floor finishes"},
    "40.30": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_40_30", "uniclass_name": "Internal stairs and ramps"},
    "40.40": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_40_90", "uniclass_name": "Signage"},

    # 50 - Instalaciones
    "50": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25", "uniclass_name": "Building services systems"},
    "50.10": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_30", "uniclass_name": "Plumbing systems"},
    "50.20": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_40", "uniclass_name": "Drainage systems"},
    "50.30": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_50", "uniclass_name": "HVAC systems"},
    "50.40": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_60", "uniclass_name": "Fuel systems"},
    "50.50": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_70", "uniclass_name": "Fire protection systems"},
    "50.60": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_80", "uniclass_name": "Electrical systems"},
    "50.70": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_90", "uniclass_name": "Communications systems"},
    "50.80": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_90_10", "uniclass_name": "Security systems"},
    "50.90": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_50", "uniclass_name": "Specialist systems"},
    "50.100": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_25_95", "uniclass_name": "Common services elements"},

    # 60 - Equipamiento y mobiliario
    "60": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_40", "uniclass_name": "Furniture and equipment"},
    "60.10": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_40_30", "uniclass_name": "Sanitary appliances"},
    "60.20": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_40_40", "uniclass_name": "Fixed and movable furniture"},
    "60.30": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_30_50", "uniclass_name": "Transport systems"},

    # 70 - Urbanización
    "70": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_70", "uniclass_name": "External works"},
    "70.10": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_70_10", "uniclass_name": "External structures"},
    "70.20": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_20_80", "uniclass_name": "Boundary protection"},
    "70.30": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_70_30", "uniclass_name": "Paving and surfacing"},
    "70.40": {"uniclass_table": "Ss_Systems", "uniclass_code": "Ss_30_20", "uniclass_name": "External lighting and drainage"},
    "70.50": {"uniclass_table": "EF_Elements", "uniclass_code": "EF_70_50", "uniclass_name": "Planting and landscaping"},
    "70.60": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_40_50", "uniclass_name": "Street furniture"},

    # 80 - Implantación de obra
    "80": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_30", "uniclass_name": "Construction site setup"},
    "80.10": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_30_10", "uniclass_name": "Site accommodation and access"},
    "80.20": {"uniclass_table": "Ac_Activities", "uniclass_code": "Ac_30_20", "uniclass_name": "Temporary works for construction"},
    "80.30": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_65", "uniclass_name": "Construction machinery"},
    "80.40": {"uniclass_table": "Pr_Products", "uniclass_code": "Pr_80_30", "uniclass_name": "Health and safety equipment"},
}

def find_best_match(code, mapping):
    """Encontrar el mejor match en el mapeo (más específico primero)"""
    # Buscar código exacto
    if code in mapping:
        return mapping[code]

    # Buscar por prefijo (padre más cercano)
    parts = code.split('.')
    for i in range(len(parts), 0, -1):
        prefix = '.'.join(parts[:i])
        if prefix in mapping:
            return mapping[prefix]

    return None

def main():
    df = pd.read_csv(GUBIMCLASS_CLEAN, encoding='utf-8')
    print(f"Cargados {len(df)} códigos GuBIMclass")

    mapping_rows = []
    unmapped = []

    for _, row in df.iterrows():
        code = row['code']
        name = row['name']
        level = int(row['level'])
        parent = row['parent']

        match = find_best_match(code, UNICLASS_MAPPING)

        if match:
            mapping_rows.append({
                'gubimclass_code': code,
                'gubimclass_name': name,
                'gubimclass_level': level,
                'gubimclass_parent': parent,
                'uniclass_table': match['uniclass_table'],
                'uniclass_code': match['uniclass_code'],
                'uniclass_name': match['uniclass_name'],
                'match_type': 'exact' if code in UNICLASS_MAPPING else 'parent_inherited'
            })
        else:
            # Sin mapeo encontrado - heredar del padre si existe
            parent_match = None
            if parent:
                parent_match = find_best_match(parent, UNICLASS_MAPPING)

            if parent_match:
                mapping_rows.append({
                    'gubimclass_code': code,
                    'gubimclass_name': name,
                    'gubimclass_level': level,
                    'gubimclass_parent': parent,
                    'uniclass_table': parent_match['uniclass_table'],
                    'uniclass_code': parent_match['uniclass_code'],
                    'uniclass_name': parent_match['uniclass_name'] + " (heredado)",
                    'match_type': 'parent_inherited'
                })
            else:
                unmapped.append({'code': code, 'name': name, 'level': level, 'parent': parent})
                mapping_rows.append({
                    'gubimclass_code': code,
                    'gubimclass_name': name,
                    'gubimclass_level': level,
                    'gubimclass_parent': parent,
                    'uniclass_table': 'UNMAPPED',
                    'uniclass_code': '',
                    'uniclass_name': 'SIN MAPEO - REVISAR MANUALMENTE',
                    'match_type': 'unmapped'
                })

    # Exportar CSV
    mapping_df = pd.DataFrame(mapping_rows)
    mapping_df.to_csv(OUTPUT_MAPPING, index=False, encoding='utf-8')
    print(f"\nMapeo exportado: {OUTPUT_MAPPING} ({len(mapping_df)} filas)")

    # Exportar JSON para uso en GH Python
    mapping_dict = {}
    for _, m in mapping_df.iterrows():
        mapping_dict[m['gubimclass_code']] = {
            'gubimclass_name': m['gubimclass_name'],
            'uniclass_table': m['uniclass_table'],
            'uniclass_code': m['uniclass_code'],
            'uniclass_name': m['uniclass_name'],
            'match_type': m['match_type']
        }

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(mapping_dict, f, ensure_ascii=False, indent=2)
    print(f"JSON exportado: {OUTPUT_JSON}")

    # Estadísticas
    print(f"\n--- ESTADÍSTICAS MAPEO ---")
    print(f"  Total: {len(mapping_df)}")
    print(f"  Exactos: {len(mapping_df[mapping_df['match_type'] == 'exact'])}")
    print(f"  Heredados: {len(mapping_df[mapping_df['match_type'] == 'parent_inherited'])}")
    print(f"  Sin mapear: {len(mapping_df[mapping_df['match_type'] == 'unmapped'])}")

    if unmapped:
        print(f"\n--- SIN MAPEAR (requieren revisión) ---")
        for u in unmapped:
            print(f"  [{u['level']}] {u['code']}: {u['name']} (parent: {u['parent']})")

    # Mostrar mapeos clave para arquitectura
    print(f"\n--- MAPEOS CLAVE ARQUITECTURA ---")
    key_codes = ['20.10.10', '20.10.20', '20.10.30', '20.20.10', '20.20.20',
                 '30.10.10', '30.10.20', '30.20.10', '30.20.20',
                 '40.10.10', '40.10.20', '40.20.10', '40.20.20',
                 '50.10', '50.20', '50.30', '50.50', '50.60']
    for kc in key_codes:
        match = find_best_match(kc, UNICLASS_MAPPING)
        if match:
            print(f"  {kc} -> {match['uniclass_table']}.{match['uniclass_code']} ({match['uniclass_name']})")

if __name__ == "__main__":
    main()