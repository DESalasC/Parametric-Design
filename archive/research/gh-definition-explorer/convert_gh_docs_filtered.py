import os
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Rutas base: ajusta si las tuyas cambian
SOURCE_ROOT = Path(r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\grasshopper-api-docs")
HTML_ROOT = SOURCE_ROOT / "api" / "grasshopper" / "html"

OUTPUT_ROOT = Path(r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown")
ASSETS_ROOT = OUTPUT_ROOT / "_assets"

# Namespaces que quieres incluir (puedes añadir/quitar)
NAMESPACE_FILTER = {
    "GH_IO.Serialization",
    "Grasshopper",
    "Grasshopper.Kernel",
    # añade más según necesites
}

# Estructuras para construir índices
namespaces_index: Dict[str, List[Tuple[str, Path]]] = {}  # ns -> [(class_name, md_path)]
all_classes_index: List[Tuple[str, str, Path]] = []       # (namespace, class_name, md_path)


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def infer_namespace_from_filename(fname: str) -> str:
    """
    Inferir namespace usando convenciones de nombre de archivo.
    Ejemplo:
      N_GH_IO_Serialization.htm  -> GH_IO.Serialization
      T_Grasshopper_Kernel_GH_Document.htm -> Grasshopper.Kernel
    """
    base = Path(fname).stem  # sin extensión
    parts = base.split("_")

    if len(parts) >= 3 and parts[0] in ("N", "T", "M", "P"):
        # N_Grasshopper_Kernel -> namespace
        if parts[0] == "N":
            # Namespace completo después del prefijo
            ns = ".".join(parts[1:])
            return ns

        # T_Grasshopper_Kernel_GH_Document -> type en namespace
        if parts[0] == "T":
            # todo menos el último trozo suele ser namespace
            ns_parts = parts[1:-1]
            ns = ".".join(ns_parts)
            return ns

        # M_Grasshopper_Kernel_GH_Document_Read -> method
        if parts[0] == "M":
            ns_parts = parts[1:-2]
            ns = ".".join(ns_parts) if ns_parts else ""
            return ns

    # Si no encaja, devolver vacío y que otro método decida
    return ""


def extract_title_and_namespace(soup: BeautifulSoup, html_path: Path) -> Tuple[str, str]:
    """
    Extrae el título y trata de determinar el namespace.
    """
    # Título: intentar usar <title> o el primer h1/h2
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    else:
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            title = h1.get_text(strip=True)
        else:
            h2 = soup.find("h2")
            if h2 and h2.get_text(strip=True):
                title = h2.get_text(strip=True)

    # Intentar inferir namespace desde filename
    ns = infer_namespace_from_filename(html_path.name)

    # Si sigue vacío, intentar buscar pistas en el contenido
    if not ns:
        # A veces el namespace aparece en algún span/div con clase especial
        maybe_ns = soup.find(string=lambda s: s and "Namespace" in s)
        if maybe_ns:
            ns = maybe_ns.strip().split()[-1]

    return title or html_path.stem, ns


def update_image_paths_and_copy(soup: BeautifulSoup, html_path: Path, md_rel_path: Path):
    """
    Encuentra imágenes en el HTML, las copia a OUTPUT_ROOT/_assets y actualiza src
    para que Obsidian las use vía rutas relativas.
    """
    # Directorio de destino para assets de este archivo
    # Opción simple: todas las imágenes van a _assets
    ensure_dir(ASSETS_ROOT)

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        # Resolver ruta original de la imagen
        img_path = (html_path.parent / src).resolve()
        if not img_path.exists():
            continue

        # Copiar a assets con nombre único (namespace/clase + nombre)
        asset_name = f"{md_rel_path.stem}__{Path(src).name}"
        dest_asset_path = ASSETS_ROOT / asset_name

        try:
            shutil.copy2(img_path, dest_asset_path)
        except Exception as e:
            print(f"Error copiando imagen {img_path}: {e}")
            continue

        # Actualizar el src a ruta relativa desde el .md
        # Ej: ![alt](../_assets/filename.png)
        rel_src = os.path.relpath(dest_asset_path, OUTPUT_ROOT / md_rel_path.parent)
        img["src"] = rel_src


def convert_html_to_markdown(html_path: Path) -> Tuple[str, str]:
    """
    Convierte HTML a Markdown y devuelve (markdown, namespace_detectado).
    Maneja imágenes y limpia un poco el HTML.
    """
    try:
        raw_html = html_path.read_text(encoding="utf-8", errors="ignore")
    except UnicodeDecodeError:
        raw_html = html_path.read_text(encoding="latin-1", errors="ignore")

    soup = BeautifulSoup(raw_html, "html.parser")

    # Manejar imágenes antes de convertir
    # NOTA: necesitamos saber md_rel_path, lo pasaremos luego en el flujo principal
    # Aquí solo devolvemos el soup, y afuera llamaremos update_image_paths_and_copy

    # Limpiar navegación/footers básicos si conoces sus ids/clases
    # Ejemplo genérico (ajusta según la estructura real del sitio):
    for selector in ["div.nav", "div.footer", "div#header", "div#footer"]:
        for tag in soup.select(selector):
            tag.decompose()

    # Convertir a Markdown
    markdown = md(str(soup), heading_style="ATX")

    # Extraer namespace (puede usarse para filtrar)
    title, ns = extract_title_and_namespace(soup, html_path)

    # Añadir título explícito como encabezado h1 al inicio
    markdown = f"# {title}\n\n" + markdown

    return markdown, ns


def process_file(html_path: Path):
    """
    Procesa un HTML:
    - Detecta namespace.
    - Aplica filtro por namespace.
    - Convierte a Markdown.
    - Copia imágenes.
    - Actualiza índices.
    """
    # Construir ruta relativa desde HTML_ROOT
    rel = html_path.relative_to(HTML_ROOT)
    md_rel = rel.with_suffix(".md")

    # Leer y parsear HTML
    try:
        raw_html = html_path.read_text(encoding="utf-8", errors="ignore")
    except UnicodeDecodeError:
        raw_html = html_path.read_text(encoding="latin-1", errors="ignore")

    soup = BeautifulSoup(raw_html, "html.parser")

    title, ns = extract_title_and_namespace(soup, html_path)

    # Si hay filtro de namespace y este archivo no entra, saltarlo
    if NAMESPACE_FILTER and ns and ns not in NAMESPACE_FILTER:
        # Debug opcional:
        # print(f"Skipping {html_path} (namespace {ns} no está en filtro)")
        return

    # Manejar imágenes (copiar y actualizar src)
    update_image_paths_and_copy(soup, html_path, md_rel)

    # Convertir a Markdown usando el soup modificado
    markdown = md(str(soup), heading_style="ATX")
    markdown = f"# {title}\n\n" + markdown

    # Crear directorio destino
    md_dest = OUTPUT_ROOT / md_rel
    ensure_dir(md_dest.parent)

    md_dest.write_text(markdown, encoding="utf-8")
    print(f"Converted: {html_path} -> {md_dest} (ns={ns})")

    # Registrar clase para índices si parece ser una página de tipo/clase
    # Heurística: archivos que empiezan por "T_" suelen ser tipos/clases
    if html_path.name.startswith("T_"):
        class_name = title
        if ns:
            namespaces_index.setdefault(ns, []).append((class_name, md_rel))
            all_classes_index.append((ns, class_name, md_rel))


def build_namespace_index_files():
    """
    Crea un archivo index por namespace, con enlaces a todas las clases de ese namespace.
    """
    for ns, entries in namespaces_index.items():
        # Ruta sugerida: OUTPUT_ROOT/ns/index.md
        # Transformar namespace (GH_IO.Serialization) en path GH_IO.Serialization/index.md
        ns_path = OUTPUT_ROOT / ns.replace(".", "/")
        ensure_dir(ns_path)

        index_path = ns_path / "index.md"

        lines = [f"# Namespace {ns}\n"]
        lines.append("## Clases\n")

        # Ordenar alfabéticamente por nombre de clase
        for class_name, md_rel in sorted(entries, key=lambda e: e[0].lower()):
            rel_link = os.path.relpath(OUTPUT_ROOT / md_rel, ns_path)
            lines.append(f"- [{class_name}]({rel_link})")

        index_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Namespace index creado: {index_path}")


def build_master_index():
    """
    Crea un índice maestro en la raíz (OUTPUT_ROOT/index.md) con todos los namespaces y clases.
    """
    master_path = OUTPUT_ROOT / "index.md"
    lines = ["# Índice maestro Grasshopper SDK\n"]

    # Índice por namespace
    lines.append("## Por namespace\n")

    # Ordenar por namespace
    for ns in sorted(namespaces_index.keys()):
        # Link al index del namespace
        ns_path = ns.replace(".", "/") + "/index.md"
        lines.append(f"- [{ns}]({ns_path})")

    # Lista completa de clases
    lines.append("\n## Todas las clases\n")

    for ns, class_name, md_rel in sorted(all_classes_index, key=lambda e: (e[0].lower(), e[1].lower())):
        rel_link = os.path.relpath(OUTPUT_ROOT / md_rel, OUTPUT_ROOT)
        lines.append(f"- **{ns}**: [{class_name}]({rel_link})")

    master_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Índice maestro creado: {master_path}")


def main():
    print(f"HTML root: {HTML_ROOT}")
    print(f"Output root: {OUTPUT_ROOT}")
    ensure_dir(OUTPUT_ROOT)
    ensure_dir(ASSETS_ROOT)

    for root, dirs, files in os.walk(HTML_ROOT):
        for name in files:
            if name.lower().endswith(".htm") or name.lower().endswith(".html"):
                html_path = Path(root) / name
                process_file(html_path)

    # Crear índices
    build_namespace_index_files()
    build_master_index()


if __name__ == "__main__":
    main()