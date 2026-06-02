# Function Packs

## runtime flow

```text
request
-> Task Intake Pack
-> External Research Pack
-> Final Goal Lock Pack
-> Working Behavior Contract Pack
-> Critical Risk Scan Pack
-> AI Patch Trust Pack
-> Solo Suitability Pack
-> Project Surface Pack
-> Scope Lock Pack
-> Design Checkpoint Pack
-> Maintainability Gate Pack
-> Dependency Gate Pack
-> Security Gate Pack
-> Data Safety and Rollback Pack
-> Agent Role Draft Pack
-> Agent Sequence Pack
-> Code Work Pack
-> Implementation Checkpoint Pack
-> Verification Gate Pack
-> Decision Trace Pack
-> Runbook Pack
-> Release Boundary Pack
-> Memory Export Pack
-> Closeout Pack
```

## principles

```text
single_thread_first:true
external_research_when_needed:true
final_goal_before_design:true
proper_working_behavior_first:true
critical_risk_before_implementation:true
ai_patch_untrusted_until_verified:true
agent_count_zero_by_default:true
agent_created_only_for_clear_role:true
design_implementation_verification_separated:true
maintainability_for_non_developer_owner:true
scope_before_patch:true
verification_before_done:true
```

## packs

### Task Intake Pack

```text
functions:
  task_goal_bind
  target_project_bind
  task_type_classify
  acceptance_condition_bind
output:
  task_intake_packet
stop_condition:
  target project or coding goal is unknown
```

### Solo Suitability Pack

```text
functions:
  repo_count_check
  surface_count_estimate
  role_independence_check
  multi_thread_need_detect
output:
  solo_suitability_result
stop_condition:
  multi-thread work is required
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

### Project Surface Pack

```text
functions:
  project_surface_confirm
  local_rules_discover
  publish_boundary_bind
  verification_surface_discover
output:
  project_surface_packet
stop_condition:
  project surface cannot be located or created
```

### Scope Lock Pack

```text
functions:
  allowed_change_bind
  forbidden_change_bind
  expected_files_estimate
  verification_requirement_bind
output:
  scope_lock_packet
stop_condition:
  requested scope is too broad for single-thread work
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

### Agent Role Draft Pack

```text
functions:
  needed_role_detect
  toml_agent_contract_draft
  unnecessary_agent_skip_reason
  active_agent_write
output:
  active_agent_plan
stop_condition:
  no clear role boundary exists
```

### Design Checkpoint Pack

```text
functions:
  design_stage_record
  forbidden_change_record
  verification_plan_record
  no_agent_reason_or_agent_need_record
output:
  design_checkpoint
stop_condition:
  design checkpoint cannot name scope, forbidden changes, and required checks
```

### Agent Sequence Pack

```text
functions:
  agent_dependency_order
  sequential_execution_plan
  reentry_checkpoint_bind
output:
  agent_sequence
stop_condition:
  roles require independent parallel threads
```

### Code Work Pack

```text
functions:
  repo_pattern_follow
  minimal_patch_plan
  code_edit_execute
  changed_files_track
output:
  code_work_result
stop_condition:
  change would violate locked scope
```

### Implementation Checkpoint Pack

```text
functions:
  changed_files_record
  active_agent_output_collect
  scope_drift_check
  verification_request_record
output:
  implementation_checkpoint
stop_condition:
  implementation cannot be compared against the design checkpoint
```

### Verification Gate Pack

```text
functions:
  checks_select
  checks_run_or_record_blocker
  failure_interpret
  pass_fail_decide
output:
  verification_gate_result
stop_condition:
  required verification is failing or unavailable
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
  release_artifact_note
output:
  release_boundary_result
stop_condition:
  publish target includes brain operation files
```

### Memory Export Pack

```text
functions:
  reusable_lesson_extract
  agent_pattern_extract
  non_exportable_filter
  memory_export_write
output:
  memory_export_packet
stop_condition:
  no reusable lesson or agent pattern exists
```

### Closeout Pack

```text
functions:
  final_report_write
  agent_archive_or_discard
  residual_risk_list
  next_action_report
output:
  closeout_report
stop_condition:
  verification state or agent state is unknown
```
