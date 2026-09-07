# OpenAI prompting reference

Last verified: 2026-09-07. Sources are linked beside the guidance they support.

## Routing and freshness

Use the user's exact target. This is a dated reference, not live model discovery. For "latest", an unknown version, or API configuration, check the official [model catalog](https://developers.openai.com/api/docs/models), [current model guide](https://developers.openai.com/api/docs/guides/latest-model), and [deprecations](https://developers.openai.com/api/docs/deprecations), then open the relevant model's guide. Follow published links; do not construct a guide URL from a guessed name. If access fails, disclose that limitation and use verified family-level guidance without claiming freshness or substituting a version.

| Target | Guidance to load |
| --- | --- |
| `gpt-6-astra` | Shared principles + GPT-6 Astra |
| `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`; `gpt-5.6` aliases Sol | Shared principles + GPT-5.6 |
| `gpt-5.5`, `gpt-5.5-pro`; `gpt-5.4`, `gpt-5.4-pro`, `gpt-5.4-mini`, `gpt-5.4-nano` | Earlier GPT models; preserve the specific tier |
| GPT-5, GPT-5.1, GPT-5.2 and their listed variants | Earlier GPT models + exact version guide |
| `gpt-5.3-codex` and earlier Codex-suffixed models | Coding models and harnesses |
| `o1`, `o1-pro`, `o3`, `o3-mini`, `o3-pro`, `o4-mini` | Earlier reasoning models |
| GPT-4.1, GPT-4.1 mini/nano; GPT-4o and GPT-4o mini | Non-reasoning models |
| Voice, image, video, research, or cyber targets | Specialized targets; verify availability |

GPT-6 Astra is the catalog's flagship recommendation; Terra and Luna retain their cost/latency roles. That recommendation does not override an explicit older target. `chat-latest` is a moving ChatGPT Instant alias, not a pinned Astra snapshot. Catalog presence alone does not establish availability: retired entries remain listed. For example, `o1-preview`, `o1-mini`, `codex-mini-latest`, and `chatgpt-4o-latest` have shutdown entries in the deprecations page.

**Lifecycle at this review:** GPT-5/5.1/5.2 Codex-suffixed models and both dedicated deep-research models retired on 2026-07-23; GPT-5.2/5.3 chat aliases retired on 2026-08-10. Sora 2 and the Videos API are scheduled to shut down on 2026-09-24. Several older GPT/o-series snapshots retire on 2026-10-23, and GPT-5/o3 snapshots on 2026-12-11. Check the exact ID and date before recommending deployment. Historical prompt adaptation can preserve an explicitly requested target while disclosing its status.

## Shared principles

Specify the result, relevant context, constraints, evidence, and output contract. Resolve conflicting rules. Add examples when they clarify a real format or decision boundary; use the smallest useful set. Modern GPT reasoning models also benefit from lean prompts: they are not an opposite prompting regime to o-series.

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

## Earlier GPT models

- **GPT-5.5 / Pro:** outcome-focused prompting, fewer prescribed steps, and schema enforcement through supported Structured Outputs. Preserve required context and output meaning while removing redundant scaffolding. See the [GPT-5.5 guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.5).
- **GPT-5.4 / Pro / mini / nano:** specify completion across every requested item, retrieval recovery, evidence boundaries, and proportionate validation. Give compact, explicit routing and output rules to smaller tiers. See the [GPT-5.4 guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.4); verify individual tier capabilities in the catalog.
- **GPT-5 / mini / nano / Pro, GPT-5.1, GPT-5.2 / Pro:** preserve exact-version controls and defaults. Avoid conflicting instructions; tune autonomy, progress reporting, and response length to the task. See [GPT-5](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide), [GPT-5.1](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide), and [GPT-5.2](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide).

Do not carry one version's reasoning levels, sampling support, context window, or pro naming into another. OpenAI's [reasoning guide](https://developers.openai.com/api/docs/guides/reasoning) documents differences; verify controls for the requested endpoint before suggesting settings.

## Earlier reasoning models

For o-series, start with direct instructions and zero-shot prompting. Add carefully aligned examples if evaluation shows they help; examples are not prohibited. Specify success criteria, constraints, and relevant evidence. Request an explanation or calculation when it is part of the deliverable, without demanding private chain of thought. The literal `Formatting re-enabled` developer-message convention is documented for relevant o-series models, not a universal GPT setting. See [reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices).

For o3/o4-mini tool workflows, document prerequisites, input requirements, and retry conditions in tool descriptions. Schema strictness belongs in tool configuration. See the [o3/o4-mini guide](https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide). This older guide's model comparisons do not establish today's recommended model.

## Coding models and harnesses

The [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) covers `gpt-5.3-codex`, with older examples for the retired `gpt-5.1-codex-max`. Retired targets also include `gpt-5-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-mini`, and `gpt-5.2-codex`; retain their guidance only for explicit historical adaptation.

Give the agent the task, repository constraints, relevant checks, and completion/reporting expectations. Let it inspect existing patterns before editing. Preserve local tools and their actual schemas; guide-specific examples such as parallel wrappers, shell tools, or patch functions are not universally available commands. Do not hard-code a guide's sample progress cadence into every coding prompt. Preserve assistant `phase` metadata in API history; instructions alone cannot repair a replay bug.

A Codex harness may run Astra, GPT-5.6, or another model. Use that model's guidance, not automatically the Codex-suffixed model guide.

## Non-reasoning models

GPT-4.1 (including mini/nano) and GPT-4o/mini benefit from explicit task logic, ordered dependencies, representative examples, and a clear output shape. Use procedures when correctness depends on order. The [GPT-4.1 guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) recommends testing instruction placement around long context. Do not suggest reasoning-effort or pro controls for models that lack them; verify older message-role support before giving API examples.

## Specialized targets

These still receive ordinary prompt text. Load the relevant linked guide when the user names the modality; do not apply desktop-agent rules to a voice or image brief.

| Target | Prompting distinction and source |
| --- | --- |
| `gpt-realtime-2.1`, `gpt-realtime-2.1-mini`, earlier Realtime models | Define spoken response length, turn-taking, uncertain audio/identifiers, tool triggers, confirmation boundaries, and recovery. The [Realtime guide](https://developers.openai.com/api/docs/guides/realtime-models-prompting) still describes Realtime 2; confirm version-specific controls on [2.1](https://developers.openai.com/api/docs/models/gpt-realtime-2.1) or [2.1 mini](https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini). Do not assume its effort table transfers unchanged. |
| `gpt-audio-1.5`, `gpt-transcribe`, `gpt-live-transcribe`, and TTS models | Keep spoken instructions distinct from transcription hints and reference transcripts; check the exact model's accepted inputs in the [catalog](https://developers.openai.com/api/docs/models). Earlier Whisper/4o transcription models have announced retirements; consult the lifecycle source above. |
| `gpt-image-2`, earlier GPT Image models | Describe subject, composition, style, exact visible text, and edits versus preserved elements. Inputs and output settings are client configuration. For Image 2, omit `input_fidelity`; it processes inputs at high fidelity. See [image generation](https://developers.openai.com/api/docs/guides/image-generation). |
| `sora-2`, `sora-2-pro` | Deprecated; shutdown scheduled for 2026-09-24. For an explicit existing target, describe a coherent scene, subject action, camera, timing, and audio. See [video generation](https://developers.openai.com/api/docs/guides/video-generation). |
| `o3-deep-research`, `o4-mini-deep-research` | Retired; historical adaptation only. The [old research guide](https://developers.openai.com/api/docs/guides/deep-research) requires a complete brief up front because these API models did not ask clarifying questions. For a new research agent, select a supported model with configured research tools. |
| `gpt-daybreak-blue-latest`, `gpt-daybreak-red-latest`, `gpt-5.6-cyber` | Restricted/provisioned cybersecurity targets. Blue currently points to Sol; Red to Cyber. Preserve the authorized task scope and check access; do not infer availability from a model name. See [Blue](https://developers.openai.com/api/docs/models/gpt-daybreak-blue-latest), [Red](https://developers.openai.com/api/docs/models/gpt-daybreak-red-latest), and [Cyber](https://developers.openai.com/api/docs/models/gpt-5.6-cyber). |

Open-weight `gpt-oss` deployments require their own model/runtime documentation; do not assume OpenAI API controls. Embeddings and moderation endpoints are not conversational prompt targets. Model discovery includes these categories, but Promptify does not configure or invoke them.
