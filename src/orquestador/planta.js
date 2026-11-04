/* planta.js - Sección 1e: Planta (bloques y cotas MDT)
   Replica EXACTAMENTE la estructura, escala y distribución de la sección 1d (frontal.js).
   - Izquierda: planta del lote (bbox ±25 m oriente/occidente), lote, vecinos por lado, bloques "Bloque 1..n"
     con colores, lados coloreados de planta, lista inferior MSN/diferencias desde 0,00.
   - Derecha: sección transversal W=1180×H=640, mismo estilo que el alzado de la 1d.
   Todo en MSNM (rango Z ~25 m, igual que la 1d). */
(function (global) {
  'use strict';

  var NS = 'http://www.w3.org/2000/svg';
  var PCOL = ['#1f6feb', '#0e7490', '#b45309', '#4d7c0f', '#6d28d9', '#b42318', '#16a34a', '#d97706', '#64748b', '#0891b2'];
  var COL_LOTE = '#111827';
  var COL_LOTE_FILL = '#ffffff';
  var COL_VECINO = '#9ca3af';
  var COL_CALLE = '#1f6feb';
  var Z0_MSNM = 2634.52; // nivel 0,00 establecido (L 01 en ArchiCAD)
  var F2 = new Intl.NumberFormat('es-CO', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var F1 = new Intl.NumberFormat('es-CO', { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  var FSCALE = 1.15;
  var S = null;

  function q(sel, root) { return (root || document).querySelector(sel); }
  function qa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
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
      'paint-order': o.halo ? 'stroke' : null,
      stroke: o.halo ? '#ffffff' : null, 'stroke-width': o.halo ? (o.haloWidth || 3) : null,
      'stroke-linejoin': o.halo ? 'round' : null,
      transform: o.transform || null }, p);
    t.textContent = str;
    return t;
  }
  function r1(v) { return Math.round(v * 10) / 10; }
  function f2(v) { return (v == null || !isFinite(v)) ? '—' : F2.format(Number(v)); }
  function f1(v) { return (v == null || !isFinite(v)) ? '—' : F1.format(Number(v)); }

  // ------------------------------------------------------------------ esqueleto (idéntico a la 1d)
  function esqueleto() {
    return '' +
      '<div class="pl-toolbar">' +
        '<div class="pl-tool pl-grow"><label>Vista</label>' +
          '<span class="pl-badge" id="pl-badge">SECCIÓN TRANSVERSAL</span>' +
          '<span class="pl-src" id="pl-src"></span></div>' +
        '<div class="pl-tool"><label>Lado de referencia (calle)</label>' +
          '<select id="pl-lado-corte"></select></div>' +
        '<div class="pl-tool"><label>MDT</label>' +
          '<select id="pl-mdt"><option value="malla">Malla ETAPA1 (IDW)</option><option value="rest">MDT Catastro REST</option></select></div>' +
        '<div class="pl-tool"><label>Acciones</label>' +
          '<button class="pl-btn primary" id="pl-regenerar" type="button">Regenerar grupos y alturas</button>' +
          '<button class="pl-ghost" id="pl-refrescar" type="button">Refrescar planta</button>' +
          '<button class="pl-ghost" id="pl-reset" type="button">Reset</button></div>' +
        '<div class="pl-tool"><label>Capas</label>' +
          '<label class="pl-check"><input type="checkbox" id="pl-bloques" checked> Bloques</label>' +
          '<label class="pl-check"><input type="checkbox" id="pl-cotas" checked> Cotas</label>' +
          '<label class="pl-check"><input type="checkbox" id="pl-lados"> Lados coloreados</label></div>' +
      '</div>' +
      '<div class="pl-grid">' +
        '<div class="fr-col-plan"><div class="pl-card">' +
          '<div class="pl-card-head"><h4>Planta — bloques sobre el MDT</h4><span class="pl-chip" id="pl-info"></span></div>' +
          '<div class="pl-plano" id="pl-plano"></div>' +
          '<div class="pl-hint" id="pl-plano-msg">Bloques y linderos sobre el terreno. Cotas en MSNM.</div>' +
          '<div class="pl-lados-lista" id="pl-lados-lista"></div>' +
        '</div></div>' +
        '<div class="pl-col-alz"><div class="pl-card">' +
          '<div class="pl-card-head"><h4>Corte transversal del lote (perpendicular a la calle)</h4><span class="pl-readout" id="pl-readout">Eje X: distancia desde la calle (m) · Eje Y: altura MSNM</span></div>' +
          '<div class="pl-svg" id="pl-svg"></div>' +
          '<div class="pl-leyenda" id="pl-leyenda"></div>' +
          '<div class="pl-notes" id="pl-notes"></div>' +
        '</div></div>' +
      '</div>' +
      '<div class="pl-card pl-card-tabla">' +
        '<div class="pl-card-head"><h4>Cotas de los bloques</h4>' +
          '<span class="pl-chip" id="pl-norma-chip"></span></div>' +
        '<div class="pl-tabla" id="pl-tabla-msnm"></div>' +
      '</div>';
  }

  function placeholder(msg) {
    var svg = q('#pl-svg', S.cont);
    var plano = q('#pl-plano', S.cont);
    if (plano) plano.innerHTML = '<div class="pl-loading">' + esc(msg) + '</div>';
    if (svg) svg.innerHTML = '<div class="pl-loading">' + esc(msg) + '</div>';
    var le = q('#pl-leyenda', S.cont); if (le) le.innerHTML = '';
    var no = q('#pl-notes', S.cont); if (no) no.innerHTML = '';
    var bd = q('#pl-badge', S.cont); if (bd) bd.textContent = 'SECCIÓN TRANSVERSAL';
    var sc = q('#pl-src', S.cont); if (sc) sc.textContent = '';
    var info = q('#pl-info', S.cont); if (info) info.textContent = '';
    var tb = q('#pl-tabla-msnm', S.cont); if (tb) tb.innerHTML = '';
  }

  function cargando(txt) {
    var svg = q('#pl-svg', S.cont);
    var plano = q('#pl-plano', S.cont);
    if (plano) plano.innerHTML = '<div class="pl-loading"><span class="pl-spin"></span>' + esc(txt || 'Calculando sección transversal...') + '</div>';
    if (svg) svg.innerHTML = '<div class="pl-loading"><span class="pl-spin"></span>' + esc(txt || 'Calculando sección transversal...') + '</div>';
  }

  function error(msg) {
    var svg = q('#pl-svg', S.cont);
    var plano = q('#pl-plano', S.cont);
    var h = '<div class="pl-err"><b>No se pudo cargar la sección transversal.</b><br>' + esc(msg) + '</div>';
    if (plano) plano.innerHTML = h;
    if (svg) svg.innerHTML = h;
  }

  // ------------------------------------------------------------------- montaje
  function montar(contId, opts) {
    opts = opts || {};
    var cont = document.getElementById(contId);
    if (!cont) return;
    S = { cont: cont, chip: opts.chip || null, mdt: 'malla', ladoCorte: null, data: null, busy: false };
    cont.innerHTML = esqueleto();
    bind();
    if (S.chip) cargar(false);
    else placeholder('Seleccione un CHIP para ver la sección transversal.');
  }

  function setChip(chip) {
    if (!S) return;
    chip = (chip || '').trim().toUpperCase();
    if (S.chip === chip) return;
    S.chip = chip; S.ladoCorte = null; S.data = null;
    if (!chip) { placeholder('Seleccione un CHIP para ver la sección transversal.'); return; }
    cargar(false);
  }

  function bind() {
    var c = S.cont;
    q('#pl-regenerar', c).addEventListener('click', function () { cargar(true); });
    q('#pl-refrescar', c).addEventListener('click', function () { cargar(true); });
    q('#pl-reset', c).addEventListener('click', function () {
      q('#pl-bloques', c).checked = true;
      q('#pl-cotas', c).checked = true;
      q('#pl-lados', c).checked = false;
      if (S.data) renderTodo();
    });
    q('#pl-mdt', c).addEventListener('change', function () { S.mdt = this.value; cargar(true); });
    q('#pl-lado-corte', c).addEventListener('change', function () {
      S.ladoCorte = this.value || null;
      if (S.data) renderTodo();
    });
    q('#pl-bloques', c).addEventListener('change', function () { if (S.data) renderTodo(); });
    q('#pl-cotas', c).addEventListener('change', function () { if (S.data) renderTodo(); });
    q('#pl-lados', c).addEventListener('change', function () { if (S.data) renderTodo(); });
  }

  async function cargar(regen) {
    if (!S || !S.chip || S.busy) return;
    S.busy = true;
    cargando();
    var url = '/api/planta?chip=' + encodeURIComponent(S.chip) +
              '&mdt=' + encodeURIComponent(S.mdt) + (regen ? '&regen=1' : '');
    var r;
    try { r = await fetch(url).then(function (x) { return x.json(); }); }
    catch (e) { r = { ok: false, error: String(e) }; }
    S.busy = false;
    if (!r || !r.ok || !r.planta) { error((r && (r.error || r.mensaje)) || 'sin datos'); return; }
    S.data = r.planta;
    // Poblar selector de lado de corte
    var sel = q('#pl-lado-corte', S.cont);
    var lados = S.data.lote.lados || [];
    sel.innerHTML = '';
    lados.forEach(function (l) {
      var o = document.createElement('option');
      o.value = l.lado_id;
      o.textContent = (l.cardinal_label || 'lado ' + l.lado_id) + ' (' + l.frente + ') · ' + f1(l.longitud_m) + ' m';
      sel.appendChild(o);
    });
    // Lado de referencia por defecto: la calle (lado frontal del predio)
    if (lados.length) {
      var frenteId = S.data.lado_frontal;
      var existe = lados.some(function (l) { return String(l.lado_id) === String(frenteId); });
      var refId = existe ? frenteId : lados[0].lado_id;
      sel.value = String(refId);
      S.ladoCorte = sel.value;
    }
    renderTodo();
  }

  function renderTodo() {
    if (!S.data) return;
    renderInfo();
    renderPlano();
    renderSeccion();
    renderLeyenda();
    renderListaLados();
    renderTablaMsnm();
  }

  function renderInfo() {
    var d = S.data;
    var info = q('#pl-info', S.cont);
    var bd = q('#pl-badge', S.cont);
    var sc = q('#pl-src', S.cont);
    if (!info) return;
    var n = (d.bloques || []).length;
    var verts = (d.lote.vertices || []).length;
    info.textContent = n + ' bloque(s) · ' + verts + ' vertice(s) · área ' + f2(d.lote.area_m2) + ' m²';
    bd.textContent = 'SECCIÓN TRANSVERSAL';
    if (sc) sc.textContent = d.mdt + ' · z_ref ' + f2(d.z_ref) + ' · 0,00 = ' + f2(Z0_MSNM) + ' msnm';
  }

  // ----------------------------------------------------------- planta (izquierda) - misma estructura que 1d
  function renderPlano() {
    var d = S.data;
    var lote = d.lote;
    var vertices = lote.vertices || [];
    var lados = lote.lados || [];
    var bloques = d.bloques || [];
    var cont = q('#pl-plano', S.cont);
    if (!cont) return;

    var xs = [], ys = [];
    vertices.forEach(function (v) { xs.push(v.x); ys.push(v.y); });
    if (!xs.length) { cont.innerHTML = '<div class="pl-err">Sin coordenadas del lote.</div>'; return; }

    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);

    var padX = 25.0, padY = 10.0;
    var x0 = xmin - padX, x1 = xmax + padX;
    var y0 = ymin - padY, y1 = ymax + padY;
    var w = x1 - x0, h = y1 - y0;
    if (!(w > 0) || !(h > 0)) { cont.innerHTML = '<div class="pl-err">Extension invalida.</div>'; return; }

    // Escala: cuantos metros representa 1 px del panel (~294 px utiles).
    var PANEL_PX = 294;
    var U = w / PANEL_PX;            // 1 px  ->  U unidades de datos
    function fs(px) { return px * U; }

    cont.innerHTML = '';
    var svg = sv('svg', { viewBox: x0 + ' ' + (-y1) + ' ' + w + ' ' + h,
      preserveAspectRatio: 'xMidYMid meet', role: 'img',
      'aria-label': 'Planta del lote con bloques' }, cont);
    rect(svg, x0, -y1, w, h, '#fbfcfc', 1);

    // Vias de acceso (contexto de fondo)
    (d.vias || []).forEach(function (v) {
      var pts = (v.polyline || []).map(function (p) { return [p[0], -p[1]]; });
      if (pts.length > 1) poly(svg, pts, '#cbd5e1', fs(1.2), null, '#e2e8f0', 0.5);
    });

    // Lados del lote con su color
    (lados || []).forEach(function (l) {
      var pts = (l.polyline || []).map(function (p) { return [p[0], -p[1]]; });
      if (pts.length < 2) return;
      var esFrente = (String(l.lado_id) === String(d.lado_frontal));
      poly(svg, pts, esFrente ? l.color : '#94a3b8', esFrente ? fs(2.2) : fs(1.1), null, null, 0);
    });

    // Perimetro del lote
    var ring = vertices.map(function (v) { return [v.x, -v.y]; });
    poly(svg, ring, '#111827', fs(0.8), null, '#ffffff', 0.92);

    // Bloques con su ID (texto escalado a unidades de datos)
    bloques.forEach(function (b, idx) {
      var pts = (b.poligono || []).map(function (p) { return [p[0], -p[1]]; });
      if (pts.length < 3) return;
      var color = PCOL[idx % PCOL.length];
      poly(svg, pts, color, fs(1.6), null, color, 0.26);

      var cx = 0, cy = 0;
      pts.forEach(function (p) { cx += p[0]; cy += p[1]; });
      cx /= pts.length; cy /= pts.length;

      var t = sv('text', { x: r1(cx), y: r1(cy + fs(3.4)), 'font-size': r1(fs(10)),
        fill: '#ffffff', 'text-anchor': 'middle', 'font-weight': 800,
        'paint-order': 'stroke', stroke: '#000000', 'stroke-width': r1(fs(2.6)),
        'stroke-linejoin': 'round' }, svg);
      t.textContent = 'B' + (idx + 1);
    });

    // Norte
    var mx = x1 - fs(12);
    var myTop = y1 - fs(10);
    line(svg, mx, -myTop, mx, -myTop + fs(14), '#374151', fs(1.6));
    sv('polygon', { fill: '#374151', points:
      [r1(mx), r1(-myTop)].join(',') + ' ' +
      [r1(mx - fs(3.4)), r1(-myTop + fs(7))].join(',') + ' ' +
      [r1(mx + fs(3.4)), r1(-myTop + fs(7))].join(',') }, svg);
    var tn = sv('text', { x: r1(mx), y: r1(-myTop - fs(2.5)), 'font-size': r1(fs(9)),
      fill: '#374151', 'text-anchor': 'middle', 'font-weight': 700 }, svg);
    tn.textContent = 'N';
  }

  // ------------------------------------------- lista de lados y vecinos (HTML)
  function renderListaLados() {
    var d = S.data;
    var cont = q('#pl-lados-lista', S.cont);
    if (!cont) return;
    var lados = d.lote.lados || [];
    if (!lados.length) { cont.innerHTML = ''; return; }

    var h = '<div class="pl-lados-tit">Linderos y vecinos</div><ul class="pl-lados-ul">';
    lados.forEach(function (l) {
      var esFrente = (String(l.lado_id) === String(d.lado_frontal));
      var vns = (l.vecinos || []).map(function (v) { return v.nombre || v.chip || 'vecino'; });
      var txtVec = vns.length ? vns.join(', ') : '—';
      h += '<li>' +
        '<span class="pl-lados-sw" style="background:' + (l.color || '#94a3b8') + '"></span>' +
        '<b>' + esc(l.cardinal_label || ('lado ' + l.lado_id)) + '</b>' +
        (esFrente ? ' <span class="pl-lados-tag">calle</span>' : '') +
        ' · ' + f1(l.longitud_m) + ' m · ' + esc(l.frente || '') +
        '<br><span class="pl-lados-vec">' + esc(txtVec) + '</span>' +
        '</li>';
    });
    h += '</ul>';
    cont.innerHTML = h;
  }

  // -------------------------------------------------------- sección transversal (derecha) - mismo estilo que alzado 1d
  function renderSeccion() {
    var d = S.data;
    var lote = d.lote;
    var lados = lote.lados || [];
    var vertices = lote.vertices || [];
    var bloques = d.bloques || [];
    var zRef = d.z_ref || 0;
    var norma = d.norma || {};
    var cont = q('#pl-svg', S.cont);
    if (!cont) return;

    var W = 1180, H = 640;
    var M = { l: 104, r: 168, t: 64, b: 82 };
    var wp = W - M.l - M.r, hp = H - M.t - M.b;

    // ---- Lado de referencia: la calle ---------------------------------------
    var refId = S.ladoCorte != null ? S.ladoCorte : d.lado_frontal;
    var calle = null;
    for (var i = 0; i < lados.length; i++) {
      if (String(lados[i].lado_id) === String(refId)) { calle = lados[i]; break; }
    }
    if (!calle) {
      for (var i2 = 0; i2 < lados.length; i2++) {
        if (String(lados[i2].lado_id) === String(d.lado_frontal)) { calle = lados[i2]; break; }
      }
    }
    if (!calle && lados.length) calle = lados[0];
    if (!calle) { cont.innerHTML = '<div class="pl-err">Sin lado de referencia para el corte.</div>'; return; }

    var cpts = calle.polyline || [];
    if (cpts.length < 2) { cont.innerHTML = '<div class="pl-err">El lado de referencia no tiene puntos.</div>'; return; }

    // ---- Eje del corte: perpendicular a la calle ---------------------------
    var c0 = cpts[0], c1 = cpts[cpts.length - 1];
    var ex = c1[0] - c0[0], ey = c1[1] - c0[1];
    var en = Math.sqrt(ex * ex + ey * ey) || 1;
    ex /= en; ey /= en;
    var nx = -ey, ny = ex;

    var omx = 0, omy = 0;
    cpts.forEach(function (p) { omx += p[0]; omy += p[1]; });
    omx /= cpts.length; omy /= cpts.length;

    var clx = 0, cly = 0;
    vertices.forEach(function (v) { clx += v.x; cly += v.y; });
    clx /= (vertices.length || 1); cly /= (vertices.length || 1);
    if ((clx - omx) * nx + (cly - omy) * ny < 0) { nx = -nx; ny = -ny; }

    function T(x, y) { return (x - omx) * nx + (y - omy) * ny; }

    function ext(poly) {
      var a = 1e9, b = -1e9;
      poly.forEach(function (p) {
        var t = T(p[0], p[1]);
        if (t < a) a = t;
        if (t > b) b = t;
      });
      return [a, b];
    }

    var tLote = ext(vertices.map(function (v) { return [v.x, v.y]; }));

    // ---- Norma de edificabilidad + entrepiso configurado -------------------
    var rango = d.entrepiso_rango_m || { min: 2.20, max: 3.80, defecto: 3.00 };
    var ENTREPISO = rango.defecto || 3.00;
    var pisosNorma = (norma.pisos_max != null) ? Number(norma.pisos_max) : null;
    var alturaMax = (norma.altura_max_m != null) ? Number(norma.altura_max_m) : null;

    function entrepisoDe(b) {
      var e = Number(b.altura_entrepiso_m);
      if (!isFinite(e) || e <= 0) return ENTREPISO;
      return Math.min(Math.max(e, rango.min), rango.max);
    }

    function alturaBloque(b) {
      var pisos = Number(b.pisos || 1);
      var ent = entrepisoDe(b);
      // Solo el RANGO DE EDIFICABILIDAD limita el numero de pisos.
      // La altura reglamentaria es una cota sobre el MDT: se reporta como advertencia.
      var tope = pisosNorma ? Math.min(pisos, pisosNorma) : pisos;
      if (tope < 1) tope = 1;
      var h = tope * ent;
      // advertencia si la altura sobre el MDT supera el limite reglamentario
      var altMaxMdt = (b.altura_max_sobre_mdt_m != null) ? Number(b.altura_max_sobre_mdt_m) : null;
      var advAltura = !!b.advertencia_altura;
      return { h: h, pisosEf: tope, pisosOrig: pisos, ent: ent,
               excede: tope < pisos, altMaxMdt: altMaxMdt, advAltura: advAltura };
    }

    var bloquesT = [];
    bloques.forEach(function (b, idx) {
      var poly = b.poligono || [];
      if (poly.length < 3) return;
      var e = ext(poly);
      bloquesT.push({
        idx: idx, ref: b, t0: e[0], t1: e[1], tMed: (e[0] + e[1]) / 2,
        color: PCOL[idx % PCOL.length], alt: alturaBloque(b)
      });
    });

    var tMin = Math.min(tLote[0], 0);
    var tMax = Math.max(tLote[1], 1);
    bloquesT.forEach(function (bt) { tMin = Math.min(tMin, bt.t0); tMax = Math.max(tMax, bt.t1); });
    var padT = Math.max(1.5, (tMax - tMin) * 0.05);
    tMin -= padT; tMax += padT;

    function X(t) { return M.l + (t - tMin) / (tMax - tMin) * wp; }

    // ---- Perfil del terreno ------------------------------------------------
    var zCalle = cpts.reduce(function (a, p) { return a + (p[2] + zRef); }, 0) / cpts.length;
    var perfil = [{ t: T(omx, omy), z: zCalle }];
    bloquesT.forEach(function (bt) {
      if (bt.ref.z_terreno_medio_m != null) perfil.push({ t: bt.tMed, z: bt.ref.z_terreno_medio_m });
    });
    var vFondo = null, tFondo = -1e9;
    vertices.forEach(function (v) {
      var t = T(v.x, v.y);
      if (t > tFondo) { tFondo = t; vFondo = v; }
    });
    if (vFondo && vFondo.msnm != null) perfil.push({ t: tFondo, z: vFondo.msnm });
    var vFrente = null, tFrente = 1e9;
    vertices.forEach(function (v) {
      var t = T(v.x, v.y);
      if (t < tFrente) { tFrente = t; vFrente = v; }
    });
    if (vFrente && vFrente.msnm != null) perfil.push({ t: tFrente, z: vFrente.msnm });
    perfil.sort(function (a, b) { return a.t - b.t; });

    function zTerr(t) {
      var P = perfil;
      if (!P.length) return 0;
      if (t <= P[0].t) return P[0].z;
      if (t >= P[P.length - 1].t) return P[P.length - 1].z;
      for (var i = 1; i < P.length; i++) {
        if (t <= P[i].t) {
          var a = P[i - 1], b = P[i];
          var f = (t - a.t) / ((b.t - a.t) || 1);
          return a.z + f * (b.z - a.z);
        }
      }
      return P[P.length - 1].z;
    }

    // ---- Rango Z -----------------------------------------------------------
    var zVals = [];
    perfil.forEach(function (p) { if (p.z != null && isFinite(p.z)) zVals.push(p.z); });
    bloquesT.forEach(function (bt) {
      var zb = (bt.ref.z_base_m != null) ? bt.ref.z_base_m + zRef : bt.ref.z_terreno_medio_m;
      zVals.push(zb);
      zVals.push(zb + bt.alt.h);
      zVals.push(zTerr(bt.t0) + bt.alt.h);
    });
    zVals.push(Z0_MSNM);
    var zmin = Math.min.apply(null, zVals), zmax = Math.max.apply(null, zVals);
    var padZ = Math.max(1.2, (zmax - zmin) * 0.08);
    zmin -= padZ * 1.6;   // aire abajo
    zmax += padZ * 2.6;   // aire arriba para ID + aviso + etiquetas N/C/S
    if (zmax - zmin < 3) { zmin -= 1.5; zmax += 1.5; }

    function Y(z) { return M.t + hp - (z - zmin) / (zmax - zmin) * hp; }

    // ---- Dibujo ------------------------------------------------------------
    cont.innerHTML = '';
    var svg = sv('svg', { viewBox: '0 0 ' + W + ' ' + H, width: '100%',
      preserveAspectRatio: 'xMidYMid meet', role: 'img',
      'aria-label': 'Sección transversal del lote' }, cont);
    rect(svg, 0, 0, W, H, '#ffffff', 1);
    rect(svg, M.l, M.t, wp, hp, '#fbfcfa', 1);

    var nGrid = 8;
    for (var g = 0; g <= nGrid; g++) {
      var tg = tMin + (tMax - tMin) * g / nGrid;
      line(svg, X(tg), M.t, X(tg), M.t + hp, '#f1f5f9', 1);
      var zg = zmin + (zmax - zmin) * g / nGrid;
      line(svg, M.l - 5, Y(zg), M.l, Y(zg), '#374151', 1);
      text(svg, M.l - 10, Y(zg) + 3, f1(zg), { size: 9, fill: '#6b7280', anchor: 'end' });
    }

    // Terreno
    if (perfil.length > 1) {
      var arr = perfil.map(function (p) { return [X(p.t), Y(p.z)]; });
      var rell = arr.slice();
      rell.push([X(perfil[perfil.length - 1].t), Y(zmin)], [X(perfil[0].t), Y(zmin)]);
      poly(svg, rell, 'none', 0, null, '#efeade', 0.7);
      poly(svg, arr, COL_LOTE, 2.6, null);
    }

    // 0,00
    var yZ0 = Y(Z0_MSNM);
    line(svg, M.l, yZ0, M.l + wp, yZ0, '#b42318', 1.3, '8 4', 0.9);
    text(svg, M.l + wp - 4, yZ0 - 5, '0,00 = ' + f2(Z0_MSNM) + ' msnm',
      { size: 9.5, weight: 700, fill: '#b42318', anchor: 'end', halo: true });

    // Calle
    line(svg, X(tMin), M.t, X(tMin), M.t + hp, '#1f6feb', 1.6, '4 3', 0.5);
    text(svg, X(tMin) + 5, M.t + 14, 'calle ' + (calle.cardinal_label || ''),
      { size: 10, weight: 700, fill: '#1f6feb', halo: true });

    // ---- Bloques + cotas verticales a izquierda y derecha ------------------
    bloquesT.forEach(function (bt) {
      var b = bt.ref;
      var zb = (b.z_base_m != null) ? b.z_base_m + zRef
               : (b.z_terreno_medio_m != null ? b.z_terreno_medio_m : zmin);
      var zt = zb + bt.alt.h;

      var x0b = X(bt.t0), x1b = X(bt.t1);
      var ancho = Math.max(3, x1b - x0b);
      if (x1b - x0b < 3) { var cxx = (x0b + x1b) / 2; x0b = cxx - 1.5; ancho = 3; }

      rect(svg, x0b, Y(zt), ancho, Y(zb) - Y(zt), bt.color, 0.22, bt.color, 1.8);

      // ID del bloque arriba (encima de las etiquetas N/C/S)
      text(svg, x0b + ancho / 2, Y(zt) - 42, 'B' + (bt.idx + 1),
        { size: 10, weight: 800, fill: bt.color, anchor: 'middle', halo: true, haloWidth: 3 });

      // Advertencia: la altura sobre el MDT supera el limite reglamentario
      if (bt.alt.advAltura) {
        var lblW = '⚠ ' + f2(bt.alt.altMaxMdt) + ' m sobre MDT';
        text(svg, x0b + ancho / 2, Y(zt) - 31, lblW,
          { size: 8, weight: 800, fill: '#b45309', anchor: 'middle', halo: true, haloWidth: 2.4 });
      }

      // ---- Cotas verticales: BORDES (I/D) + NORTE / CENTRO / SUR ----
      // I/D: terreno interpolado en los bordes del bloque sobre el eje del corte.
      // N/C/S: IDW del MDT en los extremos y el centro de la franja (backend).
      var terr3 = b.terreno_msnm || {};
      var alt3 = b.altura_sobre_mdt_m || {};

      var xI = x0b + ancho * 0.06;
      var xN = x0b + ancho * 0.28;
      var xC = x0b + ancho * 0.50;
      var xS = x0b + ancho * 0.72;
      var xD = x0b + ancho * 0.94;

      function cotaPlano(xBase, zTerrMsnm, etiqueta, punteada, color) {
        if (zTerrMsnm == null || !isFinite(zTerrMsnm)) return;
        var hAlt = Math.max(0, zt - zTerrMsnm);
        if (hAlt <= 0.03) return;
        var col = color || (punteada ? '#6b7280' : '#111827');

        line(svg, xBase, Y(zTerrMsnm), xBase, Y(zt), col,
             punteada ? 1.2 : 1.5, punteada ? '5 3' : null, punteada ? 0.95 : 1);
        line(svg, xBase - 4, Y(zt), xBase + 4, Y(zt), col, 1.3);
        line(svg, xBase - 4, Y(zTerrMsnm), xBase + 4, Y(zTerrMsnm), col, 1.1);

        var ym = (Y(zTerrMsnm) + Y(zt)) / 2;
        text(svg, xBase - 5, ym, f2(hAlt) + ' m',
          { size: 7.8, weight: punteada ? 600 : 800, fill: col, anchor: 'middle',
            halo: true, haloWidth: 2.8,
            transform: 'rotate(-90 ' + r1(xBase - 5) + ' ' + r1(ym) + ')' });
        text(svg, xBase, Y(zt) - 17, etiqueta,
          { size: 8.2, weight: 800, fill: col, anchor: 'middle', halo: true, haloWidth: 2.8 });
      }

      // Bordes del bloque sobre el eje del corte (terreno interpolado)
      b._mdt = {
        i: Math.max(0, zt - zTerr(bt.t0)),
        n: terr3.norte, c: terr3.centro, s: terr3.sur,
        d: Math.max(0, zt - zTerr(bt.t1))
      };
      cotaPlano(xI, zTerr(bt.t0), 'I', false, '#0f6b5f');
      // Extremos y centro de la franja (IDW del MDT)
      cotaPlano(xN, terr3.norte, 'N', true);
      cotaPlano(xC, terr3.centro, 'C', false);
      cotaPlano(xS, terr3.sur, 'S', true);
      // Borde derecho
      cotaPlano(xD, zTerr(bt.t1), 'D', false, '#0f6b5f');

      // Plano de cubierta punteado entre los extremos N y S
      if (terr3.norte != null && terr3.sur != null) {
        line(svg, xN, Y(zt) - 6, xS, Y(zt) - 6, '#6b7280', 1.0, '3 3', 0.75);
      }

      // Diferencia desde 0,00 al pie del bloque
      var dif = zb - Z0_MSNM;
      text(svg, x0b + ancho / 2, Y(zb) + 12, '+' + f2(dif),
        { size: 8, fill: '#6b7280', anchor: 'middle', halo: true, haloWidth: 2.2 });
    });

    // Ejes
    line(svg, M.l, M.t + hp, M.l + wp, M.t + hp, '#374151', 1.5);
    line(svg, M.l, M.t, M.l, M.t + hp, '#374151', 1.5);

    for (var g2 = 0; g2 <= nGrid; g2++) {
      var tt = tMin + (tMax - tMin) * g2 / nGrid;
      line(svg, X(tt), M.t + hp, X(tt), M.t + hp + 6, '#374151', 1);
      text(svg, X(tt), M.t + hp + 18, f1(tt), { size: 9, fill: '#6b7280', anchor: 'middle' });
    }

    text(svg, M.l + wp / 2, M.t + hp + 40, 'Distancia desde la calle hacia el interior del lote (m)',
      { size: 11.5, weight: 600, fill: '#374151', anchor: 'middle' });
    text(svg, M.l - 26, M.t + hp / 2, 'Altura MSNM (m)',
      { size: 11.5, weight: 600, fill: '#374151', anchor: 'middle',
        transform: 'rotate(-90 ' + r1(M.l - 26) + ' ' + r1(M.t + hp / 2) + ')' });

    // Titulo
    var ttl = 'Corte transversal perpendicular a ' + (calle.cardinal_label || ('lado ' + calle.lado_id)) +
              ' · ancho ' + f1(tMax - tMin) + ' m';
    if (pisosNorma) ttl += ' · norma: ' + pisosNorma + ' pisos';
    if (alturaMax) ttl += ' / ' + f1(alturaMax) + ' m';
    var ents = bloquesT.map(function (bt) { return bt.alt.ent; });
    if (ents.length) {
      var uniq = {};
      ents.forEach(function (e) { uniq[e.toFixed(2)] = 1; });
      ttl += ' · entrepiso: ' + Object.keys(uniq).join(' / ') + ' m';
    }
    text(svg, M.l, M.t - 12, ttl, { size: 11.5, weight: 700, fill: '#15201f' });
  }

  // -------------------------------------------------------- lista inferior MSN y diferencias desde 0,00
  function renderTablaMsnm() {
    var d = S.data;
    var bloques = d.bloques || [];
    var norma = d.norma || {};
    var rango = d.entrepiso_rango_m || { min: 2.20, max: 3.80, defecto: 3.00 };
    var cont = q('#pl-tabla-msnm', S.cont);
    var chip = q('#pl-norma-chip', S.cont);
    if (!cont) return;

    var pisosNorma = (norma.pisos_max != null) ? Number(norma.pisos_max) : null;
    var alturaMax = (norma.altura_max_m != null) ? Number(norma.altura_max_m) : null;

    if (chip) {
      var partes = [];
      if (norma.rango_edificabilidad != null) partes.push('rango edificabilidad: ' + norma.rango_edificabilidad);
      if (pisosNorma) partes.push('máx. ' + pisosNorma + ' pisos');
      if (alturaMax) partes.push('altura reglamentaria: ' + f1(alturaMax) + ' m sobre el MDT');
      if (norma.tratamiento) partes.push(norma.tratamiento);
      chip.textContent = partes.join(' · ') || 'sin datos de norma';
    }

    if (!bloques.length) {
      cont.innerHTML = '<div class="pl-hint">No hay bloques generados para este CHIP.</div>';
      return;
    }

    var h = '<table class="pl-ptab"><thead><tr>' +
      '<th>Bloque</th>' +
      '<th class="num">z_terreno centro</th>' +
      '<th class="num">z_base MSNM</th>' +
      '<th class="num">Altura desde 0,00</th>' +
      '<th class="num">Entrepiso</th>' +
      '<th class="num">Pisos</th>' +
      '<th class="num">Altura bloque</th>' +
      '<th class="num">MDT → tope (I · N · C · S · D)</th>' +
      '<th>Altura reglamentaria</th>' +
      '</tr></thead><tbody>';

    bloques.forEach(function (b, idx) {
      var color = PCOL[idx % PCOL.length];
      var terr3 = b.terreno_msnm || {};
      var alt3 = b.altura_sobre_mdt_m || {};

      var zTerrC = (terr3.centro != null) ? terr3.centro
                 : ((b.z_terreno_medio_m != null) ? b.z_terreno_medio_m : 0);
      var zBaseMsnm = (b.z_base_m != null) ? b.z_base_m + d.z_ref : zTerrC;
      var altDesde00 = zBaseMsnm - Z0_MSNM;

      var ent = Number(b.altura_entrepiso_m);
      if (!isFinite(ent) || ent <= 0) ent = rango.defecto || 3.0;
      ent = Math.min(Math.max(ent, rango.min), rango.max);

      // Solo el rango de edificabilidad limita los pisos
      var pisos = Number(b.pisos || 0);
      var tope = pisosNorma ? Math.min(pisos, pisosNorma) : pisos;
      if (tope < 1) tope = 1;
      var hBloque = tope * ent;
      var excedePisos = tope < pisos;

      var mdt5 = b._mdt || {};
      var fI = (mdt5.i != null) ? f2(mdt5.i) : '—';
      var fN = (alt3.norte != null) ? f2(alt3.norte) : '—';
      var fC = (alt3.centro != null) ? f2(alt3.centro) : '—';
      var fS = (alt3.sur != null) ? f2(alt3.sur) : '—';
      var fD = (mdt5.d != null) ? f2(mdt5.d) : '—';
      var maxMdt = (alt3.max != null) ? Number(alt3.max) : null;

      var adv = null;
      if (alturaMax && maxMdt != null && maxMdt > alturaMax + 0.01) {
        adv = '⚠ excede ' + f2(maxMdt - alturaMax) + ' m';
      }

      h += '<tr>' +
        '<td><span class="fr-dot" style="background:' + color + '"></span><b>B' + (idx + 1) + '</b></td>' +
        '<td class="num">' + f2(zTerrC) + '</td>' +
        '<td class="num">' + f2(zBaseMsnm) + '</td>' +
        '<td class="num">' + f2(altDesde00) + '</td>' +
        '<td class="num">' + f2(ent) + ' m</td>' +
        '<td class="num"' + (excedePisos ? ' style="color:#b42318;font-weight:700"' : '') + '>' +
          tope + (excedePisos ? ' <span title="bloques.json pide ' + pisos + ' pisos">(!)</span>' : '') +
        '</td>' +
        '<td class="num">' + f2(hBloque) + ' m</td>' +
        '<td class="num">' + fI + ' · ' + fN + ' · ' + fC + ' · ' + fS + ' · ' + fD + '</td>' +
        '<td style="font-size:11px">' +
          (alturaMax ? f1(alturaMax) + ' m' : '—') +
          (adv ? ' <span style="color:#b45309;font-weight:700">' + adv + '</span>'
               : ' <span style="color:#166534">✓ dentro</span>') +
        '</td>' +
        '</tr>';
    });
    h += '</tbody></table>';

    var nota = '<div class="pl-nota-tabla">' +
      '0,00 = ' + f2(Z0_MSNM) + ' msnm (nivel L 01 en ArchiCAD). ' +
      'Entrepiso válido en Bogotá: ' + f2(rango.min) + '–' + f2(rango.max) + ' m. ' +
      '<b>Pisos</b> = mín(pisos de bloques.json, rango de edificabilidad' +
      (pisosNorma ? ' = ' + pisosNorma : '') + '). ' +
      '<b>MDT → tope</b> = altura medida desde el terreno hasta el tope del bloque en los extremos ' +
      'norte (N), centro (C) y sur (S) de la franja. ' +
      'La altura reglamentaria (' + (alturaMax ? f1(alturaMax) + ' m' : '—') +
      ') es una <b>cota sobre el MDT</b>: si se excede se reporta como advertencia, no recorta los pisos.' +
      '</div>';

    cont.innerHTML = h + nota;
  }

  function renderLeyenda() {
    var d = S.data;
    var bloques = d.bloques || [];
    var le = q('#pl-leyenda', S.cont);
    if (!le) return;
    var items = bloques.map(function (b, idx) {
      var color = PCOL[idx % PCOL.length];
      var a = b.altura_sobre_mdt_m || {};
      var m = b._mdt || {};
      var ncs = (a.norte != null || m.n != null)
        ? ' · MDT→tope I ' + f2(m.i) + ' / N ' + f2(a.norte) + ' / C ' + f2(a.centro) +
          ' / S ' + f2(a.sur) + ' / D ' + f2(m.d) + ' m'
        : '';
      return '<span style="display:inline-flex;align-items:center;gap:6px;margin-right:14px;font-size:12px;">' +
        '<span style="display:inline-block;width:12px;height:12px;background:' + color + ';border:1px solid #333;border-radius:2px;"></span>' +
        '<b>B' + (idx + 1) + '</b> ' + f2(b.altura_bloque_m || 0) + ' m · ' + (b.pisos_efectivos || b.pisos) +
        ' p @ ' + f2(b.altura_entrepiso_m) + ' m' + ncs +
        '</span>';
    }).join('');
    le.innerHTML =
      '<div style="font-size:11px;color:#6b7280;margin-bottom:4px;"><b>Bloques en el corte:</b></div>' + items +
      (d.avisos && d.avisos.length ? '<div style="font-size:11px;color:#b42318;margin-top:8px;">' + d.avisos.join(' ') + '</div>' : '');
  }

  // ------------------------------------------------------------------ API publica
  global.Planta = { montar: montar, setChip: setChip };

})(this);
