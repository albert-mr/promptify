# Upstream review — 2026-09-07

Version 2 updates Promptify's drafting contract and refreshes its OpenAI/Anthropic guidance. Research used official provider documentation, including model catalogs, prompting guides, migrations, lifecycle notices, and installation docs. Linked references contain the maintained source inventory; temporary fetched pages and behavioral outputs are in the workspace's ignored `.context/` directory.

## Decisions from the source review

| Finding | Result in Promptify |
| --- | --- |
| [OpenAI's current guide](https://developers.openai.com/api/docs/guides/latest-model) now describes GPT-6 Astra. | Added Astra guidance for autonomy, instruction conflicts, writing style, delegation, proportional testing, and the tool-calling/parameter migration boundary. GPT-5.6 points to its own stable guide. |
| [GPT-5.6's prompting guide](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6) emphasizes concise outcome/evidence contracts and conditional tool routing. | Removed the old claim that GPT prompting should be broadly verbose or the opposite of o-series. Preserved the user's explicit requirements, examples that serve a purpose, and runtime configuration separation. |
| [Claude's shared guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) now routes to Fable 5.1 in addition to earlier dedicated guides. | Added Fable/Mythos 5.1; removed the fixed count of model-specific guides. Kept Opus, Sonnet, Fable, and Haiku differences separate. |
| [Fable 5.1 migration](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) has actual client compatibility changes. | Recorded unsupported forced tool choices, thinking-history preservation/binding, and progress display. A prompt cannot repair missing runtime support. Mythos is not assumed to share Fable's prefix enforcement. |
| [Opus 5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) discourages inherited self-verification rituals. | Remove redundant checks while retaining checks explicitly requested by the user. Do not turn a performance recommendation into permission to skip validation. |
| [Haiku 4.5 remains in the current lineup](https://platform.claude.com/docs/en/models/overview). | Removed its misleading placement as a legacy default; preserved its extended-thinking distinction. |
| [OpenAI's catalog](https://developers.openai.com/api/docs/models) includes Realtime 2.1/mini, Image 2, new transcription models, and restricted Daybreak/Cyber targets. | Added specialized routing without importing unrelated text-agent settings or implying access. Embeddings/moderation are not conversational prompt targets. |
| [OpenAI lifecycle notices](https://developers.openai.com/api/docs/deprecations) disagree with the apparent freshness of several still-published guides/catalog entries. | Marked retired coding/research targets, retired chat aliases, and Sora's scheduled 2026-09-24 shutdown. Availability comes from lifecycle/model docs, not catalog presence. |
| [Claude Code hooks](https://code.claude.com/docs/en/hooks#sessionstart-input) can include an active `model`, and [Codex config](https://learn.chatgpt.com/docs/config-file/config-reference) has a model field. | Removed the unsupported claim that neither harness exposes model information. Distinguished session-supplied evidence from defaults, aliases, and uncertain self-identification. No hooks/config changes are installed. |
| [Codex discovery](https://learn.chatgpt.com/docs/build-skills) follows symlinks. | Clarified that updates follow the actual referenced checkout; merging another worktree does not update a symlink's target checkout. |

## Source caveats

- This review is dated, not a promise of continuing freshness. Unknown versions and "latest" requests require a new official-doc check when permitted; otherwise the skill must disclose its limitation.
- The Realtime prompting guide still centers Realtime 2 while the catalog includes 2.1/mini. The reference links both model pages and does not carry over unverified effort controls.
- Several Anthropic model documents moved into `/models/<model>/...`; the old migration URL is now an index. Guessed GPT-5.4/5.5 cookbook URLs and guessed Fable 5.1 URLs returned 404. Published version-guide and migration links resolved the required material. HTTP 403 responses from the default Python client succeeded when retried with a descriptive User-Agent.
- General prompting pages sometimes retain historical comparisons and examples. Model-specific pages and lifecycle notices govern version-specific facts. Pricing, billing, retention, and platform tool matrices were removed from drafting references to reduce unrelated drift.
- Restricted availability is not ordinary access. No provider account provisioning, model configuration, API invocation, or plugin deployment was performed by this review.

## Validation method

The previous skill was applied independently to three scenarios before editing. It blocked ordinary Claude task drafting on a mode question, blocked a simple rewrite on model identity, and conflated a destination model with the drafting runtime.

The updated behavior is evaluated with the [scenario suite](../tests/scenarios.md). These are independent drafting simulations using the supplied skill, not measurements of every named provider model. Structural packaging checks run separately with `python3 scripts/validate.py`; neither check proves provider endpoint behavior. API compatibility notes were checked against the cited official docs.

Results for this update:

- All 18 scenario rubrics passed after fixing and re-running the legacy-format ambiguity, offline API-note ambiguity, and JSON failure-format case. The online freshness case fetched the catalog, current guide, lifecycle page, and exact Astra pages; the offline case disclosed that latest-model identity was unverified.
- Structural validation and the skill-authoring frontmatter validator passed. Negative checks in a temporary copy correctly rejected a reintroduced command, a broken relative link, and a broken discovery symlink.
- All 56 distinct official documentation URLs linked by the current README, maintenance guide, references, and this review returned content through their Markdown endpoints. This reachability check is separate from the claim-by-claim source review above.
- An independent review of the final changes and relevant saved sources found no actionable issues. No live model endpoint or installed plugin was exercised; application-specific schemas and edge-case policy still need evaluation in the destination application.
