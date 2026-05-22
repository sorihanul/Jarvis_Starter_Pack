# Jarvis Starter Pack v3

AILO functionized edition.

이 저장소는 두 폴더 체제로 운용한다.

## 기본 관점

자비스 스타터 v3는 운용형 에이전트가 아니다.
모델이 읽고 따를 문서형 하네스다.

범용 모델은 이미 넓은 지식과 도구를 가진다. 자비스 스타터는 그 능력을 특정 목적에 맞게 유도하는 작업 제어 문서 묶음이다.

v3의 핵심 변화는 `AILO function layer`다.
사용자 자연어를 바로 큰 스킬이나 브레인으로 키우기 전에, 필요한 동작을 함수로 나누고 관련 동작을 함수팩으로 묶는다.

```text
user request
-> intent slots
-> functions
-> function packs
-> engine / skill / brain component
-> brain / project / option pack
-> verification
```

함수는 가장 작은 동작 하나다.
함수팩은 관련된 가장 작은 행동 단위 묶음이다.
함수팩 묶음은 사용 방식에 따라 엔진, 스킬, 브레인 부품이 된다.

구성은 호스트 모델과 작업 환경에 따라 달라진다.
같은 자비스 스타터라도 어떤 모델이 읽는지, 어떤 파일 접근과 도구 사용이 가능한지, 어떤 산출물이 필요한지에 따라 실제 사용 방식은 달라진다.

```text
general model:
  broad knowledge and tools

brain:
  direction, boundary, source use, output shape

jarvis:
  document harness, AILO functions, source pack, option packs, task records, reusable artifacts
```

즉 브레인은 범용 모델의 지식을 새로 주입하는 것이 아니라, 이미 가진 지식과 도구를 어디에 쓰고 어디에는 쓰지 말아야 하는지 정한다.

자비스는 그 결과가 한 번 쓰고 사라지지 않게 한다. 필요한 자료를 읽고, 불필요한 방향으로 새지 않고, 작업 흔적을 남기고, 다음 작업에서 다시 쓸 수 있게 만든다.

## 독립 배포 원칙

이 패키지는 이 폴더 안의 파일만으로 이해되고 부팅되어야 한다.

- 특정 개인 로컬 경로를 요구하지 않는다.
- 특정 외부 문서를 다시 열어야만 작동하지 않는다.
- 외부 자료에서 얻은 아이디어는 중립적인 기능 규칙으로 다시 쓴다.
- 이 패키지 안의 파일만으로 설명되고 부팅된다.

## 먼저 여는 곳

- `00_Orchestrator/`
  - 모델이 먼저 읽는 자비스 메인 하네스
  - 처음 사용하는 사람은 여기서 시작한다
  - 현재 작업, 로그, 인수인계 요약도 이 폴더 아래에서 관리한다
  - 사용자의 자연어 요청을 AILO식 의도 슬롯으로 정리해 브레인, 스킬, 프로젝트 작업장, 소환문구로 바꾼다
  - v3에서는 의도 슬롯 다음에 함수와 함수팩으로 작업 조건을 먼저 구조화한다

## 원천소스

- `01_Source_Pack/`
  - 기존 자비스 스타터 자산 전체
  - AILO 함수화 레이어
  - 코어, 모듈, 프로토콜, 메모리, 스크립트, 에이전트, 스킬, 작업 문서가 들어 있다
  - 직접 작업장으로 쓰기보다 오케스트레이터가 참고하는 원천소스로 둔다

## 빠른 시작

처음이면 [INSTALL_AND_USAGE_GUIDE.md](INSTALL_AND_USAGE_GUIDE.md) 또는 [QUICK_START_3_MIN.md](QUICK_START_3_MIN.md)를 먼저 봐도 된다.

1. 모델에게 이 폴더를 열게 한다.
2. "부팅해"라고 지시한다.
3. 모델은 `BOOT.md`, `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`, `00_Orchestrator/LOCAL_RULEBOOK.md`, `00_Orchestrator/MEMORY_MAP.md`, `00_Orchestrator/SESSION_CARD.md`, `00_Orchestrator/TASKS/CURRENT_TASK.md`, `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`, `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`, `00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md`, `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`, `00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md` 기준으로 메인 하네스를 읽는다.
4. 새 브레인이나 프로젝트가 필요하면 메인 브레인에게 만들라고 지시한다.

사용자는 옵션팩 이름을 외울 필요가 없다.
하고 싶은 일을 자연어로 말하면, 자비스가 필요한 옵션팩을 요청에 맞게 고른다.

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

패키지를 고친 뒤에는 [ACCEPTANCE_TESTS.md](ACCEPTANCE_TESTS.md)를 기준으로 부팅, 원천소스 경계, 옵션팩 선택, 새 브레인 제작, 작업 적치, 배포 위생을 확인한다.
브랜치에 올리기 전에는 [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md)로 개인 경로, 생성물, v3 함수화 정의 노출 여부를 확인한다.

## 한 줄 원칙

사용자는 `00_Orchestrator`에서 시작하고, 자비스는 AILO 함수화로 필요한 동작과 함수팩을 먼저 구조화한 뒤 `01_Source_Pack`을 원천소스로 참고하며, 호스트 모델의 넓은 능력을 목적 있는 작업 흐름으로 유도한다.
