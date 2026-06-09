# Decision Tables

## owner-first intake decision

```text
final_goal_required:
  user provides vague purpose
  new app or tool is requested
  owner cannot state technical requirements

lock_allowed:
  target user is known
  usage situation is known
  primary success flow is known
  must-have outcome is known
  failure boundary is known
  first version scope is known

lock_forbidden:
  goal is only a category name
  user flow is unknown
  data behavior is unknown
  risk boundary is unknown
  done condition is vague
  first version scope is unbounded

external_research_required:
  technology choice is unknown
  new dependency may be added
  security, deployment, or domain pattern is involved

implementation_forbidden:
  final goal is not locked
  final goal is copied from raw owner wording without probing
  working behavior contract is missing
  critical risk scan is missing
```

## risk gate decision

```text
proceed:
  risk_level is low

proceed_with_stronger_verification:
  risk_level is medium

ask_owner_or_simplify:
  risk_level is high

stop:
  risk_level is blocked
  destructive data action has no rollback
  new dependency has no check
  security-sensitive change has no security gate
```

## maintainability decision

```text
prefer_boring_standard:
  owner is non-developer
  future handoff is likely
  common framework or documented pattern exists

reject_clever_solution:
  custom architecture is unnecessary
  niche dependency is not justified
  run/test steps cannot be documented
```

## workflow separation decision

```text
design_stage_complete:
  task scope is bound
  forbidden changes are named
  acceptance conditions are named
  verification plan is named
  role split decision is recorded

implementation_stage_allowed:
  design_stage_complete is true
  handoff packet exists for every selected sub-brain thread

verification_stage_allowed:
  implementation report exists
  changed files are known
  verification request is named

done_forbidden:
  design, implementation, and verification are reported as one undifferentiated claim
```

## sub-brain thread decision

```text
if task is small and single-surface:
  use single-thread mode

if frontend and backend contracts both change:
  select Frontend_Brain, Backend_Brain, Integration_Brain, Verification_Brain

if UI quality or layout is central:
  select Design_Brain and Verification_Brain

if release or publish is requested:
  select Release_Gate_Brain

if failures are unclear after first verification:
  route to Verification_Brain or Integration_Brain
```

## done decision

```text
done_allowed:
  scope satisfied
  original purpose satisfied
  target behavior verified
  regressions checked or explicitly bounded
  maintainability checked
  required verification passed or blocker is explicit
  publish boundary known
  final report written

done_forbidden:
  tests failing without explanation
  build failing without explanation
  verification skipped without reason
  behavior loop not closed
  problem cause guessed without verification
  final goal not checked against working behavior
  critical risk unresolved
  decision trace missing for major choice
  runbook missing for deliverable project
  unrelated refactor included
  operational brain files mixed into publish output
```

## memory export decision

```text
export_allowed:
  lesson is reusable
  evidence is named
  applies_to and does_not_apply_to are clear
  no secret or repo-private fact is included

export_forbidden:
  raw log
  one-off workaround
  unverified guess
  private credential or internal endpoint
```
