# Jarvis Starter Pack Map

## 구조

```text
Jarvis_Starter_Pack/
  README.md
  BOOT.md
  START_HERE.md
  MAP.md
  ACCEPTANCE_TESTS.md
  LICENSE

  00_Orchestrator/
    LOCAL_RULEBOOK.md
    MEMORY_MAP.md
    SESSION_CARD.md
    Jarvis_Main_Brain/
      BOOT.md
      BRAIN.md
      AILO_INTENT_LAYER.md
      MODE_REGISTRY.md
      SOURCE_USAGE_RULE.md
      BRAIN_BUILD_PROTOCOL.md
      HANDOFF_PROMPTS.md
      ACCEPTANCE_TESTS.md
    TASKS/
      CURRENT_TASK.md
      BRAIN_BUILD_REQUESTS/
      PROJECT_REQUESTS/
    LOGS/
      SESSION_OPS_LOG.md
    CAPSULES/
      CURRENT_CAPSULE.md

  01_Source_Pack/
    00_Core/
    01_Modules/
    02_Protocols/
    03_Memory/
    04_Knowledge/
    05_Scripts/
    06_Option_Packs/
    AGENTS/
    SKILLS/
    TASKS/
    CAPSULES/
    LOGS/
```

## 핵심 파일

- `START_HERE.md`: 새 진입 안내
- `BOOT.md`: `부팅해` 명령을 메인 브레인 부팅으로 연결하는 루트 부팅 파일
- `ACCEPTANCE_TESTS.md`: 공개 패키지가 제대로 동작하는지 보는 최소 검증표
- `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`: 메인 브레인 부팅 지시
- `00_Orchestrator/LOCAL_RULEBOOK.md`: 오케스트레이터 로컬 운용 규칙
- `00_Orchestrator/MEMORY_MAP.md`: 오케스트레이터 기억 표면 구분
- `00_Orchestrator/SESSION_CARD.md`: 새 세션 재진입용 정체성 카드
- `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`: 메인 브레인의 정체성
- `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`: 자연어를 AILO식 의도 슬롯으로 좁히는 내부 제어층
- `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`: 올라운드 모드 목록
- `00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`: 원천소스 사용 규칙
- `00_Orchestrator/TASKS/CURRENT_TASK.md`: 현재 오케스트레이터 작업 상태
- `00_Orchestrator/LOGS/SESSION_OPS_LOG.md`: 현재 오케스트레이터 운영 기록
- `00_Orchestrator/CAPSULES/CURRENT_CAPSULE.md`: 다음 세션 인수인계 요약
- `01_Source_Pack/START_HERE.md`: 기존 스타터 자산의 원래 시작점
- `01_Source_Pack/MAP.md`: 기존 스타터 자산 지도
- `01_Source_Pack/04_Knowledge/`: 지식/검색 계층 원천소스
- `01_Source_Pack/06_Option_Packs/`: 외부 시스템 흡수, 정보 수집, 메모리/프로필, 외부자료 방어 같은 선택형 능력팩

## 읽기 순서

1. `BOOT.md`
2. `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`
3. `00_Orchestrator/LOCAL_RULEBOOK.md`
4. `00_Orchestrator/MEMORY_MAP.md`
5. `00_Orchestrator/SESSION_CARD.md`
6. `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`
7. `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
8. 필요할 때만 `01_Source_Pack/START_HERE.md`

## 경계

- `00_Orchestrator`는 부팅과 설계의 실행면이다.
- `00_Orchestrator/TASKS`, `LOGS`, `CAPSULES`는 현재 오케스트레이터 작업면이다.
- `01_Source_Pack`은 원천소스다.
- 원천소스는 참고하고, 새 작업은 별도 산출면에 둔다.
- 옵션팩은 기본 부팅 때 모두 읽지 않고, 해당 능력이 필요한 요청에서만 선택적으로 읽는다.
