# Brain Build Protocol v0.2

## 목적

사용자가 새 브레인을 요청했을 때 메인 브레인이 따르는 제작 절차다.

목표는 사용자가 긴 명령어를 외우지 않아도, 호스트 작업 환경에서 바로 부팅 가능한 독립 브레인 구조와 소환 문구를 만드는 것이다.

## Function Pack Preflight

브레인 제작 요청이 들어와도 바로 브레인 폴더를 만들지 않는다.
먼저 요청이 정말 브레인이 필요한지 확인한다.

```text
사용자 요청
-> 의도 슬롯 잠금
-> 필요한 함수팩 선택
-> 브레인으로 만들지, 스킬/엔진/부품으로 충분한지 판정
-> 브레인 제작 프로토콜 실행
```

이 단계의 목적은 브레인 남발을 막는 것이다.
사용자는 브레인이라고 말했더라도 실제로는 스킬, 엔진, 브레인 부품, 또는 단순 함수팩이면 충분할 수 있다.

## 사전 판정 기준

### 함수팩으로 충분한 경우

아래에 해당하면 새 브레인을 만들지 않는다.

```text
single_session_task:true
identity_required:false
memory_surface_required:false
local_rule_required:false
reusable_folder_required:false
```

예:

```text
"이 요청 범위만 잠가줘."
"읽을 파일 순서만 정해줘."
"출력 형식만 잡아줘."
```

### 엔진 후보인 경우

아래에 해당하면 브레인이 아니라 엔진 후보로 본다.

```text
strict_order_required:true
intermediate_handoff_required:true
verification_gate_required:true
wrong_order_breaks_result:true
identity_required:false
```

예:

```text
"자료를 읽기 경로, 근거 확인, 출력 형식 순서로 검증 보고서화해줘."
```

### 스킬 후보인 경우

아래에 해당하면 브레인이 아니라 스킬 후보로 본다.

```text
user_callable_procedure:true
repeatable:true
examples_required:true
acceptance_tests_required:true
independent_identity_required:false
```

예:

```text
"앞으로 자주 쓸 프롬프트 검증 절차로 만들어줘."
```

### 브레인 부품 후보인 경우

아래에 해당하면 독립 브레인보다 브레인 부품 후보로 본다.

```text
belongs_to_existing_brain:true
identity_required:false
memory_surface_required:limited
output_contract_required:true
local_rule_required:limited
```

예:

```text
"정보형 브레인에 항상 붙을 자료 읽기 부품을 만들어줘."
```

### 독립 브레인이 필요한 경우

아래에 해당할 때만 독립 브레인 제작으로 간다.

```text
persistent_identity_required:true
domain_or_role_boundary_required:true
local_memory_required:true
local_rule_required:true
output_contract_required:true
reentry_required:true
task_deposit_required:true
```

예:

```text
"음악 연구소 브레인 만들어줘."
"검증 전용 브레인 만들어줘. 계속 개선하면서 쓸 거야."
"정보형 브레인 만들어줘. 자료 수집과 위키화를 계속 맡길 거야."
```

## Preflight 출력

브레인 제작 전에는 내부적으로 아래 형태를 만든다.

```text
preflight_result:
  normalized_goal:
  selected_function_packs:
  sufficient_layer: function_pack | engine | skill | brain_component | brain
  reason:
  build_allowed: true | false
  required_surfaces:
  next_action:
```

`build_allowed:false`이면 브레인 폴더를 만들지 않는다.
대신 스킬, 엔진, 부품, 함수팩 설계로 응답한다.

`build_allowed:true`이면 이 결과를 새 브레인 안의 `TASKS/PREFLIGHT_RESULT.md`에 남긴다.
즉 preflight는 채팅 중 설명으로 끝나지 않고, 산출 브레인의 재진입 표면에 남아야 한다.

또한 독립 브레인은 `FUNCTION_PACKS.md`를 가진다.
`TASKS/PREFLIGHT_RESULT.md`가 제작 근거라면, `FUNCTION_PACKS.md`는 실행 구조다.

```text
PREFLIGHT_RESULT.md
-> why this should be a brain

FUNCTION_PACKS.md
-> how this brain uses functions and function packs at runtime
```

## 제작 순서

1. 사용자 요청을 목적, 사용자, 산출물, 금지로 정규화한다.
2. Function Pack Preflight를 수행한다.
3. 함수팩, 엔진, 스킬, 브레인 부품으로 충분한지 판정한다.
4. `sufficient_layer: brain`일 때만 독립 브레인 제작으로 진행한다.
5. 브레인이 직접 맡을 일과 맡지 않을 일을 나눈다.
6. 필요한 원천소스를 고른다.
7. 브레인 이름과 폴더 이름을 정한다.
8. 최소 완전체 파일 세트를 만든다.
9. `TASKS/PREFLIGHT_RESULT.md`에 preflight 결과를 기록한다.
10. `FUNCTION_PACKS.md`에 브레인의 런타임 함수팩 표면을 만든다.
11. 반복 판단이 3개 이상이면 `DECISION_TABLES.md`를 만든다.
12. 재진입 표면과 작업 적치면을 만든다.
13. 새 스레드 시작 문구를 제공한다.
14. acceptance test를 붙인다.

## 요청 기록 위치

- 새 브레인 제작 요청 초안은 `../TASKS/BRAIN_BUILD_REQUESTS`에 둔다.
- 제작 중 결정 기록은 `../LOGS/SESSION_OPS_LOG.md`에 남긴다.
- 다음 세션에 넘길 요약은 `../CAPSULES/CURRENT_CAPSULE.md`에 반영한다.
- `../../01_Source_Pack` 안에는 제작 진행 기록을 새로 쓰지 않는다.

## 경로 기준

- `../TASKS`, `../LOGS`, `../CAPSULES`는 현재 파일이 있는 `00_Orchestrator/Jarvis_Main_Brain` 기준의 오케스트레이터 작업면이다.
- 아래 기본 구조의 `START_HERE.md`, `MAP.md`, `LOCAL_RULEBOOK.md`, `SOURCE_BINDINGS.md`, `OUTPUT_CONTRACT.md` 등은 현재 패키지 안의 기존 파일이 아니라, 새로 만들 브레인 루트 안에 생성할 파일이다.
- `../../01_Source_Pack`은 참고할 원천소스 위치이며, 새 브레인이 이 폴더를 다시 읽어야만 작동하도록 만들지 않는다.

## Path Basis 규칙

새 브레인이 경로를 남길 때는 그 경로가 어느 루트를 기준으로 하는지 반드시 밝힌다.

```text
path_basis:
  brain_root_relative:
    - 새 브레인 루트 기준 경로
    - 예: START_HERE.md, FUNCTION_PACKS.md, TASKS/CURRENT_TASK.md, REPORTS/
  starter_root_relative:
    - Jarvis Starter Pack 루트 기준 경로
    - 예: 00_Orchestrator/, 01_Source_Pack/, 02_Brains/, scripts/
  user_given_absolute:
    - 사용자가 검증/조사 대상으로 직접 준 절대경로
    - 공개 산출물의 고정 의존성으로 쓰지 않는다.
  external_url:
    - 웹 URL
```

`SOURCE_BINDINGS.md`, `JARVIS_STARTER_BINDING.md`, `RUNTIME_BOUNDARY.md`처럼 새 브레인 바깥 표면을 가리키는 파일은 `path_basis` 섹션을 가진다.

금지:
- `01_Source_Pack/...`을 쓰면서 `starter_root_relative`라고 밝히지 않기
- `scripts/...`를 쓰면서 패키지 루트 기준이라고 밝히지 않기
- 새 브레인 내부 파일과 스타터 루트 파일을 같은 기준처럼 섞기

## 기본 브레인 폴더

```text
<Brain_Name>/
  START_HERE.md
  MAP.md
  LOCAL_RULEBOOK.md
  MEMORY_MAP.md
  SESSION_CARD.md
  BOOT.md
  BRAIN.md
  MODE_REGISTRY.md
  FUNCTION_PACKS.md
  DECISION_TABLES.md (optional when repeated decisions exist)
  SOURCE_BINDINGS.md
  OUTPUT_CONTRACT.md
  ACCEPTANCE_TESTS.md
  TASKS/
    PREFLIGHT_RESULT.md
    CURRENT_TASK.md
  LOGS/
    SESSION_OPS_LOG.md
  CAPSULES/
    CURRENT_CAPSULE.md
```

## 최소 파일 역할

- `START_HERE.md`: 사람이 처음 열 때 보는 진입면
- `MAP.md`: 폴더와 파일의 길찾기
- `LOCAL_RULEBOOK.md`: 이 브레인 안에서만 적용되는 운영 규칙
- `MEMORY_MAP.md`: 무엇이 정체성, 경로, 정본, 흔적인지 구분하는 지도
- `SESSION_CARD.md`: 새 스레드가 자신의 역할과 경계를 빠르게 잡는 카드
- `BOOT.md`: 새 스레드가 처음 읽는 파일
- `BRAIN.md`: 정체성, 역할, 금지
- `MODE_REGISTRY.md`: 작업 모드
- `FUNCTION_PACKS.md`: 이 브레인이 실제 작업 중 사용하는 함수팩, 선택 규칙, 실패/중단 형식
- `DECISION_TABLES.md`: 반복 판단이 흔들리지 않도록 고정하는 판정표
- `SOURCE_BINDINGS.md`: 참고할 원천소스와 path basis
- `OUTPUT_CONTRACT.md`: 답변과 산출물 형식
- `ACCEPTANCE_TESTS.md`: 제대로 작동하는지 확인할 테스트
- `TASKS/PREFLIGHT_RESULT.md`: 왜 함수팩, 엔진, 스킬, 브레인 부품이 아니라 독립 브레인인지 남기는 v3 사전 판정 기록
- task current file: 현재 작업 상태
- session log file: 진행 기록
- capsule file: 다음 세션 인수인계

## Boot Route 규칙

새 브레인의 `START_HERE.md`와 `BOOT.md`는 `MAP.md`를 초반 읽기 순서에 포함한다.

권장 순서:

```text
START_HERE.md
MAP.md
LOCAL_RULEBOOK.md
MEMORY_MAP.md
SESSION_CARD.md
BRAIN.md
FUNCTION_PACKS.md
SOURCE_BINDINGS.md
OUTPUT_CONTRACT.md
TASKS/PREFLIGHT_RESULT.md
TASKS/CURRENT_TASK.md
```

특수 브레인이 `RUNTIME_BOUNDARY.md`, binding 문서, domain policy를 가진다면 `MEMORY_MAP.md` 뒤와 `BRAIN.md` 앞 사이에 둔다.

금지:
- `MAP.md` 없이 `LOCAL_RULEBOOK.md`나 세부 정책으로 바로 들어가기
- `START_HERE.md`와 `BOOT.md`의 읽기 순서가 서로 다른 의미를 갖게 만들기

## Source Binding 규칙

새 브레인은 항상 `SOURCE_BINDINGS.md`를 가진다.

도메인 특성상 `SOURCE_POLICY.md`, `EVIDENCE_POLICY.md`, `DATA_POLICY.md` 같은 별도 출처 정책 파일이 필요할 수 있다.
그 경우에도 `SOURCE_BINDINGS.md`를 생략하지 않는다.

```text
SOURCE_BINDINGS.md
-> 어떤 출처 표면을 쓸 수 있는가
-> 각 출처 경로가 brain_root_relative, starter_root_relative, user_given_absolute, external_url 중 무엇인지

SOURCE_POLICY.md
-> 그 출처를 어떻게 판단하고 다룰 것인가
```

즉 `SOURCE_POLICY.md`는 `SOURCE_BINDINGS.md`를 대체하지 않는다.
정책 파일이 추가되면 `SOURCE_BINDINGS.md`에서 그 관계를 짧게 명시한다.

## Preflight Result 파일 규칙

새 독립 브레인은 `TASKS/PREFLIGHT_RESULT.md`를 가진다.

이 파일은 아래를 포함한다.

```text
preflight_result:
  normalized_goal:
  selected_function_packs:
  sufficient_layer: brain
  reason:
  build_allowed: true
  required_surfaces:
  next_action:
```

또한 아래 네 가지 축을 분리해 쓴다.

```text
why_not_function_pack:
why_not_engine:
why_not_skill:
why_not_brain_component:
```

이 파일의 목적은 “좋아 보이는 브레인 설명”이 아니다.
v3가 함수팩 사전 판정을 거쳐 독립 브레인을 만들었다는 증거를 남기는 것이다.

## Function Packs 파일 규칙

새 독립 브레인은 `FUNCTION_PACKS.md`를 가진다.

이 파일은 아래를 포함한다.

```text
purpose:
runtime_flow:
function_use_principles:
pack_design_basis:
packs:
  - pack_name:
    use_when:
    functions:
    output:
    stop_condition:
default_combinations:
failure_output:
promotion_rule:
```

`FUNCTION_PACKS.md`는 사용자 메뉴가 아니다.
사용자는 함수 이름을 몰라도 된다.
브레인이 사용자의 자연어 요청을 내부 작업 슬롯으로 좁힌 뒤, 필요한 함수팩만 선택한다.

`FUNCTION_PACKS.md`는 고정 함수 목록을 복사하는 파일도 아니다.
각 브레인은 자기 목적에 맞는 함수와 함수팩을 설계한다.
기존 씨앗 함수가 충분하면 재사용하고, 부족하면 같은 규격으로 새 함수를 만든다.

```text
seed_functions_are_examples:true
fixed_inventory:false
brain_specific_pack_design:true
new_function_allowed_when_contract_clear:true
```

## Function Pack Growth Rule

함수는 계속 커지는 단일 만능 함수가 아니다.
새 목적이 반복되면 기존 함수를 비대하게 확장하기보다 목적별 function pack 후보로 분리한다.

```text
do_not_grow_one_function_forever:true
prefer_new_purpose_pack_when_repeated:true
single_use_request_is_not_new_pack:true
stable_output_contract_required:true
stop_condition_required:true
```

새 function pack 후보는 아래를 가져야 한다.

```text
purpose:
use_when:
input_condition:
functions:
output_contract:
stop_condition:
failure_output:
promotion_condition:
```

승격 기준:

```text
repeated_need:true
boundary_clear:true
output_contract_stable:true
existing_pack_insufficient:true
single_use_only:false
```

금지:
- `Verification Report Pack`처럼 기존 팩 하나가 모든 판단을 먹게 만들기
- 새 목적이 한 번 나왔다는 이유만으로 새 pack을 만들기
- output contract와 stop condition 없는 pack 만들기
- pack 이름만 나누고 내부 역할은 겹치게 만들기

함수팩은 아래처럼 작아야 한다.

```text
question lock pack
source route pack
evidence split pack
output contract pack
memory policy pack
permission gate pack
```

아래처럼 크면 안 된다.

```text
do all research pack
write everything pack
manage whole brain pack
think like expert pack
```

각 함수팩은 실패 형식을 가져야 한다.

```text
ok:false
reason:
missing_slots:
next_pack:
stop_condition:
```

이 파일의 목적은 v3 브레인이 관성적으로 룰북 문장만 따라 일하지 않게 하는 것이다.
브레인은 자기 정체성에 맞는 함수형 손발을 가져야 한다.
그 손발은 공용 씨앗을 그대로 복사한 목록이 아니라, 브레인 목적에 맞게 설계된 런타임 함수팩이어야 한다.

## Decision Tables 파일 규칙

새 브레인이 반복 판단을 가진다면 `DECISION_TABLES.md`를 둔다.

반복 판단은 같은 기준을 여러 번 적용해야 하는 경우다.

```text
route_decision
sufficiency_decision
priority_or_severity_decision
stop_or_close_decision
retry_or_revalidation_decision
source_or_evidence_decision
```

생성 기준:

```text
repeated_decision_count >= 3
-> create DECISION_TABLES.md

repeated_decision_count < 3
-> keep the short rule inside OUTPUT_CONTRACT.md or LOCAL_RULEBOOK.md
```

`DECISION_TABLES.md`는 작업 로그가 아니다.
브레인이 같은 상황에서 같은 판정을 내리도록 돕는 기준 정본이다.

기본 형태:

```text
# DECISION TABLES

## purpose

## shared rules

## route_decision

## sufficiency_decision

## priority_or_severity_decision

## stop_or_close_decision

## retry_or_revalidation_decision
```

금지:
- 단순 설명문을 `DECISION_TABLES.md`로 만들기
- 한 번만 쓰는 판단을 표로 과잉 고정하기
- `DECISION_TABLES.md`를 작업 로그나 감상 기록으로 쓰기
- `FUNCTION_PACKS.md`와 충돌하는 판정 기준을 만들고 관계를 설명하지 않기

## 질문 정책

막히지 않으면 바로 초안을 만든다.

질문이 필요하면 한 번에 핵심만 묻는다.

## 완료 기준

- 새 브레인 폴더가 있다.
- Function Pack Preflight 결과가 있다.
- Function Pack Preflight 결과가 새 브레인의 `TASKS/PREFLIGHT_RESULT.md`에 기록되어 있다.
- 새 브레인의 `FUNCTION_PACKS.md`에 런타임 함수팩 표면이 있다.
- 새 브레인의 `SOURCE_BINDINGS.md` 또는 binding 문서에 `path_basis`가 있다.
- 반복 판단이 3개 이상이면 새 브레인의 `DECISION_TABLES.md`에 판정표가 있다.
- 왜 브레인이 필요한지 설명되어 있다.
- 스킬, 엔진, 브레인 부품으로 충분하지 않은 이유가 있다.
- `START_HERE.md`와 `MAP.md`가 있다.
- `START_HERE.md`와 `BOOT.md`의 초반 읽기 순서에 `MAP.md`가 있다.
- `LOCAL_RULEBOOK.md`, `MEMORY_MAP.md`, `SESSION_CARD.md`가 있다.
- `BOOT.md`가 바로 부팅 가능하다.
- 원천소스 참조가 명시되어 있다.
- 금지 범위가 있다.
- 작업 기록 위치가 있다.
- 테스트 문장이 있다.
- 사용자가 새 스레드에 붙일 시작 문구가 있다.

## 금지

- Function Pack Preflight 없이 바로 브레인 폴더부터 만들지 않는다.
- Function Pack Preflight를 채팅 설명으로만 남기고 새 브레인 내부에 기록하지 않는다.
- `FUNCTION_PACKS.md` 없이 룰북 문장만으로 브레인을 작동하게 만들지 않는다.
- 반복 판단이 3개 이상인데도 판정표 없이 즉흥 판단하게 만들지 않는다.
- 스킬이면 충분한 요청을 독립 브레인으로 키우지 않는다.
- 엔진이면 충분한 요청을 정체성 있는 브레인으로 키우지 않는다.
- 기존 브레인에 붙을 부품이면 충분한 요청을 새 독립 브레인으로 키우지 않는다.
- `SOURCE_POLICY.md` 같은 도메인 정책 파일을 만들었다는 이유로 `SOURCE_BINDINGS.md`를 생략하지 않는다.
- `START_HERE.md`나 `BOOT.md`에서 `MAP.md`를 건너뛰고 바로 세부 정책으로 들어가지 않는다.
- `01_Source_Pack`, `00_Orchestrator`, `02_Brains`, `scripts` 경로를 쓰면서 `starter_root_relative` 기준을 밝히지 않는다.
- 사용자가 긴 전문 주문을 직접 작성해야만 작동하는 구조로 만들지 않는다.
- 원천소스를 새 브레인 안에서 다시 읽어야만 이해되는 구조로 만들지 않는다.
- `01_Source_Pack` 안에 새 브레인 작업 기록을 남기지 않는다.
- 모든 모듈을 복제하지 않는다.
- 브레인 제작을 설명만 하고 소환 문구를 빠뜨리지 않는다.
