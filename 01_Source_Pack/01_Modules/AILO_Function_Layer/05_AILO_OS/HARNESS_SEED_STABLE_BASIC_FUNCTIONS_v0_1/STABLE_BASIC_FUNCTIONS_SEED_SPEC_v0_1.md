# Stable Basic Functions Seed Spec v0.1

## Purpose
Define the minimal mock harness for all stable AILO basic functions.

## Flow

```text
parse(input)
-> registry_lookup(function_id)
-> explicit_select(function_id)
-> run_basic_function()
-> validate_output()
-> emit(result, trace)
```

## Input

```text
{
  "run_id":"string?",
  "function_id":"basic_fn.<name>.v0.1",
  "slots":{}
}
```

`function_id` is required in this expanded seed.

This prevents accidental smart routing.

## Registry

Registry contains exactly seven stable basic functions:

```text
scope_lock
route_lock
missing_slot_detect
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

## Selection

Selection is explicit:

```text
selected_function = input.function_id
```

Fail when:

```text
function_id is missing
function_id is unknown
```

## Runner boundary

Each runner performs one control operation.

It must not:

```text
execute final task
interpret hidden meaning
call cognitive function
call engine
write memory
modify files
```

## Validation

Validation checks:

```text
required slots exist
output schema matches registry
trace exists
memory_written:false
final_task_executed:false
```

## Prototype status

```text
mock_prototype_ready:true
runtime_ready:false
rust_ready:false
smart_router_ready:false
```

## One-line rule
This seed expands execution proof from one stable function to the seven stable basic functions without adding routing intelligence.
