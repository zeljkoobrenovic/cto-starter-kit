"""Build docs/communities/ from the communities config and HTML template.

Usage:
    python3 _wiring/communities/generate-docs.py

Uses only the Python standard library, like the start-page generator.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "_config" / "communities"
CONFIG_FILE = CONFIG_DIR / "data.json"
TEMPLATE_FILE = REPO_ROOT / "_templates" / "communities" / "index.html"
OUT_DIR = REPO_ROOT / "docs" / "communities"


def inline_json(value: object) -> str:
    """Keep config strings from terminating the inline script element."""
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")


def main() -> int:
    for source in (TEMPLATE_FILE, CONFIG_FILE):
        if not source.is_file():
            raise SystemExit(f"error: missing source at {source}")

    data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    metadata = data.get("metadata") or {}
    logos_dir = CONFIG_DIR / "logos"
    available_logos = sorted(
        logo.relative_to(CONFIG_DIR).as_posix()
        for logo in logos_dir.rglob("*") if logo.is_file()
    )
    substitutions = {
        "domain_name": html.escape(metadata.get("title") or "CTO Communities"),
        "domain_description": html.escape(
            metadata.get("description")
            or "Connect with communities for technology and engineering leaders."
        ),
        "communities": inline_json(data),
        "available_logos": inline_json(available_logos),
    }
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    page = re.sub(
        r"\$\{(" + "|".join(substitutions) + r")\}",
        lambda match: substitutions[match.group(1)],
        template,
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if logos_dir.is_dir():
        shutil.copytree(logos_dir, OUT_DIR / "logos", dirs_exist_ok=True)
    (OUT_DIR / "icons").mkdir(exist_ok=True)
    shutil.copy2(REPO_ROOT / "_config" / "communities" / "icons" / "logo.png", OUT_DIR / "icons" / "logo.png")
    (OUT_DIR / "index.html").write_text(page, encoding="utf-8")

    print(f"[built] communities -> {(OUT_DIR / 'index.html').relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
