# AILO Function Definition v0.1

## Definition
An AILO function is the smallest AILO operation.

It usually handles:
- slot normalization
- missing slot detection
- route lock
- scope lock
- output schema binding
- memory policy check
- trace policy check
- permission or gate labeling

## Primary allocation
AILO functions belong mainly to the Jarvis v2 research lane.

Reason:
- they stabilize lightweight document harness operation
- they are small and low-cost
- they do not require deep cognitive engine machinery

## Function shape

```text
function_name:
purpose:
input_slots:
operation:
output_schema:
failure_output:
guards:
memory_policy:
trace_policy:
cost_class:
```

## Examples
```text
scope_lock()
route_lock()
missing_slot_detect()
output_schema_bind()
memory_policy_check()
trace_min_pack()
gate_judgment()
source_command_filter()
```

## Not this
If the operation interprets meaning, judges evidence, recovers hidden premises, or transforms a lens into an engine, it is not just an AILO function.

That belongs to AILO cognitive function or AILO engine.

## One-line rule
AILO function is slot and operation hygiene for lightweight control.
