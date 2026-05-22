# Verification Report Contract v0.1

## 목적

검증 결과를 재실행 가능한 형태로 보고한다.

## 보고 형식

```text
target:
goal:
success_criteria:
proof_level:
checks_run:
findings:
fixes_applied:
revalidation:
remaining_risks:
close_status:
next_action:
```

## 보고 원칙

- 결론을 먼저 쓴다.
- 무엇을 실제로 확인했는지 적는다.
- 확인하지 못한 것은 확인하지 못했다고 적는다.
- 수정한 것과 수정하지 않은 것을 분리한다.
- 남은 리스크를 성공으로 포장하지 않는다.
- 다음 행동은 하나만 제시한다.

## close_status

```text
complete:
  성공 기준을 통과했고 blocking/major가 없다.

partial:
  핵심은 진척됐지만 major 또는 검증 공백이 남았다.

blocked:
  blocking 문제가 남았다.

not_verified:
  검증을 수행하지 못했다.
```

## 나쁜 보고

```text
대체로 좋아 보입니다.
큰 문제는 없어 보입니다.
아마 됩니다.
일단 완성입니다.
```

## 좋은 보고

```text
목표:
검사:
통과:
실패:
수정:
재검증:
남은 리스크:
```
