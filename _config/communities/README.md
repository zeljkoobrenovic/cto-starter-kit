# Communities config reference

`data.json` drives the communities directory at `docs/communities/index.html`.
Rebuild after editing the config, logos, or template:

```bash
python3 _wiring/communities/generate-docs.py
```

The page uses the start page's typography, cards, and tabs. Each region becomes a
tab, and search matches community names, descriptions, regions, and links across
all tabs. The selected region is remembered for the browser session.

Benelux groups communities in the Netherlands, Belgium, and Luxembourg.
Scand (Scandinavia) groups communities in Denmark, Norway, and Sweden. Name the city
and country in descriptions so readers can find local groups through search.
For regional entries belonging to a wider network, describe both the local
activities and the network's wider reach.

Country tabs may use short labels (for example, CN for China, IN for India,
and JP for Japan). LATAM (Latin America), MENA (Middle East and North Africa),
and SSA (Sub-Saharan Africa) combine national networks and city groups; descriptions
identify their countries and any wider regional reach.
Keep native community names where useful, with searchable English descriptions.

The Balkans tab includes communities in Serbia, Croatia, Slovenia, Bosnia and
Herzegovina, North Macedonia, Bulgaria, Romania, and Greece. MENA includes the
Egypt-based Prdkt+ community; groups based in Nigeria, Kenya, Uganda, and South
Africa belong under SSA.

```jsonc
{
  "metadata": {                          // optional; {} uses the defaults
    "title": "CTO Communities",
    "description": "Connect with communities for technology and engineering leaders.",
    "openInNewTab": true,
    "enableSearch": true
  },
  "regions": [
    {
      "name": "Global",
      "communities": [
        {
          "name": "CTO Craft",
          "logo": "logos/cto-craft.jpeg",
          "description": "A community for technology leaders.",
          "links": [
            { "name": "Website", "url": "https://ctocraft.com/" }
          ]
        }
      ]
    }
  ]
}
```

Titles, descriptions, and link names are plain text. Put local logos in `logos/`;
the generator copies them into `docs/communities/logos/`. Missing or omitted logos
use the community's initials. The site logo is copied from
`_config/communities/icons/logo.png`.

For artwork designed for a dark background, set an optional `logoBackground`
color on the community (for example, `"#181818"`).

`logo-sources.json` records where downloaded community artwork came from. Keep
each community's links pointed at its official website or organizer-managed
group page so readers can check membership criteria and current events.

The template at `_templates/communities/index.html` uses `${domain_name}`,
`${domain_description}`, `${communities}` (the full config), and
`${available_logos}` (the local logo paths available at build time). The config is
embedded in the HTML, so the page also works when opened directly from disk.
