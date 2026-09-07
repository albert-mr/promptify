# promptify

Turn a rough idea or an existing prompt into one clear, copyable prompt for **OpenAI or Anthropic** models. Works as a skill in Claude Code and Codex.

Promptify preserves your intent, chooses guidance for the model you name, and makes missing inputs explicit. If you do not name a model, it uses authoritative session information when available and otherwise drafts with general guidance. It never executes the task inside the prompt.

**Version 2 produces normal prompts only.** The mode picker and `/goal` completion-condition output have been removed. Autonomous tasks still get ordinary instructions with success criteria and stopping conditions.

## Example

> For GPT-6 Astra, turn this into a prompt: review my PR for security issues. Be thorough, but don't change code.

Target: GPT-6 Astra (user-specified).

```text
Review the pull request for actionable security defects introduced or exposed by its changes. Inspect the diff and the affected callers and trust boundaries. Keep the work read-only.

For each finding, give severity, file and line, the concrete failure or abuse path, supporting evidence, and a suggested fix. Distinguish confirmed issues from unresolved concerns. Omit style-only comments.

Finish with any limits on coverage or checks you could not perform. If there are no actionable findings, say so directly. Keep the report concise while preserving the evidence needed to assess each finding.
```

Say "only the prompt" to omit the target line. Name a destination such as "for Claude Fable 5.1" even when drafting inside Codex; the destination takes precedence over the running model.

## Model coverage

References checked **2026-09-07** against official documentation:

- **OpenAI:** GPT-6 Astra; GPT-5.6 Sol, Terra, and Luna; older GPT and o-series targets; coding-model guidance; specialized voice, image, research, and restricted cyber targets.
- **Anthropic:** Claude Fable/Mythos 5.1, Opus 5, Sonnet 5, Haiku 4.5, and earlier supported versions.

Current, older, restricted, and retired models are distinguished in the references. Unknown versions use disclosed general guidance. Requests for "latest" require a live official-doc check when browsing is available. API settings and availability are verified separately when integration advice is requested.

See the [OpenAI reference](skills/promptify/references/openai-families.md), [Anthropic reference](skills/promptify/references/claude-families.md), and [upstream review](docs/upstream-review-2026-09-07.md) for sources and limitations. This is a prompt-writing skill, not a model selector or API client.

## Install in Claude Code

```text
/plugin marketplace add albert-mr/promptify
/plugin install promptify@promptify
```

Invoke with `/promptify:promptify` followed by your idea. These commands register the marketplace and install its plugin; see [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

## Install in Codex

This repository includes `.agents/skills/promptify`, a symlink to `skills/promptify`, so no installation is needed when working here. Invoke with `$promptify`.

For another project, run from this checkout:

```bash
mkdir -p /path/to/project/.agents/skills
ln -s "$(pwd)/skills/promptify" /path/to/project/.agents/skills/promptify
```

For a global install:

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/skills/promptify" ~/.agents/skills/promptify
```

Use `cp -R skills/promptify /path/to/destination` for a fixed copy instead of a symlink. Do not overwrite an existing installation without checking its location. Restart Codex if the skill does not appear. See [Codex skills](https://learn.chatgpt.com/docs/build-skills) for discovery rules.

## Update and validate

Claude Code caches installed plugins. After an update is merged:

```bash
claude plugin marketplace update promptify
claude plugin update promptify@promptify
```

Then run `/reload-plugins` or restart the session. A symlinked Codex install follows **its actual checkout**; fetch/pull that checkout to receive merged changes. Copied installs need recopying.

Run the same structural checks as CI:

```bash
python3 scripts/validate.py
```

The [behavior scenarios](tests/scenarios.md) test drafting decisions separately; structural validation does not prove model behavior. See [MAINTAINING.md](MAINTAINING.md) for source checks, versioning, and review requirements.

## Layout

- `skills/promptify/SKILL.md`: drafting workflow.
- `skills/promptify/references/`: provider guidance and target resolution.
- `.claude-plugin/`: marketplace and plugin manifests.
- `.agents/skills/promptify`: Codex discovery symlink.
- `scripts/validate.py`: dependency-free structural validation used by CI.
- `tests/scenarios.md`: behavioral regression cases.

## License

[MIT](LICENSE) © Albert Martinez
