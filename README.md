# promptify

![Is this Astra 6?](assets/is-this-astra-6.svg)

Turn a rough idea or existing instructions into a clear, copyable **OpenAI or Anthropic prompt**, or a native **TypeSafe/Jev request template**. Works as a skill in Claude Code and Codex.

Promptify preserves your intent, chooses guidance for the destination you name, and makes missing inputs explicit. If you do not name a destination, it drafts a normal prompt using authoritative session information when available and general guidance otherwise. It never executes the drafted task or calls an inference API.

**Version 3 adds native Jev authoring.** OpenAI/Anthropic destinations still receive normal prompts. Explicit TypeSafe/Jev destinations receive JSON request templates. There is no mode picker; autonomous tasks still get ordinary instructions with success criteria and stopping conditions, without `/goal` command output.

## Example

> For GPT-6 Astra, turn this into a prompt: review my PR for security issues. Be thorough, but don't change code.

Target: GPT-6 Astra (user-specified).

```text
Review the pull request for actionable security defects introduced or exposed by its changes. Inspect the diff and the affected callers and trust boundaries. Keep the work read-only.

For each finding, give severity, file and line, the concrete failure or abuse path, supporting evidence, and a suggested fix. Distinguish confirmed issues from unresolved concerns. Omit style-only comments.

Finish with any limits on coverage or checks you could not perform. If there are no actionable findings, say so directly. Keep the report concise while preserving the evidence needed to assess each finding.
```

Say "only the prompt" to omit the target line. Name a destination such as "for Claude Fable 5.1" even when drafting inside Codex; the destination takes precedence over the running model.

## TypeSafe / Jev

> For Jev, turn this into a reusable request: detect whether a customer ticket asks for a refund and whether it asks to cancel a subscription. Both can apply.

Promptify produces a JSON template with `model`, `state`, and `questions`, using two independent Noul questions. It also supports Choice categories and descriptive Score rubrics. See the [TypeSafe reference and copyable example](skills/promptify/references/typesafe.md).

"For Claude, write a prompt to build a TypeSafe router" still produces a Claude prompt. Jev cannot generate customer replies or free-text explanations; Promptify identifies incompatible requests instead of inventing support. Say "only the JSON" to omit the target line, or explicitly request just the `questions` object.

This feature needs no TypeSafe key, SDK, or plugin. It drafts requests without evaluating them. Application thresholds and execution policy belong in separately requested integration notes; templates do not prove classification accuracy or calibrated routing.

## Model coverage

References checked against official documentation:

- **OpenAI:** GPT-6 Astra, GPT-6.1 Sol, GPT-6 Sol, and GPT-6 Luna (2026-09-30); GPT-5.6 Sol, Terra, and Luna (2026-09-14 guidance retained).
- **Anthropic:** Claude Sonnet 5.5 (2026-09-30); Claude Opus 5.5 (2026-09-27); Claude Fable 5.1, Opus 5, and Sonnet 5 (2026-09-14 guidance retained).
- **TypeSafe (2026-09-21):** Jev `jev-1.13.0`; explicitly requested aliases are preserved without assuming their current mapping.

Other OpenAI or Anthropic targets use disclosed general guidance. Unknown Jev versions retain their requested ID with unverified-compatibility disclosure. Requests for "latest" require a live official-doc check when browsing is available; offline Jev drafting discloses its dated guidance. API settings and availability are verified separately when integration advice is requested.

See the [OpenAI reference](skills/promptify/references/openai-families.md), [Anthropic reference](skills/promptify/references/claude-families.md), [TypeSafe reference](skills/promptify/references/typesafe.md), and [latest model review](docs/upstream-review-2026-09-30.md) for sources and limitations. Promptify authors artifacts; it does not switch your running model or provide an API client.

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
