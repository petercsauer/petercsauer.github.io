# Writing guide: no AI-sounding copy

This applies to every word a visitor can read on this site:

- page text
- project write-ups
- the resume (`resume-modern.html` and its PDFs)
- `<title>`, meta descriptions and `alt` text
- button and link labels

Readers who use ChatGPT, Claude and similar tools regularly can spot AI text almost every time. In one study a panel of five such readers misidentified only 1 of 300 articles (Russell et al., ACL 2025). Hiring managers say they skip applications that read as AI. So treat "sounds like AI" as a defect, the same as a typo or a broken link.

Readers don't react to any single word. They react to **clusters**: one em dash is fine, but an em dash plus a triad plus "seamless" plus a punchy closing line is AI. Fixing this means changing structure and content, not swapping synonyms.

---

## The core rule

> **Every sentence must contain something only Peter could have written.**

Before keeping a sentence, ask: *could this appear unchanged on another engineer's portfolio?* If yes, it tells the reader nothing about Peter. Rewrite it around one of these:

- a **number** (5 → 30 FPS, 50 vessels, 6 months → 2)
- a **named thing** (PIC32MX250F128B, Triton, WAM-V 16', Port Hueneme)
- a **decision and its reason** ("dropped the electromagnet for neodymium magnets because…")
- **something that went wrong** ("the electromagnet failed three days before the demo")
- **what Peter personally did**, as opposed to the team

If none of these exist for a claim, cut the claim. **Never invent numbers, names or anecdotes to satisfy this rule.** The sources for facts are the resume, the project detail pages, and Peter himself. When a fact is missing, leave a visible `TODO(peter): …` comment in the source and ask.

---

## How to write or revise copy

1. **Get the facts down first.** List what happened: what was built, with what, for whom, what changed, and what broke. Write prose only after that.
2. **Write it the way Peter would say it to another engineer.** Use plain verbs: built, wrote, cut, shipped, fixed, ran, tested, designed. If you wouldn't say a sentence out loud, rewrite it.
3. **Start with the fact.** Delete any opening sentence that only sets the scene ("In today's world of robotics…"), and delete any closing sentence that only restates or moralizes.
4. **Run the pattern pass** (sections A–F below), or run the checker:
   ```sh
   python3 scripts/check_copy.py            # all top-level *.html
   python3 scripts/check_copy.py wamv.html  # one file
   ```
   The script catches word- and phrase-level tells. It can't judge rhythm, specificity or structure, so you still have to read the text.
5. **Do a rhythm pass.** Look at one paragraph at a time. If every sentence is 15–25 words, combine two and shorten one. Paragraphs should vary in length too. Let the variation come from the content; don't add fragments for effect.
6. **Do a read-aloud pass.** Anything that sounds like a brochure, a press release or a LinkedIn post gets rewritten.

---

## A. Content patterns (the most important group)

| Pattern | Looks like | Do instead |
|---|---|---|
| **Impact without a number** | "significantly improved performance", "reduced downtime considerably" | Give the number, or cut the claim. |
| **Inflated significance** | "a pivotal role", "a testament to", "marking a key moment", "shaping the future of", "Engineering the Future of Robotics" | State what happened. Let the reader judge how much it matters. |
| **Abstraction in place of a picture** | "intelligent autonomous systems for challenging real-world environments" | Say what and where: "boats doing seafloor surveys off Alaska." |
| **Responsibility lists** | "Responsible for firmware, hardware and documentation" | Say what you did and what came of it. |
| **Vague ownership** | "contributed to", "was involved in", "helped drive", "played a key role" | "I built…" / "I wrote…". If it was a team effort, say which part was yours. |
| **Polished, risk-free stories** | everything worked, every choice was right | Include one real failure or tradeoff. The wrench page's broken-electromagnet story is the model to follow. |
| **Vague attribution** | "recognized by industry leaders", "experts agree" | Name who, or cut it. |
| **Promotional tone** | "cutting-edge", "state-of-the-art", "world-class", "innovative solutions" | Describe the thing. Specific detail is what impresses. |
| **Mirroring a job post** | skills listed in the same order and wording as an ad | Use Peter's own order, and lead with his strongest work. |
| **Same-y projects** | every card has the identical shape and length | Give each project the space its substance deserves. A big project can run long and a small one can be two lines. |

## B. Sentence patterns

| Pattern | Example | Fix |
|---|---|---|
| **"Not X, but Y" / "not just X"** | "I don't just write code — I build systems." "It's not about speed, it's about reliability." | Say Y. No one claimed X. |
| **"Not only… but also"** | "not only designed the hull but also wrote firmware" | "Designed the hull and wrote the firmware." |
| **Rule of three** | "scalable, reliable, and maintainable"; "design, build, and deploy" | Use as many items as actually exist. Two or four is fine. Don't stack triads. |
| **Trailing "-ing" commentary** | "Built the GUI, enabling intuitive control and monitoring." "…ensuring robust operation." | End the sentence on the fact. If the effect matters, give it its own sentence with evidence. |
| **Avoiding "is"/"has"** | "serves as", "stands as", "functions as", "boasts", "features" | "is", "has", "was". |
| **Colon or question reveal** | "The result? A 6× speedup." "The catch: …" | "That took it from 5 to 30 FPS." |
| **Fake suspense** | "Here's the thing", "But here's the kicker" | Delete it. |
| **"Whether you're X or Y"** | "Whether you're a recruiter or an engineer…" | Delete it. Write for one reader. |
| **False range** | "from firmware to the cloud", "from concept to deployment" | List the real items, or name only the one that matters. |
| **Synonym cycling** | the GUI / the interface / the dashboard / the portal, all for one thing | Pick one name and repeat it. |
| **Strings of short fragments** | "Fast. Reliable. Battle-tested." | Write one sentence with a verb. |
| **Restating a sentence as its own summary** | "…which made the system far more reliable." | Delete it, or replace it with the measurement. |
| **Hedging plus significance** | "While details are limited, this highlights…" | Either know it and say it, or leave it out. |

## C. Rhythm and structure

- **Uniform sentence length.** This is the "steady, even cadence" readers notice. Mix a 6-word sentence with a 30-word one, driven by the content.
- **Every paragraph built the same way** (claim, elaboration, punchy closing line). Break the template, and cut most of the closing lines.
- **Mirrored openers.** Bullets that all start with "Designed…", "Developed…", "Implemented…", all the same length, all ending in a benefit. Vary them, and let some bullets just state a fact.
- **Signposting.** "Let's dive in", "In this section", "Overall", "In summary", "In conclusion", "At its core", "When it comes to". Delete them.
- **A moral or summary at the end.** "This experience sparked my passion for…", "…to deliver mission-critical capabilities." End on the last real fact.
- **Hook intros.** "Imagine a robot that…", rhetorical openers. Start with the subject.

## D. Words

These words aren't banned, but each one needs a reason. Several from this list together mean the passage needs rewriting.

**LLM-overused (research-backed):** delve, tapestry, testament, pivotal, crucial, vital, key (as an adjective), landscape, realm, intricate, meticulous(ly), underscore, highlight(ing), showcase, foster, bolster, garner, enhance, elevate, empower, harness, leverage, utilize, facilitate, streamline, seamless(ly), robust, comprehensive, multifaceted, nuanced, notable/notably, additionally, furthermore, moreover, ultimately, vibrant, enduring, transformative, groundbreaking, innovative, cutting-edge, unparalleled, invaluable, holistic, dynamic, align with, resonate, navigate (used figuratively), journey (used figuratively), quietly, steady, matters, deep dive, game-changer, north star, lean into, heavy lifting.

**Resume and portfolio buzzwords:** spearheaded, passionate, results-driven, drove impact, synergy, cross-functional, end-to-end, best-in-class, world-class, mission-critical, state-of-the-art, thought leader, proven track record, detail-oriented, team player, wear many hats.

**Plain replacements:**

| Instead of | Write |
|---|---|
| utilize / leverage | use |
| facilitate / enable | let, allow, or just the verb |
| spearheaded | led, started, built |
| robust | name the failure it survives (e.g. "ran N days unattended", with the real N) |
| seamless | delete, or say what is actually smooth |
| comprehensive documentation | what the docs were and what they changed ("build docs that helped cut build time from 6 months to 2") |
| in order to / owing to the fact that | to / because |

**Intensifiers to cut:** very, truly, deeply, highly, incredibly, extremely, significantly, considerably, fundamentally, remarkably.

## E. Formatting

- **Em dashes (—):** no more than about one per page section. Use a period, comma, colon or parentheses.
- **Bold-label bullets** ("**Firmware Engineering**: Worked to ensure…"). One or two can be fine, but a whole list of them reads as AI. Write a sentence or a plain bullet instead.
- **Bold scattered through paragraphs.** Bold nothing in body copy, or at most one term per section.
- **Title Case Headings** ("Engineering The Future Of Robotics"). Use sentence case, and use plain labels ("Projects", "Experience").
- **"X and Y" section titles** ("Awards and Recognition", "Challenges and Solutions"). Use one plain word where possible.
- **Emoji** as bullets or heading decoration: none.
- **Arrows (→)** in link text are fine as a UI element, one per link. Never use them inside prose.
- **Symmetrical bullet lists** where every item has the same length and shape. Vary them.

## F. Chatbot artifacts (always a bug)

- "Certainly!", "I hope this helps", "Here is a…", "Let me know", "As an AI…"
- Placeholders: `[Your Name]`, `XX`, `Lorem ipsum`, `2025-XX-XX`
- Leaked markup: `oaicite`, `contentReference`, `turn0search`, `utm_source=chatgpt.com`, `[cite: 1]`, leftover `**` or `##` in HTML
- Credit lines nobody needs, such as "with assistance from Claude" in project copy (unless Peter wants it there on purpose)

---

## Before and after (from this site)

**WAM-V firmware (current site)**
> Firmware Engineering: Worked meticulously to ensure robust and reliable on-board systems for real-time operations.

This has a bold label, the words "meticulously" and "robust", a near-redundant pair ("robust and reliable"), no object and no result. Rewritten from facts in the resume:
> Wrote the embedded firmware for propulsion, steering, cameras, and comms (GPS, Iridium, Starlink, cellular, mesh radio) that let the boats run without a pilot.

**WAM-V GUI**
> Spearheaded the creation of the control GUI which enabled intuitive control and monitoring of our vehicles.

> Built the control GUI operators used to drive and monitor the boats. `TODO(peter): what made it better than what came before?`

**Hero tagline**
> Senior Software Engineer · Roboticist · Developer
> Building distributed systems and autonomous platforms for defense and maritime applications

> I build autonomy software for fleets of uncrewed boats. At Applied Intuition that means comms and perception for 50 vessels on the water; before that, firmware for the WAM-V.

(The first draft of this rewrite was "from the firmware on each boat to the comms between 50 of them", which is a false range. Check rewrites against this guide too.)

**About stats**
> 20+ Projects Completed · CO Based in Boulder

> 50 vessels run autonomously · 5 → 30 FPS perception · 6 deployment sites

**Closing line on i²robotics**
> This experience sparked my passion for robotics and engineering that continues today.

> *(deleted; the card ends on the World Championship awards)*

**Cyclone**
> …helping reduce machine downtime considerably.

> Raised $50K in startup competitions and shipped a working MVP.

---

## Don't overcorrect

- Don't add typos, slang or fake casualness to seem human. The aim is specific and plain, not sloppy.
- Don't strip every comma list or every long word. A real list of four protocols is fine.
- Don't swap a flagged word for a fancier synonym ("delve" → "dig deep"). Rewrite the sentence around a fact.
- The site's existing voice is first person, direct and technical. Keep it.

---

## Sources

- Wikipedia, "Signs of AI writing" (WikiProject AI Cleanup): https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Kobak et al., "Delving into LLM-assisted writing in biomedical publications through excess vocabulary": https://arxiv.org/abs/2406.07016
- Juzek & Ward, "Why Does ChatGPT 'Delve' So Much?" (COLING 2025): https://arxiv.org/abs/2412.11385
- Russell, Karpinska & Iyyer, "People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text" (ACL 2025): https://aclanthology.org/2025.acl-long.267/
- Hollis Robbins, "How to Tell if Something is AI Written": https://hollisrobbinsanecdotal.substack.com/p/how-to-tell-if-something-is-ai-written
- tropes.fyi: https://tropes.fyi/
- Hacker News, "Please stop sending AI-generated job applications": https://news.ycombinator.com/item?id=37761045
- Paul Graham, "Write Like You Talk": https://paulgraham.com/talk.html
- Orwell, "Politics and the English Language": https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/
- Strunk, *The Elements of Style*, rules 11–13: https://www.gutenberg.org/files/37134/37134-h/37134-h.htm
- Gopen & Swan, "The Science of Scientific Writing": https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf
