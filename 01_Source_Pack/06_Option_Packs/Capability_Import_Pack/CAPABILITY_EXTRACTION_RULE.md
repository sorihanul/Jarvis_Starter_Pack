# Capability Extraction Rule v0.1

## 목적

외부 시스템을 자비스가 쓸 수 있는 능력 단위로 바꾼다.

## 능력 단위

외부 시스템을 볼 때 기능명이 아니라 아래 단위로 쪼갠다.

```text
condition_input: 무엇을 입력 조건으로 받는가
memory_write: 무엇을 저장하는가
memory_read: 무엇을 다시 꺼내는가
tool_boundary: 어떤 외부 연산을 실행하는가
profile_rule: 사용자 취향과 금지를 어떻게 다루는가
guard_rule: 어떤 오염과 공격을 막는가
delegation_rule: 하위 작업자를 어떻게 제한하는가
verification_rule: 결과를 어떻게 확인하는가
stop_rule: 어디서 멈추는가
artifact_rule: 어떤 파일이나 산출물을 남기는가
preview_rule: 최종 확정 전 어떤 중간 확인면을 두는가
audit_rule: 나중에 무엇을 검토하거나 삭제할 수 있는가
```

## 자비스 변환

추출한 능력은 아래 중 하나로 바꾼다.

```text
core rule: 항상 필요한 얇은 규칙
option pack: 특정 요청에서만 켜는 능력
skill: 반복 가능한 절차
brain blueprint: 새 브레인 설계 재료
project workspace: 별도 작업장 구조
test rule: 검증 기준
```

## 거절 조건

아래 능력은 바로 흡수하지 않는다.

- 제품 UI에만 의미 있는 기능
- 특정 서비스 계정 연결에 묶인 기능
- 실행 비용이 큰 always-on 수집
- 라이선스상 직접 반입이 위험한 구현
- 자비스 기본 코어를 무겁게 만드는 기능
- always-on 기억, 수집, 실행을 기본값으로 요구하는 기능
- 검증 기준 없이 좋아 보이는 작업 습관

## 추출 후 판정

추출한 능력은 바로 채택하지 않는다.

```text
1. IMPORT_DECISION_GATE.md로 흡수 등급을 정한다.
2. candidate 이상이면 CAPABILITY_CARD_TEMPLATE.md로 카드화한다.
3. LOCAL_VALIDATION_CHECKLIST.md로 검증 가능성을 본다.
4. 검증 전에는 active 능력처럼 설명하지 않는다.
```
