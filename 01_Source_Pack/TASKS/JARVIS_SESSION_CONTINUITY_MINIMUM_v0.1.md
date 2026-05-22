# Jarvis Session Continuity Minimum v0.1

## 목적

- 세션에 다시 복귀하는 속도가 느려질 만큼 파일이 늘어나기 전에, 무엇을 남기고 무엇을 분리할지 정하는 최소 기준을 적는다.

## 한 줄 원칙

- 세션을 다시 이어갈 때 필요한 표면은 적게 두고, 기록이 늘어나면 `TASKS`, `LOGS`, `CAPSULES`, `프로젝트 작업장`으로 나눈다.

## `SESSION_CARD` 표면 규칙

- 이 문서에서 `SESSION_CARD`는 실제 세션 카드 문서를 뜻한다.
- 기본 위치는 `TASKS/` 아래다.
- 프로젝트 세션이면 `TASKS/PROJECTS/<project_id>/` 아래에 둔다.
- 새 카드를 만들거나 갱신할 때는 `TASKS/SESSION_CARD_TEMPLATE_v0.1.md`를 기준으로 한다.

## 최소 권장 표면

### 1. `SESSION_CARD` (권장)
- 지금 어떤 세션을 운용하는가
- 지금 이 세션을 왜 유지하는가
- 실제 세션 카드 파일 위치가 어디인가

### 2. 현재 안건이 적힌 `TASKS/` 문서
- 지금 실제로 처리하는 작업은 무엇인가
- 다음 행동이 무엇인가

### 3. 현재 안건과 직접 연결된 `LOGS/` 문서
- 최근에 실행한 행동을 짧게 기록한다
- 실패, 경고, 검증 결과 원본은 여기에 둔다

### 4. 관련 `CAPSULES/` 문서 (선택)
- 다음 세션이 먼저 읽어야 할 짧은 압축본
- 이미 끝난 판단 중 다시 써야 할 결론

### 5. `TASKS/PROJECTS/<project_id>/` 작업장 (선택)
- 프로젝트 세션에서만 운용한다
- `BOOT_ENTRY`, `MISSION`, `ROADMAP`, `ORCHESTRATOR`를 기준으로 진행한다

## 세션 카드와의 관계

- `SESSION_CARD`는 정체성 카드다.
- `TASKS`의 현재 안건 문서를 대체하지 않는다.
- `LOGS`나 `CAPSULES`도 대체하지 않는다.
- 판단 순서를 바로 설명하기 어려우면 `TASKS/JARVIS_CONTEXT_REALIGNMENT_NOTE_v0.1.md`를 별도로 읽는다.
- 세션 카드가 없으면 `TASKS/SESSION_CARD_TEMPLATE_v0.1.md` 기준으로 먼저 만든다.

즉:
- `SESSION_CARD` = 이 세션은 누구인가
- `TASKS`의 현재 안건 문서 = 지금 무엇을 처리하나
- `LOGS` = 최근 어떤 행동을 실행했나
- `CAPSULES` = 무엇을 압축해 남기나
- `JARVIS_CONTEXT_REALIGNMENT_NOTE` = 판단 순서를 바로 설명하기 어려울 때 무엇부터 다시 확인하나

## 언제 표면을 더 나누나

- 현재 안건 문서가 길어져 실행 계획과 참고 메모가 섞일 때 -> `LOGS/`로 분리
- 원시 기록이 길어져 다시 읽기 어려울 때 -> `CAPSULES/`로 압축
- 작업이 프로젝트 단위로 커질 때 -> `TASKS/PROJECTS/<project_id>/`
- 여러 세션이 병행되어 정체성이 자주 섞일 때 -> `SESSION_CARD`

## 경고

- live 안건 문서를 기록 보관소처럼 쓰지 않는다
- `LOGS`에 최종 결론까지 전부 몰아넣지 않는다
- `CAPSULES`를 현재 작업 보드처럼 쓰지 않는다
- 프로젝트 내용은 `TASKS/PROJECTS/` 작업장 밖으로 흩어 놓지 않는다
