"""
================================================================================
F3_PROGRAMA_AREAS_v01.py — Generador de Programa y Matriz de Adyacencias
Proyecto: DisenoParametrico / Fase 3
Python 3.12 Standalone
================================================================================

OBJETIVO:
  Tomar el GFA máximo y un mix de usos (definido por F2 o por el operario) y
  estructurar el programa de áreas por piso, definiendo la matriz de
  adyacencias para el generador de masa en Grasshopper.

USO:
  python src/fase-3-masa/F3_PROGRAMA_AREAS_v01.py --gfa 1053 --pisos 5 --mix 0.1,0.1,0.8

SALIDA:
  data/fase-3-masa/programa-areas.json
================================================================================
"""

import argparse
import json
import os
from typing import Dict, Any, List

# Matriz de adyacencias base (Architect Skills: spatial-planning)
MATRIZ_ADYACENCIA = {
    "Comercio": {"Comercio": 1, "Salud": 1, "Vivienda": -1, "Nucleo": 0, "Servicios": 0},
    "Salud": {"Comercio": 1, "Salud": 1, "Vivienda": 0, "Nucleo": 1, "Servicios": 1},
    "Vivienda": {"Comercio": -1, "Salud": 0, "Vivienda": 1, "Nucleo": 1, "Servicios": -1},
    "Nucleo": {"Comercio": 0, "Salud": 1, "Vivienda": 1, "Nucleo": 1, "Servicios": 1},
    "Servicios": {"Comercio": 0, "Salud": 1, "Vivienda": -1, "Nucleo": 1, "Servicios": 1}
}

# Eficiencias típicas (NTG Ratio) por uso
EFICIENCIAS = {
    "Comercio": 0.85, # Poco muro divisor,-open plan
    "Salud": 0.75,    # Consultorios requieren circulaciones internas
    "Vivienda": 0.75, # Circulación interna, muros, patios
    "Nucleo": 1.0,    # Área bruta = área neta
    "Servicios": 0.90 # Cuartos técnicos
}

def distribuir_usos(gfa: float, pisos: int, mix_str: str) -> Dict[str, Any]:
    """
    Distribuye el GFA en pisos y usos.
    mix_str: "comercio,salud,vivienda" en porcentajes (0.1, 0.1, 0.8)
    """
    try:
        m_com, m_sal, m_viv = [float(x) for x in mix_str.split(",")]
    except:
        m_com, m_sal, m_viv = 0.1, 0.1, 0.8

    area_por_piso = gfa / pisos
    
    programa = []
    
    # PISO 1: Comercio + Salud + Núcleo
    p1_com = area_por_piso * m_com
    p1_sal = area_por_piso * m_sal
    p1_nuc = area_por_piso * 0.10 # 10% siempre para núcleo
    
    # PISO 2 a N-1: Vivienda + Salud (si hay) + Núcleo
    # PISO N: Vivienda + Servicios (azotea) + Núcleo
    
    for i in range(1, pisos + 1):
        if i == 1:
            usos = [
                {"uso": "Comercio", "area_bruta": round(p1_com, 2), "area_neta": round(p1_com * EFICIENCIAS["Comercio"], 2)},
                {"uso": "Salud", "area_bruta": round(p1_sal, 2), "area_neta": round(p1_sal * EFICIENCIAS["Salud"], 2)},
                {"uso": "Nucleo", "area_bruta": round(p1_nuc, 2), "area_neta": round(p1_nuc * EFICIENCIAS["Nucleo"], 2)}
            ]
        elif i == pisos:
            viv_area = area_por_piso * m_viv / (pisos - 2) if pisos > 2 else area_por_piso * m_viv
            serv_area = area_por_piso * 0.05
            usos = [
                {"uso": "Vivienda", "area_bruta": round(viv_area, 2), "area_neta": round(viv_area * EFICIENCIAS["Vivienda"], 2)},
                {"uso": "Servicios", "area_bruta": round(serv_area, 2), "area_neta": round(serv_area * EFICIENCIAS["Servicios"], 2)},
                {"uso": "Nucleo", "area_bruta": round(p1_nuc, 2), "area_neta": round(p1_nuc * EFICIENCIAS["Nucleo"], 2)}
            ]
        else:
            viv_area = area_por_piso * m_viv / (pisos - 2) if pisos > 2 else area_por_piso * m_viv
            usos = [
                {"uso": "Vivienda", "area_bruta": round(viv_area, 2), "area_neta": round(viv_area * EFICIENCIAS["Vivienda"], 2)},
                {"uso": "Nucleo", "area_bruta": round(p1_nuc, 2), "area_neta": round(p1_nuc * EFICIENCIAS["Nucleo"], 2)}
            ]
            
        programa.append({
            "piso": i,
            "altura_z": (i - 1) * 3.0, # Asumiendo 3m entrepiso por defecto
            "usos": usos
        })

    return {
        "gfa_total": gfa,
        "pisos": pisos,
        "area_por_piso": round(area_por_piso, 2),
        "programa_pisos": programa,
        "matriz_adyacencia": MATRIZ_ADYACENCIA
    }

def main():
    parser = argparse.ArgumentParser(description="Generador de Programa de Áreas F3")
    parser.add_argument("--gfa", type=float, required=True, help="GFA total de Fase 1")
    parser.add_argument("--pisos", type=int, required=True, help="Número de pisos")
    parser.add_argument("--mix", type=str, default="0.1,0.1,0.8", help="Mix de usos: comercio,salud,vivienda")
    
    args = parser.parse_args()
    
    resultado = distribuir_usos(args.gfa, args.pisos, args.mix)
    
    output_dir = "data/fase-3-masa"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "programa-areas.json")
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)
        
    print("\n=== PROGRAMA DE ÁREAS GENERADO ===")
    print("GFA: {} m2 | Pisos: {}".format(args.gfa, args.pisos))
    print("Mix: Comercio {}, Salud {}, Vivienda {}".format(*args.mix.split(",")))
    print("\nDistribución por piso:")
    for p in resultado["programa_pisos"]:
        print("  Piso {} (Z={:.1f}m):".format(p["piso"], p["altura_z"]))
        for u in p["usos"]:
            print("    - {}: {:.1f} m2 (Neta: {:.1f} m2)".format(u["uso"], u["area_bruta"], u["area_neta"]))
            
    print("\nMatriz de adyacencias guardada en: {}\n".format(output_path))

if __name__ == "__main__":
    main()
    