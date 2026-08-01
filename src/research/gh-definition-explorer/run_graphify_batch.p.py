#!/usr/bin/env python3
import subprocess
from pathlib import Path
import os

# Rutas base (ajustadas a tu estructura)
MARKDOWN_ROOT = Path(
    r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
)
BATCH_ROOT = MARKDOWN_ROOT / "graphify_batch"
PROGRESS_FILE = MARKDOWN_ROOT / "graphify_progress.txt"

# Lista de backends en el orden que quieres probar
# Ajusta según las APIs que realmente usas y que Graphify soporte
BACKENDS = ["gemini", "openai", "deepseek"]

def load_batch_files():
    """Devuelve rutas relativas (respecto a MARKDOWN_ROOT) de los .md en graphify_batch."""
    files = []
    for root, dirs, fs in os.walk(BATCH_ROOT):
        root_path = Path(root)
        for name in fs:
            if name.lower().endswith(".md"):
                full = root_path / name
                rel = full.relative_to(MARKDOWN_ROOT)
                files.append(rel)
    return files

def append_progress(files):
    """Añade las rutas de archivos procesados al archivo de progreso."""
    with PROGRESS_FILE.open("a", encoding="utf-8") as f:
        for rel in files:
            f.write(str(rel) + "\n")

def run_graphify_with_backend(backend: str) -> bool:
    """Ejecuta Graphify sobre BATCH_ROOT con un backend; devuelve True si termina bien."""
    if not BATCH_ROOT.exists():
        print(f"[ERROR] No existe la carpeta de lote: {BATCH_ROOT}")
        return False

    print(f"[INFO] Ejecutando Graphify sobre el lote con backend '{backend}'...")
    cmd = ["graphify", "--backend", backend, str(BATCH_ROOT)]
    print(f"[GRAPHIFY] {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print("[ERROR] No se encontró el comando 'graphify'.")
        print("  Verifica que has ejecutado:")
        print("    pip install graphifyy")
        print("    graphify install")
        return False

    if result.returncode == 0:
        print("[OK] Graphify terminó correctamente con backend", backend)
        return True

    stderr = result.stderr or ""
    stdout = result.stdout or ""
    combined = (stderr + "\n" + stdout).lower()

    # Detectar errores de cuota (429, RESOURCE_EXHAUSTED, quota exceeded)
    if "resource_exhausted" in combined or "quota" in combined or "429" in combined:
        print("[WARN] Error de cuota para backend", backend)
        print("      Mensaje (primeros 500 caracteres):")
        print((stderr + "\n" + stdout).strip()[:500], "...")
        return False

    # Otro tipo de error
    print("[ERROR] Graphify falló con backend", backend)
    print("        returncode:", result.returncode)
    print("        stderr (primeros 500 caracteres):")
    print(stderr.strip()[:500])
    return False

def main():
    if not BATCH_ROOT.exists():
        print(f"[ERROR] No existe la carpeta de lote: {BATCH_ROOT}")
        print("  Ejecuta primero prepare_graphify_batch_prioritized.py.")
        return

    batch_files = load_batch_files()
    if not batch_files:
        print("[WARN] No hay .md dentro de graphify_batch. Nada que procesar.")
        return

    print(f"[OK] Lote con {len(batch_files)} archivos listo en {BATCH_ROOT}")

    # Probar cada backend en orden hasta que uno funcione
    for backend in BACKENDS:
        success = run_graphify_with_backend(backend)
        if success:
            append_progress(batch_files)
            print(f"[OK] Progreso actualizado en {PROGRESS_FILE}")
            return
        else:
            print(f"[INFO] Cambiando al siguiente backend (falló '{backend}').")

    print("[ERROR] Ningún backend pudo procesar el lote (cuota agotada o errores).")
    print("        Intenta más tarde, reduce BATCH_SIZE, o ajusta BACKENDS/API keys.")

if __name__ == "__main__":
    main()