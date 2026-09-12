# Cloudocol — Landing Page

Marketing site for **Cloudocol Technologies Pvt. Ltd.** — a design and engineering
practice building digital products, platforms and the technology that runs them.

A single-page, static site. No build step, no dependencies, no framework runtime.
Open `index.html` and it works.

---

## Contents

- [Stack](#stack)
- [File structure](#file-structure)
- [Running locally](#running-locally)
- [Design system](#design-system)
- [Section map](#section-map)
- [Customising](#customising)
- [Placeholders to replace before launch](#placeholders-to-replace-before-launch)
- [Accessibility and performance](#accessibility-and-performance)
- [Browser support](#browser-support)
- [Deploying](#deploying)
- [Pushing to GitHub](#pushing-to-github)
- [Porting to Next.js](#porting-to-nextjs)
- [Licence](#licence)

---

## Stack

| Layer | Choice | Reason |
|---|---|---|
| Markup | Semantic HTML5 | One page, crawlable, no hydration cost |
| Styling | Hand-written CSS with custom properties | Full control of the type scale and motion curves; no utility-class churn |
| Behaviour | Vanilla ES5-safe JavaScript, ~180 lines | `IntersectionObserver` covers every scroll effect the design needs |
| Type | Manrope 200–800, Google Fonts | One family across display and body |
| Graphics | Inline SVG, authored by hand | No raster assets, no stock photography, sharp at any density |

There is deliberately **no** animation library. GSAP or Lenis would add 40–80 KB
for effects that `IntersectionObserver` plus CSS transitions already handle.

Total page weight is roughly **80 KB** before the webfont, with zero third-party
JavaScript.

---

## File structure

```
cloudocol-website/
├── index.html                  # Home
├── services.html               # Three practices, 15 services, engagement models, FAQ
├── work.html                   # Work index
├── work-commerce-platform.html # Case study 1
├── work-operations-console.html# Case study 2
├── work-field-reporting.html   # Case study 3
├── expertise.html              # Four technology layers + how we choose
├── process.html                # Discover / Design / Build / Evolve, in depth
├── about.html                  # The practice, philosophy, principles
├── contact.html                # Enquiry form + what happens next
├── privacy.html                # Template, needs legal review
├── terms.html                  # Template, needs legal review
├── 404.html                    # Not-found page with route suggestions
├── assets/
│   ├── css/
│   │   └── styles.css          # Tokens, components, sections, motion
│   ├── js/
│   │   └── main.js             # Two modules: home page, then shared page behaviour
│   └── img/                    # Empty — drop the logo and any OG image here
├── tools/                      # Generator. Not deployed, not required at runtime.
│   ├── build.py                # Writes all 13 pages
│   ├── shell.py                # <head>, nav, footer, page fragments
│   ├── content_a.py            # Services, work index, case studies
│   ├── content_b.py            # Expertise, process, about, contact, legal, 404
│   └── home_body.html          # Home page body — edit here
├── .github/workflows/deploy.yml
├── .gitignore
└── README.md
```

### Why there is a generator

Thirteen pages share one header and one footer. Hand-copying that markup means
it drifts within a week. `tools/` is a ~100-line static generator that composes
every page from a single shell:

```bash
python3 tools/build.py      # rewrites all 13 .html files
```

**Edit content in `tools/`, not in the generated HTML** — a rebuild overwrites
the root `.html` files. Home page content lives in `tools/home_body.html`; the
nav and footer live in `tools/shell.py`; every other page body is in
`tools/content_a.py` or `tools/content_b.py`.

The generator is a convenience, not a dependency. The output is plain static
HTML — GitHub Pages, Netlify and every other host see only the `.html` files.
If you would rather not use it, delete `tools/` and edit the pages directly.

`styles.css` is ordered top to bottom:

1. Design tokens (`:root`)
2. Reset and base
3. Layout primitives (`.wrap`, `.section`, `.ruled`)
4. Typography (`.display`, `.h2`, `.lede`, `.label`)
5. Buttons and links
6. One block per section, in page order
7. Reveal system, cursor, `prefers-reduced-motion` overrides

---

## Running locally

No build, no `npm install`. Either open the file directly:

```bash
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

Or serve it, which is closer to production:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

```bash
npx serve .              # if you prefer Node
```

---

## Pages and routing

| Page | Route | Nav state | Notable behaviour |
|---|---|---|---|
| Home | `index.html` | none — indicator follows the scrolled section | Hero sequence, process scroll sync |
| Services | `services.html` | Services | Sticky sub-nav, 15 anchored services, FAQ accordion |
| Work | `work.html` | Work | Tile grid |
| Case studies | `work-*.html` | Work | Prev/next pager, sample-content notice |
| Expertise | `expertise.html` | Expertise | Sticky sub-nav across four layers |
| How we work | `process.html` | About | Stage-by-stage, sticky sub-nav |
| About | `about.html` | About | Overlap diagram, principles |
| Contact | `contact.html` | Contact | Validated form, FAQ |
| Privacy / Terms | `privacy.html`, `terms.html` | none | Sticky table of contents |
| Not found | `404.html` | none | Route suggestions |

**Navigation details:**

- The active route is marked server-side with `aria-current="page"`, so the nav
  is correct before JavaScript runs. The sliding indicator is positioned on load
  and re-measured when the webfont finishes loading.
- On the home page there is no active route, so the indicator follows the
  section you are reading instead — the original scroll-spy behaviour.
- Every service row on the home page deep-links into `services.html#<slug>`,
  and every "View case study" link resolves to a real page. 496 internal links,
  all verified.
- Anchored targets carry `scroll-margin-top` so they clear the fixed header and
  the sticky sub-nav.
- Sub-nav chips use the same reading-line calculation as the process section, and
  the active chip scrolls itself into view on the mobile chip rail.

## Design system

### Colour

| Token | Value | Use |
|---|---|---|
| `--ink` | `#0A100F` | Primary dark surface (green-black, not pure black) |
| `--ink-2` | `#0E1615` | Alternate dark surface, used to separate adjacent dark sections |
| `--ink-3` | `#141D1B` | Raised dark elements |
| `--paper` | `#EDEAE3` | Light surface (warm bone) |
| `--accent` | `#DFA23C` | Brass. CTAs, active states, the hero route, section numbers |
| `--moss` | `#8FB3A8` | Secondary, micro-detail only |
| `--on-ink` | `#E8E6DF` | Text on dark |
| `--on-ink-mute` | `#8A938E` | Secondary text on dark |
| `--on-paper` | `#0A100F` | Text on light |
| `--on-paper-mute` | `#5A615D` | Secondary text on light |

The accent appears in roughly 5% of the page area. That restraint is the point —
widening its use is the fastest way to make the page look ordinary.

### Type

One family, Manrope. The scale is fluid via `clamp()` so it recomposes rather than
shrinks on small screens.

| Role | Size | Weight | Tracking |
|---|---|---|---|
| Display | `clamp(2.6rem, 7.4vw, 6.1rem)` | 300 | `-0.042em` |
| Section heading | `clamp(2rem, 4.4vw, 3.9rem)` | 300 | `-0.036em` |
| Sub-heading | `clamp(1.3rem, 2vw, 1.85rem)` | 400 | `-0.028em` |
| Lede | `clamp(1.02rem, 1.18vw, 1.28rem)` | 300 | `-0.012em` |
| Body | `clamp(15px, 0.52vw + 13.4px, 17px)` | 400 | `-0.005em` |
| Label | `0.7rem` uppercase | 600 | `0.16em` |

Body measure is capped between 40 and 62 characters throughout.

### Layout

- Max width `1560px`, gutter `clamp(20px, 5vw, 80px)`
- Section rhythm `clamp(84px, 11vw, 180px)`, with `--tight` and `--tall` modifiers
- `.ruled` paints six faint vertical hairlines behind a section as a shared measure,
  masked at the top and bottom edges and hidden below 720px

### Motion

Every transition uses one of two curves: `--ease` for colour and opacity,
`--ease-out` for movement. Nothing bounces, nothing overshoots.

| Effect | Mechanism |
|---|---|
| Hero entrance | `.is-lit` class added on load, staggered CSS transition delays |
| Headline reveal | `overflow:hidden` mask, inner span `translateY(105%) → 0` |
| Route drawing | SVG `stroke-dashoffset` 1200 → 0 over 2.6s |
| Section reveals | `IntersectionObserver` adds `.is-in`, stagger via `--d` |
| Counters | `requestAnimationFrame`, cubic ease-out |
| Work images | `clip-path: inset(0 0 100% 0)` wipe, plus scroll parallax on the inner group |
| Magnetic buttons | Pointer offset applied to transform, inner content at 30% |
| Process | `IntersectionObserver` with a `-40% / -45%` root margin drives the active step |

The whole motion layer is suppressed under `prefers-reduced-motion: reduce`, and
`main.js` returns early before binding any pointer-driven effect.

---

## Section map

| # | Section | ID | Surface |
|---|---|---|---|
| — | Navigation | `#nav` | Transparent, condenses on scroll |
| 1 | Hero | `#hero` | Ink |
| 2 | Credibility strip | — | Ink-2, hairline bounded |
| 3 | Services | `#services` | Paper |
| 4 | How we work | `#process` | Ink |
| 5 | Selected work | `#work` | Paper |
| 6 | Why Cloudocol | — | Ink-2 |
| 7 | Expertise | `#expertise` | Ink |
| 8 | About | `#about` | Paper |
| 9 | Final CTA | `#contact` | Ink |
| 10 | Footer | — | `#070C0B` |

Contrast between surfaces does the sectioning, which is why there is no card grid.

---

## Customising

### The logo

The header and footer each contain a logo slot:

```html
<a class="logo" href="#top" aria-label="Cloudocol — home">
  <span class="logo-mark">
    <!-- replace this inline SVG with the Cloudocol mark -->
  </span>
  <span class="logo-word">Cloudocol</span>
</a>
```

Replace the inner SVG with your mark, or swap the whole `.logo-mark` for
`<img src="assets/img/cloudocol-mark.svg" alt="" width="26" height="26">`.
If your mark already contains the wordmark, delete the `.logo-word` span.

`.logo-mark` is sized in CSS and shrinks with the nav on scroll — the markup does
not need to change.

### The accent colour

One value, one place:

```css
:root { --accent: #DFA23C; }
```

Four literal copies exist outside the token, all in SVG `stroke` and `fill`
attributes that cannot read CSS variables — search `index.html` for `DFA23C`.
Check contrast after changing it: `--accent` is used as a background under dark
text on the primary button.

### Copy

All text is in `index.html`. Nothing is generated at runtime.

### Work projects

Each is an `<article class="proj" data-proj>`. Add `proj--flip` to reverse the
layout. Alternate it down the page. To use a photograph instead of the SVG,
replace the `<svg>` inside `.proj-media` with an `<img>` — the aspect ratio,
clip-path reveal and parallax all still apply.

### Services

Each row is a `<li class="svc-row">` with a `<button class="svc-btn">`. Keep the
`svc-idx` numbers sequential across all three practices. The hover, focus and
click handlers bind automatically from `main.js` — no registration needed.

### Expertise tags

Plain `<span class="tag">` inside `.marquee-track`. `main.js` duplicates the track
contents at load for a seamless loop, so write each tag once only.

---

## Wiring the contact form

`contact.html` validates on the client and then stops — there is no backend, and
submitting shows a notice saying so. Pick one:

**Formspree** (or similar) — change two attributes, delete nothing:

```html
<form class="form" id="projectForm" action="https://formspree.io/f/YOUR_ID" method="POST">
```

Then in `assets/js/main.js`, remove the `e.preventDefault()` line in the submit
handler so the browser posts normally once validation passes.

**Netlify Forms** — add `netlify` and a hidden name field:

```html
<form class="form" id="projectForm" name="enquiry" method="POST" data-netlify="true">
  <input type="hidden" name="form-name" value="enquiry" />
```

**Your own endpoint** — replace the success branch of the submit handler with a
`fetch()` POST, and keep the existing `formOk` panel for the response.

Whichever you choose, update the copy in `#formOk` (in `tools/content_b.py`) so
it confirms a real submission rather than explaining the placeholder.

## Placeholders to replace before launch

- [ ] Logo mark in the header and footer
- [ ] `hello@cloudocol.example` → real address (`.example` is a reserved domain, safe to ship by accident but not to keep)
- [ ] `Phone — to be added`
- [ ] Social links — all currently `href="#contact"`
- [ ] Three work projects, each tagged `Sample layout` in the corner
- [ ] Metrics: `4+` years, `20+` projects — confirm before publishing
- [ ] `View case study` links → real case study URLs
- [ ] Privacy and Terms links in the footer
- [ ] Add an Open Graph image and `og:` / `twitter:` meta tags
- [ ] Add `favicon.ico` and an apple touch icon
- [ ] Wire the contact form to a real endpoint (see above)
- [ ] Have `privacy.html` and `terms.html` reviewed — both are templates with bracketed placeholders
- [ ] Confirm the sample case study copy is acceptable, or replace with real work
- [ ] Check `404.html` is served by your host (GitHub Pages and Netlify pick it up automatically)

---

## Accessibility and performance

Built in, not retrofitted:

- Semantic landmarks — `header`, `nav`, `main`, `section`, `article`, `footer`
- Every interactive element is a real `<a>` or `<button>`; service rows respond to
  focus as well as hover
- Visible focus ring: `2px solid var(--accent)` at `3px` offset, never removed
- `prefers-reduced-motion` respected in both CSS and JS
- Mobile menu sets `aria-expanded`, locks body scroll, closes on `Escape`
- Decorative SVG marked `aria-hidden="true"`; meaningful SVG has `role="img"` and a label
- Body text meets WCAG AA on both surfaces; muted text is reserved for secondary copy
- Fonts preconnected and loaded with `display=swap`
- Scroll listeners are passive and rAF-throttled; observers disconnect after firing

Worth running Lighthouse after you add real images — that is the only thing likely
to move the score.

---

## Browser support

Chrome, Edge, Firefox and Safari, last two versions. Requires
`IntersectionObserver`, CSS custom properties, `clamp()` and `clip-path` — all
baseline since 2020. No IE support, no polyfills.

`backdrop-filter` on the scrolled nav degrades to a solid background where
unsupported.

---

## Deploying

It is a static site, so anything that serves files works.

### GitHub Pages, from the repository

Settings → Pages → Source: *Deploy from a branch* → `main` / `/ (root)`.
Live at `https://<user>.github.io/<repo>/` in about a minute.

### GitHub Pages, via Actions

`.github/workflows/deploy.yml` is included. Settings → Pages → Source:
*GitHub Actions*. It publishes on every push to `main`.

### Netlify / Vercel / Cloudflare Pages

Connect the repository. Build command: leave empty. Publish directory: `.` (root).

### A custom domain

Add a `CNAME` file at the root containing `cloudocol.com`, then point the DNS
records at your host.

---

## Pushing to GitHub

```bash
cd cloudocol-website

git init
git add .
git commit -m "Cloudocol landing page"
git branch -M main
git remote add origin https://github.com/<your-username>/cloudocol-website.git
git push -u origin main
```

If the repository is new and empty, that is all. If GitHub created a README for
you, run `git pull --rebase origin main` before pushing.

Suggested first issues, if you want the work tracked:

1. Replace the logo placeholder
2. Add real contact details and social URLs
3. Publish the first case study
4. Add Open Graph and favicon assets
5. Wire the CTA to a contact form

---

## Porting to Next.js

The structure maps onto components one to one, with no refactoring:

```
app/page.tsx
components/
  Nav.tsx  Hero.tsx  Credibility.tsx  Services.tsx  Process.tsx
  Work.tsx  Why.tsx  Expertise.tsx  About.tsx  CTA.tsx  Footer.tsx
  ui/Button.tsx  ui/Marquee.tsx  ui/Reveal.tsx  ui/SectionHeading.tsx
```

Three notes if you do:

- The tokens in `:root` become the `theme.extend` block in `tailwind.config.ts`.
  The fluid `clamp()` scale carries over as `fontSize` entries unchanged.
- The observers in `main.js` become one `useReveal()` hook shared by every section.
- Load Manrope through `next/font/google` to drop the render-blocking stylesheet
  link.

---

## Licence

Not yet set. This is proprietary work for Cloudocol Technologies Pvt. Ltd. — if
the repository is public, add a `LICENSE` file stating your terms, or keep the
repository private. A repository with no licence grants no rights to anyone, which
may be exactly what you want here.

---

**Cloudocol Technologies Pvt. Ltd.**
