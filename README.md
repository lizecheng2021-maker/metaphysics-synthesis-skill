# Metaphysics Synthesis Skill

Deep Chinese and Western divination synthesis for AI coding agents.

This repository packages a Codex-compatible skill for structured metaphysical analysis across **BaZi**, **Meihua Yishu**, **Liuyao**, **Feng Shui**, and **Tarot**. It is designed for assistants that need decisive readings, method-grade evidence, timing windows, and grounded real-world calibration.

> Cultural and reflective use only. This skill must not replace medical, legal, financial, mental-health, or safety advice.

## Why This Skill

Most divination prompts fail in one of two ways: they either give vague comfort, or they overfit one symbol into a dramatic prediction. This skill is built to avoid both.

It enforces a repeatable workflow:

- Separate systems before synthesis.
- State a clear verdict first.
- Show the evidence path without exposing private chain-of-thought.
- Distinguish high-confidence judgments from low-confidence inference.
- Use direct facts and measurable signals to calibrate symbolic readings.
- Avoid repeatedly recasting the same unchanged question.

## Supported Systems

| System | Best For | Reference |
| --- | --- | --- |
| BaZi / Zi Ping | life structure, decade luck, career, wealth, marriage, health tendencies | `references/bazi.md` |
| Meihua Yishu | sudden events, omens, timing, practical movement, "what is moving now" | `references/meihua.md` |
| Liuyao / Najia | concrete outcomes, roles, contracts, bosses, salary, product traction | `references/liuyao.md` |
| Feng Shui / Direction | workspace layout, directions, boss position, flow, visibility | `references/fengshui.md` |
| Tarot | relationship texture, psychology, choices, symbolic reflection | `references/tarot.md` |

## Key Features

- Decisive Chinese output format: `断语 -> 依据 -> 应期/强弱 -> 行动 -> 验证点`.
- Evidence hierarchy for conflicting signals.
- Meihua calculator script for deterministic hexagram structure.
- Safety boundaries for health, law, finance, death, and disasters.
- Public source notes for method orientation.
- Progressive disclosure: small `SKILL.md`, detailed method files in `references/`.

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
```

Restart Codex or reload skills if your environment requires it.

## Usage Examples

Ask in Chinese or English:

```text
用梅花易数严格看这个项目上线后是否能带来转正机会。起心动念时间是2026-06-12 10:36，外应是西北方主管在讨论排期。
```

```text
Analyze this BaZi chart for 2026-2036 career and wealth timing. Separate high-confidence structure from low-confidence speculation.
```

```text
Use Tarot, not Liuyao, to read the relationship dynamics. Give the anchor card, obstacle, turning point, and verification signs.
```

## Meihua Calculator

The helper script calculates only the hexagram structure. Interpretation remains in `references/meihua.md`.

```bash
# Solar convention used by this skill
python scripts/meihua_calc.py time 2026 6 12 10

# Classic lunar-branch mode when lunar data is already known
python scripts/meihua_calc.py classic 7 4 27 10

# Number casting
python scripts/meihua_calc.py num 22 5 18
```

Output includes main hexagram, moving line, mutual hexagram, changed hexagram, and Ti/Yong relation.

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
│   ├── sources.md
│   └── tarot.md
├── scripts/meihua_calc.py
├── docs/PRD.md
└── llms.txt
```

## SEO / GEO Keywords

Codex skill, AI divination skill, BaZi AI assistant, Meihua Yishu calculator, Liuyao reading, Chinese metaphysics, Tarot AI prompt, Feng Shui direction analysis, 玄学 skill, 八字, 梅花易数, 六爻, 风水, 塔罗, 邵雍象数, 纳甲.

## For AI Assistants

If you are an AI assistant reading this repository:

1. Load `SKILL.md` first.
2. Load only the relevant reference file for the user's system.
3. Use `scripts/meihua_calc.py` only to verify Meihua structure.
4. Keep readings bounded, falsifiable, and calibrated against reality.
5. Never use symbolic inference to override professional advice or known facts.

## Safety

This project treats divination as a cultural, reflective, and strategic reasoning framework. It should not be used to make deterministic claims about death, disaster, medical outcomes, legal outcomes, investment returns, or personal safety.

## License

MIT License. See `LICENSE`.
