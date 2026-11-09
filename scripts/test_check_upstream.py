"""Check the upstream diff and extraction logic without network access."""

import re

from check_upstream import MODELS, NEWEST, diff, first, fingerprint

base = {"models": {"openai": ["a"]}, "newest": {"x": "Nov 5"}, "pages": {"u": "1"}}
assert diff(base, base) == []
changed = {"models": {"openai": ["b"]}, "newest": {"x": "Nov 9"}, "pages": {"u": "2"}}
assert diff(base, changed) == [
    "New openai model ID: b",
    "Removed openai model ID: a",
    "New x entry: Nov 9 (was Nov 5)",
    "Page changed: u",
]
assert fingerprint("a  b\n") == fingerprint("a b")
assert re.findall(MODELS["openai"][1], "[x](/api/docs/models/gpt-6.1-sol.md)") == ["gpt-6.1-sol"]
assert re.findall(MODELS["typesafe"][1], "`jev-1.14.0` and jev-latest") == ["jev-1.14.0", "jev-latest"]
assert first("## May\n\n### Nov 5\n\n### Nov 4", NEWEST["openai changelog"][1]) == "Nov 5"
print("check_upstream logic passed")
