# Basic Function Index v0.2

## Purpose
This index extends the v0.1 stable common layer with a tested skill-skeleton series.

The goal is not to add domain intelligence.
The goal is to make skills from reusable control functions.

## Stable common layer v0.1

| id | name | status | role |
| --- | --- | --- | --- |
| `basic_fn.scope_lock.v0.1` | `scope_lock` | `stable` | lock current task scope |
| `basic_fn.route_lock.v0.1` | `route_lock` | `stable` | choose first route and non-read surfaces |
| `basic_fn.missing_slot_detect.v0.1` | `missing_slot_detect` | `stable` | expose missing inputs without guessing |
| `basic_fn.output_schema_bind.v0.1` | `output_schema_bind` | `stable` | bind output shape |
| `basic_fn.memory_policy_check.v0.1` | `memory_policy_check` | `stable` | decide memory side-effect policy |
| `basic_fn.trace_policy_check.v0.1` | `trace_policy_check` | `stable` | decide trace shape |
| `basic_fn.gate_label.v0.1` | `gate_label` | `stable` | label proceed / hold / block |

## Skill-skeleton series v0.2

| id | name | status | role |
| --- | --- | --- | --- |
| `basic_fn.input_contract_bind.v0.2` | `input_contract_bind` | `stable_candidate` | bind required and optional inputs for a skill |
| `basic_fn.step_sequence_lock.v0.2` | `step_sequence_lock` | `stable_candidate` | lock user-facing skill step order without executing it |
| `basic_fn.acceptance_criteria_bind.v0.2` | `acceptance_criteria_bind` | `stable_candidate` | bind pass/fail criteria before work starts |
| `basic_fn.fixture_contract_bind.v0.2` | `fixture_contract_bind` | `stable_candidate` | define minimal positive and negative fixtures |
| `basic_fn.handoff_packet_bind.v0.2` | `handoff_packet_bind` | `stable_candidate` | bind what must be handed to the next stage |
| `basic_fn.retry_policy_check.v0.2` | `retry_policy_check` | `stable_candidate` | decide retry, hold, or stop policy |
| `basic_fn.cost_budget_lock.v0.2` | `cost_budget_lock` | `stable_candidate` | set read, token, and time budgets |
| `basic_fn.dependency_check.v0.2` | `dependency_check` | `stable_candidate` | check required prerequisites without resolving them |

## Why these belong to basic functions

They control:

```text
input
step shape
acceptance
fixtures
handoff
retry
budget
dependency
```

They do not judge:

```text
meaning
source authority
domain truth
hidden premise
creative quality
brain identity
```

## Stability note

The v0.2 series is `stable_candidate`, not stable.

It passed the first three skill manufacturing samples and the first three small real-trial checks.

It may become stable only after broader skill-family use shows that the functions are not overlapping, too generic, or leaking into domain meaning.

Review:

```text
SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md
SKILL_SKELETON_OVERLAP_REVIEW_v0_1.md
SKILL_SKELETON_FAILURE_CONSISTENCY_REVIEW_v0_1.md
```

Overlap review result:

```text
duplicate_functions:0
merge_required:0
failure_consistency:"PASS"
remaining_stable_blockers:["skill_family_spread","no_meaning_leak","small_surface"]
```

## One-line rule
v0.1 controls task execution shape; v0.2 controls skill skeleton construction.
