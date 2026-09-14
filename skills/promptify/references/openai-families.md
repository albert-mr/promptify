# OpenAI prompting reference

Last verified: 2026-09-14. Sources are linked beside the guidance they support.

## Routing and freshness

Use the user's exact target. This is a dated reference, not live model discovery. For "latest", an unknown version, or API configuration, check the official [model catalog](https://developers.openai.com/api/docs/models), [current model guide](https://developers.openai.com/api/docs/guides/latest-model), and [deprecations](https://developers.openai.com/api/docs/deprecations), then open the relevant model's guide. Follow published links; do not construct a guide URL from a guessed name. If access fails, disclose that limitation and use verified family-level guidance without claiming freshness or substituting a version.

| Target | Guidance to load |
| --- | --- |
| `gpt-6-astra` | Shared principles + GPT-6 Astra |
| `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`; `gpt-5.6` aliases Sol | Shared principles + GPT-5.6 |

These are the maintained text models. Other OpenAI targets receive general guidance with the coverage limit disclosed; do not restore removed model sections from historical documents. For a new model discovered through a live check, distinguish freshly verified guidance from bundled coverage.

A Codex harness does not establish the target model. Use supplied session evidence or the user's explicit destination.

## Shared principles

Specify the result, relevant context, constraints, evidence, and output contract. Resolve conflicting rules. Add examples when they clarify a real format or decision boundary; use the smallest useful set. Keep prompts lean while preserving the required context.

For API integrations, current models accept application instructions through `developer` messages or Responses `instructions`; these outrank user input, not provider/system instructions. Keep untrusted retrieved material in clearly delimited input, outside privileged instructions. Responses `instructions` must be supplied again on later requests; `previous_response_id` does not carry that field forward. See [prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering).

Keep runtime configuration separate from copyable prompt text. Reasoning effort, pro mode, Structured Outputs, tool availability, and image detail are not enabled by prose. A JSON-only instruction describes the desired result; a supported runtime schema enforces its structure. Preserve user-requested fields, evidence, and checks even when simplifying a prompt.

## GPT-6 Astra

Use [Astra's prompting and migration guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra) and [model page](https://developers.openai.com/api/docs/models/gpt-6-astra).

- For action requests, describe the full deliverable and which routine decisions the agent should make itself. Ask only about ambiguity or authorization that changes the work; carry on with independent authorized work while awaiting an answer.
- Audit loaded skills and repository instructions for contradictory process requirements. Do not add approval gates for work the user already authorized. Preserve the actual instruction hierarchy.
- Specify the writing style, structure, and length needed by the product; Astra can otherwise produce lengthy, heavily formatted replies.
- When delegation is available and warranted, give concrete criteria for independent work. Do not assume the harness supports subagents or mandate delegation for every task.
- Scope validation to the change and required checks. Once those pass, repeat or broaden testing only for new changes, failures, or unresolved concerns.

**Integration only:** Astra supports `low`, `medium`, `high`, `xhigh`, and `max` reasoning effort, not `none` or `minimal`. When migrating from those unsupported values, begin at `low`. Remove `temperature`, `top_p`, and log-probability options as specified in the migration guide. Tool calling requires Responses even though text-only Chat Completions is supported. Async tool calling and mid-turn steering require application support; a prompt cannot create either. Keep corrections and side questions connected to the original task unless the user changes it.

## GPT-5.6 Sol, Terra, Luna

Read the dedicated [GPT-5.6 prompting guide](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6) and [version-specific model guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6). The unqualified latest-model URL now describes Astra.

- State each requirement once. Remove repeated process, irrelevant tools, and examples that add no useful behavior; retain domain constraints, evidence, completion criteria, and failure handling.
- Separate personality from collaboration: tone controls wording; collaboration rules govern asking, acting, checking, and stopping. Preserve requested facts, genre, language, and length in rewrites.
- Define tool prerequisites and when empty or partial retrieval warrants another attempt. Parallelize independent reads; keep dependent decisions sequential. Programmatic tool calling suits bounded data reduction, not every multi-tool task.
- Require citations to retrieved evidence and distinguish missing evidence from a factual negative. Do not sacrifice required evidence merely to reduce tool calls.

**Integration only:** `reasoning.effort` supports `none`, `low`, `medium`, `high`, `xhigh`, `max`; default `medium`. On migration, compare the existing setting and one level lower. Pro mode uses `reasoning.mode: "pro"` on the selected model, not a made-up `gpt-5.6-pro` slug. `text.verbosity` is independent of reasoning. Persisted reasoning defaults to `all_turns` (`auto` resolves to it); use `current_turn` when prior assumptions no longer apply. Preserve response items and assistant phase values when manually replaying history. Configure these in the client, not the generated prompt.

## Agent runtimes

For coding tasks, give the agent the task, repository constraints, required checks, and completion/reporting expectations. Let it inspect existing patterns before editing. Preserve local tools and their actual schemas; do not invent harness commands or mandate a fixed progress cadence.

The [Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) supplies a managed Codex harness. Model, instructions, tools, and environment are configured separately. A prompt does not provision a sandbox or durable session.
