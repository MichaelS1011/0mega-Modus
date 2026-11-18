"""Single source of truth for the release version.

The version is declared exactly once, in `pyproject.toml`. Release scripts
read it from there and must not hard-code it. The tag gate fails the build
when the commit being built carries a release tag that contradicts the
declared version, which prevents publishing archives under a wrong tag.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_version() -> str:
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not match:
        raise SystemExit("version not found in pyproject.toml")
    return match.group(1)


def _git(*args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None  # git unavailable; gates are skipped, not faked
    return result.stdout if result.returncode == 0 else None


def tag_gate(version: str) -> None:
    """Fail when HEAD's release tag contradicts a committed pyproject version.

    A tagged HEAD that differs from pyproject.toml is drift — unless
    pyproject.toml itself has uncommitted changes, which marks a pending
    version bump and only produces a note.
    """
    head_tags = _git("tag", "--points-at", "HEAD")
    expected = f"v{version}"
    if head_tags is not None:
        tags = [tag for tag in head_tags.split() if tag.startswith("v")]
        if tags and expected not in tags:
            dirty = bool((_git("status", "--porcelain", "--", "pyproject.toml") or "").strip())
            if dirty:
                print(
                    f"NOTE: HEAD is tagged {', '.join(tags)} and pyproject.toml declares "
                    f"{version} with uncommitted changes (pending release bump)"
                )
            else:
                raise SystemExit(
                    f"version drift: HEAD is tagged {', '.join(tags)} "
                    f"but the committed pyproject.toml declares {version}"
                )
    latest = _git("describe", "--tags", "--abbrev=0")
    if latest:
        newest = latest.strip()
        if newest != expected:
            print(
                f"NOTE: newest reachable tag is {newest}; pyproject.toml declares "
                f"{version} (expected while {version} is unreleased)"
            )
