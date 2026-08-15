# Fase 2 — Demanda y Modelo Financiero

Motor de viabilidad comercial, programa de áreas y **modelo financiero de prefactibilidad**.

## Pipeline (scripts migrados)

| Script | Líneas | Función |
|---|---|---|
| `F2_DEMANDA_MOTOR_v01.py` | 690 (original) | Motor de demanda del pipeline (datos de mercado del pipeline) |
| `F2_OPTIMIZADOR_ADYACENCIA_v01.py` | 1166 | Optimización de adyacencias de unidades |
| `F2_PROG_INTERIOR_v01.py` | 347 | Programa interior de unidades |
| `F2_PROGRAMA_AREAS_v01.py` | 488 | Programa de áreas por tipología |

> El **motor mejorado** (v3.0: KPIs, alertas, sensibilidad ±10%, escenarios D/E, flujo de caja,
> informe HTML, CLI `--chip/--gfa/--costo-lote` compatible con el pipeline, **hook GFA desde Fase 1**)
> vive en **`F2_Modelo_Financiero\`** dentro de esta carpeta. Ver su `MANUAL_DE_USO.md`.
> Hook: si no se pasa `--gfa`, el motor lee `data\fase-2-demanda\<CHIP>-gfa-gh.json` (escrito por
> `F1_EXPORTAR_GFA_v02` en el canvas) y usa `gfa_total_m2`. Igual en `F2_Modelo_Renta\` (v3.0).

## Datos de entrada (canónicos)

`data\fase-2-demanda\` (raíz `data\` del proyecto):

| Archivo | Contenido |
|---|---|
| `AAA0127AZPA-prefactibilidad.json` | Caso actual: GFA 632,695 m² (Fase 1 verificada) |
| `AAA0127AZPA-prefactibilidad-gfa1054.json` | **Alternativa curaduría:** GFA 1054,49 m² (la zona está autorizando mayor edificabilidad) |

## Ejecución

```powershell
cd src\fase-2-demanda\F2_Modelo_Financiero
python F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_mercado2026.json
python F2_DEMANDA_MOTOR_v03.py --parametros parametros_AAA0127AZPA_gfa1054_mercado2026.json
```

## Resultados clave (mercado 2026, CL $1.200 M)

- **GFA 633 (actual):** compra del lote → todos NO VIABLES; aporte del dueño ~30% → B viable
  (ROI 23,0%, dueño recibe $225 M); arriendo sobre valor soportable → A y B viables.
- **GFA 1054 (alternativa curaduría):** B y C dejan utilidad comprando (ROI 8,9%/7,4%);
  **arriendo del lote → las 3 tipologías VIABLES** (B ROI 35,2% con canon sobre precio pedido).

## Documentación

Vault → `20-fases\fase-2-demanda\` (prefactibilidad financiera, datos de mercado, lecciones).
