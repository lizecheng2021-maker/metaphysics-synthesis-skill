#!/usr/bin/env python3
"""Render localized social cards from the shared background image."""

from __future__ import annotations

import pathlib
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
BACKGROUND = ROOT / "assets/social/generated/metaphysics-synthesis-twitter-bg.png"
OUT_DIR = ROOT / "assets/social/generated"

FONT_LATIN = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_CJK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

W, H = 1600, 900

CARDS = {
    "en": {
        "filename": "twitter-card-en.png",
        "title": "Metaphysics\nSynthesis Skill",
        "subtitle": "BaZi · Meihua · Liuyao\nFeng Shui · Tarot",
        "tag": "For AI Agents",
        "font": FONT_LATIN,
    },
    "zh": {
        "filename": "twitter-card-zh-CN.png",
        "title": "玄学合参\nAgent Skill",
        "subtitle": "八字 · 梅花 · 六爻\n风水 · 塔罗",
        "tag": "给 AI Agent 的结构化术数工作流",
        "font": FONT_CJK,
    },
    "ko": {
        "filename": "twitter-card-ko-KR.png",
        "title": "형이상학 종합\nAgent Skill",
        "subtitle": "사주 · 매화역수 · 육효\n풍수 · 타로",
        "tag": "AI Agent를 위한 구조화된 상징 추론",
        "font": FONT_CJK,
    },
    "ja": {
        "filename": "twitter-card-ja-JP.png",
        "title": "形而上学総合\nAgent Skill",
        "subtitle": "四柱推命 · 梅花易数 · 六爻\n風水 · タロット",
        "tag": "AI Agent のための構造化された占術ワークフロー",
        "font": FONT_CJK,
    },
    "fr": {
        "filename": "twitter-card-fr-FR.png",
        "title": "Synthèse\nMétaphysique",
        "subtitle": "BaZi · Meihua · Liuyao\nFeng Shui · Tarot",
        "tag": "Pour AI Agents",
        "font": FONT_LATIN,
    },
    "es": {
        "filename": "twitter-card-es-ES.png",
        "title": "Síntesis\nMetafísica",
        "subtitle": "BaZi · Meihua · Liuyao\nFeng Shui · Tarot",
        "tag": "Para AI Agents",
        "font": FONT_LATIN,
    },
}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def fit_font(text: str, path: str, start: int, max_width: int) -> ImageFont.FreeTypeFont:
    size = start
    while size >= 20:
        candidate = font(path, size)
        dummy = Image.new("RGB", (10, 10))
        draw = ImageDraw.Draw(dummy)
        widths = [draw.textbbox((0, 0), line, font=candidate)[2] for line in text.splitlines()]
        if max(widths) <= max_width:
            return candidate
        size -= 2
    return font(path, 20)


def draw_text_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: tuple[int, int, int], spacing: int) -> None:
    x, y = xy
    shadow = (0, 12, 28, 210)
    for dx, dy in [(3, 3), (0, 4)]:
        draw.multiline_text((x + dx, y + dy), text, font=fnt, fill=shadow, spacing=spacing)
    draw.multiline_text((x, y), text, font=fnt, fill=fill, spacing=spacing)


def render_card(spec: dict[str, str]) -> pathlib.Path:
    image = Image.open(BACKGROUND).convert("RGB")
    image = image.resize((W, H), Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    panel = (70, 128, 760, 724)
    draw.rounded_rectangle(panel, radius=34, fill=(2, 14, 32, 132), outline=(216, 169, 91, 92), width=2)
    draw.rectangle((70, 128, 82, 724), fill=(21, 164, 217, 150))
    draw.line((118, 174, 650, 174), fill=(218, 171, 93, 168), width=2)

    title_font = fit_font(spec["title"], spec["font"], 76, 580)
    subtitle_font = fit_font(spec["subtitle"], spec["font"], 36, 560)
    tag_font = fit_font(spec["tag"], spec["font"], 26, 560)

    draw_text_block(draw, (118, 220), spec["title"], title_font, (245, 239, 222), 14)
    draw_text_block(draw, (122, 438), spec["subtitle"], subtitle_font, (102, 219, 255), 12)

    tag = spec["tag"]
    wrapped = "\n".join(textwrap.wrap(tag, width=28, break_long_words=False)) if len(tag) > 28 else tag
    draw.rounded_rectangle((118, 610, 650, 676), radius=20, fill=(218, 171, 93, 42), outline=(218, 171, 93, 110), width=1)
    draw_text_block(draw, (146, 625), wrapped, tag_font, (236, 202, 139), 8)

    composed = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")
    out = OUT_DIR / spec["filename"]
    composed.save(out, quality=95)
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for code, spec in CARDS.items():
        out = render_card(spec)
        print(f"{code}: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
