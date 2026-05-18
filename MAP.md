# Jarvis Starter Pack Map

## 구조

이 패키지는 운용형 에이전트가 아니라 문서형 하네스다.
호스트 모델은 이 문서 묶음을 읽고, 자기 도구와 접근 권한에 맞게 작업 방식을 구성한다.

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
    READ_REPORT.md
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
    CANON_MEMORY/
      README.md
      INDEX.md
      CANDIDATES/
      WIKI/
      ROUTES/

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
- `ACCEPTANCE_TESTS.md`: 배포 패키지가 제대로 동작하는지 보는 최소 검증표
- `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`: 메인 브레인 부팅 지시
- `00_Orchestrator/LOCAL_RULEBOOK.md`: 문서형 하네스의 로컬 사용 규칙
- `00_Orchestrator/MEMORY_MAP.md`: 오케스트레이터 기억 표면 구분
- `00_Orchestrator/READ_REPORT.md`: 최신 1회 route-first 읽기 감사 표면
- `00_Orchestrator/SESSION_CARD.md`: 새 세션 재진입용 정체성 카드
- `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`: 메인 브레인의 정체성
- `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`: 자연어를 AILO식 의도 슬롯으로 정리하는 의도 제어층
- `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`: 올라운드 모드 목록
- `00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`: 원천소스 사용 규칙
- `00_Orchestrator/TASKS/CURRENT_TASK.md`: 현재 오케스트레이터 작업 상태
- `00_Orchestrator/LOGS/SESSION_OPS_LOG.md`: 현재 사용 세션 기록
- `00_Orchestrator/CAPSULES/CURRENT_CAPSULE.md`: 다음 세션 인수인계 요약
- `00_Orchestrator/CANON_MEMORY/`: 대화에서 나온 재사용 가능한 지식을 후보와 정본으로 나누는 위키형 기억층
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
- `00_Orchestrator/CANON_MEMORY`는 대화 원문이 아니라 반복 재사용 가능한 지식만 올리는 정본 기억층이다.
- `CANON_MEMORY`는 기본 부팅 대상이 아니다.
- `CANON_MEMORY/WIKI`를 열기 전에는 `CANON_MEMORY/INDEX.md` 또는 `CANON_MEMORY/ROUTES/INDEX.md`로 필요한 항목을 고른다.
- route/canon/source memory가 결과에 영향을 줬으면 `00_Orchestrator/READ_REPORT.md`를 최신 1회로 덮어쓴다.
- `01_Source_Pack`은 원천소스다.
- 원천소스는 참고하고, 새 작업은 별도 산출면에 둔다.
- 옵션팩은 기본 부팅 때 모두 읽지 않고, 해당 능력이 필요한 요청에서만 선택적으로 읽는다.
