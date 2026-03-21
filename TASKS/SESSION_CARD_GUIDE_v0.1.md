# Session Card Guide v0.1

이 문서는 `Jarvis Starter Pack`에서 `세션 카드`를 왜 쓰는지와 어떻게 쓰는지 설명한다.

## 목적

- 같은 브레인을 쓰는 여러 세션이 서로 섞이지 않게 한다.
- 이 세션이 무엇을 위한 세션인지 먼저 고정한다.
- 읽기 범위, 쓰기 범위, 금지 범위를 세션 단위로 분명히 한다.

## 세션 카드란 무엇인가

세션 카드는 특정 세션의 얇은 정체성 문서다.

세션 카드가 답하는 질문:
- 이 세션은 무엇을 하는가
- 무엇을 읽는가
- 어디에 기록하는가
- 무엇을 건드리면 안 되는가
- 언제 닫히는가

## 세션 카드가 아닌 것

- 장기 로그가 아니다
- 캡슐 요약이 아니다
- 프로젝트 전체 헌법을 대체하지 않는다

즉:
- `Session Card` = 이 세션은 누구인가
- `LOGS` = 이 세션에서 무슨 일이 있었나
- `CAPSULES` = 이 세션에서 무엇을 남길 가치가 있나

## 언제 쓰는가

아래 중 하나면 권장:

1. 메인 세션과 프로젝트 세션을 동시에 굴릴 때
2. 같은 브레인으로 여러 작업 세션을 병행할 때
3. 프로젝트 오케스트레이션 세션을 따로 열 때
4. 코딩, 리뷰, 리서치, 글쓰기 세션이 서로 겹칠 때

짧은 단발 질의응답에는 생략 가능하다.

## 권장 세션 타입

- `main`
- `orchestration`
- `task`
- `research`
- `writing`
- `coding`
- `review`

## 최소 필드

- `session_name`
- `session_type`
- `purpose`
- `current_scope`
- `read_order`
- `write_targets`
- `do_not_touch`
- `active_rules`
- `handoff_to`
- `close_condition`

## 권장 위치

- 단발 세션: 필요 시 `TASKS/` 아래 임시로 둔다
- 프로젝트 세션: `TASKS/PROJECTS/<project_id>/` 아래 둔다
- 메인 세션: `TASKS/` 아래 유지보수 문서와 함께 둔다

## 운영 흐름

1. 세션 시작 시 세션 카드를 만든다.
2. 읽기 순서와 쓰기 범위를 먼저 적는다.
3. 작업 중 세션 역할이 바뀌면 카드를 갱신한다.
4. 세션 종료 후 카드는 남겨도 되고, 핵심만 `CAPSULES/`로 압축해도 된다.

## 주의

- 세션 카드에 장문의 실행 로그를 넣지 않는다.
- 세션 카드에 프로젝트 전체 상세 설계를 몰아넣지 않는다.
- 세션 카드는 짧고 선명해야 한다.

## 같이 읽으면 좋은 문서

- `TASKS/JARVIS_STARTER_ORCHESTRATION_METHOD_v0.1.md`
- `TASKS/SESSION_LOGGING_GUIDE_v0.1.md`
- `TASKS/SESSION_CARD_TEMPLATE_v0.1.md`
