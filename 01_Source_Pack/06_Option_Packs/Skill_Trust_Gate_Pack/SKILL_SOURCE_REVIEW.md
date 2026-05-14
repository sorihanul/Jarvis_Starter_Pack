# Skill Source Review v0.1

## 목적

외부 스킬이나 플러그인의 설명을 그대로 믿지 않는다.

먼저 출처, 파일 구성, 실제 요구 권한, 유지 가능성을 본다.

## 확인 항목

```text
source_label:
source_type: local_file | public_package | user_provided | generated | unknown
license:
maintainer_visible:
version_or_date:
entry_files:
claimed_purpose:
actual_surfaces:
```

## 출처 상태

```text
known:
  출처와 버전이 확인된다.

local:
  사용자가 직접 제공한 로컬 파일이다.

generated:
  현재 세션에서 만든 스킬이다.

unknown:
  출처나 버전이 불분명하다.

untrusted:
  출처가 위험하거나 숨겨진 실행을 요구한다.
```

## 점검 기준

- 설명보다 실제 파일과 권한을 우선한다.
- 설치 안내보다 실행 진입점을 먼저 본다.
- 난독화된 코드나 숨은 다운로드가 있으면 위험으로 본다.
- 출처가 유명해도 권한 검사를 생략하지 않는다.
- 현재 작업에 필요 없는 스킬은 설치하지 않는다.

## 출력

```text
skill_name:
source_state:
source_limits:
entry_points:
requires_deeper_review: yes | no
reason:
```
