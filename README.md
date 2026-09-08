# CTO Starter Kit

A lightweight, static toolkit for engineering leaders: a **start page** indexing key data, guidelines, and strategic documents, a **communities directory** for finding engineering and product peers, plus **controls dashboards** for tracking security, management, operational, and engineering controls with red/yellow/green maturity scoring.

Everything is plain HTML + vanilla JavaScript generated from JSON config files by standard-library-only Python scripts. No frameworks, no build dependencies, no server — the output in `docs/` can be served by GitHub Pages or any static host.

## Repository layout

```
_config/      Content (what the site says)
  start/        apps.json — start page tabs, steps, tools, and apps
  communities/  data.json — communities grouped by region, with logos and links
  controls/     *_controls.json — one file per controls dashboard
_templates/   Presentation (what the site looks like)
  start/        index.html — start page template
  communities/  index.html — communities directory template
  controls/     index.html (dashboard), landing_page.html (control detail)
_wiring/      Build scripts (how config + template become docs)
  start/        generate-docs.py
  communities/  generate-docs.py
  controls/     generate-controls-docs.py
docs/         Generated output — do not edit by hand
```

The rule of thumb: **change content in `_config`, change look-and-feel in `_templates`, then rebuild.** Files in `docs/` are always overwritten by the generators.

## Building

Requires Python 3 (standard library only):

```bash
python3 _wiring/start/generate-docs.py        # builds docs/start/
python3 _wiring/communities/generate-docs.py  # builds docs/communities/
python3 _wiring/controls/generate-controls-docs.py  # builds docs/controls/*
```

Preview locally by opening the generated files directly, or:

```bash
python3 -m http.server -d docs 8000
# → http://localhost:8000/start/, http://localhost:8000/communities/, and http://localhost:8000/controls/security-controls/
```

## Common tasks

| Task | Where |
|---|---|
| Add or edit a tool/app/step on the start page | `_config/start/apps.json` — see [`_config/start/README.md`](_config/start/README.md) |
| Add or edit a community, region, or logo | `_config/communities/data.json` — see [`_config/communities/README.md`](_config/communities/README.md) |
| Update a control's status, owner, or evidence | `_config/controls/*_controls.json` — see [`_config/controls/README.md`](_config/controls/README.md) |
| Add a whole new controls dashboard | New JSON in `_config/controls/` + register it in `_wiring/controls/generate-controls-docs.py` |
| Change the design | `_templates/` (mind the `${placeholder}` markers — see the config READMEs) |

After any change, rerun the matching generator and commit both the config and the regenerated `docs/` output.

## Controls scoring model

Each control has a status (`red` = 1, `yellow` = 2, `green` = 3). Domain and overall maturity are weighted averages (domain weight × control weight), reported on a 1.00–3.00 scale and mapped to maturity bands defined in each config's `scoring_model`. Controls marked `"inFocus": true` are highlighted on the dashboard as the current improvement priorities.

## Publishing

The site is designed for GitHub Pages serving the `docs/` folder from `main` (Settings → Pages → Deploy from a branch → `main` / `docs`). Relative links between the start page and the dashboards (`../controls/...`) work under that layout.
