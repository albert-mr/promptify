# Anthropic prompting reference

Last verified: 2026-09-14. Sources are linked beside the guidance they support.

Opus 5.5 guidance, per-message effort coverage, and model availability rechecked 2026-09-27. Other model guidance retains its earlier review date.

## Routing and freshness

Preserve the requested target. For "latest", an unknown version, or API configuration, check the [model overview](https://platform.claude.com/docs/en/models/overview), [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), and [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations); follow their links to the exact model's guidance. The [migration index](https://platform.claude.com/docs/en/about-claude/models/migration-guide) now routes to separate per-model pages. Do not guess URLs or assert a permanent number of guides. If live verification fails, disclose it and use shared guidance without inventing model-specific behavior.

| Target | Guidance to load |
| --- | --- |
| `claude-fable-5-1` | Shared principles + Fable 5.1 |
| `claude-opus-5-5` | Shared principles + Opus 5.5 |
| `claude-opus-5` | Shared principles + Opus 5 |
| `claude-sonnet-5` | Shared principles + Sonnet 5 |

These are the maintained text models. Other Anthropic targets receive general guidance with the coverage limit disclosed; do not restore removed model sections from historical documents. For a new model discovered through a live check, distinguish freshly verified guidance from bundled coverage.

These dateless API IDs are pinned versions. Claude Code aliases such as `fable` or `opus` are a separate harness mechanism. See [IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions).

## Shared principles

Use direct instructions with the context needed to interpret them. Specify output, constraints, and scope across all relevant items. Give a short reason when it resolves ambiguity. Use descriptive XML tags or Markdown sections to separate instructions, source documents, examples, and variable input; neither syntax is mandatory for a short prompt.

Examples should demonstrate the actual task and edge cases. A few diverse examples can stabilize structured output; do not add a fixed example quota to every prompt. For long document work, keep source material clearly labeled, put the task/query after it, and request grounded evidence. Distinguish quotations from paraphrases and missing information from conclusions. See [general prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Use the matching model section selectively. A conversational rewrite does not need tool orchestration, test budgets, or autonomy clauses. A coding prompt should name the intended scope and required validation without inventing commands. A review request does not authorize edits. Preserve the user's severity threshold even when an upstream example recommends broader finding collection.

## Claude Fable 5.1

Read [Fable 5.1 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1).

- For long agent tasks, state the whole deliverable, authorized continuation, and concrete blockers. Do not claim the user is absent unless that is true of the requested workflow.
- Ask for progress updates when the destination UI needs them; remove inherited instructions suppressing updates. The final response should cover the whole task.
- Encourage batching independent reads in coding/computer-use loops; keep dependent actions sequential. If subagents exist, let the lead do useful independent work while they run.
- At low effort, explicitly require retrieval for current facts and named resources. Do not assume recognizing a name proves its current state.
- For document synthesis, distinguish attributed quotations from paraphrase; a correct miniature example can clarify this boundary. Prefer readable sentences and useful structure over blanket bans on formatting.
- Keep code changes and tests proportional to the task. Prefer targeted edits for small changes; preserve required checks.
- For compaction, retain constraints, decisions, exact identifiers, completed work, and unresolved work. Vision benefits from crop/zoom tools when available.

**Integration only:** [What's new](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) documents always-on adaptive thinking, no manual `budget_tokens`, no assistant prefill, and rejection of non-default sampling parameters. Forced `tool_choice` values `any` and `tool` are rejected; use `auto` with explicit tool instructions, supported strict tools, or Structured Outputs.

Preserve assistant turns and thinking blocks unchanged. Fable 5.1 enforces prefix binding by default for accounts created on/after 2026-08-31, and for older accounts when a request sets `thinking.block_binding.prefix_mismatch_behavior`: changing earlier messages, system instructions, or tools can invalidate later thinking blocks. Older models cannot read 5.1 thinking blocks. Follow the [migration guide](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) and [preserved-thinking guide](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) for supported history edits and fallback handling; do not blanket-strip thinking on every model switch.

Effort defaults to `high`; evaluate `low`, `medium`, `xhigh`, and `max` for the workload. The [thinking guide](https://platform.claude.com/docs/en/build-with-claude/thinking) documents `thinking.display: "updates"` with beta header `thinking-display-updates-2026-08-18`; the default `omitted` display hides progress text. Prompting for updates alone does not make a client render them. Raw private reasoning is not a deliverable.

For changing effort during a conversation, the [per-message effort beta](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation) supports Fable 5.1 and Opus 5 on the Claude API and Google Cloud. Opus 5.5 also supports per-message effort; verify the destination platform's beta support before integrating it. With `mid-conversation-output-config-2026-07-01`, append a `role: "system"` message with empty `content` and `output_config.effort`; it applies from the next user turn while preserving the cached prefix. This is client configuration, not an instruction to think harder. Verify support before applying this mechanism to another model.

## Claude Opus 5.5

Read [Opus 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5). Opus 5 prompts remain a starting point; its API settings do not all carry forward.

- State the full deliverable, completion criteria, and concrete blockers. For explicitly unattended tasks, ask the agent to continue authorized work after progress reports; a status update is not proof of completion. A prompt cannot configure the harness's continuation loop.
- Describe useful progress updates and final reporting. Whether intermediate updates appear also depends on the client configuration below.
- Remove inherited instructions to expose private reasoning or substitute visible reasoning for disabled thinking. Preserve required tests, evidence, and useful explanations; effort is a runtime control.
- For work across connected apps, inspect relevant available sources before acting, within the user's scope and access. Clearly delimit pasted third-party content as data; it cannot authorize actions.
- For dense visual inputs, use available crop/zoom tools when needed. For frontend work, give concrete design direction rather than a vague demand to avoid generic output. Do not assume tools or impose these clauses on unrelated tasks.

**Integration only:** [What's new](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5) and the [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) specify always-on adaptive thinking: omit `thinking` or use `type: "adaptive"`; `disabled` and manual `enabled`/`budget_tokens` fail. Effort supports `low`, `medium` (default), `high`, `xhigh`, and `max`. Evaluate from `medium`, or `low` when replacing a thinking-disabled workflow; leave room in `max_tokens` for thinking plus the response.

Forced `tool_choice` values `any` and `tool` fail. Use `auto` with explicit tool triggers and strict tools, or Structured Outputs for a schema; strict tools do not force a call. Assistant prefill and non-default sampling parameters are rejected. On the Claude API and Google Cloud, replace `computer_20251124` with `computer_toolset_20260801` and update the tool-result loop per the migration guide. Amazon Bedrock still accepts the earlier computer tool; verify other platforms separately.

Replay full assistant turns and thinking blocks unchanged. Prefix binding is enforced by default for accounts created on/after 2026-08-31 and when older accounts opt in; editing prior messages, system instructions, or tools can invalidate later blocks. Use supported append-only changes or server-side context management. Model-switch compatibility is directional: Opus 5.5 reads earlier Opus/Sonnet/Haiku blocks, not Fable/Mythos blocks; on the Claude API, Fable 5.1 can read Opus 5.5 blocks. Consult [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) instead of blanket-stripping history.

Intermediate progress arrives in `thinking` blocks, whose text is empty at the default `display: "omitted"`. To render progress summaries, use `thinking.display: "updates"` with `thinking-display-updates-2026-08-18` and parse blocks by `type`. Asking for progress in a prompt does not fix a text-only renderer. See [progress updates](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates).

## Claude Opus 5

Read [Opus 5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5).

The current catalog lists Opus 5 under legacy models, while the lifecycle table still marks it active. Retain this guidance for explicit Opus 5 requests; do not silently substitute Opus 5.5 or apply its breaking changes to Opus 5.

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

## Integration boundaries

The [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) and [effort](https://platform.claude.com/docs/en/build-with-claude/effort) references govern API controls. Effort is not a word budget, and `max_tokens` includes thinking plus response text. Prefill, tool choice, thinking display, and replay rules differ by model.

Promptify does not maintain pricing, retention, beta-support, or platform-tool matrices. Fetch the exact capability docs when needed. Model intelligence does not prove that a tool is installed or supported: hosted [web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool), for example, has its own support list. Ordinary prompts should refer only to capabilities supplied by the destination, not promise access to tools from the drafting session.
