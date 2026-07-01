# promptify

A skill that drafts polished prompts — or Claude Code `/goal` completion conditions, where applicable — tuned to whichever Claude or OpenAI model family is currently running. The runtime model is auto-detected with a best-effort, disclosed guess, since neither Anthropic nor OpenAI exposes a reliable runtime model ID; you can always correct the detected family if it's wrong.

## Install in Claude Code

```
/plugin marketplace add albert-mr/promptify
```
Registers this repo as a plugin marketplace so Claude Code can find and install `promptify`.

```
/plugin install promptify@promptify
```
Installs the `promptify` plugin from that marketplace into your Claude Code environment.

```
/promptify:promptify
```
Invokes the skill to turn your rough idea into a polished prompt or `/goal` completion condition.

## Install in Codex CLI

Codex CLI has no plugin marketplace, so there are two ways to make the skill available:

- **Project-scoped (auto-discovered):** clone or keep this repo checked out so that `.agents/skills/promptify/` sits inside your project tree. Codex CLI's repo-level directory walk scans for skills under `.agents/skills/`, so it will be picked up automatically for that project — no extra configuration needed.
- **Global install:** copy or symlink `skills/promptify/` to `~/.codex/skills/promptify/`. This makes the skill available to Codex CLI across all projects, not just the one containing this repo.

## Repo layout

- `skills/promptify/SKILL.md` — the skill definition itself.
- `skills/promptify/references/*.md` — supporting reference docs:
  - `claude-families.md`
  - `openai-families.md`
  - `goal-vs-normal.md`
  - `detection-fallbacks.md`
- `.claude-plugin/` — Claude Code packaging metadata (marketplace + plugin manifest).
- `.agents/skills/promptify` — symlink used for Codex CLI's repo-level skill discovery.

## Scope and honesty notes

- No provider (Anthropic or OpenAI) gives reliable runtime model-ID introspection — model-family detection here is best-effort and its guess is always disclosed and correctable, never asserted as fact.
- Codex CLI has no equivalent of Claude Code's `/goal` completion-condition primitive, so goal-mode prompt drafting is Claude-Code-only; on Codex, promptify only produces normal (system/task/agent) prompts.
- When in doubt about which model family is actually running, trust your own knowledge of your environment over promptify's guess and correct it.
