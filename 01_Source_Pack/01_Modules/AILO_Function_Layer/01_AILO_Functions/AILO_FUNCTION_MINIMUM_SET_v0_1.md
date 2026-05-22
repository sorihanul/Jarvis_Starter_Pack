# AILO Function Minimum Set v0.1

## Purpose
This is the minimum function set for the first implementation proof.

The goal is not to cover every use case.
The goal is to prove the base layer.

## Active workspace
Use the stable common layer inside:

```text
BASIC_FUNCTION_WORKSPACE/
```

That folder contains the stable contract, index, function cards, fixtures, acceptance check, proof report, development log, and stable lock.

Stable lock:

```text
BASIC_FUNCTION_WORKSPACE/BASIC_FUNCTION_STABLE_LOCK_v0_1.md
```

## Minimum functions

### 1. scope_lock
Locks the current request scope.

Input:
```text
user_request
known_context?
```

Output:
```text
bounded_scope
out_of_scope
missing_slots
stop_condition
```

### 2. route_lock
Chooses the first read or first execution route.

Input:
```text
bounded_scope
available_routes
constraints?
```

Output:
```text
first_route
conditional_routes
do_not_read_by_default
stop_rule
```

### 3. missing_slot_detect
Finds missing information without guessing.

Input:
```text
input_slots
required_slots
```

Output:
```text
missing
assumed
needs_user?
```

### 4. output_schema_bind
Binds the expected output shape.

Input:
```text
task_type
output_goal
constraints?
required_fields?
forbidden_fields?
```

Output:
```text
required_fields
forbidden_fields
format_rule
pass_if
```

If `required_fields` or `forbidden_fields` are supplied, the function preserves them.
If they are not supplied, the function returns the default compact output fields.

### 5. memory_policy_check
Decides whether the result can create memory side effects.

Input:
```text
artifact_type
user_confirmed?
reuse_value?
```

Output:
```text
memory_policy
allowed_surface
forbidden_surface
promotion_required?
```

### 6. trace_policy_check
Decides trace level.

Input:
```text
task_risk
repeatability_need
debug_need
```

Output:
```text
trace_policy
trace_fields
redaction_required?
```

### 7. gate_label
Labels whether the operation can proceed.

Input:
```text
requested_action
risk
permission_state
```

Output:
```text
gate
reason
required_confirmation?
safe_next_action
```

## Shared contract
Every minimum function must include:

```text
name
purpose
input_slots
output_schema
failure_output
guards
memory_policy
trace_policy
test_fixture
```

## Exclusion
Do not include cognitive judgment here.

If a function must interpret hidden premises, compare evidence authority, or transform a lens, it belongs to the cognitive function layer.

## One-line rule
The minimum set must be boring, stable, and testable.
