<div align="center">

# 🎯 Codex Goal Writer Skill

### Turn fuzzy intentions into focused, evidence-driven Codex `/goal` prompts.

<p>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge"></a>
  <a href="./goal-writer/SKILL.md"><img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-0969da?style=for-the-badge"></a>
  <a href="./goal-writer/scripts/count_goal_chars.py"><img alt="Goal Limit" src="https://img.shields.io/badge/Goal%20Limit-4000%20chars-f97316?style=for-the-badge"></a>
</p>

<p>
  <b>Implicit drafting</b> · <b>One-question clarification</b> · <b>Evidence-based completion</b> · <b>4000-char safe</b>
</p>

<p>
  <a href="./README.zh-CN.md">中文文档</a> ·
  <a href="#-quick-install">Quick Install</a> ·
  <a href="#-examples">Examples</a> ·
  <a href="#-what-it-generates">Output</a>
</p>

</div>

---

## ✨ Why This Exists

Codex Goals are great for work that should continue across turns: migrations, audits, benchmark investigations, refactors, research, product polish, and other tasks where "looks done" is not enough.

But hand-written Goals often miss the pieces that make autonomous work reliable:

| Common problem | What this skill adds |
| --- | --- |
| The objective is vague | Converts it into an observable outcome. |
| Completion is subjective | Defines concrete verification evidence. |
| Scope expands mid-task | Adds constraints and boundaries. |
| Codex keeps asking too much | Asks only one material clarification question per turn. |
| Goals get too long | Keeps the final Goal under the 4000-character hard limit. |
| Research claims get muddy | Separates confirmed evidence, approximations, blockers, and uncertainty. |

## 🚀 Quick Install

Paste this into Codex:

```text
$skill-installer https://github.com/yuxuanchiadm/codex-goal-writer-skill/tree/main/goal-writer
```

Then restart Codex to pick up the new skill.

## 🧠 What It Optimizes For

<table>
<tr>
<td width="50%">

### ✅ Strong Goals

- Observable end state
- Named verification surface
- Clear constraints and boundaries
- Iteration policy for multi-turn work
- Specific blocked stop condition

</td>
<td width="50%">

### 🛡️ Safer Agent Behavior

- Drafts stay hidden until final handoff
- No oversized Goals sent to the tool
- No fake completion without evidence
- Explicit uncertainty for research/audits
- Narrow enough to audit, broad enough to explore

</td>
</tr>
</table>

## ⚡ Before / After

**Before**

```text
Make this app better and fix any issues you find.
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

## 🧩 Usage

Ask Codex to use the skill when your objective is still rough:

```text
Use $goal-writer to turn this objective into a Codex Goal:
Investigate why the benchmark regressed, fix it if safe, and report evidence if not.
```

Or ask it to set the Goal immediately:

```text
Use $goal-writer to create and set an active Goal for migrating this project to the new API without breaking existing behavior.
```

## 💡 Examples

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

## 🧾 What It Generates

The skill produces one copy-ready Goal with the standard Codex Goal contract:

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

## 🔢 Character Limit Helper

The included helper counts generated Goal text before it is sent to the goal-setting tool:

```bash
python goal-writer/scripts/count_goal_chars.py goal.txt
```

It is for generated Goal text, not for limiting `SKILL.md` itself.

## 🛠️ Manual Install

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

## ✅ Validation

If you have the Codex `skill-creator` system skill installed:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/goal-writer
```

## 📦 Repository Layout

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

## ⚠️ Disclaimer

This is an unofficial community skill inspired by OpenAI's public Codex Goal guidance. It is not an official OpenAI release.

## 📄 License

MIT
