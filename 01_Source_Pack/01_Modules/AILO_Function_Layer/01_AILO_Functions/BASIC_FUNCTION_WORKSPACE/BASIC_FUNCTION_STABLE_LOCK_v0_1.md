# Basic Function Stable Lock v0.1

## Purpose
This document locks the v0.1 AILO basic function common layer.

It marks the first seven basic functions as stable document-level contracts.

## Stable function set

```text
scope_lock
missing_slot_detect
route_lock
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

## What stable means

Stable means:

```text
contract exists
function card exists
positive fixture exists
negative fixture exists
real-task fixture exists
failure_output exists
acceptance check exists
proof report exists
no cognitive interpretation is required
no final task execution is allowed by default
memory side effects are controlled
trace shape is explicit
```

Stable does not mean:

```text
runtime implemented
Rust runner complete
no future revision possible
more functions should be added
```

## Layer boundary

```text
basic function
-> controls execution shape

cognitive function
-> interprets meaning surface

skill
-> packages several moves for user-facing work

engine
-> orders several moves with verification gates

OS harness
-> runs, traces, validates, governs, and preserves state
```

## Growth rule

Do not add a new basic function directly.

New function ideas must pass:

```text
BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md
```

Promote only when:

```text
repeated_need:true
control_facing:true
input_output_stable:true
existing_functions_insufficient:true
meaning_judgment_required:false
fixtures_exist:true
```

## Default use order

```text
scope_lock
missing_slot_detect
route_lock
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

For small tasks:

```text
scope_lock
missing_slot_detect
gate_label
```

## Use in next layers

The stable basic function layer may now support:

```text
cognitive function expansion
AILO engine design
AILO OS harness seed
Jarvis v2 public/basic function subset
```

But the basic layer itself stays small.

## One-line rule
The AILO basic function v0.1 layer is locked as a small stable control layer; future growth goes through candidate-gated proof, not direct expansion.
