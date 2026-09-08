# Start page config reference

`apps.json` drives the start page at `docs/start/index.html`. Rebuild after any edit:

```bash
python3 _wiring/start/generate-docs.py
```

## Top level

```jsonc
{
  "config": {
    "domainName": "CTO Starter Kit",          // page title
    "domainDescription": "…",                 // subtitle
    "openInNewTab": true,
    "enableSearch": true
  },
  "apps": [ /* one entry per tab */ ]
}
```

## Tabs

Each entry in `apps` is a tab, in one of three shapes:

**Step tabs** (guided sequences — e.g. "First 90 Days", "First Year", "Long Term"):

```jsonc
{
  "tab": "First 90 Days",
  "steps": [
    {
      "group": "Align and Communicate Guiding Principles",  // section heading
      "links": [                     // optional links for the group, shown as chips
        { "name": "guide", "link": "https://…", "icon": "icons/….png", "description": "…" }  // icon optional (defaults to icons/link.png); description optional, shown as tooltip on hover
      ],
      "logo": "images/….jpg",        // file in _config/start/images/
      "description": "…",
      "steps": [
        {
          "name": "…",               // the step itself
          "description": "…",        // why it matters, one sentence
          "tools": [                 // supporting links; may be empty
            { "name": "…", "link": "https://…", "icon": "icons/….png" }
          ]
        }
      ]
    }
  ]
}
```

**App tabs** (link collections — e.g. "Tools", "Playbooks"):

```jsonc
{
  "tab": "Tools",
  "apps": [
    {
      "group": "product",            // grouping label
      "apps": [
        {
          "name": "…",
          "link": "https://…",
          "icon": "icons/….png",     // local (icons/…) or absolute URL
          "description": "…",
          "source": ""               // optional link to source/repo
        }
      ]
    }
  ]
}
```

**Link tabs** (navigation to another page):

```json
{
  "tab": "Communities&nbsp;&#x2192;",
  "link": "../communities/index.html"
}
```

A non-empty `link` makes the tab open that URL in the same browser tab, without a content panel. The label supports HTML entities. Any `apps` or `steps` on a link tab are ignored. Link tabs can appear anywhere in the list; the first content tab is selected by default, or the previously selected content tab is restored.

## Assets

- Icons go in `_config/start/icons/`, images in `_config/start/images/`; both are mirrored into `docs/start/` at build time. Reference them with relative paths (`icons/foo.png`, `images/bar.jpg`).
- `_sources/` holds reference PDFs the content is derived from; it is not published by the generator.
- Links to the controls dashboards are relative: `../controls/<name>/index.html`.
