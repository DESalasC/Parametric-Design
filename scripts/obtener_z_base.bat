@echo off
:: ============================================
::   EXTRACCION AUTOMATICA DE COTAS DE ARRANQUE (Z_BASE)
:: ============================================
:: Este script extrae las cotas de arranque necesarias para crear stories en ArchiCAD
:: y las guarda en niveles_deseados.json dentro del directorio del CHIP activo
:: ============================================

:: Configurar entorno
set "SCRIPT_DIR=%~dp0"
set "PROJECT_DIR=%SCRIPT_DIR%.."

echo.
echo ============================================
echo   EXTRACCION AUTOMATICA DE COTAS DE ARRANQUE
echo ============================================
echo.

:: Verificar que estamos en el entorno correcto
if not exist "%PROJECT_DATA%\src\fase-3-masa" (
    echo ERROR: No se encontro el directorio del proyecto
    echo Verifique que este bat se encuentre en:
    echo   %PROJECT_DIR%\scripts\
    pause
    exit /b 1
)

:: Preguntar por el CHIP (en versiones futuras se puede detectar automaticamente)
set /p CHIP_ID=Ingrese el ID del CHIP (ej: B, AAA0030JKOE, etc.): 
if "%CHIP_ID%"=="" (
    echo Error: Se requiere un ID de CHIP
    pause
    exit /b 1
)

:: Ejecutar el script de Python
echo.
echo Procesando chip: %CHIP_ID%
python "%SCRIPT_DIR%extraer_z_base.py" %CHIP_ID%
set ERRORLEVEL=%ERRORLEVEL%

if %ERRORLEVEL% neq 0 (
    echo.
    echo ERROR: El script de extraccion fallo con codigo %ERRORLEVEL%
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ============================================
echo   PROCESO COMPLETADO
echo ============================================
echo.
echo Próximos pasos:
echo 1. Copiar los valores de z_base a los stories en ArchiCAD
echo 2. Ejecutar F3_StorySync v02 --check para verificar
echo 3. Continuar con generación de volumenes
echo.
pause