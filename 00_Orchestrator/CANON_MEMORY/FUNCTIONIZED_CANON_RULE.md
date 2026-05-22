# Functionized Canon Memory Rule

## 목적

v3의 Canon Memory는 대화 저장소가 아니다.
반복 재사용 가능한 지식을 함수팩 흐름으로 좁혀 후보, 정본, route, read report로 나누는 기억 표면이다.

이 문서는 새 폴더를 늘리기 위한 문서가 아니다.
`CANDIDATES/`, `WIKI/`, `INDEX.md`, `ROUTES/INDEX.md`, `READ_REPORT.md`를 v3 함수화 방식으로 쓰기 위한 규칙이다.

## 기본 흐름

```text
conversation_or_task_result
-> candidate_extract
-> reuse_value_check
-> confidence_label
-> conflict_check
-> promotion_gate
-> wiki_note_bind
-> route_update
-> read_report_update_if_needed
```

## 함수팩 관점

아래 이름은 물리 폴더가 아니라 처리 계약이다.
필요하면 같은 이름의 스킬이나 브레인 전용 함수팩으로 확장할 수 있다.

### Candidate Extract Pack

대화나 작업 결과에서 오래 남길 후보만 뽑는다.

```text
functions:
  reusable_claim_extract
  one_time_noise_filter
  source_trace_bind

output:
  candidate_note
  rejected_noise
  source_trace

stop_condition:
  no reusable decision, rule, concept, failure pattern, or how-to found
```

### Promotion Gate Pack

후보를 바로 정본으로 올리지 않고 승격 가능성을 판정한다.

```text
functions:
  repeatability_check
  confidence_label
  operator_confirmation_check
  promotion_decision

output:
  promote_to_wiki: true | false
  confidence: high | medium | low
  reason:

stop_condition:
  user did not confirm, evidence is weak, or rule is one-time only
```

### Conflict And Supersession Pack

정본끼리 충돌하거나 새 정본이 옛 정본을 대체할 때 관계를 묶는다.

```text
functions:
  conflict_check
  supersedes_bind
  superseded_by_bind
  deprecated_status_label

output:
  conflict_check: clear | unresolved | prefer:<file> | see:<file>
  supersedes:
  superseded_by:
  status:

stop_condition:
  conflict exists but no priority can be established
```

### Wiki Note Bind Pack

승격된 후보를 짧은 정본 노트로 고정한다.

```text
functions:
  metadata_bind
  one_line_bind
  rule_bind
  boundary_bind
  source_trace_bind

output:
  WIKI/<note>.md
  INDEX.md entry

stop_condition:
  metadata cannot be filled enough to avoid future confusion
```

### Route Update Pack

정본을 언제 읽고 언제 읽지 않을지 route에 연결한다.

```text
functions:
  read_when_bind
  do_not_read_when_bind
  route_index_update

output:
  ROUTES/INDEX.md entry

stop_condition:
  read condition is too vague
```

### Read Report Pack

Canon Memory나 route가 실제 결과에 영향을 줬을 때만 최신 1회 읽기 보고를 갱신한다.

```text
functions:
  route_use_trace
  opened_note_list
  skipped_note_list
  route_revision_hint

output:
  READ_REPORT.md updated

stop_condition:
  Canon Memory did not affect this task
```

## 기본 출력 계약

```text
canon_update_result:
  candidate_created:
  promoted_to_wiki:
  wiki_file:
  index_updated:
  route_updated:
  read_report_updated:
  confidence:
  conflict_check:
  supersedes:
  superseded_by:
  stop_reason:
```

## 금지

- 대화 원문 전체를 `WIKI/`로 복사하지 않는다.
- 사용자가 확정하지 않은 판단을 정본처럼 쓰지 않는다.
- `confidence`와 `conflict_check` 없이 정본을 늘리지 않는다.
- `ROUTES/INDEX.md` 없이 `WIKI/` 전체를 읽게 만들지 않는다.
- `READ_REPORT.md`를 누적 로그처럼 계속 늘리지 않는다.
- 함수팩 이름을 이유로 새 물리 폴더를 자동 생성하지 않는다.

## 한 줄 원칙

```text
Canon Memory is not stored conversation.
It is reusable knowledge passed through candidate, promotion, conflict, wiki, route, and read-report functions.
```
