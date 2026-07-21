Source: condensed from Anthropic's official prompt-engineering and model docs, research pass archived at /private/tmp/claude-501/-Users-albert/0865ef07-09e0-4a31-b5c6-31472d2fed27/tasks/wi9gw2xj5.output

# Claude Model-Family Prompting Quirks

The prompt-engineering nav has exactly **three** dedicated model-specific pages: Fable 5, Opus 4.8, Sonnet 5. Sonnet 4.6, Opus 4.6/4.7, and Haiku 4.5 have no dedicated page — they're covered only by the general best-practices page (confirmed by checking the full left-nav; not a missed link).

## Claude Fable 5 / Mythos 5

- **Model IDs**: `claude-fable-5`, `claude-mythos-5` (Project Glasswing, limited availability), `claude-mythos-preview` (invitation-only). Bedrock: `anthropic.claude-fable-5`. Google Cloud: `claude-fable-5`.
- **Doc URL**: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- **Release/API URL**: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
- **STATUS — fully available (verified 2026-07-21)**: generally available since June 9, 2026. Fable 5 is on the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud, and Microsoft Foundry; Mythos 5 is limited-availability Project Glasswing (invitation-only, offered separately for defensive cybersecurity workflows) and is the successor to Claude Mythos Preview. Fable 5 is presented as the highest-capability widely released model for hard, long-running, ambiguous work.
- **Fable vs Mythos**: Mythos 5 does **not** include the safety classifiers — the refusal/fallback/billing behavior below applies to Fable 5 only.
- **Specs/pricing/retention**: 1M token context by default, up to 128k output tokens, $10 / input MTok and $50 / output MTok. Fable/Mythos require 30-day data retention and are not available under zero data retention.
- **Capability improvements over Opus 4.8**:
  - Long-horizon autonomy: sustains productive output over multi-day, goal-directed runs with strong instruction retention.
  - First-shot correctness on complex, well-specified problems.
  - Vision: interprets dense technical images, web apps, and screenshots more accurately, often with fewer output tokens; trained to use bash/crop tools for flipped, blurry, or noisy images.
  - Enterprise workflows: stronger at financial analysis, spreadsheets, slides, and documents.
  - Code review and debugging: noticeably higher bug-finding recall (outside the cybersecurity domains the safety classifiers cover), including cross-codebase and repo-history search.
  - Navigating ambiguity and multi-threaded requests.
  - Delegation: more dependable at dispatching and sustaining parallel subagents, with reliable ongoing communication to long-running subagents/peer agents.
- **Rules/quirks**:
  - Migration from Opus 4.8 is mostly drop-in: same Messages API, same tool-use patterns, same 1M context and 128k max output, and roughly unchanged token counts.
  - Fable runs safety classifiers for offensive cybersecurity, bio/life-sciences content, and thinking-extraction; benign requests can still trigger `stop_reason: "refusal"` as an HTTP 200 response with `stop_details.category` (`"cyber"`, `"bio"`, `"reasoning_extraction"`, or `null`). Three fallback options: server-side `fallbacks` param (beta, Claude API + Claude Platform on AWS), client-side SDK middleware (works on any platform), or manual retry. Worked example: platform.claude.com/cookbook/fable-5-fallback-billing-guide.
  - Refusals before output are not billed; mid-stream classifier stops bill input plus already-streamed output, and the partial output should be discarded. "Fallback credit" refunds the prompt-cache cost of retrying on another model.
  - Requesting Fable 5 from an org whose data-retention setting doesn't meet the 30-day requirement returns a 400 `invalid_request_error` (it is not silently downgraded).
  - Thinking is **always on** (adaptive only); omit the `thinking` field and use `output_config.effort` to steer depth. `thinking: {"type": "disabled"}` and manual `budget_tokens` both return 400 errors.
  - Raw thinking is never returned. `thinking.display: "summarized"` returns readable summaries; default `"omitted"` returns empty thinking fields. Pass thinking blocks back unchanged on the same model, but strip them before replaying history on a different model unless following fallback-credit rules.
  - Effort levels: `high` = default for most tasks, `xhigh` for capability-sensitive work, `medium`/`low` for routine work. Lower efforts still often beat xhigh on prior models.
  - Lower prompt caching minimum than Opus 4.8 on the Claude API: 512 tokens; Bedrock remains 1,024 tokens.
  - Longer turns by default — hard tasks can run many minutes to hours; adjust client timeouts/streaming; discourage overplanning ("when you have enough information, act").
  - At higher effort on *routine* work it can over-gather context and do unrequested tidying/refactoring — the doc ships an anti-overengineering snippet ("Don't add features, refactor, or introduce abstractions beyond what the task requires… Only validate at system boundaries…").
  - Checkpoint pattern: "Pause for the user only when the work genuinely requires them: a destructive or irreversible action, a real scope change, or input only they can provide… ask and end the turn, rather than ending on a promise."
  - Strong instruction-following: brief instructions steer broad behaviors; "lead with the outcome" style prevents elaboration/over-explaining.
  - Ground progress claims: instruct it to audit claims against actual tool-call evidence during long runs — nearly eliminates fabricated status reports.
  - State explicit boundaries: prone to unrequested actions (drafting emails, defensive git backups) unless scoped.
  - Dispatches parallel subagents very readily; prefer async orchestrator/subagent communication, long-lived subagents.
  - Performs well with an explicit memory system (markdown lesson files) it can read/write across sessions; bootstrap it by having Fable review past sessions with subagents to seed the lesson store ("Reflect on the previous sessions we've had together…").
  - Rare early-stopping: can end a turn with "I'll now run X" and no tool call, or ask permission when it already has enough info — needs an explicit "you are operating autonomously, don't stop on a promise" system reminder.
  - Rare context-budget anxiety: can suggest new sessions/summarizing near visible token countdowns — avoid surfacing token counts, or add reassurance text.
  - Give reasons not just requests — performs better when told *why*.
  - Readability: in long agentic runs it can produce dense arrow-chain shorthand/jargon in user-facing summaries; needs an explicit instruction to write final summaries in plain, complete sentences distinct from internal shorthand.
  - Supports a custom `send_to_user` tool pattern for verbatim mid-task messages without ending its turn (must be paired with explicit elicitation instructions or it's rarely called).
  - **Never** instruct it to echo/transcribe its reasoning as response text — can trigger the `reasoning_extraction` refusal category and cause fallback to Opus 4.8.
  - Recommended scaffolding: assign harder tasks than you would to prior models; use fresh-context verifier subagents for self-checks at intervals; audit/loosen prior over-prescriptive skills, since Fable 5 needs less scaffolding (it's also good at updating skills on the fly based on what it learns from the task).
  - Supported at launch: effort, task budgets (beta header `task-budgets-2026-03-13`), memory tool, code execution, programmatic tool calling, tool-result clearing via context editing (beta header `context-management-2025-06-27`), compaction, vision. Uses the tokenizer introduced with Opus 4.7.

## Claude Opus 4.8

- **Model IDs**: `claude-opus-4-8`. Bedrock: `anthropic.claude-opus-4-8` (no `-v1` suffix — dropped starting Sonnet 4.6). Google Cloud: `claude-opus-4-8`.
- **Doc URL**: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8
- **Specs/pricing**: $5 / input MTok, $25 / output MTok; 1M context by default (no beta header); 128k output; prompt-cache minimum 1,024 tokens; `stop_details` on refusals is public (no beta header). New tokenizer starting Opus 4.7: ~30% more tokens than Opus 4.6 for the same text.
- **Rules/quirks**:
  - Calibrates response length/verbosity to perceived task complexity rather than a fixed default — tune prompts if you need consistent brevity.
  - Effort: default is `high` on all surfaces (levels recalibrated vs 4.7 — re-baseline at the same level); `xhigh` recommended for coding/agentic; `max` can show diminishing returns/overthinking; `medium`/`low` for cost/latency-sensitive or scoped tasks. Effort matters more here than prior Opus versions.
  - `temperature`/`top_p`/`top_k` return 400 (sampling params removed starting Opus 4.7 — applies to Opus 4.7+, Sonnet 5, and Fable/Mythos alike).
  - Mid-conversation system messages are supported: `role: "system"` is accepted in the `messages` array after a user turn.
  - Task budgets (beta): `output_config.task_budget: {"type": "tokens", "total": N}`, minimum 20k — the model sees a countdown and self-moderates (not a hard cap).
  - High-res images: up to 2,576px long edge (~3x more image tokens), 1:1 pixel coordinates — remove any scale-factor conversion.
  - Respects effort strictly, especially at the low end — scopes work to exactly what's asked; risk of under-thinking on moderately complex tasks at `low`.
  - Thinking is **off by default** unless you explicitly set `thinking: {type: "adaptive"}` (opposite of Sonnet 5's default-on). Adaptive-thinking *triggering* is steerable by prompt (e.g. "Thinking adds latency and should only be used when it will meaningfully improve answer quality… When in doubt, respond directly.") — useful when large system prompts cause over-thinking.
  - If running `max`/`xhigh` effort, set a large `max_tokens` budget (start ~64k) to leave room for thinking/tool calls/subagents.
  - Favors reasoning over tool calls by default; raising effort (`high`/`xhigh`) substantially increases tool usage in agentic search/coding.
  - Gives more regular, higher-quality proactive progress updates — remove scaffolding that forced "summarize every 3 tool calls."
  - More literal instruction following: does not silently generalize an instruction across items; must state scope explicitly ("apply to every section, not just the first").
  - Tone defaults to direct/opinionated with minimal validation-language and sparing emoji — re-tune style prompts if a warmer voice is needed.
  - Spawns fewer subagents by default than the older Opus line (steerable via explicit "when to spawn" guidance).
  - Has a persistent default design house-style (cream/off-white bg ~#F4F1EA, serif display fonts, terracotta accents) that fights generic "avoid X" instructions — must give a concrete alternative spec or ask it to propose several directions first.
  - Uses more tokens on interactive/multi-turn coding sessions (reasons more after each user turn) vs. single-turn autonomous agents; front-load task/intent/constraints to save tokens.
  - Meaningfully better bug-finding recall/precision than priors, but harnesses tuned for older models with conservative language ("only report high severity") can see *lower* measured recall because it more faithfully filters below the stated bar — recommend "report every issue including uncertain/low-severity ones, tag confidence/severity, let a downstream step filter."
  - Computer use: up to 2576px/3.75MP; 1080p is the recommended cost/performance balance; 720p/1366×768 for cost-sensitive.

## Claude Sonnet 5

- **Model IDs**: `claude-sonnet-5`. Bedrock: `anthropic.claude-sonnet-5`. Google Cloud: `claude-sonnet-5`.
- **Doc URL**: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
- **Specs/pricing**: introductory $2 / input MTok and $10 / output MTok through Aug 31, 2026, then $3 / $15; 1M context; 128k output. Priority Tier is **not** available on Sonnet 5.
- **Rules/quirks**:
  - Same verbosity-calibration behavior as Opus 4.8 (length scales with perceived complexity).
  - Effort defaults to `high` (same default as Sonnet 4.6); `xhigh` for the hardest coding/agentic tasks; cross-model mapping: Sonnet 5 `medium` ≈ Sonnet 4.6 `high`; Sonnet 5 `high` ≈ Sonnet 4.6 `max` — match by observed thinking length, not effort label, when benchmarking.
  - Respects effort strictly at the low end, same under-thinking risk as Opus 4.8.
  - **Adaptive thinking is ON by default** (unlike Opus 4.8) — a behavior change from Sonnet 4.6 where the same requests ran with no thinking. Pass `thinking: {type: "disabled"}` to turn it off entirely. If you ran Sonnet 4.6 with thinking off, try thinking on at *lower effort levels* on Sonnet 5 before disabling.
  - Manual extended thinking (`budget_tokens`) is fully removed — 400 error.
  - New tokenizer produces ~30% more tokens for the same text than Sonnet 4.6 — old `max_tokens` limits tuned for 4.6 may truncate output now (watch for thinking consuming the whole budget → `stop_reason: "max_tokens"`).
  - More agentic/tool-reaching by default than Sonnet 4.6; with thinking disabled it's less likely to reach for tools — needs explicit nudges if you rely on tool calls with thinking off.
  - Same literalism, tone-recalibration, and code-review-harness-recall caveats as Opus 4.8 (identical prose in both docs).
  - Setting `temperature`, `top_p`, or `top_k` to any non-default value returns a 400 error (shared with Opus 4.7+/Fable, not Sonnet-specific) — remove these params when migrating; use system-prompt instructions instead of temperature for stylistic/design variety.
  - Tool-parameter JSON escaping may differ slightly from Sonnet 4.6 — use standard JSON parsers, don't pattern-match on the raw string.
  - *May* settle into a consistent default visual style (the doc doesn't attribute Opus 4.8's specific cream/serif/terracotta palette to Sonnet 5); same two mitigations as Opus 4.8 (concrete alternative spec, or ask model to propose 4 directions first).
  - Computer use: supports the `computer_20251124` tool version; same resolution/cost guidance as Opus 4.8 (2576px max, 1080p recommended).

## Legacy / general Claude models (Opus 4.6/4.7, Sonnet 4.6, Haiku 4.5)

- **Model IDs**: `claude-opus-4-7`, `claude-opus-4-6` (Bedrock: `anthropic.claude-opus-4-6-v1`, last one with the `-v1` suffix), `claude-sonnet-4-6`, `claude-haiku-4-5-20251001` (alias `claude-haiku-4-5`; Bedrock `anthropic.claude-haiku-4-5-20251001-v1:0`).
- **Doc URL**: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (no dedicated per-model page exists for these — this shared page is genuinely the only source; don't invent a page).
- **Rules/quirks** (quirks called out specifically for these older models within the shared page):
  - Opus 4.5/4.6 are more responsive to system-prompt language than earlier models — aggressive tool-triggering phrasing ("CRITICAL: you MUST use this tool") now causes *overtriggering*; dial language back to normal ("use this tool when...").
  - Opus 4.6 does more upfront exploration/thoroughness than priors at high effort — replace blanket "default to using [tool]" with targeted "use [tool] when it would help"; remove "if in doubt, use [tool]" language; use effort as a fallback lever to reduce aggressiveness.
  - Opus 4.6/4.7/4.8/Sonnet 4.6 use manual `thinking: {type: "adaptive"}` (opt-in) — off when the `thinking` param is omitted (contrast with Fable/Mythos always-on). Haiku 4.5 has **no adaptive thinking** at all — it's the only current model still on extended thinking (`budget_tokens`).
  - `budget_tokens` manual extended thinking still functions but is deprecated on Opus 4.6/Sonnet 4.6 (and remains fully functional on Haiku 4.5); returns 400 on Opus 4.7+ and Fable/Mythos.
  - Opus 4.5 with thinking disabled is particularly sensitive to the word "think" and its variants — use "consider", "evaluate", "reason through" instead.
  - Opus 4.6 has a strong predilection to over-spawn subagents even for simple tasks (e.g., using a subagent instead of a direct grep) — needs explicit "use subagents only when parallel/isolated-context work is needed" guidance.
  - Opus 4.6 may take irreversible actions (deleting files, force-push) without confirming — needs an explicit "ask before destructive/hard-to-reverse/shared-system actions" clause.
  - Opus 4.5/4.6 tend to overengineer (extra files, unneeded abstractions/flexibility) — needs explicit minimalism instructions.
  - Opus 4.5/4.6 have improved vision (multi-image, computer-use screenshot interpretation); pairing with a crop/zoom tool boosts image-eval performance further.
  - Opus 4.5/4.6 have strong frontend design instincts but default to generic "AI slop" patterns without an explicit `<frontend_aesthetics>` style directive.
  - Sonnet 5, Sonnet 4.6, Sonnet 4.5, and Haiku 4.5 all have **context awareness** (can track remaining token budget) — an agent harness that compacts/checkpoints should tell the model this explicitly, or it may try to "wrap up" as it nears the limit.
  - The best-practices page's migration cross-link now targets "Migrating to Claude Sonnet 5 from Claude Sonnet 4.5 or earlier" (`migration-guide#migrating-from-sonnet-45`) — no longer the 4.5→4.6 section.
  - Prefilled last-assistant-turn messages are unsupported starting with Claude 4.6 models and Mythos Preview (400 error) — migration guidance given for common prefill use cases (format control, eliminating preambles, avoiding bad refusals, continuations, role consistency).

---

## Model self-knowledge (from the best-practices page)

Anthropic's documented position: **Claude does not reliably know its own precise model name/ID unless you tell it in the system prompt.** The docs give two literal sample prompts to inject:

- For self-identification: *"The assistant is Claude, created by Anthropic. The current model is Claude Opus 4.8."*
- For apps that need to emit a model string themselves: *"When an LLM is needed, please default to Claude Opus 4.8 unless the user requests otherwise. The exact model string for Claude Opus 4.8 is `claude-opus-4-8`."*

This implies a running Claude instance (via API) has no built-in ground truth for its own snapshot — a prompting tool should inject the current model name/ID explicitly rather than rely on introspection. No dedicated "how Claude Code exposes its own model ID" section was found on platform.claude.com/docs in this pass (would need Claude Code's own docs/CLI, e.g. `/model` command or the `model` field in Messages API responses, which are outside the prompt-engineering docs tree checked here) — flagging as a gap if that specific detail is needed.

## Model ID format rules (from model-ids-and-versions page)

- 4.6-generation and later: dateless, pinned format `claude-{name}-{major}[-{minor}]` (e.g. `claude-sonnet-5`, `claude-opus-4-8`) — these are NOT evergreen aliases; each ID is a fixed snapshot forever.
- Pre-4.6 models: dated format `claude-{name}-{major}-{minor}-{YYYYMMDD}` (e.g. `claude-haiku-4-5-20251001`), with a shorter alias on the Claude API (`claude-haiku-4-5`) that resolves to the latest dated snapshot — this is the one place where a "moving pointer" alias exists.
- Model weights are fixed per ID, but serving infrastructure (request router, safety classifiers, sampling logic) can change — minor behavioral differences can appear on a stable model ID.
