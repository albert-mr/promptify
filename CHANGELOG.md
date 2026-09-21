# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [3.0.0] - 2026-09-21

### Added
- Explicit TypeSafe/Jev authoring support: native JSON request templates with Choice, Noul, and Score questions, a dated provider reference, and behavioral regression scenarios.
- JSON syntax checks for bundled examples in the existing dependency-free validator.

### Changed
- Expanded the output contract: OpenAI/Anthropic destinations still receive normal prompts; explicit TypeSafe/Jev destinations receive request templates. Prompts about building with TypeSafe retain their named generative destination.
- Updated target resolution, packaging, and maintenance for the third provider, including offline/unknown-version disclosures and incompatible-request handling. Promptify drafts only; it does not call inference APIs, install SDKs, or require API keys.

## [2.1.1] - 2026-09-14

### Changed
- Focused model-specific guidance on GPT-6 Astra, GPT-5.6 Sol/Terra/Luna, Claude Fable 5.1, Opus 5, and Sonnet 5. Removed older and specialized model sections, including Haiku 4.5 and GPT-5.3 Codex; other OpenAI/Anthropic targets retain an explicit general-guidance fallback.
- Restored the README illustration as `assets/is-this-astra-6.svg` with “IS THIS ASTRA 6?” text and updated accessible description.
- Updated maintenance scope and regression cases to match the focused model list. Historical review documents record their original coverage.

## [2.1.0] - 2026-09-14

### Added
- GPT-Live 1 guidance for conversation/backend separation, handoff policies, interruptions, and confirmed outcomes.
- GPT Image 2.5 Sunburst/Flare prompting guidance, reference-image roles, edit preservation, transparency, and correct Responses tool-model selection.
- GPT-Rosalind routing for approved internal life-sciences research and focused analysis of large datasets.
- Regression scenarios for the new targets, Claude effort changes, both online and offline Anthropic freshness, and blocked model switches.

### Changed
- Rechecked both providers' catalogs, prompting guides, migrations, and lifecycle notices. GPT-6 Astra and the Claude Fable/Mythos 5.1, Opus 5, Sonnet 5, and Haiku 4.5 lineup remain current; their existing drafting guidance is retained.
- Added GPT-5.4-Cyber's October 1 shutdown, image-model retirement dates, and the managed Agents API's distinction from a model target.
- Clarified Claude per-message effort support, tokenizer versus token-usage changes, optional prefix binding on older accounts, and pending versus completed Claude Code model switches.
- Replaced the broken Realtime prompting URL and redirected Anthropic release-note URL. Normal-prompt-only behavior remains unchanged.

## [2.0.0] - 2026-09-07

### Removed
- Goal mode, its mandatory mode question, completion-condition reference, and packaging/CI dependencies. All requests now produce normal prompts, including autonomous-task briefs.
- Unsupported runtime-identification claims, the model-guessing illustration, and pricing/billing tables unrelated to prompt drafting.

### Changed
- Explicit destination models take precedence over the drafting runtime. Target disclosure distinguishes user input, supplied session identity, and unknown identity; simple requests no longer block on model detection. Prompt-only formatting is respected.
- Provider references now use dated official sources, version-specific routing, lifecycle checks, and an honest fallback for unknown versions or unavailable live docs.
- Replaced the false GPT-versus-o-series "opposite rules" framing with conditional examples, concise outcome-focused instructions, evidence requirements, and separate API configuration notes.
- Preserved requested scope, checks, languages, formats, and authorization while removing redundant scaffolding; draft contents are treated as input and never executed.
- Rewrote installation and maintenance guidance, including correct checkout/symlink update behavior. Historical entries below remain records of their original versions.
- Updated CI to the current checkout action with the Node 24 runtime, removing the deprecated-runtime warning.

### Added
- GPT-6 Astra and its prompting/API differences; refreshed GPT-5.6 Sol/Terra/Luna guidance and older-model lifecycle notes.
- Claude Fable/Mythos 5.1, including current prompting guidance, forced-tool restrictions, progress display, and thinking-history compatibility; refreshed Opus 5, Sonnet 5, and current Haiku 4.5 coverage.
- Routing for specialized OpenAI targets, including Realtime 2.1/mini, Image 2, transcription, and restricted Daybreak/Cyber models, with retired-target caveats.
- A dependency-free local/CI validator, reproducible behavioral scenarios, and a dated upstream review.

## [1.4.0] - 2026-07-25

### Added
- claude-families.md: new `## Claude Opus 5` section (released 2026-07-24) — model IDs, $5/$25 pricing, 1M context as default *and* max, 512-token cache minimum, Fast mode, no Priority Tier, and its prompting quirks: thinking on by default, `thinking: disabled` rejected above effort `high`, `max` as a genuine top tier, verbosity not controlled by effort, self-verification that makes carried-over verification scaffolding harmful, scope widening, eager subagent delegation, and the tool-call-as-text / leaked-`<thinking>`-tag artifacts that appear with thinking disabled. Also records four things the Opus 5 page itself does *not* say, each verified against the docs after a regression run surfaced them as gaps: sampling params and prefill 400 (documented only in the migration guide, where Opus 5 is named); literalism carries forward from Opus 4.7 though the Opus 5 page drops the topic; Opus 5 has **no** context awareness and should be paced with task budgets; and early-stopping / promise-ending / fabricated-progress guidance is Fable 5-specific and must not be ported to Opus 5.
- MAINTAINING.md: Opus 5 prompting and what's-new pages added to the tracked source list.

### Changed
- claude-families.md: dedicated model-page count corrected from three to four (Opus 5 added); Opus 4.8 marked legacy as of Opus 5's release; model self-knowledge sample prompts now quote Opus 5 per upstream; thinking-default rule extended to cover Opus 5 / Sonnet 5 default-on behavior; Priority Tier exclusion list corrected (Mythos 5, Mythos Preview, Opus 5, Sonnet 5 — and commitments no longer sold) instead of "Sonnet 5 only"; Fable 5's 512-token cache minimum no longer described as unique; web fetch tool noted as unavailable on Opus 5 specifically — it is the one server tool Opus 5 drops, while Fable 5 and Mythos 5 both support it.
- openai-families.md: lean-prompt gains now include the 33-67% cost reduction figure. No new OpenAI models — the GPT-5.6 trio is still the frontier line.
- MAINTAINING.md: prompt-engineering overview page no longer enumerates per-model pages, so the best-practices page is now the authoritative list; regression scenario 3 retargeted from Opus 4.8 to Opus 5.

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
