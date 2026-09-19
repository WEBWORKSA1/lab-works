# Lab.Works

Lab.Works is a static website that runs on the free GitHub Pages plan. It combines a lab-testing quote marketplace, 12 free science calculators, testing guides, videos, an equipment buyer hub, a jobs board, contests and a donations page.

- **Live site:** https://webworksa1.github.io/lab-works/
- **Strategy and phase-wise build prompt:** [PROMPT.md](PROMPT.md)
- **Competitor research (28 sites):** [RESEARCH.md](RESEARCH.md)

## Go-live checklist

All settings are in `assets/js/config.js`.

1. **Forms.** Submit any form once on the live site. FormSubmit then sends a one-time activation email to the site inbox; click it to confirm. Every form, quote, pledge, application and entry after that is delivered by email.
2. **AdSense.** Set `adsenseClient` and the slot IDs in the config file, then add your line to `ads.txt`.
3. **Donations.** Paste your PayPal, Stripe, Buy Me a Coffee, GitHub Sponsors or Patreon links. Each button appears only once its link is filled in. Until then, the pledge form collects pledges by email.
4. **Analytics and affiliate.** Set `ga4` and `amazonTag` if you use them.
5. **Custom domain.** Add a `CNAME` file containing `lab.works` and point DNS at GitHub Pages. Then, in `_config.yml`, set `baseurl: ""` and `url: https://lab.works`.

## How it's built

The site runs on GitHub Pages' built-in **Jekyll**, which is free and needs no Actions. The shared header, footer, banner and scripts live in `_layouts/default.html`, and reusable blocks live in `_includes/`. Each page file contains only its own content.

To regenerate the pages after editing content:

```bash
python3 build/build.py                # regenerates pages, sitemap and search index (Jekyll mode)
LW_JEKYLL=0 python3 build/build.py    # alternative: fully static HTML with no Jekyll needed
```

Where content lives:

- `build/data.py`: test categories, calculators, guides, equipment and videos.
- `build/pages_*.py`: page templates.

## Privacy of the contact inbox

The contact email address never appears as plain text anywhere on the site. It is stored XOR-encoded in `assets/js/main.js` and decoded in the browser only when a form is submitted or an "Email us" link is clicked.
