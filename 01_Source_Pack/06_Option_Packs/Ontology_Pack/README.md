# Ontology Pack

## 목적

자료를 객체, 속성, 관계, 사건, 규칙, 근거로 나눠 설계 가능한 구조로 바꾼다.

핵심은 어려운 온톨로지 용어를 늘리는 것이 아니다.
핵심은 섞여 있는 정보를 모델이 다시 쓸 수 있는 구조로 쪼개는 것이다.

## 언제 켜는가

```text
사용자가 "체계화해봐"라고 할 때
개념 관계가 복잡할 때
자료를 브레인, 스킬, 위키, 지식팩으로 바꿔야 할 때
인물, 도구, 규칙, 사건, 근거가 뒤섞여 있을 때
정보 수집 결과를 설계 재료로 바꿔야 할 때
```

## 기본 슬롯

```text
entity:
property:
relation:
event:
action:
control_rule:
evidence:
uncertainty:
scope:
```

## 구분 규칙

```text
entity:
  독립적으로 이름 붙일 수 있는 대상.

property:
  entity가 가진 성질이나 상태.

relation:
  entity와 entity 사이의 연결.

event:
  시간 속에서 발생한 일.

action:
  누군가 하거나 시스템이 실행하는 동작.

control_rule:
  허용, 금지, 우선순위, 중단 기준.

evidence:
  이 판단을 뒷받침하는 출처나 관찰.
```

## 금지

- 모든 문장을 억지로 객체화하지 않는다.
- 근거 없는 관계를 확정하지 않는다.
- 추론 관계와 사실 관계를 섞지 않는다.
- 도메인 전문 용어를 설명 없이 사용하지 않는다.
- 그래프를 만드는 것이 목적이 아니라 재사용 가능한 구조를 만드는 것이 목적이다.

## 출력 계약

```text
ontology_scope:
entities:
properties:
relations:
events:
actions:
control_rules:
evidence:
unknowns:
next_design_use:
```

## 지식팩 제작에 같이 읽을 파일

- `PACK_SCHEMA_STANDARD.md`: 지식팩 안에 들어갈 객체/관계/근거 카드 규격
- `PROJECT_STRUCTURE.md`: 지식팩 폴더 구조
- `VALIDATION_TEMPLATE.md`: 지식팩 검증 기준
