---
name: goal-writer
description: Interactive Goal drafting for Codex. Use when a user gives a vague objective and wants help creating, refining, clarifying, setting, or copying a Codex /goal with outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop condition. Produces concise Goals within the goal-setting tool's 4000-character limit, keeps drafting implicit until Final Handoff, and applies evidence-based quality rules from OpenAI's Goal guidance. Trigger for requests about writing goals, goal mode, /goal prompts, goal clarification, setting active goals, or turning ambiguous work into a reusable Codex goal.
---

# Goal Writer

Turn a vague objective into a directly usable Codex Goal. Treat the Goal as an auditable work contract: observable, evidence-based, bounded, and flexible enough for Codex to choose tactics.

Use the user's current language for clarification, final Goal, and handoff choices. If the user mixes languages, follow the language that carries the main request unless the user asks otherwise.

## When To Use

Use a Goal only for durable objectives with an evidence-based finish line and likely multi-turn investigation, implementation, or iteration. Do not draft a Goal for one-line edits, simple explanations, short reviews, or one-answer questions unless the user explicitly asks for a Goal.

## Required Goal Shape

Every final Goal must include these six sections:

- **Outcome**: Observable end state, not implementation steps.
- **Verification surface**: Evidence proving progress or completion, such as tests, screenshots, diffs, logs, command output, docs, artifacts, or user-visible behavior.
- **Constraints**: Scope, quality bar, environment, budget, style, performance, safety, compatibility, or deadline requirements.
- **Boundaries**: What is out of scope, must not change, or remains for later.
- **Iteration policy**: How Codex proceeds across turns, summarizes, continues autonomously, and incorporates new user input.
- **Blocked stop condition**: The repeated, meaningful impasse that should cause Codex to stop and mark the Goal blocked.

## Hard Limits

The full copy-ready Goal, including the `/goal` line and all sections, must be under the goal-setting tool's 4000-character hard limit. Target 3200-3600 characters; if tool-based counting is unavailable, target 3200 or fewer.

Before presenting or setting a Goal:

1. Prepare the exact final Goal text internally.
2. When shell and temp text are available, count it with `scripts/count_goal_chars.py` from this skill directory, using a temp file or stdin.
3. If over 4000 characters, compress and count again.
4. Never call the goal-setting tool with text over 4000 characters.
5. If it cannot fit without losing essential meaning, ask one narrowing question instead of presenting or setting it.

Compression order: remove repetition/examples; merge bullets; replace explanation with acceptance criteria; remove implementation details; keep all six sections with fewer bullets; preserve safety-critical constraints and the blocked stop condition.

## Visibility And Questions

Draft and revise the Goal internally. During clarification, do not show complete Goals, partial sections, provisional drafts, or "here is a draft" unless the user explicitly asks to inspect one.

Ask at most one question per assistant turn, only when the answer materially changes the Goal's direction, success criteria, verification surface, risk tolerance, or scope boundary. Prefer asking about success criteria, scope, verification, risk tolerance, and time or budget limits. Prefer multiple choice: label the first option `Recommended`, give each option a concrete tradeoff, and include an option for the user to answer in their own words. Use open-ended questions only when useful options would be misleading. Avoid questions about implementation details Codex can discover, safe-to-infer preferences, cosmetic details outside design tasks, or the first tactical step.

Treat user answers as evidence, not unquestionable truth: preserve stated preferences, add guardrails for risky choices, and ask a follow-up only when the risk changes the Goal itself.

## Quality Rules

Before Final Handoff, silently verify:

- Outcome is observable; verification names concrete evidence.
- Constraints guide the work and are not incidental preferences.
- Boundaries prevent likely scope creep and important unsafe changes.
- Iteration policy explains continuation, summaries, and new input.
- Blocked stop condition is specific enough to trigger only after a real repeated impasse.
- The Goal is narrow enough to audit and broad enough for Codex to choose the next useful action.
- Completion can only be marked after checking the named verification surface.

Do not hide uncertainty. If data, benchmarks, credentials, external resources, exact reproduction, or proxy evidence may be unavailable, encode how Codex should label partial success, blocked claims, and remaining uncertainty.

For research, reproduction, or audit Goals, define the evidence standard up front: identify claims, map claims to evidence, attempt feasible checks, label blocked claims, and produce a final artifact separating confirmed findings, approximate support, blockers, and uncertainty.

Fill gaps with reasonable assumptions when safe; ask only when the gap would materially change the Goal.

## Workflow

1. Restate the rough objective only if it helps the conversation.
2. Draft the six sections internally in the user's language.
3. Find the largest material uncertainty.
4. If needed, ask exactly one clarification question without showing the draft, then repeat.
5. When clear enough, compress and count to fit the hard limit.
6. Present exactly one complete copy-ready Goal only in the Final Handoff.

## Output Format

At Final Handoff, provide a concise note and one copy-ready Goal under 4000 characters:

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

Keep sections short, usually 1-3 bullets each. Avoid long rationale, duplicated constraints, and detailed implementation plans unless the user explicitly wants the plan in the Goal.

## Final Handoff

If the user explicitly asked to set the Goal immediately, perform the final length check and call the goal-setting tool directly. Otherwise, after presenting the complete Goal, ask what to do next:

1. **Set it as the active Goal (Recommended)**: Use it immediately in this thread.
2. **Leave it as copy-ready text**: Keep it in chat for copying or later edits.
3. **Adjust it first**: Let the user request one change before setting or copying.

If goal-setting tools are unavailable, say so briefly and leave the copy-ready Goal visible.

