<div align="center">

# 🎯 Codex Goal Writer Skill

### 把模糊想法变成清晰、可验证的 Codex `/goal`。

<p>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge"></a>
  <a href="./goal-writer/SKILL.md"><img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-0969da?style=for-the-badge"></a>
  <a href="./goal-writer/scripts/count_goal_chars.py"><img alt="Goal Limit" src="https://img.shields.io/badge/Goal%20Limit-4000%20chars-f97316?style=for-the-badge"></a>
</p>

<p>
  <b>隐式起草</b> · <b>单问题澄清</b> · <b>证据驱动完成</b> · <b>4000 字符安全线</b>
</p>

<p>
  <a href="./README.md">English</a> ·
  <a href="#-快速安装">快速安装</a> ·
  <a href="#-示例">示例</a> ·
  <a href="#-它会生成什么">输出格式</a>
</p>

</div>

---

## ✨ 为什么需要它

Codex Goal 很适合需要持续推进的多轮任务：迁移、审计、benchmark 调查、重构、研究、产品打磨等。对于这类任务，"看起来完成了" 不够，必须有证据。

但手写 Goal 很容易漏掉关键部分：

| 常见问题 | 这个 skill 会补上什么 |
| --- | --- |
| 目标太模糊 | 转成可观察的最终结果。 |
| 完成标准主观 | 明确具体的验证证据。 |
| 范围容易膨胀 | 写清约束和边界。 |
| Codex 问太多问题 | 每轮最多问一个真正关键的问题。 |
| Goal 太长 | 控制在目标工具 4000 字符硬限制内。 |
| 研究结论混乱 | 区分 confirmed、approximate support、blocked 和 uncertainty。 |

## 🚀 快速安装

复制下面这行发给 Codex：

```text
$skill-installer https://github.com/yuxuanchiadm/codex-goal-writer-skill/tree/main/goal-writer
```

安装后重启 Codex，让新 skill 生效。

## 🧠 它优化什么

<table>
<tr>
<td width="50%">

### ✅ 更强的 Goal

- 可观察的最终状态
- 明确的验证面
- 清晰的约束和边界
- 适合多轮工作的迭代策略
- 具体的 blocked 停止条件

</td>
<td width="50%">

### 🛡️ 更稳的 Agent 行为

- 草稿只在内部形成，最终交接才展示
- 不把超长 Goal 发送给工具
- 不在缺少证据时假装完成
- 研究/审计任务明确标注不确定性
- 既能被审计，又不限制 Codex 探索路径

</td>
</tr>
</table>

## ⚡ Before / After

**Before**

```text
把这个应用变好，看到问题就修。
```

**After**

```text
/goal Improve the app until the main user flow is production-ready and verified.

Outcome:
- The main user flow works reliably on supported desktop and mobile viewports.
- Obvious UI, console, and interaction defects found during inspection are fixed or documented.

Verification surface:
- Relevant tests, build output, browser checks, screenshots, or logs demonstrate the final state.

Constraints:
- Preserve existing product behavior unless a change is necessary and explained.
- Keep changes focused on user-visible quality and correctness.

Boundaries:
- Do not introduce unrelated redesigns, dependencies, or architecture rewrites.

Iteration policy:
- Continue autonomously while evidence suggests clear next fixes; summarize changes and verification after each major pass.

Blocked stop condition:
- Stop and report blocked after the same required verification or dependency is unavailable for three consecutive attempts.
```

## 🧩 使用方式

当你的目标还比较粗略时，让 Codex 使用这个 skill：

```text
Use $goal-writer to turn this objective into a Codex Goal:
Investigate why the benchmark regressed, fix it if safe, and report evidence if not.
```

也可以要求它直接设置为 active Goal：

```text
Use $goal-writer to create and set an active Goal for migrating this project to the new API without breaking existing behavior.
```

## 💡 示例

```text
Use $goal-writer to turn this into a Goal:
Make this React dashboard production-quality on desktop and mobile.
```

```text
Use $goal-writer to turn this into a Goal:
Audit this PR for behavioral regressions, missing tests, and risky assumptions.
```

```text
Use $goal-writer to turn this into a Goal:
Research whether this benchmark result is reproducible and separate confirmed evidence from uncertainty.
```

## 🧾 它会生成什么

这个 skill 会生成一个可直接复制的标准 Codex Goal：

```text
/goal <one-sentence objective>

Outcome:
- ...

Verification surface:
- ...

Constraints:
- ...

Boundaries:
- ...

Iteration policy:
- ...

Blocked stop condition:
- ...
```

## 🔢 字符限制辅助脚本

附带脚本用于在发送给目标工具前统计生成出来的 Goal 文本：

```bash
python goal-writer/scripts/count_goal_chars.py goal.txt
```

这个脚本统计的是生成出来的 Goal，不是限制 `SKILL.md` 本身。

## 🛠️ 手动安装

如果不使用 `$skill-installer`，可以 clone 或下载这个仓库，然后只复制这个文件夹：

```text
goal-writer/
```

复制到 Codex skills 目录：

```text
~/.codex/skills/goal-writer
```

Windows：

```text
C:/Users/<your-name>/.codex/skills/goal-writer
```

安装后重启 Codex。

## ✅ 校验

如果你安装了 Codex `skill-creator` 系统 skill，可以运行：

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/goal-writer
```

## 📦 仓库结构

```text
codex-goal-writer-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
└── goal-writer/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── scripts/
        └── count_goal_chars.py
```

## ⚠️ 免责声明

这是一个受 OpenAI 公开 Codex Goal 指南启发的非官方社区 skill，不是 OpenAI 官方发布。

## 📄 许可证

MIT
