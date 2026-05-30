# Preflight Result

## Build Preflight

```text
preflight_result:
  normalized_goal: 범용 정보조사 브레인
  selected_function_packs:
    - goal_scope_lock
    - route_lock
    - evidence_uncertainty_split
    - output_contract_bind
    - memory_policy_check
    - trace_policy_check
  sufficient_layer: brain
  reason: 지속 정체성, 로컬 작업 적치, 반복 조사 기억, 출처 장부, 출력 계약, 재진입 표면이 필요하다.
  build_allowed: true
  required_surfaces:
    - START_HERE.md
    - BOOT.md
    - MAP.md
    - LOCAL_RULEBOOK.md
    - MEMORY_MAP.md
    - SESSION_CARD.md
    - BRAIN.md
    - MODE_REGISTRY.md
    - SOURCE_BINDINGS.md
    - SOURCE_POLICY.md
    - OUTPUT_CONTRACT.md
    - FUNCTION_PACKS.md
    - DECISION_TABLES.md
    - ACCEPTANCE_TESTS.md
    - TASKS/
    - LOGS/
    - CAPSULES/
    - NOTES/
next_action: 조사 요청을 받으면 질문을 좁히고 출처와 판단을 분리한 뒤 필요한 표면에만 기록한다.
```

## Why Not Smaller

### why_not_function_pack

부족하다.
이 브레인은 한 번의 제어 동작이 아니라 반복 조사, 출처 장부, 미확인 질문, 재진입 상태를 다룬다.

### why_not_engine

부족하다.
조사는 정해진 순서만 있는 내부 처리 장치가 아니라, 주제마다 출처 선택과 모드 전환이 필요하다.

### why_not_skill

부족하다.
단일 반복 절차보다 넓고, 로컬 메모리와 조사 누적 표면이 필요하다.

### why_not_brain_component

부족하다.
다른 브레인에 붙는 보조 부품이 아니라, 정보조사 요청 자체를 독립적으로 받아 처리해야 한다.

## Decision

`Info_Research_Brain`은 독립 브레인으로 유지한다.
단, 요청마다 필요한 함수팩만 작게 사용하고 조사 범위를 무한 확장하지 않는다.

## Runtime Function Packs

실제 조사 요청에서는 아래 함수팩을 사용한다.

- `Research Question Lock Pack`
- `Source Route Pack`
- `Evidence Split Pack`
- `Freshness and Risk Pack`
- `Conflict Map Pack`
- `Output and Memory Pack`

## Repeated Decisions

반복 판단이 3개 이상이므로 `DECISION_TABLES.md`를 둔다.

```text
route_decision
evidence_decision
source_grade_decision
freshness_decision
conflict_decision
memory_decision
stop_or_close_decision
```
