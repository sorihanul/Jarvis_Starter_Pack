# Output Contract

## 기본 검증 보고

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

## Findings 형식

```text
- finding:
  severity:
  evidence:
  why_it_matters:
  fix_needed:
```

## Proof 형식

```text
claim:
proof_level:
evidence:
limits:
can_call_complete:
```

## Close Status

세부 판정은 `DECISION_TABLES.md`의 `stop_or_close_decision`을 따른다.

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

## 출력 규칙

- 결론을 먼저 쓴다.
- 무엇을 실제로 확인했는지 적는다.
- 확인하지 못한 것은 확인하지 못했다고 적는다.
- 남은 리스크를 성공으로 포장하지 않는다.
- 다음 행동은 하나만 제시한다.
