/* Lab.Works — calculator engine. Each <form data-calc="name"> gets live results. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  function num(f, n) { var el = f.elements[n]; if (!el) return NaN; var v = String(el.value).trim().replace(",", "."); return v === "" ? NaN : Number(v); }
  function val(f, n) { var el = f.elements[n]; return el ? el.value : ""; }
  function fmt(x, d) {
    if (!isFinite(x)) return "—";
    var a = Math.abs(x);
    if (a !== 0 && (a < 1e-3 || a >= 1e7)) return x.toExponential(d == null ? 3 : d);
    return Number(x.toFixed(d == null ? 4 : d)).toLocaleString(undefined, { maximumFractionDigits: d == null ? 4 : d });
  }
  var VOL = { L: 1, mL: 1e-3, "µL": 1e-6, nL: 1e-9 };
  var CONC = { M: 1, mM: 1e-3, "µM": 1e-6, nM: 1e-9 };
  var MASS = { kg: 1e3, g: 1, mg: 1e-3, "µg": 1e-6, ng: 1e-9 };
  function bestMass(g) { var u = ["kg","g","mg","µg","ng"]; for (var i = 0; i < u.length; i++) if (Math.abs(g) >= MASS[u[i]] || i === u.length - 1) return fmt(g / MASS[u[i]], 4) + " " + u[i]; }
  function bestVol(l) { var u = ["L","mL","µL","nL"]; for (var i = 0; i < u.length; i++) if (Math.abs(l) >= VOL[u[i]] || i === u.length - 1) return fmt(l / VOL[u[i]], 4) + " " + u[i]; }
  function bestConc(m) { var u = ["M","mM","µM","nM"]; for (var i = 0; i < u.length; i++) if (Math.abs(m) >= CONC[u[i]] || i === u.length - 1) return fmt(m / CONC[u[i]], 4) + " " + u[i]; }

  /* ---- Atomic weights (IUPAC 2021 conventional/standard) ---- */
  var AW = {H:1.008,He:4.0026,Li:6.94,Be:9.0122,B:10.81,C:12.011,N:14.007,O:15.999,F:18.998,Ne:20.180,Na:22.990,Mg:24.305,Al:26.982,Si:28.085,P:30.974,S:32.06,Cl:35.45,Ar:39.948,K:39.098,Ca:40.078,Sc:44.956,Ti:47.867,V:50.942,Cr:51.996,Mn:54.938,Fe:55.845,Co:58.933,Ni:58.693,Cu:63.546,Zn:65.38,Ga:69.723,Ge:72.630,As:74.922,Se:78.971,Br:79.904,Kr:83.798,Rb:85.468,Sr:87.62,Y:88.906,Zr:91.224,Nb:92.906,Mo:95.95,Tc:98,Ru:101.07,Rh:102.91,Pd:106.42,Ag:107.87,Cd:112.41,In:114.82,Sn:118.71,Sb:121.76,Te:127.60,I:126.90,Xe:131.29,Cs:132.91,Ba:137.33,La:138.91,Ce:140.12,Pr:140.91,Nd:144.24,Pm:145,Sm:150.36,Eu:151.96,Gd:157.25,Tb:158.93,Dy:162.50,Ho:164.93,Er:167.26,Tm:168.93,Yb:173.05,Lu:174.97,Hf:178.49,Ta:180.95,W:183.84,Re:186.21,Os:190.23,Ir:192.22,Pt:195.08,Au:196.97,Hg:200.59,Tl:204.38,Pb:207.2,Bi:208.98,Po:209,At:210,Rn:222,Fr:223,Ra:226,Ac:227,Th:232.04,Pa:231.04,U:238.03,Np:237,Pu:244,Am:243,Cm:247,Bk:247,Cf:251,Es:252,Fm:257};
  function parseFormula(str) {
    var s = str.replace(/\s+/g, "").replace(/[·*•.]/g, "·");
    var parts = s.split("·"), total = {};
    parts.forEach(function (part) {
      var m = part.match(/^(\d+)(.*)$/), mult = 1;
      if (m) { mult = +m[1]; part = m[2]; }
      var counts = parseGroup(part);
      Object.keys(counts).forEach(function (k) { total[k] = (total[k] || 0) + counts[k] * mult; });
    });
    return total;
  }
  function parseGroup(s) {
    var stack = [{}], i = 0;
    while (i < s.length) {
      var ch = s[i];
      if (ch === "(" || ch === "[") { stack.push({}); i++; }
      else if (ch === ")" || ch === "]") {
        i++; var n = ""; while (i < s.length && /\d/.test(s[i])) n += s[i++];
        var g = stack.pop(), top = stack[stack.length - 1], k = n ? +n : 1;
        if (!top) throw new Error("Unbalanced brackets");
        Object.keys(g).forEach(function (e) { top[e] = (top[e] || 0) + g[e] * k; });
      } else if (/[A-Z]/.test(ch)) {
        var el = ch; i++; while (i < s.length && /[a-z]/.test(s[i])) el += s[i++];
        if (!(el in AW)) throw new Error("Unknown element: " + el);
        var d = ""; while (i < s.length && /[\d.]/.test(s[i])) d += s[i++];
        var t = stack[stack.length - 1]; t[el] = (t[el] || 0) + (d ? +d : 1);
      } else throw new Error("Unexpected character: " + ch);
    }
    if (stack.length !== 1) throw new Error("Unbalanced brackets");
    return stack[0];
  }
  function molarMass(str) { var c = parseFormula(str), m = 0; Object.keys(c).forEach(function (e) { m += AW[e] * c[e]; }); return { mw: m, c: c }; }
  window.LWmolarMass = molarMass;

  var T975 = [0,12.706,4.303,3.182,2.776,2.571,2.447,2.365,2.306,2.262,2.228,2.201,2.179,2.160,2.145,2.131,2.120,2.110,2.101,2.093,2.086,2.080,2.074,2.069,2.064,2.060,2.056,2.052,2.048,2.045,2.042];
  function tcrit(df) { return df <= 30 ? T975[df] : (df <= 60 ? 2.00 : (df <= 120 ? 1.98 : 1.96)); }

  var CALCS = {
    molarity: function (f) {
      var M = num(f, "conc") * CONC[val(f, "concU")], V = num(f, "vol") * VOL[val(f, "volU")], mw = num(f, "mw");
      var mode = val(f, "mode");
      if (mode === "mass") {
        if (!(M > 0 && V > 0 && mw > 0)) return "Enter concentration, volume and molecular weight.";
        var g = M * V * mw;
        return "Weigh out <b>" + bestMass(g) + "</b> and dissolve to a final volume of " + bestVol(V) + ".<br><small>moles = " + fmt(M * V, 6) + " mol</small>";
      }
      var mass = num(f, "mass") * MASS[val(f, "massU")];
      if (!(mass > 0 && V > 0 && mw > 0)) return "Enter mass, volume and molecular weight.";
      return "Concentration: <b>" + bestConc(mass / mw / V) + "</b><br><small>" + fmt(mass / mw, 6) + " mol in " + bestVol(V) + "</small>";
    },
    dilution: function (f) {
      var c1 = num(f, "c1"), v1 = num(f, "v1"), c2 = num(f, "c2"), v2 = num(f, "v2"), vu = val(f, "vu"), cu = val(f, "cu");
      var blanks = [c1, v1, c2, v2].filter(function (x) { return isNaN(x); }).length;
      if (blanks !== 1) return "Fill in exactly three of the four values — leave the unknown blank.";
      if (isNaN(v1)) { if (c2 > c1) return "C2 cannot exceed C1 for a dilution."; var r = c2 * v2 / c1; return "Take <b>" + fmt(r) + " " + vu + "</b> of stock and add <b>" + fmt(v2 - r) + " " + vu + "</b> of diluent (final " + fmt(v2) + " " + vu + ").<br><small>Dilution factor " + fmt(c1 / c2, 2) + "×</small>"; }
      if (isNaN(c1)) return "Stock concentration C1 = <b>" + fmt(c2 * v2 / v1) + " " + cu + "</b>";
      if (isNaN(c2)) return "Final concentration C2 = <b>" + fmt(c1 * v1 / v2) + " " + cu + "</b><br><small>Dilution factor " + fmt(v2 / v1, 2) + "×</small>";
      return "Final volume V2 = <b>" + fmt(c1 * v1 / c2) + " " + vu + "</b> (add " + fmt(c1 * v1 / c2 - v1) + " " + vu + " diluent)";
    },
    serial: function (f) {
      var c0 = num(f, "c0"), fac = num(f, "factor"), n = Math.min(24, Math.round(num(f, "steps"))), vf = num(f, "vfinal"), u = val(f, "cu");
      if (!(c0 > 0 && fac > 1 && n > 0 && vf > 0)) return "Enter a starting concentration, a dilution factor > 1, number of steps and final volume per tube.";
      var transfer = vf / (fac - 1), diluent = vf;
      var rows = "<table><tr><th>Tube</th><th>Concentration</th><th>Dilution</th></tr>";
      for (var i = 1; i <= n; i++) rows += "<tr><td>" + i + "</td><td>" + fmt(c0 / Math.pow(fac, i)) + " " + u + "</td><td>1:" + fmt(Math.pow(fac, i), 0) + "</td></tr>";
      return "Pre-fill each tube with <b>" + fmt(diluent) + " µL</b> of diluent, then transfer <b>" + fmt(transfer) + " µL</b> from tube to tube, mixing each time. Each tube (except the last) ends with " + fmt(vf) + " µL; discard " + fmt(transfer) + " µL from the final tube.<div style='overflow-x:auto'>" + rows + "</table></div>";
    },
    molarmass: function (f) {
      var s = val(f, "formula").trim();
      if (!s) return "Type a formula, e.g. NaCl, C6H12O6, CuSO4·5H2O, Ca(OH)2.";
      try {
        var r = molarMass(s), rows = "<table><tr><th>Element</th><th>Count</th><th>Mass</th><th>% mass</th></tr>";
        Object.keys(r.c).forEach(function (e) { var m = AW[e] * r.c[e]; rows += "<tr><td>" + e + "</td><td>" + fmt(r.c[e], 3) + "</td><td>" + fmt(m, 3) + "</td><td>" + fmt(m / r.mw * 100, 2) + "%</td></tr>"; });
        return "Molar mass of " + s + ": <b>" + fmt(r.mw, 3) + " g/mol</b><div style='overflow-x:auto'>" + rows + "</table></div>";
      } catch (e) { return "⚠ " + e.message; }
    },
    buffer: function (f) {
      var pKa = num(f, "pka"), pH = num(f, "ph"), C = num(f, "total") * CONC[val(f, "totalU")], V = num(f, "vol") * VOL[val(f, "volU")];
      var mwA = num(f, "mwa"), mwB = num(f, "mwb");
      if (!(isFinite(pKa) && isFinite(pH) && C > 0 && V > 0)) return "Enter pKa, target pH, total buffer concentration and volume.";
      var ratio = Math.pow(10, pH - pKa), base = C * ratio / (1 + ratio), acid = C - base;
      var out = "Ratio [A⁻]/[HA] = <b>" + fmt(ratio, 3) + "</b><br>Conjugate base: " + bestConc(base) + " → " + fmt(base * V, 6) + " mol" + (mwB > 0 ? " = <b>" + bestMass(base * V * mwB) + "</b>" : "") +
        "<br>Weak acid: " + bestConc(acid) + " → " + fmt(acid * V, 6) + " mol" + (mwA > 0 ? " = <b>" + bestMass(acid * V * mwA) + "</b>" : "");
      if (Math.abs(pH - pKa) > 1) out += "<br><small>⚠ Target pH is more than 1 unit from pKa — buffering capacity will be poor. Choose a buffer with pKa closer to your pH.</small>";
      return out + "<br><small>Always verify with a calibrated pH meter and adjust.</small>";
    },
    rcf: function (f) {
      var r = num(f, "radius") * (val(f, "radiusU") === "mm" ? 0.1 : 1), rpm = num(f, "rpm"), g = num(f, "g");
      if (!(r > 0)) return "Enter the rotor radius (from rotor manual, centre to tube bottom).";
      if (rpm > 0 && isNaN(g)) return "RCF = <b>" + fmt(1.118e-5 * r * rpm * rpm, 0) + " × g</b>";
      if (g > 0 && isNaN(rpm)) return "Speed = <b>" + fmt(Math.sqrt(g / (1.118e-5 * r)), 0) + " RPM</b>";
      return "Fill in either RPM or g-force (leave the other blank).";
    },
    pcr: function (f) {
      var n = num(f, "n"), over = num(f, "overage") / 100, vol = num(f, "rxn");
      if (!(n > 0 && vol > 0)) return "Enter number of reactions and reaction volume.";
      var k = n * (1 + (over || 0));
      var comp = [["Buffer (10×)", vol / 10], ["dNTPs (10 mM each → 0.2 mM)", vol * 0.02], ["Forward primer (10 µM → 0.5 µM)", vol * 0.05], ["Reverse primer (10 µM → 0.5 µM)", vol * 0.05],
        ["MgCl₂ (25 mM → 1.5 mM, if not in buffer)", num(f, "mg") ? vol * 0.06 : 0], ["DNA polymerase (5 U/µL → 1.25 U/50 µL)", vol * 0.005]];
      var tmpl = num(f, "template") || 0, used = 0, rows = "<table><tr><th>Component</th><th>1 rxn (µL)</th><th>Master mix (µL)</th></tr>";
      comp.forEach(function (c) { if (!c[1]) return; used += c[1]; rows += "<tr><td>" + c[0] + "</td><td>" + fmt(c[1], 2) + "</td><td>" + fmt(c[1] * k, 1) + "</td></tr>"; });
      var water = vol - used - tmpl;
      if (water < 0) return "⚠ Template volume too large for this reaction volume.";
      rows += "<tr><td>Nuclease-free water</td><td>" + fmt(water, 2) + "</td><td>" + fmt(water * k, 1) + "</td></tr>";
      rows += "<tr><td><em>Template (add separately)</em></td><td>" + fmt(tmpl, 2) + "</td><td>—</td></tr></table>";
      return "Master mix for <b>" + fmt(k, 1) + "</b> reactions (" + fmt(n, 0) + " + " + fmt((over || 0) * 100, 0) + "% overage). Dispense <b>" + fmt(vol - tmpl, 2) + " µL</b> per tube.<div style='overflow-x:auto'>" + rows + "</div>";
    },
    cells: function (f) {
      var live = num(f, "live"), dead = num(f, "dead") || 0, sq = num(f, "squares"), dil = num(f, "dilution") || 1, target = num(f, "target"), wells = num(f, "wells") || 1, per = num(f, "perwell");
      if (!(live >= 0 && sq > 0)) return "Enter live cell count and number of squares counted.";
      var conc = live / sq * dil * 1e4, total = (live + dead) / sq * dil * 1e4, via = (live + dead) ? live / (live + dead) * 100 : 0;
      var out = "Live cells: <b>" + fmt(conc, 0) + " cells/mL</b> (" + fmt(conc, 2) + ")<br>Total cells: " + fmt(total, 0) + " cells/mL · Viability: <b>" + fmt(via, 1) + "%</b>";
      if (target > 0 && per > 0 && conc > 0) {
        var need = target * wells, vcell = need / conc * 1000, vtot = per * wells;
        out += "<br><br>To seed " + fmt(wells, 0) + " well(s) at " + fmt(target, 0) + " cells each in " + fmt(per) + " mL: mix <b>" + fmt(vcell, 1) + " µL</b> cell suspension with <b>" + fmt(vtot * 1000 - vcell, 1) + " µL</b> medium.";
        if (vcell > vtot * 1000) out += "<br><small>⚠ Suspension too dilute — concentrate by centrifugation first.</small>";
      }
      return out;
    },
    stats: function (f) {
      var xs = val(f, "data").split(/[\s,;]+/).map(Number).filter(function (x) { return isFinite(x) && x !== ""; });
      xs = val(f, "data").split(/[\s,;]+/).filter(function (s) { return s !== "" && isFinite(Number(s)); }).map(Number);
      var n = xs.length; if (n < 2) return "Paste at least two numbers (comma, space or newline separated).";
      var mean = xs.reduce(function (a, b) { return a + b; }, 0) / n, s = xs.slice().sort(function (a, b) { return a - b; });
      var med = n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2, ss = xs.reduce(function (a, x) { return a + (x - mean) * (x - mean); }, 0);
      var sd = Math.sqrt(ss / (n - 1)), sem = sd / Math.sqrt(n), ci = tcrit(n - 1) * sem;
      var g = Math.max(Math.abs(s[0] - mean), Math.abs(s[n - 1] - mean)) / sd, susp = Math.abs(s[0] - mean) > Math.abs(s[n - 1] - mean) ? s[0] : s[n - 1];
      return "<table><tr><td>n</td><td><b>" + n + "</b></td></tr><tr><td>Mean</td><td><b>" + fmt(mean) + "</b></td></tr><tr><td>Median</td><td>" + fmt(med) + "</td></tr><tr><td>SD (sample)</td><td><b>" + fmt(sd) + "</b></td></tr><tr><td>SEM</td><td>" + fmt(sem) +
        "</td></tr><tr><td>95% CI of mean</td><td>" + fmt(mean - ci) + " to " + fmt(mean + ci) + "</td></tr><tr><td>CV %</td><td>" + fmt(sd / Math.abs(mean) * 100, 2) + "%</td></tr><tr><td>Min / Max</td><td>" + fmt(s[0]) + " / " + fmt(s[n - 1]) +
        "</td></tr><tr><td>Grubbs G (most extreme: " + fmt(susp) + ")</td><td>" + fmt(g, 3) + "</td></tr></table>";
    },
    nucleic: function (f) {
      var a260 = num(f, "a260"), a280 = num(f, "a280"), a230 = num(f, "a230"), type = val(f, "type"), dil = num(f, "dil") || 1, path = num(f, "path") || 1;
      var factor = type === "custom" ? num(f, "custom") : +type;
      if (!(a260 >= 0 && factor > 0)) return "Enter A260 and select a sample type.";
      var c = a260 * factor * dil / path, out = "Concentration: <b>" + fmt(c, 2) + " ng/µL</b> (" + fmt(c, 2) + " µg/mL)";
      if (a280 > 0) { var r = a260 / a280; out += "<br>A260/A280 = <b>" + fmt(r, 2) + "</b> " + (r >= 1.8 ? "✓ pure (DNA ≈1.8, RNA ≈2.0)" : "⚠ possible protein/phenol contamination"); }
      if (a230 > 0) { var r2 = a260 / a230; out += "<br>A260/A230 = <b>" + fmt(r2, 2) + "</b> " + (r2 >= 1.8 ? "✓ acceptable (2.0–2.2 ideal)" : "⚠ possible salt/guanidine/carbohydrate carry-over"); }
      return out;
    },
    beer: function (f) {
      var A = num(f, "A"), e = num(f, "eps"), l = num(f, "l"), c = num(f, "c");
      var b = [A, e, l, c].filter(function (x) { return isNaN(x); }).length;
      if (b !== 1) return "Fill three of A, ε, l, c — leave the unknown blank.";
      if (isNaN(A)) return "Absorbance A = <b>" + fmt(e * l * c) + "</b>";
      if (isNaN(c)) return "Concentration c = <b>" + fmt(A / (e * l)) + " mol/L</b> (" + bestConc(A / (e * l)) + ")";
      if (isNaN(e)) return "Molar absorptivity ε = <b>" + fmt(A / (l * c)) + " L·mol⁻¹·cm⁻¹</b>";
      return "Path length l = <b>" + fmt(A / (e * c)) + " cm</b>";
    },
    ppm: function (f) {
      var v = num(f, "value"), from = val(f, "from"), mw = num(f, "mw"), d = num(f, "density") || 1;
      if (isNaN(v)) return "Enter a value to convert.";
      // normalise to mg/L
      var mgL;
      switch (from) {
        case "mgL": case "ppm": mgL = v; break;
        case "ugL": case "ppb": mgL = v / 1000; break;
        case "gL": mgL = v * 1000; break;
        case "pct": mgL = v * 10000; break; // % w/v
        case "M": if (!(mw > 0)) return "Molecular weight is required to convert from molarity."; mgL = v * mw * 1000; break;
        case "mM": if (!(mw > 0)) return "Molecular weight is required to convert from molarity."; mgL = v * mw; break;
      }
      var rows = [["mg/L", mgL], ["ppm (≈ mg/L in water)", mgL / d], ["µg/L (ppb)", mgL * 1000 / d], ["g/L", mgL / 1000], ["% w/v", mgL / 10000]];
      if (mw > 0) { rows.push(["Molarity (M)", mgL / 1000 / mw]); rows.push(["Millimolar (mM)", mgL / mw]); rows.push(["Micromolar (µM)", mgL / mw * 1000]); }
      return "<table>" + rows.map(function (r) { return "<tr><td>" + r[0] + "</td><td><b>" + fmt(r[1], 6) + "</b></td></tr>"; }).join("") + "</table><small>ppm/ppb assume a dilute aqueous solution (density " + d + " g/mL).</small>";
    }
  };

  document.querySelectorAll("form[data-calc]").forEach(function (f) {
    var fn = CALCS[f.getAttribute("data-calc")], out = $(".out", f);
    function run() { try { out.innerHTML = fn(f); } catch (e) { out.textContent = "⚠ " + e.message; } }
    f.addEventListener("input", run); f.addEventListener("change", run);
    f.addEventListener("submit", function (e) { e.preventDefault(); run(); });
    f.addEventListener("reset", function () { setTimeout(run, 0); });
    var mode = f.elements.mode;
    if (mode) { var sync = function () { f.querySelectorAll("[data-mode]").forEach(function (el) { el.style.display = el.getAttribute("data-mode") === mode.value ? "" : "none"; }); }; mode.addEventListener("change", sync); sync(); }
    var preset = f.querySelector("[data-preset]");
    if (preset) preset.addEventListener("change", function () { var p = preset.value.split("|"); if (p[0]) { f.elements.pka.value = p[0]; if (p[1]) f.elements.mwa.value = p[1]; if (p[2]) f.elements.mwb.value = p[2]; run(); } });
    var mwbtn = f.querySelector("[data-mw-lookup]");
    if (mwbtn) mwbtn.addEventListener("click", function () { var s = prompt("Chemical formula (e.g. NaCl, C6H12O6, CuSO4·5H2O):"); if (!s) return; try { f.elements.mw.value = molarMass(s).mw.toFixed(3); run(); } catch (e) { alert(e.message); } });
    run();
  });
})();
