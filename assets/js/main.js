/* Lab.Works — core interactions */
(function () {
  "use strict";
  var C = window.LW_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
  };

  /* ---------- Private inbox (never rendered in the page) ---------- */
  var _k = [96,114,117,96,120,101,124,100,118,38,87,112,122,118,126,123,57,116,120,122];
  function inbox() { return _k.map(function (c) { return String.fromCharCode(c ^ 23); }).join(""); }
  function endpoint() { return "https://formsubmit.co/ajax/" + inbox(); }
  function openMail(subject, body) {
    window.location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(subject || "Lab.Works enquiry") +
      (body ? "&body=" + encodeURIComponent(body) : "");
  }
  window.LW = { openMail: openMail };

  /* Elements with data-mail open the mail client without exposing the address */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-mail]");
    if (!a) return;
    e.preventDefault();
    openMail(a.getAttribute("data-mail") || "Lab.Works enquiry");
  });

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  var saved = store.get("lw-theme");
  if (saved) root.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var dark = root.getAttribute("data-theme") === "dark" ||
        (!root.getAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
      var next = dark ? "light" : "dark";
      root.setAttribute("data-theme", next); store.set("lw-theme", next);
    });
  });

  /* ---------- Mobile menu ---------- */
  var burger = $(".burger"), menu = $(".menu");
  if (burger && menu) burger.addEventListener("click", function () {
    var open = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", open);
  });

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: .08 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else $$(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* ---------- Forms → email (FormSubmit AJAX) ---------- */
  function formToObject(form) {
    var o = {}, fd = new FormData(form);
    fd.forEach(function (v, k) {
      if (v instanceof File) return;
      if (o[k]) o[k] = o[k] + ", " + v; else o[k] = v;
    });
    return o;
  }
  function status(form, cls, msg) {
    var s = $(".form-status", form);
    if (!s) { s = document.createElement("div"); s.className = "form-status"; s.setAttribute("role", "status"); form.appendChild(s); }
    s.className = "form-status " + cls; s.textContent = msg;
  }
  function submitForm(form) {
    var hp = form.querySelector("[name=_honey]");
    if (hp && hp.value) return;
    var data = formToObject(form);
    delete data._honey;
    var subject = form.getAttribute("data-subject") || "Lab.Works form";
    data._subject = "[Lab.Works] " + subject + (data.name ? " — " + data.name : "");
    data._template = "table";
    data.form = subject;
    data.page = location.href;
    data.submitted = new Date().toISOString();
    if (data.email) data._replyto = data.email;
    var btn = form.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
    fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false" || j.success === false) throw new Error(j.message || "send failed"); return j; }); })
      .then(function () {
        if (typeof gtag === "function") gtag("event", "generate_lead", { form: subject });
        store.del("lw-draft-" + (form.id || ""));
        var next = form.getAttribute("data-next");
        if (next) { location.href = next; return; }
        status(form, "ok", form.getAttribute("data-ok") || "Thank you! We received your submission and will reply shortly.");
        form.reset();
      })
      .catch(function () {
        status(form, "err", "Our form service didn't respond. Your email app will open with your details pre-filled — just press send.");
        var body = Object.keys(data).filter(function (k) { return k[0] !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
        setTimeout(function () { openMail(data._subject, body); }, 900);
      })
      .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
  }
  $$("form[data-lw-form]").forEach(function (form) {
    if (!form.querySelector("[name=_honey]")) {
      var hp = document.createElement("input"); hp.type = "text"; hp.name = "_honey"; hp.className = "hp"; hp.tabIndex = -1; hp.autocomplete = "off"; hp.setAttribute("aria-hidden", "true");
      form.appendChild(hp);
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      submitForm(form);
    });
  });

  /* ---------- Multi-step wizard ---------- */
  $$("[data-wizard]").forEach(function (wz) {
    var form = wz.tagName === "FORM" ? wz : $("form", wz);
    var steps = $$(".wstep", wz), i = 0, bar = $(".progress i", wz), labels = $$(".step-labels span", wz);
    var key = "lw-draft-" + (form.id || "");
    // restore draft
    try {
      var d = JSON.parse(store.get(key) || "{}");
      Object.keys(d).forEach(function (k) {
        $$("[name='" + k + "']", form).forEach(function (el) {
          if (el.type === "checkbox" || el.type === "radio") el.checked = [].concat(d[k]).indexOf(el.value) > -1;
          else if (el.type !== "file") el.value = d[k];
        });
      });
    } catch (e) {}
    // URL prefill (?cat=water&test=...)
    var qs = new URLSearchParams(location.search);
    qs.forEach(function (v, k) {
      $$("[name='" + k + "']", form).forEach(function (el) {
        if (el.type === "radio" || el.type === "checkbox") { if (el.value === v) el.checked = true; }
        else el.value = v;
      });
    });
    function saveDraft() {
      var o = {};
      $$("input,select,textarea", form).forEach(function (el) {
        if (!el.name || el.name[0] === "_" || el.type === "file") return;
        if (el.type === "checkbox" || el.type === "radio") { if (el.checked) { o[el.name] = o[el.name] ? [].concat(o[el.name], el.value) : el.value; } }
        else o[el.name] = el.value;
      });
      store.set(key, JSON.stringify(o));
    }
    form.addEventListener("change", saveDraft);
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("on", k === n); });
      labels.forEach(function (s, k) { s.classList.toggle("on", k <= n); });
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
      i = n;
    }
    function valid(n) {
      var ok = true;
      $$("input,select,textarea", steps[n]).forEach(function (el) { if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; } });
      var group = steps[n].getAttribute("data-need");
      if (ok && group && !$("[name='" + group + "']:checked", steps[n])) { alert("Please choose at least one option to continue."); ok = false; }
      return ok;
    }
    $$("[data-next-step]", wz).forEach(function (b) { b.addEventListener("click", function () { if (valid(i)) { saveDraft(); show(Math.min(i + 1, steps.length - 1)); wz.scrollIntoView({ behavior: "smooth", block: "start" }); } }); });
    $$("[data-prev-step]", wz).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(i - 1, 0)); }); });
    show(0);
  });

  /* ---------- Site search ---------- */
  var IDX = window.LW_INDEX || [];
  $$("[data-site-search]").forEach(function (inp) {
    var wrap = inp.closest(".search-wrap"), box = wrap && $(".search-results", wrap);
    if (!box) return;
    function run() {
      var q = inp.value.trim().toLowerCase();
      if (q.length < 2) { box.style.display = "none"; return; }
      var terms = q.split(/\s+/);
      var hits = IDX.map(function (p) {
        var hay = (p.t + " " + p.d + " " + p.k).toLowerCase(), s = 0;
        terms.forEach(function (t) { if (hay.indexOf(t) > -1) s += p.t.toLowerCase().indexOf(t) > -1 ? 3 : 1; });
        return { p: p, s: s };
      }).filter(function (h) { return h.s >= terms.length; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 8);
      box.innerHTML = hits.length ? hits.map(function (h) { return '<a href="' + h.p.u + '"><strong>' + h.p.t + '</strong><br><small>' + h.p.c + ' · ' + h.p.d + '</small></a>'; }).join("")
        : '<a href="quote.html?details=' + encodeURIComponent(inp.value) + '"><strong>Can\'t find it? Request a custom lab quote →</strong><br><small>Our team will match your need with accredited labs</small></a>';
      box.style.display = "block";
    }
    inp.addEventListener("input", run); inp.addEventListener("focus", run);
    document.addEventListener("click", function (e) { if (!wrap.contains(e.target)) box.style.display = "none"; });
    var f = inp.closest("form");
    if (f) f.addEventListener("submit", function (e) { e.preventDefault(); var a = $("a", box); if (a) location.href = a.getAttribute("href"); });
  });

  /* ---------- Filterable lists ---------- */
  $$("[data-filter-list]").forEach(function (wrap) {
    var items = $$("[data-tags]", wrap), q = $("[data-filter-q]", wrap), sel = $$("[data-filter-sel]", wrap), chips = $$("[data-chip]", wrap), active = "all";
    function apply() {
      var t = q ? q.value.toLowerCase() : "", n = 0;
      items.forEach(function (it) {
        var tags = it.getAttribute("data-tags").toLowerCase(), txt = it.textContent.toLowerCase(), ok = true;
        if (t && txt.indexOf(t) < 0 && tags.indexOf(t) < 0) ok = false;
        sel.forEach(function (s) { if (s.value && tags.indexOf(s.value.toLowerCase()) < 0) ok = false; });
        if (active !== "all" && tags.indexOf(active) < 0) ok = false;
        it.style.display = ok ? "" : "none"; if (ok) n++;
      });
      var c = $("[data-filter-count]", wrap); if (c) c.textContent = n;
    }
    if (q) q.addEventListener("input", apply);
    sel.forEach(function (s) { s.addEventListener("change", apply); });
    chips.forEach(function (c) { c.addEventListener("click", function () { chips.forEach(function (x) { x.classList.remove("active"); }); c.classList.add("active"); active = c.getAttribute("data-chip"); apply(); }); });
    apply();
  });

  /* ---------- YouTube facades ---------- */
  $$(".video").forEach(function (v) {
    v.addEventListener("click", function () {
      var id = v.getAttribute("data-yt");
      if (id) v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.getAttribute("data-title") || "Video") + '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      else window.open("https://www.youtube.com/results?search_query=" + encodeURIComponent(v.getAttribute("data-q") || "laboratory techniques"), "_blank", "noopener");
    });
  });

  /* ---------- Countdown ---------- */
  $$("[data-countdown]").forEach(function (el) {
    var end = new Date(el.getAttribute("data-countdown")).getTime();
    function tick() {
      var d = Math.max(0, end - Date.now()), s = Math.floor(d / 1000);
      var v = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
      $$("b", el).forEach(function (b, k) { b.textContent = String(v[k]).padStart(2, "0"); });
    }
    tick(); setInterval(tick, 1000);
  });

  /* ---------- Donations ---------- */
  var amt = 25;
  $$("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      $$("[data-amount]").forEach(function (x) { x.classList.remove("active"); }); b.classList.add("active");
      amt = b.getAttribute("data-amount"); var o = $("#donate-custom"); if (o) o.value = amt;
      var f = $("#pledge-amount"); if (f) f.value = amt;
    });
  });
  $$("[data-donate]").forEach(function (b) {
    var via = b.getAttribute("data-donate"), url = (C.donate || {})[via];
    if (!url && via !== "pledge") { b.style.display = "none"; return; }
    b.addEventListener("click", function (e) {
      e.preventDefault();
      if (url) { window.open(url, "_blank", "noopener"); return; }
      var m = $("#pledge"); if (m) { m.scrollIntoView({ behavior: "smooth" }); var f = $("#pledge-amount"); if (f) f.value = ($("#donate-custom") || {}).value || amt; }
    });
  });

  /* ---------- Modal ---------- */
  $$("[data-modal]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); var m = $(b.getAttribute("data-modal")); if (m) { m.classList.add("show"); var s = m.querySelector("[name=plan],[name=item]"); if (s && b.dataset.value) s.value = b.dataset.value; } }); });
  $$(".modal").forEach(function (m) { m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".modal-close")) m.classList.remove("show"); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") $$(".modal.show").forEach(function (m) { m.classList.remove("show"); }); });

  /* ---------- Consent + AdSense + GA4 ---------- */
  function loadAds() {
    if (C.adsenseClient) {
      var s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
      s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
      document.head.appendChild(s);
      $$(".ad-slot").forEach(function (el) {
        var slot = (C.adSlots || {})[el.getAttribute("data-ad") || ""] || "";
        el.classList.add("live");
        el.innerHTML = '<div><div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '"' + (slot ? ' data-ad-slot="' + slot + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"></ins></div>';
        try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
      });
    }
    if (C.ga4) {
      var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4; document.head.appendChild(g);
      window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", C.ga4);
    }
  }
  var consent = store.get("lw-consent"), ck = $(".cookie");
  if (consent === "yes") loadAds();
  else if (!consent && ck) ck.classList.add("show");
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-consent"); store.set("lw-consent", v); if (ck) ck.classList.remove("show"); if (v === "yes") loadAds();
    });
  });

  /* ---------- Misc ---------- */
  $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });
  if (/quote\.html/.test(location.pathname)) $$(".float-cta").forEach(function (e) { e.remove(); });
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var d = { title: document.title, url: location.href };
      if (navigator.share) navigator.share(d).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(function () { b.textContent = "Link copied ✓"; });
    });
  });
  $$("[data-print]").forEach(function (b) { b.addEventListener("click", function () { window.print(); }); });
})();
