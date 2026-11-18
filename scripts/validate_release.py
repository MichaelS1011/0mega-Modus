#!/usr/bin/env python3
"""Static integrity checks for OMEGA Modus source and release artefacts.

The version is declared exactly once, in pyproject.toml; see scripts/_version.py.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import zipfile

from _version import read_version

ROOT = Path(__file__).resolve().parents[1]
VERSION = read_version()
OUTPUT = ROOT / "dist" / f"omega-modus-v{VERSION}"
REQUIRED_METHODS = ["PDCA", "Five Whys", "Ishikawa", "Poka-Yoke", "FMEA", "Pareto", "A3", "Kaizen"]
REQUIRED_DIRS = ["skills/omega-modus/references", "evaluation/scenarios", "scripts", "docs"]
REQUIRED_BUNDLES = [
    "codex/AGENTS.md",
    "codex/.agents/skills/omega-modus/SKILL.md",
    "claude-code/.claude/skills/omega-modus/SKILL.md",
    "gemini-cli/GEMINI.md",
    "gemini-cli/.agents/skills/omega-modus/SKILL.md",
    "cursor/.cursor/rules/omega-modus.mdc",
    "github-copilot/.github/copilot-instructions.md",
    "github-copilot/.github/skills/omega-modus/SKILL.md",
    "chatgpt/instructions.md",
    "chatgpt/skill/omega-modus/SKILL.md",
    "generic/OMEGA-MODUS-PROMPT.md",
]
ADAPTERS = ["codex", "claude-code", "gemini-cli", "cursor", "github-copilot", "chatgpt", "generic"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    for item in REQUIRED_DIRS:
        if not (ROOT / item).is_dir():
            fail(f"missing directory: {item}")

    skill = ROOT / "skills/omega-modus/SKILL.md"
    skill_text = skill.read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: omega-modus\n"):
        fail("SKILL.md frontmatter is missing or malformed")
    if "description:" not in skill_text.split("---", 2)[1]:
        fail("SKILL.md description field missing")

    refs = ROOT / "skills/omega-modus/references"
    expected_refs = ["CORE_PROTOCOL.md", "QUALITY_INTELLIGENCE.md", "SAFETY_AND_TRUST.md", "WORKFLOWS.md"]
    for filename in expected_refs:
        if not (refs / filename).is_file():
            fail(f"missing skill reference: {filename}")

    method_text = (refs / "QUALITY_INTELLIGENCE.md").read_text(encoding="utf-8")
    for method in REQUIRED_METHODS:
        if method.lower() not in method_text.lower():
            fail(f"quality method not covered: {method}")

    scenario_files = list((ROOT / "evaluation/scenarios").glob("S*.md"))
    if len(scenario_files) < 12:
        fail(f"expected at least 12 evaluation scenarios, found {len(scenario_files)}")

    marker = OUTPUT / ".omegamodus-generated-by-build_release.py"
    if not marker.is_file():
        fail(f"release output marker missing: {marker.relative_to(ROOT)}; run scripts/build_release.py")

    for relative in REQUIRED_BUNDLES:
        if not (OUTPUT / "bundles" / relative).is_file():
            fail(f"missing generated bundle file: {OUTPUT.relative_to(ROOT)}/bundles/{relative}; run scripts/build_release.py")

    cursor_rule = (OUTPUT / "bundles/cursor/.cursor/rules/omega-modus.mdc").read_text(encoding="utf-8")
    if not cursor_rule.startswith("---\ndescription:") or "alwaysApply: false" not in cursor_rule:
        fail("Cursor rule frontmatter missing expected fields")

    archives = OUTPUT / "archives"
    expected_archives = [f"omega-modus-v{VERSION}-{name}.zip" for name in ADAPTERS] + [
        f"omega-modus-v{VERSION}-source.zip",
        f"omega-modus-v{VERSION}-all-platform-bundles.zip",
    ]
    for filename in expected_archives:
        archive = archives / filename
        if not archive.is_file():
            fail(f"missing archive: {archive.relative_to(ROOT)}")
        try:
            with zipfile.ZipFile(archive) as zf:
                bad_member = zf.testzip()
                if bad_member:
                    fail(f"corrupt member in {filename}: {bad_member}")
        except zipfile.BadZipFile:
            fail(f"invalid ZIP archive: {filename}")

    sums_file = OUTPUT / "SHA256SUMS.txt"
    if not sums_file.is_file():
        fail("SHA256SUMS.txt missing")
    for line in sums_file.read_text(encoding="utf-8").splitlines():
        digest, filename = line.split("  ", 1)
        actual = hashlib.sha256((archives / filename).read_bytes()).hexdigest()
        if digest != actual:
            fail(f"SHA-256 mismatch: {filename}")

    all_bundle = archives / f"omega-modus-v{VERSION}-all-platform-bundles.zip"
    with zipfile.ZipFile(all_bundle) as zf:
        members = set(zf.namelist())
        for name in ADAPTERS:
            expected_member = f"platform-zips/omega-modus-v{VERSION}-{name}.zip"
            if expected_member not in members:
                fail(f"all-platform archive missing {expected_member}")
        if "SHA256SUMS.txt" not in members:
            fail("all-platform archive is missing SHA256SUMS.txt")

    print("PASS: source structure, quality methods, evaluation scenarios, adapter bundles, archives, and checksums.")
    print("NOTE: these checks validate packaging and repository integrity, not model behavior or live platform activation.")


if __name__ == "__main__":
    main()
