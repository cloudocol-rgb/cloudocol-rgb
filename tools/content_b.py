"""Page bodies: expertise, process, about, contact, legal, 404."""

from shell import pagehero, subnav, band, ARROW


def _tags(items):
    return "".join(f'<span class="tag">{t}</span>' for t in items)


# ---------------------------------------------------------------- expertise

def _layer(anchor, num, name, blurb, detail, tags, surface):
    return f"""<section class="section {surface}" id="{anchor}">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">{num}</span><span class="slash">/</span>Layer</div>
      <h2 class="h2" data-reveal style="margin-top:1em">{name}</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.2em">{blurb}</p>
    </div>
    <div data-reveal style="--d:.1s">
      <p class="body-mute" style="font-size:1.02rem">{detail}</p>
      <div style="margin-top:2em;display:flex;flex-wrap:wrap;gap:8px">{_tags(tags)}</div>
    </div>
  </div>
</section>"""


EXPERTISE_BODY = (
    pagehero(
        [("Home", "index.html"), ("Expertise", None)],
        "Expertise", "03",
        "Four layers, one delivery team.",
        "A working knowledge of the whole stack means fewer handoffs, and decisions that still hold "
        "up once they meet production.",
        facts=[("Layers", "Product · Engineering · Intelligence · Infrastructure"),
               ("Bias", "Boring, proven, well-documented"),
               ("Ownership", "Your accounts, your repository")],
    )
    + subnav([("product", "Product"), ("engineering", "Engineering"), ("intelligence", "Intelligence"),
              ("infrastructure", "Infrastructure"), ("choosing", "How we choose")])
    + _layer("product", "01", "Product",
             "Strategy, research and the design system that keeps everything downstream consistent.",
             "The work that decides whether the rest is worth doing. We spend real time here because a "
             "well-shaped brief saves more engineering hours than any framework choice.",
             ["Product strategy", "User research", "Information architecture", "Prototyping",
              "Design systems", "Accessibility (WCAG 2.2 AA)", "Brand identity", "Content design"],
             "panel-paper ruled")
    + _layer("engineering", "02", "Engineering",
             "Frontend, backend, mobile and the APIs that join them.",
             "TypeScript end to end where we can, because one language across the stack removes a whole "
             "category of mistakes. Tests where they earn their keep — around money, permissions and data "
             "integrity rather than everywhere for the sake of a percentage.",
             ["React", "Next.js", "TypeScript", "Node.js", "Python", "React Native", "Flutter",
              "GraphQL", "REST", "PostgreSQL", "Redis", "Playwright"],
             "panel-ink ruled")
    + _layer("intelligence", "03", "Intelligence",
             "AI, automation and the data work that has to come first.",
             "Applied to specific, checkable jobs: extracting fields from documents, routing support "
             "requests, searching an internal corpus. We measure accuracy against a labelled set before "
             "anything reaches a user, and we will say when a rule engine would do the job better.",
             ["LLM integration", "Retrieval-augmented search", "Document processing", "Classification",
              "Workflow automation", "Data pipelines", "Evaluation harnesses", "Analytics"],
             "panel-paper ruled")
    + _layer("infrastructure", "04", "Infrastructure",
             "Cloud, DevOps and the integrations holding it together.",
             "Defined in code, running in your cloud account, with the monitoring in place before launch "
             "rather than after the first incident. Cost is a design constraint we track from the start.",
             ["AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Terraform", "GitHub Actions",
              "Observability", "Incident response", "Cost monitoring"],
             "panel-ink ruled")
    + """
<section class="section panel-paper" id="choosing">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">05</span><span class="slash">/</span>How we choose</div>
        <h2 class="h2" data-reveal>Technology choices, and why.</h2>
      </div>
      <p class="lede" data-reveal style="--d:.08s">The tool list above is a starting position, not a commitment. These are the rules we apply when something new is proposed.</p>
    </div>
    <dl class="deflist" data-reveal>
      <div class="defrow"><dt>Boring beats novel</dt><dd>A technology with five years of production history and clear documentation usually beats the interesting one, unless the interesting one solves a problem you actually have.</dd></div>
      <div class="defrow"><dt>Hiring pool matters</dt><dd>We will not leave you with a stack you cannot hire for. If a choice narrows your future options, we raise it before making it.</dd></div>
      <div class="defrow"><dt>Exit cost is part of the cost</dt><dd>Before adopting a managed service we check what leaving it would take. Convenience that cannot be reversed is a liability with a delay on it.</dd></div>
      <div class="defrow"><dt>Fewer moving parts</dt><dd>Every service added is one more thing to monitor, patch and explain to the next developer. Additions have to earn their place.</dd></div>
      <div class="defrow"><dt>Write the trade-off down</dt><dd>Significant choices get a short decision record in the repository: what we picked, what we rejected, and what would make us revisit it.</dd></div>
    </dl>
  </div>
</section>
"""
    + band("Wondering whether your stack still fits?",
           "A technical review is a normal first engagement, and a short one.",
           "Ask for a review")
)


# ---------------------------------------------------------------- process

def _stage(num, name, blurb, does, gets, length, surface):
    return f"""<section class="section {surface}" id="stage-{num}">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">{num}</span><span class="slash">/</span>Stage</div>
      <h2 class="h2" data-reveal style="margin-top:1em">{name}</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.2em">{blurb}</p>
      <p class="body-mute" data-reveal style="--d:.12s;margin-top:1.6em;font-size:.88rem"><strong style="color:var(--accent)">Typically</strong> {length}</p>
    </div>
    <div data-reveal style="--d:.1s">
      <h3 class="h3" style="margin-bottom:1em">What happens</h3>
      <p class="body-mute">{does}</p>
      <h3 class="h3" style="margin:2.2em 0 1em">What you get</h3>
      <dl class="deflist">{gets}</dl>
    </div>
  </div>
</section>"""


PROCESS_BODY = (
    pagehero(
        [("Home", "index.html"), ("How we work", None)],
        "How we work", "04",
        "Think. Design. Build. Evolve.",
        "Four stages, one continuous engagement. You see working software long before the last one, "
        "and you can stop at the end of any stage.",
        facts=[("Cadence", "Two-week cycles"), ("Visibility", "Shared board, weekly note"),
               ("Handover", "Docs, walkthrough, support window")],
    )
    + subnav([("stage-01", "01 Discover"), ("stage-02", "02 Design"), ("stage-03", "03 Build"),
              ("stage-04", "04 Evolve"), ("working", "Working together")])
    + _stage("01", "Discover",
             "Understand the business, the users and the opportunity — before anyone opens a design tool.",
             "We interview the people who own the outcome and the people who will use the thing. We read "
             "the existing system if there is one, and we look at whatever data already exists rather than "
             "asking for opinions about it. By the end we can state the problem in one paragraph and agree "
             "what would count as solving it.",
             """<div class="defrow"><dt>Problem statement</dt><dd>One page, agreed by everyone who has a say. The reference point for every later argument about scope.</dd></div>
             <div class="defrow"><dt>Technical audit</dt><dd>Where the current system helps, where it blocks, and what has to be carried forward.</dd></div>
             <div class="defrow"><dt>Scope and estimate</dt><dd>Written, with assumptions listed, priced by phase so you can cut without renegotiating everything.</dd></div>""",
             "one to three weeks", "panel-paper ruled")
    + _stage("02", "Design",
             "Turn the agreed problem into something you can click, and test the risky parts while changing them is cheap.",
             "Flows first, then screens. We prototype the two or three interactions that carry the most risk "
             "and put them in front of real users. Visual design follows the structure rather than leading it. "
             "The output is a design system, not a folder of screens, so the build has rules to follow.",
             """<div class="defrow"><dt>Flows and wireframes</dt><dd>The whole journey, including the states people hit when things go wrong.</dd></div>
             <div class="defrow"><dt>Interactive prototype</dt><dd>Clickable, testable, and used in front of users before a line of production code exists.</dd></div>
             <div class="defrow"><dt>Design system</dt><dd>Tokens, components and usage rules in Figma and in code, with contrast and focus states specified.</dd></div>""",
             "three to six weeks", "panel-ink ruled")
    + _stage("03", "Build",
             "Engineer it properly, in short cycles, with something working at the end of each one.",
             "Two-week cycles. Each one ends with a build you can use on a real device, not a screenshot. "
             "Infrastructure, automated tests and documentation are written alongside the features, because "
             "the version that gets them 'later' never gets them. Accessibility and performance are checked "
             "in the pipeline, so regressions fail before review rather than after launch.",
             """<div class="defrow"><dt>Working software, fortnightly</dt><dd>Deployed to a staging environment you can reach, with notes on what changed.</dd></div>
             <div class="defrow"><dt>A pipeline</dt><dd>Automated build, test and deploy. Releasing becomes a routine action rather than an event.</dd></div>
             <div class="defrow"><dt>Documentation as you go</dt><dd>Architecture notes, decision records and a README that a new developer can start from.</dd></div>""",
             "six weeks to several months", "panel-paper ruled")
    + _stage("04", "Evolve",
             "Watch how it behaves with real users and keep improving it — performance, cost and the next set of features.",
             "Launch is the point at which you start learning. We instrument the things we agreed to measure "
             "in Discover, review them monthly, and use them to decide what happens next. Cloud spend gets the "
             "same attention as page speed, because both compound quietly.",
             """<div class="defrow"><dt>Instrumentation</dt><dd>The agreed metrics, on a dashboard you own, live from launch day.</dd></div>
             <div class="defrow"><dt>Monthly review</dt><dd>What moved, what did not, and a recommendation for the next cycle — including doing nothing.</dd></div>
             <div class="defrow"><dt>Support you can define</dt><dd>Response times agreed in advance, and an allocation that carries rather than expires.</dd></div>""",
             "ongoing, month to month", "panel-ink ruled")
    + """
<section class="section panel-paper" id="working">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">05</span><span class="slash">/</span>Working together</div>
        <h2 class="h2" data-reveal>How it runs day to day.</h2>
      </div>
      <p class="lede" data-reveal style="--d:.08s">Predictable rhythm, minimal ceremony. You should never have to ask where a project stands.</p>
    </div>
    <div class="cols cols--3">
      <div class="block" data-reveal><span class="bnum">Rhythm</span><h3>One call a week</h3><p>Thirty minutes, same slot, with a written note afterwards. Anything urgent happens in a shared channel rather than waiting for the call.</p></div>
      <div class="block" data-reveal style="--d:.08s"><span class="bnum">Visibility</span><h3>One board</h3><p>The same board we work from, open to you. No separate client-facing status document that quietly diverges from reality.</p></div>
      <div class="block" data-reveal style="--d:.16s"><span class="bnum">Decisions</span><h3>Written down</h3><p>Significant calls get a short record in the repository. Six months on, the reasoning is still there for whoever needs it.</p></div>
    </div>

    <div style="margin-top:clamp(48px,6vw,84px)">
      <h3 class="h3" data-reveal style="margin-bottom:1.4em">What we need from you</h3>
      <dl class="deflist" data-reveal>
        <div class="defrow"><dt>One decision-maker</dt><dd>Someone who can settle a disagreement in a day. Design by committee is the most expensive way to build software.</dd></div>
        <div class="defrow"><dt>Access to real users</dt><dd>A few hours across the project. Testing with the people who will actually use it changes outcomes more than any other input.</dd></div>
        <div class="defrow"><dt>Honest constraints</dt><dd>The deadline that is real, the budget that is fixed, the system we are not allowed to touch. Early is cheap; late is not.</dd></div>
      </dl>
    </div>
  </div>
</section>
"""
    + band("Ready to start at stage one?",
           "Discovery is a small, fixed commitment. It ends with a written scope you can take anywhere.")
)


# ---------------------------------------------------------------- about

ABOUT_BODY = (
    pagehero(
        [("Home", "index.html"), ("About", None)],
        "About", "05",
        "We build digital experiences that move businesses forward.",
        "Cloudocol Technologies is a design and engineering practice. We work with founders and in-house "
        "teams who need one partner across the whole problem — the interface, the software behind it, and "
        "the infrastructure it runs on.",
        facts=[("Founded", "Building since 2021"), ("Shape", "Small, senior, multidisciplinary"),
               ("Entity", "Cloudocol Technologies Pvt. Ltd.")],
    )
    + subnav([("story", "The practice"), ("philosophy", "Philosophy"), ("principles", "Principles"),
              ("setup", "How we are set up")])
    + """
<section class="section panel-paper ruled" id="story">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">01</span><span class="slash">/</span>The practice</div>
    </div>
    <div>
      <p data-reveal style="font-size:clamp(1.1rem,1.6vw,1.4rem);font-weight:300;letter-spacing:-.022em;line-height:1.5;max-width:44ch">
        Most digital work fails in the gaps — between the designer and the developer, the developer and
        the person running the servers, and all three and the business paying for it.
      </p>
      <p class="body-mute" data-reveal style="--d:.08s;margin-top:1.6em">
        Cloudocol exists to remove those gaps. Three disciplines, deliberately overlapping: designers who
        understand what is expensive to build, engineers who care how a thing feels to use, and a strategy
        layer keeping both pointed at the commercial outcome.
      </p>
      <p class="body-mute" data-reveal style="--d:.12s">
        We stay small on purpose. The people you meet are the people who do the work, and there is no
        layer of account management translating between you and them.
      </p>
    </div>
  </div>
</section>

<section class="section panel-ink ruled" id="philosophy">
  <div class="wrap about-grid">
    <div class="about-copy">
      <div class="label" style="margin-bottom:clamp(20px,2.4vw,34px)"><span class="num">02</span><span class="slash">/</span>Philosophy</div>
      <h2 class="h2" data-reveal>Three disciplines that only work together.</h2>
      <p class="lede" data-reveal style="--d:.08s;margin-top:1.4em">
        Design without engineering produces things that cannot be built. Engineering without design
        produces things nobody wants to use. Either without strategy produces work that is excellent
        and pointless.
      </p>
    </div>
    <figure class="about-fig" data-fig style="margin:0">
      <svg class="vn" viewBox="0 0 500 420" role="img" aria-label="Design, technology and strategy overlapping at Cloudocol">
        <circle cx="250" cy="145" r="105"/>
        <circle cx="182" cy="262" r="105"/>
        <circle cx="318" cy="262" r="105"/>
        <text class="lb" x="250" y="58" text-anchor="middle" fill="#E8E6DF">Design</text>
        <text class="lb" x="72" y="362" text-anchor="middle" fill="#E8E6DF">Technology</text>
        <text class="lb" x="428" y="362" text-anchor="middle" fill="#E8E6DF">Strategy</text>
        <text class="ctr" x="250" y="222" text-anchor="middle" fill="#DFA23C">CLOUDOCOL</text>
      </svg>
    </figure>
  </div>
</section>

<section class="section panel-paper" id="principles">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">03</span><span class="slash">/</span>Principles</div>
        <h2 class="h2" data-reveal>Six things we hold to.</h2>
      </div>
      <p class="lede" data-reveal style="--d:.08s">Not values on a wall. These are the arguments we are willing to have with a client.</p>
    </div>
    <dl class="deflist" data-reveal>
      <div class="defrow"><dt>Design leads the brief</dt><dd>Design decides how work is understood, so it shapes what gets built rather than dressing the result afterwards.</dd></div>
      <div class="defrow"><dt>Every feature needs a reason</dt><dd>Tied to a commercial outcome. If we cannot find one, we say so before you pay to build it.</dd></div>
      <div class="defrow"><dt>Code is read more than written</dt><dd>Clear architecture, honest tests and documentation. Your next developer should not need an archaeologist.</dd></div>
      <div class="defrow"><dt>Scale for the next stage</dt><dd>Not for a hypothetical one. Systems sized for where you are going, with room to grow rather than architecture for a company you are not.</dd></div>
      <div class="defrow"><dt>Test with real people</dt><dd>Including the ones who never asked for new software. They find the problems a demo never will.</dd></div>
      <div class="defrow"><dt>Optimise for the second project</dt><dd>Most of our work is with clients we have already shipped for. That changes how we scope the first one.</dd></div>
    </dl>
  </div>
</section>

<section class="section panel-ink" id="setup">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <div class="label"><span class="num">04</span><span class="slash">/</span>How we are set up</div>
        <h2 class="h2" data-reveal>Small team, senior work.</h2>
      </div>
      <p class="lede" data-reveal style="--d:.08s">Roughly how an engagement is staffed, and what that means for you.</p>
    </div>
    <div class="cols cols--3">
      <div class="block" data-reveal><span class="bnum">Team</span><h3>Four to six people</h3><p>A lead, designers and engineers, sized to the work. No junior staffed onto a project to make the margin work.</p></div>
      <div class="block" data-reveal style="--d:.08s"><span class="bnum">Access</span><h3>Direct</h3><p>You talk to the people doing the work. Questions get answered by whoever knows the answer, in hours rather than through a chain.</p></div>
      <div class="block" data-reveal style="--d:.16s"><span class="bnum">Ownership</span><h3>Yours, entirely</h3><p>Code, designs, infrastructure and accounts are in your name from the start. Nothing is held as leverage to keep you.</p></div>
    </div>
  </div>
</section>
"""
    + band("Want to know if we are a fit?",
           "One conversation is usually enough for both of us to tell.")
)


# ---------------------------------------------------------------- contact

CONTACT_BODY = (
    pagehero(
        [("Home", "index.html"), ("Contact", None)],
        "Contact", "06",
        "Have an idea worth building?",
        "Tell us what you are trying to build. We will come back with an honest view of scope, cost, "
        "and whether we are the right team for it.",
        facts=[("Response", "Within two working days"), ("First call", "30 minutes, no charge"),
               ("NDA", "Happy to sign yours")],
    )
    + """
<section class="section panel-ink">
  <div class="wrap split split--plain">
    <div>
      <h2 class="h3" data-reveal style="margin-bottom:1.4em">Start a project</h2>
      <p class="body-mute" data-reveal style="font-size:.94rem">The more you can tell us about the problem, the more useful our first reply will be. Rough is fine — we are not expecting a specification.</p>

      <div style="margin-top:clamp(32px,4vw,52px)">
        <h3 class="h3" data-reveal style="font-size:1.1rem;margin-bottom:1.2em">What happens next</h3>
        <dl class="deflist" data-reveal>
          <div class="defrow"><dt>We read it</dt><dd>A person, not an autoresponder. If it is not for us, we will say so and suggest who might be a better fit.</dd></div>
          <div class="defrow"><dt>A short call</dt><dd>Thirty minutes to understand the problem properly. No deck, no pitch.</dd></div>
          <div class="defrow"><dt>Something in writing</dt><dd>Scope, approach, cost and assumptions. Yours to take elsewhere if you want a comparison.</dd></div>
        </dl>
      </div>

      <!-- Replace these placeholders with real contact details before launch -->
      <div style="margin-top:clamp(32px,4vw,52px)">
        <h3 class="h3" data-reveal style="font-size:1.1rem;margin-bottom:1.2em">Or reach us directly</h3>
        <dl class="deflist" data-reveal>
          <div class="defrow"><dt>Email</dt><dd><a class="link-a" href="mailto:hello@cloudocol.example">hello@cloudocol.example</a></dd></div>
          <div class="defrow"><dt>Phone</dt><dd>To be added</dd></div>
          <div class="defrow"><dt>Social</dt><dd>LinkedIn, Instagram and GitHub — links to be added</dd></div>
        </dl>
      </div>
    </div>

    <div>
      <form class="form" id="projectForm" novalidate data-reveal style="--d:.08s">
        <div class="field-row">
          <div class="field">
            <label for="name">Your name <span class="req">*</span></label>
            <input id="name" name="name" type="text" autocomplete="name" required />
            <span class="err" role="alert"></span>
          </div>
          <div class="field">
            <label for="email">Email <span class="req">*</span></label>
            <input id="email" name="email" type="email" autocomplete="email" required />
            <span class="err" role="alert"></span>
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="company">Company</label>
            <input id="company" name="company" type="text" autocomplete="organization" />
            <span class="err" role="alert"></span>
          </div>
          <div class="field">
            <label for="budget">Indicative budget</label>
            <select id="budget" name="budget">
              <option value="">Prefer not to say</option>
              <option>Under $10k</option>
              <option>$10k – $25k</option>
              <option>$25k – $75k</option>
              <option>$75k+</option>
              <option>Ongoing retainer</option>
            </select>
            <span class="err" role="alert"></span>
          </div>
        </div>

        <fieldset class="field" style="border:0;padding:0;margin:0">
          <legend style="font-size:.74rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--on-ink-mute);padding:0;margin-bottom:.8em">What do you need</legend>
          <div class="choice">
            <input type="checkbox" id="n1" name="need" value="design" /><label for="n1">Design</label>
            <input type="checkbox" id="n2" name="need" value="web" /><label for="n2">Web build</label>
            <input type="checkbox" id="n3" name="need" value="mobile" /><label for="n3">Mobile app</label>
            <input type="checkbox" id="n4" name="need" value="software" /><label for="n4">Custom software</label>
            <input type="checkbox" id="n5" name="need" value="cloud" /><label for="n5">Cloud &amp; DevOps</label>
            <input type="checkbox" id="n6" name="need" value="ai" /><label for="n6">AI &amp; automation</label>
            <input type="checkbox" id="n7" name="need" value="unsure" /><label for="n7">Not sure yet</label>
          </div>
        </fieldset>

        <div class="field">
          <label for="message">About the project <span class="req">*</span></label>
          <textarea id="message" name="message" required placeholder="What are you trying to build, who is it for, and what is driving the timing?"></textarea>
          <span class="err" role="alert"></span>
        </div>

        <div style="display:flex;flex-wrap:wrap;align-items:center;gap:20px;margin-top:.6em">
          <button class="btn btn--solid magnetic" type="submit"><span class="btn-in"><span class="dot"></span>Send enquiry</span></button>
          <p class="form-note" style="margin:0">We reply within two working days. Your details are used to answer your enquiry and nothing else.</p>
        </div>
      </form>

      <div class="form-ok" id="formOk" role="status">
        <h3>Validation passed — but nothing was sent.</h3>
        <p>This form has no backend yet. Connect it to your own endpoint, Formspree or a Netlify form before launch; the README explains how in three lines. Until then, email <a class="link-a" href="mailto:hello@cloudocol.example">hello@cloudocol.example</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight panel-paper">
  <div class="wrap split">
    <div>
      <div class="label"><span class="num">02</span><span class="slash">/</span>Questions</div>
      <h2 class="h2" data-reveal style="margin-top:1em;font-size:clamp(1.6rem,3vw,2.4rem)">Common first questions.</h2>
    </div>
    <div data-reveal style="--d:.08s">
      <details class="faq">
        <summary>I only have a rough idea. Too early?<span class="pm"></span></summary>
        <div class="faq-body"><p>No. Early is the cheapest point to change direction. A first call about a rough idea is often more useful than one about a finished specification.</p></div>
      </details>
      <details class="faq">
        <summary>Do you work with clients in other countries?<span class="pm"></span></summary>
        <div class="faq-body"><p>Yes. Most work is remote, with overlapping hours agreed at the start so there is a reliable window for questions.</p></div>
      </details>
      <details class="faq">
        <summary>Can you take over an existing project?<span class="pm"></span></summary>
        <div class="faq-body"><p>Often. We start with a short technical review so both sides know what is actually there before committing to anything.</p></div>
      </details>
      <details class="faq">
        <summary>What if we just need advice?<span class="pm"></span></summary>
        <div class="faq-body"><p>That is a legitimate engagement. A technical review or platform assessment is small, fixed-scope, and ends with a document you can act on with or without us.</p></div>
      </details>
    </div>
  </div>
</section>
"""
)


# ---------------------------------------------------------------- legal

LEGAL_NOTE = ('<p class="note-band" data-reveal style="margin-bottom:clamp(32px,4vw,52px)">'
              '<strong>Template, not legal advice.</strong> This page is a starting structure. '
              'Have it reviewed against the law that applies to Cloudocol Technologies Pvt. Ltd. '
              'and the jurisdictions you operate in before publishing. Replace every bracketed '
              'placeholder.</p>')


def _legal(title, sections):
    toc = "".join(f'<a href="#{anchor}">{heading}</a>' for anchor, heading, _ in sections)
    body = "".join(
        f'<h2 id="{anchor}">{heading}</h2>{content}' for anchor, heading, content in sections
    )
    return f"""<section class="section panel-paper">
  <div class="wrap split">
    <div>
      <nav class="prose-toc" aria-label="On this page">
        <div class="label" style="margin-bottom:1.4em">On this page</div>
        {toc}
      </nav>
    </div>
    <div>
      {LEGAL_NOTE}
      <div class="prose">{body}</div>
      <p style="margin-top:3em;font-size:.82rem;color:var(--on-paper-mute)">Last updated: [date]. Questions about this policy: <a class="link-a" href="mailto:hello@cloudocol.example">hello@cloudocol.example</a></p>
    </div>
  </div>
</section>"""


PRIVACY_BODY = (
    pagehero(
        [("Home", "index.html"), ("Privacy", None)],
        "Legal", "—", "Privacy policy",
        "What we collect when you use this website or contact us, why we collect it, and what you can ask us to do with it.",
    )
    + _legal("Privacy", [
        ("collect", "What we collect", """
        <p>Two kinds of information:</p>
        <ul>
          <li><strong>What you send us.</strong> If you use the contact form or email us, we hold your name, email address, company and whatever you write in the message.</li>
          <li><strong>Basic usage data.</strong> [If you add analytics, describe it here — the tool, what it records, and whether it uses cookies. If you add none, say so plainly: this site sets no cookies and runs no analytics.]</li>
        </ul>"""),
        ("why", "Why we hold it", """
        <p>To answer your enquiry, to deliver work you have engaged us for, and to meet our record-keeping obligations as a registered company. We do not sell personal data, and we do not share it for advertising.</p>"""),
        ("legal-basis", "Legal basis", """
        <p>[Set out the basis that applies in your jurisdiction — for example, legitimate interest in responding to a business enquiry, or consent where you have asked for it. If you handle data from the EU or UK, this section needs specific attention.]</p>"""),
        ("retention", "How long we keep it", """
        <p>Enquiries that do not become projects: [period]. Project records: for the duration of the engagement and [period] afterwards, or longer where law requires it.</p>"""),
        ("sharing", "Who else sees it", """
        <p>Service providers who help us operate — [email provider], [hosting provider], [form handler]. Each is bound by its own agreement with us. We name them here so you can check their terms too.</p>"""),
        ("rights", "Your rights", """
        <p>You can ask us for a copy of what we hold about you, ask us to correct it, or ask us to delete it. Write to <a href="mailto:hello@cloudocol.example">hello@cloudocol.example</a> and we will respond within [period].</p>"""),
        ("security", "Security", """
        <p>Data is held in access-controlled systems, transmitted over encrypted connections, and available only to people who need it for the work. No system is perfectly secure; if something goes wrong that affects you, we will tell you.</p>"""),
        ("changes", "Changes", """
        <p>If this policy changes materially we will update the date below and, where the change affects you directly, tell you.</p>"""),
    ])
)


TERMS_BODY = (
    pagehero(
        [("Home", "index.html"), ("Terms", None)],
        "Legal", "—", "Terms of use",
        "The terms on which this website is provided. Project work is governed by a separate signed agreement.",
    )
    + _legal("Terms", [
        ("site", "About this site", """
        <p>This website is operated by Cloudocol Technologies Pvt. Ltd. ("Cloudocol", "we"). By using it you accept these terms.</p>"""),
        ("content", "Content on this site", """
        <p>Descriptions of services, process and sample work are provided for information. They do not constitute an offer, a quotation, or a commitment to deliver on particular terms. Work published as sample or illustrative is exactly that, and does not represent a named client engagement.</p>"""),
        ("ip", "Intellectual property", """
        <p>The design, code, text and graphics of this site are owned by Cloudocol unless stated otherwise. You may view and share pages; you may not copy the site or substantial parts of it for your own commercial use without written permission.</p>"""),
        ("engagements", "Client engagements", """
        <p>Any project we undertake is governed by a separate written agreement covering scope, fees, timelines, intellectual property and liability. Nothing on this site varies that agreement. Where the two conflict, the signed agreement takes precedence.</p>"""),
        ("links", "Links to other sites", """
        <p>We link to third-party sites where useful. We do not control them and are not responsible for their content or practices.</p>"""),
        ("liability", "Liability", """
        <p>[This section needs review by a qualified adviser in your jurisdiction. It typically sets out that the site is provided as-is, and limits liability for indirect loss arising from its use, to the extent the law allows.]</p>"""),
        ("law", "Governing law", """
        <p>These terms are governed by the laws of [jurisdiction], and disputes are subject to the exclusive jurisdiction of its courts.</p>"""),
        ("contact-legal", "Contact", """
        <p>Questions about these terms: <a href="mailto:hello@cloudocol.example">hello@cloudocol.example</a>.</p>"""),
    ])
)


# ---------------------------------------------------------------- 404

NOTFOUND_BODY = f"""<section class="pagehero ruled" style="min-height:72svh;display:flex;align-items:center">
  <div class="wrap">
    <div class="label" style="margin-bottom:clamp(18px,2vw,28px)"><span class="num">404</span><span class="slash">/</span>Page not found</div>
    <h1 class="display" data-reveal style="max-width:16ch">This page doesn't exist.</h1>
    <p class="lede" data-reveal style="--d:.08s;margin-top:1.4em">The link may be out of date, or the address mistyped. Everything below is still where it should be.</p>

    <div class="err-links" data-reveal style="--d:.14s">
      <a href="services.html"><strong>Services</strong><span>Design, development and technology, in detail.</span></a>
      <a href="work.html"><strong>Work</strong><span>Sample engagements and how they were run.</span></a>
      <a href="contact.html"><strong>Contact</strong><span>Start a project, or just ask a question.</span></a>
    </div>

    <div style="margin-top:clamp(32px,4vw,48px)">
      <a class="btn btn--ghost magnetic" href="index.html" data-reveal style="--d:.2s"><span class="btn-in">Back to the homepage {ARROW}</span></a>
    </div>
  </div>
</section>"""
