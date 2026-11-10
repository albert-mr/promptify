# Promptify

Promptify is an instruction-only skill. The product is `skills/promptify/`. Read [MAINTAINING.md](MAINTAINING.md) before changing it.

- Work on a branch and open a PR against `main`. Do not commit to or merge into `main` directly.
- Run `python3 scripts/validate.py` before finishing.
- After changing skill behavior, run the relevant cases in [tests/scenarios.md](tests/scenarios.md) in fresh contexts and read the actual outputs.
- Any change under `skills/` needs a version bump in `.claude-plugin/plugin.json` and a matching `CHANGELOG.md` entry, because installed plugins stay on their version until it changes.
- Fetch the primary source yourself before quoting a provider's docs. Use quotation marks only for verbatim text, and do not quote from another agent's summary.
- The skill itself only drafts artifacts: it does not run the task inside a prompt or call an inference API. Running scenarios is how maintainers evaluate it.
