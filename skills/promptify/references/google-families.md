# Google prompting reference

Catalog and lifecycle checked 2026-11-23. Sources are linked beside the guidance they support. For a dated offline disclosure, cite the target's Reviewed date below: the last full review of that model's guidance.

## Routing and freshness

Use the user's exact target. This is a dated reference, not live model discovery. For "latest", an unknown version, or API configuration, check the official [model catalog](https://ai.google.dev/gemini-api/docs/models), [latest models](https://ai.google.dev/gemini-api/docs/latest-model), and [deprecations](https://ai.google.dev/gemini-api/docs/deprecations), then open the relevant model's what's-new page. Follow published links; do not construct a guide URL from a guessed name. If access fails, disclose that limitation and use verified family-level guidance without claiming freshness or substituting a version.

| Target | Guidance to load | Reviewed |
| --- | --- | --- |
| `gemini-4-carbon`, `gemini-4-argon` | Shared principles + Gemini 4; Carbon and Argon integration rules | 2026-11-23 |
| `gemini-4-neon`, `gemini-4-hydrogen` | Shared principles + Gemini 4; Neon and Hydrogen integration rules | 2026-11-23 |

These are the maintained text models. Other Google targets, including Gemini 3.8 Flash, Gemini 3.5 Flash-Lite, the Gemini 2.5 family, and media, voice, or agent models, receive general guidance with the coverage limit disclosed. Never transfer Gemini 4 API rules to an older target; integration notes for it need live verification. For a new model discovered through a live check, distinguish freshly verified guidance from bundled coverage.

The [Decisions API](https://ai.google.dev/gemini-api/docs/decisions-api) (`gemini-decision-1`) takes typed yes/no, choice, and score questions rather than a prompt. Promptify does not author Decisions requests. If the user explicitly names it as the destination, say it is unsupported and ask whether a normal Gemini prompt or a TypeSafe/Jev template fits; do not reshape a Jev template for it.

A "Gemini" or Antigravity harness does not establish the exact model. Use supplied session evidence or the user's explicit destination.

## Shared principles

State the task, the context the model needs, constraints, and the response format; do not assume the model already has the required information. Add a few specific, varied examples when they show the format or decision boundary, and keep their structure and delimiters identical; too many can overfit the response to them. See [prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies).

Application instructions go in the `system_instruction` request field; a prompt cannot set it. Put shared system instructions, tool definitions, and reference documents first and the per-request input last: implicit caching runs by default on Gemini 4 prompts of at least 4,096 tokens, and Google recommends this order to maximize cache hits. See [choosing a model](https://ai.google.dev/gemini-api/docs/choosing-a-model).

Keep runtime configuration separate from copyable prompt text. Thinking level, Google Search grounding, code execution, structured outputs, and declared functions are not enabled by prose. When integration advice is requested, the guide recommends enabling Search for recent or obscure facts and code execution for arithmetic and counting.

For agents, the guide lists the behaviors to state rather than leave implicit: how deeply to diagnose before accepting the obvious cause, whether to hold the plan or pivot on new observations, how long to retry and when to stop, which actions are low-risk reads versus state-changing writes, when to assume versus ask for clarification or permission, how much to narrate between tool calls, and whether exact figures or estimates are acceptable. Its long system-instruction template is one evaluated example, not required wording.

The guide's model-specific section is written for Gemini 3, and Google links prompting patterns for Gemini 4 Carbon from a [developer guide](https://aistudio.google.com/learn/gemini-4-carbon-developer-guide) that this reference could not read. Do not add the Gemini 3 Flash date, knowledge-cutoff, or strict-grounding clauses to a Gemini 4 prompt unless the user asks.

## Gemini 4

Use [Hydrogen](https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-hydrogen) as the default for everyday coding, tool-using agents, and parallel subagents; [Neon](https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-neon) for complex engineering and knowledge work where someone is waiting on the result; [Carbon](https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-carbon) for long-running asynchronous work and deep verification; and [Argon](https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-argon) as the faster, lower-token alternative to Carbon, when the user asks how to choose. Offer this as a starting point to test, without prices.

- Do not write a system instruction that tells the model to emit tool calls as raw-text JSON when no tools are declared; Google documents this for Neon and Hydrogen as a cause of `MALFORMED_FUNCTION_CALL`. Describe when to use each declared tool, and leave the call format and JSON structure to function calling and structured outputs.
- Thinking is on by default and its depth is a request setting. Leave out "think step by step" scaffolding. For a long output, a line asking for less deliberation is a documented way to save tokens when the user wants that.
- Hydrogen flags missing context instead of guessing and batches read and search calls in parallel. Say what to do when information is missing only where the task needs a specific behavior.

**API and migration notes for all four models.** Remove `temperature`, `top_p`, and `top_k`; custom values are ignored. `thinking_level` `minimal` is not supported. Explicit context caching (`cachedContents`, `caches.create`) is not supported; implicit caching is on by default. `max_output_tokens` caps thinking plus output, so a low cap can truncate or empty the answer; lower the thinking level to save tokens instead. Input, thinking, and output share one 1,048,576-token window. A response past 65,536 tokens needs `background: true` (or client-side continuation) with a higher `max_output_tokens`. Hard requests can take minutes: use background execution or client timeouts of at least 15 minutes. Keep multi-turn and tool-calling state with `previous_interaction_id`; if the client manages history, resend earlier model turns, thought blocks, and signatures unchanged. See [thinking](https://ai.google.dev/gemini-api/docs/thinking) and [long decode](https://ai.google.dev/gemini-api/docs/long-decode).

**Carbon and Argon integration only:** levels are `low`, `medium` (default), and `high`. Raise an explicit `max_output_tokens` to at least 32,768. A non-streaming REST call returns up to 32,768 tokens per hop. Both need the paid tier. Moving from Argon to Carbon needs no request changes, but Carbon spends more thinking tokens per turn, so recheck limits and timeouts.

**Neon and Hydrogen integration only:** levels are `low`, `medium`, `high` (default), and `xhigh`. Start at `high` and keep `xhigh` for hard multi-step problems; it can overthink simple extraction. Remove low `max_output_tokens` caps or raise them to 65,536. Out-of-range sampling values return a 400 error. Do not copy a thought signature across parallel function-call parts. Neon needs the paid tier; Hydrogen is also on the free tier. When switching from Carbon or Argon, set `thinking_level` explicitly because the default changes from `medium` to `high`.
