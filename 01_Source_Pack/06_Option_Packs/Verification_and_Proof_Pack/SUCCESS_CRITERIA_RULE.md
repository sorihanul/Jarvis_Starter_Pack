# Success Criteria Rule v0.1

## 목적

사용자의 요청을 검증 가능한 성공 기준으로 바꾼다.

검증은 느낌으로 하지 않는다.
무엇이 되면 통과이고, 무엇이 남으면 실패인지 먼저 정한다.

## 성공 기준 형식

```text
target:
goal:
must_pass:
must_not_happen:
evidence_needed:
out_of_scope:
```

## 좋은 기준

```text
The boot path lists the required files in order.
The new option pack has a README and at least one usage example.
No public package file contains internal local paths.
The validation command reports zero missing required files.
```

## 나쁜 기준

```text
Looks good.
Feels complete.
Should be enough.
Probably works.
```

## 기준 작성 원칙

- 한 문장 목표를 먼저 쓴다.
- 통과 조건과 실패 조건을 분리한다.
- 증거가 필요한 항목을 지정한다.
- 이번 작업 범위 밖은 따로 뺀다.
- 검증할 수 없는 표현은 쓰지 않는다.

## 출력

```text
goal:
success_criteria:
failure_conditions:
evidence_needed:
out_of_scope:
```
