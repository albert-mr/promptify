# MAINTAINING.md

This document is the maintenance runbook for `promptify` — a Claude Code / Codex CLI skill that drafts prompts and Claude Code `/goal` conditions, tuned per detected model family. It is written for two audiences equally: a human maintainer, and the automated monthly cloud agent that checks for upstream doc drift. Both should follow it exactly.

## Versioning policy

This repo uses Semantic Versioning, tracked in the `"version"` field of `.claude-plugin/plugin.json`.

- **PATCH** (`x.y.Z`) — Reference-file corrections, typo fixes, wording cleanups, or clarifications that do not change behavior. Example: fixing a stale link, rewording a sentence in `references/claude-families.md` for clarity without changing the guidance it gives.
- **MINOR** (`x.Y.0`) — Adding a new model family, deprecating or flagging a model as dormant, or a non-breaking workflow improvement. Example: adding a `references/gpt-6.md` section, marking an older Claude model as legacy, or improving how the skill selects a reference file without changing its output contract.
- **MAJOR** (`X.0.0`) — Any change to `SKILL.md`'s frontmatter contract, or any change to the shape of what promptify outputs. Example: changing the disclosure template, changing the goal-vs-normal decision logic in a way that alters past behavior, renaming or restructuring the skill's inputs/outputs.

Every version bump — regardless of size — gets a corresponding entry in `CHANGELOG.md`. No version bump without a changelog entry, and no changelog entry without a version bump.

## Source docs this skill tracks

The reference files under `skills/promptify/references/` are condensed from the following canonical sources. Any future re-check — automated or manual — must re-fetch exactly these URLs, not paraphrases or cached copies of them.

**Claude:**
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
- https://platform.claude.com/docs/en/about-claude/models/migration-guide — check the Fable/Mythos sections specifically for migration/API changes
- https://platform.claude.com/docs/en/about-claude/models/overview — check model IDs, specs, availability, pricing, and NEW model-specific docs
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview — check this one specifically for NEW dedicated prompt-engineering model pages that don't yet exist in `claude-families.md`
- https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions

**OpenAI:**
- https://developers.openai.com/api/docs/guides/latest-model — check for new model families and model-specific prompting or migration guidance
- https://developers.openai.com/api/docs/guides/prompt-engineering
- https://developers.openai.com/api/docs/guides/reasoning-best-practices
- https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- https://developers.openai.com/api/docs/models — check for new model IDs not yet listed

**Codex CLI mechanism** (check less urgently, but still track):
- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/environment-variables

**Claude Code packaging:**
- https://code.claude.com/docs/en/plugin-marketplaces

## How updates are triggered

A monthly scheduled cloud agent — a Claude Code "routine," configured outside this repo — re-fetches every URL listed above, diffs the fetched content against the corresponding files in `skills/promptify/references/*.md`, and, if there's a meaningful difference:

1. Updates the affected reference file(s) to reflect the new upstream content.
2. Bumps the version in `.claude-plugin/plugin.json` per the versioning policy above.
3. Adds a `CHANGELOG.md` entry describing the change.
4. Opens a pull request.

The routine **never** commits directly to `main`. A human maintainer (or a future Claude Code session acting as reviewer) must review and merge every such PR before the update takes effect anywhere. Nothing the routine produces is live until it is merged.

Manual updates follow the identical process by hand: re-fetch the relevant source doc(s), diff against the current reference file, edit the reference file, bump the version, add a `CHANGELOG.md` entry, and open a PR for review. There is no shortcut path that skips the PR step, even for a maintainer editing the repo directly.

## Propagating an update to installed copies

Merging a PR does not update every installed copy of promptify the same way. The two install paths are asymmetric:

- **Codex CLI: automatic for symlinks.** The checked-in project install (`.agents/skills/promptify`) and any global symlink at `$HOME/.agents/skills/promptify` point into this repo's `skills/promptify/` directory. Once a PR is merged into `main`, any Codex CLI session using one of those symlinked install paths picks up the change immediately. A copied global install must be recopied after updates.

- **Claude Code: not automatic.** The installed plugin is a cached git clone, not a symlink. After a PR is merged, the user must:
  1. Run `claude plugin marketplace update promptify` to refresh the cached clone.
  2. Run `claude plugin update promptify@promptify` to update the installed plugin pointer (the bare plugin name alone fails with "Plugin not found" — verified live; the `plugin@marketplace` form is required here even though `install` accepts either).
  3. Restart the Claude Code session, or run `/reload-plugins`, for the change to take effect.

  There is no CLI-level auto-reload for Claude Code — skipping any of these three steps means the session keeps running stale reference content.

## Regression checklist before merging any update PR

Before merging any PR that changes a reference file, `SKILL.md`, or the version, re-run these six scenarios against the updated content. Each is a concrete pass/fail check — the reviewer (human or agent) should be able to state clearly whether it passed.

1. **Claude Sonnet 5, normal-mode ask (no override).** Pass if: the disclosure line correctly names Claude Code + Sonnet 5, and the drafted prompt reflects Sonnet 5's rules — no invented `temperature`/`top_p` parameters, and explicit scope language is present.

2. **Claude Sonnet 5, goal-mode ask.** Pass if: the output is a single `/goal ...` line, at or under 4000 characters, containing a measurable end state, an exact check command, enumerated constraints, and a bound clause.

3. **Claude Opus 4.8 override, goal-mode ask.** Pass if: the disclosure reflects the override to Opus 4.8, and the drafted condition reflects Opus 4.8's specific quirks — not a copy of Sonnet 5's guidance.

4. **An ask naming a different target system entirely (e.g. "this is for GPT-5.2").** Pass if: the goal-vs-normal question is skipped entirely (never asked), and the output is always a normal prompt drafted per `openai-families.md`.

5. **OpenAI o-series override (e.g. `o4-mini`) with a prompt asking for step-by-step verification.** Pass if: the drafted prompt does NOT include chain-of-thought instructions or multiple few-shot examples — confirming the inverted-rules note for o-series still holds.

6. **Codex CLI harness, loop-shaped ask.** Pass if: no fabricated goal construct appears in the output, and the output is a normal prompt with an explicit prose success-criteria section instead.

If any scenario fails, the PR must not be merged until the failure is fixed and the checklist is re-run in full.
