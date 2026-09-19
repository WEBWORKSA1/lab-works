"""Home, tests, quote, directory, list-your-lab, testing category pages."""
from layout import *
from data import CATEGORIES, TOOLS, GUIDES, VIDEOS, EQUIPMENT, JOB_CATS

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Lab.Works", "url": DOMAIN,
       "logo": f"{DOMAIN}/assets/img/favicon.svg", "sameAs": []}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "name": "Lab.Works", "url": DOMAIN}


def cat_cards(pre, cats=CATEGORIES):
    return "".join(f'<a class="card reveal" href="{pre}testing/{c["slug"]}.html"><div class="ico">{c["icon"]}</div><h3>{c["name"]}</h3><p>{c["short"]}</p><div class="meta">{len(c["tests"])} popular tests →</div></a>' for c in cats)

def tool_cards(pre, tools=TOOLS):
    return "".join(f'<a class="card reveal" href="{pre}tools/{t["slug"]}.html"><div class="ico">{t["icon"]}</div><h3>{t["name"]}</h3><p>{t["short"]}</p><div class="meta">Free · instant · no sign-up</div></a>' for t in tools)

def guide_cards(pre, guides=GUIDES):
    return "".join(f'<a class="card reveal" href="{pre}guides/{g["slug"]}.html"><span class="badge">{g["cat"]}</span><h3 style="margin-top:10px">{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in guides)

def video_cards(vids):
    return "".join(f'<div class="card reveal"><div class="video" data-q="{esc(q)}" data-title="{esc(t)}" role="button" tabindex="0" aria-label="Play: {esc(t)}"><div class="play"><div><span>▶</span><strong>{t}</strong></div></div></div><div class="meta"><span class="badge purple">{c}</span></div></div>' for t, q, c in vids)


def home():
    pre = PRE_ROOT
    s = head("Lab.Works", "Get free quotes from accredited testing labs, use 12 free science calculators, and learn lab techniques with guides and videos. Water, food, environmental, materials, pharma & clinical testing.", "index.html", pre, [ORG, WEBSITE, faq_schema(HOME_FAQ)])
    s += header(pre, "")
    s += f"""<section class="hero"><div class="container hero-grid">
<div>
<span class="eyebrow"><span class="dot"></span> Free for requesters · Accredited labs · 10 testing categories</span>
<h1>Lab testing quotes, <span class="grad-text">science calculators</span> & lab know-how — in one place.</h1>
<p class="lead">Tell us what you need tested and get matched with accredited labs. Or use our free calculators, protocols and videos to work faster at the bench.</p>
<form class="search-wrap" role="search" onsubmit="return false"><div class="search-box"><label class="sr-only" for="q">Search</label><input id="q" data-site-search placeholder="Search tests, calculators, guides… e.g. well water, molarity" autocomplete="off"><button class="btn btn-primary" type="submit">Search</button></div><div class="search-results"></div></form>
<div class="hero-ctas"><a class="btn btn-primary" href="quote.html">Get free lab quotes →</a><a class="btn btn-ghost" href="tools/index.html">Open calculators</a></div>
<div class="chips"><a class="chip" href="testing/water-testing.html">Well water test</a><a class="chip" href="testing/food-testing.html">Nutrition label</a><a class="chip" href="testing/environmental-testing.html">Asbestos</a><a class="chip" href="tools/molarity-calculator.html">Molarity</a><a class="chip" href="tools/dilution-calculator.html">C1V1</a><a class="chip" href="testing/pharma-cosmetics-testing.html">Supplement COA</a></div>
</div>
<div class="hero-card">
<h3 class="mt0">What brings you here?</h3>
<div class="list">
<a class="row-item" href="quote.html" style="text-decoration:none;color:inherit"><span><strong>🏠 I need something tested</strong><br><small class="muted">Water, soil, food, product, materials…</small></span><span>→</span></a>
<a class="row-item" href="tools/index.html" style="text-decoration:none;color:inherit"><span><strong>🧪 I work in a lab</strong><br><small class="muted">Calculators, protocols, videos</small></span><span>→</span></a>
<a class="row-item" href="list-your-lab.html" style="text-decoration:none;color:inherit"><span><strong>🏢 I run a testing lab</strong><br><small class="muted">Get qualified client requests</small></span><span>→</span></a>
<a class="row-item" href="jobs.html" style="text-decoration:none;color:inherit"><span><strong>🎓 I'm looking for a lab job</strong><br><small class="muted">Job alerts & career guides</small></span><span>→</span></a>
</div></div>
</div></section>

<section style="padding-top:0"><div class="container"><div class="stats">
<div class="stat"><b>10</b><span>testing categories</span></div>
<div class="stat"><b>70+</b><span>test types explained</span></div>
<div class="stat"><b>12</b><span>free lab calculators</span></div>
<div class="stat"><b>$0</b><span>cost to request quotes</span></div>
</div></div></section>

<section class="section-alt"><div class="container">
<div class="section-head"><div><span class="kicker">How it works</span><h2 class="mt0">From question to certified results in 3 steps</h2></div><a class="btn btn-ghost" href="quote.html">Start a request</a></div>
<div class="steps">
<div class="step"><h3>Describe your test</h3><p class="muted mb0">What's being tested, how many samples, your deadline and any standard (ISO, ASTM, EPA, USP).</p></div>
<div class="step"><h3>Get matched</h3><p class="muted mb0">We route your request to up to 3 accredited labs whose scope fits your matrix and method.</p></div>
<div class="step"><h3>Compare & choose</h3><p class="muted mb0">Compare price, turnaround and accreditation. You're never obligated to proceed.</p></div>
</div></div></section>

<section><div class="container">
<div class="section-head"><div><span class="kicker">Lab testing</span><h2 class="mt0">What do you need tested?</h2><p>Plain-English guides to tests, standards, typical turnaround and indicative costs — with instant quote requests.</p></div><a class="btn btn-ghost" href="tests.html">All lab tests →</a></div>
<div class="grid g4">{cat_cards(pre, CATEGORIES[:8])}</div>
</div></section>
<div class="container">{ad("inArticle")}</div>

<section class="section-alt"><div class="container">
<div class="section-head"><div><span class="kicker">Free tools</span><h2 class="mt0">Lab calculators scientists bookmark</h2><p>Fast, accurate, mobile-friendly. No sign-up, no paywall.</p></div><a class="btn btn-ghost" href="tools/index.html">All calculators →</a></div>
<div class="grid g4">{tool_cards(pre, TOOLS[:8])}</div>
</div></section>

<section><div class="container">
<div class="section-head"><div><span class="kicker">Featured labs</span><h2 class="mt0">Accredited partner labs</h2><p>Featured placements are open to verified labs. Founding partners get launch pricing and priority matching.</p></div><a class="btn btn-primary" href="list-your-lab.html">List your lab</a></div>
<div class="grid g3">
<div class="card"><span class="badge lime">Featured slot open</span><h3 style="margin-top:10px">Water & environmental lab</h3><p>Reach homeowners, consultants and facilities managers requesting water, soil and air testing.</p><a class="btn btn-ghost btn-sm" style="margin-top:14px" href="list-your-lab.html?plan=Featured">Claim this slot</a></div>
<div class="card"><span class="badge lime">Featured slot open</span><h3 style="margin-top:10px">Food & supplement lab</h3><p>Connect with food brands needing nutrition panels, shelf-life studies and COAs.</p><a class="btn btn-ghost btn-sm" style="margin-top:14px" href="list-your-lab.html?plan=Featured">Claim this slot</a></div>
<div class="card"><span class="badge lime">Featured slot open</span><h3 style="margin-top:10px">Materials & product lab</h3><p>Get RFQs for mechanical, failure analysis, RoHS and product-safety testing.</p><a class="btn btn-ghost btn-sm" style="margin-top:14px" href="list-your-lab.html?plan=Featured">Claim this slot</a></div>
</div></div></section>

<section class="section-alt"><div class="container">
<div class="section-head"><div><span class="kicker">Learn</span><h2 class="mt0">Guides & protocols</h2></div><a class="btn btn-ghost" href="guides/index.html">All guides →</a></div>
<div class="grid g3">{guide_cards(pre, GUIDES[:6])}</div>
</div></section>

<section><div class="container">
<div class="section-head"><div><span class="kicker">Watch</span><h2 class="mt0">Lab technique videos</h2><p>Short, practical video lessons on essential techniques.</p></div><a class="btn btn-ghost" href="videos.html">Video library →</a></div>
<div class="grid g3">{video_cards(VIDEOS[:3])}</div>
</div></section>
<div class="container">{ad("inArticle")}</div>

<section class="section-alt"><div class="container grid g2">
<div class="card"><span class="kicker">Careers</span><h2 class="mt0">Lab jobs & career alerts</h2><p>Chemistry, microbiology, clinical, QC/QA, environmental and research roles. Get matching jobs by email — or post a vacancy to reach lab professionals.</p><div class="hero-ctas" style="margin-top:16px"><a class="btn btn-primary" href="jobs.html">Browse & get alerts</a><a class="btn btn-ghost" href="jobs.html#post">Post a job</a></div></div>
<div class="card"><span class="kicker">Contests & prizes</span><h2 class="mt0">Lab.Works Science Challenge</h2><p>Share your best lab hack, science photo, tutorial video or tool idea. Win cash prizes, gear from sponsors and a feature on Lab.Works.</p><div class="hero-ctas" style="margin-top:16px"><a class="btn btn-primary" href="contests.html">Enter the challenge</a><a class="btn btn-ghost" href="contests.html#sponsor">Sponsor a prize</a></div></div>
</div></section>

<section><div class="container">
<div class="section-head"><div><span class="kicker">Equipment</span><h2 class="mt0">Buying lab equipment? Start here.</h2><p>Independent buyer checklists plus free supplier quotes.</p></div><a class="btn btn-ghost" href="equipment.html">All buyer guides →</a></div>
<div class="grid g4">{''.join(f'<a class="card reveal" href="equipment.html#{i}"><div class="ico">{e[0]}</div><h3>{e[1]}</h3><p>{e[2][:90]}…</p></a>' for i, e in enumerate(EQUIPMENT[:4]))}</div>
</div></section>

<section class="section-alt"><div class="container">
<div class="section-head"><div><span class="kicker">Why Lab.Works</span><h2 class="mt0">Built on transparency</h2></div></div>
<div class="grid g4">
<div class="card"><div class="ico">🏅</div><h3>Accreditation first</h3><p>We prioritise labs with ISO/IEC 17025, ISO 15189, CLIA/CAP, GLP/GMP or equivalent scope.</p></div>
<div class="card"><div class="ico">🔍</div><h3>Editorial independence</h3><p>Guides and calculators are written to be useful — sponsorships are always labelled.</p></div>
<div class="card"><div class="ico">🔐</div><h3>Privacy respected</h3><p>Your request goes only to matched labs. We never sell your data.</p></div>
<div class="card"><div class="ico">⚡</div><h3>Fast responses</h3><p>Most requests receive a first response within 24–48 business hours.</p></div>
</div></div></section>

<section><div class="container grid g2" style="align-items:start">
<div><span class="kicker">FAQ</span><h2 class="mt0">Questions, answered</h2>{faq_html(HOME_FAQ)}</div>
<div class="grid">{quick_quote(pre)}{domain_card(pre)}</div>
</div></section>

<section class="section-alt"><div class="container"><div class="cta-band"><div><h2 class="mt0">Keep science tools free ♥</h2><p class="mb0">Lab.Works is independent. Your support funds operations, new tools, videos, promotion, hiring talented contributors — and prizes for our community contests.</p></div><div style="text-align:right"><a class="btn btn-lime" href="support.html">Support Lab.Works →</a></div></div></div></section>
"""
    s += footer(pre) + close(pre)
    return s

HOME_FAQ = [
 ("Is it free to request lab testing quotes?", "Yes. Requesting quotes through Lab.Works is 100% free with no obligation. Labs pay for featured listings and qualified leads, which keeps the service free for you."),
 ("How quickly will I hear back?", "Most requests receive a first response within 24–48 business hours. Rush requests are flagged to labs that offer expedited turnaround."),
 ("Are the labs accredited?", "We prioritise labs holding accreditation relevant to your test — for example ISO/IEC 17025 for testing, ISO 15189/CLIA/CAP for clinical, and GLP/GMP for regulated work. Always confirm the scope before sending samples."),
 ("Are the calculators free to use?", "Yes — every calculator is free, requires no sign-up and works on mobile. They're supported by advertising and by donations from our community."),
 ("Can I list my laboratory?", "Yes. Basic listings are free; Featured and Premium plans add priority placement and more client requests. See the List Your Lab page."),
]


def tests_page():
    pre = PRE_ROOT
    rows = ""
    for c in CATEGORIES:
        for t, method, tat in c["tests"]:
            q = f'quote.html?category={c["key"]}&details={t.replace(" ", "+").replace("&", "%26")}'
            rows += f'<div class="row-item" data-tags="{c["key"]} {esc(method.lower())}"><div><strong>{t}</strong><br><small class="muted">{c["icon"]} {c["name"]} · {method} · typical turnaround {tat}</small></div><div style="display:flex;gap:8px"><a class="btn btn-ghost btn-sm" href="testing/{c["slug"]}.html">Learn</a><a class="btn btn-primary btn-sm" href="{q}">Get quote</a></div></div>'
    chips = '<button class="chip active" data-chip="all">All</button>' + "".join(f'<button class="chip" data-chip="{c["key"]}">{c["icon"]} {c["name"].split(" ")[0].rstrip(",")}</button>' for c in CATEGORIES)
    s = head("All Lab Tests — Search 70+ Test Types & Get Quotes", "Browse 70+ laboratory tests across water, food, environmental, materials, pharma, clinical, microbiology, agriculture, cannabis and DNA testing. Compare turnaround and request free quotes.", "tests.html", pre, [breadcrumb_schema([("tests.html", "Lab tests")])])
    s += header(pre, "tests.html")
    s += page_hero(pre, "Find the right lab test", "Search 70+ test types, see typical turnaround, and request quotes from accredited labs in one click.", [("", "Lab tests")], "Test directory")
    s += f"""<section><div class="container layout"><div data-filter-list>
<div class="filters"><input data-filter-q placeholder="Search tests: lead, salmonella, PFAS, tensile…" aria-label="Search tests"></div>
<div class="chips" style="margin-bottom:18px">{chips}</div>
<p class="muted"><span data-filter-count></span> tests shown</p>
<div class="list">{rows}</div>
{ad("inArticle")}
<div class="card mt2"><h3>Don't see your test?</h3><p>Labs run thousands of methods. Describe your need and we'll find a lab that can do it.</p><a class="btn btn-primary btn-sm" style="margin-top:12px" href="quote.html">Request a custom test</a></div>
</div>{sidebar(pre)}</div></section>
<section class="section-alt"><div class="container"><div class="section-head"><h2 class="mt0">Browse by category</h2></div><div class="grid g4">{cat_cards(pre)}</div></div></section>"""
    s += footer(pre) + close(pre)
    return s


def category_page(c):
    pre = PRE_SUB
    path = f'testing/{c["slug"]}.html'
    trs = "".join(f'<tr><td><strong>{t}</strong></td><td>{m}</td><td>{tat}</td><td><a href="{pre}quote.html?category={c["key"]}&details={t.replace(" ", "+").replace("&", "%26")}">Quote →</a></td></tr>' for t, m, tat in c["tests"])
    others = [x for x in CATEGORIES if x["slug"] != c["slug"]][:4]
    schema = [breadcrumb_schema([("tests.html", "Lab tests"), (path, c["name"])]), faq_schema(c["faqs"]),
              {"@context": "https://schema.org", "@type": "Service", "serviceType": c["name"], "provider": {"@type": "Organization", "name": "Lab.Works"}, "areaServed": "Worldwide", "description": c["intro"]}]
    s = head(f'{c["name"]}: Tests, Standards, Costs & Free Quotes', f'{c["short"]} Learn which {c["name"].lower()} you need, standards, turnaround, indicative costs — and get free quotes from accredited labs.', path, pre, schema)
    s += header(pre, "tests.html")
    s += page_hero(pre, f'{c["icon"]} {c["name"]}', c["short"] + " Compare tests, standards and turnaround — then get free quotes from accredited labs.", [("tests.html", "Lab tests"), ("", c["name"])], "Lab testing guide")
    s += f"""<section><div class="container layout"><article class="prose">
<p>{c["intro"]}</p>
<p><strong>Who uses it:</strong> {c["who"]}</p>
<h2 id="tests">Popular {c["name"].lower()}</h2>
<table><tr><th>Test</th><th>Method / type</th><th>Typical turnaround</th><th></th></tr>{trs}</table>
{ad("inArticle")}
<h2 id="standards">Standards & accreditation</h2><p>{c["standards"]}</p>
<h2 id="cost">How much does it cost?</h2><p>{c["price"]}</p><p class="form-note">Indicative ranges only — prices vary by lab, country, sample count, detection limits and turnaround. Request quotes for exact pricing.</p>
<h2 id="process">How the testing process works</h2><ol><li><strong>Request quotes</strong> — describe your samples, test and deadline.</li><li><strong>Receive a sampling kit</strong> — containers, preservatives and chain-of-custody form.</li><li><strong>Collect & ship</strong> — follow holding times and temperature requirements.</li><li><strong>Get your report</strong> — certificate of analysis with methods, limits and results.</li></ol>
<div class="callout"><strong>Get it right first time:</strong> read <a href="{pre}guides/how-to-choose-an-accredited-testing-lab.html">how to choose an accredited testing lab</a>.</div>
<h2 id="faq">Frequently asked questions</h2>{faq_html(c["faqs"])}
<div class="mt2">{quick_quote(pre, c["key"], f'Get {c["name"].lower()} quotes')}</div>
<h2>Related testing</h2><div class="grid g2">{cat_cards(pre, others)}</div>
</article>{sidebar(pre, c["key"])}</div></section>"""
    s += footer(pre) + close(pre)
    return s


def quote_page():
    pre = PRE_ROOT
    tiles = "".join(f'<label class="tile"><input type="radio" name="category" value="{c["key"]}" required><span><i>{c["icon"]}</i>{c["name"].replace(" Testing", "").replace(" Lab Tests", "")}</span></label>' for c in CATEGORIES)
    tiles += '<label class="tile"><input type="radio" name="category" value="other"><span><i>❓</i>Other / not sure</span></label>'
    faqs = [("What happens after I submit?", "We review your request, then share it with up to 3 labs whose accreditation scope fits. They contact you directly with quotes, usually within 24–48 business hours."),
            ("Is my information shared?", "Only with the labs matched to your request, and only to prepare your quote. We never sell your data."),
            ("Do I have to accept a quote?", "No. Requests are free and there's no obligation.")]
    s = head("Request Free Lab Testing Quotes", "Get free, no-obligation quotes from accredited testing laboratories. Water, food, environmental, materials, pharma, clinical, microbiology and more. One request, up to 3 matched labs.", "quote.html", pre, [faq_schema(faqs)])
    s += header(pre, "")
    s += page_hero(pre, "Get free quotes from accredited labs", "One short request. Up to 3 matched labs. Replies in 24–48 business hours. No obligation, ever.", [("", "Request quotes")], "Free lab quote request")
    s += f"""<section><div class="container layout">
<div class="wizard" data-wizard>
<form id="rfq" data-lw-form data-subject="Lab quote request (RFQ)" data-next="thanks.html?f=quote" novalidate>
<div class="progress" aria-hidden="true"><i></i></div>
<div class="step-labels"><span>1. Test</span><span>2. Samples</span><span>3. Timing</span><span>4. Contact</span></div>

<fieldset class="wstep" data-need="category" style="border:0;padding:0;margin:0">
<legend class="sr-only">What do you need tested?</legend>
<h2 class="mt0" style="font-size:1.5rem">What do you need tested?</h2>
<div class="tiles">{tiles}</div>
<div><label for="details">Describe the test(s) or analytes <span class="req">*</span></label><textarea id="details" name="details" required placeholder="e.g. Lead, arsenic and E. coli in private well water / Nutrition facts panel for a protein bar / Tensile test on 6061 aluminium"></textarea></div>
<div class="form-row"><div><label>Sample / product type</label><input name="matrix" placeholder="e.g. well water, granola, plastic housing"></div><div><label>Required standard or method (if known)</label><input name="standard" placeholder="e.g. EPA 200.8, ISO 6579, ASTM E8, USP 61"></div></div>
<div class="wnav"><span></span><button type="button" class="btn btn-primary" data-next-step>Continue →</button></div>
</fieldset>

<fieldset class="wstep" style="border:0;padding:0;margin:0">
<h2 class="mt0" style="font-size:1.5rem">About your samples</h2>
<div class="form-row"><div><label>Number of samples <span class="req">*</span></label><select name="samples" required><option value="">Select…</option><option>1</option><option>2–5</option><option>6–20</option><option>21–100</option><option>100+</option></select></div>
<div><label>Frequency</label><select name="frequency"><option>One-time</option><option>Weekly</option><option>Monthly</option><option>Quarterly</option><option>Per production batch</option></select></div></div>
<div><label>Sample state</label><div class="chips"><label class="check"><input type="radio" name="state" value="Liquid"> Liquid</label><label class="check"><input type="radio" name="state" value="Solid"> Solid</label><label class="check"><input type="radio" name="state" value="Powder"> Powder</label><label class="check"><input type="radio" name="state" value="Gas/air"> Gas/air</label><label class="check"><input type="radio" name="state" value="Swab/surface"> Swab/surface</label><label class="check"><input type="radio" name="state" value="Biological"> Biological</label></div></div>
<div><label>Accreditation required</label><div class="chips"><label class="check"><input type="checkbox" name="accreditation" value="ISO/IEC 17025"> ISO/IEC 17025</label><label class="check"><input type="checkbox" name="accreditation" value="ISO 15189 / CLIA / CAP"> ISO 15189 / CLIA / CAP</label><label class="check"><input type="checkbox" name="accreditation" value="GLP / GMP"> GLP / GMP</label><label class="check"><input type="checkbox" name="accreditation" value="Government certified"> Government certified</label><label class="check"><input type="checkbox" name="accreditation" value="Not sure"> Not sure</label></div></div>
<div><label>Link to specification / SDS (optional)</label><input type="url" name="spec_link" placeholder="https://…"></div>
<div class="wnav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="button" class="btn btn-primary" data-next-step>Continue →</button></div>
</fieldset>

<fieldset class="wstep" style="border:0;padding:0;margin:0">
<h2 class="mt0" style="font-size:1.5rem">Timing, budget & location</h2>
<div class="form-row"><div><label>Turnaround needed <span class="req">*</span></label><select name="turnaround" required><option value="">Select…</option><option>Standard (best price)</option><option>Rush (1–3 days)</option><option>Flexible</option></select></div>
<div><label>Results needed by</label><input type="date" name="deadline"></div></div>
<div class="form-row"><div><label>Budget range</label><select name="budget"><option>Not sure</option><option>Under $250</option><option>$250 – $1,000</option><option>$1,000 – $5,000</option><option>$5,000 – $25,000</option><option>$25,000+</option></select></div>
<div><label>Sample logistics</label><select name="logistics"><option>I can ship samples</option><option>I can drop off locally</option><option>Need on-site sampling</option></select></div></div>
<div class="form-row"><div><label>Country <span class="req">*</span></label><input name="country" required autocomplete="country-name"></div><div><label>City / postcode</label><input name="city" autocomplete="address-level2"></div></div>
<div class="wnav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="button" class="btn btn-primary" data-next-step>Continue →</button></div>
</fieldset>

<fieldset class="wstep" style="border:0;padding:0;margin:0">
<h2 class="mt0" style="font-size:1.5rem">Where should labs send your quotes?</h2>
<div class="form-row"><div><label>Full name <span class="req">*</span></label><input name="name" required autocomplete="name"></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required autocomplete="email"></div></div>
<div class="form-row"><div><label>Phone (optional)</label><input type="tel" name="phone" autocomplete="tel"></div><div><label>Company / organisation</label><input name="company" autocomplete="organization"></div></div>
<div class="form-row"><div><label>You are a…</label><select name="role"><option>Homeowner / individual</option><option>Small business</option><option>Manufacturer / brand</option><option>Consultant / engineer</option><option>Researcher / university</option><option>Government / municipality</option></select></div>
<div><label>How did you hear about us?</label><select name="source"><option>Google search</option><option>YouTube</option><option>Social media</option><option>Referral</option><option>Other</option></select></div></div>
<div><label>Anything else labs should know?</label><textarea name="message" placeholder="Special handling, reporting format, regulatory body…"></textarea></div>
<label class="check"><input type="checkbox" name="match" value="Match me with up to 3 labs" checked> Match me with up to 3 suitable labs</label>
<label class="check"><input type="checkbox" name="newsletter" value="yes"> Send me the Lab Notes newsletter</label>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that Lab.Works may share my request with matched labs so they can contact me. <a href="privacy.html">Privacy</a></label>
<div class="wnav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="submit" class="btn btn-primary">Get my free quotes →</button></div>
<div class="trust-row"><span>100% free</span><span>No obligation</span><span>Replies in 24–48h</span><span>Data never sold</span></div>
</fieldset>
</form>
</div>
<aside class="sidebar">
<div class="card"><h3>Why request through Lab.Works?</h3><ul style="padding-left:1.2em;color:var(--ink2)"><li>One form instead of calling dozens of labs</li><li>Matched by accreditation scope and method</li><li>Compare price and turnaround side by side</li><li>Your progress is saved automatically</li></ul></div>
<div class="card"><h3>FAQ</h3>{faq_html(faqs)}</div>
<div class="card"><h3>Prefer to talk?</h3><p>Send us a message and a specialist will get back to you.</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="#" data-mail="Lab testing enquiry">Email our team</a></div>
</aside>
</div></section>"""
    s += footer(pre) + close(pre)
    return s


ACCRED = [("ILAC (global MRA signatories)", "https://ilac.org/signatory-search/"), ("A2LA (USA)", "https://www.a2la.org/"), ("ANAB (USA)", "https://anab.ansi.org/"),
          ("UKAS (UK)", "https://www.ukas.com/"), ("CALA / SCC (Canada)", "https://cala.ca/"), ("DAkkS (Germany)", "https://www.dakks.de/"),
          ("NABL (India)", "https://nabl-india.org/"), ("NATA (Australia)", "https://nata.com.au/"), ("IAS (International)", "https://www.iasonline.org/")]

def directory_page():
    pre = PRE_ROOT
    opts = "".join(f'<option value="{c["key"]}">{c["name"]}</option>' for c in CATEGORIES)
    s = head("Find a Testing Lab — Accredited Laboratory Directory", "Find accredited testing laboratories by test type, country and accreditation. Get matched with up to 3 labs for free, or list your lab.", "directory.html", pre)
    s += header(pre, "directory.html")
    s += page_hero(pre, "Find an accredited testing lab", "Search by testing type, location and accreditation — or let us match you with the right labs for free.", [("", "Lab directory")], "Lab directory")
    s += f"""<section><div class="container layout"><div>
<form class="card form" data-lw-form data-subject="Lab match request (directory)" data-next="thanks.html?f=quote">
<h3 class="mt0">Get matched with labs near you</h3>
<div class="form-row"><div><label>Testing type <span class="req">*</span></label><select name="category" required><option value="">Choose…</option>{opts}</select></div><div><label>Country / city <span class="req">*</span></label><input name="location" required></div></div>
<div class="form-row"><div><label>Accreditation</label><select name="accreditation"><option>Any</option><option>ISO/IEC 17025</option><option>ISO 15189 / CLIA / CAP</option><option>GLP / GMP</option></select></div><div><label>Turnaround</label><select name="turnaround"><option>Standard</option><option>Rush</option></select></div></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> Share my request with matched labs. <a href="privacy.html">Privacy</a></label>
<button class="btn btn-primary" type="submit">Find my labs →</button>
</form>
<h2 class="mt2">Featured laboratories</h2>
<p class="muted">Our verified directory is onboarding founding partner labs. Featured placements appear here first.</p>
<div class="grid g2">
<div class="card"><span class="badge lime">Founding partner slot</span><h3 style="margin-top:8px">Your lab here</h3><p>Top placement in your category and region, accreditation badges, and priority RFQ routing.</p><a class="btn btn-primary btn-sm" style="margin-top:12px" href="list-your-lab.html?plan=Featured">Become a founding partner</a></div>
<div class="card"><span class="badge">Free listing</span><h3 style="margin-top:8px">Basic listing</h3><p>Lab profile with services, accreditations and contact link. Free forever.</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="list-your-lab.html?plan=Free">List for free</a></div>
</div>
{ad("inArticle")}
<h2>Browse labs by testing type</h2><div class="grid g2">{cat_cards(pre)}</div>
<h2 class="mt2">Verify any lab's accreditation</h2><p class="muted">Always check the lab's scope of accreditation directly with the accreditation body:</p>
<div class="grid g3">{''.join(f'<a class="card" href="{u}" target="_blank" rel="noopener nofollow"><h3 style="font-size:1rem">{n}</h3><p>Search accredited labs & scopes ↗</p></a>' for n, u in ACCRED)}</div>
<h2 class="mt2">How we vet labs</h2><div class="steps"><div class="step"><h3>Accreditation check</h3><p class="muted mb0">Certificate & scope verified with the accreditation body.</p></div><div class="step"><h3>Capability review</h3><p class="muted mb0">Methods, matrices, detection limits and turnaround confirmed.</p></div><div class="step"><h3>Client feedback</h3><p class="muted mb0">Responsiveness and satisfaction tracked on every request.</p></div></div>
</div>{sidebar(pre)}</div></section>"""
    s += footer(pre) + close(pre)
    return s


def list_lab_page():
    pre = PRE_ROOT
    cats = "".join(f'<label class="check"><input type="checkbox" name="services" value="{c["name"]}"> {c["name"]}</label>' for c in CATEGORIES)
    faqs = [("How do leads work?", "When a request matches your categories, region and accreditation, we send you the requester's details so you can quote directly. Featured and Premium labs receive priority routing."),
            ("Is there a contract?", "No long-term contract. Paid plans are month-to-month and can be cancelled anytime."),
            ("Do you verify accreditation?", "Yes. We check certificates and scopes with the issuing accreditation body before awarding verification badges.")]
    s = head("List Your Lab — Get Qualified Testing Requests", "List your testing laboratory on Lab.Works. Free basic listing, featured placements and qualified RFQs from businesses, consultants and consumers.", "list-your-lab.html", pre, [faq_schema(faqs)])
    s += header(pre, "")
    s += page_hero(pre, "Grow your lab with qualified requests", "Reach businesses, consultants, researchers and consumers actively looking for testing. Basic listings are free.", [("", "List your lab")], "For laboratories")
    s += f"""<section><div class="container">
<div class="grid g3">
<div class="card plan"><h3>Basic</h3><div class="price">Free</div><ul><li>Lab profile page</li><li>Services & accreditation list</li><li>Website link</li><li>Eligible for standard matching</li></ul><a class="btn btn-ghost btn-block" href="#apply" data-plan="Free" onclick="document.getElementById('plan').value='Free'">List for free</a></div>
<div class="card plan pop"><span class="badge lime ribbon">Most popular</span><h3>Featured</h3><div class="price">$99<small>/month</small></div><ul><li>Everything in Basic</li><li>Top placement in category & region</li><li>Verified accreditation badge</li><li>Priority RFQ routing</li><li>Logo on category pages</li></ul><a class="btn btn-primary btn-block" href="#apply" onclick="document.getElementById('plan').value='Featured'">Get featured</a></div>
<div class="card plan"><h3>Premium Partner</h3><div class="price">$299<small>/month</small></div><ul><li>Everything in Featured</li><li>Homepage placement</li><li>Sponsored guide or video</li><li>Newsletter feature</li><li>Dedicated account manager</li></ul><a class="btn btn-ghost btn-block" href="#apply" onclick="document.getElementById('plan').value='Premium Partner'">Become a partner</a></div>
</div>
<p class="form-note center">Founding-partner launch pricing. Pay-per-lead options available on request.</p>
</div></section>
<section class="section-alt" id="apply"><div class="container layout">
<div class="wizard" data-wizard>
<form id="lab" data-lw-form data-subject="Lab listing application" data-next="thanks.html?f=lab">
<div class="progress"><i></i></div><div class="step-labels"><span>1. Lab details</span><span>2. Capabilities</span><span>3. Plan</span></div>
<fieldset class="wstep" style="border:0;padding:0;margin:0">
<div class="form-row"><div><label>Laboratory name <span class="req">*</span></label><input name="lab_name" required></div><div><label>Website <span class="req">*</span></label><input type="url" name="website" required placeholder="https://"></div></div>
<div class="form-row"><div><label>Country <span class="req">*</span></label><input name="country" required></div><div><label>City / address</label><input name="address"></div></div>
<div class="form-row"><div><label>Contact name <span class="req">*</span></label><input name="name" required></div><div><label>Work email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div><label>Phone</label><input type="tel" name="phone"></div>
<div class="wnav"><span></span><button type="button" class="btn btn-primary" data-next-step>Continue →</button></div>
</fieldset>
<fieldset class="wstep" data-need="services" style="border:0;padding:0;margin:0">
<div><label>Testing services <span class="req">*</span></label><div class="grid g2" style="gap:8px">{cats}</div></div>
<div class="form-row"><div><label>Accreditations</label><input name="accreditations" placeholder="e.g. ISO/IEC 17025 (A2LA #1234.01), CLIA"></div><div><label>Typical turnaround</label><select name="turnaround"><option>24–48 h</option><option>3–5 days</option><option>1–2 weeks</option><option>Varies by test</option></select></div></div>
<div><label>Sample intake</label><div class="chips"><label class="check"><input type="checkbox" name="intake" value="Ship-in"> Ship-in</label><label class="check"><input type="checkbox" name="intake" value="Drop-off"> Drop-off</label><label class="check"><input type="checkbox" name="intake" value="On-site sampling"> On-site sampling</label><label class="check"><input type="checkbox" name="intake" value="Mobile lab"> Mobile lab</label></div></div>
<div><label>Regions served</label><input name="regions" placeholder="e.g. Ontario & Quebec; nationwide shipping"></div>
<div class="wnav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="button" class="btn btn-primary" data-next-step>Continue →</button></div>
</fieldset>
<fieldset class="wstep" style="border:0;padding:0;margin:0">
<div><label>Plan</label><select name="plan" id="plan"><option>Free</option><option>Featured</option><option>Premium Partner</option><option>Pay-per-lead (tell me more)</option></select></div>
<div><label>Short description of your lab</label><textarea name="message" placeholder="Specialities, instruments, industries served…"></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I confirm I'm authorised to list this laboratory and accept the <a href="terms.html">terms</a>.</label>
<div class="wnav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="submit" class="btn btn-primary">Submit application →</button></div>
</fieldset>
</form></div>
<aside class="sidebar"><div class="card"><h3>What labs get</h3><ul style="padding-left:1.2em;color:var(--ink2)"><li>Requests with sample count, standard, deadline and budget</li><li>Traffic from test guides & calculators</li><li>Verified accreditation badge</li><li>No long-term contracts</li></ul></div><div class="card"><h3>FAQ</h3>{faq_html(faqs)}</div></aside>
</div></section>"""
    s += footer(pre) + close(pre)
    return s
