/*
 * qcwall.js — QC-003's chapter-condensing diagram module for Open Dossier
 * living figures. One registered type ("qc") with a spec-declared "kind"
 * choosing among five generic diagram forms:
 *
 *   kind:"origins"  — staggered-origin arrows (claims measured from different
 *                     zeros; the layout ENACTS incomparability: arrow tips are
 *                     deliberately not comparable, and that is the message)
 *   kind:"lines"    — small line chart: linear/log axes, series from tiny
 *                     generators (exp decay / survival (1-p)^N / linear) or
 *                     explicit points; optional bands, markers, notes
 *   kind:"budget"   — one 100% stacked horizontal bar (where a budget goes)
 *   kind:"quadrant" — a labeled 2x2 with placed points and a cluster
 *   kind:"ruler"    — one log axis with labeled points, a comparison pair on
 *                     a second row, and span brackets
 *
 * DOCTRINE (same as every module here):
 *   - Vendored, zero-dependency, reader-side. Loaded after figures.js; extends
 *     window.DossierFigures. Composes the general primitives (el/escAttr/escTxt);
 *     never re-rolls them. The chart mini-kit (value->px scales, decade ticks,
 *     polyline paths) is LOCAL to this module by design: the engine ships no
 *     charting layer yet (see figures/README.md, "Honest scope").
 *   - SHARED-COMPUTE SPLIT: one computeQC(spec) produces the full SVG body
 *     string; the poster emitter and the live renderer both consume it, so the
 *     JS-off floor can never drift from the lightbox ceiling.
 *   - The spec carries the CONTENT (every number, label and provenance note);
 *     this module carries only FORM. A figure's numbers are the manuscript's
 *     numbers — change the manuscript, change the spec, re-seal.
 *   - Text uses tier classes (lf-tick / lf-axis / lf-callout) only — sizing is
 *     owned by the runtime; this module sets none of its own.
 *   - Colors are role names resolved to the dossier skin's literal palette
 *     (validated: the four accents pass the six categorical checks on white).
 *     Sealed posters are static, so literals — not CSS vars — keep the floor
 *     self-contained everywhere (page, lightbox breakout, JS-off).
 */
(function () {
  "use strict";
  var W = (typeof window !== "undefined") ? window : global.window;
  var DF = W.DossierFigures;
  if (!DF) throw new Error("qcwall.js requires figures.js to be loaded first");
  var escA = DF.escAttr, escT = DF.escTxt;

  // The dossier skin's palette, as literals (skin/edition.html :root).
  var C = {
    ink: "#17262c", ink2: "#586a6f", line: "#dbe3e1", card: "#ffffff",
    teal: "#0c8f86", tealSoft: "#e2efed",
    coral: "#cf5d36", coralSoft: "#fbe9e3",
    violet: "#6b4e9b", violetSoft: "#efe9f6",
    amber: "#bd861d", amberSoft: "#fdf6e9"
  };
  function col(role) { return C[role] || role || C.ink; }
  var MONO = "ui-monospace,Menlo,Consolas,monospace";

  // ---------------------------------------------------------------- mini-kit
  function r2(v) { return Math.round(v * 100) / 100; }
  function scaleFor(axis, lo, hi) {
    // axis: {min,max,log} -> value->px map onto [lo,hi]
    var mn = axis.min, mx = axis.max, lg = !!axis.log;
    var a = lg ? Math.log10(mn) : mn, b = lg ? Math.log10(mx) : mx;
    return function (v) {
      var t = ((lg ? Math.log10(v) : v) - a) / (b - a);
      return lo + t * (hi - lo);
    };
  }
  function decadeTicks(axis) {
    var out = [], e0 = Math.ceil(Math.log10(axis.min)), e1 = Math.floor(Math.log10(axis.max));
    for (var e = e0; e <= e1; e++) out.push(Math.pow(10, e));
    return out;
  }
  function fmtPow(v) {
    var e = Math.round(Math.log10(v));
    if (Math.abs(Math.pow(10, e) - v) / v < 1e-9 && (e < -2 || e > 3)) {
      var sup = { "-": "⁻", "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶" };
      return "10" + String(e).split("").map(function (ch) { return sup[ch] || ch; }).join("");
    }
    return v >= 1000 ? String(v.toLocaleString("en-US")) : String(v);
  }
  function txt(x, y, str, opts) {
    opts = opts || {};
    return '<text x="' + r2(x) + '" y="' + r2(y) + '"' +
      (opts.tier ? ' class="' + opts.tier + '"' : "") +
      ' fill="' + escA(col(opts.color || "ink")) + '"' +
      (opts.anchor ? ' text-anchor="' + opts.anchor + '"' : "") +
      (opts.mono ? ' font-family="' + MONO + '"' : "") +
      (opts.bold ? ' font-weight="600"' : "") +
      (opts.opacity ? ' opacity="' + opts.opacity + '"' : "") + ">" +
      escT(str) + "</text>";
  }
  function lineSeg(x1, y1, x2, y2, color, sw, dash, op) {
    return '<line x1="' + r2(x1) + '" y1="' + r2(y1) + '" x2="' + r2(x2) + '" y2="' + r2(y2) +
      '" stroke="' + escA(col(color)) + '" stroke-width="' + (sw || 1) + '"' +
      (dash ? ' stroke-dasharray="' + dash + '"' : "") +
      (op ? ' opacity="' + op + '"' : "") + "></line>";
  }
  function dot(x, y, r, color, hollow) {
    return '<circle cx="' + r2(x) + '" cy="' + r2(y) + '" r="' + r + '" ' +
      (hollow ? 'fill="' + escA(C.card) + '" stroke="' + escA(col(color)) + '" stroke-width="2"'
              : 'fill="' + escA(col(color)) + '" stroke="' + escA(C.card) + '" stroke-width="2"') + "></circle>";
  }
  function pathFrom(pts, sx, sy, color, sw, dash) {
    var d = pts.map(function (p, i) { return (i ? "L" : "M") + r2(sx(p[0])) + " " + r2(sy(p[1])); }).join(" ");
    return '<path d="' + d + '" fill="none" stroke="' + escA(col(color)) + '" stroke-width="' + (sw || 2) +
      '" stroke-linejoin="round" stroke-linecap="round"' + (dash ? ' stroke-dasharray="' + dash + '"' : "") + "></path>";
  }
  function genSeries(s, axis) {
    if (s.pts) return s.pts;
    var g = s.gen || {}, pts = [], N = 64, i, x;
    var x0 = axis.min, x1 = axis.max, lg = !!axis.log;
    for (i = 0; i <= N; i++) {
      x = lg ? Math.pow(10, Math.log10(x0) + (i / N) * (Math.log10(x1) - Math.log10(x0)))
             : x0 + (i / N) * (x1 - x0);
      if (g.kind === "exp") pts.push([x, Math.exp(-x / (g.tau || 1))]);
      else if (g.kind === "survival") pts.push([x, Math.pow(1 - g.p, x)]);
      else if (g.kind === "linear") pts.push([x, g.k * x]);
      else if (g.kind === "const") pts.push([x, g.v]);
    }
    return pts;
  }

  // ---------------------------------------------------------------- kinds ---
  function drawLines(spec) {
    var Wd = 800, Hd = spec.h || 430, padL = 74, padR = 26, padT = 56, padB = 60;
    var xa = spec.xaxis, ya = spec.yaxis;
    var sx = scaleFor(xa, padL, Wd - padR);
    var syRaw = scaleFor(ya, Hd - padB, padT);
    var sy = function (v) { // clamp into plot so log/linear tails stay inside
      var y = syRaw(Math.max(v, ya.min)); return Math.max(padT, Math.min(Hd - padB, y));
    };
    var s = "";
    // frame + ticks
    var xticks = xa.ticks || (xa.log ? decadeTicks(xa) : null) || [];
    var yticks = ya.ticks || (ya.log ? decadeTicks(ya) : null) || [];
    xticks.forEach(function (v) {
      s += lineSeg(sx(v), padT, sx(v), Hd - padB, "line", 1);
      s += txt(sx(v), Hd - padB + 18, xa.fmt === "pct" ? (v * 100) + "%" : fmtPow(v), { tier: "lf-tick", color: "ink2", anchor: "middle", mono: true });
    });
    yticks.forEach(function (v) {
      s += lineSeg(padL, sy(v), Wd - padR, sy(v), "line", 1);
      s += txt(padL - 8, sy(v) + 4, ya.fmt === "pct" ? Math.round(v * 100) + "%" : fmtPow(v), { tier: "lf-tick", color: "ink2", anchor: "end", mono: true });
    });
    s += lineSeg(padL, Hd - padB, Wd - padR, Hd - padB, "ink", 1.5);
    s += lineSeg(padL, padT, padL, Hd - padB, "ink", 1.5);
    s += txt((padL + Wd - padR) / 2, Hd - padB + 40, xa.label, { tier: "lf-axis", color: "ink2", anchor: "middle" });
    s += '<g transform="rotate(-90 20 ' + r2((padT + Hd - padB) / 2) + ')">' +
         txt(20, (padT + Hd - padB) / 2, ya.label, { tier: "lf-axis", color: "ink2", anchor: "middle" }) + "</g>";
    // bands
    (spec.hbands || []).forEach(function (b) {
      var y0 = sy(b.y1), y1 = sy(b.y0);
      s += '<rect x="' + padL + '" y="' + r2(y0) + '" width="' + r2(Wd - padR - padL) + '" height="' + r2(y1 - y0) +
           '" fill="' + escA(col(b.color || "amber")) + '" opacity="0.14"></rect>';
      if (b.label) s += txt(Wd - padR - 6, y0 + 16, b.label, { tier: "lf-tick", color: b.color || "amber", anchor: "end" });
    });
    // legend row (top) — identity never color-alone: chip + name per series
    var lx = padL;
    (spec.series || []).forEach(function (ser) {
      s += '<rect x="' + r2(lx) + '" y="' + (padT - 34) + '" width="14" height="4" rx="2" fill="' + escA(col(ser.color)) + '"></rect>';
      s += txt(lx + 20, padT - 27, ser.name, { tier: "lf-tick", color: "ink" });
      lx += 20 + ser.name.length * 6.6 + 26;
    });
    // series + direct end labels
    (spec.series || []).forEach(function (ser) {
      var pts = genSeries(ser, xa);
      s += pathFrom(pts, sx, sy, ser.color, 2.5, ser.dash);
      if (ser.endLabel) {
        var last = pts[pts.length - 1];
        s += txt(sx(last[0]) - 6, sy(last[1]) - 8, ser.endLabel, { tier: "lf-tick", color: ser.color, anchor: "end", bold: true });
      }
    });
    (spec.markers || []).forEach(function (m) {
      s += dot(sx(m.x), sy(m.y), 5.5, m.color || "teal");
      s += txt(sx(m.x) + 10, sy(m.y) - 8, m.label, { tier: "lf-tick", color: m.color || "teal", bold: true });
    });
    (spec.notes || []).forEach(function (n) {
      s += txt(sx(n.x), sy(n.y), n.text, { tier: n.big ? "lf-callout" : "lf-tick", color: n.color || "ink", anchor: n.anchor || "start", bold: !!n.big });
    });
    return { W: Wd, H: Hd, body: s };
  }

  function drawOrigins(spec) {
    var Wd = 800, rowH = 56, padT = 64, padB = 66, Hd = padT + spec.rows.length * rowH + padB;
    var s = "", unit = 120; // px per log10 of the multiplier
    s += txt(24, 34, spec.headline || "", { tier: "lf-callout", color: "ink", bold: true });
    spec.rows.forEach(function (row, i) {
      var y = padT + i * rowH + 26;
      var ox = 24 + (i % 3) * 84 + (i * 17) % 41; // deliberately staggered origins
      var len = unit * Math.log10(row.mult);
      s += lineSeg(ox, y, ox, y - 14, "ink", 2);                       // the origin tick
      s += txt(ox, y + 15, row.base, { tier: "lf-tick", color: "ink2" });
      s += lineSeg(ox, y - 7, ox + len, y - 7, "coral", 3);
      s += '<path d="M' + r2(ox + len) + ' ' + r2(y - 7) + ' l -9 -5 v 10 z" fill="' + escA(C.coral) + '"></path>';
      s += txt(ox + len + 12, y - 3, row.label, { tier: "lf-axis", color: "coral", mono: true, bold: true });
    });
    var fy = Hd - 26;
    s += txt(24, fy, spec.footline || "", { tier: "lf-axis", color: "ink", bold: true });
    return { W: Wd, H: Hd, body: s };
  }

  function drawBudget(spec) {
    var Wd = 800, Hd = spec.h || 240, padL = 26, padR = 26, y0 = 96, bh = 56;
    var s = "", x = padL, span = Wd - padL - padR, thinIdx = 0;
    s += txt(padL, 44, spec.headline || "", { tier: "lf-callout", color: "ink", bold: true });
    spec.segments.forEach(function (seg) {
      var w = span * seg.pct / 100;
      s += '<rect x="' + r2(x) + '" y="' + y0 + '" width="' + r2(Math.max(w - 2, 1.5)) + '" height="' + bh +
           '" rx="3" fill="' + escA(col(seg.color)) + '"></rect>';
      if (w > 60) {
        s += txt(x + w / 2, y0 + bh / 2 - 4, seg.name, { tier: "lf-axis", color: "card", anchor: "middle", bold: true });
        s += txt(x + w / 2, y0 + bh / 2 + 15, seg.pct + "%", { tier: "lf-tick", color: "card", anchor: "middle", mono: true });
      } else { // thin slivers get leader labels below, STAGGERED so two
        // adjacent slivers can never collide (each takes its own row)
        var depth = 20 + thinIdx * 26;
        s += lineSeg(x + w / 2, y0 + bh, x + w / 2, y0 + bh + depth, seg.color, 1.5);
        s += txt(Math.min(x + w / 2 - 8, Wd - 30), y0 + bh + depth + 15, seg.name + " " + seg.pct + "%", { tier: "lf-axis", color: seg.color, bold: true, anchor: "end" });
        thinIdx += 1;
      }
      x += w;
    });
    return { W: Wd, H: Hd, body: s };
  }

  function drawQuadrant(spec) {
    var Wd = 800, Hd = spec.h || 430, pad = 92;
    var x0 = pad, x1 = Wd - 40, y0 = 64, y1 = Hd - pad;
    var cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    var s = "";
    s += '<rect x="' + x0 + '" y="' + y0 + '" width="' + r2(x1 - x0) + '" height="' + r2(y1 - y0) + '" fill="' + escA(C.card) + '" stroke="' + escA(C.ink) + '" stroke-width="1.5"></rect>';
    s += lineSeg(cx, y0, cx, y1, "line", 1.5);
    s += lineSeg(x0, cy, x1, cy, "line", 1.5);
    s += txt(x0, y1 + 26, spec.xlab.lo, { tier: "lf-tick", color: "ink2" });
    s += txt(x1, y1 + 26, spec.xlab.hi, { tier: "lf-tick", color: "ink2", anchor: "end" });
    s += txt((x0 + x1) / 2, y1 + 46, spec.xlab.axis, { tier: "lf-axis", color: "ink", anchor: "middle", bold: true });
    s += '<g transform="rotate(-90 24 ' + r2((y0 + y1) / 2) + ')">' + txt(24, (y0 + y1) / 2, spec.ylab.axis, { tier: "lf-axis", color: "ink", anchor: "middle", bold: true }) + "</g>";
    s += txt(x0 - 10, y1, spec.ylab.lo, { tier: "lf-tick", color: "ink2", anchor: "end" });
    s += txt(x0 - 10, y0 + 12, spec.ylab.hi, { tier: "lf-tick", color: "ink2", anchor: "end" });
    (spec.cluster || []).forEach(function (c, i) {
      var jx = x0 + (x1 - x0) * c.x, jy = y1 - (y1 - y0) * c.y;
      s += dot(jx, jy, 5, "ink2");
    });
    if (spec.clusterLabel) s += txt(x0 + (x1 - x0) * spec.clusterLabel.x, y1 - (y1 - y0) * spec.clusterLabel.y, spec.clusterLabel.text, { tier: "lf-tick", color: "ink2" });
    (spec.points || []).forEach(function (p) {
      var px = x0 + (x1 - x0) * p.x, py = y1 - (y1 - y0) * p.y;
      s += dot(px, py, 9, p.color);
      s += txt(px + (p.dx || 14), py + (p.dy || 4), p.name, { tier: "lf-callout", color: p.color, bold: true, anchor: p.anchor || "start" });
      if (p.sub) s += txt(px + (p.dx || 14), py + (p.dy || 4) + 18, p.sub, { tier: "lf-tick", color: "ink2", anchor: p.anchor || "start" });
    });
    return { W: Wd, H: Hd, body: s };
  }

  function drawRuler(spec) {
    var Wd = 800, Hd = spec.h || 400, padL = 46, padR = 46;
    var ax = { min: spec.axis.min, max: spec.axis.max, log: true };
    var sx = scaleFor(ax, padL, Wd - padR);
    // Vertical layout, top to bottom, with the pair row WELL CLEAR of the
    // axis labels (the first cut collided them; caught at render-and-look):
    // span label 50 / bracket 60 / names 118 / subs 135 / dots 150 /
    // axis 230 / ticks 254 / axis label 276 / pair label 318 / pair 330 / 354.
    var yA = 150, axisY = 230, yB = 330, s = "";
    s += lineSeg(padL, axisY, Wd - padR, axisY, "ink", 1.5);
    decadeTicks(ax).forEach(function (v) {
      s += lineSeg(sx(v), axisY - 5, sx(v), axisY + 5, "ink", 1.5);
      s += txt(sx(v), axisY + 24, fmtPow(v), { tier: "lf-tick", color: "ink2", anchor: "middle", mono: true });
    });
    s += txt((padL + Wd - padR) / 2, axisY + 46, spec.axis.label, { tier: "lf-axis", color: "ink2", anchor: "middle" });
    // row A points (at-target)
    (spec.points || []).forEach(function (p) {
      s += lineSeg(sx(p.v), yA, sx(p.v), axisY, p.color, 1.5, "3 3", 0.6);
      s += dot(sx(p.v), yA, 8, p.color);
      s += txt(sx(p.v), yA - 32, p.name, { tier: "lf-axis", color: p.color, anchor: "middle", bold: true });
      s += txt(sx(p.v), yA - 15, p.sub, { tier: "lf-tick", color: "ink2", anchor: "middle", mono: true });
    });
    // span bracket over row A
    if (spec.span) {
      var b0 = sx(spec.span.lo), b1 = sx(spec.span.hi), by = yA - 90;
      s += lineSeg(b0, by, b1, by, "teal", 2);
      s += lineSeg(b0, by, b0, by + 8, "teal", 2);
      s += lineSeg(b1, by, b1, by + 8, "teal", 2);
      s += txt((b0 + b1) / 2, by - 10, spec.span.label, { tier: "lf-callout", color: "teal", anchor: "middle", bold: true });
    }
    // row B: the accounting pair on the same axis
    if (spec.pair) {
      var p0 = sx(spec.pair.lo), p1 = sx(spec.pair.hi);
      s += lineSeg(p0, yB, p1, yB, "ink2", 2, "5 4");
      s += dot(p0, yB, 7, "ink2", true);
      s += dot(p1, yB, 7, "ink2", true);
      s += txt(p0, yB + 24, spec.pair.loLab, { tier: "lf-tick", color: "ink2", anchor: "middle", mono: true });
      s += txt(p1, yB + 24, spec.pair.hiLab, { tier: "lf-tick", color: "ink2", anchor: "middle", mono: true });
      s += txt((p0 + p1) / 2, yB - 12, spec.pair.label, { tier: "lf-axis", color: "ink", anchor: "middle", bold: true });
    }
    return { W: Wd, H: Hd, body: s };
  }

  // ------------------------------------------------------------- dispatch ---
  function computeQC(spec) {
    var f;
    if (spec.kind === "lines") f = drawLines(spec);
    else if (spec.kind === "origins") f = drawOrigins(spec);
    else if (spec.kind === "budget") f = drawBudget(spec);
    else if (spec.kind === "quadrant") f = drawQuadrant(spec);
    else if (spec.kind === "ruler") f = drawRuler(spec);
    else throw new Error('qcwall: unknown kind "' + spec.kind + '"');
    f.ariaLabel = spec.title || ("QC figure: " + spec.kind);
    return f;
  }

  function renderQCPosterSVG(spec) {
    if (typeof spec === "string") { try { spec = JSON.parse(spec); } catch (e) { return ""; } }
    if (!spec || !spec.kind) return "";
    var f = computeQC(spec);
    return '<svg viewBox="0 0 ' + f.W + " " + f.H + '" width="100%" class="lf-svg" role="img" aria-label="' +
      escA(f.ariaLabel) + '" style="background:' + escA(spec.stage || C.card) + '">' + f.body + "</svg>";
  }

  // Live renderer (lightbox): SAME string, re-mounted — a static-reading figure's
  // ceiling is the floor at overlay size. No animation state, so no __lfHandle.
  function renderQC(container, spec) {
    if (typeof spec === "string") { try { spec = JSON.parse(spec); } catch (e) { return; } }
    if (DF.dedupPoster) DF.dedupPoster(container);
    var host = document.createElement("div");
    host.innerHTML = renderQCPosterSVG(spec);
    container.appendChild(host.firstChild);
  }

  DF.renderQC = renderQC;
  DF.registerPoster("qc", renderQCPosterSVG);
  DF.registerRenderer("qc", renderQC);
})();
