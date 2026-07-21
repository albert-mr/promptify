# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.3.0] - 2026-07-21

### Added
- claude-families.md: Mythos 5 has no safety classifiers (Fable-only behavior) and succeeds Mythos Preview; `stop_details.category` value set; SDK-middleware fallback + fallback credit; ZDR 400 error; Fable anti-tidying and checkpoint prompt patterns; memory bootstrap; launch feature list. Opus 4.8 specs block ($5/$25, 1M default, cache min 1,024, +30% tokenizer from 4.7), `high` effort default, sampling-params 400 generalized to Opus 4.7+/Fable, mid-conversation system messages, task budgets beta, high-res image handling, prompt-steerable adaptive-thinking triggering. Sonnet 5 intro pricing ($2/$10 through 2026-08-31), no Priority Tier, JSON-escaping nuance, softer design-default claim. Haiku 4.5 has no adaptive thinking (still `budget_tokens`); Opus 4.5 "think"-word sensitivity; serving-infrastructure drift note.
- openai-families.md: GPT-5.6 `reasoning.context` param, per-effort use-case mapping, image detail settings, lean-prompt gains figures; Responses API `instructions` param; prompt-objects June 3, 2026 de-emphasis date. Codex guide refresh: gpt-5.3-codex current / gpt-5.1-codex-max legacy framing, `parallel_tool_calls: true`, ~10k-token tool-output truncation, `view_image`, apply_patch single-file scope, update_plan statuses, preamble cadence minimums, expanded AGENTS.md injection mechanics, stop-and-summarize rule.
- MAINTAINING.md: added the Opus 4.8 / Sonnet 5 "what's new" pages to the Claude source list.

### Changed
- claude-families.md: best-practices migration cross-link now targets Sonnet 5 (was Sonnet 4.5→4.6).
- MAINTAINING.md: Codex doc URLs moved to learn.chatgpt.com (old developers.openai.com/codex URLs are 308 redirects); "Claude Code: not automatic" qualified — opt-in per-marketplace auto-update exists (disabled by default for third-party marketplaces), and both update paths skip the plugin unless the pinned version changed, making the version bump load-bearing for propagation.

### Added
- openai-families.md: added GPT-5.6 Sol, Terra, and Luna model IDs plus GPT-5.6-specific guidance for lean prompts, autonomy boundaries, reasoning effort, pro mode, and response verbosity.
- MAINTAINING.md: added OpenAI's current model-guidance page to the freshness-check sources.

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
