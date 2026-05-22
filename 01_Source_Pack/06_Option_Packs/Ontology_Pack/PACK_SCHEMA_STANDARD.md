# Ontology Knowledge Pack Schema Standard

## 목적

전문 지식을 지식팩으로 만들 때 필요한 최소 카드 규격을 정한다.

이 문서는 복잡한 온톨로지 시스템을 강제하지 않는다.
목표는 모델이 다시 읽고 쓸 수 있는 지식 구조를 만드는 것이다.

## 기본 카드

```text
id:
name:
type:
definition:
scope:
properties:
relations:
rules:
evidence:
confidence:
unknowns:
last_reviewed:
```

## type 값

```text
entity:
  독립적으로 이름 붙일 수 있는 대상.

concept:
  설명해야 이해되는 개념.

process:
  순서와 조건이 있는 흐름.

rule:
  허용, 금지, 우선순위, 중단 기준.

claim:
  참/거짓 또는 근거 수준을 따져야 하는 주장.

source:
  근거로 쓰는 자료.
```

## relation 값

```text
is_a:
part_of:
depends_on:
causes:
contradicts:
supports:
updates:
example_of:
used_for:
```

## evidence 규칙

```text
evidence:
  source_id:
  quote_or_summary:
  evidence_type: direct | indirect | inferred
  confidence: high | medium | low
```

## 금지

- 근거 없는 관계를 확정하지 않는다.
- 추론을 사실처럼 쓰지 않는다.
- 카드 수를 늘리는 것 자체를 목표로 삼지 않는다.
- 도메인 용어를 정의 없이 쓰지 않는다.

## 완료 기준

- 카드 하나만 읽어도 그 카드가 무엇인지 이해된다.
- 관계는 방향과 의미가 분명하다.
- 근거와 추론이 분리되어 있다.
- unknowns가 비어 있지 않아도 실패가 아니다.
