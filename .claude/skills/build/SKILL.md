---
name: build
description: Regenerate all site output in docs/ from _config and _templates, then sanity-check it. Use after any change to config JSON, templates, or build scripts, or when the user asks to build/rebuild/regenerate the site.
---

# Build the site

Run both generators from the repo root:

```bash
python3 _wiring/start/generate-docs.py
python3 _wiring/controls/generate-controls-docs.py
```

Both must print their output paths and exit 0. They are standard-library-only Python; if one fails, the cause is almost always malformed JSON in `_config/` — validate with `python3 -m json.tool <file> > /dev/null` and report the exact parse error.

## Sanity checks after building

1. No unresolved template placeholders in output (must print nothing):
   ```bash
   grep -rho '\${[a-z_]*}' docs --include='*.html' | sort -u
   ```
2. Every control links to an existing landing page — for each dashboard dir, landing page count should match the number of controls in its config.
3. If templates changed, screenshot at least one generated page with headless Chrome and inspect it:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --hide-scrollbars \
     --window-size=1400,1600 --screenshot=<scratchpad>/check.png \
     "file://$PWD/docs/controls/security-controls/index.html"
   ```
   Note: headless Chrome clamps window width to ~500px, so narrow screenshots crop rather than reflow — check mobile layouts by measuring `scrollWidth`, not by eyeballing a 390px screenshot.

Never edit files in `docs/` directly; fix the source in `_config/` or `_templates/` and rebuild.
