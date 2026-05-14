# Brain Build Protocol v0.2

## 목적

사용자가 새 브레인을 요청했을 때 메인 브레인이 따르는 제작 절차다.

목표는 사용자가 긴 명령어를 외우지 않아도, Codex에서 바로 부팅 가능한 독립 브레인 구조와 소환 문구를 만드는 것이다.

## 제작 순서

1. 사용자 요청을 목적, 사용자, 산출물, 금지로 정규화한다.
2. 직접 처리할 작업인지, 별도 브레인이 필요한 작업인지 판단한다.
3. 브레인이 직접 맡을 일과 맡지 않을 일을 나눈다.
4. 필요한 원천소스를 고른다.
5. 브레인 이름과 폴더 이름을 정한다.
6. 최소 완전체 파일 세트를 만든다.
7. 재진입 표면과 작업 적치면을 만든다.
8. 새 스레드 시작 문구를 제공한다.
9. acceptance test를 붙인다.

## 요청 기록 위치

- 새 브레인 제작 요청 초안은 `../TASKS/BRAIN_BUILD_REQUESTS`에 둔다.
- 제작 중 결정 기록은 `../LOGS/SESSION_OPS_LOG.md`에 남긴다.
- 다음 세션에 넘길 요약은 `../CAPSULES/CURRENT_CAPSULE.md`에 반영한다.
- `../../01_Source_Pack` 내부에는 제작 진행 기록을 새로 쓰지 않는다.

## 경로 기준

- `../TASKS`, `../LOGS`, `../CAPSULES`는 현재 파일이 있는 `00_Orchestrator/Jarvis_Main_Brain` 기준의 오케스트레이터 작업면이다.
- 아래 기본 구조의 `START_HERE.md`, `MAP.md`, `LOCAL_RULEBOOK.md`, `SOURCE_BINDINGS.md`, `OUTPUT_CONTRACT.md` 등은 현재 패키지 안의 기존 파일이 아니라, 새로 만들 브레인 루트 안에 생성할 파일이다.
- `../../01_Source_Pack`은 참고할 원천소스 위치이며, 새 브레인이 이 폴더를 다시 읽어야만 작동하도록 만들지 않는다.

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
  SOURCE_BINDINGS.md
  OUTPUT_CONTRACT.md
  ACCEPTANCE_TESTS.md
  TASKS/
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
- `SOURCE_BINDINGS.md`: 참고할 원천소스
- `OUTPUT_CONTRACT.md`: 답변과 산출물 형식
- `ACCEPTANCE_TESTS.md`: 제대로 작동하는지 확인할 테스트
- task current file: 현재 작업 상태
- session log file: 진행 기록
- capsule file: 다음 세션 인수인계

## 질문 정책

막히지 않으면 바로 초안을 만든다.

질문이 필요하면 한 번에 핵심만 묻는다.

## 완료 기준

- 새 브레인 폴더가 있다.
- `START_HERE.md`와 `MAP.md`가 있다.
- `LOCAL_RULEBOOK.md`, `MEMORY_MAP.md`, `SESSION_CARD.md`가 있다.
- `BOOT.md`가 바로 부팅 가능하다.
- 원천소스 참조가 명시되어 있다.
- 금지 범위가 있다.
- 작업 기록 위치가 있다.
- 테스트 문장이 있다.
- 사용자가 새 스레드에 붙일 시작 문구가 있다.

## 금지

- 사용자가 긴 전문 주문을 직접 작성해야만 작동하는 구조로 만들지 않는다.
- 원천소스를 새 브레인 내부에서 다시 읽어야만 이해되는 구조로 만들지 않는다.
- `01_Source_Pack` 내부에 새 브레인 작업 기록을 남기지 않는다.
- 모든 모듈을 복제하지 않는다.
- 브레인 제작을 설명만 하고 소환 문구를 빠뜨리지 않는다.
