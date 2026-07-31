cd D:\WORK\PROJECTS\DiseñoParametrico

# Crear venv
python -m venv .venv

# Activar
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -e .[dev]
pip install pyogrio shapely click rich pyproj
pip install rhino3dm  # para validate-neighbors.py