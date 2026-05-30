# Runtime Boundary

## 목적

이 파일은 정보조사 브레인에서 무엇이 브레인 본체이고, 무엇이 운용 중 생기는 로컬 기록인지 구분한다.

원소스와 맞출 때 운용 기록까지 동기화하지 않는다.
동기화 대상은 브레인의 정체성, 함수팩, 출처 계약, 출력 계약, 테스트 같은 본체 표면이다.

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
  - NOTES/
starter_root_relative:
  - 00_Orchestrator/
  - 01_Source_Pack/
  - 02_Brains/
  - scripts/
user_given_absolute:
  - 사용자가 수입, 조사, 검토 대상으로 직접 준 로컬 절대경로
  - 공개 산출물의 고정 의존성으로 쓰지 않는다.
external_url:
  - 사용자가 준 웹 링크
```

## Core Brain Surface

아래 파일은 브레인 본체다.
리뉴얼, 배포, 원소스 반영, 다른 사본 이식에서 우선 보존한다.

```text
START_HERE.md
BOOT.md
MAP.md
LOCAL_RULEBOOK.md
MEMORY_MAP.md
SESSION_CARD.md
BRAIN.md
MODE_REGISTRY.md
FUNCTION_PACKS.md
DECISION_TABLES.md
SOURCE_BINDINGS.md
SOURCE_REVIEW_BINDING.md
SOURCE_POLICY.md
OUTPUT_CONTRACT.md
ACCEPTANCE_TESTS.md
TASKS/PREFLIGHT_RESULT.md
```

## Runtime Local Surface

아래 파일과 폴더는 운용 중 생기는 로컬 상태다.
원소스와 맞추기 위해 억지로 동기화하지 않는다.

```text
TASKS/CURRENT_TASK.md
TASKS/RESEARCH_QUEUE.md
LOGS/SESSION_OPS_LOG.md
CAPSULES/CURRENT_CAPSULE.md
NOTES/SOURCE_LEDGER.md
NOTES/FINDINGS_INDEX.md
NOTES/OPEN_QUESTIONS.md
```

## Sync Rule

원소스가 갱신되면:

```text
import core protocol changes
keep local runtime records
recheck boot path
recheck FUNCTION_PACKS.md contract
recheck acceptance tests
do not delete local brain output unless explicitly requested
```

정보조사 브레인을 원소스나 배포 패키지로 승격할 때:

```text
keep core brain surface
reset runtime local surface to empty/default state
remove session-specific logs
keep PREFLIGHT_RESULT.md as build evidence
keep SOURCE_REVIEW_BINDING.md as source proof binding
keep DECISION_TABLES.md as repeated judgment evidence
```

## Promotion Rule

운용 중 쌓인 기록은 자동으로 브레인 본체가 되지 않는다.

```text
runtime observation
-> candidate note
-> repeated usefulness
-> contract update
-> acceptance test update
-> core brain surface update
```

## One-line Rule

브레인 본체는 동기화하고, 운용 기록은 로컬에 둔다.
