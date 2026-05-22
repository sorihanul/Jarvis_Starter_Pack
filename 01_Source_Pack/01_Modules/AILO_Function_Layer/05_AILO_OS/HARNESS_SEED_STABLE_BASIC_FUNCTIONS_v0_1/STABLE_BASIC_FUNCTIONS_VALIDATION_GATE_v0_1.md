# Stable Basic Functions Validation Gate v0.1

## Purpose
Validate explicit execution of the seven stable AILO basic functions.

## Pass conditions

```text
function_id is present
function_id exists in the seven-function registry
required slots exist
selected_function equals function_id
output contains all fields required by the registry
trace exists
trace.memory_policy is none
final_task_executed is false
memory_written is false
```

## Fail conditions

```text
function_id missing
unknown function_id
required slot missing
output field missing
trace missing
memory write occurs
final task execution occurs
```

## Explicit selection rule

```text
selected_function = input.function_id
```

There is no smart routing in v0.1.

## One-line rule
This gate validates explicit stable-function execution, not function discovery.
