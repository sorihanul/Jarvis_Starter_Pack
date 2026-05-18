# Switching Lens Pack

## Purpose

This option pack helps Jarvis switch the working lens inside one task.

It is for tasks where the same material must be viewed from different judgment postures:

```text
intake:
  what is the user really asking?

evidence:
  what is known, inferred, missing, or risky?

structure:
  how should the material be organized?

execution:
  what is the smallest useful next action?

review:
  what could be wrong, excessive, or unstable?

user_surface:
  how should the result be explained so the user can decide?
```

## Core Definition

```text
lens:
  a temporary way of seeing the task
  it changes what Jarvis notices first, ignores, checks, and reports

skill:
  a repeatable procedure or tool-like move
  it does a bounded action such as research, verification, cleanup, summarization, or formatting
```

The lens decides how to look.

The skill decides what move to perform.

## What This Pack Does

```text
choose:
  select the active lens for the next step

focus:
  state what this lens sees first

ignore:
  state what this lens should not expand into

pair:
  choose whether a skill or option pack is needed

return:
  close the lens and report what changed
```

## What This Pack Does Not Do

```text
does not create a new brain
does not replace a domain brain
does not execute tools by itself
does not replace skills
does not make every task multi-step
does not pretend to run several agents
```

## Skill Difference

Use this pack when the problem is:

```text
which viewpoint should Jarvis use now?
what should be noticed first?
what should be held back?
what should the next judgment posture be?
```

Use a skill when the problem is:

```text
what repeatable procedure should run?
what exact checklist, script, template, or workflow should be applied?
what output format should be produced by a known move?
```

## Skill Synergy

The best pattern is:

```text
lens -> choose skill -> run skill -> review with lens -> return
```

Examples:

```text
evidence lens
-> use research or source-check skill
-> return facts, uncertainty, and missing sources

review lens
-> use verification or security checklist skill
-> return findings, severity, and remaining risk

user_surface lens
-> use writing or formatting skill
-> return a decision-ready explanation
```

## First Read

```text
1. README.md
2. ACTIVATION_RULE.md
3. INPUT_SLOTS.md
4. LENS_SET.md
5. LENS_SKILL_BOUNDARY.md
6. OPERATING_RULE.md
7. OUTPUT_CONTRACT.md
8. STOP_RULE.md
9. VALIDATION_RULE.md
10. ACCEPTANCE_TESTS.md
```

## Completion Rule

This pack is usable when a new reader can answer:

```text
which lens is active now?
why is this lens needed?
what does this lens see first?
what should it not expand into?
does this lens need a skill?
what changed after the lens pass?
when should Jarvis return to the main task?
```
