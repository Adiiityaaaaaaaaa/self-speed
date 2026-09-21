# Self Speed — Production Plan

Turning the prototype into a live, ad-monetised site.

**Live prototype:** https://adiiityaaaaaaaaa.github.io/self-speed/
**Target domain:** `selfspeed.in` or `selfspeed.app`

---

## The core insight

The code is a weekend. **AdSense approval is the long pole**, and it is gated on
content that doesn't exist yet. Google rejects thin single-purpose pages as
"low value content" — a lone gauge with 40 words of text is the canonical
rejection case.

So this plan is mostly **content and compliance**, not JavaScript.

Benchmark: [zpeed.in](https://zpeed.in) does ~484K visits/month (Similarweb,
Oct 2025) on Google AdSense (`ca-pub-5200094130124288`, 8 ad slots). Estimated
revenue ~$500–1,000/month. Working backwards, that is roughly **$0.002 per
visit**. The gauge is ~10% of that site; the content that ranks is the business.

---

## Domain

Checked via RDAP on 2026-09-21 — confirm at a registrar before trusting:

| Domain | Status | Notes |
|---|---|---|
| `selfspeed.com` | **taken** | — |
| `selfspeed.in` | available | ~₹500–900/yr. Matches where this niche's traffic is |
| `selfspeed.app` | available | ~$14–20/yr. `.app` is HSTS-preloaded — forced HTTPS |
| `selfspeed.net` / `.org` | available | weaker fit |

Recommendation: `.in` for the India-first audience, `.app` to read as a global
product. Both is ~$25 and hedges.

---

## Phase 1 — Fix the product (2–3 days)

Gaps that make it unusable in the field today.

- [x] **Screen Wake Lock** — the screen sleeps mid-ride and tracking dies.
      Highest-value fix.
- [x] **PWA + offline** — manifest, service worker, installable to home screen.
      Also a ranking signal.
- [x] **Trip history** — persist sessions to `localStorage`; gives people a
      reason to return.
- [x] **GPX export** — differentiates from every competitor, cheap to build.
- [x] **Honest desktop state** — detect no-GPS and say so instead of showing a
      dead zero.

## Phase 2 — Content (1–3 weeks, the real work)

~12–15 indexable pages. Each targets one keyword and doubles as AdSense
evidence. 800+ words each, actually useful.

- [ ] Six use-case pages: cycling, running, driving, boating (knots), skiing, transit
- [ ] Converter pages: `kmh-to-mph`, `mph-to-kmh`, `knots-to-kmh` — boring, cheap, rank well
- [ ] "How GPS speedometers work" / "Is GPS speed accurate?" — genuine explainer depth
- [ ] About, Contact, Privacy, Terms

## Phase 3 — Infrastructure (half a day)

- [ ] **Cloudflare Pages** over GitHub Pages — free, custom domain, better India
      latency, real analytics
- [ ] Point DNS at Cloudflare, enable HTTPS + HSTS
- [ ] **Google Search Console** + `sitemap.xml` + `robots.txt` — submit on day
      one, indexing takes weeks
- [ ] GA4 or Cloudflare Web Analytics

## Phase 4 — Compliance (half a day, non-negotiable)

- [ ] **Privacy policy explicitly covering geolocation.** Even though location
      never leaves the device, say so. Also cover AdSense cookies.
- [ ] **A Google-certified CMP.** Mandatory for EEA/UK traffic. Google's own
      Privacy & Consent Management is free. Serving ads to EU users without one
      violates policy.
- [ ] India DPDP Act compliance if going `.in`.

## Phase 5 — AdSense (week 4, then wait 1–4 weeks)

Apply only once Phases 2–4 are live.

- [ ] **Auto Ads with the anchor unit** — this is what makes long sessions pay.
      The sticky bar stays visible for the whole ~7-minute session.
- [ ] **Nothing over the gauge.** People read this while driving. Keep the
      instrument clean; ads go above and below.
- [ ] **Do not auto-refresh ads.** Common AdSense ban reason. Auto Ads anchor is
      the compliant way to monetise long sessions.

Expect rejection the first time. Add content and reapply.

## Phase 6 — SEO (months 2–12)

- [ ] Backlinks from cycling and sailing forums, Reddit, niche communities
- [ ] Track rankings in Search Console
- [ ] Expand whichever use-case page gains traction

Do not chase "gps speedometer" — unwinnable against an incumbent at 484K
visits. Target "ski speed tracker", "sailing speed knots log", "cycling
speedometer GPX export".

---

## Costs

| Item | Cost |
|---|---|
| Domain | $10–20/yr |
| Cloudflare Pages | $0 |
| Everything else | $0 |
| **Total** | **~$15/yr** |

## Timeline

| When | Milestone |
|---|---|
| Week 1 | Product fixes done |
| Week 3–4 | Content live, AdSense applied |
| Month 2–3 | Approved, first pages indexed, first revenue |
| Month 6 | ~5–20K visits → $10–40/mo |
| Month 12+ | 50K+ visits → $100+/mo, if the SEO lands |

## Honest expectations

At ~$0.002/visit this is a long game where the content compounds and the code
does not. It costs ~$15 to find out. The SEO and ad-ops experience transfers to
anything built next.
