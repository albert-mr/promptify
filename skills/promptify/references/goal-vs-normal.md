## Telling goal-mode from normal-mode

A Claude Code `/goal` completion condition is a harness-native construct: a short block of text that a **transcript-only evaluator model** reads after the fact to decide whether the loop is done. It never sees your intent, your conversation history, or anything outside the transcript it's handed — only what actually happened in the run. Because of that, a goal condition has to be self-contained, verifiable from output alone, and bounded, since the harness will keep looping until the evaluator says stop (or a turn limit forces it).

A normal prompt is everything else: a system prompt, a task prompt, an agent/subagent prompt. It's consumed by the acting model itself, not by a separate evaluator, and there is no harness-level loop mechanism attached to it. The model reads it once (per turn) and acts — there's no external judge deciding "done or not done."

The practical tell is whether the user is asking for a *condition an evaluator checks* or *instructions an agent follows*.

| Signal in the ask | Mode |
|---|---|
| User mentions `/goal` explicitly | Goal mode |
| Autonomous / overnight / unattended loop | Goal mode |
| "Keep going until X" / "don't stop until X" | Goal mode |
| A turn-bound ("run for N turns", "stop after...") | Goal mode |
| Everything else — a task, a persona, a system/agent prompt, a one-shot instruction | Normal mode |

If none of the goal-mode signals are present, default to normal mode. Don't invent a loop condition where the user just wanted a well-written prompt.

## Why Codex CLI never gets a /goal

`/goal` is a Claude Code harness feature. It exists because Claude Code has a documented mechanism for it: a transcript-only evaluator model that the harness invokes between turns to decide whether to keep looping. Codex CLI has no equivalent anywhere in its documented mechanisms — not in `AGENTS.md`, not in Agent Skills, not in plugins, not in hooks. None of those surfaces expose a loop primitive, a completion-condition primitive, or an evaluator-model hook. There is nothing in Codex CLI for a goal condition to attach to.

So the rule is plain: when the detected or confirmed harness is Codex CLI, always draft a **normal prompt** — never a fabricated goal construct, never a "pretend `/goal`" dressed up as Codex CLI syntax. If the underlying ask genuinely wants a definition of "done," the correct move is to add an explicit prose **"Success criteria"** section inside the normal prompt. That's just ordinary good prompting — consistent with OpenAI's own guidance on writing clear, verifiable instructions for Codex CLI — not a harness mechanism, and it carries no loop, no evaluator, and no bound. It's instruction text the acting model reads once, same as the rest of the prompt.

## /goal condition checklist

A good `/goal` condition has these elements, in order:

1. **One measurable end state** — a single outcome, demonstrable by output the model can paste into the transcript. Not a bundle of goals, not a vibe.
2. **A stated check** — the exact command to run and the exact expected result, shown actually running in the transcript (not described, not assumed).
3. **Constraints that must not change** — enumerated explicitly (files not to touch, behavior not to break, scope not to expand).
4. **A bound clause** — e.g., "or stop after N turns" — so the loop cannot run unbounded if the end state is never reached.
5. **Total length ≤ 4000 characters.**

Before finalizing, verify every external identifier the condition references — file paths, command names, flag names, labels — actually exists in the repo or environment. Don't let the evaluator check something that was never real.

For conditions shaped like "all X satisfy Y," give any unsatisfiable item an explicit exit: require a ledger file that the model must `cat` into the transcript, listing exceptions or blockers, so the loop can terminate honestly instead of spinning forever chasing an item that can never pass.
