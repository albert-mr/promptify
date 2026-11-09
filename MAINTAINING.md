# Maintaining Promptify

Promptify drafts normal prompts for OpenAI/Anthropic and native JSON request templates for explicitly requested TypeSafe/Jev destinations. Its product is the authored artifact and its references; source accuracy and drafting behavior both need review. It does not execute inference requests.

## Versioning

Use Semantic Versioning in `.claude-plugin/plugin.json` and add a matching dated `CHANGELOG.md` entry:

- **PATCH:** factual corrections, source links, and wording that preserve behavior.
- **MINOR:** new model guidance or compatible workflow improvements.
- **MAJOR:** changes to the skill's input/output contract, including removing a mode or changing target disclosure.

Keep plugin and marketplace names/descriptions consistent. The marketplace delegates the version to the plugin manifest. Version bumps also let Claude Code recognize an updated plugin.

## Source review

The source inventories are the official links in the [OpenAI reference](skills/promptify/references/openai-families.md), [Anthropic reference](skills/promptify/references/claude-families.md), [Anthropic integration notes](skills/promptify/references/claude-integration.md), [TypeSafe reference](skills/promptify/references/typesafe.md), and the target-resolution sources below. Fetch their current contents, not search snippets. Append `.md` where the provider supports it; fall back to normal pages when Markdown fails, and follow published links rather than guessing URLs.

Start with `python3 scripts/check_upstream.py`, which reports new model IDs, new changelog entries, and changed guide pages since the committed snapshot. It does not explain a change, so still read what it flags. After review, run it with `--update` and commit the snapshot in the same PR. A full review also starts from these indexes, even when the existing references appear current:

| Provider | Discovery sources |
| --- | --- |
| OpenAI | [Models](https://developers.openai.com/api/docs/models), [latest model](https://developers.openai.com/api/docs/guides/latest-model), [prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering), [API changelog](https://developers.openai.com/api/docs/changelog), [deprecations](https://developers.openai.com/api/docs/deprecations) |
| Anthropic | [Models](https://platform.claude.com/docs/en/models/overview), [prompting overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [migration index](https://platform.claude.com/docs/en/about-claude/models/migration-guide), [release notes](https://platform.claude.com/docs/en/release-notes/overview), [deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) |
| TypeSafe | [Index](https://docs.typesafe.ai/llms.txt), [models](https://docs.typesafe.ai/models), [API](https://docs.typesafe.ai/api), [primitives](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [known limitations](https://docs.typesafe.ai/model-jaggedness), [model changelog](https://docs.typesafe.ai/changelog) |
| Installation | [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [discover plugins](https://code.claude.com/docs/en/discover-plugins) |

For each update:

1. Discover new in-scope text models and Jev versions and their dedicated guides; check lifecycle before calling a catalog entry available. Keep the maintained scope focused on the models listed in README. Do not restore older, specialized, or restricted model sections during routine freshness updates. Remove a model's section once the provider labels it legacy or previous-generation, or a same-tier successor supersedes it in the catalog; agents typically read the whole provider reference, so superseded sections cost context on every draft. Distinguish product aliases, exact IDs, API access, and partner-platform differences.
2. Read the exact model's prompting guide and relevant migration/capability pages. Treat old cookbook recommendations as version-specific. Do not copy every model's workaround into shared guidance.
3. Preserve user requirements over general optimization advice. Remove unsupported universals, redundant process, and operational details that do not affect prompt drafting. Link to current pricing/tool-support docs rather than maintaining unrelated tables.
4. Update the model's Reviewed date only after a full read of its guide, and record the review in the [upstream log](docs/upstream-log.md). If a source is inaccessible or contradictory, record the gap; a successful HTTP status alone does not verify a claim. Do not mark an unread page verified.
5. Update affected behavior, metadata, examples, validation, and changelog together. Run structural checks and relevant behavior scenarios, then inspect the complete diff.
6. Submit a PR against `main`; never commit directly to or automatically merge into `main`. Manual and automated updates use the same review path.

The [Upstream docs check](.github/workflows/upstream.yml) workflow runs weekly and opens one issue when the snapshot is out of date. Resolve that issue with the procedure above. Keep each provider reference to prompt-drafting guidance: API and migration detail for Claude belongs in the integration notes, so ordinary drafts do not load it.

The [upstream log](docs/upstream-log.md) records past reviews. Historical changelog and log entries describe their original releases; they are not runtime guidance.

## Target-resolution sources

Claude Code documents a model picker, launch flags, `ANTHROPIC_MODEL`, settings, and model aliases. Its hooks can expose model information **when passed into the current session**; Promptify does not install hooks. `SessionStart.model` is optional. `PreModelSwitch` describes a requested change that may be blocked; `PostModelSwitch` records a completed session-model change. Neither guarantees the model used for every later request or fallback. Alias mappings can vary by provider, account, and harness version, so preserve an unresolved alias instead of expanding it from memory. See [model configuration](https://code.claude.com/docs/en/model-config) and [hooks](https://code.claude.com/docs/en/hooks).

Codex documents a `model` configuration setting and separate overrides. That establishes a configured preference, not a universal API for skills to discover the effective model on every request. Use supplied session metadata when available; otherwise retain uncertainty. See [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

Claude's prompting docs demonstrate supplying model identity through instructions. That is useful evidence for an explicitly informed session, not proof that unaided self-identification is reliable. See [model self-knowledge](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#model-self-knowledge).

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

  Run `/reload-plugins` or restart. Third-party marketplace auto-update is opt-in; consult [marketplace update behavior](https://code.claude.com/docs/en/discover-plugins) before relying on it.
