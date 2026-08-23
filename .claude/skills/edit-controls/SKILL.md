---
name: edit-controls
description: Update controls dashboards — change a control's status/owner/evidence, mark controls in focus, add controls or domains, or create a whole new dashboard. Use for any edit to _config/controls/*_controls.json.
---

# Edit controls dashboards

Content lives in `_config/controls/*_controls.json` (one file per dashboard: security, management, operational, engineering). Full field reference: `_config/controls/README.md`. Never edit `docs/` — it is generated.

## Updating a control's status

1. Find the control by `id` or `name` in the right JSON file.
2. Set `status` (`red`/`yellow`/`green`) **and** `score` (1/2/3) — they must stay consistent.
3. Update `last_reviewed` to today's date, and where possible add an `evidence_links` entry or a `notes` sentence explaining the change.
4. Rebuild and verify (see `/build`).

## Marking focus priorities

Set `"inFocus": true` on the few controls currently being worked on (and remove it from ones that no longer are). Keep the in-focus set small — it renders as the "working on now" signal on the dashboard.

## Adding a control

Copy an existing control in the same domain as a template. Required: unique `id` (kebab-case, prefixed by domain, e.g. `grc-07` — it becomes the landing page filename), `name`, `description`, `status` + `score`, and `scoring_criteria` with concrete red/yellow/green definitions specific to that control. Default `weight` to 1.0.

## Adding a domain

Add to the `domains` array: `id`, `name`, `description`, `weight` (1.0 unless it genuinely matters more/less), and `controls`.

## Adding a whole new dashboard

1. Create `_config/controls/<name>_controls.json` (copy an existing file's `metadata` and `scoring_model` as a starting point; add an icon PNG to `_config/controls/icons/` and reference it in `metadata.icon`).
2. Register it in the `CONTROLS` list in `_wiring/controls/generate-controls-docs.py` (config path + docs output dir, dashes not underscores for the dir name).
3. Optionally link it from the start page (`_config/start/apps.json`, relative link `../controls/<dir>/index.html`).
4. Rebuild.

## Always finish by

Validating the JSON (`python3 -m json.tool <file> > /dev/null`), running `python3 _wiring/controls/generate-controls-docs.py`, and confirming the affected dashboard renders (the `/build` skill has the checks).
