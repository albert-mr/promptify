# Model review — 2026-09-30

Version 3.2 adds GPT-6.1 Sol and Claude Sonnet 5.5. Existing explicit model destinations remain supported. Discovery covered all three providers; the detailed guidance review focused on the two additions and the shared pages they change.

## Findings

| Official sources | Result in Promptify |
| --- | --- |
| OpenAI's [catalog](https://developers.openai.com/api/docs/models), [September 29 release notes](https://developers.openai.com/api/docs/changelog), [GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol), and [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model) add GPT-6.1 Sol. It supports `low` through `max` effort, not `none` or `minimal`; tool calling requires Responses; Chat Completions works without tools. | Added the exact ID and grouped its integration rules with Astra's. GPT-6 Sol retains its own `none`, sampling, and Chat Completions function-calling rules. The three Sol models are distinct targets. |
| The [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) and [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) model pages still match the existing effort and endpoint rules. The [GPT-6 Sol page](https://developers.openai.com/api/docs/models/gpt-6-sol) points to 6.1 Sol as the newer Sol model; the GPT-6 guide's family list now names Astra, 6.1 Sol, and Luna. [Deprecations](https://developers.openai.com/api/docs/deprecations) list no GPT-6 Sol retirement. | Retained GPT-6 Sol for explicit requests. |
| The [Multi-agent guide](https://developers.openai.com/api/docs/guides/responses-multi-agent) documents its beta for GPT-6.1 Sol and all GPT-5.6 models. | Recorded as client configuration; the existing delegation bullet already avoids assuming harness support. |
| Anthropic's [catalog](https://platform.claude.com/docs/en/models/overview), [September 28 release notes](https://platform.claude.com/docs/en/release-notes/overview), [Sonnet 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5), [what's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5), and [migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) establish Sonnet 5.5. | Added drafting guidance for scope, check-ins, unrequested additions, real verification, search, reasoning-heavy JSON, reasoning-extraction refusals, and progress updates. Separate integration notes cover recalibrated effort, `between_tools`, rejected forced tools/prefill/sampling, model- and account-bound replay, computer-use toolsets, advisor pairings, and mid-turn user input placement. |
| Anthropic's [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking), and [preserved-thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) pages cover Sonnet 5.5. | Added Sonnet 5.5 to per-message effort coverage, excluding `between_tools`. |
| The catalog now lists Sonnet 5 as legacy; the [lifecycle table](https://platform.claude.com/docs/en/about-claude/model-deprecations) still marks it active. | Retained Sonnet 5 guidance for explicit requests with the same note used for Opus 5. |
| The TypeSafe [index](https://docs.typesafe.ai/llms.txt) and [model page](https://docs.typesafe.ai/models) still list `jev-1.13.0`, with both aliases resolving to it. | No change. |

## Scope and source limitations

- Other OpenAI changes since the last review (Astra Ultrafast mode, Agents API computer use) are service or harness configuration, not new text-model targets or prompt guidance. Specialized and restricted models remain outside maintained coverage.
- OpenAI's GPT-6 guide lists multi-agent orchestration among capabilities GPT-6 inherits from GPT-5.6, while the Multi-agent guide names only GPT-6.1 Sol and GPT-5.6 for the beta. Promptify does not assert Multi-agent support for Astra, GPT-6 Sol, or Luna.
- GPT-6 prompting patterns remain documented as Astra-derived starting points for the family, not measured identical behavior on 6.1 Sol.
- Sonnet 5.5's documented "Think the problem through before you answer." line is a scoped exception for reasoning-heavy JSON with adaptive thinking; it prompts internal thinking, not visible reasoning, and does not relax the general rule against step-by-step scaffolding.
- Sources were fetched as Markdown directly from official docs. Captures and drafting outputs are in the workspace's ignored `.context/review-0930/` directory. The whole GPT-6 family was rechecked against its guide and all four model pages; its integration paragraphs were clarified, not changed in substance. GPT-5.6, Fable 5.1, Opus 5.5, Opus 5, and Sonnet 5 guidance retains its earlier review date except where noted above; this is not a complete re-audit of every historical claim.

## Validation

Before editing, offline baseline samples for N6 and N7 on `main` disclosed missing exact-model coverage honestly but could not give the new API differences, and the evaluator noted the old wording left room to transfer GPT-6 Sol or Opus 5.5 rules. This established the reference gap.

The [scenario suite](../tests/scenarios.md) adds N6–N8 for GPT-6.1 Sol's break from GPT-6 Sol, Sonnet 5.5's thinking/tool/progress changes, and explicit Sonnet 5 routing. All 12 selected revised samples passed: N6–N8, N1–N3, B6, A7, C6, J1, A9, and C5. A9 and C5 fetched live official discovery, lifecycle, and exact-model pages; the rest used bundled guidance offline.

Evaluator flags led to clarifications: explicit log-probability parameters, unambiguous GPT-6 Sol built-in-tool routing, self-contained Sonnet 5.5 replay and rendering notes, existing checks versus unrequested tests, scoped use of the documented "think" line, and per-message effort moved to shared integration guidance. A focused recheck of C4, N3, N6, N7, and two Sonnet 5.5 prompt-only probes (multi-step JSON and a short rewrite) passed.

Remaining evaluator flags concern pre-existing workflow questions outside this model update: placement of requested notes relative to the single copyable block, a tie-break for "latest" when provider docs name different flagship, newest, and most capable models, target-line wording when "latest" cannot be verified, browsing defaults when a request is silent, and unspecified output field types.

Samples came from fresh evaluator sessions with logically separate cases, not isolated provider sessions or a statistical reliability test; the recheck was self-graded. Full outputs were inspected. No target-model inference, provider endpoint integration, installed-plugin update, or drafted task was executed.

`python3 scripts/validate.py` and `git diff --check` passed. The skill entrypoint and executable validator are unchanged.
