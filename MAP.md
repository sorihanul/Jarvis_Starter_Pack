# Jarvis Starter Pack v3 Map

## 구조

이 패키지는 운용형 에이전트가 아니라 문서형 하네스다.
호스트 모델은 이 문서 묶음을 읽고, 자기 도구와 접근 권한에 맞게 작업 방식을 구성한다.

v3는 AILO functionized edition이다.
자연어 요청을 의도 슬롯으로 정리한 뒤, 필요한 동작을 함수로 나누고 관련 동작을 함수팩으로 묶어 엔진, 스킬, 브레인 부품으로 올린다.

```text
Jarvis_Starter_Pack/
  README.md
  BOOT.md
  START_HERE.md
  MAP.md
  ACCEPTANCE_TESTS.md
  RELEASE_CHECKLIST.md
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
      AILO_FUNCTION_LAYER.md
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
      FUNCTIONIZED_CANON_RULE.md
      INDEX.md
      CANDIDATES/
      WIKI/
      ROUTES/

  01_Source_Pack/
    00_Core/
    01_Modules/
      AILO_Function_Layer/
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

## 생성 브레인 경계

배포본은 사전 제작된 `02_Brains/` 폴더를 요구하지 않는다.

새 브레인은 사용자가 요청했을 때 호스트 작업 환경에 생성되는 산출물이다.
`02_Brains/`가 존재한다면 그것은 생성 브레인 위치이지 원천소스가 아니다.

공개 패키지의 원천소스는 `01_Source_Pack`이다.
생성된 브레인은 자기 폴더 안의 `START_HERE.md`, `BOOT.md`, `MAP.md`, `LOCAL_RULEBOOK.md`, `MEMORY_MAP.md`, `SESSION_CARD.md`, `FUNCTION_PACKS.md`, `TASKS/`, `LOGS/`, `CAPSULES/`로 기본 목적과 재진입 경로를 설명해야 한다.

## 선택형 레퍼런스 서브 브레인

`02_Brains/`에는 공개 예시로 포함된 선택형 문서형 서브 브레인이 있다.
이 브레인들은 사용자가 직접 부팅하기 전까지 실행되지 않는 dormant documents다.
기본 Jarvis v3 부팅에는 포함되지 않고, 필수 구성도 아니다.
사용자는 필요한 브레인만 예시, 템플릿, 또는 직접 운용 브레인으로 사용할 수 있다.

- `02_Brains/Info_Research_Brain/`: 범용 정보조사형 브레인
- `02_Brains/Jarvis_Verification_Brain/`: 범용 검증 브레인
- `02_Brains/Ontology_Builder_Design_Brain/`: 도메인 온톨로지 브레인 생산용 설계 브레인

## 핵심 파일

- `START_HERE.md`: 새 진입 안내
- `BOOT.md`: `부팅해` 명령을 메인 브레인 부팅으로 연결하는 루트 부팅 파일
- `ACCEPTANCE_TESTS.md`: 배포 패키지가 제대로 동작하는지 보는 최소 검증표
- `RELEASE_CHECKLIST.md`: GitHub 브랜치에 올리기 전 확인할 배포 위생 체크리스트
- `02_Brains/README.md`: 선택형 레퍼런스 서브 브레인 안내
- `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`: 메인 브레인 부팅 지시
- `00_Orchestrator/LOCAL_RULEBOOK.md`: 문서형 하네스의 로컬 사용 규칙
- `00_Orchestrator/MEMORY_MAP.md`: 오케스트레이터 기억 표면 구분
- `00_Orchestrator/READ_REPORT.md`: 최신 1회 route-first 읽기 감사 표면
- `00_Orchestrator/SESSION_CARD.md`: 새 세션 재진입용 정체성 카드
- `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`: 메인 브레인의 정체성
- `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`: 자연어를 AILO식 의도 슬롯으로 정리하는 의도 제어층
- `00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md`: 의도 슬롯 다음에 함수와 함수팩으로 작업 구조를 만드는 v3 제어층
- `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`: 올라운드 모드 목록
- `00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`: 원천소스 사용 규칙
- `00_Orchestrator/TASKS/CURRENT_TASK.md`: 현재 오케스트레이터 작업 상태
- `00_Orchestrator/LOGS/SESSION_OPS_LOG.md`: 현재 사용 세션 기록
- `00_Orchestrator/CAPSULES/CURRENT_CAPSULE.md`: 다음 세션 인수인계 요약
- `00_Orchestrator/CANON_MEMORY/`: 대화에서 나온 재사용 가능한 지식을 후보와 정본으로 나누는 위키형 기억층
- `00_Orchestrator/CANON_MEMORY/FUNCTIONIZED_CANON_RULE.md`: v3에서 후보, 승격, 충돌/대체, route 갱신을 함수팩 흐름으로 다루는 규칙
- `01_Source_Pack/START_HERE.md`: 기존 스타터 자산의 원래 시작점
- `01_Source_Pack/MAP.md`: 기존 스타터 자산 지도
- `01_Source_Pack/01_Modules/AILO_Function_Layer/`: AILO 함수화 설계, 함수/함수팩 씨앗, v0.2 skill-skeleton 함수, 비-Rust 미니 하네스, 제조 proof
- `01_Source_Pack/04_Knowledge/`: 지식/검색 계층 원천소스
- `01_Source_Pack/06_Option_Packs/`: 외부 시스템 흡수, 정보 수집, 메모리/프로필, 외부자료 방어 같은 선택형 능력팩

## 읽기 순서

1. `BOOT.md`
2. `START_HERE.md`
3. `MAP.md`
4. `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`
5. `00_Orchestrator/LOCAL_RULEBOOK.md`
6. `00_Orchestrator/MEMORY_MAP.md`
7. `00_Orchestrator/SESSION_CARD.md`
8. `00_Orchestrator/TASKS/CURRENT_TASK.md`
9. `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`
10. `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
11. `00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md`
12. `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`
13. `00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md`
14. 필요할 때만 `00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`
15. 필요할 때만 `01_Source_Pack/START_HERE.md`

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
- AILO Function Layer는 기본 부팅 때 전체를 읽지 않는다. 함수팩 설계, 함수 계약, 스킬 제조, 엔진 후보 판단, 브레인 부품화가 필요할 때 `01_Source_Pack/01_Modules/AILO_Function_Layer/START_HERE.md`부터 연다.
