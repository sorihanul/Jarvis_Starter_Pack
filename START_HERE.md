# START HERE

## 목적

이 문서는 자비스 스타터 v3의 진입점이다.

이제 자비스 스타터는 두 폴더로 나뉜다.

- `00_Orchestrator`: 모델이 먼저 읽는 문서형 하네스
- `01_Source_Pack`: 원천소스와 AILO 함수화 레이어

## 핵심 생각

자비스 스타터는 운용형 에이전트가 아니다.
모델이 읽고 따를 문서형 하네스다.

범용 모델은 넓은 지식과 도구를 가진다. 자비스의 브레인은 그 능력을 목적, 경계, 자료 사용, 산출물 형태로 유도한다.

어떤 모델이 읽는지에 따라 실제 구성은 달라진다.
파일 접근이 강한 모델, 웹 검색이 강한 모델, 코드 수정이 강한 모델, 긴 문서 이해가 강한 모델은 같은 하네스를 다르게 사용한다.

그래서 자비스는 아래 일을 맡는다.

- 사용자 말을 AILO식 의도 슬롯으로 정리한다.
- v3에서는 의도 슬롯을 바로 큰 작업으로 키우기 전에 필요한 동작을 함수로 나누고 관련 동작을 함수팩으로 묶는다.
- 필요한 자료를 먼저 고른다.
- 필요 없는 방향으로 새지 않게 한다.
- 작업 결과와 판단을 남긴다.
- 남긴 자료를 다음 작업에서 다시 쓰게 한다.

```text
자연어 요청
-> 의도 슬롯
-> 함수
-> 함수팩
-> 엔진 / 스킬 / 브레인 부품
-> 브레인 / 프로젝트 / 옵션팩
-> 검증
```

## 처음 시작

처음 사용하는 사람은 아래 파일을 먼저 읽힌다.

0. `BOOT.md`
1. `START_HERE.md`
2. `MAP.md`
3. `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`
4. `00_Orchestrator/LOCAL_RULEBOOK.md`
5. `00_Orchestrator/MEMORY_MAP.md`
6. `00_Orchestrator/SESSION_CARD.md`
7. `00_Orchestrator/TASKS/CURRENT_TASK.md`
8. `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`
9. `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
10. `00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md`
11. `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`
12. `00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md`
13. 필요할 때만 `00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`

그다음 이렇게 지시한다.

```text
부팅해.
```

이 저장소 루트에서 `부팅해`는 `00_Orchestrator/Jarvis_Main_Brain`의 문서형 하네스를 먼저 읽고 작업 자세를 맞추라는 뜻이다.

사용자는 옵션팩 이름을 몰라도 된다.
필요한 일만 자연어로 말하면 메인 브레인이 직접 처리, 브레인 제작, 프로젝트 작업장, 옵션팩 선택 중 하나로 나눈다.

## 원천소스 사용

`01_Source_Pack`은 기존 자비스 스타터 자산이다.

오케스트레이터는 필요할 때만 이 원천소스를 읽는다. 사용자는 보통 이 폴더를 직접 조립하지 않는다.

v3의 AILO 함수화 레이어는 아래에 있다.

```text
01_Source_Pack/01_Modules/AILO_Function_Layer/
```

이 레이어는 기본 부팅 때 전체를 읽지 않는다.
스킬 제작, 브레인 제작, 함수팩 설계, 작업 범위 잠금, 읽기 경로 잠금, 출력 계약, 기억 부작용, 추적, 권한, 재시도, 비용 예산처럼 작업 제어가 필요할 때만 연다.

## 오케스트레이터 작업면

메인 브레인은 현재 작업을 `00_Orchestrator` 아래에 기록한다.

- `00_Orchestrator/TASKS/CURRENT_TASK.md`: 현재 작업 상태
- `00_Orchestrator/LOGS/SESSION_OPS_LOG.md`: 세션 운영 기록
- `00_Orchestrator/CAPSULES/CURRENT_CAPSULE.md`: 다음 세션 인수인계

`01_Source_Pack/TASKS`, `LOGS`, `CAPSULES`는 원천소스 안의 참고면이다.

## 새 브레인 제작

새 브레인, 에이전트, 스킬, 프로젝트 작업장이 필요하면 메인 브레인에게 요청한다.

예:

```text
리서치용 브레인 하나 만들어줘.
코딩 보조 브레인 설계해줘.
내 글쓰기 스타일을 반영하는 브레인 폴더를 만들어줘.
```

메인 브레인은 `01_Source_Pack`을 참고해 새 브레인 폴더와 부팅 문구를 만든다.

배포본에 `02_Brains/` 폴더가 없어도 정상이다.
브레인 폴더는 사용자의 요청과 호스트 작업 환경에 맞춰 나중에 생성되는 산출물이다.
생성된 브레인은 원천소스를 다시 읽지 않아도 자기 목적, 부팅 순서, 함수팩, 작업 기록 위치를 자기 폴더 안에서 설명해야 한다.

짧게 말해도 된다.

```text
검증용 브레인 만들어줘. 부족한 건 네가 정리하고, 바로 쓸 수 있게 폴더와 소환문구까지 준비해.
```

전문 지식팩이 필요하면 이렇게 말하면 된다.

```text
이 주제로 전문 지식팩 만들어줘.
자료 수집, 구조화, 검증, 읽기 경로까지 네가 잡아줘.
```

## 금지

- `01_Source_Pack`을 작업 로그 저장소처럼 쓰지 않는다.
- 원천소스를 수정해 현재 작업을 해결하지 않는다.
- 새 브레인과 프로젝트 산출물은 별도 브레인 폴더나 작업 폴더에 둔다.
