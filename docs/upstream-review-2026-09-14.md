# Upstream review — 2026-09-14

> This report records the version 2.1.0 audit. Version 2.1.1 subsequently narrows maintained guidance to seven text models; see the [current model list](../README.md#model-coverage). The source findings and validation results below describe the earlier audit, not the current coverage.

Version 2.1 refreshes both providers after the [September 7 review](upstream-review-2026-09-07.md). Normal prompts remain the only output mode. Research compared fresh official catalogs, release notes, lifecycle pages, prompting guides, and migration docs with the previous captures, then followed published links for new models. Saved sources, diffs, and drafting evaluations live in this workspace's ignored `.context/` directory.

## Findings and changes

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

## Source limitations

- The image guide's `input_fidelity` omission rule explicitly names Image 2. The reviewed Image 2.5 prompting/model pages do not establish that setting's compatibility; the reference avoids transferring the older rule. Its confirmed model, quality, transparency, and Responses routing guidance remains usable.
- Some examples and lifecycle replacement recommendations still name older models. Follow the exact model's current guide and validate the intended workflow instead of globally replacing every historical example.
- Claude Code and Codex configuration changes were checked for effects on discovery and installation. Existing packaging remains compatible; no hooks, model settings, credentials, or installed plugins were changed.
- These sources describe provider behavior as of this review. They are not substitutes for live verification on a later "latest" request, or tests in the destination application.

## Validation

Before editing, two independent offline drafting simulations exposed missing GPT-Live and Image 2.5 coverage. The image case correctly declined to invent Responses model placement from the old bundle. The voice case preserved the request but lacked Live-specific handoff guidance.

The [scenario suite](../tests/scenarios.md) now contains 26 cases, including eight additions for this refresh. Results:

- All 17 selected drafting samples met their rubrics: C1–C8 plus nine existing cross-provider, unknown-target, normal-mode, API, and voice cases. Two independent evaluators treated cases as separate logical invocations; these were not 17 isolated provider sessions or a statistical reliability measurement.
- Both providers' online "latest" cases fetched fresh official discovery, lifecycle, and exact-model pages. Offline cases disclosed that latest-model identity could not be verified. The Claude JSON/API case also retrieved current integration docs.
- The Haiku classifier case preserves its requested three-label contract, but routing wholly empty or irrelevant input remains unspecified application policy. A destination application must supply that policy; a passing drafting rubric does not settle it.
- `python3 scripts/validate.py`, the skill-authoring frontmatter validator, and Git whitespace checks passed. The normal-prompt entrypoint and executable validator were not changed in this refresh.
- All 66 official URLs linked by the current README, maintenance guide, references, and this review returned content: 65 Markdown pages and Rosalind's HTML article. Claim review was separate from this reachability check. The superseded 404 remains recorded in the research evidence and historical September 7 report.
- Independent final source/content review found no actionable issues. No destination model, image generation, installed plugin, or provider integration was exercised.
