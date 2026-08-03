#!/usr/bin/env python3
"""Test de validación de tool use - Nemotron"""
import json
from pathlib import Path

def test_read_pot_cache():
    """Verifica que puede leer el caché POT"""
    cache_path = Path(__file__).parent.parent.parent / "data" / "pot-cache" / "REAL-002407033006.json"
    if cache_path.exists():
        data = json.loads(cache_path.read_text(encoding="utf-8"))
        altura = data.get("pot", {}).get("altura_maxima_m")
        upz = data.get("pot", {}).get("upz", {}).get("nombre")
        print(f"✅ Archivo leído correctamente")
        print(f"   Altura máxima: {altura} m")
        print(f"   UPZ: {upz}")
        return True
    else:
        print(f"❌ No se encontró: {cache_path}")
        return False

if __name__ == "__main__":
    test_read_pot_cache()