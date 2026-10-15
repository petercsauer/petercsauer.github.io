#!/usr/bin/env python3
"""Flag AI-sounding patterns in the visible text of HTML pages.

Usage:
    python3 scripts/check_copy.py              # every top-level *.html
    python3 scripts/check_copy.py wamv.html    # specific files

Only catches word- and phrase-level tells. Rhythm, specificity and
structure still need a human read. See WRITING_GUIDE.md.
Exits 1 if anything is flagged.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

WORDS = """
delve delves delving tapestry testament pivotal crucial vital landscape realm
intricate intricacies meticulous meticulously underscore underscores underscoring
showcase showcases showcasing foster fosters fostering bolster bolstered garner
enhance enhances enhancing elevate elevates empower empowers empowering harness
leverage leverages leveraging leveraged utilize utilizes utilized utilizing
facilitate facilitates facilitated streamline streamlined seamless seamlessly
robust comprehensive multifaceted nuanced notably additionally furthermore
moreover ultimately vibrant enduring transformative groundbreaking innovative
cutting-edge unparalleled invaluable holistic dynamic resonate resonates journey
spearheaded spearheading passionate results-driven synergy cross-functional
end-to-end best-in-class world-class mission-critical state-of-the-art
game-changer game-changing quietly
truly deeply incredibly extremely significantly considerably fundamentally remarkably
""".split()

PHRASES = [
    (r"\bnot (just|only|merely)\b", "not-just / not-only construction"),
    (r"\b(it'?s|it is|isn'?t|is not) (not )?(about|just)\b.*\b(it'?s|but)\b", "'not X, it's Y'"),
    (r"\bhere'?s (the|what|why|how)\b", "fake suspense / signposting"),
    (r"\bwhether you'?re\b", "'whether you're X or Y'"),
    (r"\blet'?s (dive|explore|take a look|break)", "signposting"),
    (r"\b(in conclusion|in summary|to sum up|overall,)", "summary signpost"),
    (r"\b(at its core|when it comes to|in today'?s)\b", "filler opener"),
    (r"\b(serves|stands|functions) as\b", "copula avoidance (use is/was)"),
    (r"\b(plays?|played) an? (key|pivotal|crucial|vital|important) role\b", "inflated significance"),
    (r"\b(a key|pivotal|key) (moment|milestone|turning point)\b", "inflated significance"),
    (r"\b(contributed to|was involved in|helped drive)\b", "vague ownership"),
    (r"\bdeep dive\b|\bnorth star\b|\blean into\b|\bheavy lifting\b", "cliche"),
    (r",\s*(highlighting|underscoring|ensuring|showcasing|fostering|enabling|reflecting|"
     r"emphasizing|leveraging|enhancing|contributing|demonstrating|providing)\b",
     "trailing -ing commentary"),
    (r"\b(The|This|Our) (result|catch|kicker|twist|answer|secret)\?", "question reveal"),
    (r"\bfrom (concept|idea|ideation|design|firmware|hardware) to\b", "false range"),
    (r"\bsparked my passion\b|\bpassion for\b", "moral / passion closer"),
    (r"(certainly!|i hope this helps|as an ai|let me know if|\[your [a-z ]+\]|lorem ipsum)",
     "chatbot artifact / placeholder"),
    (r"(oaicite|contentreference|turn0search|utm_source=chatgpt|\[cite:)", "leaked AI markup"),
    (r"\*\*|(^|\s)##\s", "leftover markdown"),
    (r"[\U0001F300-\U0001FAFF☀-➿]", "emoji"),
]

WORD_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in WORDS) + r")\b", re.I)
PHRASE_RES = [(re.compile(p, re.I), why) for p, why in PHRASES]
EM_DASHES_PER_FILE = 3


def visible_lines(text):
    """Strip tags/scripts/styles but keep line numbers aligned with the source."""
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", blank, text)
    text = re.sub(r"(?s)<!--.*?-->", blank, text)
    # keep alt/title/content attribute values, since visitors and crawlers see them
    text = re.sub(r'(?i)\b(?:alt|title|content|aria-label)="([^"]*)"', lambda m: " " + m.group(1) + " ", text)
    text = re.sub(r"(?s)<[^>]*>", blank, text)
    return html.unescape(text).split("\n")


def check(path):
    hits = []
    dashes = 0
    for n, line in enumerate(visible_lines(path.read_text(encoding="utf-8")), 1):
        if not line.strip():
            continue
        dashes += line.count("—")
        for m in WORD_RE.finditer(line):
            hits.append((n, f"word: {m.group(0)}", line))
        for rx, why in PHRASE_RES:
            if rx.search(line):
                hits.append((n, why, line))
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    for n, why, line in hits:
        print(f"{rel}:{n}: {why}\n    {line.strip()[:140]}")
    if dashes > EM_DASHES_PER_FILE:
        print(f"{rel}: {dashes} em dashes in visible text (aim for <= {EM_DASHES_PER_FILE})")
    return len(hits) + (dashes > EM_DASHES_PER_FILE)


def main(argv):
    files = [Path(a).resolve() for a in argv] or sorted(ROOT.glob("*.html"))
    total = sum(check(f) for f in files)
    print(f"\n{total} flag(s) in {len(files)} file(s). Flags are prompts to reread, not automatic failures.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
