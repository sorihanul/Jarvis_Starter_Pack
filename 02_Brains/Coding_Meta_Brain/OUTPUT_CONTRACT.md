# Output Contract

## required outputs

### owner goal and behavior result

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

### research and risk result

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

### case intake result

```text
case_id:
goal:
project_surface:
task_type:
risk_level:
selected_mode:
```

### sub-brain selection result

```text
selected_sub_brains:
why_selected:
why_not_selected:
thread_plan:
```

### workflow separation result

```text
design_stage:
  scope:
  forbidden_changes:
  acceptance_conditions:
  verification_plan:
implementation_stage:
  changed_files:
  scope_drift_check:
  implementation_notes:
verification_stage:
  required_checks:
  pass_fail:
  failure_interpretation:
close_decision:
```

### verification result

```text
required_checks:
commands_or_methods:
pass_fail:
failure_interpretation:
remaining_blocker:
```

### closeout report

```text
changed_project_files:
operational_files_changed:
final_goal_check:
working_behavior_evidence:
decision_trace_location:
runbook_location:
verification_summary:
publish_boundary:
memory_export_location:
residual_risks:
next_action:
```

## forbidden outputs

```text
claim_done_without_verification:true
publish_operational_files_as_project:true
promote_memory_export_as_canon:true
hide_test_failure:true
```
