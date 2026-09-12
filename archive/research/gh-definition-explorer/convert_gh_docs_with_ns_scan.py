import os
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup
from markdownify import markdownify as md

# === CONFIGURACIÓN DE RUTAS ===

SOURCE_ROOT = Path(r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\grasshopper-api-docs")
HTML_ROOT = SOURCE_ROOT / "api" / "grasshopper" / "html"

OUTPUT_ROOT = Path(r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown")
ASSETS_ROOT = OUTPUT_ROOT / "_assets"

# Si está vacío, NO se filtra por namespace (se procesa todo)
# Luego puedes restringir, por ejemplo:
# NAMESPACE_FILTER = {"GH_IO.Serialization", "GH_IO.Types", "GH_IO.UserInterface"}
NAMESPACE_FILTER: set[str] = set()

# Índices y resumen
namespaces_index: Dict[str, List[Tuple[str, Path]]] = {}  # ns -> [(class_name, md_rel)]
all_classes_index: List[Tuple[str, str, Path]] = []       # (ns, class_name, md_rel)
namespaces_count: Dict[str, int] = {}                     # ns -> count de páginas


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def infer_namespace_from_filename(fname: str) -> str:
    """
    Heurística basada en la convención de nombres de grasshopper-api-docs.

    Ejemplos típicos:
    - N_GH_IO_Serialization.htm                  -> GH_IO.Serialization
    - N_Grasshopper_Kernel.htm                  -> Grasshopper.Kernel
    - T_GH_IO_Serialization_GH_Archive.htm       -> GH_IO.Serialization
    - T_GH_IO_Types_GH_BoundingBox.htm           -> GH_IO.Types
    - T_GH_IO_UserInterface_GH_ArchiveMessageViewer.htm -> GH_IO.UserInterface
    - T_Grasshopper_Kernel_GH_Document.htm       -> Grasshopper.Kernel
    """
    stem = Path(fname).stem
    parts = stem.split("_")

    if not parts:
        return ""

    prefix = parts[0]

    # N_* archivos de namespace
    if prefix == "N" and len(parts) >= 2:
        # N_Grasshopper_Kernel -> Grasshopper.Kernel
        # N_GH_IO_Serialization -> GH_IO.Serialization
        ns = ".".join(parts[1:])
        return ns

    # T_* archivos de tipo (clase)
    if prefix == "T" and len(parts) >= 3:
        # GH_IO.*
        if parts[1] == "GH" and parts[2] == "IO":
            # T_GH_IO_Serialization_GH_Archive
            # parts = ["T", "GH", "IO", "Serialization", "GH", "Archive"]
            if len(parts) >= 4:
                sub = parts[3]  # Serialization, Types, UserInterface, ...
                ns = f"GH_IO.{sub}"
                return ns
            else:
                return "GH_IO"

        # Grasshopper.*
        if parts[1] == "Grasshopper":
            if len(parts) >= 3:
                # T_Grasshopper_Kernel_GH_Document -> Grasshopper.Kernel
                ns_parts = parts[1:-1]
                ns = ".".join(ns_parts)
                return ns
            else:
                return "Grasshopper"

        # fallback genérico
        return parts[1]

    # M_* archivos de métodos (similar lógica)
    if prefix == "M" and len(parts) >= 3:
        if parts[1] == "GH" and parts[2] == "IO":
            if len(parts) >= 4:
                sub = parts[3]
                ns = f"GH_IO.{sub}"
                return ns
            else:
                return "GH_IO"

        if parts[1] == "Grasshopper":
            if len(parts) >= 3:
                ns_parts = parts[1:-2]
                ns = ".".join(ns_parts) if ns_parts else "Grasshopper"
                return ns
            else:
                return "Grasshopper"

        return parts[1]

    return ""