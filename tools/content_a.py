"""Page bodies: services, work index, three case studies."""

from shell import pagehero, subnav, band, ARROW

# ---------------------------------------------------------------- artwork
# Hand-authored SVG. No raster assets anywhere in the project.

ART_COMMERCE = """<svg viewBox="0 0 800 550" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
  <rect width="800" height="550" fill="#0A100F"/>
  <g stroke="rgba(232,230,223,.07)">
    <line x1="0" y1="137" x2="800" y2="137"/><line x1="0" y1="275" x2="800" y2="275"/><line x1="0" y1="412" x2="800" y2="412"/>
    <line x1="200" y1="0" x2="200" y2="550"/><line x1="400" y1="0" x2="400" y2="550"/><line x1="600" y1="0" x2="600" y2="550"/>
  </g>
  <circle cx="400" cy="275" r="60" fill="none" stroke="#DFA23C" stroke-width="1.4"/>
  <circle cx="400" cy="275" r="110" fill="none" stroke="rgba(223,162,60,.55)" stroke-width="1"/>
  <circle cx="400" cy="275" r="165" fill="none" stroke="rgba(232,230,223,.22)" stroke-width="1" stroke-dasharray="2 7"/>
  <circle cx="400" cy="275" r="222" fill="none" stroke="rgba(232,230,223,.13)" stroke-width="1"/>
  <path d="M400 110 A165 165 0 0 1 540 195" fill="none" stroke="#DFA23C" stroke-width="3" stroke-linecap="round"/>
  <circle cx="400" cy="165" r="5" fill="#DFA23C"/>
  <circle cx="510" cy="275" r="4" fill="#8FB3A8"/>
  <circle cx="290" cy="275" r="4" fill="rgba(232,230,223,.5)"/>
</svg>"""

ART_OPS = """<svg viewBox="0 0 800 550" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
  <rect width="800" height="550" fill="#0E1615"/>
  <g stroke="rgba(232,230,223,.06)">
    <line x1="0" y1="110" x2="800" y2="110"/><line x1="0" y1="220" x2="800" y2="220"/>
    <line x1="0" y1="330" x2="800" y2="330"/><line x1="0" y1="440" x2="800" y2="440"/>
  </g>
  <g fill="rgba(143,179,168,.30)">
    <rect x="90" y="330" width="34" height="110"/><rect x="146" y="286" width="34" height="154"/>
    <rect x="202" y="352" width="34" height="88"/><rect x="258" y="242" width="34" height="198"/>
    <rect x="314" y="308" width="34" height="132"/><rect x="370" y="198" width="34" height="242"/>
  </g>
  <g fill="#DFA23C">
    <rect x="426" y="264" width="34" height="176"/><rect x="482" y="176" width="34" height="264"/>
    <rect x="538" y="220" width="34" height="220"/><rect x="594" y="132" width="34" height="308"/>
    <rect x="650" y="176" width="34" height="264"/>
  </g>
  <path d="M107 300 L163 262 L219 322 L275 212 L331 278 L387 168 L443 234 L499 146 L555 190 L611 102 L667 146"
        fill="none" stroke="rgba(232,230,223,.75)" stroke-width="1.4"/>
  <circle cx="611" cy="102" r="5" fill="#EDEAE3"/>
</svg>"""

ART_FIELD = """<svg viewBox="0 0 800 550" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
  <rect width="800" height="550" fill="#0A100F"/>
  <g stroke="rgba(232,230,223,.06)">
    <line x1="160" y1="0" x2="160" y2="550"/><line x1="320" y1="0" x2="320" y2="550"/>
    <line x1="480" y1="0" x2="480" y2="550"/><line x1="640" y1="0" x2="640" y2="550"/>
  </g>
  <rect x="262" y="96" width="176" height="358" rx="20" fill="none" stroke="rgba(232,230,223,.30)" stroke-width="1.4"/>
  <rect x="286" y="132" width="128" height="10" rx="5" fill="rgba(232,230,223,.30)"/>
  <rect x="286" y="162" width="90" height="10" rx="5" fill="rgba(232,230,223,.16)"/>
  <rect x="286" y="200" width="128" height="62" rx="8" fill="rgba(223,162,60,.18)" stroke="#DFA23C" stroke-width="1"/>
  <rect x="286" y="278" width="128" height="46" rx="8" fill="rgba(232,230,223,.06)"/>
  <rect x="286" y="338" width="128" height="46" rx="8" fill="rgba(232,230,223,.06)"/>
  <rect x="378" y="140" width="176" height="358" rx="20" fill="#0E1615" stroke="rgba(232,230,223,.18)" stroke-width="1.4" opacity=".92"/>
  <rect x="402" y="176" width="128" height="10" rx="5" fill="rgba(232,230,223,.22)"/>
  <path d="M402 250 L438 286 L530 210" fill="none" stroke="#DFA23C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="466" cy="410" r="30" fill="none" stroke="rgba(143,179,168,.55)" stroke-width="1"/>
</svg>"""

CASES = [
    ("work-commerce-platform.html", "Replatforming a multi-region storefront", "Commerce platform", ART_COMMERCE),
    ("work-operations-console.html", "An operations console for a distributed team", "Operations software", ART_OPS),
    ("work-field-reporting.html", "Field reporting without the paperwork", "Mobile &amp; automation", ART_FIELD),
]

SAMPLE_NOTE = ('<p class="note-band" data-reveal><strong>Illustrative case study.</strong> '
               'This describes how Cloudocol runs an engagement of this shape. It is not an '
               'account of a specific client project, and no client is named or implied. '
               'Published case studies will replace these pages as they are cleared for release.</p>')


# ---------------------------------------------------------------- services

def _svc(slug, name, detail):
    return f'<div class="defrow" id="{slug}"><dt>{name}</dt><dd>{detail}</dd></div>'


SERVICES_BODY = (
    pagehero(
        [("Home", "index.html"), ("Services", None)],
        "Services", "01",
        "Three practices, one delivery team.",
        "Most engagements need design, engineering and infrastructure at the same time. "
        "We keep them in one team so decisions are made once, by people who carry them through.",
        facts=[("Practices", "Design · Development · Technology"),
               ("Services", "15 disciplines"),
               ("Engagement", "Project, embedded or retained")],
    )
    + subnav([("design", "Design"), ("development", "Development"), ("technology", "Technology"),
              ("engagement", "How we engage"), ("faq", "Questions")])
    + f"""
<section class="section panel-paper ruled" id="design">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">01</span><span class="slash">/</span>Practice</div>
      <h2 class="h2" data-reveal style="margin-top:1em">Design</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.2em">Interfaces people understand on first use, and a visual system that still holds together two years later.</p>
      <p class="body-mute" data-reveal style="--d:.12s;margin-top:1.4em;font-size:.94rem">Design leads the brief here. It decides what gets built and in what order, not how the finished thing is decorated.</p>
    </div>
    <dl class="deflist" data-reveal style="--d:.1s">
      {_svc("uiux", "UI/UX design", "Interface and interaction design, from the first flow diagram through to production-ready screens with every state specified — loading, empty, error, permission-denied.")}
      {_svc("product-design", "Product design", "Shaping what gets built and in what order. We work from the outcome you are measured on backwards, which usually means cutting the first feature list in half.")}
      {_svc("design-systems", "Design systems", "Tokens, components and written usage rules, delivered in both Figma and code so the two cannot drift apart. Built for your team to extend without us.")}
      {_svc("branding", "Branding &amp; visual identity", "Identity work made for screens first: logo, type scale, colour with contrast checked, motion principles, and the rules that keep it coherent as it is applied.")}
      {_svc("ux-research", "UX research", "Interviews, usability testing and behavioural data. Enough evidence to settle an internal argument, run at a scale that fits the decision being made.")}
    </dl>
  </div>
</section>

<section class="section panel-ink ruled" id="development">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">02</span><span class="slash">/</span>Practice</div>
      <h2 class="h2" data-reveal style="margin-top:1em">Development</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.2em">Software written to be read, extended and handed over. Performance and accessibility are part of the build, not a later pass.</p>
      <p class="body-mute" data-reveal style="--d:.12s;margin-top:1.4em;font-size:.94rem">You own the repository from the first commit. Every project ships with a README that a developer who has never met us can follow.</p>
    </div>
    <dl class="deflist" data-reveal style="--d:.1s">
      {_svc("web-development", "Web development", "Marketing sites, customer portals and web applications on React, Next.js and TypeScript. Server-rendered where it helps the user, static where it helps the bill.")}
      {_svc("mobile-apps", "Mobile app development", "iOS and Android, native or cross-platform depending on what the app actually does. Released through your own store accounts, under your own identity.")}
      {_svc("custom-software", "Custom software", "Internal tools and line-of-business systems — the ones that replace a shared spreadsheet, three inboxes and a person who knows the process by heart.")}
      {_svc("api-backend", "API &amp; backend development", "Services, data models and integrations designed for the load you will actually see, with the schema documented and versioned from day one.")}
      {_svc("ecommerce", "E-commerce", "Storefronts, checkout and payments, headless or platform-based. Measured on completed orders, not page count.")}
    </dl>
  </div>
</section>

<section class="section panel-paper ruled" id="technology">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">03</span><span class="slash">/</span>Practice</div>
      <h2 class="h2" data-reveal style="margin-top:1em">Technology</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.2em">The layer underneath: infrastructure, automation, and the judgement calls about what to build, buy or retire.</p>
      <p class="body-mute" data-reveal style="--d:.12s;margin-top:1.4em;font-size:.94rem">Infrastructure is defined in code and lives in your cloud account. Nothing we set up requires us to keep the lights on.</p>
    </div>
    <dl class="deflist" data-reveal style="--d:.1s">
      {_svc("cloud", "Cloud solutions", "Architecture, migration and cost control across AWS, Azure and Google Cloud. Sized for the next stage of growth rather than a hypothetical one.")}
      {_svc("ai-automation", "AI &amp; automation", "Applied where it removes real work — document handling, support triage, internal search. We will tell you when a rule engine is the better answer.")}
      {_svc("devops", "DevOps", "Pipelines, environments, monitoring and alerting, so that releasing stops being an event people schedule around.")}
      {_svc("integration", "System integration", "Connecting the tools you already run, including the old one nobody wants to touch. Contracts first, then the adapters.")}
      {_svc("consulting", "IT consulting", "Technical due diligence, platform selection and roadmaps, with the trade-offs written down rather than delivered as a recommendation.")}
    </dl>
  </div>
</section>

<section class="section panel-ink" id="engagement">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">04</span><span class="slash">/</span>How we engage</div>
        <h2 class="h2" data-reveal>Three ways to work with us.</h2>
      </div>
      <p class="lede" data-reveal style="--d:.08s">Most relationships start with a fixed-scope project and move to a retainer once there is something live to look after.</p>
    </div>
    <div class="cols cols--3">
      <div class="block" data-reveal>
        <span class="bnum">Model 01</span>
        <h3>Fixed-scope project</h3>
        <p>A defined outcome, a fixed price and a delivery date. Best when the problem is clear and you need it built. Scope changes are quoted, not absorbed silently.</p>
      </div>
      <div class="block" data-reveal style="--d:.08s">
        <span class="bnum">Model 02</span>
        <h3>Embedded team</h3>
        <p>Our designers and engineers work inside your process — your standups, your board, your repository. Best when you have direction and need capacity.</p>
      </div>
      <div class="block" data-reveal style="--d:.16s">
        <span class="bnum">Model 03</span>
        <h3>Ongoing retainer</h3>
        <p>A monthly allocation for improvement, support and the next set of features. Unused time is carried, not billed twice.</p>
      </div>
    </div>
  </div>
</section>

<section class="section panel-paper" id="faq">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">05</span><span class="slash">/</span>Questions</div>
      <h2 class="h2" data-reveal style="margin-top:1em">Before you ask.</h2>
      <p class="body-mute" data-reveal style="--d:.08s;margin-top:1.4em;font-size:.94rem">If your question is not here, it is probably a good one. Send it over.</p>
    </div>
    <div data-reveal style="--d:.1s">
      <details class="faq">
        <summary>How much does a project cost?<span class="pm"></span></summary>
        <div class="faq-body"><p>It depends on scope, and we would rather say so than publish a number that means nothing. After a first conversation we send a written estimate with the assumptions it rests on, so you can see which parts are driving the cost and cut them if you want to.</p></div>
      </details>
      <details class="faq">
        <summary>How long does it take?<span class="pm"></span></summary>
        <div class="faq-body"><p>A focused marketing site is usually four to six weeks. A product build is measured in months, with a working version in your hands long before the end. We share a build every two weeks from the start of development.</p></div>
      </details>
      <details class="faq">
        <summary>Do we own the code and the designs?<span class="pm"></span></summary>
        <div class="faq-body"><p>Yes, in full, on final payment. The repository is yours from the first commit and the design files are in your workspace, not ours.</p></div>
      </details>
      <details class="faq">
        <summary>Can you work with our existing team?<span class="pm"></span></summary>
        <div class="faq-body"><p>Often that is the better arrangement. We can take one layer — design, or the frontend, or the infrastructure — and work to your standards and review process rather than importing ours.</p></div>
      </details>
      <details class="faq">
        <summary>What happens after launch?<span class="pm"></span></summary>
        <div class="faq-body"><p>Every project ends with a handover: documentation, a walkthrough recording and a support window. After that you can take it in-house, keep us on a retainer, or call when something needs doing. All three are normal.</p></div>
      </details>
      <details class="faq">
        <summary>Will you sign an NDA?<span class="pm"></span></summary>
        <div class="faq-body"><p>Yes. Send yours, or ask and we will send a short mutual one.</p></div>
      </details>
    </div>
  </div>
</section>
"""
    + band("Know what you need building?",
           "Send the outline. We will come back with scope, cost and an honest view of whether we are the right team.")
)


# ---------------------------------------------------------------- work index

def _tile(href, art, cat, title, desc, delay):
    return f"""<a class="tile" href="{href}" data-reveal style="--d:{delay}">
        <div class="tile-media">{art}</div>
        <div class="tile-body">
          <div class="kcat">{cat}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </a>"""


WORK_BODY = (
    pagehero(
        [("Home", "index.html"), ("Work", None)],
        "Work", "02",
        "Selected work.",
        "Representative engagement formats, shown while client case studies are prepared for publication. "
        "Named projects will appear here as they are released.",
        facts=[("Status", "Sample layouts"), ("Sectors", "Commerce, operations, field services"),
               ("Disciplines", "Design, engineering, cloud")],
    )
    + f"""
<section class="section panel-paper ruled">
  <div class="wrap">
    <div class="cols cols--3" style="align-items:start">
      {_tile(CASES[0][0], ART_COMMERCE, "Commerce platform", CASES[0][1],
             "A headless rebuild of a catalogue-heavy store, with checkout rewritten around the three steps customers actually complete.", ".0s")}
      {_tile(CASES[1][0], ART_OPS, "Operations software", CASES[1][1],
             "One interface replacing four tools and a shared inbox, with roles, audit trails and reporting built in from day one.", ".08s")}
      {_tile(CASES[2][0], ART_FIELD, "Mobile &amp; automation", CASES[2][1],
             "An offline-capable mobile app for site teams, feeding a workflow that turns submissions into approved records automatically.", ".16s")}
    </div>

    <div style="margin-top:clamp(48px,6vw,84px);max-width:60ch" data-reveal>
      <p class="work-note">Each page describes how we run an engagement of that shape — the problem, the approach, what shipped and what we measure. They are written from our own delivery process, not from a specific client account.</p>
    </div>
  </div>
</section>
"""
    + band("Have something at this scale?",
           "Tell us where it is now — an idea, a half-built product, or a system that has stopped keeping up.")
)


# ---------------------------------------------------------------- case studies

def case_body(index):
    href, title, cat, art = CASES[index]
    prev_i, next_i = (index - 1) % len(CASES), (index + 1) % len(CASES)

    content = CASE_CONTENT[index]

    pager = f"""<nav class="pager" aria-label="More work">
  <a href="{CASES[prev_i][0]}"><span class="inner"><span class="dir">Previous</span><span class="ttl">{CASES[prev_i][1]}</span></span></a>
  <a href="{CASES[next_i][0]}"><span class="inner"><span class="dir">Next</span><span class="ttl">{CASES[next_i][1]}</span></span></a>
</nav>"""

    return (
        pagehero(
            [("Home", "index.html"), ("Work", "work.html"), (content["crumb"], None)],
            cat, f"0{index + 1}", title, content["lede"],
            facts=content["facts"],
        )
        + f"""
<section class="section section--tight panel-paper">
  <div class="wrap">
    <figure style="margin:0" data-reveal>
      <div class="case-fig">{art}</div>
      <figcaption class="case-cap">{content["caption"]}</figcaption>
    </figure>
    <div style="margin-top:clamp(32px,4vw,56px);max-width:64ch">{SAMPLE_NOTE}</div>
  </div>
</section>

<section class="section panel-paper">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">01</span><span class="slash">/</span>The problem</div>
    </div>
    <div data-reveal>
      {content["problem"]}
    </div>
  </div>
</section>

<section class="section panel-ink ruled">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">02</span><span class="slash">/</span>Approach</div>
      <p class="pull" data-reveal style="margin-top:1.6em">{content["pull"]}</p>
    </div>
    <div data-reveal style="--d:.08s">
      {content["approach"]}
    </div>
  </div>
</section>

<section class="section panel-paper">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">03</span><span class="slash">/</span>What shipped</div>
        <h2 class="h2" data-reveal>{content["shipped_head"]}</h2>
      </div>
    </div>
    <dl class="deflist" data-reveal>
      {content["shipped"]}
    </dl>
  </div>
</section>

<section class="section panel-ink">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">04</span><span class="slash">/</span>What we measure</div>
        <h2 class="h2" data-reveal>Success, defined before the build.</h2>
      </div>
      <p class="lede" data-reveal style="--d:.08s">Numbers here are the ones we agree at the start and instrument on day one — not figures assembled afterwards to make a case study read well.</p>
    </div>
    <dl class="case-meta" data-reveal>
      {content["measures"]}
    </dl>
  </div>
</section>

{pager}
"""
        + band("Working on something similar?",
               "We will tell you quickly whether this shape of engagement fits your problem.")
    )


CASE_CONTENT = [
    {  # commerce
        "crumb": "Commerce platform",
        "lede": "A catalogue-heavy storefront rebuilt headless, with checkout reduced to the steps customers "
                "actually complete and content the merchandising team can change without a release.",
        "facts": [("Sector", "Retail &amp; commerce"), ("Engagement", "Fixed-scope, then retainer"),
                  ("Team", "2 design, 3 engineering"), ("Disciplines", "UX, design system, Next.js, cloud")],
        "caption": "Composition showing the catalogue and checkout surfaces of a headless storefront.",
        "problem": """<p class="body-mute" style="font-size:1.05rem">A store that had grown by addition. Every campaign added a template, every market added a
        rule, and the checkout had collected six steps that nobody could justify individually.</p>
        <p class="body-mute" style="margin-top:1.2em">Pages were slow on mobile, where most of the traffic was. Merchandising could not change a
        banner without an engineering ticket, so campaigns shipped late or not at all. Three regions
        ran slightly different code, which meant every fix was made three times.</p>""",
        "pull": "The fastest performance work is deleting the thing that was slow.",
        "approach": """<p class="body-mute" style="font-size:1.05rem">We started with session recordings and the checkout funnel rather than the design. Two of the
        six steps existed for a payment method that accounted for a rounding error of orders.</p>
        <p class="body-mute" style="margin-top:1.2em">From there: one component library covering all three regions, with market differences expressed
        as configuration rather than forked templates. Content moved into a headless CMS so the
        merchandising team owns the page, and the frontend renders statically with product data
        fetched at the edge.</p>
        <div class="out" style="margin-top:1.8em;display:flex;flex-wrap:wrap;gap:8px">
          <span class="chip">Funnel analysis</span><span class="chip">Component audit</span>
          <span class="chip">Headless CMS</span><span class="chip">Edge rendering</span>
        </div>""",
        "shipped_head": "Four things, in this order.",
        "shipped": """<div class="defrow"><dt>A shorter checkout</dt><dd>Six steps to three, with address and payment on one screen and guest checkout promoted rather than buried.</dd></div>
        <div class="defrow"><dt>One component library</dt><dd>Shared across every market, with region differences as configuration. Documented in Storybook and in the design file.</dd></div>
        <div class="defrow"><dt>Editable content</dt><dd>Campaign pages, banners and navigation moved to a headless CMS with a preview environment, removing engineering from the campaign path.</dd></div>
        <div class="defrow"><dt>A performance budget</dt><dd>Enforced in CI. A pull request that pushes the mobile bundle past the agreed limit fails before review.</dd></div>""",
        "measures": """<div><dt>Primary</dt><dd>Checkout completion rate, by device</dd></div>
        <div><dt>Secondary</dt><dd>Mobile Largest Contentful Paint at the 75th percentile</dd></div>
        <div><dt>Operational</dt><dd>Campaign pages published without an engineering ticket</dd></div>
        <div><dt>Guardrail</dt><dd>Error rate and refund requests, watched for regressions</dd></div>""",
    },
    {  # operations
        "crumb": "Operations console",
        "lede": "Four tools, a shared inbox and a spreadsheet replaced by one interface, with roles, "
                "audit trails and reporting designed in from the first week rather than added under pressure.",
        "facts": [("Sector", "Services &amp; operations"), ("Engagement", "Embedded team"),
                  ("Team", "1 design, 3 engineering"), ("Disciplines", "Product design, TypeScript, APIs, DevOps")],
        "caption": "Composition showing the reporting surface of an internal operations console.",
        "problem": """<p class="body-mute" style="font-size:1.05rem">The work got done, but only because a handful of people held the process in their heads. Status
        lived in an inbox, exceptions lived in a spreadsheet, and reporting meant someone reconciling
        both on a Friday.</p>
        <p class="body-mute" style="margin-top:1.2em">Onboarding a new coordinator took weeks. Nobody could answer how long a job actually took,
        because no system recorded the moment it changed hands.</p>""",
        "pull": "Software cannot fix a process nobody has agreed on. First write it down.",
        "approach": """<p class="body-mute" style="font-size:1.05rem">Two weeks of sitting with the team before any design work. We mapped the real process, including
        the informal steps, and found three places where two people were doing the same job.</p>
        <p class="body-mute" style="margin-top:1.2em">The build followed the state machine rather than the screens: every job has a defined status,
        every transition is recorded with who and when, and the interface is a view onto that. Reporting
        stopped being a feature and became a by-product.</p>
        <div class="out" style="margin-top:1.8em;display:flex;flex-wrap:wrap;gap:8px">
          <span class="chip">Process mapping</span><span class="chip">State machine</span>
          <span class="chip">Role-based access</span><span class="chip">Audit trail</span>
        </div>""",
        "shipped_head": "One console, four capabilities.",
        "shipped": """<div class="defrow"><dt>A single queue</dt><dd>Every live job in one view, filtered by role, with the next action obvious without opening the record.</dd></div>
        <div class="defrow"><dt>Roles and permissions</dt><dd>Coordinators, field staff and finance each see what they need and cannot alter what they should not.</dd></div>
        <div class="defrow"><dt>An audit trail</dt><dd>Every status change recorded with actor, timestamp and prior value. Exportable, and used to answer disputes.</dd></div>
        <div class="defrow"><dt>Reporting by default</dt><dd>Cycle time, throughput and exception rate generated from the same data the console runs on, so no reconciliation step exists.</dd></div>""",
        "measures": """<div><dt>Primary</dt><dd>Median time from job created to closed</dd></div>
        <div><dt>Secondary</dt><dd>Jobs handled per coordinator per week</dd></div>
        <div><dt>Operational</dt><dd>Time for a new coordinator to work unsupervised</dd></div>
        <div><dt>Guardrail</dt><dd>Exception and rework rate, tracked against the old baseline</dd></div>""",
    },
    {  # field
        "crumb": "Field reporting",
        "lede": "An offline-capable app for site teams, feeding a workflow that turns a submission into an "
                "approved, filed record without anybody retyping it.",
        "facts": [("Sector", "Field services"), ("Engagement", "Fixed-scope, then retainer"),
                  ("Team", "1 design, 2 engineering"), ("Disciplines", "Mobile, automation, integration")],
        "caption": "Composition showing capture and review screens of an offline-capable field app.",
        "problem": """<p class="body-mute" style="font-size:1.05rem">Site teams filled in paper forms, photographed them, and emailed the photographs to an office
        where someone typed them into a system. Every step added delay and a chance to lose something.</p>
        <p class="body-mute" style="margin-top:1.2em">Connectivity on site was unreliable, which had killed a previous attempt at an app: it assumed a
        network, and the first crew to lose signal stopped trusting it.</p>""",
        "pull": "Offline is not an edge case when the work happens where there is no signal.",
        "approach": """<p class="body-mute" style="font-size:1.05rem">Offline first, in the literal sense: the app writes to a local store, and synchronisation is a
        background concern the user never has to think about or trigger.</p>
        <p class="body-mute" style="margin-top:1.2em">On the office side, submissions route automatically — complete ones file themselves, incomplete
        ones go to a review queue with the specific gap flagged. Photographs are compressed on the
        device, so a day of captures uploads over a weak connection without stalling.</p>
        <div class="out" style="margin-top:1.8em;display:flex;flex-wrap:wrap;gap:8px">
          <span class="chip">Offline sync</span><span class="chip">Conflict handling</span>
          <span class="chip">Automated routing</span><span class="chip">ERP integration</span>
        </div>""",
        "shipped_head": "Capture, sync, route, file.",
        "shipped": """<div class="defrow"><dt>An app that works with no signal</dt><dd>Full capture offline, with a visible sync state and conflict handling for records edited in two places.</dd></div>
        <div class="defrow"><dt>Guided capture</dt><dd>Forms that adapt to job type, validate on the device, and will not let a crew leave site missing a required photograph.</dd></div>
        <div class="defrow"><dt>Automatic routing</dt><dd>Complete submissions file straight to the system of record; incomplete ones raise a review task naming the missing field.</dd></div>
        <div class="defrow"><dt>An integration that holds</dt><dd>A documented contract with the existing system, with retries and a dead-letter queue so nothing is silently lost.</dd></div>""",
        "measures": """<div><dt>Primary</dt><dd>Time from site visit to filed record</dd></div>
        <div><dt>Secondary</dt><dd>Share of submissions needing manual correction</dd></div>
        <div><dt>Operational</dt><dd>Office hours spent on data entry per week</dd></div>
        <div><dt>Guardrail</dt><dd>Sync failure rate and app crash-free sessions</dd></div>""",
    },
]
