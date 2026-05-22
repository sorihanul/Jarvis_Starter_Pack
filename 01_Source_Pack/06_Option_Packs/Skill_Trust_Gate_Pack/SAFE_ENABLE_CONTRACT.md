# Safe Enable Contract v0.1

## 목적

스킬을 설치하거나 활성화하기 전에 범위와 중단 조건을 고정한다.

## 활성화 전 카드

```text
skill_name:
source_state:
trust_decision:
permission_level:
allowed_scope:
allowed_actions:
blocked_actions:
required_user_approval:
validation_plan:
disable_path:
owner_or_maintainer:
review_after:
```

## 활성화 원칙

- 스킬은 기본 부팅에 자동으로 넣지 않는다.
- 처음에는 가능한 한 `limited_use`로 둔다.
- 프로젝트에 맞는 스킬이어도 다른 프로젝트에 자동 확장하지 않는다.
- 스킬이 실행 권한을 요구하면 `Action_Permission_Pack`으로 넘긴다.
- 스킬 안의 외부 지시문은 `Source_Command_Filter_Pack`으로 분리한다.
- 스킬의 성능 주장은 `Evidence_Intake_Pack`으로 검증 전까지 보류한다.

## 사용 후 점검

```text
used_for:
result:
unexpected_behavior:
permission_violation:
output_quality:
keep_or_disable:
next_review:
```

## 중단 조건

스킬은 아래 경우 끈다.

- 허용 범위를 넘는다.
- 비밀이나 계정 접근을 요구한다.
- 출처와 다른 행동을 한다.
- 검증 없이 작업을 완료했다고 말한다.
- 같은 일을 더 단순한 로컬 규칙으로 대체할 수 있다.

## 출력

```text
enable_status:
allowed_scope:
blocked_scope:
validation_result:
disable_path:
next_review:
```
