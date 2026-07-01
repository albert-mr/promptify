---
name: promptify
description: Use when the user gives a rough idea, brain-dump, or long unstructured ask and wants it turned into a polished, ready-to-use prompt — either a Claude Code /goal completion condition or a normal (system/task/agent) prompt. Triggers on "/promptify", "turn this into a prompt", "write me a prompt for X", "clean this idea up into a proper prompt".
---

# Promptify

## Overview

Promptify turns a rough idea or brain-dump into a polished, ready-to-use prompt — either a normal task/system/agent prompt or a Claude Code `/goal` completion condition. It auto-detects which model family is actually running (Claude vs. OpenAI) via a best-effort, disclosed guess, since neither provider exposes a reliable runtime model ID; see [references/detection-fallbacks.md](references/detection-fallbacks.md) for the full fallback chain.

## Workflow

1. **Get the raw idea.** Take whatever the user hands you — a brain-dump, a fragment, a half-formed ask — as the seed for the prompt.
2. **Detect harness.** Determine whether you're running in Claude Code or Codex CLI, per [references/detection-fallbacks.md](references/detection-fallbacks.md).
3. **Detect model family.** Use a soft self-report, deferring to any explicit override the user states, per [references/detection-fallbacks.md](references/detection-fallbacks.md). Output the one-line disclosure template from that file so the user sees the guess and its confidence.
4. **Ask goal-vs-normal — only if the harness is Claude Code AND the drafted prompt targets this same Claude Code session/harness.** Explicitly ask the user whether they want a `/goal` completion condition or a normal prompt, per [references/goal-vs-normal.md](references/goal-vs-normal.md). Skip the question and go straight to normal mode whenever: the harness is Codex CLI (never a fabricated goal construct — see that file's "Why Codex CLI never gets a /goal" section), or the ask names a different target system entirely (e.g. "this is for GPT-5.2" or "write a prompt for our support bot") — `/goal` only makes sense for a loop running in this harness, never for a prompt destined for some other system.
5. **Draft.** Write the prompt using the matching family's reference file: [references/claude-families.md](references/claude-families.md) for Claude, [references/openai-families.md](references/openai-families.md) for OpenAI.
6. **Output.** Deliver the finished prompt (or `/goal` condition) as a single copyable block, text only. Never auto-execute it as instructions in the current session.

## Example

Input: "make an agent that reviews PRs for security issues, kind of exhaustive but shouldn't take forever."

- Harness detected: Claude Code.
- Model family detected: Claude (disclosed guess, per the template).
- Goal-vs-normal asked explicitly: user picks "normal prompt" (not a `/goal`).
- Output shape: a single copyable normal task/system prompt drafted per [references/claude-families.md](references/claude-families.md), covering scope, exhaustiveness/time tradeoff, and output format — delivered as text, not executed.

If the same input came through Codex CLI instead, step 4 is skipped entirely and the output is always a normal prompt drafted per [references/openai-families.md](references/openai-families.md).
