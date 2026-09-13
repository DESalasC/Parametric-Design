# Plan de Corrección y Validación para F1_CONTEXTO50_BUILD_v02.py

## Antecedentes
Los scripts F1_CONTEXTO50_BUILD_v01.py y F1_CONTEXTO50_BUILD_v01a.py no lograban encontrar el archivo JSON generado por F1_CONTEXTO50_FETCH_v01.py, el cual se ubica en `data/pot-cache/<chip>-contexto50.json`.

## Corrección Aplicada
Se ha creado la versión `F1_CONTEXTO50_BUILD_v02.py` con los siguientes cambios:
1. Añadido `os.path.join(BASE_DIR, "data", "pot-cache")` a la lista `SEARCH_DIRS` para que el autodescubrimiento incluya el caché de POT donde se guarda el JSON de CONTEXTO50.
2. Actualizado el historial de versiones y los comentarios para reflejar el cambio.
3. Mantener la compatibilidad con IronPython 2.7 y las convenciones del proyecto.

## Pasos de Validación
1. **Prerrequisitos**:
   - Ejecutar previamente `F1_CONTEXTO50_FETCH_v01.py` para generar el JSON en `data/pot-cache/AAA0240ZXJH-contexto50.json` (ya hecho).
   - Verificar que el JSON exista y sea válido.

2. **Ejecutar el script en Rhino**:
   - Abrir Rhino 8 y cargar el archivo .3dm de trabajo (o crear uno nuevo).
   - Ejecutar el script `F1_CONTEXTO50_BUILD_v02.py` mediante `_EditPythonScript` o `_-RunPythonScript`.
   - Asegurarse de que JSON_PATH esté vacío (autodescubrimiento) o apuntar explícitamente al JSON.

3. **Salida Esperada**:
   - El script debe imprimir un resumen similar a:
     ```
     F1_CONTEXTO50_BUILD v02 | CHIP AAA0240ZXJH | R 50m | Objetos 94 | Descartados 0 | Fallbacks 0 | Alturas 3.8-19.0m
     Layer: 70-20-30_Volumetrias_vecinas (ok)
     3dm: D:\Work\PROJECTS\DiseñoParametrico\exports\contexto50\AAA0240ZXJH-contexto50.3dm
     obj: D:\Work\PROJECTS\DiseñoParametrico\exports\contexto50\AAA0240ZXJH-contexto50.obj
     JSON: D:\Work\PROJECTS\DiseñoParametrico\data\pot-cache\AAA0240ZXJH-contexto50.json
     ```
   - Deben crearse 94 volúmenes (uno por edificio encontrado) en la capa `70-20-30_Volumetrias_vecinas`.
   - Los archivos .3dm y .obj deben exportarse a la carpeta `exports/contexto50`.

4. **Verificación Adicional**:
   - Comprobar que los objetos creados sean sólidos cerrados (Breps) y que su altura corresponda a la del edificio.
   - Verificar que la huella (polilínea base) coincida en perímetro con la del volumen extruido.
   - Revisar que no haya errores en la consola de Rhino.

5. **Integración con Pipeline**:
   - Una vez validado, el script puede ser utilizado por el componente GHPython `F1_ETAPA3_CONTEXTO50_v01.py` (si existe) o llamado manualmente para generar las volumetrías vecinas necesarias para las etapas posteriores.

## Notas
- Si el script sigue sin encontrar el JSON, verificar que la variable `BASE_DIR` apunte a la raíz correcta del proyecto (`D:\Work\PROJECTS\DiseñoParametrico`).
- En caso de problemas de permisos o rutas, usar rutas absolutas en `JSON_PATH` para depurar.
- El script está diseñado para ser tolerante a fallos: si un edificio no tiene huella válida o altura, se omite y se cuenta en los descartados/fallbacks.

## Próximos Pasos
- Ejecutar la validación en Rhino y reportar resultados.
- Si se necesitan ajustes adicionales (por ejemplo, manejo de multi-anillos o huecos), crear una versión v03.
- Considerar agregar pruebas unitarias para las funciones de ayuda (leer_json, normalizar_vertices, altura_de) usando mocks de Rhino si es factible en el entorno de pruebas.