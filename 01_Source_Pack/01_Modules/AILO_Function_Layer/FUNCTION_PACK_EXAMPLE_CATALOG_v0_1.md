# Function Pack Example Catalog v0.1

## Purpose

This file gives practical function pack examples for Jarvis Starter Pack v3.

The examples are not a fixed function list.
They show how a model can group small AILO functions into reusable action units.

## Rule

```text
Function
-> one smallest action

Function Pack
-> related smallest action-unit group

Function Pack Group
-> may become engine, skill, or brain component depending on use
```

## Pack 1. Goal and Scope Pack

Use when the request is vague, too broad, or likely to expand.

```text
goal_lock
scope_lock
success_criteria_bind
out_of_scope_mark
```

Expected output:

```text
goal:
bounded_scope:
success_criteria:
out_of_scope:
missing_slots:
```

Do not use for final writing, coding, or research execution.
This pack only makes the work target smaller and testable.

## Pack 2. Read Route Pack

Use when the model must decide what to read first and what not to read.

```text
route_lock
source_candidate_select
do_not_read_mark
stop_condition_define
```

Expected output:

```text
first_read:
second_read:
do_not_read_by_default:
stop_when:
route_risk:
```

Do not use as a wiki, memory store, or search engine.
This pack only chooses the reading path.

## Pack 3. Output Contract Pack

Use when the answer shape matters.

```text
output_schema_bind
section_shape_lock
length_budget_lock
final_report_shape
```

Expected output:

```text
output_type:
required_sections:
forbidden_sections:
length_budget:
completion_shape:
```

Do not use to decide truth or meaning.
This pack only fixes what the result should look like.

## Pack 4. Evidence and Uncertainty Pack

Use when claims, sources, and uncertain points must be separated.

```text
claim_extract
evidence_check
uncertainty_split
next_check_bind
```

Expected output:

```text
claims:
evidence:
uncertainty:
unsupported_points:
next_check:
```

Do not use as a full research engine.
If source ranking, contradiction mapping, and synthesis order are required, promote the pack group to an engine.

## Pack 5. Permission and Stop Pack

Use when a task may touch files, run commands, browse the web, or change state.

```text
permission_gate
side_effect_label
risk_label
stop_condition_define
```

Expected output:

```text
allowed_actions:
hold_actions:
risk:
stop_condition:
needs_user_approval:
```

Do not use to bypass safety or permission rules.
This pack exists to prevent hidden execution.

## Pack 6. Skill Skeleton Pack

Use when a repeated user-facing procedure should be drafted.

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

Expected output:

```text
skill_name:
input_contract:
steps:
acceptance_criteria:
fixtures:
handoff_packet:
retry_policy:
cost_budget:
dependencies:
```

This pack can draft a skill skeleton.
It is not the final skill until the user-facing procedure, examples, and validation are added.

## Quick Selection

```text
vague request
-> Goal and Scope Pack

too many files
-> Read Route Pack

format-sensitive output
-> Output Contract Pack

claim/source uncertainty
-> Evidence and Uncertainty Pack

file write / command / web / state change
-> Permission and Stop Pack

repeatable procedure
-> Skill Skeleton Pack
```

## One-line Rule

Start from the smallest pack that controls the current failure risk; do not open a larger engine, skill, or brain component unless the pack is no longer enough.
