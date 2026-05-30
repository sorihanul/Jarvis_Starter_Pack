# Runtime Boundary

## 목적

검증 브레인의 본체와 운용 기록을 분리한다.

## path_basis

```text
brain_root_relative:
  - START_HERE.md
  - BOOT.md
  - MAP.md
  - DECISION_TABLES.md
  - TASKS/
  - LOGS/
  - CAPSULES/
  - REPORTS/
starter_root_relative:
  - 00_Orchestrator/
  - 01_Source_Pack/
  - 02_Brains/
  - scripts/
user_given_absolute:
  - 사용자가 검증 대상으로 직접 준 로컬 절대경로
  - 공개 산출물의 고정 의존성으로 쓰지 않는다.
external_url:
  - 사용자가 검증 대상으로 준 웹 링크
```

## Core Brain Surface

아래는 브레인 본체다.

```text
START_HERE.md
BOOT.md
MAP.md
LOCAL_RULEBOOK.md
MEMORY_MAP.md
RUNTIME_BOUNDARY.md
SESSION_CARD.md
BRAIN.md
MODE_REGISTRY.md
FUNCTION_PACKS.md
DECISION_TABLES.md
SOURCE_BINDINGS.md
JARVIS_STARTER_BINDING.md
OUTPUT_CONTRACT.md
ACCEPTANCE_TESTS.md
TASKS/PREFLIGHT_RESULT.md
```

## Runtime Local Surface

아래는 운용 중 생기는 로컬 상태다.

```text
TASKS/CURRENT_TASK.md
TASKS/VERIFICATION_QUEUE.md
LOGS/SESSION_OPS_LOG.md
CAPSULES/CURRENT_CAPSULE.md
REPORTS/
```

## Sync Rule

원소스나 상위 프로토콜이 갱신되면:

```text
import protocol changes
keep local verification records
recheck FUNCTION_PACKS.md contract
recheck SOURCE_BINDINGS.md
recheck ACCEPTANCE_TESTS.md
do not delete local reports unless explicitly requested
```

## Promotion Rule

운용 중 발견한 검증 패턴은 바로 본체가 되지 않는다.

```text
runtime finding
-> repeated pattern
-> function pack update
-> output contract update
-> acceptance test update
```

## One-line Rule

검증 브레인의 본체는 계약이고, 검증 기록은 로컬 상태다.
