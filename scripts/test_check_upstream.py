"""Check the upstream diff and extraction logic without network access."""

import re

from check_upstream import MODELS, diff, fingerprint

base = {"models": {"openai": ["a"]}, "pages": {"u": "1"}}
assert diff(base, base) == []
changed = {"models": {"openai": ["b"]}, "pages": {"u": "2"}}
assert diff(base, changed) == [
    "New openai model ID: b",
    "Removed openai model ID: a",
    "Page changed: u",
]
assert fingerprint("a  b\n") == fingerprint("a b")
sample = "[x](/api/docs/models/gpt-6.1-sol.md) [y](/api/docs/models/gpt-image-2.md) [z](/api/docs/models/gpt-live-1.md)"
assert re.findall(MODELS["openai"][1], sample) == ["gpt-6.1-sol"]
assert re.findall(MODELS["typesafe"][1], "`jev-1.14.0` and jev-latest") == ["jev-1.14.0", "jev-latest"]
print("check_upstream logic passed")
