# Preference Memory Pack

## 목적

사용자 기억, 취향, 금지, 반복 선호를 무제한으로 쌓지 않고 안정적으로 다룬다.

## 핵심 원칙

- 기억은 모두 같은 등급이 아니다.
- 사용자 취향은 추측보다 명시가 강하다.
- 한 번 나온 말은 후보일 뿐이다.
- 반복되거나 사용자가 고정한 항목만 안정 기억으로 둔다.
- 사용자가 잊으라고 한 것은 다시 승격하지 않는다.

## 기억 등급

```text
trace:
  작업 중 생긴 흔적. LOGS에 가깝다.

capsule:
  다음 세션에 재투입할 압축 기억. CAPSULES에 가깝다.

profile:
  사용자의 안정된 취향, 금지, 작업 방식.

canon:
  오래 남길 지식 또는 규칙.

route:
  무엇을 다시 읽을지 알려주는 접근 지도.
```

## 프로필 후보 등급

```text
candidate:
  한 번 관찰됨. 바로 적용하지 않는다.

provisional:
  반복되거나 근거가 생김. 조심해서 참고한다.

active:
  명시되었거나 충분히 안정됨. 기본값으로 적용한다.

pinned:
  사용자가 고정함. 자동 판단보다 우선한다.

forgotten:
  사용자가 버리라고 함. 다시 자동 승격하지 않는다.
```

## 예산 원칙

프로필은 길어지면 오히려 모델을 흐리게 한다.

```text
style: 적게
identity: 필요한 만큼만
tooling: 반복 작업에 필요한 만큼
veto: 강하게
goal: 현재 큰 목표만
```

## 기억 후보 트리거

아래에 걸릴 때만 기억 후보로 올린다.

```text
explicit_user_rule:
  사용자가 직접 고정한 규칙.

repeated_preference:
  여러 작업에서 반복된 선호.

repeated_failure:
  같은 실패를 막기 위해 필요한 금지.

stable_workspace_fact:
  작업 재진입에 필요한 안정된 폴더, 진입면, 권한 경계.

forget_request:
  사용자가 버리라고 한 기억.
```

## 기억하지 않는 것

- 한 번 나온 감정적 반응
- 일회성 작업 세부사항
- 출처 없는 추측
- 오래된 상태와 충돌하는 과거 판단
- 다음 작업에 다시 넣을 필요가 없는 대화 흔적

## 감사와 삭제

기억은 쌓기만 하는 것이 아니다.

```text
audit_when:
  기억이 현재 작업을 방해하거나, 충돌하거나, 너무 길어졌을 때.

forget_when:
  사용자가 삭제를 요구하거나, 더 이상 사실이 아니거나, 더 좋은 규칙으로 대체됐을 때.

demote_when:
  active였던 기억이 최근 작업에서 반복적으로 맞지 않을 때.
```

## 출력 계약

프로필을 만들 때는 아래처럼 쓴다.

```text
preference:
evidence:
state: candidate | provisional | active | pinned | forgotten
scope:
last_seen:
apply_when:
do_not_apply_when:
audit_when:
forget_rule:
```
