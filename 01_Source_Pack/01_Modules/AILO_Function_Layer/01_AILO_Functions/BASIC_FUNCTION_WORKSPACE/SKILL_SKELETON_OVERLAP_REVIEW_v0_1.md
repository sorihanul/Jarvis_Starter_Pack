# Skill Skeleton Overlap Review v0.1

## Purpose
This review checks whether the v0.2 skill-skeleton basic functions duplicate the v0.1 stable basic functions.

The question is not whether names look related.
The question is whether two functions make the same control decision from the same input surface.

## Review result
```text
overlap_review:"PASS_WITH_BOUNDARY_NOTES"
duplicate_functions:0
merge_required:0
rename_required:0
tightening_required:3
tightening_applied:3
stable_candidate_blocker_closed:"overlap_review"
```

## Layer rule
```text
v0.1 stable functions
-> control the current task execution surface

v0.2 skill-skeleton functions
-> control the construction surface of a reusable skill
```

If a v0.2 function starts controlling a live task instead of shaping a skill contract, it has leaked into v0.1 territory.

## Pair review

### `input_contract_bind` vs `missing_slot_detect`
```text
input_contract_bind:
  binds what inputs a skill requires before the skill exists

missing_slot_detect:
  detects which required inputs are absent in a current call
```

Decision:
```text
duplicate:false
relation:"producer -> checker"
tightening:"input_contract_bind must not decide whether a current user call can proceed"
```

### `step_sequence_lock` vs `route_lock`
```text
step_sequence_lock:
  locks user-facing skill step order

route_lock:
  chooses the first read or execution route for the current task
```

Decision:
```text
duplicate:false
relation:"skill procedure shape vs current route"
tightening:"step_sequence_lock must not select files, folders, or read routes"
```

### `acceptance_criteria_bind` vs `output_schema_bind`
```text
acceptance_criteria_bind:
  binds pass/fail criteria for a skill

output_schema_bind:
  binds the expected output fields and format rule
```

Decision:
```text
duplicate:false
relation:"quality gate vs output shape"
tightening:"acceptance_criteria_bind may reference output fields but must not replace output_schema_bind"
```

### `fixture_contract_bind` vs `output_schema_bind`
```text
fixture_contract_bind:
  defines positive and negative fixture shape

output_schema_bind:
  defines output shape for generated artifacts
```

Decision:
```text
duplicate:false
relation:"test input/output example shape vs final output schema"
tightening:"fixture_contract_bind must remain small; it must not create a full test harness"
```

### `handoff_packet_bind` vs `output_schema_bind`
```text
handoff_packet_bind:
  binds what passes to the next stage

output_schema_bind:
  binds what the current output must look like
```

Decision:
```text
duplicate:false
relation:"stage transfer packet vs artifact output shape"
tightening:"handoff_packet_bind may use output_schema_bind but must keep next-stage fields explicit"
```

### `retry_policy_check` vs `gate_label`
```text
retry_policy_check:
  decides retry, hold, stop, or escalate after a failed attempt

gate_label:
  labels whether a requested operation can proceed
```

Decision:
```text
duplicate:false
relation:"post-failure retry control vs operation permission gate"
tightening:"retry_policy_check must not bypass gate_label when permission or safety is unclear"
```

### `cost_budget_lock` vs `route_lock`
```text
cost_budget_lock:
  sets read, token, and time budget

route_lock:
  chooses the first route and optional routes
```

Decision:
```text
duplicate:false
relation:"budget constraint vs route choice"
tightening:"cost_budget_lock may constrain route_lock but must not choose the route itself"
```

### `dependency_check` vs `missing_slot_detect`
```text
dependency_check:
  checks required prerequisites such as files, tools, policies, or source availability

missing_slot_detect:
  checks required input slots
```

Decision:
```text
duplicate:false
relation:"environment prerequisite check vs input slot check"
tightening:"dependency_check must not install, fetch, or resolve missing dependencies"
```

## Boundary locks to keep
```text
1. v0.2 functions define skill construction contracts.
2. v0.2 functions do not execute the skill.
3. v0.2 functions do not judge domain meaning.
4. v0.2 functions do not select live read routes unless route_lock is called separately.
5. v0.2 functions do not write memory.
6. v0.2 functions do not replace v0.1 functions; they compose with them.
```

## Functions requiring tighter wording
These are not duplicates, but their boundary must stay explicit.

The wording was tightened in:

```text
BASIC_FUNCTION_SKILL_SKELETON_SERIES_v0_2.md
```

```text
input_contract_bind
acceptance_criteria_bind
cost_budget_lock
```

Reason:
- `input_contract_bind` can be confused with `missing_slot_detect`
- `acceptance_criteria_bind` can be confused with `output_schema_bind`
- `cost_budget_lock` can be confused with `route_lock`

## Stable-candidate effect
This review closes the first stable promotion blocker:

```text
overlap_review:closed
```

Remaining blockers:
```text
skill_family_spread
failure_consistency
no_meaning_leak
small_surface
```

## One-line decision
The v0.2 skill-skeleton series does not duplicate the v0.1 stable functions, but three functions need explicit boundary wording to prevent future drift.
