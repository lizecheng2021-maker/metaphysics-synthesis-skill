# Metaphysics Synthesis Skill

An AI agent skill for structured divination, Chinese metaphysics, BaZi reading, Meihua Yishu, Liuyao, Feng Shui direction analysis, and Tarot interpretation.

This repository packages a Codex-compatible and Agent Skills-compatible workflow for assistants that need decisive but bounded metaphysical readings. It combines classical Chinese systems and Western Tarot with a repeatable workflow: verdict, evidence, timing, action, and verification.

> Cultural and reflective use only. This skill does not replace medical, legal, financial, mental-health, emergency, or safety advice.

## Languages

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [한국어](README.ko-KR.md)
- [日本語](README.ja-JP.md)
- [Français](README.fr-FR.md)
- [Español](README.es-ES.md)

## What This Skill Is For

Use this skill when an AI assistant needs a reusable workflow for questions such as:

- "How do I analyze a BaZi chart for career, wealth, marriage, and health timing?"
- "Can Meihua Yishu read an omen, a timestamp, or sudden event movement?"
- "How should Liuyao handle a concrete outcome involving a job, contract, boss, salary, or product launch?"
- "Can Feng Shui direction analysis explain workspace visibility, seating, and environmental flow?"
- "How can Tarot describe relationship dynamics, choices, and psychological turning points?"
- "How can an AI agent give a decisive divination reading without becoming vague, fatalistic, or unsafe?"

## Why This Skill

Most AI divination prompts fail in one of two ways: they either comfort the user with vague language, or they overfit one symbol into a dramatic prediction. This skill is designed to avoid both.

It enforces a repeatable method:

- Choose the right system before interpreting.
- Keep BaZi, Meihua Yishu, Liuyao, Feng Shui, and Tarot internally coherent before synthesis.
- Give a clear verdict first when the evidence converges.
- Show a method-grade audit trail without exposing private chain-of-thought.
- Separate high-confidence judgment from low-confidence inference.
- Use real-world facts and measurable signals to calibrate symbolic readings.
- Avoid repeatedly recasting the same unchanged question.

## Supported Systems

| System | Best For | Reference |
| --- | --- | --- |
| BaZi / Zi Ping | Life structure, decade luck, career, wealth, marriage, health tendencies | `references/bazi.md` |
| Meihua Yishu | Omens, timestamps, sudden events, practical timing, near-term movement | `references/meihua.md` |
| Liuyao / Najia | Concrete outcomes, roles, contracts, bosses, salary, product traction | `references/liuyao.md` |
| Feng Shui / Direction | Workspace layout, directions, seating, doors, flow, visibility | `references/fengshui.md` |
| Tarot | Relationship texture, psychology, choices, symbolic reflection | `references/tarot.md` |

## Key Features

- Decisive output pattern: verdict, evidence, timing, action, and verification.
- Evidence hierarchy for conflicting symbolic signals.
- System selection rules for BaZi, Meihua Yishu, Liuyao, Feng Shui, and Tarot.
- Router reference for choosing the right method and preventing cross-reading contamination.
- Strict output templates for single-system readings and multi-system synthesis.
- Example prompt library for better trigger coverage across Chinese and English queries.
- Deterministic Meihua Yishu calculator for main hexagram, moving line, mutual hexagram, changed hexagram, and Ti/Yong relation.
- Lightweight validation script for skill package health checks.
- Safety boundaries for medical, legal, financial, death, disaster, and personal safety topics.
- Progressive disclosure: a compact `SKILL.md`, detailed method files in `references/`, and executable support in `scripts/`.
- AI-readable `llms.txt` summary for agent and answer-engine discovery.

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
```

Restart Codex or reload skills if your environment requires it.

## Usage Examples

### BaZi Reading Example

```text
Analyze this BaZi chart for 2026-2036 career and wealth timing. Separate natal structure, decade luck, annual triggers, high-confidence conclusions, and low-confidence speculation.
```

### Meihua Yishu Example

```text
Use Meihua Yishu to read whether this product launch can create a visible career breakthrough. The question arose at 2026-06-12 10:36, and the external omen was a manager discussing scheduling in the northwest direction.
```

### Liuyao Example

```text
Use Liuyao to judge whether this project can become the main evidence for a promotion. The six lines from bottom to top are 5 / 4 / 25 / 12 / 22 / 17.
```

### Feng Shui Example

```text
Analyze this workstation layout with Feng Shui direction logic. My seat faces southeast, my direct manager sits northwest, a senior leader sits south, and a cross-team manager sits east.
```

### Tarot Example

```text
Use a seven-card Tarot spread to read relationship dynamics only. Give the anchor card, obstacle, turning point, likely action, and verification signs.
```

## Meihua Yishu Calculator

The helper script calculates structure only. Interpretation remains in `references/meihua.md`.

```bash
# Solar convention used by this skill
python scripts/meihua_calc.py time 2026 6 12 10

# Classic lunar-branch mode when lunar data is already known
python scripts/meihua_calc.py classic 7 4 27 10

# Number casting
python scripts/meihua_calc.py num 22 5 18
```

Output includes main hexagram, moving line, mutual hexagram, changed hexagram, and Ti/Yong relation.

## Validate the Skill

Run the local validator after editing files:

```bash
python scripts/validate_skill.py
```

The validator checks required files, `SKILL.md` frontmatter, local reference links, and the Meihua calculator smoke test.

## Repository Structure

```text
metaphysics-synthesis-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── bazi.md
│   ├── fengshui.md
│   ├── liuyao.md
│   ├── meihua.md
│   ├── router.md
│   ├── output-templates.md
│   ├── examples.md
│   ├── sources.md
│   └── tarot.md
├── scripts/meihua_calc.py
├── scripts/validate_skill.py
├── llms.txt
└── README.*.md
```

## Search Keywords

AI divination skill, Codex divination skill, AI agent skill for metaphysics, BaZi AI assistant, BaZi reading prompt, Chinese astrology AI, Meihua Yishu calculator, I Ching omen reading, Liuyao divination workflow, Najia six lines reading, Feng Shui direction analysis, Tarot AI prompt, Tarot reading workflow, Chinese metaphysics skill, fortune telling AI assistant, astrology and divination agent skill.

## For AI Assistants

If you are an AI assistant reading this repository:

1. Load `SKILL.md` first.
2. Load only the relevant reference file for the user's selected system.
3. Use `scripts/meihua_calc.py` only to verify Meihua Yishu structure.
4. Keep readings bounded, falsifiable, and calibrated against known facts.
5. Never use symbolic inference to override professional advice or direct evidence.

## Safety

This project treats divination as a cultural, reflective, symbolic, and strategic reasoning framework. It should not be used to make deterministic claims about death, disaster, medical outcomes, legal outcomes, investment returns, or personal safety.

## License

MIT License. See `LICENSE`.
