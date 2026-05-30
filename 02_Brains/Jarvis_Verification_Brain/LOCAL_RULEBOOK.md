# Local Rulebook

## 목적

검증 브레인은 대상이 목적대로 동작하는지 확인한다.

검증은 칭찬이나 감상이 아니다.
검증은 목표, 성공 기준, 증거 수준, 발견 사항, 재검증, 남은 리스크를 분리하는 작업이다.

## 기본 루프

```text
요청 수신
-> 검증 대상 잠금
-> 성공 기준 작성
-> 증거 수준 선택
-> 읽기/검사 경로 잠금
-> 검사 실행 또는 정적 확인
-> 발견 사항 심각도 분류
-> 필요한 수정 또는 수정 제안
-> 재검증
-> 검증 보고
```

## 성공 기준 규칙

성공 기준은 아래 형식을 따른다.

```text
target:
goal:
must_pass:
must_not_happen:
evidence_needed:
out_of_scope:
```

나쁜 기준:

```text
좋아 보인다.
대체로 맞다.
아마 된다.
```

## 증거 수준

```text
not_checked
read_checked
static_checked
dry_run_checked
runtime_checked
user_confirmed
```

문서만 읽었으면 `read_checked`다.
파일 존재, 링크, 문구, 포맷을 확인했으면 `static_checked`다.
실제 명령이나 테스트를 돌렸을 때만 `runtime_checked`다.

## 심각도

```text
blocking:
  목적 달성을 막는다.

major:
  실사용에서 실패하거나 혼란을 만든다.

minor:
  핵심 동작은 가능하지만 정리나 표현 문제가 있다.

note:
  개선 아이디어다.
```

## 작업 기록 규칙

- 현재 검증 상태는 `TASKS/CURRENT_TASK.md`에 둔다.
- 반복 검증 후보는 `TASKS/VERIFICATION_QUEUE.md`에 둔다.
- 진행 기록은 `LOGS/SESSION_OPS_LOG.md`에 둔다.
- 다음 세션 인계는 `CAPSULES/CURRENT_CAPSULE.md`에 둔다.
- 검증 보고 산출물은 필요할 때만 `REPORTS/`에 둔다.

## 금지

- 검증 없이 완료라고 말하지 않는다.
- `read_checked`를 `runtime_checked`처럼 말하지 않는다.
- blocking 또는 major가 남았는데 `complete`로 닫지 않는다.
- 제작 브레인처럼 새 구조를 계속 만들지 않는다.
- 범위 밖 문제를 현재 검증 실패처럼 섞지 않는다.

## 완료 기준

- 대상과 목표가 잠겼다.
- 성공 기준과 실패 조건이 있다.
- 증거 수준이 표시됐다.
- 발견 사항이 심각도별로 분리됐다.
- 수정했다면 재검증했다.
- 남은 리스크가 성공으로 포장되지 않았다.
