# Resolve the target without inventing identity

Last verified: 2026-09-14.

The **target** consumes the finished artifact. The **runtime** is where Promptify drafts it. The **subject** is what the artifact discusses. They can differ: "For Claude, implement an app using TypeSafe" targets Claude and produces a normal prompt; "For Jev, classify these tickets" targets TypeSafe and produces a native request template. A repository's packaging does not identify the target or runtime.

TypeSafe routing added 2026-09-21: only an explicit TypeSafe/Jev destination selects native request output. Follow [TypeSafe requests](typesafe.md) for model selection and freshness. Merely mentioning Jev or asking a GPT/Claude classifier for JSON does not change the artifact to a Jev request.

## Resolution order

1. **Explicit destination:** preserve the user's named model, version, alias, and deployment surface. "For Claude Fable 5.1" in Codex means a Claude-targeted prompt. A current-session identity does not override that destination.
2. **Authoritative session evidence:** if no destination was specified, use model metadata explicitly supplied by the host or higher-priority session instructions. A model field from a request/response describes that request; it need not describe later turns or fallback requests.
3. **Known family only:** use that family's shared guidance. Do not turn "Claude", "OpenAI", "Codex", or a model's unsupported self-description into an exact version.
4. **Unknown:** draft using the common principles in `SKILL.md`. Ask about the destination only if its capabilities materially affect the deliverable, such as a tool-dependent integration.

Do not inspect credentials, dump environment variables, read private transcripts, or modify settings to identify a model. Configured defaults can be overridden; inspect configuration only if the user asks for configuration help. Tool names, directory names, writing style, and model self-reports are not proof of identity. Never switch the user's model while drafting.

## Target line

Use a short, truthful line outside the copyable block:

- `Target: Claude Fable 5.1 (user-specified).`
- `Target: GPT-6 Astra (session-provided).`
- `Target: OpenAI family (exact model unknown).`
- `Target: unspecified; using general prompting guidance.`
- `Target: TypeSafe Jev (jev-1.13.0; bundled selection, 2026-09-21); request template.`

For an unverified version, keep the requested name and say its version-specific guidance is unverified. For "latest", identify the model selected from current official docs as a selection, not a detected runtime. Omit this line when the user requests prompt-only or JSON-only output.

## What the harness docs actually establish

Claude Code documents a model picker, launch flags, `ANTHROPIC_MODEL`, settings, and model aliases. Its hooks can expose model information **when passed into the current session**; Promptify does not install hooks. `SessionStart.model` is optional. `PreModelSwitch` describes a requested change that may be blocked; `PostModelSwitch` records a completed session-model change. Neither guarantees the model used for every later request or fallback. Alias mappings can vary by provider, account, and harness version, so preserve an unresolved alias instead of expanding it from memory. See [model configuration](https://code.claude.com/docs/en/model-config) and [hooks](https://code.claude.com/docs/en/hooks).

Codex documents a `model` configuration setting and separate overrides. That establishes a configured preference, not a universal API for skills to discover the effective model on every request. Use supplied session metadata when available; otherwise retain uncertainty. See [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

Claude's prompting docs demonstrate supplying model identity through instructions. That is useful evidence for an explicitly informed session, not proof that unaided self-identification is reliable. See [model self-knowledge](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#model-self-knowledge).
