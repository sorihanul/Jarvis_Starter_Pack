# Basic Function Proof Report v0.1

## Result

```text
PASS_STABLE
```

The v0.1 basic function set passes the stable document-level contract check.

This means the first seven functions are stable enough to be used as the common basic function layer.

It does not mean no future revision is possible.
It means new functions should not be added directly; future changes must go through the candidate gate.

## Tested function set

| function | fixture | result |
| --- | --- | --- |
| `scope_lock` | `fixture.scope_lock.001` | `PASS` |
| `route_lock` | `fixture.route_lock.001` | `PASS` |
| `missing_slot_detect` | `fixture.missing_slot_detect.001` | `PASS` |
| `output_schema_bind` | `fixture.output_schema_bind.001` | `PASS` |
| `memory_policy_check` | `fixture.memory_policy_check.001` | `PASS` |
| `trace_policy_check` | `fixture.trace_policy_check.001` | `PASS` |
| `gate_label` | `fixture.gate_label.001` | `PASS` |

## Stable function set

```text
scope_lock: stable
route_lock: stable
missing_slot_detect: stable
output_schema_bind: stable
memory_policy_check: stable
trace_policy_check: stable
gate_label: stable
```

## Contract check

Passed:

```text
id
name
layer
status
purpose
input_slots
output_schema
operation
guards
forbids
memory_policy
trace_policy
fixture_id
pass_if
fail_if
failure_output
```

## Boundary check

Passed.

No function requires:

```text
hidden premise recovery
evidence authority comparison
domain lens judgment
brain-local identity
engine ordering
execution layer
```

## Memory check

Passed.

All functions keep memory side effects inside basic policy values:

```text
none
trace_only
candidate_only
```

No function can write canon memory.

## Trace check

Passed.

Trace policy stays in:

```text
none
min
structured
```

## Remaining risk

The remaining risks are operational, not contract-blocking:

```text
LLM may over-interpret a basic function as a cognitive function
users may ask for final task execution while a basic function should only control execution shape
future function candidates may duplicate existing functions
fixtures still need runtime-level tests if a real runner is built
```

## Next step

Use this set as the stable common function layer.

```text
basic function common layer
-> cognitive function expansion
or
-> harness seed implementation
```

Do not add new basic functions unless the candidate gate proves existing functions are insufficient.
