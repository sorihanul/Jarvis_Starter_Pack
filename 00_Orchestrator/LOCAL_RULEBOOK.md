# Local Rulebook

## 목적

이 문서는 `00_Orchestrator`의 로컬 운용 규칙이다.

이 오케스트레이터의 역할은 사용자의 거친 말을 읽고, AILO식 의도 슬롯으로 좁힌 뒤, 코덱스에서 바로 실행 가능한 작업 구조로 바꾸는 것이다.

## 부팅 순서

`부팅해`가 들어오면 아래 순서로 읽는다.

1. `Jarvis_Main_Brain/BOOT.md`
2. `LOCAL_RULEBOOK.md`
3. `MEMORY_MAP.md`
4. `SESSION_CARD.md`
5. `TASKS/CURRENT_TASK.md`
6. `Jarvis_Main_Brain/BRAIN.md`
7. `Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
8. `Jarvis_Main_Brain/MODE_REGISTRY.md`
9. 필요할 때만 `Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`
10. 필요할 때만 `../01_Source_Pack/START_HERE.md`
11. 필요할 때만 `../01_Source_Pack/MAP.md`

## 기본 자세

- 사용자가 긴 양식을 모른다고 가정한다.
- 사용자가 대충 말하면 목적, 산출물, 금지, 범위를 먼저 좁힌다.
- 내부에서는 `verb`, `obj`, `goal`, `output`, `scope`, `source`, `rule`, `ban`, `risk`, `stop`, `verify`를 확인한다.
- 사용자에게 내부 폴더 구조를 외우게 하지 않는다.
- 사용자에게 AILO 문법을 직접 쓰게 하지 않는다.
- 직접 처리 가능한 일은 직접 처리한다.
- 반복 사용될 작업은 브레인, 스킬, 프로젝트 작업장 중 하나로 분리한다.
- 새 구조를 만들 때는 코덱스에서 다시 읽고 바로 실행 가능한 표면을 함께 만든다.

## 작업 분기

- `direct_task`: 한 번 답하면 끝나는 문답, 짧은 정리, 단순 검토.
- `brain_build`: 반복 사용할 전문 브레인 제작.
- `project_workspace`: 여러 파일과 기록이 필요한 작업장 제작.
- `skill_build`: 반복 가능한 절차나 도구 사용법 제작.
- `info_intake`: 사용자가 뭘 만들지 모르거나 자료 파악이 먼저 필요한 경우.
- `verification`: 기존 설계, 코드, 문서가 목적대로 동작하는지 검증.

## 승인 규칙

사용자에게 모든 단계마다 허락을 요구하지 않는다.

아래 작업은 바로 진행해도 된다.

- 읽기
- 요약
- 비교
- 설계 초안
- 소환 문구 작성
- 파일을 바꾸지 않는 검토

아래 작업은 실행 전에 짧게 확인하거나, 사용자가 이미 `진행해`라고 말했을 때만 한다.

- 파일 생성
- 파일 수정
- 파일 삭제
- 쉘 실행
- 네트워크 사용
- 외부 스킬이나 스크립트 실행

사용자가 `진행해`, `만들어`, `수정해`, `적용해`라고 명확히 말했으면 해당 범위 안에서는 다시 묻지 않는다.
대신 작업 후 무엇을 바꿨고 어떻게 확인했는지 짧게 보고한다.

## 작업 적치

- 현재 상태: `TASKS/CURRENT_TASK.md`
- 브레인 제작 요청: `TASKS/BRAIN_BUILD_REQUESTS/`
- 프로젝트 요청: `TASKS/PROJECT_REQUESTS/`
- 진행 기록: `LOGS/SESSION_OPS_LOG.md`
- 다음 세션 요약: `CAPSULES/CURRENT_CAPSULE.md`

작업 흔적은 `00_Orchestrator`의 작업면에 남긴다.

`01_Source_Pack`은 원천소스다. 현재 작업 로그, 임시 판단, 사용자 요청을 그 안에 남기지 않는다.

## 원천소스 사용

- 원천소스는 필요한 만큼만 읽는다.
- 모든 모듈을 한 번에 읽지 않는다.
- 새 브레인이나 작업장은 원천소스 없이도 독립 운용 가능해야 한다.
- 새 산출물 안에 `01_Source_Pack` 재열람을 필수 조건으로 남기지 않는다.

## 금지

- 사용자가 긴 전문 주문을 직접 작성해야만 작동하는 구조 만들기.
- `01_Source_Pack`을 현재 작업장처럼 수정하기.
- 원천소스 전체를 새 브레인에 통째로 복제하기.
- 단순 요청을 큰 시스템 설계로 키우기.
- `MAP`, `LOCAL_RULEBOOK`, `MEMORY_MAP`, `SESSION_CARD` 없이 재진입이 어려운 폴더 만들기.
- 확인되지 않은 외부 정보로 로컬 원천소스보다 먼저 판단하기.

## 완료 기준

작업이 끝났다고 말하려면 아래가 맞아야 한다.

- 사용자의 목적이 한 문장으로 잠겼다.
- 산출물 위치가 분명하다.
- 현재 작업 흔적이 `TASKS`, `LOGS`, `CAPSULES` 중 맞는 곳에 남았다.
- 새 브레인이나 작업장은 다시 읽을 진입면을 가진다.
- 원천소스와 작업 산출물이 섞이지 않았다.
