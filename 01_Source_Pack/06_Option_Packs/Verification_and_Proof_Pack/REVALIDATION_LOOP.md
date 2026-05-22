# Revalidation Loop v0.1

## 목적

문제를 고친 뒤 다시 확인한다.

수정은 완료가 아니다.
수정 뒤 성공 기준을 다시 통과해야 완료다.

## 루프

```text
1. goal_lock:
   목표를 한 문장으로 잠근다.

2. criteria_lock:
   성공 기준과 실패 조건을 쓴다.

3. check:
   필요한 검사를 실행한다.

4. finding:
   문제를 심각도별로 나눈다.

5. bounded_fix:
   필요한 부분만 고친다.

6. recheck:
   같은 기준으로 다시 확인한다.

7. close_or_hold:
   통과하면 닫고, 남으면 리스크로 둔다.
```

## 재검증 범위

```text
same_check:
  실패했던 검사를 다시 실행한다.

adjacent_check:
  수정 때문에 영향을 받을 수 있는 가까운 항목을 본다.

regression_check:
  기존 통과 조건이 깨지지 않았는지 본다.
```

## 중단 조건

- 실패 원인을 모르면 무작정 수정하지 않는다.
- 범위 밖 문제가 나오면 별도 리스크로 분리한다.
- 삭제나 대량 이동이 필요하면 행동 권한 규칙으로 넘긴다.
- 검증할 수 없으면 완료가 아니라 `not_verified`로 보고한다.

## 출력

```text
revalidation:
original_failure:
fix_applied:
checks_rerun:
new_result:
remaining_risk:
close_status: complete | partial | not_verified
```
