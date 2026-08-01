#!/usr/bin/env python3
import os
from pathlib import Path
import shutil

MARKDOWN_ROOT = Path(
    r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
)
BATCH_ROOT = MARKDOWN_ROOT / "graphify_batch"
PROGRESS_FILE = MARKDOWN_ROOT / "graphify_progress.txt"

# Tamaño máximo de lote
BATCH_SIZE = 200  # ajusta según tu cuota y tiempos

# Prioridad de carpetas para clases individuales (relativas a MARKDOWN_ROOT)
PRIORITY_DIRS = [
    Path("GH_IO"),                # raíz GH_IO
    Path("GH_IO") / "Serialization",
    Path("GH_IO") / "Types",
]

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

def select_index_files(all_md, progress):
    """Devuelve lista de index.md pendientes (maestro + por carpetas)."""
    index_files = [rel for rel in all_md if rel.name.lower() == "index.md"]
    pending_index = [rel for rel in index_files if str(rel) not in progress]
    return pending_index

def select_class_files_prioritized(all_md, progress, limit):
    """Selecciona clases (no index.md) empezando por GH_IO, GH_IO/Serialization, GH_IO/Types, luego resto."""
    # Separar files ya procesados
    pending = [rel for rel in all_md if str(rel) not in progress and rel.name.lower() != "index.md"]

    batch = []

    # Primero las carpetas prioritarias, en orden
    for pdir in PRIORITY_DIRS:
        for rel in pending:
            if rel.parts[:len(pdir.parts)] == pdir.parts:
                batch.append(rel)
                if len(batch) >= limit:
                    return batch

    # Después el resto (carpetas no prioritarias)
    if len(batch) < limit:
        for rel in pending:
            # saltar los que ya añadimos
            if rel in batch:
                continue
            batch.append(rel)
            if len(batch) >= limit:
                break

    return batch

def main():
    all_md = list_all_md()
    progress = load_progress()

    print(f"[INFO] Total archivos .md: {len(all_md)}")
    print(f"[INFO] Ya procesados:      {len(progress)}")

    # 1) Primero: todos los index.md (si aún hay index pendientes)
    pending_index = select_index_files(all_md, progress)
    if pending_index:
        batch = pending_index[:BATCH_SIZE]
        print(f"[OK] Se encontraron {len(pending_index)} index.md pendientes.")
        print(f"[OK] Preparando lote con {len(batch)} index.md...")
    else:
        # 2) Después: clases individuales por prioridad de carpeta
        batch = select_class_files_prioritized(all_md, progress, BATCH_SIZE)
        if not batch:
            print("[OK] No hay clases pendientes, todo está procesado según graphify_progress.txt.")
            return
        print(f"[OK] Preparando lote con {len(batch)} clases (priorizando GH_IO, GH_IO/Serialization, GH_IO/Types).")

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