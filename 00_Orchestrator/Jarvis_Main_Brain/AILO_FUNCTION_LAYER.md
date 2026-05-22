# AILO Function Layer v0.2

## 목적

이 문서는 자비스 스타터 v3에서 AILO 함수화가 맡는 역할을 정한다.

AILO 의도 슬롯은 사용자의 말을 실행 조건으로 정리한다.
AILO 함수화는 그 실행 조건을 작고 호출 가능한 동작으로 나누고, 관련 동작을 함수팩으로 묶어 스킬, 엔진, 브레인 부품으로 쓸 수 있게 한다.

```text
사용자 자연어
-> AILO식 의도 슬롯
-> AILO 함수
-> AILO 함수팩
-> 엔진 / 스킬 / 브레인 부품
-> 브레인 / 프로젝트 / 옵션팩
-> 검증
```

## 핵심 정의

AILO 함수화는 프롬프트를 크게 만드는 장치가 아니다.
AILO 함수화는 반복되는 동작을 작게 나누고, 관련 동작을 함수팩으로 묶는 장치다.
AILO 함수화는 고정된 함수 목록을 외우는 방식이 아니다.
함수와 함수팩을 만드는 규격을 사용해, 작업 목적에 맞는 작은 동작과 묶음을 설계하는 방식이다.

```text
function
= one smallest action
= input slots + bounded operation + output schema + guards

function pack
= related smallest action unit
= small group of functions that belongs together

function pack group
= function packs combined for a larger purpose
```

함수팩 묶음은 사용 방식에 따라 달라진다.

```text
strict order + intermediate handoff + verification gate
-> engine

user-callable repeatable procedure
-> skill

identity + boundary + memory + output contract + operating rules
-> brain component
```

## 계층

```text
Function
-> Function Pack
-> Function Pack Group
   -> Engine
   -> Skill
   -> Brain component
-> Brain
```

## 함수팩의 크기

함수팩은 검증 전체, 글쓰기 전체, 코딩 전체처럼 큰 작업을 뜻하지 않는다.
함수팩은 가장 작은 행동 단위 묶음이다.

예:

```text
Goal Lock Pack
- goal_lock
- scope_lock
- success_criteria_bind

Evidence Check Pack
- claim_extract
- evidence_check
- uncertainty_split

Issue Label Pack
- issue_detect
- severity_label
- blocking_reason_bind
```

이 함수팩들을 순서와 검증 게이트로 묶으면 엔진이 된다.
이 함수팩이나 엔진을 사용자가 호출할 수 있는 반복 절차로 포장하면 스킬이 된다.
이것들을 정체성, 경계, 메모리, 산출물 규칙과 함께 운용하면 브레인 부품이 된다.

## 기본 함수군

현재 v3에 들어온 기본 함수군은 함수화 레이어의 예시이자 검증된 씨앗이다.
이 함수들은 작업 제어면을 주로 다룬다.
이 씨앗은 기본 재료이지 허용 목록의 끝이 아니다.

```text
scope
route
missing input
output shape
memory side effect
trace weight
permission gate
stop condition
retry rule
cost budget
dependency
handoff packet
```

## 함수로 처리하지 않는 것

아래는 단일 함수로 처리하지 않는다.

```text
숨은 전제 해석
근거 권위 비교
도메인 렌즈 판단
창작 전략 판단
독자 자세 변화
브레인 정체성 판단
여러 단계 엔진 순서
```

이런 작업은 함수팩, 인지함수, 스킬, 엔진, 브레인 중 하나로 올린다.

## 사용 규칙

- 함수는 가장 작은 동작 하나만 맡는다.
- 함수팩은 관련된 가장 작은 행동 단위로 유지한다.
- 함수팩이 너무 커지면 스킬이나 엔진 후보로 올린다.
- 순서와 중간 산출물과 검증 게이트가 중요하면 엔진으로 본다.
- 사용자가 반복 호출하는 작업 절차면 스킬로 본다.
- 브레인 정체성, 경계, 메모리, 산출물 규칙까지 가지면 브레인 부품으로 본다.
- 함수와 함수팩은 기본값으로 메모리를 쓰지 않는다.
- 실패할 때도 `ok:false`, `reason`, `missing_slots`, `suggested_layer`를 남긴다.
- 의미 판단이 들어가면 단순 제어 함수에서 멈추고 상위 계층으로 넘긴다.

## 현재 보유 함수/함수팩 씨앗

v3가 직접 활용하는 현재 씨앗은 두 묶음이다.

```text
stable function seeds v0.1
- scope_lock
- route_lock
- missing_slot_detect
- output_schema_bind
- memory_policy_check
- trace_policy_check
- gate_label

skill-skeleton functions v0.2
- input_contract_bind
- step_sequence_lock
- acceptance_criteria_bind
- fixture_contract_bind
- handoff_packet_bind
- retry_policy_check
- cost_budget_lock
- dependency_check
```

v0.1은 안정 함수 씨앗이다.
v0.2는 스킬 골격 제작을 돕는 stable candidate다.

이 둘은 최종 목록이 아니다.
v3의 본체는 “함수 목록”이 아니라 “함수와 함수팩을 만들고 묶는 방식”이다.

## 함수 제작 방식

새 함수는 아래 조건을 만족할 때 만든다.

```text
one_small_action:true
input_slots_defined:true
output_schema_defined:true
guards_defined:true
failure_output_defined:true
memory_side_effect_controlled:true
```

새 함수팩은 아래 조건을 만족할 때 만든다.

```text
related_small_actions:true
use_condition_defined:true
output_contract_defined:true
stop_condition_defined:true
not_user_menu:true
not_whole_workflow:true
```

즉 브레인은 고정된 함수 목록에서만 고르는 것이 아니다.
브레인은 자기 목적에 맞는 함수를 설계하고, 그 함수들을 작은 함수팩으로 묶을 수 있다.

다만 새 함수나 함수팩을 만들 때도 아래를 지킨다.

```text
reuse_seed_when_enough:true
create_only_when_repeated_or_needed:true
do_not_make_large_pack:true
promote_when_order_or_user_call_or_identity_required:true
```

## 원천소스 위치

함수화 계약과 검증 자료는 아래에서 확인한다.

```text
../../01_Source_Pack/01_Modules/AILO_Function_Layer/START_HERE.md
../../01_Source_Pack/01_Modules/AILO_Function_Layer/MAP.md
```

기본 부팅 때 이 폴더 전체를 읽지 않는다.
아래 상황에서만 연다.

- 새 스킬을 만들 때
- 새 브레인의 함수팩을 만들 때
- 새 브레인의 작업 표면을 작게 잠글 때
- 요청의 범위, 경로, 출력, 기억, 추적, 권한, 중단 조건이 흔들릴 때
- 스킬 제조 proof나 하네스 검증이 필요할 때
- 함수, 함수팩, 엔진, 스킬, 브레인 부품의 경계를 확인해야 할 때

## 한 줄 기준

AILO 함수화는 사용자의 의도를 더 크게 해석하는 장치가 아니라, 필요한 동작을 함수로 나누고 관련 동작을 함수팩으로 묶어 엔진, 스킬, 브레인 부품으로 조립하게 하는 v3의 제작 제어층이다.
