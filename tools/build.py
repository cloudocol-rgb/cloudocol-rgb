#!/usr/bin/env python3
"""Cloudocol — build all pages.

    python3 tools/build.py

Reads the current index.html for the home page body (so home-page content
stays editable in place), rewrites its links for a multi-page site, and
writes every page through the shared shell in shell.py.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shell import ROOT, write, ARROW                      # noqa: E402
import content_a as A                                     # noqa: E402
import content_b as B                                     # noqa: E402

SERVICE_SLUGS = [
    "uiux", "product-design", "design-systems", "branding", "ux-research",
    "web-development", "mobile-apps", "custom-software", "api-backend", "ecommerce",
    "cloud", "ai-automation", "devops", "integration", "consulting",
]


def home_body():
    """Read the home body source and re-point its links for a multi-page site."""
    path = os.path.join(ROOT, "tools", "home_body.html")
    if not os.path.exists(path):
        raise SystemExit("tools/home_body.html is missing — restore it from git before rebuilding.")
    body = open(path, encoding="utf-8").read()

    # Service rows become real links into the services page.
    parts = body.split('<button class="svc-btn" type="button">')
    if len(parts) - 1 != len(SERVICE_SLUGS):
        raise SystemExit(f"expected {len(SERVICE_SLUGS)} service rows, found {len(parts) - 1}")
    body = parts[0]
    for slug, chunk in zip(SERVICE_SLUGS, parts[1:]):
        body += f'<a class="svc-btn" href="services.html#{slug}">' + chunk
    body = body.replace("</button></li>", "</a></li>")

    # Case study links, in page order.
    for href, _title, _cat, _art in A.CASES:
        body = body.replace('<a class="link-a" href="#contact">View case study',
                            f'<a class="link-a" href="{href}">View case study', 1)

    # A route out of the work section.
    body = body.replace(
        '    <div style="margin-top:clamp(48px,6vw,84px)"',
        '    <div style="margin-top:clamp(48px,6vw,84px)"', 1)
    body = re.sub(
        r"(</article>\s*)(\n\s*</div>\s*</section>\s*<!-- ========================= WHY)",
        r'\1\n    <div style="margin-top:clamp(44px,5vw,76px)" data-reveal>\n'
        r'      <a class="btn btn--ghost magnetic" href="work.html"><span class="btn-in">View all work '
        + ARROW + r'</span></a>\n    </div>\2',
        body, count=1)

    # Remaining in-page CTAs now point at real pages.
    body = body.replace('href="#contact"', 'href="contact.html"')
    body = body.replace('href="#work"', 'href="work.html"')
    return body


PAGES = []


def add(filename, page, title, desc, body):
    PAGES.append(write(filename, page, title, desc, body))


def main():
    add("index.html", "home",
        "Cloudocol — Technology, designed around your ambition",
        "Cloudocol Technologies Pvt. Ltd. — design, engineering and cloud technology for ambitious businesses.",
        home_body())

    add("services.html", "services",
        "Services — Cloudocol",
        "Design, development and technology services: UI/UX, product design, web and mobile development, cloud, AI and automation.",
        A.SERVICES_BODY)

    add("work.html", "work",
        "Work — Cloudocol",
        "Selected engagements: commerce platforms, operations software and field applications.",
        A.WORK_BODY)

    for i, (filename, title, cat, _art) in enumerate(A.CASES):
        add(filename, "work",
            f"{re.sub('&amp;', 'and', title)} — Cloudocol",
            f"{re.sub('&amp;', 'and', cat)}: how Cloudocol runs an engagement of this shape.",
            A.case_body(i))

    add("expertise.html", "expertise",
        "Expertise — Cloudocol",
        "Product, engineering, intelligence and infrastructure — the technologies we work with and how we choose them.",
        B.EXPERTISE_BODY)

    add("process.html", "about",
        "How we work — Cloudocol",
        "Discover, design, build, evolve. How a Cloudocol engagement runs, stage by stage.",
        B.PROCESS_BODY)

    add("about.html", "about",
        "About — Cloudocol",
        "Cloudocol Technologies Pvt. Ltd. is a design and engineering practice building digital products and the technology behind them.",
        B.ABOUT_BODY)

    add("contact.html", "contact",
        "Contact — Cloudocol",
        "Start a project with Cloudocol. Tell us what you are building and we will come back with scope, cost and an honest view.",
        B.CONTACT_BODY)

    add("privacy.html", "",
        "Privacy policy — Cloudocol",
        "What Cloudocol collects, why, and what you can ask us to do with it.",
        B.PRIVACY_BODY)

    add("terms.html", "",
        "Terms of use — Cloudocol",
        "The terms on which the Cloudocol website is provided.",
        B.TERMS_BODY)

    add("404.html", "",
        "Page not found — Cloudocol",
        "That page does not exist. Here is where to go instead.",
        B.NOTFOUND_BODY)

    print(f"built {len(PAGES)} pages:")
    for p in PAGES:
        print("  ", p)


if __name__ == "__main__":
    main()
