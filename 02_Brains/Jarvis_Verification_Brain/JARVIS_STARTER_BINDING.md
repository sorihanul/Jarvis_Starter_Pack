# Jarvis Starter Binding

## 목적

이 파일은 Jarvis Starter Pack 계열을 검증할 때 보는 전용 바인딩이다.

## path_basis

```text
brain_root_relative:
  - SOURCE_BINDINGS.md
  - FUNCTION_PACKS.md
  - OUTPUT_CONTRACT.md
  - REPORTS/
starter_root_relative:
  - BOOT.md
  - START_HERE.md
  - MAP.md
  - ACCEPTANCE_TESTS.md
  - RELEASE_CHECKLIST.md
  - scripts/release_check.ps1
  - 00_Orchestrator/
  - 01_Source_Pack/
  - 02_Brains/
user_given_absolute:
  - 사용자가 검증 대상으로 직접 준 Jarvis Starter Pack 로컬 사본 경로
  - 공개 산출물의 고정 의존성으로 쓰지 않는다.
external_url:
  - 사용자가 검증 대상으로 준 배포 저장소, 문서, 이슈, 릴리즈 링크
```

## 기본 검증 표면

```text
BOOT.md
START_HERE.md
MAP.md
ACCEPTANCE_TESTS.md
RELEASE_CHECKLIST.md
scripts/release_check.ps1
00_Orchestrator/LOCAL_RULEBOOK.md
00_Orchestrator/MEMORY_MAP.md
00_Orchestrator/SESSION_CARD.md
00_Orchestrator/Jarvis_Main_Brain/BOOT.md
00_Orchestrator/Jarvis_Main_Brain/BRAIN.md
00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md
00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md
00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md
01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md
```

## v3 브레인 제작 검증

새 브레인은 아래를 가져야 한다.

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
SOURCE_BINDINGS.md
OUTPUT_CONTRACT.md
ACCEPTANCE_TESTS.md
TASKS/PREFLIGHT_RESULT.md
TASKS/CURRENT_TASK.md
LOGS/SESSION_OPS_LOG.md
CAPSULES/CURRENT_CAPSULE.md
```

## 검증 기준

- 부팅 경로가 서로 충돌하지 않는다.
- `START_HERE.md`와 `BOOT.md` 초반 읽기 순서에 `MAP.md`가 있다.
- `FUNCTION_PACKS.md`는 고정 씨앗 목록 복사가 아니라 브레인 목적에 맞는 런타임 함수팩이다.
- `TASKS/PREFLIGHT_RESULT.md`에는 `sufficient_layer: brain`, `build_allowed: true`, `why_not_function_pack`, `why_not_engine`, `why_not_skill`, `why_not_brain_component`가 있다.
- `SOURCE_BINDINGS.md`가 있다.
- `SOURCE_BINDINGS.md` 또는 binding 문서에 `path_basis`가 있다.
- `01_Source_Pack`, `00_Orchestrator`, `02_Brains`, `scripts` 참조는 `starter_root_relative`로 표시한다.
- 새 브레인 내부 파일 참조는 `brain_root_relative`로 표시한다.
- 운용 기록과 본체 계약이 분리되어 있다.
- 원천소스 `01_Source_Pack`에 현재 작업 기록을 쓰지 않는다.

## 배포 위생 검증

- 개인 로컬 절대경로가 없다.
- 생성 캐시가 없다.
- 공개 패키지 규칙에 맞지 않는 내부 이름이 없다.
- `scripts/release_check.ps1`가 통과한다.

## 주의

구조 검증은 실제 fresh-session 부팅 검증과 다르다.
새 세션에서 실제 `부팅해` 상호작용을 재현하지 않았다면 `runtime_checked`라고 말하지 않는다.
