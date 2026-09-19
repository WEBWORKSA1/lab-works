"""Shared layout for the Lab.Works static site generator."""
import json, html

SITE = "Lab.Works"
DOMAIN = "https://lab.works"
DOMAIN_CONTACT = "https://web.works/contact"
TAGLINE = "Lab testing quotes, free science calculators & lab know-how"

NAV = [
    ("tests.html", "Lab Tests"),
    ("directory.html", "Find Labs"),
    ("tools/index.html", "Calculators"),
    ("guides/index.html", "Guides"),
    ("videos.html", "Videos"),
    ("equipment.html", "Equipment"),
    ("jobs.html", "Jobs"),
    ("contests.html", "Contests"),
    ("support.html", "Support Us"),
]

def esc(s):
    return html.escape(s, quote=True)

def head(title, desc, path, pre, schema=None, og_type="website"):
    full = f"{title} | {SITE}" if title != SITE else f"{SITE} — {TAGLINE}"
    url = f"{DOMAIN}/{path}".replace("/index.html", "/")
    schemas = ""
    for s in (schema or []):
        schemas += f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0ea5a4">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{pre}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
<script>document.documentElement.className+=' js';try{{var t=localStorage.getItem('lw-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{schemas}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="domain-bar" role="note"><a href="{DOMAIN_CONTACT}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name</a></div>
"""

def header(pre, active):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items += f'<li><a href="{pre}{href}"{cur}>{label}</a></li>'
    return f"""<header class="site-header">
<div class="container nav">
<a class="logo" href="{pre}index.html" aria-label="Lab.Works home"><span class="logo-mark">⚗</span><span>Lab<b>.Works</b></span></a>
<ul class="menu" id="menu">{items}<li><a href="{pre}contact.html">Contact</a></li></ul>
<div class="nav-cta">
<button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">🌓</button>
<a class="btn btn-primary btn-sm btn-sm-hide" href="{pre}quote.html">Get Free Quotes</a>
<button class="icon-btn burger" aria-label="Open menu" aria-controls="menu" aria-expanded="false">☰</button>
</div>
</div>
</header>
<main id="main">
"""

def ad(kind="inArticle"):
    return f'<div class="ad-slot" data-ad="{kind}" aria-label="Advertisement"><span>Advertisement</span></div>'

def footer(pre):
    return f"""</main>
<section class="section-alt" aria-label="Newsletter">
<div class="container">
<div class="grid g2" style="align-items:center">
<div><span class="kicker">The Lab Notes newsletter</span><h2 class="mt0">Protocols, tools & testing insights — every week.</h2><p class="muted mb0">New calculators, lab-testing guides, job picks, contest alerts and exclusive supplier deals. Free. Unsubscribe anytime.</p></div>
<form class="form" data-lw-form data-subject="Newsletter signup" data-ok="You're in! Watch your inbox for the next Lab Notes.">
<div class="newsletter"><label class="sr-only" for="nl-email">Email</label><input id="nl-email" type="email" name="email" placeholder="you@lab.com" required><button class="btn btn-primary" type="submit">Subscribe</button></div>
<div class="chips" role="group" aria-label="Topics">
<label class="check"><input type="checkbox" name="topics" value="Lab testing" checked> Lab testing</label>
<label class="check"><input type="checkbox" name="topics" value="Calculators & protocols" checked> Protocols</label>
<label class="check"><input type="checkbox" name="topics" value="Jobs"> Jobs</label>
<label class="check"><input type="checkbox" name="topics" value="Contests"> Contests</label>
<label class="check"><input type="checkbox" name="topics" value="Equipment deals"> Equipment deals</label>
</div>
</form>
</div>
</div>
</section>
<footer class="site-footer">
<div class="container">
<div class="foot-grid">
<div>
<a class="logo" href="{pre}index.html" style="color:#fff"><span class="logo-mark">⚗</span><span>Lab<b>.Works</b></span></a>
<p style="margin-top:14px">The independent hub for laboratory testing, free science calculators, protocols, lab careers and equipment know-how.</p>
<a class="btn btn-lime btn-sm" href="{pre}quote.html">Request a lab quote →</a>
<div class="socials"><a href="{pre}videos.html" aria-label="Videos">▶</a><a href="{pre}contact.html" aria-label="Contact">✉</a><a href="{pre}support.html" aria-label="Support">♥</a></div>
</div>
<div><h4>Testing</h4><ul>
<li><a href="{pre}testing/water-testing.html">Water testing</a></li>
<li><a href="{pre}testing/food-testing.html">Food testing</a></li>
<li><a href="{pre}testing/environmental-testing.html">Environmental</a></li>
<li><a href="{pre}testing/materials-testing.html">Materials</a></li>
<li><a href="{pre}tests.html">All lab tests</a></li>
<li><a href="{pre}quote.html">Get free quotes</a></li></ul></div>
<div><h4>Tools</h4><ul>
<li><a href="{pre}tools/molarity-calculator.html">Molarity</a></li>
<li><a href="{pre}tools/dilution-calculator.html">Dilution C1V1</a></li>
<li><a href="{pre}tools/molar-mass-calculator.html">Molar mass</a></li>
<li><a href="{pre}tools/centrifuge-rpm-rcf-calculator.html">RPM ↔ RCF</a></li>
<li><a href="{pre}tools/index.html">All calculators</a></li></ul></div>
<div><h4>Community</h4><ul>
<li><a href="{pre}guides/index.html">Guides</a></li>
<li><a href="{pre}videos.html">Videos</a></li>
<li><a href="{pre}jobs.html">Lab jobs</a></li>
<li><a href="{pre}contests.html">Contests & prizes</a></li>
<li><a href="{pre}careers.html">Work with us</a></li>
<li><a href="{pre}support.html">Donate / support</a></li></ul></div>
<div><h4>Company</h4><ul>
<li><a href="{pre}about.html">About</a></li>
<li><a href="{pre}list-your-lab.html">List your lab</a></li>
<li><a href="{pre}advertise.html">Advertise</a></li>
<li><a href="{pre}contact.html">Contact</a></li>
<li><a href="{pre}privacy.html">Privacy</a></li>
<li><a href="{pre}terms.html">Terms</a> · <a href="{pre}disclaimer.html">Disclaimer</a></li></ul></div>
</div>
<div class="foot-bottom"><span>© <span data-year>2026</span> Lab.Works · All rights reserved.</span><span><a href="{DOMAIN_CONTACT}" target="_blank" rel="noopener">This domain may be available — enquire</a></span></div>
</div>
</footer>
<a class="btn btn-primary float-cta" href="{pre}quote.html">⚡ Get free lab quotes</a>
<div class="cookie" role="dialog" aria-label="Cookie consent"><strong>Cookies & ads</strong><p class="mb0">We use cookies for analytics and to show ads that keep our tools free. See our <a href="{pre}privacy.html">privacy policy</a>.</p><div class="btns"><button class="btn btn-primary btn-sm" data-consent="yes">Accept</button><button class="btn btn-ghost btn-sm" data-consent="no">Essential only</button></div></div>
<script src="{pre}assets/js/config.js"></script>
<script src="{pre}assets/js/search-index.js" defer></script>
<script src="{pre}assets/js/main.js" defer></script>
"""

def close(pre, extra_js=""):
    js = f'<script src="{pre}assets/js/{extra_js}" defer></script>\n' if extra_js else ""
    return js + "</body>\n</html>\n"

def page_hero(pre, title, lead, crumbs, kicker=""):
    cr = f'<a href="{pre}index.html">Home</a>'
    for href, label in crumbs:
        cr += f' › <a href="{pre}{href}">{label}</a>' if href else f" › <span>{label}</span>"
    k = f'<span class="kicker">{kicker}</span>' if kicker else ""
    return f"""<div class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>{k}<h1>{title}</h1><p class="lead">{lead}</p></div></div>"""

def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{DOMAIN}/{u}"} for i, (u, n) in enumerate(items)]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

def quick_quote(pre, cat="", title="Get free quotes from accredited labs", sub="Tell us what you need tested — we match you with up to 3 suitable labs. Free, no obligation."):
    return f"""<div class="card" style="border:2px solid var(--brand)">
<span class="badge lime">Free · No obligation</span>
<h3 style="margin-top:10px">{title}</h3><p style="margin-bottom:14px">{sub}</p>
<form class="form" data-lw-form data-subject="Quick quote request" data-next="{pre}thanks.html?f=quote">
<input type="hidden" name="category" value="{esc(cat)}">
<div><label>What needs testing? <span class="req">*</span></label><input name="details" required placeholder="e.g. Lead & bacteria in well water"></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required autocomplete="name"></div>
<div><label>Email <span class="req">*</span></label><input type="email" name="email" required autocomplete="email"></div></div>
<div class="form-row"><div><label>Country / city</label><input name="location" autocomplete="country-name"></div>
<div><label>Samples</label><select name="samples"><option>1</option><option>2–5</option><option>6–20</option><option>21–100</option><option>100+ / recurring</option></select></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request (see <a href="{pre}privacy.html">privacy</a>).</label>
<button class="btn btn-primary btn-block" type="submit">Get my free quotes →</button>
<div class="trust-row"><span>Replies in 24–48h</span><span>Accredited labs</span><span>Details never sold</span></div>
</form></div>"""

def cta_band(pre, title="Need something tested?", text="Send one request, receive quotes from accredited labs that fit your matrix, standard, budget and turnaround.", btn="Get free quotes", href="quote.html"):
    return f"""<section><div class="container"><div class="cta-band"><div><h2 class="mt0">{title}</h2><p class="mb0">{text}</p></div><div style="text-align:right"><a class="btn btn-lime" href="{pre}{href}">{btn} →</a></div></div></div></section>"""

def domain_card(pre):
    return f"""<div class="card" style="background:var(--bg2)"><span class="badge purple">Domain</span><h3 style="margin-top:8px">Interested in lab.works?</h3><p>This website and domain name may be available for acquisition or partnership.</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="{DOMAIN_CONTACT}" target="_blank" rel="noopener">Enquire →</a></div>"""

def sidebar(pre, cat=""):
    return f"""<aside class="sidebar">{quick_quote(pre, cat)}{ad("sidebar")}
<div class="card"><h3>Popular calculators</h3><div class="toc">
<a href="{pre}tools/molarity-calculator.html">Molarity calculator</a><a href="{pre}tools/dilution-calculator.html">Dilution C1V1 = C2V2</a><a href="{pre}tools/molar-mass-calculator.html">Molar mass</a><a href="{pre}tools/buffer-calculator.html">Buffer (Henderson–Hasselbalch)</a><a href="{pre}tools/centrifuge-rpm-rcf-calculator.html">RPM ↔ RCF</a></div></div>
<div class="card"><h3>Support free science tools</h3><p>Donations fund new tools, videos, contests and prizes.</p><a class="btn btn-primary btn-sm" style="margin-top:12px" href="{pre}support.html">Support Lab.Works ♥</a></div>
</aside>"""


# ---------------------------------------------------------------------------
# Jekyll mode (GitHub Pages builds the shared chrome, so each page file only
# carries its own body). Default on; LW_JEKYLL=0 builds fully static HTML.
# ---------------------------------------------------------------------------
import os as _os
JEKYLL = _os.environ.get("LW_JEKYLL", "1") == "1"
P = "{{ site.baseurl }}/"
PRE_ROOT, PRE_SUB, PRE_ABS = ("", "../", "/lab-works/") if not JEKYLL else (P, P, P)
_full = dict(head=head, header=header, footer=footer, close=close, quick_quote=quick_quote, sidebar=sidebar, domain_card=domain_card)

def _inc_arg(k, v):
    if v.startswith("{{"):
        return f' {k}={v.strip("{} ").strip()}'
    return f' {k}="{v}"'

if JEKYLL:
    def head(title, desc, path, pre, schema=None, og_type="website"):
        full = f"{title} | {SITE}" if title != SITE else f"{SITE} — {TAGLINE}"
        url = f"{DOMAIN}/{path}".replace("/index.html", "/")
        fm = {"layout": "default", "full_title": full, "description": desc, "canonical": url, "og_type": og_type}
        s = "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + "---\n"
        for sc in (schema or []):
            s += f'<script type="application/ld+json">{json.dumps(sc, ensure_ascii=False)}</script>\n'
        return s

    def header(pre, active):
        return f"<!--LW:NAV:{active}-->\n"

    def footer(pre):
        return ""

    def close(pre, extra_js=""):
        return f"<!--LW:JS:{extra_js}-->\n" if extra_js else ""

    def quick_quote(pre, cat="", title=None, sub=None):
        s = "{% include quick-quote.html" + _inc_arg("cat", cat)
        if title: s += _inc_arg("title", title)
        if sub: s += _inc_arg("sub", sub)
        return s + " %}"

    def domain_card(pre):
        return "{% include domain-card.html %}"

    def sidebar(pre, cat=""):
        return "{% include sidebar.html" + _inc_arg("cat", cat) + " %}"


def jekyll_scaffold():
    """Return {path: content} for _config.yml, _layouts and _includes."""
    f = _full
    h = f["head"]("__T__", "__D__", "__P__", P, [])
    h = h.replace(esc("__T__ | " + SITE), "{{ page.full_title | escape }}")
    h = h.replace(esc("__D__"), "{{ page.description | escape }}")
    h = h.replace(f"{DOMAIN}/__P__", "{{ page.canonical }}")
    h = h.replace('og:type" content="website"', "og:type\" content=\"{{ page.og_type | default: 'website' }}\"")
    h = h.replace('content="index,follow,max-image-preview:large"', "content=\"{{ page.robots | default: 'index,follow,max-image-preview:large' }}\"")
    hd = f["header"](P, "__none__")
    for href, _ in NAV:
        hd = hd.replace(f'<a href="{P}{href}">', f'<a href="{P}{href}"{{% if page.nav == "{href}" %}} aria-current="page"{{% endif %}}>')
    layout = h + hd + "{{ content }}\n" + f["footer"](P) + \
        '{% if page.extra_js %}<script src="{{ site.baseurl }}/assets/js/{{ page.extra_js }}" defer></script>{% endif %}\n</body>\n</html>\n'
    qq = f["quick_quote"](P, "{{ include.cat }}", "{{ include.title | default: 'Get free quotes from accredited labs' }}",
                          "{{ include.sub | default: 'Tell us what you need tested — we match you with up to 3 suitable labs. Free, no obligation.' }}")
    sb = f["sidebar"](P, "{{ include.cat }}")  # calls global quick_quote -> include tag in Jekyll mode
    dc = f["domain_card"](P)
    cfg = ("title: Lab.Works\nurl: \"https://webworksa1.github.io\"\nbaseurl: \"/lab-works\"\n"
           "# For the custom domain lab.works: set url to https://lab.works, baseurl to \"\", and add a CNAME file.\n"
           "exclude: [build, README.md, PROMPT.md, RESEARCH.md, \"*.py\"]\nmarkdown: kramdown\n")
    return {"_config.yml": cfg, "_layouts/default.html": layout, "_includes/quick-quote.html": qq,
            "_includes/sidebar.html": sb, "_includes/domain-card.html": dc}
