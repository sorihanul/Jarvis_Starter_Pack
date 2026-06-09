# Output Contract

## owner goal and behavior result

```text
owner_goal_raw:
purpose_probe_summary:
target_user:
usage_situation:
primary_user_flow:
must_have_outcomes:
must_not_happen:
data_lifecycle:
privacy_boundary:
first_version_scope:
open_questions:
locked_final_goal:
working_behavior_contract:
non_goals:
owner_acceptance:
```

## research and risk result

```text
external_research_used:
sources_checked:
critical_risk_level:
risk_flags:
dependency_gate:
security_gate:
data_safety_gate:
rollback_plan:
```

## task intake result

```text
task_id:
goal:
project_surface:
task_type:
acceptance_condition:
single_thread_allowed:
```

## agent plan result

```text
active_agents:
why_created:
why_skipped:
sequence:
expected_outputs:
```

## workflow separation result

```text
design_stage:
  scope:
  forbidden_changes:
  required_checks:
  agent_plan_or_no_agent_reason:
implementation_stage:
  changed_files:
  active_agents_used:
  scope_drift_check:
conservative_operation_loop_stage:
  purpose_fit_check:
  run_or_render_check:
  abnormality_detected:
  cause_location:
  fix_applied:
  rerun_after_fix:
  loop_decision:
verification_stage:
  checks_run:
  pass_fail:
  failure_interpretation:
close_decision:
```

## verification result

```text
required_checks:
checks_run:
pass_fail:
failure_interpretation:
blockers:
```

## closeout report

```text
changed_project_files:
operational_files_changed:
final_goal_check:
working_behavior_evidence:
conservative_operation_loop_result:
decision_trace_location:
runbook_location:
active_agents_archived_or_discarded:
verification_summary:
publish_boundary:
memory_export_location:
residual_risks:
next_action:
```

## forbidden outputs

```text
claim_done_without_verification:true
claim_done_without_purpose_fit_check:true
claim_fixed_without_rerun:true
create_agents_without_clear_role:true
publish_operational_files_as_project:true
promote_memory_export_as_canon:true
```
