# GPT-5.6 Support Design

## Scope

Add prompt-drafting guidance for the general GPT-5.6 family only:
`gpt-5.6`/`gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`.
Specialized realtime, audio, transcription, image, and Codex models remain
unchanged.

## Changes

- Add a focused GPT-5.6 subsection to `openai-families.md` before the shared
  GPT-5.x guidance. Record the three model IDs, the `gpt-5.6` alias, and the
  prompting behavior that affects promptify output: lean prompts, explicit
  autonomy and approval boundaries, concise-by-default output, supported
  reasoning efforts through `max`, and pro mode as a parameter rather than a
  separate model slug.
- Add the official model-guidance page to `MAINTAINING.md` so future freshness
  checks cover model-specific guidance as well as the catalog.
- Bump the plugin version from 1.1.1 to 1.2.0 because this adds support for a
  new model generation without changing promptify's output contract.
- Add a matching 1.2.0 entry to `CHANGELOG.md`.

No routing change is needed: all OpenAI models already use
`openai-families.md`.

## Verification

- Run the repository's existing validation command from its CI workflow.
- Check that the GPT-5.6 subsection contains all three IDs and that
  `gpt-5.6` is documented as the Sol alias.
- Run the existing OpenAI target-system regression scenario and confirm it
  still produces a normal prompt using `openai-families.md`.
- Confirm the plugin version and changelog version match.
