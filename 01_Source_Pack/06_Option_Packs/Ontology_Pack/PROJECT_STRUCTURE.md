# Ontology Knowledge Pack Project Structure

## 목적

전문 지식팩을 만들 때 사용할 최소 폴더 구조를 정한다.

## 기본 구조

```text
<Knowledge_Pack_Name>/
  README.md
  START_HERE.md
  MAP.md
  LOCAL_RULEBOOK.md
  SOURCE_LEDGER.md
  SCHEMA/
    CARD_SCHEMA.md
    RELATION_SCHEMA.md
  CARDS/
    entities/
    concepts/
    processes/
    rules/
    claims/
    sources/
  INDEX/
    ENTITY_INDEX.md
    RELATION_INDEX.md
    QUESTION_INDEX.md
  TASKS/
    CURRENT_TASK.md
  LOGS/
    SESSION_OPS_LOG.md
  CAPSULES/
    CURRENT_CAPSULE.md
```

## 파일 역할

- `README.md`: 이 지식팩이 무엇을 다루는지 설명한다.
- `START_HERE.md`: 처음 읽는 순서를 정한다.
- `MAP.md`: 폴더와 파일의 길찾기다.
- `LOCAL_RULEBOOK.md`: 이 지식팩 안에서만 적용되는 규칙이다.
- `SOURCE_LEDGER.md`: 사용한 자료와 근거 상태를 기록한다.
- `SCHEMA/`: 카드와 관계의 규격을 둔다.
- `CARDS/`: 실제 지식 카드를 둔다.
- `INDEX/`: 빠른 회수를 위한 인덱스를 둔다.
- `TASKS/`, `LOGS`, `CAPSULES`: 작업 흔적과 재진입 표면이다.

## 축소 구조

작은 지식팩은 아래만으로 시작해도 된다.

```text
<Knowledge_Pack_Name>/
  README.md
  START_HERE.md
  MAP.md
  SOURCE_LEDGER.md
  CARDS/
  INDEX/
```

## 금지

- 원문 자료를 `CARDS/`에 그대로 쌓지 않는다.
- 인덱스를 정본처럼 쓰지 않는다.
- 출처 없는 claim을 정식 카드로 승격하지 않는다.
- 모든 도메인을 하나의 지식팩에 섞지 않는다.
