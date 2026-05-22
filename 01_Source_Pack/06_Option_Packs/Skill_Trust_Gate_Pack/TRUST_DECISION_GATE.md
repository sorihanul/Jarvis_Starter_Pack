# Trust Decision Gate v0.1

## 목적

스킬을 읽을지, 후보로 둘지, 설치할지, 활성화할지 나눈다.

## 판정

```text
read_only_review:
  파일을 읽고 구조만 분석한다.

candidate:
  유용하지만 아직 설치하거나 활성화하지 않는다.

limited_use:
  낮은 권한 범위에서 한 번만 쓴다.

approve_for_project:
  특정 프로젝트나 폴더에서만 쓴다.

approve_as_default:
  기본 사용 가능. 매우 드물게만 허용한다.

deny:
  사용하지 않는다.
```

## 판정 기준

```text
purpose_fit:
  현재 작업에 필요한가?

source_fit:
  출처와 버전을 확인했는가?

permission_fit:
  요구 권한이 목적에 비해 과하지 않은가?

scope_fit:
  사용할 폴더와 상황이 제한되어 있는가?

rollback_fit:
  되돌릴 수 있는가?

validation_fit:
  작은 검증을 할 수 있는가?

maintenance_fit:
  나중에 누가 관리하고 끌 수 있는가?
```

## 기본값

```text
unknown source:
  read_only_review

read-only utility:
  candidate 또는 limited_use

write-local utility:
  limited_use 또는 approve_for_project

shell/network/secret/automation:
  review first, then explicit approval

destructive or obfuscated:
  deny
```

## 출력

```text
skill_name:
trust_decision:
reason:
allowed_scope:
required_approval:
validation_needed:
disable_or_rollback:
next_action:
```
