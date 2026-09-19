# Lab.Works — Business Idea + Phase-wise Build Prompt

## 1. The idea (why this wins)

**Lab.Works = "the independent hub for laboratory testing": free lab calculators & guides pull the traffic, and a lab-testing quote marketplace turns that traffic into money.**

| Revenue engine | Why it works | Unit economics (assumptions, validate) |
|---|---|---|
| **B2B lead gen: "Request a lab test quote"** | Testing buyers (food brands, well owners, manufacturers, consultants) have urgent, high-value needs. Contract Laboratory and Scientist.com already prove the model. | Testing leads sell for roughly $20–$150 each, or labs pay $99–$299/mo for placement. 300 leads/mo × $40 ≈ **$12k/mo** |
| **Featured lab listings** | Labs pay to rank first in their category and region | 30 labs × $99 ≈ **$3k/mo** |
| **AdSense** | Health, environmental and B2B science queries have above-average CPCs. Calculator pages get repeat visits because scientists bookmark them. | 200k pageviews/mo × $8–15 RPM ≈ **$1.6k–3k/mo** |
| **YouTube** (technique videos, embedded site-wide) | Evergreen tutorials, plus a second traffic channel | AdSense for YouTube plus sponsorships |
| **Job board** | Lab hiring is constant and niche boards convert | 20 posts × $99–199 ≈ **$2–4k/mo** |
| **Sponsorships, contests, equipment affiliate, donations** | Equipment is a high-ticket purchase, and vendors fund contest prizes | Extra upside |

**Moat:** calculator pages rank globally and last for years ("molarity calculator", "c1v1 calculator", "rpm to rcf"). Programmatic testing pages ("[test] testing in [city]") scale SEO. Every tool page links to the quote form.

**Research basis:** 28 competitor sites were fetched and analysed; see `RESEARCH.md`.

---

## 2. Phase-wise build prompt (copy each phase into your AI builder)

### Phase 0: Foundation
> Build a static, multi-page website for **Lab.Works** (domain lab.works) that runs free on GitHub Pages. Use HTML5, one CSS file with design tokens (light and dark mode), and vanilla JS. No build server is needed at runtime. Use a Python generator (`build/`) with a shared layout, so every page gets the same header, footer, SEO meta, Open Graph and JSON-LD.
> Every page starts with a top bar that links to `https://web.works/contact` with the text "Contact, if you are interested in this website/domain name".
> Every form posts through a form-to-email relay (FormSubmit AJAX). The destination inbox is stored only as an XOR-encoded byte array in JS and decoded at runtime. It must never appear in HTML, text or mailto hrefs. "Email us" links use `data-mail` and open the mail client via JS.

### Phase 1: Design system and core UX
> Use the Inter and Space Grotesk fonts, a teal→blue→violet gradient brand and lime accents, rounded cards and soft shadows. Build a sticky glass header with a burger menu under 1260px. Add a dark-mode toggle that remembers the choice, reveal-on-scroll animation (visible when JS is off), a floating "Get free lab quotes" CTA, and a consent banner that gates AdSense and GA4. Layouts must be mobile-first with no horizontal scroll and must meet WCAG AA (skip link, labels, focus rings, aria-live on results).

### Phase 2: Lead-generation engine (highest priority)
> 1. **quote.html**: a 4-step wizard with a progress bar.
>    - Step 1: category tiles and test description.
>    - Step 2: samples, frequency, state and accreditation.
>    - Step 3: turnaround, deadline, budget, logistics and location.
>    - Step 4: contact details and consent.
>
>    Autosave drafts to localStorage, prefill from URL (`?category=water&details=…`), and redirect to thanks.html on success.
> 2. A **quick-quote card** in the sidebar of every test, tool and guide page.
> 3. **list-your-lab.html**: Free, Featured and Premium plans plus a 3-step lab application.
> 4. A **directory** match form, accreditation-body lookup links, and "founding partner" slots.
> 5. **Equipment** quote modal, job-alert form, advertiser media-kit form and newsletter topics.
> 6. Trust copy next to every CTA: "Free · No obligation · Replies in 24–48h · Data never sold".

### Phase 3: Traffic magnets (free tools)
> Build 12 live calculators: molarity, dilution C1V1, serial dilution, molar mass (formula parser with hydrates and brackets), buffer (Henderson–Hasselbalch with presets), RPM↔RCF, PCR master mix, hemocytometer plus seeding, replicate statistics (SD, SEM, CV, 95% CI, Grubbs), DNA/RNA A260 purity, Beer–Lambert, and a ppm/mg/L/%/M converter.
> Each page follows this order: widget → explainer → formula → worked example → FAQ (FAQPage schema) → related tools → quote CTA. Add WebApplication schema, plus share and print buttons.

### Phase 4: Content and SEO
> - 10 testing-category pages. Each includes a tests table, standards, indicative costs, the process, an FAQ, and Service + FAQ schema.
> - A filterable catalogue of 80+ tests.
> - 8 long-form guides with a table of contents and Article schema.
> - Also: sitemap.xml, robots.txt, canonical tags, breadcrumbs, and client-side site search from a generated index.
> - Later, generate programmatic "[test] in [city]" pages.

### Phase 5: Monetisation layer
> - AdSense slots: in-article, sidebar and footer, loaded only after consent. Keep ads off the quote wizard.
> - ads.txt.
> - Amazon affiliate tag injection on equipment links.
> - YouTube video facades (click-to-load, privacy-enhanced embed).
> - Job-posting plans, advertiser options and sponsored calculators.
> - All IDs live in `assets/js/config.js`.

### Phase 6: Community, donations, contests and hiring
> - **support.html**: amount picker; PayPal, Stripe, Buy Me a Coffee, GitHub Sponsors and Patreon buttons that appear only once configured; a pledge form as fallback; a fund-allocation chart (operations, tools, promotion, hiring, prizes); supporter tiers; a supporters wall; FAQ.
> - **contests.html**: live countdown, 4 contest categories, entry form, rules FAQ, sponsor-a-prize tiers and form.
> - **careers.html**: 8 talent roles and an application form.
> - **videos.html**: filterable library and a submission form.

### Phase 7: Launch and growth
> 1. Enable GitHub Pages.
> 2. Submit a test form to activate FormSubmit, then swap in the alias.
> 3. Point the lab.works DNS at GitHub Pages and add a `CNAME` file.
> 4. Submit to Google Search Console.
> 5. Apply for AdSense once there are 20+ content pages.
> 6. Create a YouTube channel.
> 7. Recruit 10 founding labs.
> 8. Weekly: 2 new calculators or guides and 1 video.
> 9. Monthly: a contest, newsletter and outreach.
