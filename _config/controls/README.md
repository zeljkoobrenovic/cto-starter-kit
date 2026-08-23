# Controls config reference

Each `*_controls.json` file here becomes one dashboard under `docs/controls/`. The mapping (config file → output folder) is registered in `_wiring/controls/generate-controls-docs.py` — add a new entry there when creating a new dashboard.

Rebuild after any edit:

```bash
python3 _wiring/controls/generate-controls-docs.py
```

## File structure

```jsonc
{
  "metadata": {
    "title": "…",              // dashboard heading and page title
    "version": "2.0",
    "icon": "security.png",    // file in _config/controls/icons/ (falls back to logo.png)
    "regions": ["EU/EEA"],
    "primary_regulatory_focus": ["GDPR", "…"],   // rendered as chips
    "source": { "title": "…", "author": "…" }    // optional attribution chip
  },
  "scoring_model": {
    "status_to_score": { "red": 1, "yellow": 2, "green": 3 },
    "overall_maturity_bands": [
      { "min": 1.0, "max": 1.5, "status": "red", "label": "High risk / urgent stabilization" }
      // bands must cover 1.0–3.0; band.status colors the domain score pills
    ]
  },
  "domains": [
    {
      "id": "grc",
      "name": "Governance, Risk & Compliance",
      "description": "…",
      "weight": 1.2,            // domain weight in the overall maturity average
      "controls": [ /* see below */ ]
    }
  ]
}
```

## Control fields

```jsonc
{
  "id": "grc-01",              // unique per dashboard; becomes landing_pages/<id>.html
  "name": "Information Security Policy",
  "description": "…",          // one sentence, shown on dashboard and detail page
  "priority": "High",
  "weight": 1.0,               // control weight within the domain
  "status": "red",             // red | yellow | green
  "score": 1,                  // keep consistent with status (red=1, yellow=2, green=3)
  "inFocus": true,             // optional — highlights as a current improvement priority
  "owner": "",                 // person or team accountable
  "last_reviewed": "2026-08-01",  // ISO dates or empty string
  "target_date": "",
  "notes": "",
  "evidence_links": ["https://…"],       // live evidence (wiki pages, reports, tickets)
  "evidence_examples": ["Signed policy", "Review log"],  // what good evidence looks like
  "scoring_criteria": {        // what each status means for THIS control
    "red": "…", "yellow": "…", "green": "…"
  }
}
```

## Conventions

- Status changes should come with updated `last_reviewed`, and ideally a note or evidence link explaining the change.
- Use `inFocus` sparingly (a handful of controls at a time) — it is the "what we're working on now" signal.
- Keep IDs stable: they are the landing page URLs.
- Weights: 1.0 is the default; deviate only when a domain/control genuinely matters more or less.
