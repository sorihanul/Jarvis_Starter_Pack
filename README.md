# Jarvis Starter Pack

이 저장소는 두 폴더 체제로 운용한다.

## 독립 배포 원칙

이 패키지는 이 폴더 안의 파일만으로 이해되고 부팅되어야 한다.

- 특정 개인 로컬 경로를 요구하지 않는다.
- 특정 외부 문서를 다시 열어야만 작동하지 않는다.
- 외부 자료에서 얻은 아이디어는 중립적인 기능 규칙으로 다시 쓴다.
- 공개 범위를 넘는 내부 제작 기술은 포함하지 않는다.

## 먼저 여는 곳

- `00_Orchestrator/`
  - 실제로 부팅해서 쓰는 자비스 메인 브레인
  - 처음 사용하는 사람은 여기서 시작한다
  - 현재 작업, 로그, 인수인계 요약도 이 폴더 아래에서 관리한다
  - 사용자의 자연어 요청을 AILO식 의도 슬롯으로 좁혀 브레인, 스킬, 프로젝트 작업장, 소환문구로 바꾼다

## 원천소스

- `01_Source_Pack/`
  - 기존 자비스 스타터 자산 전체
  - 코어, 모듈, 프로토콜, 메모리, 스크립트, 에이전트, 스킬, 작업 문서가 들어 있다
  - 직접 작업장으로 쓰기보다 오케스트레이터가 참고하는 원천소스로 둔다

## 빠른 시작

처음이면 [QUICK_START_3_MIN.md](QUICK_START_3_MIN.md)를 먼저 봐도 된다.

1. 모델에게 이 폴더를 열게 한다.
2. "부팅해"라고 지시한다.
3. 모델은 `BOOT.md`, `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`, `00_Orchestrator/LOCAL_RULEBOOK.md`, `00_Orchestrator/MEMORY_MAP.md`, `00_Orchestrator/SESSION_CARD.md`, `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md` 기준으로 메인 브레인을 부팅한다.
4. 새 브레인이나 프로젝트가 필요하면 메인 브레인에게 만들라고 지시한다.

사용자는 옵션팩 이름을 외울 필요가 없다.
하고 싶은 일을 자연어로 말하면, 자비스가 필요한 옵션팩을 내부에서 고른다.

예:

```text
정보형 브레인 만들어줘. 부족한 건 네가 정리하고, 바로 쓸 수 있게 폴더와 소환문구까지 준비해.
```

다른 예:

```text
이 자료를 읽고 쓸 만한 구조만 뽑아줘.
전문 지식팩 하나 만들어줘.
외부 스킬을 붙여도 안전한지 봐줘.
긴 작업 내용을 다음 세션에서 이어갈 수 있게 압축해줘.
```

## 작업 기록 위치

- 현재 작업: `00_Orchestrator/TASKS/CURRENT_TASK.md`
- 세션 기록: `00_Orchestrator/LOGS/SESSION_OPS_LOG.md`
- 다음 세션 요약: `00_Orchestrator/CAPSULES/CURRENT_CAPSULE.md`

`01_Source_Pack/TASKS`, `LOGS`, `CAPSULES`는 원천소스 안의 참고 자료다.

## 검증

패키지를 고친 뒤에는 [ACCEPTANCE_TESTS.md](ACCEPTANCE_TESTS.md)를 기준으로 부팅, 원천소스 경계, 옵션팩 선택, 새 브레인 제작, 작업 적치, 공개 위생을 확인한다.

## 한 줄 원칙

사용자는 `00_Orchestrator`에서 시작하고, 자비스는 `01_Source_Pack`을 원천소스로 참고한다.
