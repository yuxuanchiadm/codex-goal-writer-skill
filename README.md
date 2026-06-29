# Codex Goal Writer Skill

A community Codex skill for turning vague objectives into concise, evidence-based `/goal` prompts.

This skill helps Codex clarify durable objectives, draft copy-ready Goals, keep drafting implicit until final handoff, and stay within the goal-setting tool's 4000-character hard limit.

## Features

- Uses the six Codex Goal sections: Outcome, Verification surface, Constraints, Boundaries, Iteration policy, and Blocked stop condition
- Keeps Goal drafting implicit until the final handoff
- Asks at most one material clarification question per turn
- Enforces a 4000-character hard limit for copy-ready Goals
- Includes `scripts/count_goal_chars.py` for deterministic character counting
- Supports research, audit, and reproduction Goals with evidence labeling

## Install

Copy the `goal-writer` folder into your Codex skills directory.

macOS/Linux:

```text
~/.codex/skills/goal-writer
```

Windows:

```text
C:/Users/<your-name>/.codex/skills/goal-writer
```

Restart Codex or start a new session after installing.

## Usage

```text
Use $goal-writer to turn this objective into a Codex Goal:
<your objective>
```

You can also ask Codex to set the generated Goal as the active Goal after review.

## Validate

If you have the Codex skill-creator system skill installed, run:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/goal-writer
```

Windows example:

```powershell
python C:/Users/<your-name>/.codex/skills/.system/skill-creator/scripts/quick_validate.py C:/Users/<your-name>/.codex/skills/goal-writer
```

## Notes

This is an unofficial community skill inspired by OpenAI's public Codex Goal guidance. It is not an official OpenAI release.

## License

MIT
