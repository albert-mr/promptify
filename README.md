# promptify

![Is this Astra 6?](assets/is-this-astra-6.svg)

Turn a rough idea or existing instructions into a clear, copyable prompt tuned for **OpenAI and Anthropic** models, or a native **TypeSafe/Jev request template**. Works as a skill in Claude Code and Codex.

Promptify preserves your intent, uses guidance for the destination you name, and makes missing inputs explicit. It never executes the drafted task or calls an inference API.

## Install

**Claude Code**

```text
/plugin marketplace add albert-mr/promptify
/plugin install promptify@promptify
```

Invoke it with `/promptify:promptify` followed by your idea, or ask for a prompt in plain language. See [Discover plugins](https://code.claude.com/docs/en/discover-plugins).

**Codex**

```bash
git clone https://github.com/albert-mr/promptify.git ~/promptify
mkdir -p ~/.agents/skills
ln -s ~/promptify/skills/promptify ~/.agents/skills/promptify
```

Invoke it with `$promptify`, and restart Codex if the skill does not appear. For a single project, link it into that project's `.agents/skills/` instead. Inside this repository no install is needed. See [Codex skills](https://learn.chatgpt.com/docs/build-skills).

## Example

> For GPT-6 Astra, turn this into a prompt: review my PR for security issues. Be thorough, but don't change code.

Target: GPT-6 Astra (user-specified).

```text
Review the pull request for actionable security defects introduced or exposed by its changes. Inspect the diff and the affected callers and trust boundaries. Keep the work read-only.

For each finding, give severity, file and line, the concrete failure or abuse path, supporting evidence, and a suggested fix. Distinguish confirmed issues from unresolved concerns. Omit style-only comments.

Finish with any limits on coverage or checks you could not perform. If there are no actionable findings, say so directly. Keep the report concise while preserving the evidence needed to assess each finding.
```

Say "only the prompt" to omit the target line. Name a destination such as "for Claude Fable 5.1" even when drafting inside Codex; the destination takes precedence over the running model. Ask for API or migration notes when you want them; they stay separate from the prompt.

## TypeSafe / Jev

> For Jev, turn this into a reusable request: detect whether a customer ticket asks for a refund and whether it asks to cancel a subscription. Both can apply.

Promptify produces a JSON template with `model`, `state`, and `questions`, using two independent Noul questions. It also supports Choice categories and descriptive Score rubrics. See the [TypeSafe reference and copyable example](skills/promptify/references/typesafe.md).

"For Claude, write a prompt to build a TypeSafe router" still produces a Claude prompt. Jev cannot generate customer replies or free-text explanations, so Promptify identifies incompatible requests instead of inventing support. Say "only the JSON" to omit the target line, or request just the `questions` object.

This feature needs no TypeSafe key, SDK, or plugin. Templates are drafts: they are not evaluated and do not prove classification accuracy.

## Model coverage

- **OpenAI:** GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Luna.
- **Anthropic:** Claude Fable 5.1, Opus 5.5, Sonnet 5.5, and Haiku 5.5.
- **TypeSafe:** Jev `jev-1.14.0` (default) and `jev-1.13.0`, with experimental image input and Box questions on explicit request.

Any other model, including other providers such as Gemini, gets a normal prompt with general guidance and a note saying so. Requests for "latest" check official docs when browsing is available. Each reference lists when its guidance was reviewed: [OpenAI](skills/promptify/references/openai-families.md), [Anthropic](skills/promptify/references/claude-families.md), and [TypeSafe](skills/promptify/references/typesafe.md).

## Update

Claude Code keeps an installed plugin on its version until you update it. Third-party marketplaces have auto-update off by default; turn it on in `/plugin` under **Marketplaces**, or update manually:

```bash
claude plugin marketplace update promptify
claude plugin update promptify@promptify
```

Then run `/reload-plugins`. For Codex, run `git -C ~/promptify pull`.

## Contributing

See [MAINTAINING.md](MAINTAINING.md) for source checks, versioning, and review requirements. Run the same structural checks as CI with:

```bash
python3 scripts/validate.py
```

Structural validation does not prove model behavior; the [behavior scenarios](tests/scenarios.md) cover drafting decisions.

## License

[MIT](LICENSE) © Albert Martinez
