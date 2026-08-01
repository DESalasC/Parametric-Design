#!/usr/bin/env python3
import os
from pathlib import Path
import shutil

MARKDOWN_ROOT = Path(
    r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
)
BATCH_ROOT = MARKDOWN_ROOT / "graphify_batch"
PROGRESS_FILE = MARKDOWN_ROOT / "graphify_progress.txt"

BATCH_SIZE = 200  # ajusta según tu cuota y tiempos

def load_progress():
    if not PROGRESS_FILE.exists():
        return set()
    with PROGRESS_FILE.open("r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def list_all_md():
    files = []
    for root, dirs, fs in os.walk(MARKDOWN_ROOT):
        root_path = Path(root)
        if "_assets" in root_path.parts or "graphify_batch" in root_path.parts:
            continue
        for name in fs:
            if name.lower().endswith(".md"):
                full = root_path / name
                rel = full.relative_to(MARKDOWN_ROOT)
                files.append(rel)
    return files

def main():
    all_md = list_all_md()
    progress = load_progress()

    pending = [rel for rel in all_md if str(rel) not in progress]
    if not pending:
        print("[OK] No hay archivos pendientes, todo está procesado según graphify_progress.txt.")
        return

    # Elegir lote
    batch = pending[:BATCH_SIZE]
    print(f"[INFO] Total archivos .md: {len(all_md)}")
    print(f"[INFO] Ya procesados:      {len(progress)}")
    print(f"[INFO] Pendientes:         {len(pending)}")
    print(f"[OK] Preparando lote con {len(batch)} archivos...")

    # Resetear carpeta de batch
    if BATCH_ROOT.exists():
        shutil.rmtree(BATCH_ROOT)
    BATCH_ROOT.mkdir(parents=True, exist_ok=True)

    # Copiar archivos al batch, manteniendo estructura
    for rel in batch:
        src = MARKDOWN_ROOT / rel
        dest = BATCH_ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    print(f"[OK] Lote creado en: {BATCH_ROOT}")
    print("    Ejecuta ahora run_graphify_batch.py para procesar este lote.")

if __name__ == "__main__":
    main()