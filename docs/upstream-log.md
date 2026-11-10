# Upstream review log

Newest first. Entries describe the releases they were written for and are not runtime guidance.

## Fable 5.2 follow-up — 2026-11-10

A second read of the Fable 5.2 prompting guide against the shipped reference found items the 3.6.0 rewrite left out: subagent tool descriptions, built-up cautions, reply length, refusal categories and fallback, and the guide's note that prompt changes go into new conversations only. The line on inherited delegation and token-budget text was stronger than the guide, which says to test without them, and was reworded. The guide, the what's-new page, and the Mythos 5.2 overview describe Mythos 5.2 as the same model for verified organizations, so `claude-mythos-5-2` now routes to the Fable 5.2 section instead of general guidance. No model newer than Fable 5.2 exists in the catalog or the 2026-11-09 release notes.

Anthropic's [model-choice post](https://claude.dev/blog/which-claude-model-should-you-build-with/) (2026-11-09) was read in full. Only its rule for prompts shared across models was adopted. Its prices, benchmark figures, and harness settings were left out, and the which-model answer cites the [choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) docs page instead. The blog is not watched by `scripts/check_upstream.py`. The `anthropics/claude-cookbooks` repository had no Fable 5.2 commit (latest 2026-11-04). Read in part only: the migration guide (headings) and the refusals-and-fallback page (the fallback sentence came from the what's-new page).

## Guide review — 2026-11-10

Anthropic launched Claude Fable 5.2 on 2026-11-09, after that day's discovery check, and moved Fable 5.1 to legacy. The Fable section was rewritten from the Fable 5.2 prompting guide, what's-new page, and migration guide. The Opus 5.5, Sonnet 5.5, Haiku 5.5, Claude best-practices, GPT-6, and OpenAI prompt-engineering guides were each read in full, and only additions likely to change a drafted prompt were applied; lower-value items were left out to limit the context loaded per draft. Not reread: what's-new and migration pages other than Fable 5.2's, and TypeSafe docs beyond the 2026-11-09 check.

A blind comparison on 10 scenarios, three runs each and graded by Opus, preferred the skill's output over a bare Sonnet 5.5 in 29 of 30 pairs. The skill met the scenario criteria in 26 pairs and the bare model in 12. Those criteria were written for this skill, so the result favors it, and the bare model had no access to current provider docs.

## Discovery check — 2026-11-09

No new in-scope models. OpenAI released GPT-6-Cyber (2026-11-05), which needs Daybreak Red access and stays outside maintained coverage, along with image and voice updates. GPT-6.1 Sol's catalog entry and GPT-6 Sol's page ("the newer Sol model") led to removing the GPT-6 Sol section under the successor rule. Anthropic's catalog and lifecycle tables list the same four maintained models; message threads (2026-11-02, beta) are integration-only and not added. TypeSafe has no release after Jev 1.14, but its context limits, long-context header, and `jev-preview` alias were missing and were added. This check compared section headings of the four Claude prompting guides and read selected sections; it was not a full reread.

## Discovery check — 2026-11-04

No new in-scope models. OpenAI released GPT-6 Rosalind (2026-10-30), a restricted life-sciences model available only through a trusted-access program; it stays outside maintained coverage. The OpenAI catalog page now lists only current models. Anthropic's catalog and lifecycle tables are unchanged. TypeSafe published a general [model jaggedness](https://docs.typesafe.ai/model-jaggedness) page and a [model changelog](https://docs.typesafe.ai/changelog) with no release after Jev 1.14, so the reference links were updated.

## Model review — 2026-10-12

Version 3.3 adds Claude Haiku 5.5 and corrects Anthropic thinking-replay and per-message effort claims that changed after the 2026-09-30 review. Discovery covered all three providers. The detailed review covered Haiku 5.5, the shared Anthropic pages it changed, and the GPT-6 model pages. Each page was diffed against its 2026-09-30 capture.

### Findings

| Official sources | Result in Promptify |
| --- | --- |
| Anthropic's [October 7 release notes](https://platform.claude.com/docs/en/release-notes/overview), [catalog](https://platform.claude.com/docs/en/models/overview), [lifecycle table](https://platform.claude.com/docs/en/about-claude/model-deprecations), [Haiku 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5), [what's new](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5), and [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) establish `claude-haiku-5-5` as an active current model. | Added drafting guidance for search grounding, early stopping, real verification, chatbot rule adherence, and the scoped thinking-off JSON/tool line. Separate integration notes cover `medium` default effort, disabled thinking only at `high` or below, empty replies at `xhigh`, rejected prefill/sampling/`budget_tokens`/`computer_20250124`, forced tools that skip thinking, Bedrock's missing Structured Outputs, refusals without fallback, and append-only, account-bound replay. |
| The guide's verification sample also authorizes installing declared dependencies. | Included only when the user allows installs; it must not override a no-new-dependencies or offline constraint. |
| [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), Sonnet 5.5 [what's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5), and its [migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) now say Opus 5.5 reads Sonnet 5.5 and Haiku 5.5 blocks on the Claude API and Google Cloud, and Sonnet 5.5 reads Haiku 5.5 blocks there. | Replaced the stale "no other model reads Sonnet 5.5 blocks" claim and updated the Opus 5.5 compatibility note. |
| [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) lists per-message effort for Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, and Haiku 5.5 on the Claude API and Google Cloud, and only Fable 5.1 and Opus 5.5 on Amazon Bedrock. | Replaced the "verify platform support" hedge with the documented lists. Haiku 5.5 with thinking disabled cannot change effort mid-conversation. |
| OpenAI's [October changelog](https://developers.openai.com/api/docs/changelog) adds the beta [Decisions API](https://developers.openai.com/api/docs/guides/decisions) (`gpt-6-luna` only), Ultrafast mode for GPT-6.1 Sol, a `chat-latest` refresh, and three usage tiers. GPT-6 model-page and guide diffs cover only rate tiers and Fast/Ultrafast data residency. | No new text-model target or prompting change. Decisions takes typed questions rather than a prompt, so an explicit Decisions destination is reported as unsupported instead of drafted as a Luna prompt. |
| The TypeSafe [index](https://docs.typesafe.ai/llms.txt) and [model page](https://docs.typesafe.ai/models) still list only `jev-1.13.0`. | No change. |

### Pruned coverage

Agents typically read the whole provider reference for any Anthropic or OpenAI target, so superseded sections cost context on every draft. This review removed them:

| Removed | Evidence | Fallback |
| --- | --- | --- |
| Claude Opus 5 and Sonnet 5 | The [catalog](https://platform.claude.com/docs/en/models/overview) lists both as legacy; Opus 5.5 and Sonnet 5.5 succeed them. | General guidance with disclosure. Newer models' API rules are not transferred, so integration notes need live verification. |
| GPT-5.6 Sol, Terra, Luna | The [catalog](https://developers.openai.com/api/docs/models) features only GPT-6 models, and OpenAI recommends the GPT-6 family for production. | Same. |

GPT-6 Sol is retained. It belongs to the current generation, was released 2026-09-22, and shares its integration paragraph with Luna, so removing it would save little context. Its section also keeps the documented `none` and sampling differences from 6.1 Sol explicit. Together with the Haiku 5.5 addition, the Anthropic reference shrank from 3,086 to about 2,680 words and the OpenAI reference from 1,176 to about 980. N4 and N8 now test legacy targets: each keeps its name with a coverage disclosure and no silent upgrade. A4, A6, A7, B1, B2, and C7 were retargeted to maintained models.

### Scope and source limitations

- The catalog lists Fable 5 as legacy. It remains outside maintained coverage. Haiku 4.5 also remains outside coverage, so explicit Haiku 4.5 requests keep the general-guidance disclosure.
- The Decisions API has the same three question shapes as Jev, but its fields and beta status differ. Native Decisions authoring would expand the output contract. It is left for a separate decision, preferably after the API reaches GA.
- Haiku 5.5 guidance comes from Anthropic's documented testing. Promptify did not measure it.
- Sources were fetched as Markdown directly from official docs and diffed against the 2026-09-30 captures. Captures and drafting outputs are in the workspace's ignored `.context/review-1012/` directory. Other model guidance keeps its earlier review date. This is not a complete re-audit of every historical claim.

### Validation

The [scenario suite](../tests/scenarios.md) adds N9 for Haiku 5.5's search, policy-adherence, and API differences, and N10 for the corrected Sonnet 5.5 replay compatibility. Fresh evaluator sessions drafted N9, N10, N7, D1, and an explicit Decisions API probe offline from bundled guidance.

N10, N7, D1, and the probe passed. The first N9 sample recommended `low` effort for a policy-critical chatbot because the reference omitted the guide's `high` recommendation for strict system-prompt adherence. The second sample told the user to fill the date placeholder on every request; the guide renders it once per conversation, because changing `system` breaks thinking replay. Both rules were added to the reference and to the N9 criteria. A third fresh N9 sample passed.

No baseline samples were run on `main`; the gaps were established from source diffs (no Haiku 5.5 section and an explicitly contradicted replay claim). Samples are fresh-session drafting simulations, self-graded, not a statistical reliability test. No target-model inference, provider endpoint integration, installed-plugin update, or drafted task was executed.

`python3 scripts/validate.py` and `git diff --check` passed. The skill entrypoint and executable validator are unchanged.

### Follow-up check — 2026-10-20

The PR was still open, so discovery was rerun and folded into 3.3.0.

| Official sources | Result in Promptify |
| --- | --- |
| TypeSafe's [models](https://docs.typesafe.ai/models) page adds `jev-1.14.0` (2026-10-14) as `jev-preview`; `jev-latest` still points to `jev-1.13.0`. | `jev-1.13.0` stays the stable default. 1.14.0 is used only when requested or for Box. |
| New [Images](https://docs.typesafe.ai/images) and [Box](https://docs.typesafe.ai/primitives/box) pages: images work on 1.13 and 1.14 through a top-level `assets` map and the `TypeSafe-Danger-Zone-Images` header. Box needs 1.14. TypeSafe calls both not ready for production. | Replaced "never pretend Jev sees an image" with opt-in image and Box guidance and a prototype disclosure. The header goes in integration notes, not JSON. |
| The Haiku 5.5 [what's new](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5) and [migration](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) pages and the Sonnet 5.5 [migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) dropped their caveats that Structured Outputs were unavailable on Amazon Bedrock; [Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) lists Bedrock as GA. | Removed both caveats added earlier in this review. |
| Anthropic [release notes](https://platform.claude.com/docs/en/release-notes/overview) since October 9 cover Opus 5.5 fast mode GA, a Models API `between_tools` capability, OpenTelemetry, and compliance. OpenAI's [changelog](https://developers.openai.com/api/docs/changelog) since October 8 covers GPT-Live voices and Decisions in GPT-Live. Prompting guides for Haiku 5.5, Sonnet 5.5, and GPT-6 are unchanged. | No new text model or prompting change. Decisions remains beta and unsupported. |

J13 tests the Box/preview path.

## Model review — 2026-09-30

Version 3.2 adds GPT-6.1 Sol and Claude Sonnet 5.5. Existing explicit model destinations remain supported. Discovery covered all three providers; the detailed guidance review focused on the two additions and the shared pages they change.

### Findings

| Official sources | Result in Promptify |
| --- | --- |
| OpenAI's [catalog](https://developers.openai.com/api/docs/models), [September 29 release notes](https://developers.openai.com/api/docs/changelog), [GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol), and [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model) add GPT-6.1 Sol. It supports `low` through `max` effort, not `none` or `minimal`; tool calling requires Responses; Chat Completions works without tools. | Added the exact ID and grouped its integration rules with Astra's. GPT-6 Sol retains its own `none`, sampling, and Chat Completions function-calling rules. The three Sol models are distinct targets. |
| The [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) and [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) model pages still match the existing effort and endpoint rules. The [GPT-6 Sol page](https://developers.openai.com/api/docs/models/gpt-6-sol) points to 6.1 Sol as the newer Sol model; the GPT-6 guide's family list now names Astra, 6.1 Sol, and Luna. [Deprecations](https://developers.openai.com/api/docs/deprecations) list no GPT-6 Sol retirement. | Retained GPT-6 Sol for explicit requests. |
| The [Multi-agent guide](https://developers.openai.com/api/docs/guides/responses-multi-agent) documents its beta for GPT-6.1 Sol and all GPT-5.6 models. | Recorded as client configuration; the existing delegation bullet already avoids assuming harness support. |
| Anthropic's [catalog](https://platform.claude.com/docs/en/models/overview), [September 28 release notes](https://platform.claude.com/docs/en/release-notes/overview), [Sonnet 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5), [what's new](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5), and [migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) establish Sonnet 5.5. | Added drafting guidance for scope, check-ins, unrequested additions, real verification, search, reasoning-heavy JSON, reasoning-extraction refusals, and progress updates. Separate integration notes cover recalibrated effort, `between_tools`, rejected forced tools/prefill/sampling, model- and account-bound replay, computer-use toolsets, advisor pairings, and mid-turn user input placement. |
| Anthropic's [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking), and [preserved-thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) pages cover Sonnet 5.5. | Added Sonnet 5.5 to per-message effort coverage, excluding `between_tools`. |
| The catalog now lists Sonnet 5 as legacy; the [lifecycle table](https://platform.claude.com/docs/en/about-claude/model-deprecations) still marks it active. | Retained Sonnet 5 guidance for explicit requests with the same note used for Opus 5. |
| The TypeSafe [index](https://docs.typesafe.ai/llms.txt) and [model page](https://docs.typesafe.ai/models) still list `jev-1.13.0`, with both aliases resolving to it. | No change. |

### Scope and source limitations

- Other OpenAI changes since the last review (Astra Ultrafast mode, Agents API computer use) are service or harness configuration, not new text-model targets or prompt guidance. Specialized and restricted models remain outside maintained coverage.
- OpenAI's GPT-6 guide lists multi-agent orchestration among capabilities GPT-6 inherits from GPT-5.6, while the Multi-agent guide names only GPT-6.1 Sol and GPT-5.6 for the beta. Promptify does not assert Multi-agent support for Astra, GPT-6 Sol, or Luna.
- GPT-6 prompting patterns remain documented as Astra-derived starting points for the family, not measured identical behavior on 6.1 Sol.
- Sonnet 5.5's documented "Think the problem through before you answer." line is a scoped exception for reasoning-heavy JSON with adaptive thinking; it prompts internal thinking, not visible reasoning, and does not relax the general rule against step-by-step scaffolding.
- Sources were fetched as Markdown directly from official docs. Captures and drafting outputs are in the workspace's ignored `.context/review-0930/` directory. The whole GPT-6 family was rechecked against its guide and all four model pages; its integration paragraphs were clarified, not changed in substance. GPT-5.6, Fable 5.1, Opus 5.5, Opus 5, and Sonnet 5 guidance retains its earlier review date except where noted above; this is not a complete re-audit of every historical claim.

### Validation

Before editing, offline baseline samples for N6 and N7 on `main` disclosed missing exact-model coverage honestly but could not give the new API differences, and the evaluator noted the old wording left room to transfer GPT-6 Sol or Opus 5.5 rules. This established the reference gap.

The [scenario suite](../tests/scenarios.md) adds N6–N8 for GPT-6.1 Sol's break from GPT-6 Sol, Sonnet 5.5's thinking/tool/progress changes, and explicit Sonnet 5 routing. All 12 selected revised samples passed: N6–N8, N1–N3, B6, A7, C6, J1, A9, and C5. A9 and C5 fetched live official discovery, lifecycle, and exact-model pages; the rest used bundled guidance offline.

Evaluator flags led to clarifications: explicit log-probability parameters, unambiguous GPT-6 Sol built-in-tool routing, self-contained Sonnet 5.5 replay and rendering notes, existing checks versus unrequested tests, scoped use of the documented "think" line, and per-message effort moved to shared integration guidance. A focused recheck of C4, N3, N6, N7, and two Sonnet 5.5 prompt-only probes (multi-step JSON and a short rewrite) passed.

Remaining evaluator flags concern pre-existing workflow questions outside this model update: placement of requested notes relative to the single copyable block, a tie-break for "latest" when provider docs name different flagship, newest, and most capable models, target-line wording when "latest" cannot be verified, browsing defaults when a request is silent, and unspecified output field types.

Samples came from fresh evaluator sessions with logically separate cases, not isolated provider sessions or a statistical reliability test; the recheck was self-graded. Full outputs were inspected. No target-model inference, provider endpoint integration, installed-plugin update, or drafted task was executed.

`python3 scripts/validate.py` and `git diff --check` passed. The skill entrypoint and executable validator are unchanged.

## Model review — 2026-09-27

Version 3.1 adds GPT-6 Sol, GPT-6 Luna, and Claude Opus 5.5. Existing explicit model destinations remain supported. Discovery covered all three providers; the detailed guidance review focused on these additions and the shared GPT-6 guide.

### Findings

| Official sources | Result in Promptify |
| --- | --- |
| OpenAI's [catalog](https://developers.openai.com/api/docs/models) and [September 22 release notes](https://developers.openai.com/api/docs/changelog) list GPT-6 Sol and Luna. Their [model](https://developers.openai.com/api/docs/models/gpt-6-sol) [pages](https://developers.openai.com/api/docs/models/gpt-6-luna) and the [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model) specify their API differences. | Added both exact IDs, shared family prompting, and separate integration rules: `none` supports sampling and Chat Completions function calling; reasoning with tools requires Responses. Astra's restrictions remain specific to Astra. |
| OpenAI's [September 25 fix](https://developers.openai.com/api/docs/changelog) addresses Sol/Luna image encoding. | Recommend rerunning affected image-input evaluations when advising existing integrations; no prompt workaround. |
| Anthropic's [catalog](https://platform.claude.com/docs/en/models/overview), [September 22 release notes](https://platform.claude.com/docs/en/release-notes/overview), [Opus 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5), and [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) establish the new model. | Added targeted drafting guidance and separate notes for always-on thinking, effort, forced tools, replay, computer-use toolsets, and progress display. |
| Anthropic's [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking), and [preserved-thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) pages cover Opus 5.5. | Updated per-message effort coverage and kept display and history controls in client configuration. |
| The TypeSafe [index](https://docs.typesafe.ai/llms.txt) and [model page](https://docs.typesafe.ai/models) still list `jev-1.13.0`, with both aliases currently resolving to it. | No model change. Retained the dated selection and live-verification rule for aliases; the request-authoring reference keeps its September 21 review date. |

### Scope and source limitations

- Checked both providers' discovery, prompting indexes, release notes, and lifecycle pages: [OpenAI deprecations](https://developers.openai.com/api/docs/deprecations), [Claude deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations). No new retirement affects maintained targets. Specialized and restricted models remain outside maintained coverage.
- OpenAI's catalog introduction still recommends GPT-5.6 Terra/Luna while its full catalog and current family guide include GPT-6 Sol/Luna. Exact model pages and dated release notes establish the additions; namesakes are not aliases.
- Anthropic's catalog calls Opus 5 legacy, while its lifecycle table still marks it active. Preserve explicit Opus 5 requests; neither description means it is retired.
- GPT-6 prompting patterns are documented as Astra-derived starting points for the family, not measured identical behavior on Sol and Luna. Platform support and API compatibility still require verification for an actual integration.
- Markdown sources were fetched directly after the browser reader rejected their content type. Captures and drafting outputs are in the workspace's ignored `.context/model-review/` directory. Unchanged GPT-5.6, Fable 5.1, Opus 5, and Sonnet 5 guidance retains its September 14 review date; this is not a complete re-audit of every historical claim.

### Validation

Before editing, three offline drafting samples correctly disclosed missing exact-model coverage for the new targets, leaving their API questions unresolved. This established the reference gap without treating the existing safe fallback as a defect.

The [scenario suite](../tests/scenarios.md) adds N1–N5 for the new integration differences, explicit older-model routing, and ordinary Opus 5.5 prompt output. All 12 selected drafting samples passed: N1–N5, A2, A8, B2, B3, J1, A9, and C5. Ten used bundled guidance offline; A9 and C5 fetched live official discovery, lifecycle, and exact-model pages. Older-model requests retained their targets, unknown/offline requests disclosed uncertainty, and Jev retained its native template contract.

The revised samples came from one fresh evaluator session with logically separate cases, not 12 isolated provider sessions or a statistical reliability test. Full outputs were inspected. No target-model inference, provider endpoint integration, installed-plugin update, or drafted task was executed.

`python3 scripts/validate.py` and `git diff --check` passed. The skill entrypoint and executable validator are unchanged.

## Upstream review — 2026-09-14

> This report records the version 2.1.0 audit. Version 2.1.1 subsequently narrows maintained guidance to seven text models; see the [current model list](../README.md#model-coverage). The source findings and validation results below describe the earlier audit, not the current coverage.

Version 2.1 refreshes both providers after the September 7 review. Normal prompts remain the only output mode. Research compared fresh official catalogs, release notes, lifecycle pages, prompting guides, and migration docs with the previous captures, then followed published links for new models. Saved sources, diffs, and drafting evaluations live in this workspace's ignored `.context/` directory.

### Findings and changes

| Official source finding | Result in Promptify |
| --- | --- |
| OpenAI's [September release notes](https://developers.openai.com/api/docs/changelog) add GPT Image 2.5 Sunburst/Flare on September 8 and GPT-Live 1 on September 10. [Astra's guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra) remains the flagship guide; its prompting advice and the GPT-5.6 guides are unchanged. | Retained mainline guidance and added separate sections for the new image and voice targets. |
| [GPT-Live prompting](https://developers.openai.com/api/docs/guides/live-prompting) separates conversation from backend reasoning/tools. [Delegation](https://developers.openai.com/api/docs/guides/live-delegation) distinguishes speech interruption, task cancellation, and confirmed results. | Added short policy sections, concrete handoff conditions, and separate application responsibilities. A voice prompt does not create frontend functions or cancel backend work. |
| [Image 2.5 prompting](https://developers.openai.com/api/docs/guides/image-prompting) covers reference roles, exact text, preservation across edits, and quality/latency evaluation. [Image generation](https://developers.openai.com/api/docs/guides/image-generation) selects the image model inside the Responses image tool. | Added Sunburst/Flare guidance and the correct API boundary. Pixel-identical preservation requires compositing; transparency requires an actual alpha channel. |
| The old Realtime prompting URL returns 404. The [current Realtime entry page](https://developers.openai.com/api/docs/guides/realtime) links to [voice prompting](https://developers.openai.com/api/docs/guides/voice-prompting). | Repaired the maintained reference. The guide still centers Realtime 2/1.5, so 2.1-specific settings remain subject to exact-model verification. |
| [Rosalind](https://help.openai.com/en/articles/20001193-gpt-rosalind-for-life-sciences-research) has trusted access for approved internal research. Large datasets belong in accessible storage for focused analysis. | Added a research brief route without implying general access, provisioned tools, or customer-facing deployment. |
| [Deprecations](https://developers.openai.com/api/docs/deprecations) now schedule GPT-5.4-Cyber shutdown for October 1. Existing Sora and older-image deadlines still apply. | Added the new cyber notice and explicit older-image dates. Catalog presence does not prove availability. |
| Anthropic's [model overview](https://platform.claude.com/docs/en/models/overview), lifecycle table, shared prompting page, and five dedicated prompting guides are unchanged from September 7. | Retained Fable/Mythos 5.1, Opus 5, Sonnet 5, Haiku 4.5, and earlier-model guidance. There is no new Claude model release to invent. |
| [Fable 5.1's updated notes](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) document per-message effort on Google Cloud too; [migration guidance](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) corrects token-count equivalence to tokenizer equivalence. | Added concise integration guidance for supported models and clarified that unchanged tokenization does not imply unchanged usage. Google Cloud support is recorded under September 3 in the release notes, not a new September 14 launch. |
| [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) has an older-account opt-in for prefix binding. [Claude Code hooks](https://code.claude.com/docs/en/hooks) distinguish pending and completed model switches. | Clarified both existing edge cases; neither is presented as newly introduced behavior. Aliases remain dependent on provider, account, and harness version. |
| The [Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) is a managed Codex harness. Anthropic's [September 10 release notes](https://platform.claude.com/docs/en/release-notes/overview) add Managed Agents controls. | Clarified the OpenAI harness/model distinction. Runtime provisioning and permission configuration stay outside ordinary prompts. |

### Source limitations

- The image guide's `input_fidelity` omission rule explicitly names Image 2. The reviewed Image 2.5 prompting/model pages do not establish that setting's compatibility; the reference avoids transferring the older rule. Its confirmed model, quality, transparency, and Responses routing guidance remains usable.
- Some examples and lifecycle replacement recommendations still name older models. Follow the exact model's current guide and validate the intended workflow instead of globally replacing every historical example.
- Claude Code and Codex configuration changes were checked for effects on discovery and installation. Existing packaging remains compatible; no hooks, model settings, credentials, or installed plugins were changed.
- These sources describe provider behavior as of this review. They are not substitutes for live verification on a later "latest" request, or tests in the destination application.

### Validation

Before editing, two independent offline drafting simulations exposed missing GPT-Live and Image 2.5 coverage. The image case correctly declined to invent Responses model placement from the old bundle. The voice case preserved the request but lacked Live-specific handoff guidance.

The [scenario suite](../tests/scenarios.md) now contains 26 cases, including eight additions for this refresh. Results:

- All 17 selected drafting samples met their rubrics: C1–C8 plus nine existing cross-provider, unknown-target, normal-mode, API, and voice cases. Two independent evaluators treated cases as separate logical invocations; these were not 17 isolated provider sessions or a statistical reliability measurement.
- Both providers' online "latest" cases fetched fresh official discovery, lifecycle, and exact-model pages. Offline cases disclosed that latest-model identity could not be verified. The Claude JSON/API case also retrieved current integration docs.
- The Haiku classifier case preserves its requested three-label contract, but routing wholly empty or irrelevant input remains unspecified application policy. A destination application must supply that policy; a passing drafting rubric does not settle it.
- `python3 scripts/validate.py`, the skill-authoring frontmatter validator, and Git whitespace checks passed. The normal-prompt entrypoint and executable validator were not changed in this refresh.
- All 66 official URLs linked by the current README, maintenance guide, references, and this review returned content: 65 Markdown pages and Rosalind's HTML article. Claim review was separate from this reachability check. The superseded 404 remains recorded in the research evidence and historical September 7 report.
- Independent final source/content review found no actionable issues. No destination model, image generation, installed plugin, or provider integration was exercised.

## Upstream review — 2026-09-07

Version 2 updates Promptify's drafting contract and refreshes its OpenAI/Anthropic guidance. Research used official provider documentation, including model catalogs, prompting guides, migrations, lifecycle notices, and installation docs. Linked references contain the maintained source inventory; temporary fetched pages and behavioral outputs are in the workspace's ignored `.context/` directory.

### Decisions from the source review

| Finding | Result in Promptify |
| --- | --- |
| [OpenAI's current guide](https://developers.openai.com/api/docs/guides/latest-model) now describes GPT-6 Astra. | Added Astra guidance for autonomy, instruction conflicts, writing style, delegation, proportional testing, and the tool-calling/parameter migration boundary. GPT-5.6 points to its own stable guide. |
| [GPT-5.6's prompting guide](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6) emphasizes concise outcome/evidence contracts and conditional tool routing. | Removed the old claim that GPT prompting should be broadly verbose or the opposite of o-series. Preserved the user's explicit requirements, examples that serve a purpose, and runtime configuration separation. |
| [Claude's shared guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) now routes to Fable 5.1 in addition to earlier dedicated guides. | Added Fable/Mythos 5.1; removed the fixed count of model-specific guides. Kept Opus, Sonnet, Fable, and Haiku differences separate. |
| [Fable 5.1 migration](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) has actual client compatibility changes. | Recorded unsupported forced tool choices, thinking-history preservation/binding, and progress display. A prompt cannot repair missing runtime support. Mythos is not assumed to share Fable's prefix enforcement. |
| [Opus 5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) discourages inherited self-verification rituals. | Remove redundant checks while retaining checks explicitly requested by the user. Do not turn a performance recommendation into permission to skip validation. |
| [Haiku 4.5 remains in the current lineup](https://platform.claude.com/docs/en/models/overview). | Removed its misleading placement as a legacy default; preserved its extended-thinking distinction. |
| [OpenAI's catalog](https://developers.openai.com/api/docs/models) includes Realtime 2.1/mini, Image 2, new transcription models, and restricted Daybreak/Cyber targets. | Added specialized routing without importing unrelated text-agent settings or implying access. Embeddings/moderation are not conversational prompt targets. |
| [OpenAI lifecycle notices](https://developers.openai.com/api/docs/deprecations) disagree with the apparent freshness of several still-published guides/catalog entries. | Marked retired coding/research targets, retired chat aliases, and Sora's scheduled 2026-09-24 shutdown. Availability comes from lifecycle/model docs, not catalog presence. |
| [Claude Code hooks](https://code.claude.com/docs/en/hooks#sessionstart-input) can include an active `model`, and [Codex config](https://learn.chatgpt.com/docs/config-file/config-reference) has a model field. | Removed the unsupported claim that neither harness exposes model information. Distinguished session-supplied evidence from defaults, aliases, and uncertain self-identification. No hooks/config changes are installed. |
| [Codex discovery](https://learn.chatgpt.com/docs/build-skills) follows symlinks. | Clarified that updates follow the actual referenced checkout; merging another worktree does not update a symlink's target checkout. |

### Source caveats

- This review is dated, not a promise of continuing freshness. Unknown versions and "latest" requests require a new official-doc check when permitted; otherwise the skill must disclose its limitation.
- The Realtime prompting guide still centers Realtime 2 while the catalog includes 2.1/mini. The reference links both model pages and does not carry over unverified effort controls.
- Several Anthropic model documents moved into `/models/<model>/...`; the old migration URL is now an index. Guessed GPT-5.4/5.5 cookbook URLs and guessed Fable 5.1 URLs returned 404. Published version-guide and migration links resolved the required material. HTTP 403 responses from the default Python client succeeded when retried with a descriptive User-Agent.
- General prompting pages sometimes retain historical comparisons and examples. Model-specific pages and lifecycle notices govern version-specific facts. Pricing, billing, retention, and platform tool matrices were removed from drafting references to reduce unrelated drift.
- Restricted availability is not ordinary access. No provider account provisioning, model configuration, API invocation, or plugin deployment was performed by this review.

### Validation method

The previous skill was applied independently to three scenarios before editing. It blocked ordinary Claude task drafting on a mode question, blocked a simple rewrite on model identity, and conflated a destination model with the drafting runtime.

The updated behavior is evaluated with the [scenario suite](../tests/scenarios.md). These are independent drafting simulations using the supplied skill, not measurements of every named provider model. Structural packaging checks run separately with `python3 scripts/validate.py`; neither check proves provider endpoint behavior. API compatibility notes were checked against the cited official docs.

Results for this update:

- All 18 scenario rubrics passed after fixing and re-running the legacy-format ambiguity, offline API-note ambiguity, and JSON failure-format case. The online freshness case fetched the catalog, current guide, lifecycle page, and exact Astra pages; the offline case disclosed that latest-model identity was unverified.
- Structural validation and the skill-authoring frontmatter validator passed. Negative checks in a temporary copy correctly rejected a reintroduced command, a broken relative link, and a broken discovery symlink.
- All 56 distinct official documentation URLs linked by the current README, maintenance guide, references, and this review returned content through their Markdown endpoints. This reachability check is separate from the claim-by-claim source review above.
- An independent review of the final changes and relevant saved sources found no actionable issues. No live model endpoint or installed plugin was exercised; application-specific schemas and edge-case policy still need evaluation in the destination application.
