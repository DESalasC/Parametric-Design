cd D:\WORK\PROJECTS\DiseñoParametrico

# Crear venv — SIEMPRE con Python 3.12 (los wheels del stack son cp312;
# crearlo con 3.11/3.13 lo rompe). Si quedo apuntando mal, reparar SIN reinstalar:
#   py -3.12 -m venv --upgrade .venv
py -3.12 -m venv .venv

# Activar
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -e .[dev]
pip install pyogrio shapely click rich pyproj
pip install rhino3dm  # para validate-neighbors.py