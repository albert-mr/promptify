# Model review — 2026-10-12

Version 3.3 adds Claude Haiku 5.5 and corrects Anthropic thinking-replay and per-message effort claims that changed after the 2026-09-30 review. Discovery covered all three providers. The detailed review covered Haiku 5.5, the shared Anthropic pages it changed, and the GPT-6 model pages. Each page was diffed against its 2026-09-30 capture.

## Findings

| Official sources | Result in Promptify |
| --- | --- |
| Anthropic's [October 7 release notes](https://platform.claude.com/docs/en/release-notes/overview), [catalog](https://platform.claude.com/docs/en/models/overview), [lifecycle table](https://platform.claude.com/docs/en/about-claude/model-deprecations), [Haiku 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5), [what's new](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5), and [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) establish `claude-haiku-5-5` as an active current model. | Added drafting guidance for search grounding, early stopping, real verification, chatbot rule adherence, and the scoped thinking-off JSON/tool line. Separate integration notes cover `medium` default effort, disabled thinking only at `high` or below, empty replies at `xhigh`, rejected prefill/sampling/`budget_tokens`/`computer_20250124`, forced tools that skip thinking, Bedrock's missing Structured Outputs, refusals without fallback, and append-only, account-bound replay. |
| The guide's verification sample also authorizes installing declared dependencies. | Included only when the user allows installs; it must not override a no-new-dependencies or offline constraint. |
| [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), Sonnet 5.5 [what's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5), and its [migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) now say Opus 5.5 reads Sonnet 5.5 and Haiku 5.5 blocks on the Claude API and Google Cloud, and Sonnet 5.5 reads Haiku 5.5 blocks there. | Replaced the stale "no other model reads Sonnet 5.5 blocks" claim and updated the Opus 5.5 compatibility note. |
| The Sonnet 5.5 migration guide now says Structured Outputs are unavailable for Sonnet 5.5 on Amazon Bedrock. | Added to the Sonnet 5.5 integration note. |
| [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) lists per-message effort for Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, and Haiku 5.5 on the Claude API and Google Cloud, and only Fable 5.1 and Opus 5.5 on Amazon Bedrock. | Replaced the "verify platform support" hedge with the documented lists. Haiku 5.5 with thinking disabled cannot change effort mid-conversation. |
| OpenAI's [October changelog](https://developers.openai.com/api/docs/changelog) adds the beta [Decisions API](https://developers.openai.com/api/docs/guides/decisions) (`gpt-6-luna` only), Ultrafast mode for GPT-6.1 Sol, a `chat-latest` refresh, and three usage tiers. GPT-6 model-page and guide diffs cover only rate tiers and Fast/Ultrafast data residency. | No new text-model target or prompting change. Decisions takes typed questions rather than a prompt, so an explicit Decisions destination is reported as unsupported instead of drafted as a Luna prompt. |
| The TypeSafe [index](https://docs.typesafe.ai/llms.txt) and [model page](https://docs.typesafe.ai/models) still list only `jev-1.13.0`. | No change. |

## Pruned coverage

Agents typically read the whole provider reference for any Anthropic or OpenAI target, so superseded sections cost context on every draft. This review removed them:

| Removed | Evidence | Fallback |
| --- | --- | --- |
| Claude Opus 5 and Sonnet 5 | The [catalog](https://platform.claude.com/docs/en/models/overview) lists both as legacy; Opus 5.5 and Sonnet 5.5 succeed them. | General guidance with disclosure. Newer models' API rules are not transferred, so integration notes need live verification. |
| GPT-5.6 Sol, Terra, Luna | The [catalog](https://developers.openai.com/api/docs/models) features only GPT-6 models, and OpenAI recommends the GPT-6 family for production. | Same. |

GPT-6 Sol is retained. It belongs to the current generation, was released 2026-09-22, and shares its integration paragraph with Luna, so removing it would save little context. Its section also keeps the documented `none` and sampling differences from 6.1 Sol explicit. Together with the Haiku 5.5 addition, the Anthropic reference shrank from 3,086 to about 2,680 words and the OpenAI reference from 1,176 to about 980. N4 and N8 now test legacy targets: each keeps its name with a coverage disclosure and no silent upgrade. A4, A6, A7, B1, B2, and C7 were retargeted to maintained models.

## Scope and source limitations

- The catalog lists Fable 5 as legacy. It remains outside maintained coverage. Haiku 4.5 also remains outside coverage, so explicit Haiku 4.5 requests keep the general-guidance disclosure.
- The Decisions API has the same three question shapes as Jev, but its fields and beta status differ. Native Decisions authoring would expand the output contract. It is left for a separate decision, preferably after the API reaches GA.
- Haiku 5.5 guidance comes from Anthropic's documented testing. Promptify did not measure it.
- Sources were fetched as Markdown directly from official docs and diffed against the 2026-09-30 captures. Captures and drafting outputs are in the workspace's ignored `.context/review-1012/` directory. Other model guidance keeps its earlier review date. This is not a complete re-audit of every historical claim.

## Validation

The [scenario suite](../tests/scenarios.md) adds N9 for Haiku 5.5's search, policy-adherence, and API differences, and N10 for the corrected Sonnet 5.5 replay compatibility. Fresh evaluator sessions drafted N9, N10, N7, D1, and an explicit Decisions API probe offline from bundled guidance.

N10, N7, D1, and the probe passed. The first N9 sample recommended `low` effort for a policy-critical chatbot because the reference omitted the guide's `high` recommendation for strict system-prompt adherence. The second sample told the user to fill the date placeholder on every request; the guide renders it once per conversation, because changing `system` breaks thinking replay. Both rules were added to the reference and to the N9 criteria. A third fresh N9 sample passed.

No baseline samples were run on `main`; the gaps were established from source diffs (no Haiku 5.5 section and an explicitly contradicted replay claim). Samples are fresh-session drafting simulations, self-graded, not a statistical reliability test. No target-model inference, provider endpoint integration, installed-plugin update, or drafted task was executed.

`python3 scripts/validate.py` and `git diff --check` passed. The skill entrypoint and executable validator are unchanged.
