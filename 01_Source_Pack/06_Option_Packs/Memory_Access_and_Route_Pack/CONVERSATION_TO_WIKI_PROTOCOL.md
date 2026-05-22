# Conversation to Wiki Protocol

## 목적

사용자와의 대화에서 다음에도 재사용할 수 있는 지식을 Canon Memory 후보로 분리한다.

대화 전체를 저장하지 않는다.
대화에서 생긴 결정, 규칙, 사용법, 실패 기준만 정리한다.

## 켜는 조건

```text
사용자가 "위키화해둬", "다음에도 쓰자", "이건 기억해", "정본으로 남겨"라고 말한다.
같은 규칙이나 결정이 반복된다.
브레인 제작, 프롬프트 제작, 작업 방식에 계속 재사용될 기준이 생긴다.
세션 캡슐에 남긴 내용 중 장기 재사용 가치가 있다.
```

## 제외

```text
대화 원문 전체
순간 감정
한 번만 쓰는 임시 작업
아직 확인 안 된 아이디어
원천소스 복사본
```

## 절차

```text
1. 대화에서 재사용 가능한 단위만 고른다.
2. decision / rule / how_to / failure_pattern / glossary / concept 중 하나로 분류한다.
3. 불확실하면 WIKI가 아니라 CANDIDATES에 둔다.
4. 후보에는 promotion_condition을 적는다.
5. 확정 가능한 것만 WIKI로 올린다.
6. WIKI로 올리면 INDEX에 짧은 연결을 남긴다.
7. 읽기 조건이 필요한 경우 ROUTES/INDEX에도 연결한다.
```

## 후보 산출물

```text
target: 00_Orchestrator/CANON_MEMORY/CANDIDATES/

fields:
  title:
  candidate_type:
  content:
  source_trace:
  promotion_condition:
  risk:
```

## 정본 산출물

```text
target: 00_Orchestrator/CANON_MEMORY/WIKI/

fields:
  title:
  one_line:
  when_to_use:
  rule:
  boundary:
  source_trace:
```

## 라우트 산출물

```text
target: 00_Orchestrator/CANON_MEMORY/ROUTES/INDEX.md

fields:
  title:
  file:
  read_when:
  do_not_read_when:
  scope:
  last_reviewed:
```

## 검증

- 대화 원문을 붙여넣지 않았는가?
- 후보와 정본을 구분했는가?
- 다음 모델이 이 노트만 읽어도 쓸 수 있는가?
- 출처 단서는 짧게 남겼는가?
- 기본 부팅을 무겁게 만들지 않았는가?
- WIKI 전체를 읽지 않고 INDEX/ROUTES로 필요한 항목을 고르게 했는가?
- 필요한 route/canon memory를 열었다면 READ_REPORT에 실제 읽은 경로를 남겼는가?
