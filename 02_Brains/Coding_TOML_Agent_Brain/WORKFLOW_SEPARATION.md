# Workflow Separation

## core rule

Design, implementation, and verification must be separated even in a single thread.

This brain does not create sub-brain threads.
Instead, it separates the stages through explicit checkpoints and, when useful, temporary TOML role agents.

## why

LLMs can blend planning, editing, and self-approval into one fluent answer.
That is not acceptable for coding work.

## stages

### design stage

```text
purpose:
  lock the task before code changes
required_outputs:
  task_scope
  forbidden_changes
  acceptance_conditions
  required_checks
  needed_agents_or_no_agent_reason
stop_condition:
  scope or required checks are unclear
```

### implementation stage

```text
purpose:
  modify code inside the locked scope
required_outputs:
  changed_files
  implementation_notes
  agent_contracts_used
  verification_request
stop_condition:
  work needs independent role thread or scope expansion
```

### verification stage

```text
purpose:
  test or inspect the implementation against the design contract
required_outputs:
  checks_run
  pass_fail
  failure_interpretation
  rework_or_close_decision
stop_condition:
  checks are failing, missing, or inconclusive
```

## single-thread interpretation

```text
design_agent_optional:true
implementation_agent_optional:true
verification_agent_recommended_when_checks_exist:true
all_agents_run_sequentially:true
main_thread_owns_closeout:true
```

## forbidden collapse

```text
forbidden:
  edit_before_scope_lock
  skip_agent_or_stage_reason_missing
  claim_done_without_required_checks
  active_agent_self_approves_without_verification_stage
```
