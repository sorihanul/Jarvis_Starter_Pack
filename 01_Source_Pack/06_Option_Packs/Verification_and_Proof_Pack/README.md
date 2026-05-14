# Verification and Proof Pack

## 목적

브레인, 프롬프트, 코드, 문서, 옵션팩이 목적대로 동작하는지 확인한다.

핵심은 좋은 평가를 쓰는 것이 아니다.
핵심은 목적, 성공 기준, 실패 조건, 재검증을 분리하는 것이다.

## 언제 켜는가

```text
사용자가 "검증해봐"라고 할 때
작동 여부가 중요할 때
브레인이나 옵션팩을 만든 뒤 닫기 전에
코드나 문서가 목적과 어긋날 수 있을 때
외부 시스템을 흡수한 뒤 실제 자비스식 능력으로 변환됐는지 봐야 할 때
```

## 기본 절차

1. 목적을 한 문장으로 다시 쓴다.
2. `SUCCESS_CRITERIA_RULE.md`로 성공 기준을 검증 가능한 문장으로 바꾼다.
3. 범위 밖 요구를 분리한다.
4. `PROOF_LEVELS.md`로 증거 강도를 표시한다.
5. `FINDING_SEVERITY_RULE.md`로 blocking, major, minor, note를 나눈다.
6. 필요한 최소 수정만 제안하거나 적용한다.
7. `REVALIDATION_LOOP.md`로 수정 뒤 다시 확인한다.
8. `VERIFICATION_REPORT_CONTRACT.md` 형식으로 닫는다.
9. 남은 리스크를 확정 결과처럼 말하지 않는다.

## 먼저 읽을 파일

```text
1. README.md
2. SUCCESS_CRITERIA_RULE.md
3. PROOF_LEVELS.md
4. FINDING_SEVERITY_RULE.md
5. REVALIDATION_LOOP.md
6. VERIFICATION_REPORT_CONTRACT.md
7. USAGE_EXAMPLE.md
```

## 심각도

```text
blocking:
  목적 달성을 막는다. 이 상태로 완료하면 안 된다.

major:
  목적은 일부 달성하지만 실사용에서 문제가 난다.

minor:
  혼동, 표현, 정리 문제다. 핵심 동작은 막지 않는다.

note:
  개선 아이디어지만 지금 성공 기준에는 필수 아님.
```

## 검증 모드

```text
prompt_validation:
  모호성, 지시 충돌, 과잉 일반화, 출력 계약을 본다.

code_validation:
  실제 동작, 테스트, 회귀, 에러 경로를 본다.

document_validation:
  진입 순서, 경계, 정본/작업층 분리, 재사용성을 본다.

system_validation:
  폴더 구조, 맵 연결, 부팅 경로, 작업 적치면을 본다.
```

## 출력 계약

```text
target:
goal:
success_criteria:
proof_level:
checks_run:
findings:
fixes_applied_or_needed:
revalidation:
remaining_risks:
close_status:
next_action:
```

## 완료 조건

- 검증 대상이 분명하다.
- 성공 기준이 분명하다.
- 발견한 문제와 처리 여부가 분리되어 있다.
- 수정했다면 재검증 기준이 있다.
- 수정하지 않았다면 왜 안 했는지 적혀 있다.
- 검증하지 못한 것은 완료라고 말하지 않는다.
- blocking 또는 major가 남으면 `complete`로 닫지 않는다.
