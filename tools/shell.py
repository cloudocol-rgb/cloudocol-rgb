"""Cloudocol — static site generator.

Single source of truth for the page shell. Edit the nav, footer or <head>
here (or the body content in content_*.py) and run:

    python3 tools/build.py

Output is plain static HTML in the repository root. Nothing is required at
runtime — the generator exists so the shell cannot drift between 13 pages.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("services",  "Services",  "services.html"),
    ("work",      "Work",      "work.html"),
    ("expertise", "Expertise", "expertise.html"),
    ("about",     "About",     "about.html"),
    ("contact",   "Contact",   "contact.html"),
]

LOGO_SVG = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <path d="M3 16h13a4 4 0 1 0-1.2-7.8A6 6 0 0 0 3 10" stroke="#DFA23C" stroke-width="1.6" stroke-linecap="round"/>
          <path d="M6 20h9" stroke="#E8E6DF" stroke-width="1.6" stroke-linecap="round" opacity=".55"/>
        </svg>"""

ARROW = ('<svg class="arrow" viewBox="0 0 16 16" aria-hidden="true">'
         '<line x1="1" y1="8" x2="14" y2="8"/><polyline points="9,3 14,8 9,13"/></svg>')


def nav_html(page):
    links = []
    for key, label, href in NAV:
        on = ' aria-current="page"' if key == page else ''
        cls = "nav-link is-active" if key == page else "nav-link"
        links.append(f'<a class="{cls}" href="{href}"{on}>{label}</a>')
    menu = "\n      ".join(
        f'<a class="menu-link" href="{href}">{label}</a>' for _, label, href in NAV
    )
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<div class="cursor" id="cursor" aria-hidden="true"></div>

<header class="nav" id="nav">
  <span class="progress" id="progress" aria-hidden="true"></span>
  <div class="wrap nav-in">
    <a class="logo" href="index.html" aria-label="Cloudocol — home">
      <!-- LOGO SLOT: replace the inline <svg> below with the supplied Cloudocol mark -->
      <span class="logo-mark">
        {LOGO_SVG}
      </span>
      <span class="logo-word">Cloudocol</span>
    </a>

    <nav class="nav-links" id="navLinks" aria-label="Primary">
      {chr(10) + '      ' + (chr(10) + '      ').join(links)}
      <span class="nav-ind" id="navInd" aria-hidden="true"></span>
    </nav>

    <div class="nav-right">
      <a class="btn btn--solid magnetic" href="contact.html"><span class="btn-in"><span class="dot"></span>Start a project</span></a>
      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<div class="menu" id="menu">
  <nav aria-label="Mobile">
      {menu}
  </nav>
  <div class="menu-foot">
    <span>Cloudocol Technologies Pvt. Ltd.</span>
    <span>hello@cloudocol.example</span>
  </div>
</div>"""


FOOTER = f"""<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="logo" href="index.html" aria-label="Cloudocol — home">
          <span class="logo-mark">
            {LOGO_SVG}
          </span>
          <span class="logo-word">Cloudocol</span>
        </a>
        <p>A design and engineering practice building digital products, platforms and the technology that runs them.</p>
      </div>

      <div class="foot-col">
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#design">Design</a></li>
          <li><a href="services.html#development">Development</a></li>
          <li><a href="services.html#technology">Cloud &amp; DevOps</a></li>
          <li><a href="services.html#technology">AI &amp; automation</a></li>
          <li><a href="services.html#technology">Consulting</a></li>
        </ul>
      </div>

      <div class="foot-col">
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="work.html">Work</a></li>
          <li><a href="expertise.html">Expertise</a></li>
          <li><a href="process.html">How we work</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>

      <!-- Contact details use the reserved .example domain as placeholders — swap in real ones -->
      <div class="foot-col">
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:hello@cloudocol.example">hello@cloudocol.example</a></li>
          <li><a href="contact.html">Phone — to be added</a></li>
          <li><a href="contact.html">LinkedIn</a></li>
          <li><a href="contact.html">Instagram</a></li>
          <li><a href="contact.html">GitHub</a></li>
        </ul>
      </div>
    </div>

    <div class="foot-bar">
      <span>© <span id="yr">2026</span> Cloudocol Technologies Pvt. Ltd. All rights reserved.</span>
      <span><a href="privacy.html">Privacy</a> &nbsp;·&nbsp; <a href="terms.html">Terms</a></span>
    </div>
  </div>
</footer>

<button class="totop" id="toTop" aria-label="Back to top">
  <svg width="15" height="15" viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4">
    <line x1="8" y1="14" x2="8" y2="2"/><polyline points="3,7 8,2 13,7"/>
  </svg>
</button>"""


SHELL = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="theme-color" content="#0A100F" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css" />
<noscript><style>
  /* content must never depend on JavaScript to become visible */
  [data-reveal],[data-proj],[data-why],[data-fig]{{ opacity:1 !important; transform:none !important; }}
  .mask > span{{ transform:none !important; }}
  .proj-media{{ clip-path:none !important; }}
  .proc-step{{ opacity:1 !important; }}
  .cursor,.progress{{ display:none !important; }}
</style></noscript>
</head>
<body data-page="{page}">

{nav}

<main id="main">
{body}
</main>

{footer}

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def write(filename, page, title, desc, body):
    html = SHELL.format(
        title=title, desc=desc, page=page, body=body.strip(),
        nav=nav_html(page), footer=FOOTER,
    )
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return filename


# ---------------------------------------------------------------- fragments

def pagehero(crumbs, label, num, h1, lede, facts=None):
    """Inner-page hero: breadcrumb trail, section number, headline, lede."""
    trail = []
    for i, (text, href) in enumerate(crumbs):
        if href:
            trail.append(f'<a href="{href}">{text}</a>')
        else:
            trail.append(f'<span aria-current="page">{text}</span>')
        if i < len(crumbs) - 1:
            trail.append('<span class="sep">/</span>')
    facts_html = ""
    if facts:
        rows = "".join(
            f'<div class="fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in facts
        )
        facts_html = f'<dl class="pagehero-facts" data-reveal style="--d:.12s">{rows}</dl>'
    return f"""<section class="pagehero ruled">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">{''.join(trail)}</nav>
    <div class="pagehero-grid">
      <div>
        <div class="label" style="margin-bottom:clamp(18px,2vw,28px)"><span class="num">{num}</span><span class="slash">/</span>{label}</div>
        <h1 class="display" data-reveal>{h1}</h1>
        <p class="lede" data-reveal style="--d:.08s">{lede}</p>
      </div>
      {facts_html}
    </div>
  </div>
</section>"""


def subnav(items):
    links = "".join(f'<a href="#{i}">{t}</a>' for i, t in items)
    return f"""<div class="subnav">
  <div class="wrap subnav-in">{links}</div>
</div>"""


def band(heading, text, cta_label="Start a project", cta_href="contact.html"):
    return f"""<section class="section section--tight panel-ink band">
  <div class="wrap band-in">
    <div>
      <h2 class="h2" data-reveal>{heading}</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.1em">{text}</p>
    </div>
    <a class="btn btn--solid magnetic" href="{cta_href}" data-reveal style="--d:.14s"><span class="btn-in"><span class="dot"></span>{cta_label} {ARROW}</span></a>
  </div>
</section>"""
