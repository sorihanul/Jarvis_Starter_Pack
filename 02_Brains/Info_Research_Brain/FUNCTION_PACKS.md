# Function Packs

## purpose

이 파일은 `Info_Research_Brain`이 실제 조사 요청을 처리할 때 사용하는 런타임 함수팩 표면이다.

`TASKS/PREFLIGHT_RESULT.md`가 "왜 독립 브레인인가"를 남긴다면, 이 파일은 "이 브레인이 조사 중 어떤 함수형 손발을 쓰는가"를 남긴다.

사용자는 함수 이름을 몰라도 된다. 브레인은 사용자의 자연어 요청을 내부 슬롯으로 좁힌 뒤 필요한 함수팩만 선택한다.

## runtime_flow

```text
user_request
-> intake_slots
-> function_pack_select
-> basic_function_calls
-> optional_brain_specific_functions
-> research_output
-> memory_trace_gate
-> handoff_or_stop
```

기본 순서는 아래를 따른다.

```text
scope_lock
-> missing_slot_detect
-> route_lock
-> output_schema_bind
-> memory_policy_check
-> trace_policy_check
-> gate_label
```

조사 요청이 출처 1개 검토에 가까우면 원소스의 `SOURCE_REVIEW_SKILL_SAMPLE_v0_1` 체인을 참조한다.

```text
scope_lock
input_contract_bind
dependency_check
cost_budget_lock
step_sequence_lock
output_schema_bind
acceptance_criteria_bind
fixture_contract_bind
memory_policy_check
trace_policy_check
gate_label
handoff_packet_bind
```

## function_use_principles

- 함수는 가장 작은 동작 하나만 맡는다.
- 함수팩은 함께 자주 쓰이는 작은 동작 묶음이다.
- 함수팩은 사용자 메뉴가 아니다.
- `fixed_inventory:false`
- `brain_specific_pack_design:true`
- 씨앗 함수가 충분하면 재사용한다.
- 씨앗 함수가 부족하면 같은 규격으로 브레인 목적에 맞는 작은 함수 후보를 만든다.
- 의미 판단, 출처 권위 비교, 종합 해석은 단일 basic function으로 처리하지 않는다.
- 실패는 항상 `failure_output` 형식으로 남긴다.
- 반복 판정 기준은 `DECISION_TABLES.md`를 따른다.

## function_pack_growth_rule

- 함수는 계속 커지는 단일 만능 함수가 아니다.
- 새 조사 목적이 반복되면 기존 pack을 비대하게 확장하기보다 목적별 function pack 후보로 분리한다.
- 단발 조사 요청은 새 function pack이 아니라 현재 pack 조합으로 처리한다.
- 새 function pack 후보는 하나의 조사 목적, 입력 조건, 출력 계약, stop condition, failure output을 가져야 한다.
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
- source-review proof: `01_Source_Pack/01_Modules/AILO_Function_Layer/06_Skill_Manufacturing_Proofs/SOURCE_REVIEW_SKILL_SAMPLE_v0_1/`

브레인 전용 후보 함수:

```text
question_lock
source_candidate_select
route_surface_detect
claim_extract
source_grade_label
inference_label
freshness_need_label
conflict_detect
authority_compare
read_unread_bind
```

이 후보들은 정보조사 브레인의 런타임 제어를 위한 작은 함수다.
반복 사용 중 안정성이 확인되면 별도 스킬 또는 공용 함수 후보로 승격할 수 있다.

## packs

### pack_name: Research Question Lock Pack

use_when:

```text
request_vague:true
topic_too_broad:true
scope_may_expand:true
```

functions:

```text
scope_lock
missing_slot_detect
question_lock
output_schema_bind
```

output:

```text
question:
bounded_scope:
success_criteria:
out_of_scope:
missing_slots:
ok:
```

stop_condition:

```text
required_slot_missing:true
scope_conflicts_with_user_ban:true
```

### pack_name: Source Route Pack

use_when:

```text
local_path_given:true
unknown_folder:true
source_bundle_large:true
multiple_possible_sources:true
```

functions:

```text
route_lock
source_candidate_select
route_surface_detect
cost_budget_lock
dependency_check
```

output:

```text
first_read:
second_read:
do_not_read_by_default:
read_limit:
route_risk:
stop_when:
ok:
```

stop_condition:

```text
path_missing:true
no_valid_first_route:true
read_budget_exceeded:true
```

### pack_name: Evidence Split Pack

use_when:

```text
claim_check_needed:true
source_quality_varies:true
uncertainty_present:true
```

functions:

```text
claim_extract
source_grade_label
inference_label
output_schema_bind
acceptance_criteria_bind
```

output:

```text
claims:
evidence:
source_grade:
verified_fact:
source_backed_inference:
interpretation:
unknown_or_risk:
acceptance_check:
ok:
```

stop_condition:

```text
no_source_evidence:true
unsupported_claim_would_be_presented_as_fact:true
```

### pack_name: Freshness and Risk Pack

use_when:

```text
freshness_sensitive:true
high_stakes:true
news_policy_price_law_medical_finance_security:true
```

functions:

```text
freshness_need_label
gate_label
cost_budget_lock
dependency_check
output_schema_bind
```

output:

```text
freshness_required:
current_source_needed:
risk_level:
advice_boundary:
allowed_answer_shape:
gate:
ok:
```

stop_condition:

```text
current_source_required_but_unavailable:true
unsafe_execution_advice_risk:true
gate:"HOLD|BLOCK|ESCALATE"
```

### pack_name: Conflict Map Pack

use_when:

```text
source_conflict:true
local_vs_current_conflict:true
version_or_date_conflict:true
```

functions:

```text
conflict_detect
authority_compare
source_grade_label
inference_label
handoff_packet_bind
```

output:

```text
conflicting_claims:
authority_map:
date_or_version_gap:
local_claim:
current_external_claim:
resolution_status:
next_check:
ok:
```

stop_condition:

```text
conflict_cannot_be_resolved_with_available_sources:true
jurisdiction_or_version_context_missing:true
```

### pack_name: Source Review Skill Link Pack

use_when:

```text
single_source_review:true
review_goal_given:true
repeatable_source_review_needed:true|false
```

functions:

```text
scope_lock
input_contract_bind
dependency_check
cost_budget_lock
step_sequence_lock
output_schema_bind
acceptance_criteria_bind
fixture_contract_bind
memory_policy_check
trace_policy_check
gate_label
handoff_packet_bind
```

output:

```text
source_path:
review_goal:
ordered_steps:
required_fields:
pass_if:
fail_if:
memory_policy:
trace_policy:
gate:
handoff_packet:
ok:
```

stop_condition:

```text
source_path_missing:true
local_read_permission_missing:true
unsupported_claim:true
unbounded_rewrite_risk:true
```

### pack_name: Output and Memory Pack

use_when:

```text
answer_ready:true
output_shape_needed:true
memory_candidate_possible:true
handoff_needed:true|false
```

functions:

```text
output_schema_bind
read_unread_bind
memory_policy_check
trace_policy_check
handoff_packet_bind
```

output:

```text
output_type:
read:
unread:
required_sections:
forbidden_sections:
memory_policy:
memory_candidate:
trace_policy:
handoff_packet:
ok:
```

stop_condition:

```text
read_unread_not_separated:true
memory_candidate_is_source_copy:true
output_schema_missing:true
```

## default_combinations

quick_brief:

```text
Research Question Lock Pack
-> Source Route Pack
-> Evidence Split Pack
-> Output and Memory Pack
```

local_folder_scan:

```text
Research Question Lock Pack
-> Source Route Pack
-> Evidence Split Pack
-> Output and Memory Pack
```

single_source_review:

```text
Research Question Lock Pack
-> Source Review Skill Link Pack
-> Output and Memory Pack
```

freshness_sensitive_research:

```text
Research Question Lock Pack
-> Freshness and Risk Pack
-> Source Route Pack
-> Evidence Split Pack
-> Output and Memory Pack
```

conflict_check:

```text
Research Question Lock Pack
-> Source Route Pack
-> Evidence Split Pack
-> Conflict Map Pack
-> Output and Memory Pack
```

## failure_output

모든 함수팩은 실패할 때 아래 형식을 따른다.

```text
ok:false
reason:
missing_slots:
failed_pack:
next_pack:
stop_condition:
suggested_layer:
```

`suggested_layer` 값:

```text
basic_function_tightening
function_pack
research_engine_candidate
research_skill_candidate
brain_component_candidate
domain_research_brain_candidate
```

## promotion_rule

함수팩으로 충분한 경우:

```text
single_use:true
identity_required:false
strict_order_required:false
user_callable_repeatable:false
```

엔진 후보:

```text
strict_order_required:true
intermediate_handoff_required:true
verification_gate_required:true
wrong_order_breaks_result:true
```

스킬 후보:

```text
user_callable_repeatable:true
procedure_name_needed:true
examples_required:true
acceptance_tests_required:true
```

브레인 부품 후보:

```text
identity_required:true
boundary_required:true
memory_surface_required:true
output_contract_required:true
operating_rule_required:true
```

도메인 연구 브레인 후보:

```text
domain_identity_required:true
long_running_research:true
domain_memory_required:true
special_source_policy_required:true
```

## one-line rule

정보조사 브레인은 원소스의 씨앗 함수를 그대로 베끼는 것이 아니라, 조사 목적에 맞는 작은 함수팩을 설계해 사용한다. 출처 1개 검토처럼 이미 proof가 있는 반복 절차는 `SOURCE_REVIEW_SKILL_SAMPLE_v0_1` 체인을 참고해 구조를 맞춘다.
