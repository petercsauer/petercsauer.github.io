# petercsauer.github.io

Peter Sauer's personal portfolio. Static HTML served by GitHub Pages (`.nojekyll`, no build step). `index.html` is self-contained (inline CSS/JS); the project detail pages (`wamv.html`, `wrench.html`, …) still use the old Bootstrap template in `css/` and `js/`.

## Writing copy

Any visible text you write or edit (page copy, resume, titles, meta descriptions, alt text) must follow the writing guide:

@WRITING_GUIDE.md

Before finishing a copy change, run `python3 scripts/check_copy.py <changed files>` and reread every flag. Never invent facts, numbers or anecdotes; take them from the resume or detail pages, or leave a `TODO(peter): …` and ask.
