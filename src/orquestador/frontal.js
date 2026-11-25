/* frontal.js - Vista FRONTAL interactiva del orquestador (nivel 0,00).
   Se usa en index.html (seccion 1d) y en la pagina independiente /frontal. */
(function (global) {
  'use strict';

  var NS = 'http://www.w3.org/2000/svg';
  var PCOL = ['#b42318', '#6d28d9', '#0e7490', '#b45309', '#4d7c0f'];
  var F2 = new Intl.NumberFormat('es-CO', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var F1 = new Intl.NumberFormat('es-CO', { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  var F3 = new Intl.NumberFormat('es-CO', { minimumFractionDigits: 3, maximumFractionDigits: 3 });
  var S = null;
  var FSCALE = 1.15;

  function q(sel, root) { return (root || document).querySelector(sel); }
  function qa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function sv(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]);
    });
    if (parent) parent.appendChild(e);
    return e;
  }
  function line(p, x1, y1, x2, y2, stroke, w, dash, op) {
    return sv('line', { x1: r1(x1), y1: r1(y1), x2: r1(x2), y2: r1(y2), stroke: stroke,
      'stroke-width': w == null ? 1 : w, 'stroke-dasharray': dash || null,
      'stroke-opacity': op == null ? 1 : op, 'stroke-linecap': 'round' }, p);
  }
  function rect(p, x, y, w, h, fill, fo, stroke, sw) {
    return sv('rect', { x: r1(x), y: r1(y), width: Math.max(0, r1(w)), height: Math.max(0, r1(h)),
      fill: fill || 'none', 'fill-opacity': fo == null ? 1 : fo,
      stroke: stroke || null, 'stroke-width': sw == null ? 0 : sw }, p);
  }
  function circle(p, cx, cy, rr, fill, stroke, sw) {
    return sv('circle', { cx: r1(cx), cy: r1(cy), r: rr, fill: fill || 'none',
      stroke: stroke || null, 'stroke-width': sw == null ? 0 : sw }, p);
  }
  function poly(p, pts, stroke, w, dash, fill, fo) {
    var d = pts.map(function (q, i) { return (i ? 'L ' : 'M ') + r1(q[0]) + ' ' + r1(q[1]); }).join(' ');
    return sv('path', { d: d, fill: fill || 'none', 'fill-opacity': fo == null ? 1 : fo,
      stroke: stroke || null, 'stroke-width': w == null ? 1 : w,
      'stroke-dasharray': dash || null, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, p);
  }
  function text(p, x, y, str, o) {
    o = o || {};
    var t = sv('text', { x: r1(x), y: r1(y), 'font-size': (o.size || 11) * FSCALE, fill: o.fill || '#1f2328',
      'text-anchor': o.anchor || 'start', 'font-weight': o.weight || 400,
      'font-family': o.family || null, 'paint-order': o.halo ? 'stroke' : null,
      stroke: o.halo ? '#ffffff' : null, 'stroke-width': o.halo ? (o.haloWidth || 3) : null,
      'stroke-linejoin': o.halo ? 'round' : null, transform: o.transform || null }, p);
    t.textContent = str;
    return t;
  }
  function r1(v) { return Math.round(v * 10) / 10; }
  function f2(v) { return (v == null || !isFinite(v)) ? '—' : F2.format(Number(v)); }
  function f1(v) { return (v == null || !isFinite(v)) ? '—' : F1.format(Number(v)); }
  function f3(v) { return (v == null || !isFinite(v)) ? '—' : F3.format(Number(v)); }
  function parseNum(s) {
    s = String(s == null ? '' : s).trim();
    if (!s) return null;
    if (s.indexOf(',') >= 0) s = s.replace(/\./g, '').replace(',', '.');
    var n = Number(s);
    return isFinite(n) ? n : null;
  }
  function niceStep(raw) {
    if (!isFinite(raw) || raw <= 0) return 1;
    var pow = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10));
    var n = raw / pow;
    var m = n <= 1 ? 1 : n <= 2 ? 2 : n <= 2.5 ? 2.5 : n <= 5 ? 5 : 10;
    return m * pow;
  }
  function pointInPoly(x, y, poly) {
    var dentro = false, n = poly.length, j = n - 1;
    for (var i = 0; i < n; i++) {
      var xi = poly[i][0], yi = poly[i][1], xj = poly[j][0], yj = poly[j][1];
      if (((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / ((yj - yi) || 1e-12) + xi)) dentro = !dentro;
      j = i;
    }
    return dentro;
  }
  function toSvg(svg, ev) {
    var p = svg.createSVGPoint();
    p.x = ev.clientX; p.y = ev.clientY;
    return p.matrixTransform(svg.getScreenCTM().inverse());
  }
  function fmtM(v) { return f2(v) + ' m'; }

  // ------------------------------------------------------------------ esqueleto
  function esqueleto() {
    return '' +
      '<div class="fr-toolbar">' +
        '<div class="fr-tool" style="min-width:190px"><label for="fr-lado">Lado frontal (calle)</label>' +
          '<span id="fr-lado-label" class="fr-lado-fixed">—</span></div>' +
        '<div class="fr-tool fr-grow"><label>Vista</label>' +
          '<select id="fr-vista"><option value="">—</option></select>' +
          '<span class="fr-badge" id="fr-badge">FRONTAL</span>' +
          '<span class="fr-src" id="fr-src"></span></div>' +
        '<div class="fr-tool"><label for="fr-msnm">Nivel 0,00 (MSNM)</label>' +
          '<div class="fr-inline"><input type="text" id="fr-msnm" inputmode="decimal" placeholder="2.634,79">' +
          '<button class="fr-btn primary" id="fr-fijar" type="button">Fijar</button>' +
          '<button class="fr-ghost" id="fr-min" type="button" title="Volver al datum por defecto (mínimo del lote)">Mín. lote</button></div></div>' +
        '<div class="fr-tool"><label>Capas</label>' +
          '<label class="fr-check"><input type="checkbox" id="fr-perfil"> Banda sobre el perfil</label>' +
          '<label class="fr-check"><input type="checkbox" id="fr-ref"> H desde 0,00 (ref.)</label></div>' +
        '<div class="fr-tool"><label>Cotas</label>' +
          '<div class="fr-inline"><button class="fr-ghost" id="fr-mdt" type="button" title="Lee el MDT de Catastro para el lindero y la calle">Actualizar cotas MDT</button>' +
          '<a class="fr-ghost" id="fr-open" target="_blank" rel="noopener" style="text-decoration:none;display:none">Abrir</a></div></div>' +
      '</div>' +
      '<div class="fr-grid">' +
        '<div class="fr-col-plan"><div class="fr-card">' +
          '<div class="fr-card-head"><h4>Planta · marcar puntos</h4><span class="fr-chip" id="fr-max">máx. 5</span></div>' +
          '<div class="fr-plano" id="fr-plano"></div>' +
          '<div class="fr-hint" id="fr-plano-msg">Haga clic dentro del lote para marcar P1…P5. Clic sobre un punto para eliminarlo.</div>' +
          '<div class="fr-puntos" id="fr-puntos"></div>' +
          '<div class="fr-actions"><button class="fr-btn danger" id="fr-reset" type="button">Reiniciar puntos</button></div>' +
        '</div></div>' +
        '<div class="fr-col-alz"><div class="fr-card">' +
          '<div class="fr-card-head"><h4>Alzado desde la calle</h4><span class="fr-readout" id="fr-readout">Pase el cursor para leer cotas · clic para fijar 0,00</span></div>' +
          '<div class="fr-svg" id="fr-svg"></div>' +
          '<div class="fr-leyenda" id="fr-leyenda"></div>' +
          '<div class="fr-notes" id="fr-notes"></div>' +
        '</div></div>' +
      '</div>';
  }

  function placeholder(msg) {
    var p = q('#fr-plano', S.cont), a = q('#fr-svg', S.cont);
    if (p) p.innerHTML = '<div class="fr-loading">' + esc(msg) + '</div>';
    if (a) a.innerHTML = '<div class="fr-loading">' + esc(msg) + '</div>';
    var pt = q('#fr-puntos', S.cont); if (pt) pt.innerHTML = '';
    var le = q('#fr-leyenda', S.cont); if (le) le.innerHTML = '';
    var no = q('#fr-notes', S.cont); if (no) no.innerHTML = '';
    var bd = q('#fr-badge', S.cont); if (bd) bd.textContent = 'FRONTAL';
    var sc = q('#fr-src', S.cont); if (sc) sc.textContent = '';
  }

  function cargando(txt) {
    var p = q('#fr-plano', S.cont), a = q('#fr-svg', S.cont);
    if (p) p.innerHTML = '<div class="fr-loading"><span class="fr-spin"></span>' + esc(txt || 'Calculando vista frontal…') + '</div>';
    if (a) a.innerHTML = '<div class="fr-loading"><span class="fr-spin"></span>' + esc(txt || 'Calculando vista frontal…') + '</div>';
  }

  function error(msg) {
    var p = q('#fr-plano', S.cont), a = q('#fr-svg', S.cont);
    var h = '<div class="fr-err"><b>No se pudo cargar el frontal.</b><br>' + esc(msg) + '</div>';
    if (p) p.innerHTML = h;
    if (a) a.innerHTML = h;
  }

  // ------------------------------------------------------------------- montaje
  function montar(contId, opts) {
    opts = opts || {};
    var cont = document.getElementById(contId);
    if (!cont) return;
    S = { cont: cont, chip: opts.chip || null, lado: null, mdt: 'malla', data: null,
      perfil: false, refH: false, busy: false, msg: '', standalone: !!opts.standalone };
    cont.innerHTML = esqueleto();
    bind();
    if (S.chip) cargar(false);
    else placeholder('Seleccione un CHIP para ver la vista frontal.');
  }

  function setChip(chip) {
    if (!S) return;
    chip = (chip || '').trim().toUpperCase();
    if (S.chip === chip) return;
    S.chip = chip; S.lado = null; S.data = null; S.msg = '';
    var inp = q('#fr-msnm', S.cont); if (inp) inp.value = '';
    if (!chip) { placeholder('Seleccione un CHIP para ver la vista frontal.'); return; }
    cargar(false);
  }

  function bind() {
    var c = S.cont;
    q('#fr-vista', c).addEventListener('change', function () {
      var v = this.value;
      S.lado = v === '' ? null : parseInt(v, 10);
      cargar(false);
    });
    q('#fr-fijar', c).addEventListener('click', fijarMSNM);
    q('#fr-msnm', c).addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); fijarMSNM(); }
    });
    q('#fr-min', c).addEventListener('click', function () {
      if (!S.data) return;
      fijarDatum(S.data.lote_min_z, S.data.datum.x_frente_m, null, 'min_lote');
    });
    q('#fr-perfil', c).addEventListener('change', function () {
      S.perfil = this.checked; if (S.data) renderAlzado();
    });
    q('#fr-ref', c).addEventListener('change', function () {
      S.refH = this.checked; if (S.data) renderAlzado();
    });
    q('#fr-mdt', c).addEventListener('click', function () { actualizarMDT(); });
    q('#fr-reset', c).addEventListener('click', reiniciar);
    q('#fr-puntos', c).addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-del]');
      if (b) { quitarPunto(b.getAttribute('data-del')); return; }
      var u = ev.target.closest('[data-use]');
      if (u) {
        var id = u.getAttribute('data-use');
        var p = (S.data.puntos || []).filter(function (x) { return x.id === id; })[0];
        if (p && p.z != null) fijarDatum(p.z, p.xf, p.id, 'manual');
      }
    });
    q('#fr-puntos', c).addEventListener('change', function (ev) {
      var inp = ev.target.closest('[data-h]');
      if (!inp) return;
      var id = inp.getAttribute('data-h');
      var v = parseNum(inp.value);
      if (v == null || v <= 0) { renderPuntos(); return; }
      var alturas = alturasActuales();
      alturas[id] = v;
      guardarPuntos(S.data.puntos, alturas);
    });
  }

  async function cargar(regen) {
    if (!S || !S.chip) return;
    S.busy = true;
    cargando();
    var url = '/api/frontal?chip=' + encodeURIComponent(S.chip) +
      (S.lado != null ? '&lado=' + encodeURIComponent(S.lado) : '') +
      '&mdt=' + encodeURIComponent(S.mdt) + (regen ? '&regen=1' : '');
    var r;
    try { r = await fetch(url).then(function (x) { return x.json(); }); }
    catch (e) { r = { ok: false, error: String(e) }; }
    S.busy = false;
    if (!r || !r.ok || !r.frontal) { error((r && (r.error || r.mensaje)) || 'sin datos'); return; }
    S.data = r.frontal;
    if (S.lado == null) S.lado = S.data.frente.lado_id;
    renderTodo();
  }

  function renderTodo() {
    if (!S.data) return;
    renderToolbar();
    renderPlano();
    renderPuntos();
    renderAlzado();
    renderLeyenda();
    renderNotas();
  }

  // ------------------------------------------------------------------ toolbar
  function renderToolbar() {
    var d = S.data, c = S.cont;
    var lbl = q('#fr-lado-label', c);
    if (lbl) lbl.textContent = (d.frente.cardinal_label || d.frente.cardinal || 'lado ' + d.frente.lado_id) +
      ' · ' + d.frente.etiqueta + ' · ' + f2(d.frente.largo_m) + ' m';
    var sel = q('#fr-vista', c);
    var actual = String(d.frente.lado_id);
    sel.innerHTML = '';
    (d.lados || []).forEach(function (l) {
      var o = document.createElement('option');
      o.value = String(l.lado_id);
      o.textContent = (l.cardinal_label || l.cardinal || 'lado ' + l.lado_id) +
        ' · ' + l.etiqueta + ' · ' + f1(l.longitud_m) + ' m';
      sel.appendChild(o);
    });
    sel.value = actual;
    q('#fr-badge', c).textContent = 'Vista lado del predio · ' + (d.frente.cardinal_label || d.frente.etiqueta || ('lado ' + d.frente.lado_id)) +
      ' · ' + f2(d.frente.largo_m) + ' m';
    var fuentes = [];
    if (d.frente.via_cercana) fuentes.push('vía ' + d.frente.via_cercana);
    fuentes.push(d.frente.origen);
    fuentes.push(d.mdt.metodo);
    q('#fr-src', c).textContent = fuentes.join(' · ');
    var inp = q('#fr-msnm', c);
    if (document.activeElement !== inp) inp.value = f2(d.datum.z0_msnm);
    q('#fr-max', c).textContent = 'máx. ' + (d.max_puntos || 5);
    var btn = q('#fr-mdt', c);
    btn.textContent = /REST|cache/i.test(d.mdt.metodo) ? 'Recalcular cotas MDT' : 'Actualizar cotas MDT';
    var a = q('#fr-open', c);
    if (S.standalone) { a.style.display = 'none'; }
    else { a.style.display = ''; a.href = '/frontal?chip=' + encodeURIComponent(d.chip); }
  }

  // -------------------------------------------------------------------- planta
  function renderPlano() {
    var d = S.data, cont = q('#fr-plano', S.cont);
    var pl = d.plano;
    var bb = pl.bbox;
    var pad = 7.0;
    var x0 = bb[0] - pad, y0 = bb[1] - pad, x1 = bb[2] + pad, y1 = bb[3] + pad;
    var w = x1 - x0, h = y1 - y0;
    cont.innerHTML = '';
    var svg = sv('svg', { viewBox: x0 + ' ' + (-y1) + ' ' + w + ' ' + h,
      preserveAspectRatio: 'xMidYMid meet', role: 'img',
      'aria-label': 'Planta del lote para marcar puntos' }, cont);
    rect(svg, x0, -y1, w, h, '#fbfcfc', 1);

    // vecinos
    (pl.vecinos || []).forEach(function (v) {
      poly(svg, v.anillo.map(function (p) { return [p[0], -p[1]]; }), v.color, 0.12,
        null, v.color, 0.16);
    });
    // lote
    poly(svg, pl.lote.map(function (p) { return [p[0], -p[1]]; }), '#111827', 0.4, null, '#ffffff', 0.92);
    // lados con el color de la planta
    (pl.lados || []).forEach(function (l) {
      var pts = l.polyline.map(function (p) { return [p[0], -p[1]]; });
      poly(svg, pts, l.color, l.es_frente ? 1.5 : 1.0, null, null, 0);
    });
    // flecha de vista desde la calle
    var fr = pl.frente;
    var mid = [(fr.p0[0] + fr.p1[0]) / 2, (fr.p0[1] + fr.p1[1]) / 2];
    var n = fr.normal;
    var L = 4.6;
    var tip = [mid[0] - n[0] * L, mid[1] - n[1] * L];
    line(svg, mid[0] + n[0] * 4.4, -mid[1] - n[1] * 4.4, tip[0], -tip[1], fr.color, 0.7, '2 1.4');
    var tri = sv('polygon', { fill: fr.color, points:
      [tip[0], -tip[1]].join(',') + ' ' +
      [tip[0] + n[0] * 2.0 + (-n[1]) * 0.9, -(tip[1] + n[1] * 2.0 + n[0] * 0.9)].join(',') + ' ' +
      [tip[0] + n[0] * 2.0 - (-n[1]) * 0.9, -(tip[1] + n[1] * 2.0 - n[0] * 0.9)].join(',') }, svg);
    text(svg, mid[0] + n[0] * 5.7, -(mid[1] + n[1] * 5.7) - 0.2, 'FRONTAL',
      { size: 2.2, weight: 700, fill: fr.color, anchor: 'middle', halo: true, haloWidth: 0.7 });

    // puntos
    var pts = d.puntos || [];
    pts.forEach(function (p, i) {
      var g = sv('g', { 'data-punto': p.id, style: 'cursor:pointer' }, svg);
      sv('title', { 'data-x': null }, g).textContent = p.id + ' · clic para eliminar';
      circle(g, p.x, -p.y, 1.25, p.color, '#ffffff', 0.3);
      text(g, p.x + 1.8, -p.y + 0.7 + (i % 3) * 1.9, p.id,
        { size: 2.0, weight: 700, fill: p.color, halo: true, haloWidth: 0.55 });
    });

    // interaccion
    svg.addEventListener('click', function (ev) {
      if (ev.target.closest('[data-punto]')) return;
      var q = toSvg(svg, ev);
      var x = q.x, y = -q.y;
      if (!pointInPoly(x, y, pl.lote)) {
        msgPlano('El punto debe quedar dentro del lote.');
        return;
      }
      agregarPunto(x, y);
    });
    msgPlano('Haga clic dentro del lote para marcar P1…P5. Clic sobre un punto para eliminarlo.');
  }

  function msgPlano(t) {
    var e = q('#fr-plano-msg', S.cont);
    if (e) e.textContent = t;
  }

  // -------------------------------------------------------------------- puntos
  function alturasActuales() {
    var out = {};
    ((S.data && S.data.puntos) || []).forEach(function (p) {
      if (p.h_manual) out[p.id] = p.h_m;
    });
    return out;
  }

  function renderPuntos() {
    var cont = q('#fr-puntos', S.cont);
    var pts = (S.data.puntos || []);
    if (!pts.length) {
      cont.innerHTML = '<div class="fr-empty">Sin puntos marcados. Cada punto se proyecta a la fachada con su línea de altura permitida.</div>';
      return;
    }
    var h = '<table class="fr-ptab"><thead><tr><th>Punto</th><th class="num" title="Cota del terreno en el punto (MSNM)">MSNM</th>' +
      '<th class="num">H (m)</th><th></th></tr></thead><tbody>';
    pts.forEach(function (p) {
      h += '<tr>' +
        '<td title="x=' + f2(p.x) + ' · y=' + f2(p.y) + ' · xf=' + f2(p.xf) + ' m">' +
          '<span class="fr-dot" style="background:' + p.color + '"></span><b>' + esc(p.id) + '</b>' +
          (p.h_manual ? ' <span style="color:#96620f" title="altura manual">*</span>' : '') + '</td>' +
        '<td class="num">' + f2(p.msnm) + '</td>' +
        '<td class="num"><input data-h="' + esc(p.id) + '" value="' + f2(p.h_m) + '" step="0.01" inputmode="decimal" title="Altura máxima permitida en este punto (m)"></td>' +
        '<td style="white-space:nowrap;text-align:right"><button class="fr-mini" data-use="' + esc(p.id) + '" title="Fijar el 0,00 en este punto">0,00</button>' +
        '<button class="fr-mini x" data-del="' + esc(p.id) + '" title="Quitar">&times;</button></td>' +
      '</tr>';
    });
    h += '</tbody></table>';
    cont.innerHTML = h;
  }

  async function agregarPunto(x, y) {
    if (S.busy) return;
    var pts = (S.data.puntos || []).slice();
    if (pts.length >= (S.data.max_puntos || 5)) {
      msgPlano('Máximo ' + (S.data.max_puntos || 5) + ' puntos. Use "Reiniciar puntos" para marcar otros.');
      return;
    }
    var usados = {};
    pts.forEach(function (p) { usados[p.id] = 1; });
    var id = null;
    for (var i = 1; i <= (S.data.max_puntos || 5); i++) {
      if (!usados['P' + i]) { id = 'P' + i; break; }
    }
    if (!id) return;
    pts.push({ id: id, x: x, y: y });
    await guardarPuntos(pts, alturasActuales());
  }

  async function quitarPunto(id) {
    if (S.busy) return;
    var pts = (S.data.puntos || []).filter(function (p) { return p.id !== id; });
    var alts = alturasActuales();
    delete alts[id];
    await guardarPuntos(pts, alts);
  }

  async function reiniciar() {
    if (S.busy || !S.data) return;
    var n = (S.data.puntos || []).length;
    if (!n) { msgPlano('No hay puntos que reiniciar.'); return; }
    if (!global.confirm('¿Reiniciar los ' + n + ' puntos marcados?')) return;
    await guardarPuntos([], {});
    msgPlano('Puntos reiniciados. Haga clic dentro del lote para marcar de nuevo.');
  }

  async function guardarPuntos(pts, alturas) {
    if (!S || !S.chip) return;
    S.busy = true;
    var body = { chip: S.chip, lado: S.lado, mdt: S.mdt,
      puntos: (pts || []).map(function (p) { return { id: p.id, x: p.x, y: p.y }; }),
      alturas: alturas || {} };
    var r;
    try {
      r = await fetch('/api/frontal/puntos', { method: 'POST',
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
        .then(function (x) { return x.json(); });
    } catch (e) { r = { ok: false, error: String(e) }; }
    S.busy = false;
    if (!r || !r.ok || !r.frontal) {
      msgPlano('No se pudieron guardar los puntos: ' + ((r && (r.error || r.mensaje)) || 'error'));
      return;
    }
    S.data = r.frontal;
    renderTodo();
  }

  async function fijarDatum(z, xf, puntoId, modo) {
    if (!S || !S.data || S.busy) return;
    if (z == null || !isFinite(z)) return;
    S.busy = true;
    var body = { chip: S.chip, z0_m: z, modo: modo || 'manual', origen: 'frontal',
      x_frente_m: xf == null ? S.data.datum.x_frente_m : xf };
    if (puntoId) body.punto_id = puntoId;
    var r;
    try {
      r = await fetch('/api/z0', { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body) }).then(function (x) { return x.json(); });
    } catch (e) { r = { ok: false, error: String(e) }; }
    S.busy = false;
    if (!r || !r.ok) {
      S.msg = 'No se pudo fijar el 0,00: ' + ((r && (r.error || r.mensaje)) || 'error');
      renderNotas();
      return;
    }
    S.msg = '0,00 fijado en ' + f2(r.z0_msnm) + ' msnm';
    await cargar(true);
  }

  function fijarMSNM() {
    if (!S.data) return;
    var v = parseNum(q('#fr-msnm', S.cont).value);
    if (v == null) { S.msg = 'Escriba un número válido en MSNM.'; renderNotas(); return; }
    var z = v - S.data.msnm.z_ref_m;
    fijarDatum(z, S.data.datum.x_frente_m, null, 'manual');
  }

  async function actualizarMDT() {
    if (!S || !S.chip || S.busy) return;
    S.mdt = 'rest';
    S.msg = 'Leyendo cotas del MDT de Catastro. Puede tardar hasta 30 s…';
    renderNotas();
    await cargar(true);
    if (S.data && /REST|cache/i.test(S.data.mdt.metodo)) S.mdt = 'malla';
    if (S.data && !/REST|cache/i.test(S.data.mdt.metodo)) {
      S.msg = 'No se pudo leer el MDT de Catastro; se mantiene la malla ETAPA1.';
    } else {
      S.msg = '';
    }
    if (S.data) renderNotas();
  }

  // -------------------------------------------------------------------- alzado
  function renderAlzado() {
    var d = S.data, cont = q('#fr-svg', S.cont);
    if (!d) return;
    var W = 1180, H = 640;
    var M = { l: 104, r: 168, t: 64, b: 82 };
    var wp = W - M.l - M.r, hp = H - M.t - M.b;
    var dom = d.x_rango;
    var x0 = dom[0], x1 = dom[1];
    var zr = d.msnm.z_ref_m;
    var vals = [];
    function add(v) { if (v != null && isFinite(v)) vals.push(Number(v)); }
    (d.lindero || []).forEach(function (p) { add(p.z); });
    (d.calle || []).forEach(function (p) { add(p.z); });
    (d.curvas || []).forEach(function (c) { add(c.z); });
    (d.esquinas || []).forEach(function (e) { add(e.z); });
    (d.silueta || []).forEach(function (s) { add(s.z_base); add(s.z_top); });
    (d.vecinos || []).forEach(function (v) { add(v.z_base); add(v.z_top); });
    (d.puntos || []).forEach(function (p) { add(p.z); add(p.z_top); });
    add(d.datum.z0_m); add(d.banda.base_z); add(d.banda.top_z);
    if (S.refH) add(d.datum.z0_m + d.altura.h_m);
    if (!vals.length) { error('Sin cotas para dibujar.'); return; }
    var zmin = Math.min.apply(null, vals), zmax = Math.max.apply(null, vals);
    var pad = Math.max(1.2, (zmax - zmin) * 0.07);
    zmin -= pad; zmax += pad;
    if (!(zmax - zmin > 2)) { zmin -= 2; zmax += 2; }

    function X(xf) { return M.l + (xf - x0) / (x1 - x0) * wp; }
    function Y(z) { return M.t + hp - (z - zmin) / (zmax - zmin) * hp; }
    function XD(v, lim) { return X(Math.max(x0, Math.min(x1, v))); }

    cont.innerHTML = '';
    var svg = sv('svg', { viewBox: '0 0 ' + W + ' ' + H, width: '100%',
      preserveAspectRatio: 'xMidYMid meet', role: 'img',
      'aria-label': 'Vista frontal del lote desde la calle' }, cont);
    rect(svg, 0, 0, W, H, '#ffffff', 1);
    rect(svg, M.l, M.t, wp, hp, '#fbfcfa', 1);

    // --- silueta del terreno (envolvente min-max por franja)
    var sil = (d.silueta || []).filter(function (s) { return isFinite(s.z_top) && isFinite(s.z_base); });
    if (sil.length > 1) {
      var ptsTop = sil.map(function (s) { return [X(s.xf), Y(s.z_top)]; });
      var ptsBase = sil.slice().reverse().map(function (s) { return [X(s.xf), Y(s.z_base)]; });
      poly(svg, ptsTop.concat(ptsBase), 'none', 0, null, '#efeade', 0.55);
    }

    // --- curvas de nivel (MSNM)
    (d.curvas || []).forEach(function (c) {
      var y = Y(c.z);
      if (y < M.t - 2 || y > M.t + hp + 2) return;
      var col = c.mayor ? '#bcae86' : '#ddd3bd';
      (c.tramos || []).forEach(function (t) {
        line(svg, XD(t[0]), y, XD(t[1]), y, col, c.mayor ? 1.0 : 0.7, null, c.mayor ? 0.95 : 0.55);
      });
      if (c.mayor) {
        var bx = Math.max.apply(null, c.tramos.map(function (t) { return t[1]; }));
        text(svg, XD(bx) - 3, y - 2.5, f2(c.msnm), { size: 8.4, fill: '#8a7a55', anchor: 'end', halo: true, haloWidth: 2.4 });
      }
    });

    // --- vecinos
    (d.vecinos || []).slice().sort(function (a, b) { return a.prof - b.prof; }).forEach(function (v) {
      var xa = Math.max(v.x0, x0), xb = Math.min(v.x1, x1);
      if (xb - xa < 0.2) return;
      var lat = v.rol === 'lateral_izq' || v.rol === 'lateral_der';
      var yT = Y(v.z_top), yB = Y(v.z_base);
      rect(svg, X(xa), Math.max(M.t, yT), X(xb) - X(xa), Math.min(M.t + hp, yB) - Math.max(M.t, yT),
        v.color, lat ? 0.18 : 0.09, v.color, lat ? 0.9 : 0.5);
      if (v.h != null && isFinite(v.h)) {
        var mx = (X(xa) + X(xb)) / 2;
        text(svg, mx, Math.max(M.t + 11, yT - 6), 'h ' + f2(v.h) + ' m',
          { size: 10.2, weight: 700, fill: '#374151', anchor: 'middle', halo: true });
        text(svg, mx, Math.max(M.t + 22, yT + 9), f2(v.z_top + zr) + ' msnm',
          { size: 8.8, fill: '#6b7280', anchor: 'middle', halo: true, haloWidth: 2.4 });
      }
    });

    // --- calle
    var calle = (d.calle || []).filter(function (p) { return p.z != null; });
    if (calle.length > 1) {
      var fillPts = calle.map(function (p) { return [X(p.xf), Y(p.z)]; });
      fillPts.push([X(calle[calle.length - 1].xf), Y(zmin)], [X(calle[0].xf), Y(zmin)]);
      poly(svg, fillPts, 'none', 0, null, '#e7eaec', 0.9);
      var est = calle.filter(function (p) { return p.estimado; }).length;
      var dash = est > calle.length * 0.5 ? '5 3' : null;
      poly(svg, calle.map(function (p) { return [X(p.xf), Y(p.z)]; }), '#1f6feb', 2.6, dash);
      var zc = calle.reduce(function (a, p) { return a + p.z; }, 0) / calle.length;
      text(svg, XD(calle[0].xf) + 4, Y(zc) - 7, 'calle', { size: 10, weight: 700, fill: '#1f6feb', halo: true });
      text(svg, XD(calle[calle.length - 1].xf) - 4, Y(zc) - 7,
        f2(d.perfil.calle_min + zr) + '–' + f2(d.perfil.calle_max + zr) + ' msnm',
        { size: 8.8, fill: '#1f6feb', anchor: 'end', halo: true });
    }

    // --- perimetro del lote (colores de la planta)
    var loteXmin = Math.min.apply(null, d.lote_x), loteXmax = Math.max.apply(null, d.lote_x);
    (d.lados || []).forEach(function (l) {
      var pts = (l.polyline_xz || []).map(function (p) { return [X(p[0]), Y(p[1])]; });
      if (pts.length < 2) return;
      poly(svg, pts, l.color, l.lado_id === d.frente.lado_id ? 3.0 : 2.0, null);
      if (l.lado_id === d.frente.lado_id) {
        var mid = pts[Math.floor(pts.length / 2)];
        text(svg, mid[0], mid[1] + 14, 'FRONTAL',
          { size: 10, weight: 700, fill: l.color, anchor: 'middle', halo: true });
      }
    });

    // --- esquinas del poligono (niveles)
    (d.esquinas || []).forEach(function (e, i) {
      var cx = X(e.xf), cy = Y(e.z);
      circle(svg, cx, cy, 3, '#ffffff', e.rol === 'fondo' ? '#6b7280' : '#111827', 1.1);
      var anchor = e.rol === 'izq' ? 'end' : (e.rol === 'der' ? 'start' : 'middle');
      var dx = e.rol === 'izq' ? -5 : (e.rol === 'der' ? 5 : 0);
      var ly = cy - 7 - (i % 2) * 11;
      text(svg, cx + dx, ly, f2(e.msnm), { size: 8.8, fill: '#374151', anchor: anchor, halo: true, haloWidth: 2.4 });
    });

    // --- banda de altura permitida SOBRE EL TERRENO
    var b = d.banda, h = d.altura.h_m;
    if (S.perfil) {
      var lp = (d.lindero || []).filter(function (p) { return p.z != null; });
      if (lp.length > 1) {
        var arriba = lp.map(function (p) { return [X(p.xf), Y(p.z + h)]; });
        var abajo = lp.slice().reverse().map(function (p) { return [X(p.xf), Y(p.z)]; });
        poly(svg, arriba.concat(abajo), 'none', 0, null, '#6b7280', 0.14);
        poly(svg, arriba, '#4b5563', 1.5, '6 4');
        text(svg, XD(lp[0].xf) + 5, Y(lp[0].z + h) - 6, 'H = ' + f2(h) + ' m sobre el perfil del terreno',
          { size: 10, weight: 700, fill: '#374151', halo: true });
      }
    } else {
      var xa = X(loteXmin), xb = X(loteXmax);
      rect(svg, xa, Y(b.top_z), xb - xa, Y(b.base_z) - Y(b.top_z), '#6b7280', 0.20, '#9ca3af', 0.8);
      line(svg, xa, Y(b.top_z), xb, Y(b.top_z), '#4b5563', 1.5, '6 4');
      line(svg, xa, Y(b.base_z), xb, Y(b.base_z), '#6b7280', 1.0, '2 3');
      text(svg, xa + 5, Y(b.top_z) - 6, 'H = ' + f2(h) + ' m sobre el terreno',
        { size: 10, weight: 700, fill: '#374151', halo: true });
      text(svg, xb - 4, Y(b.top_z) + 12, f2(b.top_msnm) + ' msnm',
        { size: 8.8, fill: '#4b5563', anchor: 'end', halo: true });
      // corchete de H en el borde derecho del lote
      var xbr = xb - 9;
      line(svg, xbr, Y(b.base_z), xbr, Y(b.top_z), '#4b5563', 1.2);
      [Y(b.base_z), Y(b.top_z)].forEach(function (yy) { line(svg, xbr - 4, yy, xbr + 4, yy, '#4b5563', 1.2); });
      text(svg, xbr - 3, (Y(b.base_z) + Y(b.top_z)) / 2, f2(h) + ' m',
        { size: 8.8, fill: '#4b5563', anchor: 'middle', halo: true, transform: 'rotate(-90 ' + r1(xbr - 3) + ' ' + r1((Y(b.base_z) + Y(b.top_z)) / 2) + ')' });
    }

    // --- referencia H desde 0,00
    if (S.refH) {
      var zr2 = d.datum.z0_m + h;
      line(svg, M.l, Y(zr2), M.l + wp, Y(zr2), '#b42318', 1.2, '8 4', 0.8);
      text(svg, M.l + wp - 4, Y(zr2) - 4, 'H desde 0,00 (ref.) = ' + f2(zr2 + zr) + ' msnm',
        { size: 9, fill: '#b42318', anchor: 'end', halo: true });
    }

    // --- puntos marcados en planta
    (d.puntos || []).forEach(function (p, i) {
      if (p.z == null || p.z_top == null) return;
      var xp = X(p.xf);
      line(svg, xp, Y(p.z), xp, Y(p.z_top), p.color, 2.2);
      line(svg, xp - 5, Y(p.z_top), xp + 5, Y(p.z_top), p.color, 2.2);
      circle(svg, xp, Y(p.z), 3.6, '#ffffff', p.color, 1.6);
      text(svg, xp, Y(p.z_top) - 8 - (i % 3) * 13,
        p.id + ' · H ' + f2(p.h_m) + ' m' + (p.h_manual ? ' *' : ''),
        { size: 10, weight: 700, fill: p.color, anchor: 'middle', halo: true });
      text(svg, xp + 6, Y(p.z) + 12, f2(p.msnm), { size: 8.8, fill: '#374151', halo: true, haloWidth: 2.4 });
    });

    // --- datum 0,00
    var y0 = Y(d.datum.z0_m);
    line(svg, M.l, y0, M.l + wp, y0, '#b8860b', 3.0);
    text(svg, M.l + wp + 8, y0 + 4, '0,00 (L 01) = ' + f2(d.datum.z0_msnm) + ' msnm',
      { size: 11.2, weight: 700, fill: '#8a5a00' });
    text(svg, M.l + wp + 8, y0 + 18, 'modo: ' + (d.datum.modo || '—'),
      { size: 9.2, fill: '#8a5a00' });

    // --- delta entre 0,00 y el terreno que manda la norma
    if (Math.abs(b.delta_vs_z0_m) > 0.02) {
      var xd = X(b.x_frente_m);
      line(svg, xd, y0, xd, Y(b.base_z), '#6b7280', 1.2, '2 3');
      line(svg, xd - 4, y0, xd + 4, y0, '#6b7280', 1.2);
      line(svg, xd - 4, Y(b.base_z), xd + 4, Y(b.base_z), '#6b7280', 1.2);
      text(svg, xd + 7, (y0 + Y(b.base_z)) / 2 + 3, 'Δ ' + f2(Math.abs(b.delta_vs_z0_m)) + ' m',
        { size: 9, fill: '#4b5563', halo: true });
    }

    // --- rejilla y ejes
    var paso = niceStep((zmax - zmin) / 8);
    var z = Math.ceil(zmin / paso) * paso;
    while (z <= zmax + 1e-6) {
      var yy = Y(z);
      line(svg, M.l, yy, M.l + wp, yy, '#e3e7ee', 0.8);
      text(svg, M.l - 10, yy + 3.5, f2(z + zr), { size: 10.2, fill: '#374151', anchor: 'end' });
      text(svg, W - 6, yy + 3.5, f1(z), { size: 8.8, fill: '#9aa4a2', anchor: 'end' });
      z += paso;
    }
    var px = Math.ceil(x0 / 5) * 5;
    while (px <= x1) {
      var xx = X(px);
      line(svg, xx, M.t, xx, M.t + hp, '#eef2f0', 0.7);
      text(svg, xx, M.t + hp + 15, (px === 0 ? '0' : f1(px)), { size: 9, fill: '#8a9492', anchor: 'middle' });
      px += 5;
    }
    line(svg, M.l, M.t, M.l, M.t + hp, '#c8d2cf', 1);
    line(svg, M.l, M.t + hp, M.l + wp, M.t + hp, '#c8d2cf', 1);
    text(svg, M.l - 10, M.t - 12, 'MSNM', { size: 9, weight: 700, fill: '#5c6b69', anchor: 'end' });
    text(svg, W - 8, M.t - 12, 'z local (m)', { size: 9, fill: '#9aa4a2', anchor: 'end' });
    text(svg, M.l + wp / 2, M.t + hp + 36, 'metros sobre el frente (vista desde la calle)',
      { size: 9.5, fill: '#8a9492', anchor: 'middle' });

    // --- titulo
    text(svg, M.l, 26, 'Vista lado del predio · ' + (d.frente.cardinal_label || d.frente.etiqueta || '') + ' · frente ' + f2(d.frente.largo_m) + ' m',
      { size: 14.5, weight: 700, fill: '#15201f' });
    text(svg, M.l, 43, 'msnm = z local + ' + f3(zr) + ' m · ' + d.mdt.metodo,
      { size: 10, fill: '#6b7280' });

    // --- escala grafica
    var esc = 10, xe0 = M.l + 14;
    var xe1 = xe0 + esc / (x1 - x0) * wp;
    var ye = M.t + hp - 16;
    line(svg, xe0, ye, xe1, ye, '#3a3f46', 1.6);
    line(svg, xe0, ye - 4, xe0, ye + 4, '#3a3f46', 1.6);
    line(svg, xe1, ye - 4, xe1, ye + 4, '#3a3f46', 1.6);
    text(svg, (xe0 + xe1) / 2, ye - 7, esc + ' m', { size: 9, fill: '#3a3f46', anchor: 'middle' });

    // --- interaccion
    var cross = sv('g', { 'pointer-events': 'none', opacity: 0 }, svg);
    var chH = line(cross, M.l, 0, M.l + wp, 0, '#96620f', 1, '3 3', 0.55);
    var chV = line(cross, 0, M.t, 0, M.t + hp, '#96620f', 1, '3 3', 0.55);
    var chD = circle(cross, 0, 0, 3.2, '#96620f', '#ffffff', 1);

    function paintCross(px, py) {
      chH.setAttribute('y1', r1(py)); chH.setAttribute('y2', r1(py));
      chV.setAttribute('x1', r1(px)); chV.setAttribute('x2', r1(px));
      chD.setAttribute('cx', r1(px)); chD.setAttribute('cy', r1(py));
    }
    svg.addEventListener('mousemove', function (ev) {
      var p = toSvg(svg, ev);
      if (p.x < M.l || p.x > M.l + wp || p.y < M.t || p.y > M.t + hp) {
        cross.setAttribute('opacity', 0); return;
      }
      var xf = x0 + (p.x - M.l) / wp * (x1 - x0);
      var zz = zmin + (1 - (p.y - M.t) / hp) * (zmax - zmin);
      cross.setAttribute('opacity', 1);
      paintCross(p.x, p.y);
      var ro = q('#fr-readout', S.cont);
      if (ro) ro.innerHTML = 'x <b>' + f2(xf) + ' m</b> · <b>' + f2(zz + zr) + ' msnm</b> · clic para fijar 0,00';
    });
    svg.addEventListener('mouseleave', function () {
      cross.setAttribute('opacity', 0);
      var ro = q('#fr-readout', S.cont);
      if (ro) ro.textContent = 'Pase el cursor para leer cotas · clic para fijar 0,00';
    });
    svg.addEventListener('click', function (ev) {
      var p = toSvg(svg, ev);
      if (p.x < M.l || p.x > M.l + wp || p.y < M.t || p.y > M.t + hp) return;
      var xf = x0 + (p.x - M.l) / wp * (x1 - x0);
      var zz = zmin + (1 - (p.y - M.t) / hp) * (zmax - zmin);
      fijarDatum(zz, xf, null, 'manual');
    });
  }

  // ------------------------------------------------------------------- leyenda
  function renderLeyenda() {
    var d = S.data, cont = q('#fr-leyenda', S.cont);
    var col = d.frente.color || '#2563eb';
    var items = [
      ['#1f6feb', 'calle'],
      ['#2da44e', 'lindero / terreno'],
      [col, 'perímetro del lote (color de la planta)'],
      ['#6b7280', 'banda H sobre terreno'],
      ['#b8860b', '0,00 del proyecto'],
      ['#b9a97f', 'curvas de nivel (MSNM)']
    ];
    cont.innerHTML = items.map(function (it) {
      return '<span><i class="fr-sw" style="background:' + it[0] + '"></i>' + esc(it[1]) + '</span>';
    }).join('') +
      '<span><i class="fr-dot" style="background:' + PCOL[0] + '"></i>' +
      '<i class="fr-dot" style="background:' + PCOL[1] + '"></i>' +
      '<i class="fr-dot" style="background:' + PCOL[2] + '"></i> P1…P5 (* H manual)</span>';
  }

  // -------------------------------------------------------------------- notas
  function renderNotas() {
    var d = S.data, cont = q('#fr-notes', S.cont);
    if (!d) return;
    var b = d.banda;
    var avisos = (d.avisos || []).map(function (a) { return '<div class="fr-warn">' + esc(a) + '</div>'; }).join('');
    var ref = d.altura.referencia_m;
    var extra = (ref && Math.abs(Number(ref) - Number(d.altura.h_m)) > 0.01)
      ? ' Referencia PZCB: ' + f2(ref) + ' m (no es la altura aplicada).' : '';
    cont.innerHTML =
      '<div><b>0,00 del proyecto</b> = ' + f2(d.datum.z0_msnm) + ' msnm · modo <b>' +
        esc(d.datum.modo || '—') + '</b>. En ArchiCAD es el Ground Floor (L 01 = 0,000).</div>' +
      '<div><b>Banda gris</b> = ' + f2(d.altura.h_m) + ' m sobre el terreno: ' +
        f2(b.base_msnm) + ' → ' + f2(b.top_msnm) + ' msnm. El terreno en ese punto está ' +
        f2(Math.abs(b.delta_vs_z0_m)) + ' m ' + (b.delta_vs_z0_m >= 0 ? 'por encima' : 'por debajo') +
        ' del 0,00; por eso la banda NO arranca en el 0,00.</div>' +
      '<div>Fuente de H: ' + esc(d.altura.fuente || '—') + '.' + (d.altura.tratamiento ? ' Tratamiento: ' + esc(d.altura.tratamiento) + '.' : '') + extra + '</div>' +
      '<div>Cotización: ' + esc(d.mdt.metodo) + '. Vecinos leídos de ' + esc(d.fuentes.vecinos) +
        (d.vecinos_sin_altura ? ' (' + d.vecinos_sin_altura + ' sin altura, no dibujados)' : '') + '.</div>' +
      (S.msg ? '<div class="fr-warn">' + esc(S.msg) + '</div>' : '') + avisos;
  }

  global.Frontal = { montar: montar, setChip: setChip,
    recargar: function () { if (S && S.chip) cargar(true); } };

})(window);

