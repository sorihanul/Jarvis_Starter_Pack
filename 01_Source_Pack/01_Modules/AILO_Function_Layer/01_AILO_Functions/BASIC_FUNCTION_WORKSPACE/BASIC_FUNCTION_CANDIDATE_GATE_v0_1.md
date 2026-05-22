# Basic Function Candidate Gate v0.1

## Purpose
This gate handles new basic-function ideas.

AILO can keep generating function candidates.
The common layer should not accept every candidate immediately.

## Candidate intake
When a new function idea appears, write it as:

```text
candidate_name:
source_need:
input_slots:
expected_output:
existing_function_check:
basic_or_cognitive:
promotion_condition:
status:
failure_output:
```

## Candidate lifecycle

A candidate moves through this lifecycle:

```text
raw_material
-> function_candidate
-> tested_basic_function
-> stable_basic_function
-> deprecated
```

Do not promote raw material directly into the common layer.

## Status values

```text
raw_material
function_candidate
merge_into_existing
send_to_cognitive_layer
reject
tested_basic_function
stable_basic_function
deprecated
```

## Existing function check
Before adding a new function, test whether the need can be handled by:

```text
scope_lock
missing_slot_detect
route_lock
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

If yes, do not create a new function.
Tighten the existing function instead.

Use this failure output:

```text
failure_output{
  ok:false,
  reason:"existing_function_sufficient",
  missing_slots:[],
  suggested_layer:"basic_function_tightening"
}
```

## Basic function candidate
A candidate belongs to the basic layer when it controls:

```text
scope
route
slot
schema
memory policy
trace policy
gate
stop condition
```

## Cognitive function candidate
A candidate does not belong to the basic layer when it requires:

```text
meaning judgment
hidden premise recovery
evidence authority comparison
lens selection
domain reasoning
brain-local interpretation
```

Send it to the cognitive-function expansion layer later.

Use this failure output:

```text
failure_output{
  ok:false,
  reason:"meaning_judgment_required",
  missing_slots:[],
  suggested_layer:"cognitive_function"
}
```

## Promotion condition
A candidate can be promoted only when:

```text
repeated_need:true
existing_functions_insufficient:true
input_output_stable:true
meaning_judgment_required:false
fixture_exists:true
negative_fixture_exists:true
```

## Basic failure output

When a candidate does not pass the gate, return:

```text
failure_output{
  ok:false,
  reason:"missing_required_input | meaning_judgment_required | unstable_output | existing_function_sufficient",
  missing_slots:[],
  suggested_layer:"cognitive_function | skill | engine | basic_function_tightening"
}
```

Do not hide the failure by renaming the candidate.

## Current candidate queue

```text
empty
```

## One-line rule
AILO is an infinite function source; this gate decides what becomes a common basic function.
