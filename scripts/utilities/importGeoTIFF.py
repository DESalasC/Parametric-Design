import json
import math
import requests
import rasterio
from rasterio.io import MemoryFile
from rasterio.warp import calculate_default_transform, reproject, Resampling
from pyproj import Transformer
from shapely.geometry import Point, mapping

# =========================
# CONFIGURACIÓN
# =========================
SERVICE_URL = "https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/0/export"
OUT_TIF = "mdt_bogota_clip.tif"

# Punto central del lote (LAT, LON) - cambia estos valores
LAT = 4.65
LON = -74.08

# Radio en metros
RADIUS_M = 150  # entre 100 y 200

# Extensión de salida alrededor del punto
PIXELS_PER_M = 1  # 1 pixel por metro en el resultado (ajusta si quieres)
OUT_CRS = "EPSG:3116"  # MAGNA-SIRGAS / Colombia Bogotá zone (métrico)

# =========================
# 1) Reproyectar el punto a CRS métrico
# =========================
to_metric = Transformer.from_crs("EPSG:4326", OUT_CRS, always_xy=True)
x, y = to_metric.transform(LON, LAT)

buffer_geom = Point(x, y).buffer(RADIUS_M)

# Bounding box del buffer
minx, miny, maxx, maxy = buffer_geom.bounds

# =========================
# 2) Pedir la exportación al servicio REST
# =========================
params = {
    "bbox": f"{minx},{miny},{maxx},{maxy}",
    "bboxSR": 3116,
    "imageSR": 3116,
    "size": f"{int((maxx - minx) * PIXELS_PER_M)},{int((maxy - miny) * PIXELS_PER_M)}",
    "format": "tiff",
    "transparent": "false",
    "f": "json"
}

resp = requests.get(SERVICE_URL, params=params, timeout=120)
resp.raise_for_status()
data = resp.json()

if "href" not in data:
    raise RuntimeError(f"No se recibió descarga directa. Respuesta: {json.dumps(data, indent=2)[:2000]}")

img_url = data["href"]

# =========================
# 3) Descargar el TIFF
# =========================
r = requests.get(img_url, timeout=120)
r.raise_for_status()

tmp_tif = "mdt_bogota_raw.tif"
with open(tmp_tif, "wb") as f:
    f.write(r.content)

# =========================
# 4) Reproyectar/recortar a GeoTIFF final
# =========================
with rasterio.open(tmp_tif) as src:
    profile = src.profile.copy()
    profile.update(
        driver="GTiff",
        compress="deflate",
        tiled=True,
        bigtiff="if_safer"
    )

    data = src.read(1)
    src_transform = src.transform
    src_crs = src.crs

    # Crear máscara del buffer en el raster
    from rasterio.features import geometry_mask
    mask = geometry_mask(
        [mapping(buffer_geom)],
        out_shape=data.shape,
        transform=src_transform,
        invert=True
    )

    out_data = data.copy()
    out_data[~mask] = src.nodata if src.nodata is not None else 0

    profile.update(count=1)

    with rasterio.open(OUT_TIF, "w", **profile) as dst:
        dst.write(out_data, 1)

print(f"GeoTIFF guardado en: {OUT_TIF}")