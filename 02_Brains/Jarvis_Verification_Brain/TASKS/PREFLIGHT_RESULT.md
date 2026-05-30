# Preflight Result

## Build Preflight

```text
preflight_result:
  normalized_goal: 범용 검증 브레인 + Jarvis Starter Pack 검증 바인딩
  selected_function_packs:
    - Target and Criteria Pack
    - Verification Route Pack
    - Proof Level Pack
    - Finding Severity Pack
    - Revalidation Pack
    - Verification Report Pack
  sufficient_layer: brain
  reason: 반복 검증, 증거 수준 관리, 심각도 분류, 재검증, 검증 큐, 보고 표면, Jarvis Starter 전용 바인딩이 필요하다.
  build_allowed: true
  required_surfaces:
    - START_HERE.md
    - BOOT.md
    - MAP.md
    - LOCAL_RULEBOOK.md
    - MEMORY_MAP.md
    - RUNTIME_BOUNDARY.md
    - SESSION_CARD.md
    - BRAIN.md
    - MODE_REGISTRY.md
    - FUNCTION_PACKS.md
    - DECISION_TABLES.md
    - SOURCE_BINDINGS.md
    - JARVIS_STARTER_BINDING.md
    - OUTPUT_CONTRACT.md
    - ACCEPTANCE_TESTS.md
    - TASKS/
    - LOGS/
    - CAPSULES/
    - REPORTS/
  next_action: 검증 요청을 받으면 대상, 목표, 성공 기준, 증거 수준을 잠그고 검증 보고로 닫는다.
```

## why_not_function_pack

부족하다.
검증 브레인은 단발 기준 잠금이 아니라 반복 검증, 검증 큐, 보고 표면, 재검증 기록을 다룬다.

## why_not_engine

부족하다.
검증 순서는 중요하지만 대상마다 검증 모드와 증거 수준이 달라지며, 지속 정체성과 로컬 기록이 필요하다.

## why_not_skill

부족하다.
단일 사용자 호출 절차보다 넓고, 브레인/문서/코드/배포 검증을 모두 다룰 범용 검증 정체성이 필요하다.

## why_not_brain_component

부족하다.
다른 브레인에 붙는 보조 부품이 아니라 독립적으로 검증 요청을 받고 보고를 닫아야 한다.

## Decision

`Jarvis_Verification_Brain`은 독립 브레인으로 유지한다.
