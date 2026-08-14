# -*- coding: utf-8 -*-
"""
generar_presentacion.py — Genera la presentacion final del proyecto (deck HTML autocontenido,
estilo Fathom) consolidando los resultados de los casos de estudio del ejercicio 2026-08-14:
  - AAA0127AZPA (El Prado, Suba) — GFA 1053 m2, CL $550 M  [caso resuelto]
  - AAA0030JKOE (La Candelaria)  — GFA 3312,6 m2, CL $1.420 M [centro historico]
  - 002407033006 (Venecia, sur)  — GFA 650 m2, CL $192 M      [caso de estres]

Lee los resultados_completos.json de los motores F2 (venta) y F2 Renta y los JSON de
entrada del pipeline; genera exports/presentaciones/presentacion_casos_2026-08-14.html.

USO:  python scripts/utilities/generar_presentacion.py
"""
import json
import os

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
FIN = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Financiero")
REN = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Renta")
DATA = os.path.join(ROOT, "data", "fase-2-demanda")
OUT = os.path.join(ROOT, "exports", "presentaciones")

CASOS = [
    {
        "id": "AAA0127AZPA",
        "titulo": "Caso A — El Prado, Suba (norte medio)",
        "chip": "AAA0127AZPA · UPZ 19 El Prado",
        "gfa": 1053.0,
        "cl": 550_000_000,
        "venta": os.path.join(FIN, "resultados_AAA0127AZPA_venta_gfa1053_cl550", "resultados_completos.json"),
        "renta": os.path.join(REN, "resultados_AAA0127AZPA_renta_gfa1053_cl550", "resultados_completos.json"),
        "pipeline": os.path.join(DATA, "AAA0127AZPA-prefactibilidad-gfa1053-cl550.json"),
        "color": "#1F3A5F",
        "lectura": ("Suelo renegociado ($550 M): la venta mejora (B ROI 18,5%) pero no alcanza el 22%; "
                    "la renta LP x VIS es VIABLE (TIR 11,1%, VPN +$271 M). Veredicto del caso: "
                    "construir para arrendar con producto VIS en largo plazo."),
    },
    {
        "id": "AAA0030JKOE",
        "titulo": "Caso B — La Candelaria (centro historico)",
        "chip": "AAA0030JKOE · UPZ 94 La Candelaria",
        "gfa": 3312.575,
        "cl": 1_420_000_000,
        "venta": os.path.join(FIN, "resultados_AAA0030JKOE_venta", "resultados_completos.json"),
        "renta": os.path.join(REN, "resultados_AAA0030JKOE_renta", "resultados_completos.json"),
        "pipeline": os.path.join(DATA, "AAA0030JKOE-prefactibilidad.json"),
        "color": "#7A4E2D",
        "lectura": ("Escala grande + zona turistica: la venta B Estándar ya es VIABLE (ROI 22,3%) y la "
                    "renta amplia la viabilidad a 5 de 6 combinaciones (mejor CP x A, TIR 12,8%). "
                    "El suelo soportable ($4.374 M max.) supera con holgura el CL del ejercicio."),
    },
    {
        "id": "002407033006",
        "titulo": "Caso C — Venecia, Tunjuelito (sur)",
        "chip": "002407033006 · UPZ 42 Venecia",
        "gfa": 650.0,
        "cl": 192_000_000,
        "venta": os.path.join(FIN, "resultados_002407033006_venta", "resultados_completos.json"),
        "renta": os.path.join(REN, "resultados_002407033006_renta", "resultados_completos.json"),
        "pipeline": os.path.join(DATA, "002407033006-prefactibilidad.json"),
        "color": "#3E6B4F",
        "lectura": ("Caso de estres (lote pequeno, valores bajos): ni la venta (A ROI 16,7%) ni la "
                    "renta (suelo soportable $0) alcanzan los umbrales. Leccion: en esta zona el "
                    "producto VIS apenas se acerca; se requiere revalidar canones/costos o no invertir."),
    },
]


def _fmt_m(v):
    return f"{v / 1e6:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _h(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


_CSS = """
:root{--papel:#FAF9F6;--tinta:#1C1C1A;--gris:#6B6B66;--linea:#D8D5CD;--navy:#1F3A5F;
--rojo:#B0413E;--verde:#3E6B4F;--amarillo:#9A7B2D;--celda:#F1EFE9;}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--papel);color:var(--tinta);
font-family:"Helvetica Neue",Helvetica,Arial,"Segoe UI",sans-serif;line-height:1.55;}
.hero{background:var(--tinta);color:var(--papel);padding:64px 0 48px;}
.wrap{max-width:1060px;margin:0 auto;padding:0 28px;}
.kicker{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:#A9A9A2;margin-bottom:14px;}
.hero h1{font-size:34px;line-height:1.18;letter-spacing:-.01em;max-width:18ch;}
.hero .sub{color:#CFCEC8;font-size:15px;margin-top:14px;max-width:64ch;}
.hero .meta{display:flex;flex-wrap:wrap;gap:8px 24px;margin-top:22px;font-size:12.5px;color:#A9A9A2;}
.hero .meta b{color:#fff;font-weight:600;}
section{padding:46px 0;border-bottom:1px solid var(--linea);}
section.alt{background:#F4F2EC;}
h2{font-size:17px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin-bottom:6px;}
.lead{color:var(--gris);font-size:13.5px;margin-bottom:18px;max-width:72ch;}
h3{font-size:14px;font-weight:700;margin:20px 0 8px;}
table{width:100%;border-collapse:collapse;font-size:13px;margin:10px 0 6px;}
th{background:var(--celda);text-align:left;font-weight:600;padding:8px 10px;
border-bottom:2px solid var(--tinta);font-size:11.5px;letter-spacing:.03em;}
td{padding:8px 10px;border-bottom:1px solid var(--linea);vertical-align:top;}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;}
tr.grupo td{background:var(--celda);font-weight:700;font-size:11.5px;letter-spacing:.08em;
text-transform:uppercase;color:var(--navy);border-bottom:2px solid var(--tinta);}
.estado{padding:2px 8px;border-radius:2px;font-size:11px;font-weight:600;letter-spacing:.04em;white-space:nowrap;}
.ok{background:#E3EDE6;color:var(--verde);}
.bad{background:#F6E4E3;color:var(--rojo);}
.warn{background:#F4EDDC;color:var(--amarillo);}
.nota{background:var(--celda);border-left:3px solid var(--navy);padding:14px 18px;font-size:13.5px;margin:16px 0;}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:14px 0;}
@media(max-width:760px){.cards{grid-template-columns:1fr;}}
.card{border:1px solid var(--linea);padding:16px;background:#fff;}
.card .k{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gris);}
.card .v{font-size:24px;font-weight:700;font-variant-numeric:tabular-nums;margin-top:4px;}
.card .d{font-size:12px;color:var(--gris);margin-top:2px;}
.road{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:16px 0;}
@media(max-width:760px){.road{grid-template-columns:1fr;}}
.road .f{border:1px solid var(--linea);padding:14px;background:#fff;position:relative;}
.road .f .n{font-size:10.5px;letter-spacing:.14em;color:var(--gris);}
.road .f .t{font-size:13.5px;font-weight:700;margin-top:4px;}
.road .f .s{font-size:11.5px;margin-top:6px;}
.road .f.hecha .s{color:var(--verde);}
.road .f.prox .s{color:var(--amarillo);}
footer{padding:34px 0 60px;font-size:11.5px;color:var(--gris);}
.tabla-scroll{overflow-x:auto;}
.mini{font-size:12px;color:var(--gris);}
.badge{display:inline-block;font-size:11px;letter-spacing:.18em;text-transform:uppercase;
border:1px solid currentColor;padding:3px 10px;border-radius:2px;margin-bottom:12px;}
.badge.ok{color:var(--verde);} .badge.bad{color:var(--rojo);}
"""


def _venta_html(caso) -> str:
    with open(caso["venta"], "r", encoding="utf-8") as f:
        r = json.load(f)
    filas = ""
    for esc in r["escenarios"]:
        estado = ("<span class='estado ok'>VIABLE</span>" if esc["ROI_pct"] >= r["reglas_decision"]["roi_minimo_pct"]
                  else "<span class='estado bad'>NO VIABLE</span>")
        filas += (f"<tr><td><b>{_h(esc['producto'])}</b></td>"
                  f"<td class='num'>{esc['num_unidades']}</td>"
                  f"<td class='num'>{esc['tamano_unidad_m2']:.0f}</td>"
                  f"<td class='num'>{_fmt_m(esc['ingresos_totales_cop'])}</td>"
                  f"<td class='num'>{_fmt_m(esc['costo_total_cop'])}</td>"
                  f"<td class='num'>{_fmt_m(esc['utilidad_bruta_cop'])}</td>"
                  f"<td class='num'>{esc['MUB_pct']:.1f}%</td>"
                  f"<td class='num'>{esc['ROI_pct']:.1f}%</td>"
                  f"<td class='num'>{esc['CL_IT_pct']:.1f}%</td><td>{estado}</td></tr>")
    rec = r["recomendacion"]
    cls = "ok" if rec["estado"] == "VIABLE" else "bad"
    return f"""
<h3>Modelo de venta (F2) — KPIs por escenario</h3>
<div class="tabla-scroll"><table>
<tr><th>Producto</th><th class="num">Unid.</th><th class="num">m2/u</th><th class="num">Ingresos (M$)</th>
<th class="num">CTD (M$)</th><th class="num">UB (M$)</th><th class="num">MUB</th><th class="num">ROI</th>
<th class="num">CL/IT</th><th>Estado</th></tr>{filas}</table></div>
<p class="mini">Regla: ROI ≥ 22% · MUB ≥ 18% · CL/IT ≤ 30%. Montos en millones de COP.</p>
<div class="nota"><b>Veredicto venta:</b> {_h(rec['veredicto_textual'])}</div>"""


def _renta_html(caso) -> str:
    with open(caso["renta"], "r", encoding="utf-8") as f:
        r = json.load(f)
    filas = ""
    for estr in ("CP", "LP"):
        grupo = next(x for x in r["resultados"] if x["estrategia"] == estr)
        filas += f"<tr class='grupo'><td colspan='9'>{_h(grupo['estrategia_nombre'])}</td></tr>"
        for res in [x for x in r["resultados"] if x["estrategia"] == estr]:
            alertas = r["alertas"].get(f"{res['estrategia']}_{res['escenario_id']}", [])
            criticas = [a for a in alertas if a["nivel"] == "critica"]
            estado = ("<span class='estado bad'>NO VIABLE</span>" if criticas
                      else "<span class='estado ok'>VIABLE</span>")
            tir = f"{res['TIR_pct']:.1f}%" if res["TIR_pct"] is not None else "—"
            filas += (f"<tr><td><b>{_h(res['producto'])}</b></td>"
                      f"<td class='num'>{res['num_unidades']}</td>"
                      f"<td class='num'>{_fmt_m(res['gpi_1_cop'])}</td>"
                      f"<td class='num'>{_fmt_m(res['noi_1_cop'])}</td>"
                      f"<td class='num'>{_fmt_m(res['inversion_total_cop'])}</td>"
                      f"<td class='num'>{res['cap_rate_entrada_pct']:.1f}%</td>"
                      f"<td class='num'>{tir}</td>"
                      f"<td class='num'>{_fmt_m(res['VPN_cop'])}</td><td>{estado}</td></tr>")
    rec = r["recomendacion"]
    mejor = rec.get("recomendado")
    cls = "ok" if rec["estado"] == "VIABLE" else "bad"
    mejor_txt = ""
    if mejor:
        tir = f"{mejor['TIR_pct']:.1f}%" if mejor["TIR_pct"] is not None else "—"
        mejor_txt = (f" Mejor: {_h(mejor['estrategia_nombre'].split(' — ')[0])} x "
                     f"{_h(mejor['producto'])} (TIR {tir}, VPN {_fmt_m(mejor['VPN_cop'])} M).")
    return f"""
<h3>Modelo Build-to-Rent (F2 Renta) — 10 años con valor de salida</h3>
<div class="tabla-scroll"><table>
<tr><th>Producto</th><th class="num">Unid.</th><th class="num">GPI a1 (M$)</th><th class="num">NOI a1 (M$)</th>
<th class="num">Inversion (M$)</th><th class="num">Cap rate</th><th class="num">TIR</th>
<th class="num">VPN (M$)</th><th>Estado</th></tr>{filas}</table></div>
<p class="mini">Regla: TIR ≥ 10% · cap rate entrada ≥ 5% · VPN > 0 @ 10%. Montos en millones de COP.</p>
<div class="nota"><b>Veredicto renta:</b> {_h(rec['veredicto_textual'])}{mejor_txt}</div>"""


def _suelo_html(caso) -> str:
    with open(caso["renta"], "r", encoding="utf-8") as f:
        r = json.load(f)
    filas = ""
    orden = sorted(r["resultados"], key=lambda x: x["suelo_soportable_cop"], reverse=True)
    for res in orden[:4]:
        cl = caso["cl"]
        est = ("<span class='estado ok'>cubre CL</span>" if res["suelo_soportable_cop"] >= cl
               else "<span class='estado bad'>no cubre CL</span>")
        filas += (f"<tr><td>{_h(res['estrategia_nombre'].split(' — ')[0])}</td>"
                  f"<td><b>{_h(res['producto'])}</b></td>"
                  f"<td class='num'>{_fmt_m(res['suelo_soportable_cop'])}</td>"
                  f"<td class='num'>{res['CL_inversion_pct']:.1f}%</td><td>{est}</td></tr>")
    return f"""<h3>Suelo soportable en renta (vara de negociacion)</h3>
<div class="tabla-scroll"><table>
<tr><th>Estrategia</th><th>Producto</th><th class="num">CL soportable (M$)</th>
<th class="num">CL / inversion</th><th>Vs. CL del caso ({_fmt_m(caso['cl'])} M)</th></tr>{filas}</table></div>"""


def _resumen_cards(caso) -> str:
    with open(caso["venta"], "r", encoding="utf-8") as f:
        v = json.load(f)
    with open(caso["renta"], "r", encoding="utf-8") as f:
        r = json.load(f)
    b_venta = next(x for x in v["escenarios"] if x["escenario_id"] == "B_ESTANDAR")
    mejor_renta = r["recomendacion"].get("recomendado")
    tir = f"{mejor_renta['TIR_pct']:.1f}%" if mejor_renta and mejor_renta["TIR_pct"] else "—"
    vpn = _fmt_m(mejor_renta["VPN_cop"]) if mejor_renta else "—"
    return f"""<div class="cards">
<div class="card"><div class="k">Venta · B Estándar</div><div class="v">{b_venta['ROI_pct']:.1f}%</div>
<div class="d">ROI (umbral 22%) · UB {_fmt_m(b_venta['utilidad_bruta_cop'])} M</div></div>
<div class="card"><div class="k">Renta · mejor combo</div><div class="v">{tir}</div>
<div class="d">TIR {_h(mejor_renta['estrategia_nombre'].split(' — ')[0])} x {_h(mejor_renta['producto'].split(' — ')[0]) if mejor_renta else ''} · VPN {vpn} M</div></div>
<div class="card"><div class="k">Suelo del caso</div><div class="v">{_fmt_m(caso['cl'])} M</div>
<div class="d">GFA {caso['gfa']:.0f} m²</div></div>
</div>"""


def generar() -> None:
    os.makedirs(OUT, exist_ok=True)
    secciones = ""
    for i, caso in enumerate(CASOS, start=1):
        secciones += f"""
<section style="border-top:6px solid {caso['color']}">
<div class="wrap">
<span class="badge {'ok' if 'VIABLE' in caso['lectura'] or 'VIABLE' in caso['lectura'].split('La renta')[0] or 'VIABLE' in caso['lectura'] else 'bad'}">Caso {chr(64 + i)}</span>
<h2>{_h(caso['titulo'])}</h2>
<p class="lead">{_h(caso['chip'])} · GFA {caso['gfa']:.0f} m² · CL {_fmt_m(caso['cl'])} M · fecha de datos 2026-08-14</p>
{_resumen_cards(caso)}
{_venta_html(caso)}
{_renta_html(caso)}
{_suelo_html(caso)}
<div class="nota"><b>Lectura del caso:</b> {_h(caso['lectura'])}</div>
</div>
</section>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Presentacion de casos — DiseñoParametrico (2026-08-14)</title>
<style>{_CSS}</style>
</head>
<body>
<div class="hero"><div class="wrap">
<div class="kicker">DiseñoParametrico · Proceso BIM-GIS-AI · Fase 2</div>
<h1>Prefactibilidad y presentacion de casos de estudio</h1>
<div class="sub">Ejercicio de resolucion del proceso completo con lotes reales: tres situaciones
de prueba (norte medio, centro historico y sur) evaluadas en venta y en renta (Build-to-Rent),
con reglas de decision de Bogota 2026 y datos de mercado auditables.</div>
<div class="meta"><span><b>Fecha:</b> 2026-08-14</span><span><b>Moneda:</b> COP</span>
<span><b>Motores:</b> F2_DEMANDA_MOTOR_v01 (venta) + F2_RENTA_MOTOR_v01 (renta)</span>
<span><b>Verificacion:</b> independiente PASS · tests 73/73</span></div>
</div></div>

<section><div class="wrap">
<h2>El proceso (F1 → F5)</h2>
<p class="lead">Cada caso recorre el mismo pipeline: contexto normativo (F1), demanda y modelo
financiero (F2), generacion de masa (F3), analisis ambiental (F4) e inyeccion BIM (F5). Esta
presentacion entrega la resolucion de F1-F2 y el plan de continuacion F3-F5.</p>
<div class="road">
<div class="f hecha"><div class="n">F1</div><div class="t">Contexto</div><div class="s">✅ POT/NSR-10, retiros, envolvente (GFA)</div></div>
<div class="f hecha"><div class="n">F2</div><div class="t">Demanda + financiero</div><div class="s">✅ Venta y renta, KPIs, sensibilidad</div></div>
<div class="f prox"><div class="n">F3</div><div class="t">Masa</div><div class="s">🔶 VOLUM_GENERADOR en Grasshopper</div></div>
<div class="f prox"><div class="n">F4</div><div class="t">Ambiental</div><div class="s">🔶 Ladybug + EPW Bogota</div></div>
<div class="f prox"><div class="n">F5</div><div class="t">BIM</div><div class="s">⏳ Tapir → ArchiCAD</div></div>
</div>
</div></section>
{secciones}
<section class="alt"><div class="wrap">
<h2>Resumen comparativo de la gama de pruebas</h2>
<p class="lead">Tres situaciones deliberadamente distintas para cubrir el espectro de un lote real
de proyecto: escala media en zona de valores medios, escala grande en centro historico turistico y
lote pequeno en zona de valores bajos.</p>
<div class="tabla-scroll"><table>
<tr><th>Caso</th><th>Zona</th><th class="num">Lote (m²)</th><th class="num">GFA (m²)</th><th class="num">CL (M$)</th>
<th>Venta (mejor)</th><th>Renta (mejor)</th><th>Veredicto del ejercicio</th></tr>
<tr><td><b>A — AAA0127AZPA</b></td><td>El Prado, Suba (estrato 3-4)</td><td class="num">450</td><td class="num">1.053</td><td class="num">550</td>
<td>B 18,5% (no viable)</td><td>LP×VIS TIR 11,1% (VIABLE)</td><td><span class="estado ok">Resuelto: renta LP</span></td></tr>
<tr><td><b>B — AAA0030JKOE</b></td><td>La Candelaria (centro historico)</td><td class="num">946</td><td class="num">3.313</td><td class="num">1.420</td>
<td>B 22,3% (VIABLE)</td><td>CP×VIS TIR 12,8% (VIABLE)</td><td><span class="estado ok">Viable en venta y renta</span></td></tr>
<tr><td><b>C — 002407033006</b></td><td>Venecia, Tunjuelito (sur, estrato 2)</td><td class="num">192</td><td class="num">650</td><td class="num">192</td>
<td>A 16,7% (no viable)</td><td>ninguna (suelo soportable $0)</td><td><span class="estado bad">No viable: revalidar o descartar</span></td></tr>
</table></div>
<div class="nota"><b>Conclusion del ejercicio:</b> la gama de pruebas demuestra que el pipeline
distingue correctamente los casos viables de los inviables y que la estrategia de renta (BTR)
amplia la viabilidad frente a la venta en 2 de los 3 casos. El precio del suelo, la escala (GFA)
y los canones de la zona son las palancas que gobiernan el resultado.</div>
</div></section>

<footer><div class="wrap">
Generado por scripts/utilities/generar_presentacion.py — DiseñoParametrico, 2026-08-14.
Fuentes: motores F2 (venta v2.1) y F2 Renta (v1.0) con parametros auditables; datos de mercado
Bogota 2026 (Ciencuadras Q1-2026, FincaRaiz, Properati, Tinsa, DANE) — ver vault
(20-fases/fase-2-demanda, 30-referencia). Documento de ejercicio: validar comparables antes de
decisiones de inversion.
</div></footer>
</body></html>"""

    ruta = os.path.join(OUT, "presentacion_casos_2026-08-14.html")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK presentacion: {ruta} ({len(html)} bytes)")


if __name__ == "__main__":
    generar()
