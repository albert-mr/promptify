# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.1] - 2026-07-06

### Fixed
- claude-families.md: folded in the new Fable/Mythos release and migration details now published outside the prompt-engineering page: general availability surfaces, 1M context / 128k output / $10+$50 pricing, 30-day retention requirement, always-on adaptive thinking behavior, summarized/omitted thinking output, refusal/fallback billing behavior, and the lower Claude API prompt-cache minimum.
- MAINTAINING.md: added the Fable/Mythos release page, migration guide, and models overview to the Claude source-doc checklist so future freshness checks catch API and availability drift, not just prompt-engineering drift.

## [1.1.0] - 2026-07-01

### Changed
- claude-families.md: Claude Fable 5 / Mythos 5 is no longer flagged dormant — the June 12 suspension banner is gone from the live docs as of this check, and the model is presented as fully available and recommended. Added the new "Capability improvements over Opus 4.8" section from the live doc (long-horizon autonomy, first-shot correctness, vision, enterprise workflows, code review/debugging, ambiguity navigation, delegation).
- Found and verified by the first live run of the `promptify-monthly-freshness-check` cloud routine (see MAINTAINING.md); the routine correctly detected the drift and prepared this exact fix locally, but could not push a branch or open a PR itself — both GitHub write paths in its cloud environment returned 403 (git-credential proxy, and GitHub MCP integration). It correctly stopped rather than working around that. This entry was completed manually using working local credentials so the finding wasn't lost; the cloud environment's GitHub write access still needs fixing before future scheduled runs can open PRs unattended.

## [1.0.2] - 2026-07-01

### Fixed
- MAINTAINING.md: corrected `claude plugin update` command — requires `plugin@marketplace` form, not the bare plugin name (verified live: `claude plugin update promptify` fails with "Plugin not found", `claude plugin update promptify@promptify` succeeds).

## [1.0.1] - 2026-07-01

### Added
- MAINTAINING.md: versioning policy, source-doc list, update propagation runbook, and a six-scenario regression checklist.
- A monthly scheduled cloud routine that checks the tracked source docs for drift and opens a PR with proposed reference-file updates (never auto-merges).

## [1.0.0] - 2026-07-01

### Added
- Initial release: SKILL.md workflow (get idea, detect harness, detect model family with disclosed guess, ask goal-vs-normal when applicable, draft, output as a single copyable block).
- Reference files: claude-families.md (Fable 5/Mythos 5, Opus 4.8, Sonnet 5, legacy models), openai-families.md (GPT-5.x, o-series, GPT-5-Codex), goal-vs-normal.md, detection-fallbacks.md.
- Claude Code packaging (.claude-plugin/marketplace.json + plugin.json) and Codex CLI discovery shim (.agents/skills/promptify symlink).
- README.md with install instructions for both Claude Code and Codex CLI.
