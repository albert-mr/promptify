"""Report provider doc changes since the committed snapshot. Standard library only.

python3 scripts/check_upstream.py           exit 0 unchanged, 1 changed, 2 fetch failed
python3 scripts/check_upstream.py --update  rewrite the snapshot after review
"""

import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

SNAPSHOT = Path(__file__).with_name("upstream-snapshot.json")
OPENAI = "https://developers.openai.com/api/docs"
ANTHROPIC = "https://platform.claude.com/docs/en"
PROMPTING = f"{ANTHROPIC}/build-with-claude/prompt-engineering"
TYPESAFE = "https://docs.typesafe.ai"

MODELS = {
    "openai": (f"{OPENAI}/models/all.md", r"/models/([a-z0-9][a-z0-9.-]*?)\.md"),
    "anthropic": (f"{ANTHROPIC}/models/overview.md", r"\b(claude-[a-z]+-\d[a-z0-9-]*)\b"),
    "typesafe": (f"{TYPESAFE}/models.md", r"\b(jev-(?:latest|preview|\d+\.\d+\.\d+))\b"),
}
NEWEST = {
    "openai changelog": (f"{OPENAI}/changelog.md", r"^### (.+)$"),
    "anthropic release notes": (f"{ANTHROPIC}/release-notes/overview.md", r"^### (.+)$"),
    "typesafe changelog": (f"{TYPESAFE}/changelog.md", r"\b(Jev \d+\.\d+)\b"),
}
PAGES = [
    f"{OPENAI}/guides/latest-model.md",
    f"{OPENAI}/guides/prompt-engineering.md",
    f"{OPENAI}/deprecations.md",
    f"{ANTHROPIC}/about-claude/model-deprecations.md",
    f"{PROMPTING}/claude-prompting-best-practices.md",
    f"{PROMPTING}/prompting-claude-fable-5-1.md",
    f"{PROMPTING}/prompting-claude-opus-5-5.md",
    f"{PROMPTING}/prompting-claude-sonnet-5-5.md",
    f"{PROMPTING}/prompting-claude-haiku-5-5.md",
    f"{TYPESAFE}/api.md",
    f"{TYPESAFE}/images.md",
    f"{TYPESAFE}/model-jaggedness.md",
]


def fingerprint(text):
    return hashlib.sha256(" ".join(text.split()).encode()).hexdigest()


def first(text, pattern):
    match = re.search(pattern, text, re.M)
    return match[1] if match else None


def diff(old, new):
    changes = []
    for name, ids in new["models"].items():
        before = set(old.get("models", {}).get(name, []))
        changes += [f"New {name} model ID: {i}" for i in sorted(set(ids) - before)]
        changes += [f"Removed {name} model ID: {i}" for i in sorted(before - set(ids))]
    for name, value in new["newest"].items():
        before = old.get("newest", {}).get(name)
        if value != before:
            changes.append(f"New {name} entry: {value} (was {before})")
    for url, value in new["pages"].items():
        if value != old.get("pages", {}).get(url):
            changes.append(f"Page changed: {url}")
    return changes


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "promptify-upstream-check"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode()


def collect():
    return {
        "models": {n: sorted(set(re.findall(p, fetch(u)))) for n, (u, p) in MODELS.items()},
        "newest": {n: first(fetch(u), p) for n, (u, p) in NEWEST.items()},
        "pages": {u: fingerprint(fetch(u)) for u in PAGES},
    }


def main():
    try:
        current = collect()
    except OSError as error:
        print(f"Could not fetch upstream docs: {error}")
        return 2
    empty = [n for section in ("models", "newest") for n, v in current[section].items() if not v]
    if empty:
        print(f"Extraction found nothing for: {', '.join(empty)}. The page format may have changed.")
        return 2
    if "--update" in sys.argv:
        SNAPSHOT.write_text(json.dumps(current, indent=2) + "\n")
        print(f"Updated {SNAPSHOT.name}")
        return 0
    changes = diff(json.loads(SNAPSHOT.read_text()), current)
    if not changes:
        print("No upstream changes since the snapshot.")
        return 0
    print("Upstream docs changed. Follow the Source review steps in MAINTAINING.md.\n")
    print("\n".join(f"- {change}" for change in changes))
    return 1


if __name__ == "__main__":
    sys.exit(main())
