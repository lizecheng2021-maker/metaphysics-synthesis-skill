#!/usr/bin/env python3
"""Validate multilingual README coverage and public-facing constraints."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]

README_RULES = {
    "README.md": ["BaZi", "Meihua Yishu", "Liuyao", "Feng Shui", "Tarot"],
    "README.zh-CN.md": ["八字", "梅花易数", "六爻", "风水", "塔罗"],
    "README.ko-KR.md": ["사주", "매화역수", "육효", "풍수", "타로"],
    "README.ja-JP.md": ["四柱推命", "梅花易数", "六爻", "風水", "タロット"],
    "README.fr-FR.md": ["BaZi", "Meihua Yishu", "Liuyao", "Feng Shui", "Tarot"],
    "README.es-ES.md": ["BaZi", "Meihua Yishu", "Liuyao", "Feng Shui", "Tarot"],
}

FORBIDDEN_VISIBLE_TERMS = [
    "llms.txt",
    "SEO",
    "GEO",
    "AEO",
    "answer engine",
    "AI-readable",
    "Search Keywords",
    "Búsquedas objetivo",
    "Requêtes de recherche",
    "关键词",
]

REQUIRED_COMMAND_SNIPPETS = [
    "git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git",
    "python3 scripts/validate_skill.py",
    "~/.codex/skills",
    "~/.claude/skills",
    "AGENT_SKILLS_DIR",
    "ln -sfn",
]

SOCIAL_MARKERS = {
    "README.md": "Share On X / Twitter",
    "README.zh-CN.md": "X / Twitter 分享文案",
    "README.ko-KR.md": "X / Twitter Post",
    "README.ja-JP.md": "X / Twitter 投稿文",
    "README.fr-FR.md": "Publication X / Twitter",
    "README.es-ES.md": "Publicación para X / Twitter",
}
SOCIAL_IMAGES = {
    "README.md": "assets/social/generated/twitter-card-en.png",
    "README.zh-CN.md": "assets/social/generated/twitter-card-zh-CN.png",
    "README.ko-KR.md": "assets/social/generated/twitter-card-ko-KR.png",
    "README.ja-JP.md": "assets/social/generated/twitter-card-ja-JP.png",
    "README.fr-FR.md": "assets/social/generated/twitter-card-fr-FR.png",
    "README.es-ES.md": "assets/social/generated/twitter-card-es-ES.png",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_readme(path: pathlib.Path, required_terms: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if len(text) < 2000:
        fail(f"{path.name} is too short for a complete localized guide")
    missing_terms = [term for term in required_terms if term not in text]
    if missing_terms:
        fail(f"{path.name} missing localized method terms: {', '.join(missing_terms)}")
    missing_commands = [snippet for snippet in REQUIRED_COMMAND_SNIPPETS if snippet not in text]
    if missing_commands:
        fail(f"{path.name} missing install snippets: {', '.join(missing_commands)}")
    wiki_count = len(re.findall(r"https://[a-z]+\.wikipedia\.org/", text))
    if wiki_count < 5:
        fail(f"{path.name} should include at least five Wikipedia method links")
    forbidden = [term for term in FORBIDDEN_VISIBLE_TERMS if term in text]
    if forbidden:
        fail(f"{path.name} contains visible discoverability/internal terms: {', '.join(forbidden)}")
    if "docs/" in text:
        fail(f"{path.name} references removed docs/ directory")
    image = SOCIAL_IMAGES[path.name]
    if image not in text:
        fail(f"{path.name} missing localized social image {image}")
    if not (ROOT / image).is_file():
        fail(f"{path.name} references missing social image file {image}")
    marker = SOCIAL_MARKERS[path.name]
    if marker not in text:
        fail(f"{path.name} missing localized X/Twitter section")


def main() -> None:
    for filename, required_terms in README_RULES.items():
        path = ROOT / filename
        if not path.is_file():
            fail(f"missing {filename}")
        check_readme(path, required_terms)
    print("OK: multilingual README guides validated")


if __name__ == "__main__":
    main()
