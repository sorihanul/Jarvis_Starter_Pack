# Ontology Knowledge Pack Validation Template

## 목적

지식팩이 실제로 다시 읽고 쓸 수 있는 구조인지 검증한다.

## 검증 입력

```text
pack_root:
target_domain:
source_count:
card_count:
main_use_case:
```

## 1. 구조 검증

```text
required:
  README.md
  START_HERE.md
  MAP.md
  SOURCE_LEDGER.md
  CARDS/
  INDEX/
```

통과 기준:

- 처음 읽는 순서가 보인다.
- 카드 위치가 보인다.
- 출처 목록이 따로 있다.
- 작업 흔적과 정식 지식이 섞이지 않는다.

## 2. 카드 검증

샘플 카드 3개 이상을 확인한다.

```text
card_has_definition:
card_has_scope:
card_has_evidence:
card_has_confidence:
card_has_unknowns:
```

통과 기준:

- 카드 하나만 읽어도 뜻이 잡힌다.
- 관계가 과장되어 있지 않다.
- 근거와 추론이 분리되어 있다.

## 3. 관계 검증

```text
relation_has_direction:
relation_has_type:
relation_has_reason:
relation_has_evidence_or_uncertainty:
```

통과 기준:

- 관계 방향이 분명하다.
- 관계 종류가 분명하다.
- 모르는 것은 unknown으로 남긴다.

## 4. 사용성 검증

아래 질문에 답할 수 있어야 한다.

```text
이 지식팩에서 무엇을 먼저 읽는가?
어떤 질문에 답할 수 있는가?
어떤 질문에는 답하면 안 되는가?
최신성이나 근거가 약한 카드는 어디서 보이는가?
```

## 보고 형식

```text
verdict: pass | pass_with_risk | fail
blocking_issues:
major_issues:
minor_issues:
fixed:
remaining_risk:
next_action:
```
