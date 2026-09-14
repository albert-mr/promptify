# Anthropic prompting reference

Last verified: 2026-09-14. Sources are linked beside the guidance they support. The current lineup and dedicated prompting guides are unchanged since the September 7 review.

## Routing and freshness

Preserve the requested target. For "latest", an unknown version, or API configuration, check the [model overview](https://platform.claude.com/docs/en/models/overview), [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), and [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations); follow their links to the exact model's guidance. The [migration index](https://platform.claude.com/docs/en/about-claude/models/migration-guide) now routes to separate per-model pages. Do not guess URLs, assert a permanent number of guides, or equate a legacy listing with retirement. If live verification fails, disclose it and use shared guidance without inventing model-specific behavior.

| Target | Status / routing at this review |
| --- | --- |
| `claude-fable-5-1` | Current highest-capability broadly available line; Fable 5.1 section |
| `claude-mythos-5-1` | Same-generation specialized model; Project Glasswing access only; Fable 5.1 guidance with API distinctions below |
| `claude-opus-5` | Current default recommendation for most workloads; Opus 5 section |
| `claude-sonnet-5` | Current speed/intelligence option; Sonnet 5 section |
| `claude-haiku-4-5-20251001` / `claude-haiku-4-5` | Current fast tier; Haiku section, not a legacy default |
| `claude-fable-5`, `claude-mythos-5` | Earlier generation; Mythos remains access-gated; Fable 5 section |
| `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6` | Older, still active in the lifecycle table; use their specific guidance |
| Opus 4.5 / Sonnet 4.5 | Earlier supported targets; use dated IDs or documented aliases and check lifecycle |
| `claude-mythos-preview` | Deprecated invitation-only predecessor; verify access and lifecycle, never select by default |

Opus 4.1, Opus 4, Sonnet 4, Sonnet 3.7, Haiku 3.5, and Haiku 3 have retired on the Claude API. Partner-platform retirement schedules can differ. A requested retired target should receive a clear availability note, not a silent model substitution. See [deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations).

Claude 4.6 and later use dateless pinned IDs such as `claude-fable-5-1`; these are not moving aliases. Earlier models use dated snapshots and short aliases. Claude Code aliases such as `fable` or `opus` are a separate harness mechanism. See [IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

## Shared principles

Use direct instructions with the context needed to interpret them. Specify output, constraints, and scope across all relevant items. Give a short reason when it resolves ambiguity. Use descriptive XML tags or Markdown sections to separate instructions, source documents, examples, and variable input; neither syntax is mandatory for a short prompt.

Examples should demonstrate the actual task and edge cases. A few diverse examples can stabilize structured output; do not add a fixed example quota to every prompt. For long document work, keep source material clearly labeled, put the task/query after it, and request grounded evidence. Distinguish quotations from paraphrases and missing information from conclusions. See [general prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Use the matching model section selectively. A conversational rewrite does not need tool orchestration, test budgets, or autonomy clauses. A coding prompt should name the intended scope and required validation without inventing commands. A review request does not authorize edits. Preserve the user's severity threshold even when an upstream example recommends broader finding collection.

## Claude Fable 5.1 / Mythos 5.1

Read [Fable 5.1 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1).

- For long agent tasks, state the whole deliverable, authorized continuation, and concrete blockers. Do not claim the user is absent unless that is true of the requested workflow.
- Ask for progress updates when the destination UI needs them; remove inherited instructions suppressing updates. The final response should cover the whole task.
- Encourage batching independent reads in coding/computer-use loops; keep dependent actions sequential. If subagents exist, let the lead do useful independent work while they run.
- At low effort, explicitly require retrieval for current facts and named resources. Do not assume recognizing a name proves its current state.
- For document synthesis, distinguish attributed quotations from paraphrase; a correct miniature example can clarify this boundary. Prefer readable sentences and useful structure over blanket bans on formatting.
- Keep code changes and tests proportional to the task. Prefer targeted edits for small changes; preserve required checks.
- For compaction, retain constraints, decisions, exact identifiers, completed work, and unresolved work. Vision benefits from crop/zoom tools when available.

**Integration only:** [What's new](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) documents always-on adaptive thinking, no manual `budget_tokens`, no assistant prefill, and rejection of non-default sampling parameters. Forced `tool_choice` values `any` and `tool` are rejected; use `auto` with explicit tool instructions, supported strict tools, or Structured Outputs.

Preserve assistant turns and thinking blocks unchanged. Fable 5.1 enforces prefix binding by default for accounts created on/after 2026-08-31, and for older accounts when a request sets `thinking.block_binding.prefix_mismatch_behavior`: changing earlier messages, system instructions, or tools can invalidate later thinking blocks. Mythos 5.1 does not enforce that check. Older models cannot read 5.1 thinking blocks. Follow the [migration guide](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) and [preserved-thinking guide](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) for supported history edits and fallback handling; do not blanket-strip thinking on every model switch.

Effort defaults to `high`; evaluate `low`, `medium`, `xhigh`, and `max` for the workload. The [thinking guide](https://platform.claude.com/docs/en/build-with-claude/thinking) documents `thinking.display: "updates"` with beta header `thinking-display-updates-2026-08-18`; the default `omitted` display hides progress text. Prompting for updates alone does not make a client render them. Raw private reasoning is not a deliverable.

For changing effort during a conversation, the [per-message effort beta](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation) supports Fable 5.1, Mythos 5.1, and Opus 5 on the Claude API and Google Cloud. With `mid-conversation-output-config-2026-07-01`, append a `role: "system"` message with empty `content` and `output_config.effort`; it applies from the next user turn while preserving the cached prefix. This is client configuration, not an instruction to think harder. Earlier Fable 5 does not support it. The [Fable 5.1 migration guide](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) now clarifies that the tokenizer is unchanged; that does not promise unchanged token usage or latency.

## Claude Opus 5

Read [Opus 5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5).

- Provide the complete task and constrain scope explicitly. Keep the intended depth; avoid quietly broadening or narrowing the deliverable.
- Specify conversational length and written-artifact length separately when both matter. Lower reasoning effort does not reliably shorten the visible answer.
- Tune progress cadence with a positive description of useful updates. Avoid forcing narration for every tool call.
- Remove inherited self-check rituals and mandatory verifier agents: Opus 5 already verifies readily. **Keep checks and evidence explicitly required by the user or task.**
- Delegate only where sizeable independent work justifies it and the harness supports it.
- For reviews, define the reporting threshold concretely; literal filtering can hide findings the user actually wanted.

**Integration only:** adaptive thinking is on by default. Disabling it is allowed only at effort `high` or below; `xhigh`/`max` plus disabled thinking fails. Prefer lower effort with thinking enabled where quality holds. Thinking-off tool workflows can emit tool calls as plain text or leak internal tags; that is not tool execution. Parse response blocks by `type`, not position, and preserve full assistant turns for replay. See [Opus 5 migration](https://platform.claude.com/docs/en/models/opus-5/migration-guide).

## Claude Sonnet 5

Read [Sonnet 5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5).

- State whether instructions apply to every item/section. Sonnet follows scope literally, especially at lower effort.
- Response length scales with task complexity; give explicit length and voice requirements when they matter.
- Use precise tool triggers. Thinking-off workflows may need an explicit retrieval instruction; raising effort can improve shallow work.
- Remove rigid inherited progress-message schedules unless the product needs them.
- For design work, give concrete visual direction and existing design-system constraints. Ask for alternative directions when the user wants exploration, not as an obligatory approval step.
- In code review, use a concrete reporting bar and retain the user's requested severity/scope filters.

**Integration only:** adaptive thinking defaults on, effort defaults to `high`, and manual `budget_tokens` is removed. Non-default `temperature`, `top_p`, and `top_k` fail; steer tone in the prompt. Revisit total `max_tokens` and parse typed blocks rather than assuming the first block is text. See [Sonnet 5 migration](https://platform.claude.com/docs/en/models/sonnet-5/migration-guide).

## Claude Haiku 4.5

Haiku remains the current fast tier. Use clear task boundaries, necessary context, and representative examples for repeated formatting or classification. Do not apply Fable/Opus-specific autonomy or verbosity fixes by default.

Haiku uses extended thinking with `budget_tokens`, not adaptive thinking or the effort parameter. When giving API advice, do not set both `temperature` and `top_p`. See [Haiku overview](https://platform.claude.com/docs/en/models/haiku-4-5/overview) and [migration guide](https://platform.claude.com/docs/en/models/haiku-4-5/migration-guide).

## Earlier Claude targets

- **Fable 5 / Mythos 5:** use [Fable 5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5). Ground progress claims in actual results, define scope and authorized persistence, and avoid unnecessary planning or tidying. Do not transfer 5.1-only forced-tool or prefix-binding rules to 5. Thinking is always adaptive; the [Fable 5 migration guide](https://platform.claude.com/docs/en/models/fable-5/migration-guide) covers API differences and gated Mythos access.
- **Opus 4.8:** use its [dedicated guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8). Be explicit about per-item scope and design direction. It tends to delegate less than Opus 5. Thinking is opt-in; effort labels should be re-evaluated across versions, and `max` can overthink routine work.
- **Opus 4.7/4.6, Sonnet 4.6, Opus/Sonnet 4.5:** use the [shared guide's model-specific notes](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Older Opus can overreact to aggressive tool-use language and over-delegate; conditional tool rules are preferable. Preserve the exact model's thinking/sampling support. Manual thinking is deprecated on 4.6 and removed on Opus 4.7+, while Haiku 4.5 still supports it.

## Integration boundaries

The [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) and [effort](https://platform.claude.com/docs/en/build-with-claude/effort) references govern API controls. Effort is not a word budget, and `max_tokens` includes thinking plus response text. Prefill, tool choice, thinking display, and replay rules differ by model.

Promptify does not maintain pricing, retention, beta-support, or platform-tool matrices. Fetch the exact capability docs when needed. Model intelligence does not prove that a tool is installed or supported: hosted [web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool), for example, has its own support list. Ordinary prompts should refer only to capabilities supplied by the destination, not promise access to tools from the drafting session.
