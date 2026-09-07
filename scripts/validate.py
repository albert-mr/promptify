"""Validate the shipped skill and plugin with Python's standard library."""

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/promptify"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
check(plugin.get("name") == marketplace.get("name") == "promptify", "Plugin names disagree")
check(bool(plugin.get("description")), "Plugin description missing")
version = plugin.get("version", "")
check(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), "Invalid plugin version")
check(f"## [{version}] - " in (ROOT / "CHANGELOG.md").read_text(), "Version missing from changelog")
check(bool(marketplace.get("owner", {}).get("name")), "Marketplace owner missing")
entries = marketplace.get("plugins", [])
check(len(entries) == 1, "Expected one marketplace plugin")
for entry in entries:
    check(entry.get("name") == plugin["name"] and entry.get("source") == "./", "Invalid plugin entry")
    check(entry.get("description") == plugin.get("description") == marketplace.get("description"), "Descriptions disagree")

entrypoint = (SKILL / "SKILL.md").read_text()
frontmatter = re.match(r"\A---\n(.*?)\n---\n", entrypoint, re.S)
check(frontmatter is not None, "Skill frontmatter missing")
if frontmatter:
    check(bool(re.search(r"^name: promptify$", frontmatter[1], re.M)), "Invalid skill name")
    description = re.search(r"^description: (.+)$", frontmatter[1], re.M)
    check(description is not None and len(description[1]) <= 1024, "Invalid skill description")

refs = set((SKILL / "references").glob("*.md"))
check({p.name for p in refs} == {"claude-families.md", "openai-families.md", "detection-fallbacks.md"}, "Unexpected or missing skill reference")
for path in [SKILL / "SKILL.md", *refs]:
    check(not re.search(r"/goal\b", path.read_text()), f"Removed mode remains in {path.relative_to(ROOT)}")
for path in (ROOT / ".claude-plugin").glob("*.json"):
    check(not re.search(r"/goal\b", path.read_text()), f"Removed mode remains in {path.relative_to(ROOT)}")
for path in refs:
    check(f"references/{path.name}" in entrypoint, f"Unreachable reference: {path.name}")

discovery = ROOT / ".agents/skills/promptify"
check(discovery.is_symlink() and discovery.resolve() == SKILL, "Broken Codex discovery symlink")

# ponytail: inline Markdown links only; use a Markdown parser if docs adopt reference-style links.
for path in [
    ROOT / "README.md", ROOT / "MAINTAINING.md", SKILL / "SKILL.md", *sorted(refs),
    *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "tests").glob("*.md")),
]:
    content = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", content):
        link = urlsplit(target)
        if not link.scheme and link.path:
            check((path.parent / unquote(link.path)).exists(), f"Broken link in {path.relative_to(ROOT)}: {target}")

if errors:
    raise SystemExit("\n".join(f"FAIL: {error}" for error in errors))
print(f"Validation passed: promptify {version}, manifests, skill, references, links, and discovery symlink")
