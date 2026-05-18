# 85 Idea Collection Brief

## Purpose

Use this when several threads should comment on the brain lens concept before
it becomes a stronger pack or a coding harness.

This is for collecting judgment, not for launching implementation.

## Copyable Prompt

```text
Read the brain lens concept below and evaluate it.

Concept:
- A brain lens does not control another brain.
- The current thread may temporarily read another brain's entry files and apply those rules to one task.
- If work must run elsewhere, the current thread writes a bounded handoff prompt.
- Returned output must be integrated by the main thread before final judgment.

Evaluate from your role:
1. What does this make easier?
2. Where could a beginner misunderstand it?
3. What should be forbidden?
4. What fields must a handoff always include?
5. If applied to coding, what failure mode does it prevent?
6. If applied to memory/wiki, what should be recorded and what should not?
7. What single rule would you add before this becomes a reusable pack?

Return format:
- useful:
- dangerous:
- missing:
- required_fields:
- coding_implication:
- memory_implication:
- recommended_rule:
```

## Collection Rule

Do not merge every returned opinion into the pack.

First classify returns as:

```text
must_fix:
  prevents real misuse or broken operation

useful:
  improves clarity without adding heavy structure

domain_specific:
  useful only for coding, writing, memory, research, or publishing

discard:
  adds abstraction but no operational value
```

## Stop Rule

Stop collecting when the same issues repeat.

The goal is a sharper pack, not an endless opinion archive.

