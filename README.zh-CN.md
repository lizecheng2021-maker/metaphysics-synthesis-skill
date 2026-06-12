# 玄学合参 Skill

面向 Codex / AI Agent 的玄学、命理、八字、梅花易数、六爻、风水、塔罗合参技能。

它不是用来故弄玄虚的，而是把传统象数、命理和塔罗拆成一个可复用的分析流程：先断语，再证据，再应期，再行动，再验证。

> 仅作文化、反思和策略参考。不能替代医疗、法律、投资、心理健康或安全建议。

## 适合什么问题

- 八字：人生结构、大运流年、事业财运、婚恋健康趋势。
- 梅花易数：突发事件、外应、近事应期、当前什么在动。
- 六爻：职位、合同、老板、薪资、项目起量、具体关系成败。
- 风水方位：工位、方位、领导位置、可见度、空间流动。
- 塔罗：关系动力、心理结构、选择、象征性反思。

## 核心特点

- 直接给 `断语`，不绕。
- 区分高置信判断和低置信推测。
- 先让单一体系内部自洽，再做合参。
- 不用一个符号乱断全部。
- 已知事实优先于象征推演。
- 对健康、死亡、法律、投资等高风险问题设边界。

## 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
```

然后重启或刷新 Codex skill。

## 示例

```text
严格按梅花易数看这个项目上线后是否对我转正有利。起心动念时间是2026-06-12 10:36，外应是西北方主管在讨论排期。
```

```text
用八字看2026-2036事业和财运，区分命局结构、大运、流年触发点。
```

```text
用塔罗看这段关系的动力，不要看八字，不要串旧卦。
```

## 梅花起卦脚本

```bash
python scripts/meihua_calc.py time 2026 6 12 10
python scripts/meihua_calc.py classic 7 4 27 10
python scripts/meihua_calc.py num 22 5 18
```

脚本只负责算主卦、动爻、互卦、变卦、体用生克；解释仍按 `references/meihua.md`。

## 关键词

玄学, 命理, 八字, 子平, 梅花易数, 邵雍, 六爻, 纳甲, 风水, 塔罗, Codex skill, AI Agent, divination, BaZi, Meihua Yishu, Liuyao, Feng Shui, Tarot.
