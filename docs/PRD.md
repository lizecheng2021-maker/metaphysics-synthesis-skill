# Metaphysics Synthesis Skill PRD

## 1. 需求定义

商业目标：把本地玄学合参能力整理成一个可公开安装、可搜索、可复用的 GitHub skill 仓库。

用户画像：

- 使用 Codex 或兼容 AI Agent 的个人用户。
- 需要八字、梅花易数、六爻、风水、塔罗等结构化推演的人。
- 想要“果断断语 + 证据路径 + 应期 + 行动建议”的用户。

核心功能：

- 触发并执行 metaphysics synthesis workflow。
- 按系统选择参考文件。
- 使用梅花脚本校验主卦、互卦、变卦、动爻、体用生克。
- 保留高风险边界，避免用玄学替代专业建议。

## 2. 技术选型

| 项目 | 选择 | 理由 |
| --- | --- | --- |
| Skill format | Codex skill folder | 与本地 Codex 生态兼容 |
| Documentation | Markdown | GitHub 原生展示，利于 SEO/GEO |
| Script | Python 3 stdlib | 无依赖，易运行，稳定 |
| License | MIT | 低摩擦传播和二次开发 |

## 3. 架构设计

```text
User prompt
  -> SKILL.md routes system
  -> relevant references/*.md
  -> optional scripts/meihua_calc.py
  -> answer with verdict, evidence, timing, action, verification
```

模块：

- `SKILL.md`：总入口和工作流。
- `references/`：各术数细则。
- `scripts/`：确定性计算辅助。
- `README.md` / `llms.txt`：GitHub 展示和 AI 摘要。

## 4. 安全方案

威胁清单：

- 误把玄学当医疗、法律、金融建议。
- 对死亡、灾难、安全做绝对化判断。
- 把个人隐私案例上传到公开仓库。

防护措施：

- README 和 SKILL 均明确文化/反思用途。
- Evidence hierarchy 要求事实优先。
- 发布前用关键词扫描隐私内容。
- 不上传用户个人命盘、聊天记录、工作内容。

## 5. 营销/SEO策略

关键词：

- Codex skill
- AI divination skill
- BaZi AI assistant
- Meihua Yishu calculator
- Liuyao reading
- Chinese metaphysics
- Tarot AI prompt
- 玄学, 八字, 梅花易数, 六爻, 风水, 塔罗

GEO策略：

- README 开头一句话说明用途。
- 表格列出系统、用途、文件路径。
- `llms.txt` 给 AI crawler 快速摘要。
- FAQ/Usage examples 覆盖真实查询意图。

转化路径：

1. GitHub search 发现仓库。
2. README 说明能力和边界。
3. 用户复制安装命令。
4. 使用示例问题触发 skill。

## 6. 成本预估

- GitHub public repo：0成本。
- Python脚本：无外部依赖，0运行成本。
- 维护成本：每次方法更新约10-30分钟。

## 7. 风险清单

| 风险 | 影响 | 应对 |
| --- | --- | --- |
| 用户误用为专业建议 | 高 | README/SKILL 强边界 |
| 术数体系冲突 | 中 | 单系统先自洽，再合参 |
| GitHub SEO弱 | 中 | Description/topics/README/llms.txt |
| 脚本与解释不一致 | 中 | 脚本只算结构，不下断语 |

## 8. 里程碑

| 阶段 | 验收标准 |
| --- | --- |
| 本地发布包 | README、LICENSE、Skill、references、scripts齐全 |
| 本地校验 | `python scripts/meihua_calc.py` 可运行 |
| GitHub发布 | public/private repo 创建并 push |
| 元数据优化 | description、topics 设置完成 |

## 9. 迭代日志

- 2026-06-12：创建 GitHub 发布包，补充 README、中文 README、llms.txt、LICENSE、GITHUB_METADATA、PRD。
- 2026-06-12：基于 Google Search Central、GitHub README/topics 文档和公开 agent skill 仓库写法，优化 SEO/GEO；英文 README 纯英文，新增中文、韩文、日文、法文、西文独立介绍和案例；更新 `llms.txt` 与 skill 触发描述。
