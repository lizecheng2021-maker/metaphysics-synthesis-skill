# Twitter / X Launch Kit

Use one unified visual identity for all languages. Each README uses a localized image with text already rendered into the card.

Shared background image:

```text
assets/social/generated/metaphysics-synthesis-twitter-bg.png
```

Localized ready-to-post cards:

```text
assets/social/generated/twitter-card-en.png
assets/social/generated/twitter-card-zh-CN.png
assets/social/generated/twitter-card-ko-KR.png
assets/social/generated/twitter-card-ja-JP.png
assets/social/generated/twitter-card-fr-FR.png
assets/social/generated/twitter-card-es-ES.png
```

Regenerate cards:

```bash
python3 scripts/render_social_cards.py
```

Recommended post image size: 1600 x 900.

Recommended overlay:

```text
Metaphysics Synthesis Skill
BaZi · Meihua · Liuyao · Feng Shui · Tarot
For AI Agents
```

Alt text:

```text
A dark blue and gold social card background with I Ching hexagram lines, a compass-like luopan, tarot cards, glowing AI network nodes, mountains, and a clean empty area on the left for a headline.
```

## English Long Post

```text
I built an open-source Agent Skill for structured metaphysical reasoning:

Metaphysics Synthesis Skill

It covers:
• BaZi / Four Pillars
• Meihua Yishu / I Ching omen reading
• Liuyao / Najia
• Feng Shui direction analysis
• Tarot spreads

This is not a vague fortune-telling prompt.

The goal is to make AI divination less messy and more procedural:
1. Pick the right method for the question.
2. Check whether the input is complete.
3. Mark each method as runnable, partial, or blocked.
4. Read each system internally before synthesis.
5. Give verdict, evidence, timing, action, and verification signals.

The repo includes:
• A compact SKILL.md router
• Method references for BaZi, Meihua, Liuyao, Feng Shui, and Tarot
• A Meihua structure calculator
• A reproducible Tarot draw script with seed and reversals
• Multilingual README guides
• Validation and privacy-check scripts

It is designed for Codex, Claude Code, and any AI agent that can load a local skill folder.

The interesting part is not “AI predicts fate.”
The interesting part is building a disciplined interface between symbolic systems and agent workflows.

GitHub:
https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill
```

## Chinese Long Post

```text
我做了一个开源 AI Agent Skill：

Metaphysics Synthesis Skill
玄学合参 Skill

它覆盖：
• 八字 / 子平命理
• 梅花易数 / 外应起卦
• 六爻 / 纳甲
• 风水 / 方位分析
• 塔罗 / 牌阵解读

这不是“玄学提示词”。

我想解决的问题是：AI 很容易把玄学回答成一团模糊的安慰话。
八字、梅花、六爻、风水、塔罗各有自己的问题边界、输入要求和判断逻辑，不能混成一种“感觉流”。

所以这个 skill 做了几件事：
1. 先判断问题适合哪个体系。
2. 再检查输入是否足够。
3. 把每个方法标记为可运行、可部分判断、阻塞。
4. 单体系内部先自洽，再合参。
5. 输出断语、依据、应期、行动和验证点。

仓库里包含：
• SKILL.md 总路由
• 八字、梅花、六爻、风水、塔罗方法文件
• 梅花易数结构计算脚本
• 可复现的塔罗抽牌脚本
• 中英日韩法西多语言 README
• 校验脚本和隐私检查脚本

它支持 Codex、Claude Code，也支持任何能读取本地 skill 目录的 AI Agent。

我觉得最有意思的不是“让 AI 算命”，而是把传统象征系统整理成可复用、可校验、可迁移的 Agent 工作流。

GitHub:
https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill
```

## Korean Long Post

```text
I built an open-source Agent Skill for structured metaphysical reasoning:

Metaphysics Synthesis Skill

It supports:
• 사주팔자 / BaZi
• 매화역수 / I Ching omen reading
• 육효 / Najia
• 풍수 방향 분석
• 타로 배열

This is not a generic fortune-telling prompt.

Most AI divination answers become too vague:
a few comforting words, one symbolic clue, and no clear method.

This skill tries to make the process cleaner:
1. Choose the right system for the question.
2. Check whether the input is complete.
3. Mark the method as runnable, partial, or blocked.
4. Read each system before mixing them.
5. Output verdict, evidence, timing, action, and verification signals.

The repo includes:
• A compact SKILL.md router
• References for BaZi, Meihua, Liuyao, Feng Shui, and Tarot
• A Meihua hexagram calculator
• A reproducible Tarot draw script with seed
• Korean, English, Chinese, Japanese, French, and Spanish README guides
• Validation and privacy-check scripts

It works with Codex, Claude Code, and any AI agent that can load a local skill folder.

The point is not “AI tells the future.”
The point is building a disciplined workflow for symbolic reasoning.

GitHub:
https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill
```

## Japanese Long Post

```text
I released an open-source Agent Skill for structured metaphysical reasoning:

Metaphysics Synthesis Skill

It covers:
• 四柱推命 / BaZi
• 梅花易数 / 易占
• 六爻 / 納甲
• 風水方位分析
• タロットスプレッド

This is not just a fortune-telling prompt.

AI can imitate the tone of divination very easily.
But stable readings need structure:
What is the question?
Which method fits?
Is the input complete?
What is evidence, and what is only a low-confidence inference?

This skill turns that into a workflow:
1. Route the question to the right system.
2. Validate the input.
3. Mark each method as runnable, partial, or blocked.
4. Read each method internally before synthesis.
5. Return verdict, evidence, timing, action, and verification signals.

The repo includes:
• SKILL.md routing
• Method references for BaZi, Meihua, Liuyao, Feng Shui, and Tarot
• Meihua structure calculator
• Reproducible Tarot draw script
• Multilingual README guides
• Validation and privacy-check scripts

It can be used with Codex, Claude Code, or any AI agent that can read a local skill folder.

GitHub:
https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill
```

## French Long Post

```text
I built an open-source Agent Skill for structured metaphysical readings:

Metaphysics Synthesis Skill

It covers:
• BaZi / quatre piliers
• Meihua Yishu / Yi Jing omen reading
• Liuyao / Najia
• Feng Shui direction analysis
• Tarot tirages

This is not a vague divination prompt.

The idea is simple:
AI should not mix every symbolic system into the same soft answer.

BaZi has its own inputs.
Meihua has its own timing and omen logic.
Liuyao has its own line order and role structure.
Feng Shui needs observable spatial facts.
Tarot needs spread positions and card interaction.

So the skill enforces a workflow:
1. Choose the right method.
2. Check the input.
3. Mark the method as runnable, partial, or blocked.
4. Interpret each system before synthesis.
5. Give verdict, evidence, timing, action, and verification signals.

The repository includes:
• Method references
• Meihua calculator
• Reproducible Tarot draw script
• Multilingual README guides
• Validation and privacy-check scripts

Works with Codex, Claude Code, and any local agent skill setup.

GitHub:
https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill
```

## Spanish Long Post

```text
I built an open-source Agent Skill for structured metaphysical readings:

Metaphysics Synthesis Skill

It covers:
• BaZi / cuatro pilares
• Meihua Yishu / I Ching omen reading
• Liuyao / Najia
• Feng Shui direction analysis
• Tarot tiradas

No es solo un prompt de adivinación.

The goal is to make AI symbolic reasoning more structured:
not vague comfort,
not one-card overinterpretation,
not mixing every tradition into one blurry answer.

The workflow is:
1. Pick the right method.
2. Check the input.
3. Mark each method as runnable, partial, or blocked.
4. Read each system before synthesis.
5. Return verdict, evidence, timing, action, and verification signals.

The repo includes:
• A SKILL.md router
• References for BaZi, Meihua, Liuyao, Feng Shui, and Tarot
• A Meihua calculator
• A reproducible Tarot draw script
• Multilingual README guides
• Validation and privacy-check scripts

It works with Codex, Claude Code, and any AI agent that can load a local skill folder.

GitHub:
https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill
```
