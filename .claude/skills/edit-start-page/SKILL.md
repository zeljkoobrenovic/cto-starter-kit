---
name: edit-start-page
description: Update the start page — add or edit tools, apps, steps, groups, or tabs in _config/start/apps.json, or change its title/description. Use for any start page content change.
---

# Edit the start page

Content lives in `_config/start/apps.json`. Full structure reference: `_config/start/README.md`. Never edit `docs/` — it is generated.

Two tab shapes exist:
- **Step tabs** ("First 90 Days", "First Year", "Long Term"): `steps` → groups → steps, each step with a `name`, a one-sentence `description` of why it matters, and optional supporting `tools` (name / link / icon).
- **App tabs** ("Tools", "Playbooks"): `apps` → groups → apps, each with `name`, `link`, `icon`, `description`, optional `source`.

## When adding an entry

- Match the existing tone: descriptions are single sentences stating why the thing matters, not marketing copy.
- Icons: reuse an existing file from `_config/start/icons/` when one fits; new icons go in that folder and are referenced as `icons/<file>.png`. Absolute URLs are also allowed.
- Internal links to the controls dashboards are relative: `../controls/<dashboard-dir>/index.html`.
- Keep JSON valid — the entire file is embedded into the page, so one syntax error blanks it. Validate: `python3 -m json.tool _config/start/apps.json > /dev/null`.

## Always finish by

Rebuilding (`python3 _wiring/start/generate-docs.py`) and checking any new external links are well-formed and any referenced local icons/images actually exist in `_config/start/icons|images` (a missing file 404s silently on the page).
