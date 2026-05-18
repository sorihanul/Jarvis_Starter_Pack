# 80 Coding Applications

## Boundary

This pack is not a complete coding harness.

It only helps decide:

```text
which coding role should be opened?
same thread or separate thread?
what must the handoff include?
who integrates the returned result?
```

Do not present this pack as a replacement for control planes, session and hook
harnesses, team commands, or custom-agent workflows.

If the task needs a serious reusable coding pack, read
`../Switching_Coding_Pack/README.md` first.

Use this document only when the coding work must be handed off to another
thread/brain or integrated back into a parent judgment.

## What Coding Work Can Use Here

Coding work often has several roles that should not be mixed.

```text
design
implementation
review
test repair
release check
documentation
security review
```

One thread can do some of these, but large work is safer when the roles are routed or handed off.

This pack is useful only for that route and handoff layer.
The actual coding discipline must still come from project rules, tests, proof
contracts, permission boundaries, and `Switching_Coding_Pack` when coding lens
switching is the actual need.

## Coding Mode 1. Same-Thread Lens

Use when the current thread can briefly switch to a coding role.

Example:

```text
task:
  Review this patch for regressions.

mode:
  same_thread_lens

entry_files:
  code review brain
  local project rules
  test policy

output:
  findings first
  risk
  tests run
  next fix
```

Use for:

```text
small patch review
single-file fix
quick test failure triage
short refactor check
```

## Coding Mode 2. Separate-Thread Handoff

Use when work should be split.

Example:

```text
main thread:
  owns goal, scope, final integration

worker thread:
  implements one bounded change

review thread:
  checks behavior and tests
```

The handoff must include:

```text
target files:
task:
success criteria:
do_not_touch:
expected output:
tests to run:
return format:
```

Use for:

```text
multi-file implementation
parallel code review
test repair while main thread continues design
release checklist
```

## Coding Mode 3. Integration Only

Use when specialist outputs already exist.

Example:

```text
inputs:
  worker patch summary
  reviewer findings
  test result
  release checklist

main thread:
  accepts or rejects findings
  decides remaining risk
  writes final next action
```

Use for:

```text
PR readiness
release decision
merge risk review
after-action report
```

## Coding Anti-Patterns

Do not use this pack to make vague delegation.

Bad:

```text
Make a coding sub-brain handle it.
```

Good:

```text
Create a handoff for an implementation thread.
It may edit only these files.
It must run these checks.
It must return changed files, tests run, and remaining risk.
```

Do not create many coding roles when one role is enough.

Bad:

```text
Design Brain + Implementation Brain + Test Brain + Review Brain for a one-line typo.
```

Good:

```text
Single-thread fix. No route pack needed.
```

Do not use this pack to hide vibe coding failure.

Bad:

```text
Let another coding brain figure it out.
```

Good:

```text
The parent thread owns the goal and final integration.
The worker may edit only the listed files.
The reviewer checks behavior against the stated success criteria.
The task is not complete until the named checks pass or the remaining risk is reported.
```

## Recommended Coding Combinations

Small review:

```text
Verification_and_Proof_Pack
```

Bounded implementation handoff:

```text
Brain_Routing_and_Handoff_Pack
Action_Permission_Pack
Verification_and_Proof_Pack
```

External codebase pattern import:

```text
Source_Command_Filter_Pack
Evidence_Intake_Pack
Capability_Import_Pack
Verification_and_Proof_Pack
```

Release gate:

```text
Brain_Routing_and_Handoff_Pack
Verification_and_Proof_Pack
Action_Permission_Pack
```

## Coding Close Rule

The main thread must close with:

```text
what changed:
who worked:
what was verified:
what remains risky:
next action:
```
