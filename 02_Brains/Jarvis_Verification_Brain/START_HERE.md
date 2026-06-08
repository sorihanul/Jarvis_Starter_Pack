# START HERE

## 목적

이 폴더는 범용 검증 브레인이다.

브레인, 문서, 옵션팩, 코드, 작업 결과가 목적대로 동작하는지 확인한다.
핵심은 좋은 평가를 쓰는 것이 아니라, 목적, 성공 기준, 증거 수준, 발견 사항, 재검증 여부를 분리하는 것이다.

## 먼저 읽을 파일

1. `BOOT.md`
2. `MAP.md`
3. `LOCAL_RULEBOOK.md`
4. `MEMORY_MAP.md`
5. `RUNTIME_BOUNDARY.md`
6. `SESSION_CARD.md`
7. `BRAIN.md`
8. `MODE_REGISTRY.md`
9. `FUNCTION_PACKS.md`
10. `DECISION_TABLES.md`
11. `SOURCE_BINDINGS.md`
12. `JARVIS_STARTER_BINDING.md`
13. `OUTPUT_CONTRACT.md`
14. `TASKS/PREFLIGHT_RESULT.md`
15. `TASKS/CURRENT_TASK.md`

## 기본 사용법

```text
이 브레인 검증해줘.
이 문서가 목적대로 동작하는지 봐줘.
이 옵션팩 연결이 맞는지 검증해줘.
이 코드 변경이 성공 기준을 통과하는지 봐줘.
Jarvis Starter Pack 배포 위생 점검해줘.
```

## 기본 출력

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

## 완료 기준

- 검증 대상이 분명하다.
- 성공 기준과 실패 조건이 분리됐다.
- 증거 수준이 과장되지 않았다.
- blocking/major/minor/note가 구분됐다.
- 수정했다면 재검증을 했다.
- 검증하지 못한 것은 `not_verified`로 남겼다.

- 완료/검증/공개 가능/경계 판단 전에는 필요할 때만 `CONTEXT_REHYDRATION_BINDING.md`를 읽는다.
