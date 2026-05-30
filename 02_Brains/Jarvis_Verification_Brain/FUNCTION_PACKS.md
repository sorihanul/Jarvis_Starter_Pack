# Function Packs

## purpose

이 파일은 `Jarvis_Verification_Brain`이 실제 검증 중 사용하는 런타임 함수팩 표면이다.

## runtime_flow

```text
user_request
-> target_lock
-> success_criteria_bind
-> proof_level_label
-> verification_route_lock
-> check_execution_or_static_review
-> finding_severity_label
-> revalidation_decision
-> report_bind
-> close_or_hold
```

## function_use_principles

- 함수팩은 검증 작업을 작게 나누는 내부 제어면이다.
- 사용자는 함수팩 이름을 몰라도 된다.
- `fixed_inventory:false`
- `brain_specific_pack_design:true`
- 증거 수준 판단은 과장하지 않는다.
- 심각도는 완료 판정에 직접 영향을 준다.
- 실패는 `failure_output` 형식으로 남긴다.
- 반복 판정 기준은 `DECISION_TABLES.md`를 따른다.

## function_pack_growth_rule

- 함수는 계속 커지는 단일 만능 함수가 아니다.
- 새 검증 목적이 반복되면 기존 함수를 비대하게 확장하기보다 목적별 function pack 후보로 분리한다.
- 단발 검증 요청은 새 function pack이 아니라 현재 pack 조합으로 처리한다.
- 새 function pack 후보는 하나의 검증 목적, 입력 조건, 출력 계약, stop condition, failure output을 가져야 한다.
- 반복되고 경계가 분명하며 출력 계약이 안정된 경우에만 새 pack으로 승격한다.

```text
do_not_grow_one_function_forever:true
prefer_new_purpose_pack_when_repeated:true
single_use_request_is_not_new_pack:true
stable_output_contract_required:true
stop_condition_required:true
```

## pack_design_basis

원소스 기준:

- stable basic functions v0.1: `scope_lock`, `route_lock`, `missing_slot_detect`, `output_schema_bind`, `memory_policy_check`, `trace_policy_check`, `gate_label`
- skill-skeleton functions v0.2: `input_contract_bind`, `step_sequence_lock`, `acceptance_criteria_bind`, `fixture_contract_bind`, `handoff_packet_bind`, `retry_policy_check`, `cost_budget_lock`, `dependency_check`
- verification source pack: `01_Source_Pack/06_Option_Packs/Verification_and_Proof_Pack/`

브레인 전용 후보 함수:

```text
target_lock
success_criteria_bind
failure_condition_bind
proof_level_label
check_route_lock
finding_severity_label
revalidation_scope_bind
close_status_label
```

## packs

### pack_name: Target and Criteria Pack

use_when:

```text
verification_target_unclear:true
success_criteria_missing:true
```

functions:

```text
scope_lock
target_lock
success_criteria_bind
failure_condition_bind
missing_slot_detect
```

output:

```text
target:
goal:
success_criteria:
failure_conditions:
evidence_needed:
out_of_scope:
ok:
```

stop_condition:

```text
target_missing:true
goal_unclear:true
criteria_not_testable:true
```

### pack_name: Verification Route Pack

use_when:

```text
files_or_commands_needed:true
route_unclear:true
large_target:true
```

functions:

```text
route_lock
check_route_lock
dependency_check
cost_budget_lock
gate_label
```

output:

```text
first_check:
conditional_checks:
do_not_check_by_default:
required_dependencies:
read_limit:
gate:
ok:
```

stop_condition:

```text
no_valid_check_route:true
dependency_missing:true
gate:"HOLD|BLOCK|ESCALATE"
```

### pack_name: Proof Level Pack

use_when:

```text
claim_needs_evidence:true
completion_claim_possible:true
```

functions:

```text
proof_level_label
output_schema_bind
acceptance_criteria_bind
```

output:

```text
claim:
proof_level:
evidence:
limits:
can_call_complete:
ok:
```

stop_condition:

```text
proof_level_overstated:true
evidence_missing:true
```

### pack_name: Finding Severity Pack

use_when:

```text
issue_found:true
severity_needed:true
```

functions:

```text
finding_severity_label
acceptance_criteria_bind
handoff_packet_bind
```

output:

```text
finding:
severity:
evidence:
why_it_matters:
fix_needed:
ok:
```

stop_condition:

```text
blocking_found:true
major_found:true
```

### pack_name: Revalidation Pack

use_when:

```text
fix_applied:true
fix_suggested:true
previous_failure_exists:true
```

functions:

```text
revalidation_scope_bind
step_sequence_lock
retry_policy_check
gate_label
```

output:

```text
original_failure:
fix_applied:
checks_rerun:
new_result:
remaining_risk:
close_status:
ok:
```

stop_condition:

```text
same_check_not_rerun:true
remaining_blocking_or_major:true
```

### pack_name: Verification Report Pack

use_when:

```text
verification_ready_to_report:true
```

functions:

```text
output_schema_bind
memory_policy_check
trace_policy_check
close_status_label
handoff_packet_bind
```

output:

```text
target:
goal:
success_criteria:
proof_level:
checks_run:
findings:
fixes_applied:
revalidation:
remaining_risks:
close_status:
next_action:
ok:
```

stop_condition:

```text
report_missing_required_field:true
close_status_contradicts_findings:true
```

## default_combinations

structure_validation:

```text
Target and Criteria Pack
-> Verification Route Pack
-> Proof Level Pack
-> Finding Severity Pack
-> Verification Report Pack
```

fix_and_revalidate:

```text
Target and Criteria Pack
-> Finding Severity Pack
-> Revalidation Pack
-> Verification Report Pack
```

release_hygiene:

```text
Target and Criteria Pack
-> Verification Route Pack
-> Proof Level Pack
-> Finding Severity Pack
-> Verification Report Pack
```

## failure_output

```text
ok:false
reason:
missing_slots:
failed_pack:
next_pack:
stop_condition:
suggested_layer:
```

## promotion_rule

함수팩으로 충분한 경우:

```text
single_validation:true
identity_required:false
repeatable_queue_required:false
```

엔진 후보:

```text
strict_order_required:true
intermediate_handoff_required:true
verification_gate_required:true
```

스킬 후보:

```text
user_callable_repeatable:true
examples_required:true
acceptance_tests_required:true
```

브레인 부품 후보:

```text
belongs_to_existing_brain:true
limited_memory_required:true
output_contract_required:true
```

## one-line rule

검증 브레인은 목표, 성공 기준, 증거 수준, 심각도, 재검증, 보고를 함수팩으로 나눠 처리한다.
