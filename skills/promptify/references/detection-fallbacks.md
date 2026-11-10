# Resolve the target without inventing identity

The **target** consumes the finished artifact. The **runtime** is where Promptify drafts it. The **subject** is what the artifact discusses. They can differ: "For Claude, implement an app using TypeSafe" targets Claude and produces a normal prompt; "For Jev, classify these tickets" targets TypeSafe and produces a native request template. A repository's packaging does not identify the target or runtime.

Only an explicit TypeSafe/Jev destination selects native request output. Follow [TypeSafe requests](typesafe.md) for model selection and freshness. Merely mentioning Jev or asking a GPT/Claude classifier for JSON does not change the artifact to a Jev request.

## Resolution order

1. **Explicit destination:** preserve the user's named model, version, alias, and deployment surface. "For Claude Fable 5.2" in Codex means a Claude-targeted prompt. A current-session identity does not override that destination.
2. **Authoritative session evidence:** if no destination was specified, use model metadata explicitly supplied by the host or higher-priority session instructions. A model field from a request/response describes that request; it need not describe later turns or fallback requests. A session-start model describes that start, and a requested switch can be blocked, so only a completed switch changes the session model. Preserve an unresolved alias instead of expanding it from memory.
3. **Known family only:** use that family's shared guidance. Do not turn "Claude", "OpenAI", "Codex", or a model's unsupported self-description into an exact version.
4. **Unknown:** draft using the common principles in `SKILL.md`. Ask about the destination only if its capabilities materially affect the deliverable, such as a tool-dependent integration.

Do not inspect credentials, dump environment variables, read private transcripts, or modify settings to identify a model. Configured defaults can be overridden; inspect configuration only if the user asks for configuration help. Tool names, directory names, writing style, and model self-reports are not proof of identity. Never switch the user's model while drafting.

## Target line

Use a short, truthful line outside the copyable block:

- `Target: Claude Fable 5.2 (user-specified).`
- `Target: GPT-6 Astra (session-provided).`
- `Target: OpenAI family (exact model unknown).`
- `Target: unspecified; using general prompting guidance.`
- `Target: Gemini (no bundled guidance; using general prompting guidance).`
- `Target: TypeSafe Jev (jev-1.14.0; bundled selection, 2026-11-09); request template.`

For an unverified version, keep the requested name and say its version-specific guidance is unverified. For "latest", identify the model selected from current official docs as a selection, not a detected runtime. Omit this line when the user requests prompt-only or JSON-only output.
