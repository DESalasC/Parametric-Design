import subprocess
from pathlib import Path

# Carpeta donde están tus .md del Grasshopper SDK
DOCS_ROOT = Path(
    r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
)

def main():
    if not DOCS_ROOT.exists():
        print(f"[ERROR] No existe la carpeta de documentos Markdown: {DOCS_ROOT}")
        return

    print(f"[OK] Carpeta de entrada para Graphify: {DOCS_ROOT}")
    print("[INFO] Ejecutando Graphify 0.9.20 sobre esta carpeta...")

    # Comando correcto para Graphify 0.9.20: graphify <ruta>
    cmd = ["graphify", str(DOCS_ROOT)]
    print(f"[GRAPHIFY] {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Graphify terminó con error: {e}")
        return
    except FileNotFoundError:
        print("[ERROR] No se encontró el comando 'graphify'.")
        print("  Verifica que has ejecutado:")
        print("    pip install graphifyy")
        print("    graphify install")
        return

    # Carpeta de salida de Graphify (según docs: graphify-out dentro de la carpeta de entrada)
    output_dir = DOCS_ROOT / "graphify-out"
    if output_dir.exists():
        print(f"[OK] Graphify ha generado el grafo en: {output_dir}")
        print("  - graph.html         → visualización interactiva")
        print("  - GRAPH_REPORT.md    → resumen de nodos y hallazgos")
        print("  - graph.json         → grafo persistente y queryable")
    else:
        print("[WARN] No se encontró la carpeta graphify-out.")
        print("  Revisa la salida de Graphify en la consola para detalles.")

if __name__ == "__main__":
    main()