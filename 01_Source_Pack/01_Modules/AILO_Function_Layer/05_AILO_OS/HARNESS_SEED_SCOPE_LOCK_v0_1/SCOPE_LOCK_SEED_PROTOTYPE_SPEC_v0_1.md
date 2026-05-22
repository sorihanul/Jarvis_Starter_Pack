# Scope Lock Seed Prototype Spec v0.1

## Purpose
Define the first minimal AILO OS seed prototype.

This prototype runs one stable basic function:

```text
basic_fn.scope_lock.v0.1
```

## Flow

```text
parse(input)
-> registry_lookup()
-> fixed_select()
-> run_scope_lock()
-> validate()
-> emit(result, trace)
```

## Step 1: parse

Input:

```text
{
  "run_id":"string?",
  "function_id":"basic_fn.scope_lock.v0.1?",
  "user_request":"string",
  "known_context":"string?"
}
```

Defaults:

```text
function_id:"basic_fn.scope_lock.v0.1"
known_context:null
```

Reject when:

```text
user_request is missing or empty
```

## Step 2: registry

The registry contains exactly one function:

```text
basic_fn.scope_lock.v0.1
```

Registry mismatch is a seed failure.

## Step 3: fixed select

Selection is fixed:

```text
selected_function:"basic_fn.scope_lock.v0.1"
```

No routing.
No ranking.
No fallback.

## Step 4: run_scope_lock

The runner returns only a scope-control result:

```text
bounded_scope
out_of_scope
missing_slots
stop_condition
```

It does not execute the user's final task.

## Step 5: validate

Validation passes only when:

```text
ok:true
all required output fields exist
memory_policy:"none"
trace exists
final_task_executed:false
```

Validation fails when:

```text
user_request is missing
unknown function is requested
output schema is incomplete
trace is missing
memory is written
final task is executed
```

## Step 6: emit

Every run emits:

```text
result
trace
fixture_check
```

Trace is required even when validation fails.

## Prototype status

```text
document_contract_ready:true
mock_runner_ready:true
runtime_ready:false
rust_ready:false
```

## One-line rule
The seed proves a single function can move through the harness path without becoming a smart agent or final-task executor.
