# 玄学合参 Skill

面向 Codex 和 AI Agent 的玄学、命理、八字、梅花易数、六爻、风水、塔罗合参技能。

这个仓库不是简单的“算命提示词”，而是一套可复用的玄学分析流程：先选体系，再给断语，再列依据，再定应期，再给行动，再设验证点。它适合想让 AI 助手稳定处理八字命盘、梅花易数外应、六爻成败、风水方位、塔罗关系动力的人，也适合 Codex、Claude Code、Cursor 等 Agent Skills 兼容环境参考。

> 仅作文化、反思和策略参考。不能替代医疗、法律、投资、心理健康、紧急情况或安全建议。

## 适合什么搜索

如果你在找这些内容，这个 skill 就是为这类长尾问题设计的：

- AI 八字分析 skill
- Codex 玄学 skill
- 八字命理 AI 助手
- 梅花易数起卦脚本
- 六爻占卜 AI 工作流
- 风水方位分析提示词
- 塔罗牌 AI 解读提示词
- 命理、事业、财运、婚姻、健康趋势合参
- 邵雍象数、梅花易数、纳甲六爻、子平八字综合分析

## 支持体系

| 体系 | 适合问题 | 文件 |
| --- | --- | --- |
| 八字 / 子平 | 人生结构、大运流年、事业财运、婚恋健康趋势 | `references/bazi.md` |
| 梅花易数 | 突发事件、外应、近事应期、当前什么在动 | `references/meihua.md` |
| 六爻 / 纳甲 | 职位、合同、老板、薪资、产品起量、具体关系成败 | `references/liuyao.md` |
| 风水 / 方位 | 工位、朝向、领导位置、门窗气口、空间可见度 | `references/fengshui.md` |
| 塔罗 | 关系动力、心理结构、选择、转折点、象征性反思 | `references/tarot.md` |

## 核心特点

- 直接给断语，不绕圈。
- 区分高置信判断和低置信推测。
- 先让单一体系内部自洽，再做合参。
- 每个体系先判定 `可运行 / 可部分判断 / 阻塞`，缺关键输入时不硬编。
- 八字强调“先排盘事实，后解释”；梅花强调“时间、数字、外应”；六爻强调“自下而上六爻输入和纳甲层”；风水强调“形势为体，理气为用”；塔罗强调“牌阵、种子、正逆位和可复现抽牌”。
- 不用一个符号乱断全部。
- 已知事实优先于象征推演。
- 有 `router.md` 控制八字、梅花、六爻、风水、塔罗的系统选择。
- 有 `method-contracts.md` 统一输入卡和方法状态卡。
- 有 `output-templates.md` 固定单体系和多体系合参输出格式。
- 有 `examples.md` 提供不同语言和不同术数的触发案例。
- 支持梅花易数结构计算脚本。
- 支持塔罗牌阵抽牌脚本，输出 seed、牌位、正逆位，避免反复重抽。
- 支持隐私扫描脚本，防止公开仓库误放真实姓名、出生信息、家庭信息、职场信息。
- 支持 `validate_skill.py` 校验 skill 文件完整性。
- 对健康、死亡、法律、投资、安全等高风险问题设明确边界。

## 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill.git ~/.codex/skills/metaphysics-synthesis
```

然后重启或刷新 Codex skill。

## 中文案例

### 八字案例

```text
用八字看 2026-2036 年的事业和财运，严格区分命局结构、大运、流年触发点、高置信判断和低置信推测。
```

### 梅花易数案例

```text
用梅花易数看这个项目上线后是否对我转正有利。起心动念时间是 2026-06-12 10:36，外应是西北方主管在讨论排期。
```

### 六爻案例

```text
用六爻判断这个项目能不能成为升职的主功。六个数字从初爻到上爻是 5 / 4 / 25 / 12 / 22 / 17。
```

### 风水案例

```text
按风水方位看我的工位：我面向东南，主管在西北，大领导在南方，跨团队负责人在东方。这个格局对可见度和汇报机会有什么影响？
```

### 塔罗案例

```text
用五张塔罗牌阵看这次职业选择。请抽牌并显示 seed、牌位、正逆位、断语、行动和验证点。
```

## 梅花起卦脚本

```bash
python scripts/meihua_calc.py time 2026 6 12 10
python scripts/meihua_calc.py classic 7 4 27 10
python scripts/meihua_calc.py num 22 5 18
```

脚本只负责算主卦、动爻、互卦、变卦、体用生克；解释仍按 `references/meihua.md`。

## 塔罗抽牌脚本

```bash
python scripts/tarot_draw.py --spread relationship --question "这段合作会不会成熟？" --seed 42
python scripts/tarot_draw.py --spread five --question "职业选择" --json
```

脚本只负责牌阵、牌名、正逆位和 seed；解释仍按 `references/tarot.md`。

## 校验

```bash
python scripts/validate_skill.py
python scripts/privacy_check.py
```

校验内容包括必要文件、`SKILL.md` frontmatter、本地引用链接和脚本 smoke test。隐私扫描用于公开发布前检查敏感信息。

## 关键词

玄学 skill，命理 skill，八字 AI，八字命盘分析，子平命理，梅花易数，梅花易数起卦，邵雍象数，六爻占卜，纳甲六爻，风水方位，工位风水，塔罗牌解读，塔罗 AI，事业运，财运，婚姻运，感情运，健康趋势，Codex skill，AI Agent。
