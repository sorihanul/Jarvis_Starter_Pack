# Basic Function Development Log

## 2026-05-20

### Decision
Basic function development must stay inside one folder.

This workspace is the re-entry point for all basic function work:

```text
01_AILO_Functions/BASIC_FUNCTION_WORKSPACE/
```

### Concept lock

```text
basic function = common control layer
cognitive function = meaning expansion layer
```

### Created
- `START_HERE.md`
- `MAP.md`
- `BASIC_FUNCTION_CONTRACT_v0_1.md`
- `BASIC_FUNCTION_INDEX_v0_1.md`
- `BASIC_FUNCTION_CARDS_v0_1.md`
- `BASIC_FUNCTION_TEST_FIXTURES_v0_1.md`
- `BASIC_FUNCTION_ACCEPTANCE_CHECK_v0_1.md`

### Current target
Prove the first three functions:

```text
scope_lock
route_lock
missing_slot_detect
```

### Next step
Run the fixtures against the acceptance check and record whether the first three functions are stable enough to become the first common function set.

### Verification
First workspace check passed.

Checked:
- first three function ids exist
- first three fixture ids exist
- core contract fields exist
- workspace entry files exist

Result:

```text
BASIC_FUNCTION_WORKSPACE_CHECK=PASS
```

Current status:

```text
scope_lock: tested
route_lock: tested
missing_slot_detect: tested
output_schema_bind: tested
memory_policy_check: tested
trace_policy_check: tested
gate_label: tested
```

Proof report:

```text
BASIC_FUNCTION_PROOF_REPORT_v0_1.md
result: PASS_WITH_NOTES
```

### Status note
The v0.1 basic function common layer passed the first document-level contract check.

This is not final completion.
The next work is to make the basic functions better.

Next function-quality route:

```text
tighten function boundaries
add negative fixtures
add real-task fixtures
separate pass / hold / fail examples
check whether any function is too broad
```

### Function quality tightening
Added:
- `BASIC_FUNCTIONIZATION_PRINCIPLES_v0_1.md`
- `BASIC_FUNCTION_NEGATIVE_FIXTURES_v0_1.md`
- `BASIC_FUNCTION_REAL_TASK_FIXTURES_v0_1.md`
- `BASIC_FUNCTION_USE_ORDER_v0_1.md`
- `BASIC_FUNCTION_QUALITY_REVIEW_v0_1.md`
- `BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md`

Purpose:
- stop basic functions from expanding into cognitive functions too early
- test refusal behavior
- test real design-task behavior
- keep current work focused on function quality, not implementation runtime
- define use order without turning it into an engine
- identify quality risks before adding more functions
- keep AILO open as a function source while preventing uncontrolled promotion

### Boundary tightening after review
Added to the basic function boundary:
- candidate lifecycle: `raw_material -> function_candidate -> tested_basic_function -> stable_basic_function -> deprecated`
- required failure output shape with `ok:false`, `reason`, `missing_slots`, and `suggested_layer`
- default no-execution rule: basic functions control execution shape; they do not perform the final task unless explicitly defined
- function / skill / engine split: one move, user-facing package, ordered verified internal mechanism

Purpose:
- prevent raw AILO material from becoming stable functions too early
- make rejected candidates useful by routing them to cognitive function, skill, engine, or existing-function tightening
- stop basic functions from expanding into task execution

### Stable lock
The first seven AILO basic functions were promoted from `tested` to `stable`.

Stable lock file:

```text
BASIC_FUNCTION_STABLE_LOCK_v0_1.md
```

Final v0.1 result:

```text
PASS_STABLE
```

Meaning:
- the common basic function layer is small and locked
- all seven functions now carry `failure_output`
- positive, negative, and real-task fixtures exist
- future growth must pass the candidate gate
- direct addition of new basic functions is blocked

### Skill skeleton series v0.2
Added a tested expansion series for skill manufacturing.

Files:

```text
BASIC_FUNCTION_INDEX_v0_2.md
BASIC_FUNCTION_SKILL_SKELETON_SERIES_v0_2.md
```

Functions:

```text
input_contract_bind
step_sequence_lock
acceptance_criteria_bind
fixture_contract_bind
handoff_packet_bind
retry_policy_check
cost_budget_lock
dependency_check
```

Proof:

```text
05_AILO_OS/HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2/SKILL_SKELETON_FUNCTIONS_PROOF_REPORT_v0_2.md
result: PASS
fixtures: 16 passed, 0 failed
```

Initial status:

```text
tested_basic_function
not stable yet
```

### Skill manufacturing proof sample
Added skill manufacturing proof samples.

Location:

```text
../../06_Skill_Manufacturing_Proofs/SOURCE_REVIEW_SKILL_SAMPLE_v0_1/
../../06_Skill_Manufacturing_Proofs/PROMPT_VALIDATION_SKILL_SAMPLE_v0_1/
../../06_Skill_Manufacturing_Proofs/WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1/
```

Result:

```text
SKILL_MANUFACTURING_ALL_PROOFS_OUTPUT_v0_1.json
overall: PASS
samples: 3
passed: 3
failed: 0
```

Meaning:
- a skill skeleton can be assembled from stable v0.1 functions and tested v0.2 skill-skeleton functions
- the samples do not perform real source review, prompt validation, or wikiization
- no cognitive functions, engines, Rust, smart routing, or memory writes are involved
- at this point, v0.2 functions remained `tested_basic_function` until more real skill samples were tried

### Output contract tightening
Prompt-validation real trial exposed that `output_schema_bind` was too generic for manufactured skill cards.

Fix:

```text
output_schema_bind now preserves explicit required_fields and forbidden_fields when supplied.
```

Verification:

```text
STABLE_BASIC_FUNCTIONS_FIXTURES_v0_1.json
total: 10
passed: 10
failed: 0

STABLE_BASIC_FUNCTIONS_NEGATIVE_FIXTURES_v0_1.json
total: 7
passed: 7
failed: 0

PROMPT_VALIDATION_REAL_TRIAL_v0_1
total: 2
passed: 2
failed: 0
```

### Real-trial expansion
Added real-trial checks for all three manufactured skill samples.

```text
SOURCE_REVIEW_REAL_TRIAL_v0_1: PASS
PROMPT_VALIDATION_REAL_TRIAL_v0_1: PASS
WIKI_NOTE_INTAKE_REAL_TRIAL_v0_1: PASS
```

Additional tightening:

```text
wiki_note_intake output_contract now includes candidate_status
```

Meaning:
- the current manufactured skeletons can handle small real input packets
- this still does not prove deep domain quality
- v0.2 functions can move toward stable-candidate review, but should not be promoted without one more tightening pass

### Stable-candidate review
Added:

```text
SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md
SKILL_SKELETON_OVERLAP_REVIEW_v0_1.md
SKILL_SKELETON_FAILURE_CONSISTENCY_REVIEW_v0_1.md
```

Decision:

```text
v0.2 skill-skeleton series status: stable_candidate
stable:false
```

Reason:
- 16/16 v0.2 fixtures passed
- non-Rust mini harness `run-skill-series` passed
- 3/3 skill manufacturing samples passed
- 3/3 small real-trial checks passed
- overlap review found no duplicate v0.1/v0.2 functions
- failure consistency check passed across all eight v0.2 missing-input failure cases

Still blocked from full stable promotion:
- not enough skill-family spread
- domain meaning leakage must keep being checked
- the series must stay optional, not forced for every skill

Overlap review result:

```text
duplicate_functions:0
merge_required:0
rename_required:0
tightening_required:3
tightening_applied:3
```

Boundary notes:
- `input_contract_bind` must not become `missing_slot_detect`
- `acceptance_criteria_bind` must not become `output_schema_bind`
- `cost_budget_lock` must not become `route_lock`

Failure consistency result:

```text
failure_cases:8
passed:8
failed:0
covered_function_count:8
```
