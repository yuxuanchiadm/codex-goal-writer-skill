<div align="center">

# Codex Goal Writer Skill

把模糊目标整理成简洁、可验证的 Codex `/goal`。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue.svg)](./goal-writer/SKILL.md)
[![Goal Limit](https://img.shields.io/badge/Goal%20Limit-4000%20chars-orange.svg)](./goal-writer/scripts/count_goal_chars.py)

[English](./README.md) · [快速安装](#快速安装) · [使用方式](#使用方式) · [示例](#示例)

</div>

## 为什么需要它

Codex Goal 适合长期、多轮、需要证据验证的任务，例如调试、迁移、审计、研究、重构等。

这个 skill 会帮助 Codex 把一个粗略目标整理成紧凑的 `/goal`，明确：

- 期望结果
- 验证方式
- 约束和边界
- 多轮迭代方式
- 什么时候应该停止并标记 blocked

它还会主动控制最终 Goal 长度，避免超过目标工具的 4000 字符硬限制。

## 快速安装

复制下面这行发给 Codex：

```text
$skill-installer https://github.com/yuxuanchiadm/codex-goal-writer-skill/tree/main/goal-writer
```

安装后重启 Codex，让新 skill 生效。

## 功能特性

| 功能 | 说明 |
| --- | --- |
| 六段 Goal 结构 | 使用 Outcome、Verification surface、Constraints、Boundaries、Iteration policy、Blocked stop condition。 |
| 隐式起草 | 澄清阶段不展示草稿，只在最终交接时给出一个可复制 Goal。 |
| 聚焦澄清 | 每轮最多问一个真正影响目标的问题。 |
| 4000 字符安全线 | 生成紧凑 Goal，并附带确定性字符计数脚本。 |
| 证据驱动完成 | 鼓励在标记完成前先检查具体证据。 |
| 研究/审计支持 | 区分 confirmed、approximate support、blocked 和 uncertainty。 |

## 使用方式

当你有一个粗略目标时，让 Codex 使用这个 skill：

```text
Use $goal-writer to turn this objective into a Codex Goal:
Investigate why the benchmark regressed, fix it if safe, and report evidence if not.
```

也可以要求 Codex 直接设置为 active Goal：

```text
Use $goal-writer to create and set an active Goal for migrating this project to the new API without breaking existing behavior.
```

## 示例

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

## 它会生成什么

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

## 手动安装

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

## 校验

如果你安装了 Codex `skill-creator` 系统 skill，可以运行：

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/goal-writer
```

附带的脚本用于统计“生成出来的 Goal 文本”，不是限制 `SKILL.md` 本身：

```bash
python goal-writer/scripts/count_goal_chars.py goal.txt
```

## 仓库结构

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

## 免责声明

这是一个受 OpenAI 公开 Codex Goal 指南启发的非官方社区 skill，不是 OpenAI 官方发布。

## 许可证

MIT

