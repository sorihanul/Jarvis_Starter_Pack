# Basic Function Acceptance Check v0.1

## Purpose
Use this check before calling a basic function `tested` or `stable`.

## Contract check

Pass only if every function has:

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

Exception:
Draft functions may omit detailed `operation`, `guards`, `forbids`, `pass_if`, and `fail_if`.

## Layer check

Pass only if:

```text
layer:"basic_function_common_layer"
```

Fail if a function requires:

```text
hidden premise recovery
evidence authority comparison
domain lens judgment
brain-local identity
engine ordering
runtime execution
```

Pass only if the function controls execution shape rather than performing the final task.

Exception:
The function may perform the final task only when that task is explicitly part of the function contract.

## Fixture check

Pass only if:

```text
fixture_id exists
input shape exists
expected output shape exists
failure output shape exists
expected output does not require hidden meaning judgment
```

## Negative fixture check

Pass only if a function refuses:

```text
scope expansion
route expansion
missing-slot guessing
schema bloat
unconfirmed memory write
heavy trace by default
unauthorized action
```

## Real-task fixture check

Pass only if a function survives real design-task inputs without:

```text
moving to cognitive function work too early
opening engine or OS routes
adding new function families
changing global surfaces
performing the actual domain task
```

## Memory check

Pass only if:

```text
memory_policy is none, trace_only, or candidate_only
canon write is not allowed
```

## Failure output check

Pass only if invalid candidates or blocked inputs return:

```text
ok:false
reason
missing_slots
suggested_layer
```

Fail if the function hides failure by expanding the function scope.

## v0.1 proof gate

The v0.1 proof passes only when these functions pass contract and fixture checks:

```text
scope_lock
route_lock
missing_slot_detect
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

## Result labels

```text
PASS
PASS_WITH_NOTES
PASS_STABLE
HOLD
FAIL
```

Use `PASS_STABLE` only when:

```text
all seven functions pass
all seven functions have failure_output
negative fixtures exist
real-task fixtures exist
stable lock exists
future growth is blocked by candidate gate
```

## One-line rule
If it judges meaning, it is not a basic function.
