# Maintaining Promptify

Promptify drafts normal prompts for OpenAI/Anthropic and native JSON request templates for explicitly requested TypeSafe/Jev destinations. Its product is the authored artifact and its references; source accuracy and drafting behavior both need review. It does not execute inference requests.

## Versioning

Use Semantic Versioning in `.claude-plugin/plugin.json` and add a matching dated `CHANGELOG.md` entry:

- **PATCH:** factual corrections, source links, and wording that preserve behavior.
- **MINOR:** new model guidance or compatible workflow improvements.
- **MAJOR:** changes to the skill's input/output contract, including removing a mode or changing target disclosure.

Keep plugin and marketplace names/descriptions consistent. The marketplace delegates the version to the plugin manifest. Version bumps also let Claude Code recognize an updated plugin.

## Source review

The source inventories are the official links in the [OpenAI reference](skills/promptify/references/openai-families.md), [Anthropic reference](skills/promptify/references/claude-families.md), [TypeSafe reference](skills/promptify/references/typesafe.md), and [target-resolution reference](skills/promptify/references/detection-fallbacks.md). Fetch their current contents, not search snippets. Append `.md` where the provider supports it; fall back to normal pages when Markdown fails, and follow published links rather than guessing URLs.

Start discovery with these indexes, even when the existing references appear current:

| Provider | Discovery sources |
| --- | --- |
| OpenAI | [Models](https://developers.openai.com/api/docs/models), [latest model](https://developers.openai.com/api/docs/guides/latest-model), [prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering), [API changelog](https://developers.openai.com/api/docs/changelog), [deprecations](https://developers.openai.com/api/docs/deprecations) |
| Anthropic | [Models](https://platform.claude.com/docs/en/models/overview), [prompting overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [migration index](https://platform.claude.com/docs/en/about-claude/models/migration-guide), [release notes](https://platform.claude.com/docs/en/release-notes/overview), [deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) |
| TypeSafe | [Index](https://docs.typesafe.ai/llms.txt), [models](https://docs.typesafe.ai/models), [API](https://docs.typesafe.ai/api), [primitives](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) |
| Installation | [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) |

For each update:

1. Discover new in-scope text models and Jev versions and their dedicated guides; check lifecycle before calling a catalog entry available. Keep the maintained scope focused on the models listed in README. Do not restore older, specialized, or restricted model sections during routine freshness updates. Distinguish product aliases, exact IDs, API access, and partner-platform differences.
2. Read the exact model's prompting guide and relevant migration/capability pages. Treat old cookbook recommendations as version-specific. Do not copy every model's workaround into shared guidance.
3. Preserve user requirements over general optimization advice. Remove unsupported universals, redundant process, and operational details that do not affect prompt drafting. Link to current pricing/tool-support docs rather than maintaining unrelated tables.
4. Record the review date and sources in affected references. If a source is inaccessible or contradictory, record the gap; a successful HTTP status alone does not verify a claim. Do not mark an unread page verified.
5. Update affected behavior, metadata, examples, validation, and changelog together. Run structural checks and relevant behavior scenarios, then inspect the complete diff.
6. Submit a PR against `main`; never commit directly to or automatically merge into `main`. Manual and automated updates use the same review path.

A monthly freshness routine has historically been configured outside this repository. This repo does not schedule or prove the status of that external automation. If it is running, use the procedure above and report write-access failures rather than bypassing them.

The [2026-09-30 review](docs/upstream-review-2026-09-30.md) records the latest model discovery and GPT-6.1 Sol/Sonnet 5.5 additions. The [2026-09-27 review](docs/upstream-review-2026-09-27.md) records the GPT-6 Sol/Luna and Opus 5.5 additions. The [2026-09-14 review](docs/upstream-review-2026-09-14.md) records the earlier OpenAI/Anthropic audit; the [TypeSafe reference](skills/promptify/references/typesafe.md) records its 2026-09-21 guidance. The [2026-09-07 review](docs/upstream-review-2026-09-07.md) records the version 2 workflow changes. Historical changelog and design documents describe their original releases; they are not runtime guidance.

## Validation

```bash
python3 scripts/validate.py
```

CI runs this same command. It checks manifest consistency, version/changelog pairing, skill frontmatter, reference reachability, JSON example syntax, relative documentation links, the discovery symlink, and removal of the old mode from shipped skill instructions. JSON parsing checks syntax, not provider compatibility or semantic correctness. It needs no network, model API, or third-party Python package.

Run the [behavior scenarios](tests/scenarios.md) in fresh evaluation contexts after workflow changes; for a reference-only correction, select the affected model cases plus cross-provider and unknown-target cases. Review actual outputs, not just wording matches. Save the baseline, revised outputs, and pass/fail notes in the PR or `.context/` for local review. Never execute the task inside a regression prompt. API compatibility claims require source review or real integration tests; a drafting simulation does not validate a provider endpoint.

## Propagation

- **Codex symlinks:** an install reflects the checkout it points to, including uncommitted changes. Merging elsewhere does not update a stale checkout or another worktree. Update that checkout and reload/restart if necessary. A copied install must be recopied.
- **Claude Code:** the installed plugin is cached. Refresh the marketplace, update the versioned plugin, then reload:

  ```bash
  claude plugin marketplace update promptify
  claude plugin update promptify@promptify
  ```

  Run `/reload-plugins` or restart. Third-party marketplace auto-update is opt-in; consult [marketplace update behavior](https://code.claude.com/docs/en/plugin-marketplaces) before relying on it.
