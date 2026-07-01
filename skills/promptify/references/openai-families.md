Source: condensed from OpenAI's official prompt-engineering docs and cookbook, research pass archived at /private/tmp/claude-501/-Users-albert/0865ef07-09e0-4a31-b5c6-31472d2fed27/tasks/wi9gw2xj5.output

## GPT-5.x general series

- **Model IDs**: `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-5-pro`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-pro`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.4-pro`, `gpt-5.5`, `gpt-5.5-pro` (plus `gpt-5.3-chat-latest`)
- **Docs**:
  - https://developers.openai.com/api/docs/guides/prompt-engineering
  - https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
  - https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide
  - https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide

**Distinctive prompting rules:**

- `reasoning_effort` controls thinking depth/tool-call persistence: `minimal`/`none` → `low` → `medium` (default in GPT-5) → `high` → `xhigh` (GPT-5.2 adds `none` as new default plus `xhigh`). Preserve existing effort settings when migrating between versions; only retune after evals.
- `verbosity` is a separate param from reasoning effort — controls final-answer length independent of reasoning length; can be overridden per-context via natural language (e.g. "verbose for code blocks, terse otherwise").
- Message hierarchy: `developer` role = highest-priority app instructions (replaces "system prompt" terminology); `user` = end-user input; `assistant` = model output. Think of developer+user like a function and its arguments.
- Recommended developer-message structure: **Identity → Instructions → Examples → Context**, using Markdown headers/lists and XML tags to delimit sections; keep static/reused content early for prompt-caching cost savings.
- GPT-5 is unusually literal/"surgically precise" about instructions — contradictory instructions hurt it more than older models; explicitly resolve conflicts/hierarchies (OpenAI ships a Prompt Optimizer tool for this).
- Agentic/tool-calling: use the **Responses API** (not Chat Completions) so reasoning items persist across tool calls (cited gains, e.g. Tau-Bench Retail 73.9%→78.2%). Calibrate tool "eagerness" via `reasoning_effort` plus explicit stop conditions/tool-call budgets. Use "tool preambles" — have the model state an upfront plan and short progress updates during long agentic rollouts.
- Structured XML tags recommended for agent specs, e.g. `<context_understanding>`, `<persistence>`, `<tool_preambles>`, `<code_editing_rules>`.
- Structured Outputs: supported via JSON-schema conformance (`strict` mode) for deterministic responses; distinguish required vs optional fields, use null for missing data rather than guessing.
- GPT-5.1 specifics: `reasoning_effort: "none"` forces zero reasoning tokens (like GPT-4.1/4o) and enables hosted tools (web/file search); named tools `apply_patch` and `shell` reduce failure rates; be explicit about parallelizing tool calls; model is highly steerable on persona/tone/verbosity; encourage "bias for action" (proceed rather than re-ask when the answer is already yes) and periodic short progress updates (~every 6 steps / 1-2 sentences).
- GPT-5.2 specifics: more deliberate default scaffolding, lower default verbosity, stronger conservative/grounding bias (prefers "I don't know" over fabrication); enforce strict scope discipline ("EXACTLY and ONLY what was requested," no invented UI/tokens); for >10k-token inputs, have the model build an internal outline and anchor claims to specific sections; flag ambiguous requests with 2-3 labeled interpretations rather than guessing.
- Prompt-management best practice (applies across the family): treat prompts as code — store in named modules/version control, review changes in the same PR as the behavior, avoid relying on the deprecated hosted "Prompt objects" API (being sunset; `v1/prompts` shutdown slated for Nov 30, 2026).

## o-series reasoning models

> **INVERTED RULES — do not reuse GPT-5.x guidance here.** The o-series was trained to need *less* prompt engineering, not more, and several GPT-5.x techniques actively hurt it. Treat this family as the opposite prompting regime from GPT-5.x.

- **Model IDs**: `o1`, `o1-mini`, `o1-preview`, `o1-pro`, `o3`, `o3-mini`, `o3-pro`, `o4-mini`
- **Docs**:
  - https://developers.openai.com/api/docs/guides/reasoning-best-practices
  - https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide

**Distinctive prompting rules (inverted relative to GPT-5.x):**

- **No chain-of-thought prompting.** Do NOT say "think step by step" or "explain your reasoning" — these models already reason internally, and explicitly asking them to reason more can hurt performance. This is the opposite of general LLM/GPT-5.x-style prompting.
- **Keep prompts simple and brief.** These models were trained to need less prompt engineering, not more — avoid the verbose, heavily-scaffolded prompt style that benefits GPT-5.x.
- **Minimize/avoid few-shot examples.** Test zero-shot first — multiple examples can measurably degrade performance (the opposite of typical LLM guidance, including GPT-5.x's Identity→Instructions→Examples→Context structure). If one example is used, keep it minimal and highly relevant.
- "Developer messages are the new system messages" as of `o1-2024-12-17` — instructions should be framed as developer-role directives per the model spec's chain-of-command (this part is shared terminology with GPT-5.x, but the content/density of what you put in that developer message should stay brief per the inverted rules above).
- Reasoning models suppress Markdown formatting by default; to re-enable it, put the literal string **"Formatting re-enabled"** as the first line of the developer message.
- Use clear delimiters (Markdown headers, XML tags, section titles) to separate prompt sections; state explicit constraints/budgets and clear success criteria rather than open-ended asks.
- Function/tool calling: these models are trained to invoke tools natively as part of their internal chain of thought. Best practices: explicitly order required calls ("check X exists before creating Y"), forbid promising future calls ("Do NOT promise to call a function later — if a call is required, emit it now"), enable `strict: true` for schema-conformant args, and give few-shot examples inside function *descriptions* (not the main prompt) if needed.
- No hard cap on tool count, but keep to roughly <100 tools / <20 args per tool for reliable in-distribution behavior; ambiguous/overlapping tool descriptions cause misfires or tool-call avoidance — write precise, disambiguated tool descriptions and decision rules for overlapping tools.
- Use the Responses API with `store: true` (or `include=["reasoning.encrypted_content"]`) to persist reasoning items across turns/tool calls — improves both quality and token efficiency versus reconstructing reasoning via Chat Completions.
- Filter available MCP/tool lists via `allowed_tools` to reduce payload bloat and cross-tool confusion.

## GPT-5-Codex series

- **Model family**: specialized agentic-coding variant, distinct guide from general GPT-5
- **Model IDs**: `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-mini`, `gpt-5.1-codex-max`, `gpt-5.2-codex`, `gpt-5.3-codex`
- **Docs**: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide

**Distinctive prompting rules:**

- Accessed via the Responses API; `reasoning_effort: "medium"` recommended for interactive coding, `"high"`/`"xhigh"` for long-running autonomous tasks.
- Preferred/optimized tools: `apply_patch` (structured diff format — use exactly as specified, don't reinvent), `shell_command` (pass command as a string, not a list; always set `workdir`), `update_plan` (structured TODO/plan tracking).
- Must batch parallel exploration/reads via `multi_tool_use.parallel`; avoid unnecessary sequential file calls.
- GPT-5.3-Codex introduces a required `phase` field on assistant output items (`null | "commentary" | "final_answer"`) that must be preserved when reconstructing conversation history, or performance degrades.
- Supports brief mid-rollout "preamble" progress updates (1-2 sentences every 1-3 steps) without ceremonial/ritual logging of every action.
- Biased toward autonomous action with reasonable assumptions over asking clarifying questions; preserves repo-level `AGENTS.md` instructions injected as user-role messages, applied root-to-leaf; prefers dedicated tools over raw shell commands when available.
