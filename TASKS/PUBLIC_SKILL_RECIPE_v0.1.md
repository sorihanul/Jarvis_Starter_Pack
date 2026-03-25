# Public Skill Recipe v0.1

## Purpose

- define how to write a public-safe skill card inside Jarvis Starter
- make skills reusable as small procedures that support agent lanes

## When To Use This Recipe

- when an action repeats across multiple agent cards
- when a card needs a helper procedure rather than a larger new agent
- when a bundle is unstable because the shared procedure is still implicit

## Core Rule

- a skill is not a role
- a skill is a repeatable procedure with bounded input and output

## Recommended Skill Structure

1. `목적 (Purpose)`
- one sentence for what the skill does

2. `입력 (Input)`
- what the skill expects

3. `절차 (Procedure)`
- short numbered steps

4. `출력 (Output)`
- the exact return shape

5. `실패 처리 (Fallback)`
- what to do when the procedure cannot complete safely

## Design Rules

- one skill = one repeatable move
- do not hide a whole agent inside a skill
- keep the output shape explicit
- keep the procedure short enough to reuse across bundles
- write for model execution, not human admiration

## Good Public Skill Targets

- scope lock
- route lock
- gate judgment
- evidence pack
- patch shape
- brief to draft

## Avoid

- vague philosophy in place of steps
- giant umbrella skills that absorb multiple lanes
- skills that depend on outside package knowledge
- skills that require a hidden card to make sense

## Promotion Check

- at least two agent cards can use the skill
- the procedure is stable enough to repeat
- the return shape is clear
- the skill reduces drift in a real lane

## One-Line Verdict

- a public skill should be a small reusable move that tightens a lane, not a second hidden agent
