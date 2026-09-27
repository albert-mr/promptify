# Model review — 2026-09-27

Version 3.1 adds GPT-6 Sol, GPT-6 Luna, and Claude Opus 5.5. Existing explicit model destinations remain supported. Discovery covered all three providers; the detailed guidance review focused on these additions and the shared GPT-6 guide.

## Findings

| Official sources | Result in Promptify |
| --- | --- |
| OpenAI's [catalog](https://developers.openai.com/api/docs/models) and [September 22 release notes](https://developers.openai.com/api/docs/changelog) list GPT-6 Sol and Luna. Their [model](https://developers.openai.com/api/docs/models/gpt-6-sol) [pages](https://developers.openai.com/api/docs/models/gpt-6-luna) and the [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model) specify their API differences. | Added both exact IDs, shared family prompting, and separate integration rules: `none` supports sampling and Chat Completions function calling; reasoning with tools requires Responses. Astra's restrictions remain specific to Astra. |
| OpenAI's [September 25 fix](https://developers.openai.com/api/docs/changelog) addresses Sol/Luna image encoding. | Recommend rerunning affected image-input evaluations when advising existing integrations; no prompt workaround. |
| Anthropic's [catalog](https://platform.claude.com/docs/en/models/overview), [September 22 release notes](https://platform.claude.com/docs/en/release-notes/overview), [Opus 5.5 prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5), and [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) establish the new model. | Added targeted drafting guidance and separate notes for always-on thinking, effort, forced tools, replay, computer-use toolsets, and progress display. |
| Anthropic's [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking), and [preserved-thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) pages cover Opus 5.5. | Updated per-message effort coverage and kept display and history controls in client configuration. |
| The TypeSafe [index](https://docs.typesafe.ai/llms.txt) and [model page](https://docs.typesafe.ai/models) still list `jev-1.13.0`, with both aliases currently resolving to it. | No model change. Retained the dated selection and live-verification rule for aliases; the request-authoring reference keeps its September 21 review date. |

## Scope and source limitations

- Checked both providers' discovery, prompting indexes, release notes, and lifecycle pages: [OpenAI deprecations](https://developers.openai.com/api/docs/deprecations), [Claude deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations). No new retirement affects maintained targets. Specialized and restricted models remain outside maintained coverage.
- OpenAI's catalog introduction still recommends GPT-5.6 Terra/Luna while its full catalog and current family guide include GPT-6 Sol/Luna. Exact model pages and dated release notes establish the additions; namesakes are not aliases.
- Anthropic's catalog calls Opus 5 legacy, while its lifecycle table still marks it active. Preserve explicit Opus 5 requests; neither description means it is retired.
- GPT-6 prompting patterns are documented as Astra-derived starting points for the family, not measured identical behavior on Sol and Luna. Platform support and API compatibility still require verification for an actual integration.
- Markdown sources were fetched directly after the browser reader rejected their content type. Captures and drafting outputs are in the workspace's ignored `.context/model-review/` directory. Unchanged GPT-5.6, Fable 5.1, Opus 5, and Sonnet 5 guidance retains its September 14 review date; this is not a complete re-audit of every historical claim.

## Validation

Before editing, three offline drafting samples correctly disclosed missing exact-model coverage for the new targets, leaving their API questions unresolved. This established the reference gap without treating the existing safe fallback as a defect.

The [scenario suite](../tests/scenarios.md) adds N1–N5 for the new integration differences, explicit older-model routing, and ordinary Opus 5.5 prompt output. All 12 selected drafting samples passed: N1–N5, A2, A8, B2, B3, J1, A9, and C5. Ten used bundled guidance offline; A9 and C5 fetched live official discovery, lifecycle, and exact-model pages. Older-model requests retained their targets, unknown/offline requests disclosed uncertainty, and Jev retained its native template contract.

The revised samples came from one fresh evaluator session with logically separate cases, not 12 isolated provider sessions or a statistical reliability test. Full outputs were inspected. No target-model inference, provider endpoint integration, installed-plugin update, or drafted task was executed.

`python3 scripts/validate.py` and `git diff --check` passed. The skill entrypoint and executable validator are unchanged.
