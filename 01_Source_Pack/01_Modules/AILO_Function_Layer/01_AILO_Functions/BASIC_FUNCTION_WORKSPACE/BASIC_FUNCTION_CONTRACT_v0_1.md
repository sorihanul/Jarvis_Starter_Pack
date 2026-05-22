# Basic Function Contract v0.1

## Identity
A basic function is a small callable control contract.

It does not perform deep meaning work.
It prepares clean control surfaces for later skills, brains, engines, or cognitive functions.

Default:

```text
A basic function controls execution shape.
It does not perform the final task unless explicitly defined.
```

## Required fields

```text
id
name
layer
status
purpose
input_slots
output_schema
failure_output
operation
guards
forbids
memory_policy
trace_policy
fixture_id
pass_if
fail_if
```

## Layer value

```text
layer:"basic_function_common_layer"
```

## Status values

```text
draft
fixture_ready
tested
stable
deprecated
```

Candidate-gate states use a longer lifecycle:

```text
raw_material
function_candidate
tested_basic_function
stable_basic_function
deprecated
```

Stable functions in the common layer should use `stable` or `tested`.

## Memory policy values

```text
none
trace_only
candidate_only
```

Default:

```text
memory_policy:"none"
```

Basic functions must not write canon memory.

## Trace policy values

```text
none
min
structured
```

Default:

```text
trace_policy:"min"
```

## Guard rule
A basic function must expose missing input instead of guessing.

Use:

```text
missing_slots
needs_user
stop_condition
```

Do not silently fill missing intent.

## Failure output rule

When a function cannot produce a valid output, it must return:

```text
failure_output{
  ok:false,
  reason:"missing_required_input | meaning_judgment_required | unstable_output | existing_function_sufficient",
  missing_slots:[],
  suggested_layer:"cognitive_function | skill | engine | basic_function_tightening"
}
```

Failure output is not an error message.
It is a routing surface for the next layer.

## Pass rule
A basic function passes only when:

```text
required fields exist
input slots are explicit
output schema is stable
missing information is exposed
memory side effects are controlled
trace shape is predictable
function does not perform cognitive interpretation
function does not perform the final task unless explicitly defined
```

## Fail rule
A basic function fails when it:

```text
adds unstated goals
judges hidden meaning
compares evidence authority
rewrites the user's intent
writes or edits final output as if it were the task executor
writes memory without policy
changes output shape without reason
requires brain-local knowledge
```
