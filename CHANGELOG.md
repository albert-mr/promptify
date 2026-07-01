# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
