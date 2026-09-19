"""Tools, guides, videos, equipment, jobs, careers, contests, support, advertise, info pages."""
from layout import *
from data import CATEGORIES, TOOLS, GUIDES, VIDEOS, EQUIPMENT, JOB_CATS
from forms import CALC_FORMS
from pages_core import tool_cards, guide_cards, video_cards, cat_cards


def tools_index():
    pre = PRE_SUB
    s = head("Free Lab Calculators — Molarity, Dilution, Buffer, RCF & More", "12 free laboratory calculators: molarity, dilution C1V1=C2V2, serial dilution, molar mass, buffer pH, centrifuge RPM/RCF, PCR master mix, cell count, statistics, DNA A260, Beer-Lambert and ppm converter.", "tools/index.html", pre,
             [breadcrumb_schema([("tools/", "Calculators")]), {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{DOMAIN}/tools/{t['slug']}.html", "name": t["name"]} for i, t in enumerate(TOOLS)]}])
    s += header(pre, "tools/index.html")
    s += page_hero(pre, "Free lab calculators", "Accurate, instant and mobile-friendly. Built for bench scientists, students and QC teams — no sign-up, no paywall.", [("", "Calculators")], "Toolbox")
    s += f"""<section><div class="container" data-filter-list>
<div class="filters"><input data-filter-q placeholder="Search calculators…" aria-label="Search calculators"></div>
<div class="grid g3">{''.join(f'<a class="card reveal" data-tags="{t["kw"]}" href="{t["slug"]}.html"><div class="ico">{t["icon"]}</div><h3>{t["name"]}</h3><p>{t["short"]}</p></a>' for t in TOOLS)}</div>
{ad("inArticle")}
<div class="card mt2"><h3>Suggest a calculator</h3><p>Missing a tool you use every week? Tell us — we build the most-requested ones first (and credit you).</p>
<form class="form mt2" data-lw-form data-subject="Calculator suggestion"><div class="form-row"><div><label>Calculator idea <span class="req">*</span></label><input name="idea" required></div><div><label>Email (to notify you)</label><input type="email" name="email"></div></div><button class="btn btn-primary" type="submit">Send suggestion</button></form></div>
</div></section>"""
    s += cta_band(pre)
    s += footer(pre) + close(pre)
    return s


def tool_page(t):
    pre = PRE_SUB
    path = f'tools/{t["slug"]}.html'
    others = [x for x in TOOLS if x["slug"] != t["slug"]][:6]
    schema = [breadcrumb_schema([("tools/", "Calculators"), (path, t["name"])]), faq_schema(t["faqs"]),
              {"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "url": f"{DOMAIN}/{path}", "applicationCategory": "EducationalApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": t["short"]}]
    s = head(f'{t["name"]} — Free & Instant', f'{t["short"]} Free online {t["name"].lower()} with formula, worked example and FAQ.', path, pre, schema)
    s += header(pre, "tools/index.html")
    s += page_hero(pre, f'{t["icon"]} {t["name"]}', t["short"], [("tools/index.html", "Calculators"), ("", t["name"])], "Free calculator")
    s += f"""<section><div class="container layout"><article>
<form class="calc form" data-calc="{t["calc"]}" autocomplete="off">
{CALC_FORMS[t["calc"]]}
<div class="out" aria-live="polite"></div>
<div class="actions"><button class="btn btn-primary btn-sm" type="submit">Calculate</button><button class="btn btn-ghost btn-sm" type="reset">Reset</button><button class="btn btn-ghost btn-sm" type="button" data-share>Share</button><button class="btn btn-ghost btn-sm" type="button" data-print>Print</button></div>
</form>
{ad("inArticle")}
<div class="prose">{t["body"]}
<h2>Frequently asked questions</h2>{faq_html(t["faqs"])}
<p class="form-note">Results are for guidance; verify critical values against your SOPs and supplier documentation. Found an issue? <a href="#" data-mail="Calculator feedback: {esc(t['name'])}">Tell us</a>.</p>
</div>
{ad("inArticle")}
<h2 class="mt2">More lab calculators</h2><div class="grid g3">{tool_cards(pre, others)}</div>
</article>{sidebar(pre)}</div></section>"""
    s += cta_band(pre, "Need an accredited lab to verify it?", "From concentration checks to full method validation — get quotes from accredited labs in one request.")
    s += footer(pre) + close(pre, "tools.js")
    return s


def guides_index():
    pre = PRE_SUB
    s = head("Lab Guides & Protocols", "Practical laboratory guides: choosing an accredited lab, water testing, preparing solutions, serial dilutions, centrifugation, DNA purity, shelf-life testing and lab safety.", "guides/index.html", pre, [breadcrumb_schema([("guides/", "Guides")])])
    s += header(pre, "guides/index.html")
    s += page_hero(pre, "Guides & protocols", "Step-by-step, expert-reviewed guides for lab testing clients and bench scientists.", [("", "Guides")], "Learn")
    s += f"""<section><div class="container"><div class="grid g3">{guide_cards(pre)}</div>{ad("inArticle")}
<div class="card mt2"><h3>Write for Lab.Works</h3><p>Are you a scientist, lab manager or QA professional? We pay for expert guides and protocols. <a href="{pre}careers.html">See contributor roles →</a></p></div></div></section>"""
    s += footer(pre) + close(pre)
    return s


def guide_page(g):
    pre = PRE_SUB
    path = f'guides/{g["slug"]}.html'
    import re
    heads = re.findall(r'<h2(?: id="([^"]+)")?>([^<]+)</h2>', g["body"])
    toc = "".join(f'<a href="#{i or ""}">{h}</a>' for i, h in heads if i)
    others = [x for x in GUIDES if x["slug"] != g["slug"]][:3]
    schema = [breadcrumb_schema([("guides/", "Guides"), (path, g["title"])]),
              {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "author": {"@type": "Organization", "name": "Lab.Works Editorial Team"}, "publisher": {"@type": "Organization", "name": "Lab.Works"}, "datePublished": "2026-09-19", "dateModified": "2026-09-19", "mainEntityOfPage": f"{DOMAIN}/{path}"}]
    s = head(g["title"], g["desc"], path, pre, schema, "article")
    s += header(pre, "guides/index.html")
    s += page_hero(pre, g["title"], g["desc"], [("guides/index.html", "Guides"), ("", g["cat"])], g["cat"])
    tocblock = f'<div class="card"><h3>On this page</h3><div class="toc">{toc}</div></div>' if toc else ""
    s += f"""<section><div class="container layout"><article class="prose">
<p class="form-note">By the Lab.Works Editorial Team · Updated September 2026 · <a href="{pre}about.html#editorial">Editorial policy</a></p>
{g["body"].replace("../", pre)}
{ad("inArticle")}
<div class="card mt2" style="font-size:1rem"><h3>Was this guide helpful?</h3><p>Support free, independent science content.</p><div class="hero-ctas" style="margin-top:12px"><a class="btn btn-primary btn-sm" href="{pre}support.html">Support us ♥</a><button class="btn btn-ghost btn-sm" data-share>Share this guide</button></div></div>
<h2>Keep reading</h2><div class="grid g3">{guide_cards(pre, others)}</div>
</article><div class="sidebar">{tocblock}{sidebar(pre).replace('<aside class="sidebar">', '').replace('</aside>', '')}</div></div></section>"""
    s += footer(pre) + close(pre)
    return s


def videos_page():
    pre = PRE_ROOT
    cats = sorted(set(v[2] for v in VIDEOS))
    chips = '<button class="chip active" data-chip="all">All</button>' + "".join(f'<button class="chip" data-chip="{c.lower()}">{c}</button>' for c in cats)
    cards = "".join(f'<div class="card" data-tags="{c.lower()}"><div class="video" data-q="{esc(q)}" data-title="{esc(t)}" role="button" tabindex="0" aria-label="Play: {esc(t)}"><div class="play"><div><span>▶</span><strong>{t}</strong></div></div></div><div class="meta"><span class="badge purple">{c}</span></div></div>' for t, q, c in VIDEOS)
    s = head("Lab Technique Videos", "Watch practical laboratory technique videos: pipetting, serial dilution, solution prep, cell counting, electrophoresis, PCR, water sampling and lab safety.", "videos.html", pre)
    s += header(pre, "videos.html")
    s += page_hero(pre, "Lab technique video library", "Short, practical lessons curated by topic. Watch, then use the matching calculator or guide.", [("", "Videos")], "Watch & learn")
    s += f"""<section><div class="container" data-filter-list><div class="chips" style="margin-bottom:20px">{chips}</div><div class="grid g3">{cards}</div>
{ad("inArticle")}
<div class="grid g2 mt2">
<div class="card"><h3>Submit your lab video</h3><p>Made a great tutorial? Get featured to thousands of lab professionals — and enter our video contest.</p>
<form class="form mt2" data-lw-form data-subject="Video submission"><div><label>Video URL <span class="req">*</span></label><input type="url" name="video_url" required placeholder="https://youtube.com/…"></div><div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div><label class="check"><input type="checkbox" name="contest" value="Enter into video contest"> Also enter the current video contest</label><button class="btn btn-primary" type="submit">Submit video</button></form></div>
<div class="card"><h3>Sponsor a video series</h3><p>Brands and labs can sponsor tutorial series with product integration, pre-roll mentions and a dedicated landing page.</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="advertise.html">See sponsorship options</a>
<h3 class="mt2">Subscribe on YouTube</h3><p>New lab technique videos every week.</p><a class="btn btn-primary btn-sm" style="margin-top:12px" id="yt-channel" href="https://www.youtube.com/" target="_blank" rel="noopener">▶ Open YouTube</a></div>
</div></div></section>
<script>document.addEventListener('DOMContentLoaded',function(){{var c=(window.LW_CONFIG||{{}}).youtubeChannel;if(c)document.getElementById('yt-channel').href=c;}});</script>"""
    s += footer(pre) + close(pre)
    return s


def equipment_page():
    pre = PRE_ROOT
    cards = ""
    for i, (ic, name, tips, q) in enumerate(EQUIPMENT):
        cards += f'''<div class="card" id="{i}" data-tags="{name.lower()}"><div class="ico">{ic}</div><h3>{name}</h3><p><strong>What to compare:</strong> {tips}</p>
<div class="hero-ctas" style="margin-top:14px"><a class="btn btn-primary btn-sm" href="#" data-modal="#eq-modal" data-value="{esc(name)}">Get supplier quotes</a><a class="btn btn-ghost btn-sm" data-amz href="https://www.amazon.com/s?k={q.replace(" ", "+")}" target="_blank" rel="noopener sponsored nofollow">Compare prices ↗</a></div></div>'''
    s = head("Lab Equipment Buyer's Guides & Supplier Quotes", "Independent buyer checklists for centrifuges, pipettes, balances, microscopes, pH meters, PCR cyclers, spectrophotometers, autoclaves, incubators, freezers and more — plus free supplier quotes.", "equipment.html", pre)
    s += header(pre, "equipment.html")
    s += page_hero(pre, "Lab equipment buyer's guides", "Know exactly what to compare before you buy — then get competing quotes from suppliers (new, refurbished or leased).", [("", "Equipment")], "Buy smarter")
    s += f"""<section><div class="container" data-filter-list><div class="filters"><input data-filter-q placeholder="Search equipment…"></div><div class="grid g3">{cards}</div>
<p class="form-note mt2">Disclosure: some outbound links are affiliate links. We may earn a commission at no extra cost to you. This never affects our checklists.</p>
{ad("inArticle")}
<div class="cta-band mt2"><div><h2 class="mt0">Are you an equipment supplier?</h2><p class="mb0">Receive qualified buyer requests and feature your products in our buyer's guides.</p></div><div style="text-align:right"><a class="btn btn-lime" href="advertise.html">Partner with us →</a></div></div>
</div></section>
<div class="modal" id="eq-modal" role="dialog" aria-modal="true" aria-label="Equipment quote"><div class="modal-box"><button class="icon-btn modal-close" aria-label="Close">✕</button>
<h3>Get equipment quotes</h3><p class="muted">Tell us what you need — we'll connect you with suppliers.</p>
<form class="form" data-lw-form data-subject="Equipment quote request" data-next="thanks.html?f=quote">
<div><label>Equipment <span class="req">*</span></label><input name="item" required></div>
<div class="form-row"><div><label>Condition</label><select name="condition"><option>New</option><option>Refurbished</option><option>Either</option><option>Lease / rent</option></select></div><div><label>Quantity</label><input name="qty" value="1"></div></div>
<div><label>Key requirements</label><textarea name="requirements" placeholder="Capacity, specs, brand preferences, budget, delivery date…"></textarea></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div class="form-row"><div><label>Organisation</label><input name="company"></div><div><label>Country</label><input name="country"></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> Share my request with relevant suppliers.</label>
<button class="btn btn-primary" type="submit">Request quotes</button></form></div></div>
<script>document.addEventListener('DOMContentLoaded',function(){{var t=(window.LW_CONFIG||{{}}).amazonTag;if(t)document.querySelectorAll('[data-amz]').forEach(function(a){{a.href+='&tag='+encodeURIComponent(t);}});}});</script>"""
    s += footer(pre) + close(pre)
    return s


def jobs_page():
    pre = PRE_ROOT
    cats = "".join(f'<label class="tile"><input type="checkbox" name="categories" value="{n}"><span><i>{i}</i>{n}</span></label>' for i, n in JOB_CATS)
    faqs = [("How much does it cost to post a job?", "Standard listings are $99 for 30 days. Featured listings add homepage and newsletter placement. Universities and non-profits receive 50% off."),
            ("How do job alerts work?", "Choose your fields and location. We email matching roles as they're posted. Unsubscribe anytime.")]
    s = head("Lab Jobs — Laboratory & Science Careers, Job Alerts", "Find laboratory jobs in chemistry, microbiology, clinical lab science, QC/QA, environmental and research. Free job alerts; employers can post lab jobs.", "jobs.html", pre, [faq_schema(faqs)])
    s += header(pre, "jobs.html")
    s += page_hero(pre, "Lab jobs & science careers", "Get lab roles matched to your skills by email — or reach qualified scientists and technicians with a job post.", [("", "Jobs")], "Careers")
    s += f"""<section><div class="container layout"><div>
<form class="wizard form" data-lw-form data-subject="Job alert signup" data-ok="Job alerts activated! We'll email you matching roles.">
<h2 class="mt0" style="font-size:1.5rem">🔔 Create your free job alert</h2>
<div class="form-row"><div><label>Job title / keywords <span class="req">*</span></label><input name="keywords" required placeholder="e.g. QC chemist, microbiologist, lab technician"></div><div><label>Location</label><input name="location" placeholder="City, country or Remote"></div></div>
<div><label>Fields</label><div class="tiles">{cats}</div></div>
<div class="form-row"><div><label>Experience</label><select name="level"><option>Student / intern</option><option>Entry level</option><option>Mid level</option><option>Senior / lead</option><option>Manager / director</option></select></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div><label>Link to CV / LinkedIn (optional — for recruiter matching)</label><input type="url" name="cv_link" placeholder="https://"></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> Email me job alerts. Unsubscribe anytime.</label>
<button class="btn btn-primary" type="submit">Activate job alerts</button>
</form>
{ad("inArticle")}
<h2>Browse by field</h2><div class="grid g3">{''.join(f'<div class="card"><div class="ico">{i}</div><h3 style="font-size:1.05rem">{n}</h3><p>Openings shared via alerts & newsletter</p></div>' for i, n in JOB_CATS)}</div>
<h2 class="mt2" id="post">Hiring? Post a lab job</h2>
<div class="grid g3">
<div class="card plan"><h3>Standard</h3><div class="price">$99<small>/30 days</small></div><ul><li>Job listing page</li><li>Included in matching job alerts</li><li>Google Jobs structured data</li></ul></div>
<div class="card plan pop"><span class="badge lime ribbon">Best value</span><h3>Featured</h3><div class="price">$199<small>/30 days</small></div><ul><li>Everything in Standard</li><li>Job of the Week placement</li><li>Newsletter feature</li><li>Social promotion</li></ul></div>
<div class="card plan"><h3>Hiring bundle</h3><div class="price">$499<small>/5 jobs</small></div><ul><li>5 Featured listings</li><li>Employer profile page</li><li>Access to candidate pool</li></ul></div>
</div>
<form class="card form mt2" data-lw-form data-subject="Job posting request" data-next="thanks.html?f=job">
<h3 class="mt0">Submit your vacancy</h3>
<div class="form-row"><div><label>Job title <span class="req">*</span></label><input name="job_title" required></div><div><label>Organisation <span class="req">*</span></label><input name="company" required></div></div>
<div class="form-row"><div><label>Location <span class="req">*</span></label><input name="location" required></div><div><label>Employment type</label><select name="type"><option>Full-time</option><option>Part-time</option><option>Contract</option><option>Internship</option><option>Postdoc</option></select></div></div>
<div class="form-row"><div><label>Salary range</label><input name="salary"></div><div><label>Plan</label><select name="plan"><option>Standard</option><option>Featured</option><option>Hiring bundle</option><option>University / non-profit (50% off)</option></select></div></div>
<div><label>Job description or link <span class="req">*</span></label><textarea name="description" required></textarea></div>
<div class="form-row"><div><label>Your name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<button class="btn btn-primary" type="submit">Submit job for review</button></form>
<h2 class="mt2">FAQ</h2>{faq_html(faqs)}
</div>{sidebar(pre)}</div></section>"""
    s += footer(pre) + close(pre)
    return s


def careers_page():
    pre = PRE_ROOT
    roles = [("✍️", "Science writers & editors", "Write test guides, protocols and explainers. Paid per article."),
             ("🎥", "Video creators", "Film short lab-technique tutorials for YouTube and Shorts."),
             ("💻", "Calculator developers", "Build accurate, accessible JavaScript lab tools."),
             ("🤝", "Lab partnerships (commission)", "Onboard testing labs and equipment suppliers."),
             ("📣", "Marketing & growth", "SEO, social, newsletter and community growth."),
             ("🎓", "Campus ambassadors", "Represent Lab.Works at your university; earn rewards."),
             ("🔬", "Scientific reviewers", "Review content for accuracy — credited on every page."),
             ("🛡️", "Community moderators", "Help run contests and keep our community helpful.")]
    s = head("Work With Us — Writers, Creators, Developers & Partners", "Join Lab.Works: paid science writing, video creation, calculator development, partnerships, marketing, campus ambassador and reviewer roles.", "careers.html", pre)
    s += header(pre, "")
    s += page_hero(pre, "Build the future of Lab.Works with us", "We're hiring freelance and part-time talent worldwide — funded by our partners, advertisers and supporters.", [("", "Work with us")], "Hiring talent")
    s += f"""<section><div class="container"><div class="grid g4">{''.join(f'<div class="card"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></div>' for i, n, d in roles)}</div></div></section>
<section class="section-alt"><div class="container layout"><form class="wizard form" data-lw-form data-subject="Talent application" data-next="thanks.html?f=apply">
<h2 class="mt0" style="font-size:1.5rem">Apply now</h2>
<div class="form-row"><div><label>Role <span class="req">*</span></label><select name="role" required><option value="">Choose…</option>{''.join(f'<option>{n}</option>' for _, n, _ in roles)}<option>Other</option></select></div><div><label>Availability</label><select name="availability"><option>Freelance / per project</option><option>Part-time</option><option>Full-time</option></select></div></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div class="form-row"><div><label>Portfolio / LinkedIn <span class="req">*</span></label><input type="url" name="portfolio" required placeholder="https://"></div><div><label>Country / time zone</label><input name="location"></div></div>
<div><label>Expertise & why you? <span class="req">*</span></label><textarea name="message" required></textarea></div>
<div><label>Expected rate</label><input name="rate" placeholder="e.g. $0.10/word, $40/hour"></div>
<button class="btn btn-primary" type="submit">Send application</button></form>
<aside class="sidebar"><div class="card"><h3>How we work</h3><ul style="padding-left:1.2em;color:var(--ink2)"><li>Remote-first, async</li><li>Paid on delivery</li><li>Credit on everything you create</li><li>Top contributors join revenue-share programmes</li></ul></div>{domain_card(pre)}</aside></div></section>"""
    s += footer(pre) + close(pre)
    return s


def contests_page():
    pre = PRE_ROOT
    contests = [("📸", "Lab Photo of the Season", "Your most striking microscope, gel, crystal or lab-life photo.", "Cash prize + featured gallery"),
                ("🎬", "60-Second Technique Video", "Teach one lab technique in under 60 seconds.", "Cash prize + YouTube feature"),
                ("💡", "Best Lab Hack", "A clever trick that saves time, money or reagents.", "Sponsor gear bundle"),
                ("🧮", "Calculator Idea Challenge", "Pitch a lab calculator we should build next.", "Your name on the tool + prize")]
    rules = [("Who can enter?", "Anyone 18+ (or with guardian consent) where contests are legal. Employees of prize sponsors may be excluded."),
             ("How are winners chosen?", "Entries are scored by a judging panel on originality, scientific accuracy, clarity and impact; community votes count toward a People's Choice award."),
             ("Do I keep rights to my entry?", "Yes. You grant Lab.Works a non-exclusive licence to display and promote your entry with credit."),
             ("When are winners announced?", "Within 30 days after the entry deadline, on this page, in our newsletter and on our social channels.")]
    s = head("Science Contests & Prizes — Lab.Works Science Challenge", "Enter the Lab.Works Science Challenge: lab photo, 60-second technique video, best lab hack and calculator idea contests with cash prizes and sponsor gear.", "contests.html", pre, [faq_schema(rules)])
    s += header(pre, "contests.html")
    s += page_hero(pre, "Lab.Works Science Challenge", "Show your skills, win prizes and get featured. New themes every season — funded by sponsors and community supporters.", [("", "Contests")], "Contests & prizes")
    s += f"""<section><div class="container">
<div class="grid g2" style="align-items:center"><div><h2 class="mt0">Season 1 entries close in</h2><div class="countdown" data-countdown="2026-12-31T23:59:59Z"><div><b>00</b><span>days</span></div><div><b>00</b><span>hours</span></div><div><b>00</b><span>min</span></div><div><b>00</b><span>sec</span></div></div></div>
<div class="card"><h3>How it works</h3><ol style="color:var(--ink2);padding-left:1.2em;margin:0"><li>Pick a category below</li><li>Submit your entry link with the form</li><li>Share it — People's Choice votes count</li><li>Winners announced within 30 days of close</li></ol></div></div>
<div class="grid g4 mt2">{''.join(f'<div class="card"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p><div class="meta"><span class="badge lime">🏆 {p}</span></div></div>' for i, n, d, p in contests)}</div>
</div></section>
<section class="section-alt"><div class="container layout">
<form class="wizard form" id="enter" data-lw-form data-subject="Contest entry" data-next="thanks.html?f=contest">
<h2 class="mt0" style="font-size:1.5rem">Submit your entry</h2>
<div><label>Category <span class="req">*</span></label><select name="contest" required><option value="">Choose…</option>{''.join(f'<option>{n}</option>' for _, n, _, _ in contests)}</select></div>
<div><label>Entry link (photo, video, doc) <span class="req">*</span></label><input type="url" name="entry_url" required placeholder="https://drive.google.com/… or YouTube link"></div>
<div><label>Title & short description <span class="req">*</span></label><textarea name="description" required></textarea></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div class="form-row"><div><label>Country</label><input name="country"></div><div><label>Institution / company (optional)</label><input name="org"></div></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I accept the contest rules and confirm this is my original work.</label>
<button class="btn btn-primary" type="submit">Submit entry 🏆</button></form>
<aside class="sidebar"><div class="card"><h3>Rules & FAQ</h3>{faq_html(rules)}</div></aside>
</div></section>
<section id="sponsor"><div class="container grid g2" style="align-items:start">
<div><span class="kicker">For brands</span><h2 class="mt0">Sponsor a prize</h2><p class="muted">Put your brand in front of engaged scientists, students and lab professionals. Sponsors receive logo placement on contest pages, newsletter mentions, social shout-outs and winner content rights.</p>
<div class="grid g3"><div class="stat"><b>Bronze</b><span>Gear prize + logo</span></div><div class="stat"><b>Silver</b><span>Category naming</span></div><div class="stat"><b>Gold</b><span>Title sponsor</span></div></div></div>
<form class="card form" data-lw-form data-subject="Contest sponsorship enquiry" data-next="thanks.html?f=sponsor">
<h3 class="mt0">Sponsorship enquiry</h3>
<div class="form-row"><div><label>Company <span class="req">*</span></label><input name="company" required></div><div><label>Tier</label><select name="tier"><option>Bronze</option><option>Silver</option><option>Gold</option><option>Custom</option></select></div></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div><label>Prize / budget idea</label><textarea name="message"></textarea></div>
<button class="btn btn-primary" type="submit">Send enquiry</button></form>
</div></section>
<div class="container">{ad("footer")}</div>"""
    s += footer(pre) + close(pre)
    return s


def support_page():
    pre = PRE_ROOT
    faqs = [("Is my donation tax-deductible?", "Lab.Works is an independent project, not a registered charity, so donations are generally not tax-deductible. Corporate sponsorships may qualify as marketing expenses — ask your accountant."),
            ("Can I give monthly?", "Yes. Choose monthly in your payment method, or pledge below and we'll send a secure recurring link."),
            ("How will my contribution be used?", "For operations and hosting, new calculators and guides, video production, promotion and marketing, hiring contributors, and funding contest prizes."),
            ("Can I get a refund?", "Contact us within 14 days of a one-time donation and we'll refund it, no questions asked.")]
    alloc = [("Operations & hosting", 25), ("New tools, guides & videos", 25), ("Promotion & marketing", 15), ("Hiring talented contributors", 20), ("Contests & prizes", 15)]
    bars = "".join(f'<div style="margin-bottom:12px"><div style="display:flex;justify-content:space-between;font-weight:600"><span>{n}</span><span>{p}%</span></div><div class="progress"><i style="width:{p * 4}%"></i></div></div>' for n, p in alloc)
    s = head("Support Lab.Works — Donate & Sponsor", "Support free science tools. Donations fund operations, new calculators and videos, promotion, hiring contributors and contest prizes. One-time, monthly and corporate sponsorship options.", "support.html", pre, [faq_schema(faqs)])
    s += header(pre, "support.html")
    s += page_hero(pre, "Keep science tools free for everyone ♥", "Lab.Works is independent and ad-supported. Your support funds operations, new tools and videos, promotion, hiring talent — and prizes for our community.", [("", "Support us")], "Donate & sponsor")
    s += f"""<section><div class="container layout"><div>
<div class="wizard">
<h2 class="mt0" style="font-size:1.5rem">Choose an amount</h2>
<div class="amounts"><button class="chip" data-amount="5">$5</button><button class="chip active" data-amount="25">$25</button><button class="chip" data-amount="50">$50</button><button class="chip" data-amount="100">$100</button><button class="chip" data-amount="250">$250</button><button class="chip" data-amount="500">$500</button><button class="chip" data-amount="1000">$1,000</button><input id="donate-custom" inputmode="decimal" placeholder="Custom $" aria-label="Custom amount"></div>
<p class="form-note">Pay securely with your preferred method:</p>
<div class="hero-ctas">
<a class="btn btn-primary" href="#" data-donate="paypal">Donate with PayPal</a>
<a class="btn btn-primary" href="#" data-donate="stripe">Card / Apple Pay / Google Pay</a>
<a class="btn btn-ghost" href="#" data-donate="buyMeACoffee">☕ Buy us a coffee</a>
<a class="btn btn-ghost" href="#" data-donate="githubSponsors">GitHub Sponsors</a>
<a class="btn btn-ghost" href="#" data-donate="patreon">Patreon (monthly)</a>
<a class="btn btn-lime" href="#pledge" data-donate="pledge">Pledge / request a payment link</a>
</div>
</div>
{ad("inArticle")}
<h2>Where your support goes</h2><div class="card">{bars}</div>
<h2 class="mt2">Supporter perks</h2>
<div class="grid g3">
<div class="card plan"><h3>Friend</h3><div class="price">$5<small>/mo</small></div><ul><li>Name on supporters wall</li><li>Supporter badge in newsletter</li></ul></div>
<div class="card plan pop"><span class="badge lime ribbon">Popular</span><h3>Lab Partner</h3><div class="price">$25<small>/mo</small></div><ul><li>All Friend perks</li><li>Vote on the next calculator</li><li>Early access to new tools</li></ul></div>
<div class="card plan"><h3>Principal Investigator</h3><div class="price">$100<small>/mo</small></div><ul><li>All Partner perks</li><li>Logo/link on supporters page</li><li>Quarterly roadmap call</li></ul></div>
</div>
<form class="card form mt2" id="pledge" data-lw-form data-subject="Donation pledge" data-next="thanks.html?f=donate">
<h3 class="mt0">Pledge your support</h3><p class="muted">We'll reply with a secure payment link (card, PayPal, bank transfer or UPI) and your perks.</p>
<div class="form-row"><div><label>Amount (USD) <span class="req">*</span></label><input id="pledge-amount" name="amount" required value="25" inputmode="decimal"></div><div><label>Frequency</label><select name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div><label>Direct my support to</label><select name="purpose"><option>Wherever it's needed most</option><option>Operations & hosting</option><option>New tools & videos</option><option>Promotion & marketing</option><option>Hiring contributors</option><option>Contest prizes</option></select></div>
<div><label>Message (optional)</label><textarea name="message"></textarea></div>
<label class="check"><input type="checkbox" name="public" value="Show my name on supporters wall" checked> Show my name on the supporters wall</label>
<button class="btn btn-primary" type="submit">Pledge support ♥</button></form>
<h2 class="mt2">Corporate sponsorship</h2>
<p class="muted">Support free science education and reach lab decision-makers. Packages include logo placement, sponsored tools and contest naming rights.</p>
<a class="btn btn-ghost" href="advertise.html">View sponsorship packages →</a>
<h2 class="mt2">Supporters wall</h2><div class="card center"><p>🌱 Our supporters wall is just getting started — <a href="#pledge">be the first name here</a>.</p></div>
<h2 class="mt2">FAQ</h2>{faq_html(faqs)}
</div>
<aside class="sidebar"><div class="card"><h3>Other ways to help</h3><ul style="padding-left:1.2em;color:var(--ink2)"><li>Share a calculator with your lab</li><li>Link to us from your lab's website</li><li><a href="contests.html">Enter a contest</a></li><li><a href="careers.html">Contribute a guide</a></li><li><a href="list-your-lab.html">Recommend us to labs</a></li></ul></div>{domain_card(pre)}</aside>
</div></section>"""
    s += footer(pre) + close(pre)
    return s


def advertise_page():
    pre = PRE_ROOT
    opts = [("🖼️", "Display advertising", "Premium placements on calculators, test guides and the newsletter."),
            ("🧮", "Sponsored calculator", "Your brand on a high-traffic tool with a contextual product link."),
            ("🏅", "Featured lab listing", "Top placement in testing categories plus priority RFQ routing."),
            ("🎥", "Sponsored video series", "Tutorial series featuring your products or services."),
            ("✉️", "Newsletter sponsorship", "Exclusive sponsor slot in Lab Notes."),
            ("🏆", "Contest sponsorship", "Prize and naming rights for the Science Challenge."),
            ("📝", "Sponsored guides & webinars", "Educational content co-created with our editors — clearly labelled."),
            ("🎯", "Lead generation programmes", "Pay-per-lead campaigns for labs and equipment suppliers.")]
    s = head("Advertise & Partner With Lab.Works", "Reach lab professionals, QA managers and testing buyers: display ads, sponsored calculators, featured lab listings, video sponsorship, newsletter and lead-generation programmes.", "advertise.html", pre)
    s += header(pre, "")
    s += page_hero(pre, "Advertise to people who buy lab services & equipment", "Contextual placements next to the exact moment scientists and buyers make decisions.", [("", "Advertise")], "Media kit")
    s += f"""<section><div class="container"><div class="grid g4">{''.join(f'<div class="card"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></div>' for i, n, d in opts)}</div></div></section>
<section class="section-alt"><div class="container layout"><form class="wizard form" data-lw-form data-subject="Advertising enquiry" data-next="thanks.html?f=ads">
<h2 class="mt0" style="font-size:1.5rem">Request the media kit</h2>
<div class="form-row"><div><label>Company <span class="req">*</span></label><input name="company" required></div><div><label>Website</label><input type="url" name="website" placeholder="https://"></div></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required></div><div><label>Work email <span class="req">*</span></label><input type="email" name="email" required></div></div>
<div><label>Interested in</label><div class="grid g2" style="gap:8px">{''.join(f'<label class="check"><input type="checkbox" name="interests" value="{n}"> {n}</label>' for _, n, _ in opts)}</div></div>
<div class="form-row"><div><label>Monthly budget</label><select name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div><div><label>Start date</label><input type="date" name="start"></div></div>
<div><label>Goals</label><textarea name="message"></textarea></div>
<button class="btn btn-primary" type="submit">Get the media kit</button></form>
<aside class="sidebar"><div class="card"><h3>Our audience</h3><ul style="padding-left:1.2em;color:var(--ink2)"><li>Bench scientists & technicians</li><li>QA/QC & lab managers</li><li>Food, supplement & product brands</li><li>Environmental consultants</li><li>Students & educators</li></ul></div>{domain_card(pre)}</aside></div></section>"""
    s += footer(pre) + close(pre)
    return s


def about_page():
    pre = PRE_ROOT
    s = head("About Lab.Works", "Lab.Works is an independent hub for laboratory testing, free science calculators, protocols, lab careers and equipment guidance.", "about.html", pre)
    s += header(pre, "")
    s += page_hero(pre, "About Lab.Works", "We make laboratory science easier to access — for the people who need testing and the people who do it.", [("", "About")], "Our mission")
    s += f"""<section><div class="container layout"><article class="prose">
<h2>Our mission</h2><p>Finding the right lab, method or calculation shouldn't take hours of searching. Lab.Works brings together plain-English testing guides, free calculators, practical protocols, video lessons, careers and a matching service that connects people with accredited laboratories.</p>
<h2>What we do</h2><ul><li><strong>Lab testing matching</strong> — one request, up to three suitable accredited labs.</li><li><strong>Free tools</strong> — accurate calculators for everyday bench work.</li><li><strong>Education</strong> — guides, protocols and videos.</li><li><strong>Community</strong> — contests, prizes, jobs and contributor opportunities.</li></ul>
<h2 id="editorial">Editorial policy</h2><p>Content is written and reviewed by people with laboratory experience and checked against primary standards and literature. Sponsored content is always labelled. Advertising never influences calculator results or recommendations. We correct errors promptly — <a href="#" data-mail="Correction request">report a correction</a>.</p>
<h2>How we make money</h2><p>Advertising (including Google AdSense), featured lab listings, qualified lead programmes, sponsorships, affiliate links (disclosed) and reader donations. This keeps our tools free.</p>
<h2>Not medical or legal advice</h2><p>Lab.Works provides information only. See our <a href="disclaimer.html">disclaimer</a>.</p>
</article>{sidebar(pre)}</div></section>"""
    s += footer(pre) + close(pre)
    return s


def contact_page():
    pre = PRE_ROOT
    s = head("Contact Lab.Works", "Contact Lab.Works about lab testing requests, partnerships, advertising, press or the lab.works domain.", "contact.html", pre)
    s += header(pre, "")
    s += page_hero(pre, "Contact us", "Questions, partnerships, advertising or feedback — we usually reply within one business day.", [("", "Contact")], "Get in touch")
    s += f"""<section><div class="container layout"><form class="wizard form" data-lw-form data-subject="Contact form" data-next="thanks.html?f=contact">
<div><label>Topic <span class="req">*</span></label><select name="topic" required><option value="">Choose…</option><option>Lab testing request</option><option>List my lab</option><option>Advertising / sponsorship</option><option>Donation / support</option><option>Contest question</option><option>Job posting</option><option>Write / work for Lab.Works</option><option>Domain / website acquisition (lab.works)</option><option>Press</option><option>Other</option></select></div>
<div class="form-row"><div><label>Name <span class="req">*</span></label><input name="name" required autocomplete="name"></div><div><label>Email <span class="req">*</span></label><input type="email" name="email" required autocomplete="email"></div></div>
<div class="form-row"><div><label>Phone</label><input type="tel" name="phone"></div><div><label>Organisation</label><input name="company"></div></div>
<div><label>Message <span class="req">*</span></label><textarea name="message" required></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my enquiry. <a href="privacy.html">Privacy</a></label>
<button class="btn btn-primary" type="submit">Send message</button>
</form>
<aside class="sidebar">
<div class="card"><h3>Quick links</h3><div class="toc"><a href="quote.html">Request lab quotes →</a><a href="list-your-lab.html">List your lab →</a><a href="advertise.html">Advertise →</a><a href="support.html">Support us →</a></div></div>
<div class="card"><h3>Email</h3><p>Prefer your own email app?</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="#" data-mail="Lab.Works enquiry">✉ Email Lab.Works</a></div>
{domain_card(pre)}
</aside></div></section>"""
    s += footer(pre) + close(pre)
    return s


def legal_page(slug, title, body):
    pre = PRE_ROOT
    s = head(title, f"{title} for Lab.Works.", f"{slug}.html", pre)
    s += header(pre, "")
    s += page_hero(pre, title, "Last updated: September 19, 2026", [("", title)])
    s += f'<section><div class="container"><article class="prose" style="max-width:820px">{body}</article></div></section>'
    s += footer(pre) + close(pre)
    return s

PRIVACY = """<p>This policy explains what Lab.Works ("we") collects and how we use it.</p>
<h2>Information you give us</h2><p>When you submit a form (quote request, lab listing, job alert, contest entry, pledge, contact) we receive the details you enter. Form delivery is processed by a third-party form-to-email service. We use this information to respond, to match quote requests with suitable laboratories (only with your consent), and to send newsletters you opt into.</p>
<h2>Cookies, analytics and advertising</h2><p>With your consent we use analytics and advertising cookies. Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>.</p>
<h2>Local storage</h2><p>Your browser stores your theme choice, cookie choice and in-progress form drafts locally. This data never leaves your device unless you submit a form.</p>
<h2>Sharing</h2><p>We never sell personal data. We share quote requests only with matched laboratories, and use service providers (hosting, form delivery, payments) under their own privacy terms.</p>
<h2>Your rights</h2><p>You may request access, correction or deletion of your data, or withdraw consent, at any time via our <a href="contact.html">contact form</a>. Residents of the EU/UK (GDPR), California (CCPA/CPRA), Canada (PIPEDA) and India (DPDP Act) have additional statutory rights.</p>
<h2>Children</h2><p>Our services are not directed to children under 13.</p>"""
TERMS = """<h2>Use of the site</h2><p>By using Lab.Works you agree to these terms. Content and tools are provided "as is" for informational purposes.</p>
<h2>Quote matching</h2><p>Lab.Works is not a laboratory and does not perform testing. Contracts for testing are solely between you and the laboratory you choose. We do not guarantee availability, pricing, turnaround or results.</p>
<h2>Calculators</h2><p>Calculators are provided for convenience. Verify all critical calculations independently. We are not liable for losses arising from their use.</p>
<h2>Listings, jobs & advertising</h2><p>We may accept, reject or remove listings, jobs and ads at our discretion. Advertisers are responsible for their claims.</p>
<h2>Contests</h2><p>Each contest is governed by its published rules. Void where prohibited. We may modify or cancel a contest if circumstances require.</p>
<h2>Donations</h2><p>Donations are voluntary and support the operation of Lab.Works. Lab.Works is not a registered charity unless explicitly stated.</p>
<h2>User content</h2><p>You retain ownership of content you submit and grant us a non-exclusive licence to display it with credit.</p>
<h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>"""
DISCLAIMER = """<p>Information on Lab.Works is general and educational. It is <strong>not medical, legal, regulatory or engineering advice</strong>. Always consult qualified professionals and follow your organisation's SOPs and applicable regulations.</p>
<p>Clinical test information is not a substitute for advice from a licensed healthcare provider. Indicative prices and turnaround times are estimates and vary by laboratory and region.</p>
<p><strong>Affiliate disclosure:</strong> some links are affiliate links; we may earn a commission at no cost to you. <strong>Advertising:</strong> we display ads, including Google AdSense; ads are not endorsements.</p>"""


def thanks_page():
    pre = PRE_ROOT
    s = head("Thank You", "Thank you — your submission was received.", "thanks.html", pre)
    s = s.replace('content="index,follow,max-image-preview:large"', 'content="noindex"')
    s += header(pre, "")
    s += f"""<section class="hero"><div class="container center" style="max-width:760px">
<div style="font-size:3rem">✅</div><h1>Thank you — we've got it!</h1>
<p class="lead" style="margin:0 auto">Your submission was received. We'll reply to the email you provided, usually within 24–48 business hours.</p>
<div class="hero-ctas" style="justify-content:center;margin-top:24px"><a class="btn btn-primary" href="tools/index.html">Explore free calculators</a><a class="btn btn-ghost" href="guides/index.html">Read guides</a></div>
</div></section>
<section class="section-alt"><div class="container grid g3">
<div class="card"><h3>📨 Get Lab Notes</h3><p>Weekly protocols, tools and testing tips — sign up below.</p></div>
<div class="card"><h3>🏆 Enter a contest</h3><p>Win prizes for your lab photos, videos and hacks.</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="contests.html">See contests</a></div>
<div class="card"><h3>♥ Support free tools</h3><p>Help us build more free science resources.</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="support.html">Support us</a></div>
</div></section>"""
    s += footer(pre) + close(pre)
    return s


def notfound_page():
    # absolute-path assets so 404 works at any depth on GitHub Pages project sites
    pre = PRE_ABS
    s = head("Page Not Found", "The page you're looking for doesn't exist.", "404.html", pre)
    s = s.replace('content="index,follow,max-image-preview:large"', 'content="noindex"')
    s += header(pre, "")
    s += f"""<section class="hero"><div class="container center" style="max-width:720px"><div style="font-size:3rem">🧪</div><h1>404 — experiment not found</h1><p class="lead" style="margin:0 auto">That page has evaporated. Try searching, or head to one of our most popular sections.</p>
<div class="hero-ctas" style="justify-content:center;margin-top:24px"><a class="btn btn-primary" href="{pre}index.html">Home</a><a class="btn btn-ghost" href="{pre}tools/index.html">Calculators</a><a class="btn btn-ghost" href="{pre}quote.html">Get lab quotes</a></div></div></section>"""
    s += footer(pre) + close(pre)
    return s
