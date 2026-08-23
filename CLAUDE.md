# CLAUDE.md — working on this repo

Static site generator for a CTO start page and controls dashboards. Plain HTML/JS from JSON configs via Python (standard library only). See `README.md` for the full layout.

## Golden rules

1. **Never hand-edit `docs/`** — it is generated output and gets overwritten. Edit `_config/` (content) or `_templates/` (design), then rebuild.
2. **Always rebuild after editing config or templates**, and commit the regenerated `docs/` together with the source change:
   ```bash
   python3 _wiring/start/generate-docs.py
   python3 _wiring/controls/generate-controls-docs.py
   ```
3. **Template placeholder constraint:** generators do *literal* string replacement of `${key}` markers. In `_templates/controls/index.html` the reserved keys are `${data}` and `${date}`; in `landing_page.html` they are `${control_name}`, `${control}`, `${domain}`, `${scoring_model}`, `${icon}`; in `_templates/start/index.html` they are `${domain_name}`, `${domain_description}`, `${apps}`. When writing JavaScript template literals inside these files, never produce one of those exact `${...}` strings by accident (property access like `${domain.name}` is safe; bare `${domain}` is not).
4. **Validate JSON after editing** (`python3 -m json.tool <file> > /dev/null`) — the whole config is embedded into the page verbatim, so a syntax error breaks the page.
5. **Keep `score` consistent with `status`** in controls JSON: red = 1, yellow = 2, green = 3.

## Design language (templates)

Both controls templates share one system: Inter (body/UI) + Space Grotesk (headings/scores), white cards on `#fafbfc`, indigo `#4f46e5` accent, semantic status colors only for status (red `#dc2626`, amber `#d97706`/`#f59e0b`, green `#16a34a`), violet for "In Focus". Keep new UI consistent with these tokens (defined in each template's `:root`).

## Verifying changes

Screenshot generated pages headlessly (Chrome clamps window width to ~500px, so don't trust narrow-viewport screenshots for overflow checks — measure `scrollWidth` instead):

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --hide-scrollbars \
  --window-size=1400,1600 --screenshot=/tmp/out.png \
  "file://$PWD/docs/controls/security-controls/index.html"
```

Also grep generated output for unresolved placeholders: `grep -o '\${[a-z_]*}' docs/**/*.html` should return nothing.

## Project skills

- `/build` — regenerate all docs and sanity-check the output
- `/edit-controls` — guide for updating controls JSON (statuses, evidence, new controls/domains/dashboards)
- `/edit-start-page` — guide for updating the start page's apps.json
- `/publish` — rebuild, verify, commit, and push
