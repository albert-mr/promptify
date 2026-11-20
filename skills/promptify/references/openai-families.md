# OpenAI prompting reference

Catalog and lifecycle checked 2026-11-20. Sources are linked beside the guidance they support. For a dated offline disclosure, cite the target's Reviewed date below: the last full review of that model's guidance.

## Routing and freshness

Use the user's exact target. This is a dated reference, not live model discovery. For "latest", an unknown version, or API configuration, check the official [model catalog](https://developers.openai.com/api/docs/models), [current model guide](https://developers.openai.com/api/docs/guides/latest-model), and [deprecations](https://developers.openai.com/api/docs/deprecations), then open the relevant model's guide. Follow published links; do not construct a guide URL from a guessed name. If access fails, disclose that limitation and use verified family-level guidance without claiming freshness or substituting a version.

| Target | Guidance to load | Reviewed |
| --- | --- | --- |
| `gpt-6.2-astra`, `gpt-6.2-sol` | Shared principles + GPT-6.2 Astra and Sol | 2026-11-20 |
| `gpt-6-luna` | Shared principles + GPT-6.1 Terra and GPT-6 Luna; Luna integration rules | 2026-11-10 |
| `gpt-6.1-terra` | Shared principles + GPT-6.1 Terra and GPT-6 Luna; 6.1 Terra integration rules | 2026-11-10 |

These are the maintained text models. Other OpenAI targets, including GPT-6 Astra, GPT-6.1 Sol, GPT-6 Sol, and the GPT-5.6 family, receive general guidance with the coverage limit disclosed; do not restore removed model sections from historical documents. Never transfer GPT-6 API rules to an older target; integration notes for it need live verification. For a new model discovered through a live check, distinguish freshly verified guidance from bundled coverage.

The [Decisions API](https://developers.openai.com/api/docs/guides/decisions) (`POST /v1/decisions`, generally available since 2026-10-22, `gpt-6-luna` only) takes typed `predicate`, `choice`, and `score` questions rather than a prompt. Promptify does not author Decisions requests: a Luna prompt targets Responses or Chat Completions. If the user explicitly names the Decisions API as the destination, say it is unsupported and ask whether a normal Luna prompt or a TypeSafe/Jev template fits; do not reshape a Jev template for it.

A Codex harness does not establish the target model. Use supplied session evidence or the user's explicit destination.

## Shared principles

Specify the result, relevant context, constraints, evidence, and output contract. Resolve conflicting rules. Add examples when they clarify a real format or decision boundary; use the smallest useful set. Keep prompts lean while preserving the required context. Put stable instructions and examples first and per-request context last.

For API integrations, current models accept application instructions through `developer` messages or Responses `instructions`; these outrank user input, not provider/system instructions. Keep untrusted retrieved material in clearly delimited input, outside privileged instructions. Responses `instructions` must be supplied again on later requests; `previous_response_id` does not carry that field forward. See [prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering).

Keep runtime configuration separate from copyable prompt text. Reasoning effort, pro mode, Structured Outputs, tool availability, and image detail are not enabled by prose. A JSON-only instruction describes the desired result; a supported runtime schema enforces its structure. Preserve user-requested fields, evidence, and checks even when simplifying a prompt.

## GPT-6.2 Astra and Sol

Use [GPT-6.2 Astra](https://developers.openai.com/api/docs/models/gpt-6.2-astra) for demanding reasoning and [GPT-6.2 Sol](https://developers.openai.com/api/docs/models/gpt-6.2-sol) for everyday coding and agent work when the user asks how to choose. Both use the [GPT-6.2 prompting and migration guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra.md).

- Astra writes concisely by default. When adapting an earlier prompt, check whether inherited brevity instructions cut details the reader needs. For handoffs, specify the audience and ask for a self-contained result a reader can use without seeing intermediate updates.
- For agent work, define the outcome, the decisions the agent can make, and what needs the user's input. Let it proceed on reversible assumptions, finish independent work, and verify the deliverable before handing it back.
- For code changes, identify caller behavior to preserve and repository conventions to follow. Request tests where the change needs coverage. For frontend work, name the visual reference, imagery, typography, and interface copy the task requires.

**API and migration notes for both models.** Start new integrations at `medium` effort. Migrate `none` or `minimal` to `low`. Use Responses for tool calling, including functions. Both models support text-only Chat Completions. Omit `temperature`, `top_p`, and `top_logprobs` on both endpoints. Omit `logprobs` in Chat Completions and remove `message.output_text.logprobs` from Responses `include`.

In Responses, put reusable instructions in a leading `developer` message in `input` so they are eligible for caching. Top-level `instructions` come after `input` on GPT-6.2 and suit per-request guidance. Append updated developer guidance for subsequent turns. Editing an earlier message or tool result can cause the API to discard later reasoning items. See [prefix handling](https://developers.openai.com/api/docs/guides/keep-prefix-unchanged).

## GPT-6.1 Terra and GPT-6 Luna

The [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra) offers prompting patterns derived from GPT-6 Astra as a starting point for these models. [Terra](https://developers.openai.com/api/docs/models/gpt-6.1-terra) targets visual reasoning, computer use, and writing. [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) targets high-volume tasks.

- For action requests, describe the full deliverable and which routine decisions the agent should make itself. Ask only about ambiguity or authorization that changes the work; carry on with independent authorized work while awaiting an answer. Treat "can you" or "help me" phrasing as a request to do the work, not to stop at a plan or an offer. Finish the authorized work first so the user approves a concrete, reviewable result.
- Audit loaded skills and repository instructions for contradictory process requirements. Do not add approval gates for work the user already authorized. Preserve the actual instruction hierarchy, and state whether user instructions or skills win when they conflict.
- Specify the writing style, structure, and length the reader needs. For reader-facing prose, name stock phrases to avoid and rule out unprompted "X, not Y" contrasts.
- When delegation is available and warranted, give concrete criteria for independent work. Do not assume the harness supports subagents or mandate delegation for every task.
- Scope validation to the change and required checks. Once those pass, repeat or broaden testing only for new changes, failures, or unresolved concerns.

**Luna integration only:** It supports `none`, `low`, `medium` (default), `high`, `xhigh`, and `max`. Preserve a supported effort setting during migration. Chat Completions supports function calling only with `reasoning_effort: "none"`. Built-in tools, and function calling at any other effort, require Responses. Sampling parameters such as `temperature` and `top_p` can remain at `none`. At any other effort, remove them and `top_logprobs`, Chat Completions `logprobs`, and Responses `message.output_text.logprobs`. `minimal` is unsupported; start at `low` when migrating from it.

**6.1 Terra integration only:** It supports `none`, `low`, `medium` (default), `high`, `xhigh`, and `max`. Start new integrations at `medium`; in migrations, preserve a supported effort and move `minimal` to `low`. Tool calling requires Responses at every effort, including `none`; text-only Chat Completions is supported. Sampling and log-probability options may remain only at `none`. When migrating from GPT-5.6 Terra, compare both on representative images and workflows at the same effort.

Async tool calling and mid-turn steering require application support; a prompt cannot create either. Keep corrections and side questions connected to the original task unless the user changes it. The [September 25 fix](https://developers.openai.com/api/docs/changelog) corrects degraded image encoding in GPT-6 Luna; when advising an existing image-input integration, recommend rerunning affected evaluations rather than adding prompt workarounds.

## Agent runtimes

For coding tasks, give the agent the task, repository constraints, required checks, and completion/reporting expectations. Let it inspect existing patterns before editing. Preserve local tools and their actual schemas; do not invent harness commands or mandate a fixed progress cadence.

The [Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) supplies a managed Codex harness. Model, instructions, tools, and environment are configured separately. A prompt does not provision a sandbox or durable session.
