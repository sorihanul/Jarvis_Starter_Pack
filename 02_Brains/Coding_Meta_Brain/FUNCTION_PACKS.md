# Function Packs

## runtime flow

```text
request
-> Case Intake Pack
-> External Research Pack
-> Final Goal Lock Pack
-> Working Behavior Contract Pack
-> Critical Risk Scan Pack
-> AI Patch Trust Pack
-> Project Surface Pack
-> Scope Lock Pack
-> Design Lock Pack
-> Maintainability Gate Pack
-> Dependency Gate Pack
-> Security Gate Pack
-> Data Safety and Rollback Pack
-> Sub-Brain Selection Pack
-> Thread Handoff Pack
-> Progress Review Pack
-> Implementation Review Pack
-> Conflict Mediation Pack
-> Verification Gate Pack
-> Decision Trace Pack
-> Runbook Pack
-> Release Boundary Pack
-> Memory Export Pack
-> Closeout Report Pack
```

## principles

```text
project_before_publish:true
external_research_when_needed:true
final_goal_before_design:true
proper_working_behavior_first:true
critical_risk_before_implementation:true
ai_patch_untrusted_until_verified:true
scope_before_edit:true
design_implementation_verification_separated:true
maintainability_for_non_developer_owner:true
verification_before_done:true
sub_brain_spawn_only_if_useful:true
memory_export_candidate_only:true
```

## packs

### Case Intake Pack

```text
functions:
  case_goal_bind
  target_project_bind
  task_type_classify
  risk_level_estimate
output:
  case_intake_packet
stop_condition:
  target project or task goal is unknown
```

### Project Surface Pack

```text
functions:
  project_folder_confirm
  publish_boundary_bind
  external_repo_source_bind
  local_rules_discover
output:
  project_surface_packet
stop_condition:
  project surface cannot be located or created
```

### External Research Pack

```text
functions:
  research_need_detect
  official_docs_route
  boring_standard_option_find
  research_result_bind_to_goal
output:
  external_research_packet
stop_condition:
  task needs external facts but sources are unavailable
```

### Final Goal Lock Pack

```text
functions:
  raw_owner_intent_capture
  purpose_probe_question_select
  owner_intent_translate
  target_user_and_usage_situation_bind
  primary_success_flow_bind
  failure_boundary_bind
  first_version_scope_bind
  final_state_bind
  non_goal_bind
  owner_acceptance_bind
output:
  final_goal_lock_packet
stop_condition:
  final goal is only a category name, user flow is unknown, or first-version scope is unbounded
```

### Working Behavior Contract Pack

```text
functions:
  primary_user_flow_bind
  expected_result_bind
  data_behavior_bind
  failure_behavior_bind
  evidence_required_bind
output:
  working_behavior_contract
stop_condition:
  proper working behavior cannot be verified
```

### Critical Risk Scan Pack

```text
functions:
  serious_risk_flag_scan
  plain_language_risk_explain
  safe_simplification_propose
  owner_approval_need_decide
output:
  critical_risk_packet
stop_condition:
  high or blocked risk lacks owner approval or safe simplification
```

### AI Patch Trust Pack

```text
functions:
  generated_patch_status_bind
  review_requirement_bind
  unverified_area_track
output:
  ai_patch_trust_packet
stop_condition:
  implementation is treated as trusted without verification
```

### Scope Lock Pack

```text
functions:
  allowed_change_bind
  forbidden_change_bind
  affected_surface_estimate
  acceptance_condition_bind
output:
  task_scope_packet
stop_condition:
  requested change is too broad for current case
```

### Maintainability Gate Pack

```text
functions:
  boring_standard_default_check
  unnecessary_complexity_detect
  next_AI_readability_check
  run_test_docs_need_bind
output:
  maintainability_gate_result
stop_condition:
  solution is too clever or undocumented for non-developer owner maintenance
```

### Dependency Gate Pack

```text
functions:
  new_dependency_detect
  dependency_existence_check_plan
  official_source_and_license_check
  dependency_risk_decide
output:
  dependency_gate_result
stop_condition:
  new dependency is needed but not checked
```

### Security Gate Pack

```text
functions:
  security_sensitive_surface_detect
  security_checks_select
  residual_security_risk_bind
output:
  security_gate_result
stop_condition:
  security-sensitive change lacks security gate
```

### Data Safety and Rollback Pack

```text
functions:
  data_at_risk_detect
  destructive_action_detect
  backup_or_rollback_plan_bind
  rollback_stop_condition_check
output:
  data_safety_rollback_packet
stop_condition:
  data risk exists without backup, rollback, or owner approval
```

### Sub-Brain Selection Pack

```text
functions:
  role_split_need_detect
  candidate_sub_brain_match
  selected_threads_plan
  no_spawn_reason_record
output:
  sub_brain_selection_packet
stop_condition:
  role split would add coordination cost without reducing risk
```

### Design Lock Pack

```text
functions:
  design_intent_bind
  implementation_boundary_bind
  verification_plan_bind
  role_split_reason_bind
output:
  design_lock_packet
stop_condition:
  design, implementation boundary, or verification plan is unclear
```

### Thread Handoff Pack

```text
functions:
  handoff_packet_write
  expected_output_bind
  close_condition_bind
  thread_registry_update
output:
  thread_handoff_packet
stop_condition:
  handoff cannot name scope, input, output, and close condition
```

### Progress Review Pack

```text
functions:
  report_packet_read
  scope_drift_check
  blocker_detect
  next_action_route
output:
  progress_review_result
stop_condition:
  report is missing evidence or verification state
```

### Implementation Review Pack

```text
functions:
  changed_files_compare_to_scope
  implementation_notes_read
  scope_drift_detect
  verification_request_bind
output:
  implementation_review_result
stop_condition:
  implementation changed files outside the design lock
```

### Conflict Mediation Pack

```text
functions:
  frontend_backend_contract_check
  design_implementation_conflict_check
  verification_failure_owner_route
  scope_change_escalate
output:
  mediation_decision
stop_condition:
  conflict requires user decision
```

### Verification Gate Pack

```text
functions:
  required_checks_select
  verification_result_read
  failure_interpret
  pass_fail_decide
output:
  verification_gate_result
stop_condition:
  required verification is unavailable or failing
```

### Decision Trace Pack

```text
functions:
  major_decision_record
  alternatives_record
  rejection_reason_record
  verification_link_bind
output:
  decision_trace_entry
stop_condition:
  major implementation, dependency, security, or release decision lacks reason
```

### Runbook Pack

```text
functions:
  install_run_test_commands_record
  environment_contract_summarize
  common_failure_note
  rollback_steps_record
output:
  runbook_update
stop_condition:
  owner or next AI cannot run and verify the project
```

### Release Boundary Pack

```text
functions:
  publish_target_confirm
  operational_files_exclude
  secret_scan_requirement_note
  release_artifact_list
output:
  release_boundary_result
stop_condition:
  publish output includes brain logs or private operational files
```

### Memory Export Pack

```text
functions:
  reusable_lesson_extract
  non_exportable_filter
  evidence_bind
  memory_export_write
output:
  memory_export_packet
stop_condition:
  lessons are project-specific or unsupported
```

### Closeout Report Pack

```text
functions:
  changed_surface_summarize
  verification_summarize
  residual_risk_list
  next_action_report
output:
  final_report
stop_condition:
  verification state or publish boundary is unknown
```
