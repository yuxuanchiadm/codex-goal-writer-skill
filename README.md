<div align="center">

# Codex Goal Writer Skill

Turn vague objectives into concise, evidence-based Codex `/goal` prompts.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue.svg)](./goal-writer/SKILL.md)
[![Goal Limit](https://img.shields.io/badge/Goal%20Limit-4000%20chars-orange.svg)](./goal-writer/scripts/count_goal_chars.py)

[中文文档](./README.zh-CN.md) · [Quick Install](#quick-install) · [Usage](#usage) · [Examples](#examples)

</div>

## Why

Codex Goals are useful for durable, multi-turn work: debugging, migrations, audits, research, refactors, and other tasks where success needs evidence instead of guesswork.

This skill helps Codex turn a rough objective into a compact `/goal` that defines:

- the desired outcome
- the verification surface
- constraints and boundaries
- iteration behavior
- the blocked stop condition

It also keeps the final Goal within the goal-setting tool's 4000-character hard limit.

## Quick Install

Paste this into Codex:

```text
$skill-installer https://github.com/yuxuanchiadm/codex-goal-writer-skill/tree/main/goal-writer
```

Restart Codex to pick up the new skill.

## Features

| Feature | What it does |
| --- | --- |
| Six-section Goal shape | Uses Outcome, Verification surface, Constraints, Boundaries, Iteration policy, and Blocked stop condition. |
| Implicit drafting | Keeps draft Goals hidden during clarification and shows one copy-ready Goal at final handoff. |
| Focused clarification | Asks at most one material question per turn. |
| 4000-character safety | Targets concise Goals and includes a deterministic character-count helper. |
| Evidence-based completion | Encourages concrete verification before marking work complete. |
| Research/audit support | Labels confirmed findings, approximate support, blockers, and uncertainty. |

## Usage

Ask Codex to use the skill when you have a rough objective:

```text
Use $goal-writer to turn this objective into a Codex Goal:
Investigate why the benchmark regressed, fix it if safe, and report evidence if not.
```

You can also ask Codex to set it immediately:

```text
Use $goal-writer to create and set an active Goal for migrating this project to the new API without breaking existing behavior.
```

## Examples

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

## What It Generates

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

## Manual Install

If you do not want to use `$skill-installer`, clone or download this repository and copy only this folder:

```text
goal-writer/
```

To your Codex skills directory:

```text
~/.codex/skills/goal-writer
```

Windows:

```text
C:/Users/<your-name>/.codex/skills/goal-writer
```

Restart Codex after installing.

## Validation

If you have the Codex `skill-creator` system skill installed:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/goal-writer
```

The included helper counts generated Goal text, not `SKILL.md` itself:

```bash
python goal-writer/scripts/count_goal_chars.py goal.txt
```

## Repository Layout

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

## Disclaimer

This is an unofficial community skill inspired by OpenAI's public Codex Goal guidance. It is not an official OpenAI release.

## License

MIT
