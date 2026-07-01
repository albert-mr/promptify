# Detection Fallbacks

Reference for the `promptify` skill: how to infer which coding harness and model family is actually running, when no authoritative API for that exists.

## Harness detection (Claude Code vs Codex CLI)

There is no official "detect harness" API. What follows is a heuristic inferred from the environment a skill finds itself running in — signals observed at runtime, not a documented contract. Treat all of it as best-effort.

**Claude Code signals:**
- Env vars: `CLAUDECODE`, `CLAUDE_CODE_*` (e.g. `CLAUDE_EFFORT` — confirmed present on this machine, value like `"high"`)
- Claude-Code-specific tools available in the session: `TodoWrite`, slash commands like `/goal`, `/model`
- Filesystem conventions: `.claude/` directory, `.claude-plugin/` manifests, `.claude/skills/`

**Codex CLI signals:**
- Env var: `CODEX_HOME`
- Codex-specific tools: `apply_patch`, `shell_command`, `update_plan`
- Filesystem conventions: `AGENTS.md`, `.agents/skills/`

If neither set of signals is conclusively present, do not force a guess — fall through to asking the user (see step 4 of the fallback chain below).

## Model-family detection fallback chain

Apply these in strict priority order. Stop at the first one that resolves confidently.

1. **CLI/env introspection, only if confirmed to exist.** If a later version of the current harness is confirmed to expose a model-identifying env var, config field, or hook payload field, use it. Do not assume such a mechanism exists — as of this writing, neither Claude Code nor Codex CLI exposes the pinned model ID or name anywhere a skill can read it. Claude Code exposes only `CLAUDE_EFFORT` (e.g. `"high"`), not the model name. Codex CLI's own docs confirm the identical gap: no env var, no `config.toml` field, and no hook payload field carries the active model name through to `AGENTS.md`, prompts, or skills.
2. **The running model's self-report, as a soft signal only.** A model can be asked what it is, but this is explicitly non-authoritative per both providers' own docs — self-reports can be wrong, stale, or hedged. Use it only to inform a guess, never to assert a fact.
3. **An explicit user override stated in the ask.** E.g. "I'm running Sonnet 5" or "this is for gpt-5.2-codex." This is the most reliable path available and should take precedence over any inference once given.
4. **If still ambiguous, ask.** Pose one direct clarifying question to the user rather than silently guessing. Do not chain multiple questions or bury the ask — one question, then proceed.

## Disclosure wording

Every promptify invocation outputs this exact one-line template before drafting, regardless of confidence level:

```
Detected: `<harness>`, `<family>` — say so if wrong.
```

This line is shown even when confidence is high. It is never presented as certain — it is a disclosed best guess, and the user is explicitly invited to correct it before the draft proceeds.
