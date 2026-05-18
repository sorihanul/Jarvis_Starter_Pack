# Coding Lens Set

## Intake Lens

Use when the task is not yet safe to edit.

Focus:
- goal
- files
- success criteria
- risks
- user approval boundary

Output:
- scoped task brief
- read order
- next lens

## Implement Lens

Use when the scope is clear and code should change.

Focus:
- smallest valid patch
- existing style
- no unrelated cleanup
- no secret or credential handling

Output:
- patch-shaped change
- touched files
- verification needed

## Review Lens

Use before or after implementation when defect discovery matters.

Focus:
- behavioral bug
- regression risk
- missing test
- boundary violation
- overengineering

Output:
- findings first
- file and line references when possible
- patch recommendation only when useful

## Verify Lens

Use when the result must be checked.

Focus:
- command run
- expected result
- actual result
- failure cause
- blocked check

Output:
- verification record
- pass/fail/blocked status

## Release Lens

Use when the user needs a clear closeout.

Focus:
- what changed
- what was checked
- what remains risky
- what to do next

Output:
- concise final report

## Handoff Lens

Use when the work must move to another thread, agent, or specialist.

Focus:
- exact goal
- file ownership
- no-go areas
- expected output
- verification contract

Output:
- ready-to-paste handoff prompt
