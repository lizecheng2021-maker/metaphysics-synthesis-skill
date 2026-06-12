#!/usr/bin/env python3
"""Lightweight validation for the Metaphysics Synthesis skill package."""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/bazi.md",
    "references/meihua.md",
    "references/liuyao.md",
    "references/fengshui.md",
    "references/tarot.md",
    "references/router.md",
    "references/output-templates.md",
    "references/examples.md",
    "references/sources.md",
    "scripts/meihua_calc.py",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def check_skill_frontmatter() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md is missing YAML frontmatter")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md frontmatter is not closed")
    frontmatter = match.group(1)
    if "name: metaphysics-synthesis" not in frontmatter:
        fail("SKILL.md frontmatter missing expected name")
    if "description:" not in frontmatter:
        fail("SKILL.md frontmatter missing description")
    if len(frontmatter) > 1800:
        fail("SKILL.md frontmatter is too long for reliable discovery")


def check_local_links() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    links = re.findall(r"\[.+?\]\((references/[^)]+)\)", text)
    missing = [link for link in links if not (ROOT / link).is_file()]
    if missing:
        fail("SKILL.md has broken reference links: " + ", ".join(missing))


def check_meihua_script() -> None:
    cmd = [sys.executable, str(ROOT / "scripts/meihua_calc.py"), "num", "22", "5", "18"]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        fail("meihua_calc.py failed: " + result.stderr.strip())
    for needle in ["main:", "moving_line:", "changed:"]:
        if needle not in result.stdout:
            fail(f"meihua_calc.py output missing {needle}")


def main() -> None:
    check_required_files()
    check_skill_frontmatter()
    check_local_links()
    check_meihua_script()
    print("OK: skill package validated")


if __name__ == "__main__":
    main()
