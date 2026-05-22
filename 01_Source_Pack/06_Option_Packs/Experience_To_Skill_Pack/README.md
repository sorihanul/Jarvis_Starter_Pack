# Experience To Skill Pack

## 목적

반복 작업, 반복 실패, 반복 우회를 스킬 후보로 바꾼다.

핵심은 자동으로 아무 스킬이나 만드는 것이 아니다.
핵심은 실제 반복 근거가 있는 작업만 작은 절차로 고정하는 것이다.

## 언제 켜는가

```text
같은 작업을 여러 번 반복할 때
같은 실패가 반복될 때
사용자가 "이건 매번 하는 일이다"라고 말할 때
작업 로그에서 같은 절차가 계속 보일 때
브레인이나 프로젝트가 같은 수동 절차에 막힐 때
```

## 스킬 후보 조건

아래 중 둘 이상이 있어야 한다.

```text
repeated_task:
  같은 목적의 작업이 반복된다.

stable_steps:
  절차가 매번 크게 달라지지 않는다.

clear_input:
  입력값이 무엇인지 말할 수 있다.

clear_output:
  산출물이 무엇인지 말할 수 있다.

failure_pattern:
  반복되는 실패나 누락이 있다.

verification_possible:
  결과를 확인할 방법이 있다.
```

## 후보 상태

```text
candidate:
  반복 가능성이 보이는 상태.

draft_skill:
  README와 입력/출력/중단 기준이 생긴 상태.

tested_skill:
  실제 작업 1회 이상에서 통과한 상태.

active_skill:
  사용자가 쓰기로 승인한 상태.

retired_skill:
  더 이상 쓰지 않거나 더 좋은 방식으로 대체된 상태.
```

## 스킬화 절차

```text
1. 반복 근거를 모은다.
2. 입력과 출력이 일정한지 본다.
3. 실패 조건과 중단 조건을 쓴다.
4. 작은 절차로 만든다.
5. 실제 작업 1회 이상에서 시험한다.
6. 검증 기록이 생긴 뒤에만 active 후보로 올린다.
```

## 스킬 파일의 최소 구성

```text
name:
purpose:
when_to_use:
input:
steps:
output:
stop_rule:
validation:
risk:
do_not_use_when:
```

## active 기준

스킬은 아래를 만족해야 active가 될 수 있다.

- 입력 조건이 분명하다.
- 출력물이 검증 가능하다.
- 실패하거나 멈출 조건이 있다.
- 위험 권한이 있으면 승인 규칙이 있다.
- 기존 코어 규칙을 덮어쓰지 않는다.

## 금지

- 한 번 쓴 절차를 바로 스킬로 만들지 않는다.
- 스킬을 만들었다고 자동으로 기본 부팅에 넣지 않는다.
- 스킬이 코어 규칙을 수정하게 하지 않는다.
- 검증 기준 없는 스킬을 active로 두지 않는다.
- 사용자의 명시 승인 없이 위험 권한 스킬을 활성화하지 않는다.

## 출력 계약

```text
skill_candidate:
evidence:
input:
steps:
output:
stop_rule:
validation:
risk:
status: candidate | draft_skill | tested_skill | active_skill | retired_skill
next_action:
```
