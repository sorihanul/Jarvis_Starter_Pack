# Canon Memory

## 목적

이 폴더는 사용자와의 대화에서 생긴 재사용 가능한 지식을 정리해 두는 정본 기억층이다.

대화 전체를 저장하지 않는다.
다음 세션, 다른 브레인, 새 작업에서 다시 쓸 수 있는 결정, 규칙, 사용법만 남긴다.

## 위치

```text
CANON_MEMORY/
  README.md
  FUNCTIONIZED_CANON_RULE.md
  INDEX.md
  CANDIDATES/
  WIKI/
  ROUTES/
```

## 원칙

- 기본 부팅 때 전체를 읽지 않는다.
- 대화 원문을 복사하지 않는다.
- 먼저 후보로 분리한 뒤 정본으로 올린다.
- 정본은 짧고 다시 읽기 쉬워야 한다.
- 원천소스와 세션 로그를 섞지 않는다.
- 정본 항목에는 최신성, 폐기, 충돌, 관계 메타를 남긴다.
- 새 정본이 옛 정본을 대체하면 `supersedes`와 `superseded_by`를 갱신한다.
- 정본끼리 충돌하면 `conflict_check`에 우선 기준이나 미해결 상태를 적는다.

## 흐름

```text
conversation
-> session trace
-> capsule summary
-> canon candidate
-> wiki note
-> route/index link
```

v3에서는 위 흐름을 `FUNCTIONIZED_CANON_RULE.md`의 함수팩 흐름으로 더 좁혀 다룬다.

```text
conversation_or_task_result
-> candidate_extract
-> reuse_value_check
-> confidence_label
-> conflict_check
-> promotion_gate
-> wiki_note_bind
-> route_update
-> read_report_update_if_needed
```

## 정본화 대상

- 사용자가 확정한 결정
- 반복 적용할 규칙
- 브레인 제작 기준
- 프롬프트 설계 기준
- 실패 원인과 수정 기준
- 다음에도 다시 읽을 사용법

## 정본화 금지

- 대화 원문 전체
- 순간 감정
- 한 번만 쓰는 작업 메모
- 검증되지 않은 아이디어
- 원천소스 복사본

## 라우트 원칙

정본 위키를 전부 읽지 않는다.
먼저 `INDEX.md`와 `ROUTES/INDEX.md`를 보고 현재 작업에 필요한 정본만 고른다.

`WIKI/`는 본문이고, `ROUTES/`는 언제 무엇을 읽을지 정하는 경로면이다.

정본화 절차가 필요하면 먼저 `FUNCTIONIZED_CANON_RULE.md`를 읽는다.

## 정본 메타 원칙

정본 노트는 파일 기반 정본 그래프의 노드처럼 다룬다.
링크와 관계는 거대한 DB가 아니라 아래 메타로 최소 관리한다.

```text
status: active | provisional | experimental | deprecated
confidence: high | medium | low
supersedes: none | <file>
superseded_by: none | <file>
related: []
conflict_check: clear | unresolved | prefer:<file> | see:<file>
last_reviewed: YYYY-MM-DD | unknown
```

이 필드가 없으면 노트가 늘어날수록 무엇이 최신 정본인지 알기 어려워진다.
