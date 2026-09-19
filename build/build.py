#!/usr/bin/env python3
"""Build Lab.Works static site into the repository root.  Usage:  python3 build/build.py"""
import os, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import DOMAIN
from data import CATEGORIES, TOOLS, GUIDES
import pages_core as pc
import pages_more as pm

import layout
ROOT = os.environ.get("LW_OUT") or os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
import re

def w(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return rel

pages = {}
pages["index.html"] = pc.home()
pages["tests.html"] = pc.tests_page()
pages["quote.html"] = pc.quote_page()
pages["directory.html"] = pc.directory_page()
pages["list-your-lab.html"] = pc.list_lab_page()
for c in CATEGORIES:
    pages[f'testing/{c["slug"]}.html'] = pc.category_page(c)
pages["tools/index.html"] = pm.tools_index()
for t in TOOLS:
    pages[f'tools/{t["slug"]}.html'] = pm.tool_page(t)
pages["guides/index.html"] = pm.guides_index()
for g in GUIDES:
    pages[f'guides/{g["slug"]}.html'] = pm.guide_page(g)
pages["videos.html"] = pm.videos_page()
pages["equipment.html"] = pm.equipment_page()
pages["jobs.html"] = pm.jobs_page()
pages["careers.html"] = pm.careers_page()
pages["contests.html"] = pm.contests_page()
pages["support.html"] = pm.support_page()
pages["advertise.html"] = pm.advertise_page()
pages["about.html"] = pm.about_page()
pages["contact.html"] = pm.contact_page()
pages["privacy.html"] = pm.legal_page("privacy", "Privacy Policy", pm.PRIVACY)
pages["terms.html"] = pm.legal_page("terms", "Terms of Use", pm.TERMS)
pages["disclaimer.html"] = pm.legal_page("disclaimer", "Disclaimer", pm.DISCLAIMER)
pages["thanks.html"] = pm.thanks_page()
pages["404.html"] = pm.notfound_page()

def to_jekyll(rel, html):
    nav = re.search(r"<!--LW:NAV:(.*?)-->\n?", html)
    js = re.search(r"<!--LW:JS:(.*?)-->\n?", html)
    extra = ""
    if nav and nav.group(1): extra += f"nav: {json.dumps(nav.group(1))}\n"
    if js: extra += f"extra_js: {json.dumps(js.group(1))}\n"
    if rel in ("thanks.html", "404.html"): extra += 'robots: "noindex"\n'
    if rel == "404.html": extra += "permalink: /404.html\n"
    html = re.sub(r"<!--LW:(NAV|JS):.*?-->\n?", "", html)
    assert html.startswith("---\n")
    return "---\n" + extra + html[4:]

for rel, html in pages.items():
    w(rel, to_jekyll(rel, html) if layout.JEKYLL else html)
if layout.JEKYLL:
    for rel, c in layout.jekyll_scaffold().items():
        w(rel, c)
    nj = os.path.join(ROOT, ".nojekyll")
    if os.path.exists(nj): os.remove(nj)

# ---- Search index (URLs relative to site root; fixed up per page depth at runtime) ----
idx = []
for c in CATEGORIES:
    idx.append({"t": c["name"], "d": c["short"], "c": "Lab testing", "u": f'testing/{c["slug"]}.html', "k": " ".join(t[0] for t in c["tests"]) + " " + c["key"]})
    for t in c["tests"]:
        idx.append({"t": t[0], "d": f'{c["name"]} · {t[1]} · {t[2]}', "c": "Test", "u": f'testing/{c["slug"]}.html#tests', "k": c["key"]})
for t in TOOLS:
    idx.append({"t": t["name"], "d": t["short"], "c": "Calculator", "u": f'tools/{t["slug"]}.html', "k": t["kw"]})
for g in GUIDES:
    idx.append({"t": g["title"], "d": g["desc"], "c": "Guide", "u": f'guides/{g["slug"]}.html', "k": g["cat"]})
for u, t, d in [("quote.html", "Request free lab quotes", "Get matched with accredited labs"), ("directory.html", "Find a testing lab", "Lab directory & accreditation checks"),
                ("list-your-lab.html", "List your lab", "Get qualified testing requests"), ("jobs.html", "Lab jobs & alerts", "Science careers and job alerts"),
                ("contests.html", "Science contests & prizes", "Enter the Lab.Works Science Challenge"), ("support.html", "Donate / support", "Support free science tools"),
                ("equipment.html", "Lab equipment buyer's guides", "Centrifuges, pipettes, balances, microscopes"), ("videos.html", "Lab technique videos", "Pipetting, PCR, dilution tutorials"),
                ("advertise.html", "Advertise", "Media kit and sponsorships"), ("careers.html", "Work with us", "Writers, video creators, developers")]:
    idx.append({"t": t, "d": d, "c": "Page", "u": u, "k": ""})
w("assets/js/search-index.js", "/* generated */\n(function(){var d=" + json.dumps(idx, ensure_ascii=False) +
  ";var s=document.currentScript&&document.currentScript.getAttribute('src')||'';var pre=s.split('assets/js/')[0];" +
  "window.LW_INDEX=d.map(function(x){return Object.assign({},x,{u:pre+x.u})});})();\n")

# ---- SEO / hosting files ----
urls = [r for r in pages if r not in ("404.html", "thanks.html")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for r in urls:
    pr = "1.0" if r == "index.html" else ("0.9" if r in ("quote.html", "tools/index.html", "tests.html") else "0.7")
    loc = f"{DOMAIN}/{r}".replace("/index.html", "/")
    sm += f"  <url><loc>{loc}</loc><lastmod>2026-09-19</lastmod><priority>{pr}</priority></url>\n"
sm += "</urlset>\n"
w("sitemap.xml", sm)
w("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thanks.html\nDisallow: /build/\n\nSitemap: {DOMAIN}/sitemap.xml\n")
if not os.path.exists(os.path.join(ROOT, "ads.txt")):
    w("ads.txt", "# Replace with your AdSense publisher line after approval, e.g.:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
if not layout.JEKYLL: w(".nojekyll", "")
w("manifest.webmanifest", json.dumps({"name": "Lab.Works", "short_name": "Lab.Works", "start_url": "./index.html", "display": "standalone",
   "background_color": "#07111d", "theme_color": "#0ea5a4", "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))
w("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0ea5a4"/><stop offset=".55" stop-color="#2563eb"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="url(#g)"/><path d="M26 14h12M28 14v14L17 47a4 4 0 0 0 3.5 6h23a4 4 0 0 0 3.5-6L36 28V14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="29" cy="43" r="3" fill="#a3e635"/><circle cx="37" cy="38" r="2" fill="#a3e635"/></svg>')
w("assets/img/og.svg", '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0ea5a4"/><stop offset=".55" stop-color="#2563eb"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs><rect width="1200" height="630" fill="#07111d"/><rect x="60" y="60" width="1080" height="510" rx="40" fill="url(#g)" opacity=".18"/><text x="100" y="300" font-family="Arial, sans-serif" font-size="110" font-weight="700" fill="#fff">Lab.Works</text><text x="100" y="390" font-family="Arial, sans-serif" font-size="40" fill="#b4c3d4">Lab testing quotes · free calculators · lab know-how</text></svg>')
print(f"Built {len(pages)} pages into {ROOT}")
