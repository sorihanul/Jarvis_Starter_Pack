# Acceptance Tests

## test document state

```text
document_state: acceptance_conditions
actual_result_report: false
real_solo_task_validated: false
```

## static tests

These are required conditions for the template structure.
They are not evidence that a real coding task succeeded.

```text
has_boot_surface:true
has_agent_spec:true
has_active_agents_folder:true
has_candidate_agents_folder:true
has_archive_agents_folder:true
has_project_surface:true
has_memory_export_surface:true
single_thread_status_declared:true
experimental_status_declared:true
workflow_separation_declared:true
final_goal_lock_declared:true
external_research_rule_declared:true
working_behavior_contract_declared:true
critical_risk_scan_declared:true
dependency_security_data_gates_declared:true
maintainability_and_rollback_declared:true
decision_trace_and_runbook_declared:true
```

## dry-run tests

These are dry-run expectations.
Record actual execution results in `REPORTS/VERIFICATION_REPORT.md` after a real solo coding task.

```text
small_bugfix_can_use_zero_or_one_agent:true
bounded_feature_can_create_sequential_agents:true
multi_thread_need_routes_to_Coding_Meta_Brain:true
verification_gate_required:true
memory_export_is_candidate_not_canon:true
design_implementation_verification_not_collapsed:true
owner_goal_locked_before_design:true
raw_goal_not_locked_without_purpose_probe:true
target_user_and_success_flow_required:true
first_version_scope_required:true
serious_risk_scanned_before_implementation:true
working_behavior_evidence_required:true
major_decisions_traceable:true
runbook_required_for_deliverable:true
```

## stable promotion tests

This brain must not be described as reference-ready or stable until:

```text
real_solo_coding_tasks_tested:true
agent_creation_was_useful:true
agent_ceremony_did_not_slow_small_tasks:true
verification_gate_was_used:true
memory_export_was_reviewed:true
```
