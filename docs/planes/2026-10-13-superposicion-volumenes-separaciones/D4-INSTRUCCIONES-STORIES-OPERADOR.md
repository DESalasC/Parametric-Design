# D4 — Stories en ArchiCAD: hoja del operador e instrucciones (2026-10-13)

- **Objetivo:** crear los **8 niveles** en ArchiCAD **antes** de volver a generar/pushear las zonas; paso **manual-asistido** (la API/LC de ac29 no crea stories — solo lectura).
- **Herramienta:** `src/interfases-archicad/F3_StorySync_v02.py` — opción nueva **`--hoja`** (v02.1, 2026-10-13).
- **Ejecutado hoy:** `--plan --chip AAA0030JKOE --hoja` → regeneró `niveles_deseados.json` y escribió `src/fase-3-masa/casos/AAA0030JKOE/niveles_operador.txt` (hoja lista para el operador).
- **Estado AC verificado hoy:** 3 niveles (0,000 / 3,000 / 6,000); **faltan los 8** de la lista (check ejecutado en vivo).

## Lista para crear (marco canvas — misma referencia que zonas/LC)

| Nombre | Elevación (m) | Relativa (m) |
|---|---|---|
| GF  | −11,565 | +0,000 |
| L01 | −8,515  | +3,050 |
| L02 | −5,465  | +6,100 |
| L03 | −2,415  | +9,150 |
| L04 | +0,635  | +12,200 |
| L05 | +3,685  | +15,250 |
| L06 | +6,735  | +18,300 |
| L07 | +9,785  | +21,350 |

*(entrepiso 3,05 m; base = −11,565 = menor cota de bloque; snap ≤ 0,31 m; RF opcional no incluido)*

## Pasos (ArchiCAD 29 — Test 07)

1. **Documento > Preferencias del proyecto > Configuración de pisos…**
   (EN: *Options > Project Preferences > Stories…*)
2. Ajustar los **3 niveles existentes** (nombre + cota):
   - `Ground Floor` → **GF** @ **−11.565**
   - `Story` → **L01** @ **−8.515**
   - `Story` → **L02** @ **−5.465**
3. Insertar **5 niveles nuevos** arriba (botón Insertar / «+») y fijar cota:
   - **L03** @ −2.415 · **L04** @ +0.635 · **L05** @ +3.685 · **L06** @ +6.735 · **L07** @ +9.785
4. **Aceptar** y verificar (con ArchiCAD abierto):
   ```powershell
   .venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --check --chip AAA0030JKOE
   ```
   → debe responder: «**Todos los niveles deseados existen y estan alineados.**»

## Condiciones · límites · resultado esperado

- **Condición:** AC abierto en Test 07; creación manual (no automatizable por API).
- **Límite:** mantener orden ascendente; si ArchiCAD ajusta alguna cota al insertar, volver a fijar el valor exacto. La verificación compara **cota** (tolerancia 1 cm); los nombres son recomendados (BEP) pero no bloquean el check.
- **Resultado esperado:** 8 niveles GF..L07; `--check` en verde; después, la corrida limpia (D3-F2) re-genera las zonas **por nivel** con Name/Number BEP visibles en su piso.

## Registro

- Salidas de `--plan --hoja`, `--list` y `--check` del 2026-10-13: `evidencias/2026-10-13-storysync-salida.txt`.
- Hoja vigente: `src/fase-3-masa/casos/AAA0030JKOE/niveles_operador.txt` (se regenera con `--hoja`; parámetro `--tapa` si se quiere RF).
