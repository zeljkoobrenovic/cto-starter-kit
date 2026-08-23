---
name: publish
description: Rebuild the site, verify output is in sync, then commit and push to GitHub. Use when the user asks to publish, deploy, ship, or push changes.
---

# Publish

1. **Rebuild both generators** so `docs/` matches `_config` + `_templates`:
   ```bash
   python3 _wiring/start/generate-docs.py
   python3 _wiring/controls/generate-controls-docs.py
   ```
2. **Verify**: run the sanity checks from the `/build` skill (no unresolved `${...}` placeholders in `docs/`, generators exited 0).
3. **Review the diff** (`git status`, `git diff --stat`) — confirm the changed `docs/` files correspond to the source changes being published, and nothing unexpected (e.g. `venv/`, `.idea/`) is staged.
4. **Commit** source and generated output together, with a message describing the content change (not "regenerate docs"). End the message with the Co-Authored-By line required by the harness.
5. **Push** to `origin main` and confirm with `git log --oneline -1` + `git status` (clean tree).

The site is served by GitHub Pages from the `docs/` folder on `main` — a push is a deploy, so never push a half-rebuilt `docs/`. Pages typically takes a minute or two to update after push.
