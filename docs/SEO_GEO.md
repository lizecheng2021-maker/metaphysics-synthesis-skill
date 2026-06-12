# SEO and GEO Notes

This document records the public discoverability strategy for the repository.

## Current Verdict

The repository is eligible to be crawled because it is public and has text-based Markdown content. Broad searches such as "tarot" or "fortune telling" are too competitive. The realistic target is long-tail discovery:

- "AI divination skill"
- "Codex divination skill"
- "BaZi AI assistant"
- "Meihua Yishu calculator"
- "Liuyao divination workflow"
- "Feng Shui direction analysis"
- "Tarot AI prompt"
- "Chinese metaphysics skill"
- "八字 AI skill"
- "梅花易数起卦脚本"
- "六爻占卜 AI 工作流"
- "塔罗牌 AI 解读提示词"

## Optimization Decisions

1. Keep the root README entirely English so English search intent is not diluted.
2. Keep each localized README in one language with its own examples.
3. Add natural long-tail phrases in headings and explanatory text rather than keyword stuffing.
4. Keep installation commands near the top for conversion.
5. Keep `llms.txt` as a concise AI-readable summary for answer engines and agents.
6. Use GitHub topics to improve GitHub-native discovery.
7. Keep safety boundaries visible so search engines and AI systems understand the domain limits.
8. Keep runtime logic in `SKILL.md`, `references/`, and `scripts/`; keep README focused on discovery, installation, and examples.

## Language Pages

| Language | File | Target intent |
| --- | --- | --- |
| English | `README.md` | AI divination skill, BaZi AI assistant, Tarot AI prompt |
| Simplified Chinese | `README.zh-CN.md` | 玄学 skill, 八字 AI, 梅花易数起卦, 六爻占卜 AI |
| Korean | `README.ko-KR.md` | AI 사주 분석, 매화역수 계산기, 타로 AI |
| Japanese | `README.ja-JP.md` | AI 四柱推命, 梅花易数 計算, タロット AI |
| French | `README.fr-FR.md` | skill IA de divination, BaZi, Tarot IA |
| Spanish | `README.es-ES.md` | skill de adivinación con IA, BaZi, Tarot con IA |

## Next Iterations

- Add a short demo GIF or screenshot after the first real public use case.
- Add GitHub Pages later if stronger indexing is needed, because Pages can support HTML metadata, canonical links, and hreflang tags more directly than GitHub's README renderer.
- Add a `CONTRIBUTING.md` if outside users begin opening issues or pull requests.
- Add a lightweight test for `scripts/meihua_calc.py` if the calculator grows beyond simple structure output.

## Benchmark Notes

Patterns borrowed from high-star skill and agent repositories:

- Official skill repositories keep `SKILL.md` as the source of truth and use references/scripts for progressive disclosure.
- Search-oriented skills describe the exact job they perform in the first screen, not just the technology.
- Tool-heavy skills include quickstart commands, realistic example prompts, and validation or setup checks.
- Multi-skill repositories use routers so users do not need to remember every skill name.
- Security-oriented skill tools validate file structure and risky patterns before distribution.
