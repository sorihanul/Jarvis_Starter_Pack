# START HERE

## 목적

이 문서는 자비스 스타터의 새 진입점이다.

이제 자비스 스타터는 두 폴더로 나뉜다.

- `00_Orchestrator`: 실제 부팅 브레인
- `01_Source_Pack`: 원천소스

## 처음 시작

처음 사용하는 사람은 아래 파일을 먼저 읽힌다.

0. `BOOT.md`
1. `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`
2. `00_Orchestrator/LOCAL_RULEBOOK.md`
3. `00_Orchestrator/MEMORY_MAP.md`
4. `00_Orchestrator/SESSION_CARD.md`
5. `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`
6. `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
7. `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`

그다음 이렇게 지시한다.

```text
부팅해.
```

이 저장소 루트에서 `부팅해`는 `00_Orchestrator/Jarvis_Main_Brain`을 부팅하라는 뜻이다.

사용자는 옵션팩 이름을 몰라도 된다.
필요한 일만 자연어로 말하면 메인 브레인이 직접 처리, 브레인 제작, 프로젝트 작업장, 옵션팩 선택 중 하나로 나눈다.

## 원천소스 사용

`01_Source_Pack`은 기존 자비스 스타터 자산이다.

오케스트레이터는 필요할 때만 이 원천소스를 읽는다. 사용자는 보통 이 폴더를 직접 조립하지 않는다.

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
