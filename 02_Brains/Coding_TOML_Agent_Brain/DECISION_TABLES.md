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
  required checks are named
  agent plan or no-agent reason is recorded

implementation_stage_allowed:
  design_stage_complete is true
  active agent sequence is known or no agents are required

verification_stage_allowed:
  implementation checkpoint exists
  changed files are known
  required checks are known

done_forbidden:
  same message claims design, edit, and verification without separate stage outputs
```

## conservative operation loop decision

```text
loop_required:
  code was edited
  program behavior is promised
  UI, report, data pipeline, command, or user flow exists
  prior run showed an abnormality

loop_pass:
  original purpose was checked against the result
  program or relevant output was run, rendered, or blocker recorded
  abnormalities were checked
  cause was located before fixing
  fix was minimal and maintainable
  relevant check was rerun after fixing
  result was recorded

loop_repeat:
  abnormality remains
  new cause or new fix path is available
  scope still allows progress

loop_stop_with_blocker:
  required behavior cannot be inspected
  same failure repeats without new evidence
  required permission, data, or environment is unavailable
  fix would exceed locked scope

done_forbidden:
  loop ran but purpose fit was not checked
  code changed but no rerun happened
  test passed but main user flow was not checked when required
  automation or agent structure became the deliverable instead of the program behavior
```

## solo vs multi-thread decision

```text
single_thread_allowed:
  one repo or one project surface
  task is bounded
  roles can run sequentially
  verification path is clear
  coordination overhead would be wasteful

multi_thread_required:
  roles need independent workspaces
  frontend/backend/design work is large and concurrent
  verification requires independent triage
  multiple repos are involved
  project is long-running
```

## TOML agent creation decision

```text
create_agent:
  role boundary is clear
  input and output can be named
  stop condition is clear
  role contract reduces confusion

do_not_create_agent:
  one-off tiny edit
  role duplicates the main brain
  input or output is vague
  agent would add ceremony only
```

## default solo sequence

```text
design_checkpoint
repo_intake_agent_if_needed
scope_patch_agent_if_needed
implementation_checkpoint
verification_agent_if_needed
release_check_agent_if_needed
closeout
```

## done decision

```text
done_allowed:
  scope satisfied
  conservative operation loop passed or blocker recorded
  required verification passed or blocker recorded
  active agents archived or discarded
  final report written

done_forbidden:
  verification unknown
  conservative loop result unknown
  active agent state unknown
  scope drift unresolved
  final goal not checked against working behavior
  critical risk unresolved
  decision trace missing for major choice
  runbook missing for deliverable project
  publish boundary unknown
```
