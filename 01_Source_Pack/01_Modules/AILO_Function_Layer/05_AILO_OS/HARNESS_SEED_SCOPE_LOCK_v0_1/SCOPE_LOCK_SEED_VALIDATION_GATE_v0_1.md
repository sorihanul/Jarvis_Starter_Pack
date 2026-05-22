# Scope Lock Seed Validation Gate v0.1

## Purpose
Define the validation gate for `ailo_os_harness_seed.scope_lock`.

## Pass conditions

```text
registry contains exactly basic_fn.scope_lock.v0.1
input has non-empty user_request
selected_function is basic_fn.scope_lock.v0.1
result.ok is true for valid input
output contains bounded_scope, out_of_scope, missing_slots, stop_condition
trace exists
trace.memory_policy is none
trace.trace_policy is min
final_task_executed is false
memory_written is false
```

## Fail conditions

```text
user_request is missing or empty
unknown function_id is requested
selected_function is not basic_fn.scope_lock.v0.1
required output field is missing
trace is missing
memory is written
final task is executed
```

## Accepted failure reasons

```text
missing_required_input
unknown_function
unstable_output
execution_forbidden
registry_invalid
validation_failed
```

## Fixture pass rule

A fixture passes only when:

```text
actual ok matches expected ok
actual validation_result matches expected validation_result
expected reason matches actual reason when reason is specified
expected output keys exist when required_output_keys is specified
expected out_of_scope item exists when out_of_scope_contains is specified
final_task_executed remains false
```

## One-line rule
The validation gate checks contract compliance, not task quality.
