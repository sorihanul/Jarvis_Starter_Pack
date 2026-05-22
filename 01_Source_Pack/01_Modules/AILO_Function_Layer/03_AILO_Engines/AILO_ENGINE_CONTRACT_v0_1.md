# AILO Engine Contract v0.1

## Identity
An AILO engine is an ordered execution design.

It may still be document-level.
It does not need runnable code to be called an engine.

But it must have stable order, input, output, guards, verification, and stop rules.

## Minimum engine contract

```text
input_contract
ordered_pipeline
intermediate_state_handoff
guarded_steps
output_contract
verification_gate
failure_conditions
stop_rule
```

## Required fields

```text
id
name
layer
status
purpose
entry_rule
input_slots
input_contract
pipeline
module_slots
intermediate_state_handoff
intermediate_outputs
output_contract
guards
forbids
verification_gate
failure_conditions
stop_rule
memory_policy
trace_policy
fixture_id
pass_if
fail_if
```

## Layer value

```text
layer:"ailo_engine"
```

## Status values

```text
candidate
draft
fixture_ready
tested
brain_local_stable
promoted_pattern
deprecated
```

## Pipeline rule
Pipeline must be ordered.

Each step must say:

```text
step_id
uses
input
output
handoff_to
fail_if
```

## Intermediate state handoff
Engines must define how step outputs move into later steps.

Each handoff should say:

```text
from_step
state_name
to_step
required
```

If no intermediate output is handed to another step, it may be a checklist or skill, not an engine.

## Verification gate
Every engine must include a verification gate.

Verification gate must check:

```text
entry condition
step order
intermediate state handoff
required outputs
forbidden outputs
failure conditions
stop rule
```

## Memory policy
Default:

```text
memory_policy:"trace_only"
```

Engines may create candidates or promotion requests.
Engines must not write global canon directly unless explicitly authorized by a higher rule.

## Trace policy
Default:

```text
trace_policy:"structured"
```

Reason:
Engines are ordered structures.
Trace must show what step ran and where failure occurred.

## Pass rule
An engine passes only when:

```text
entry_rule is explicit
pipeline order is stable
each step has input and output
intermediate_state_handoff is explicit
output_contract is explicit
verification_gate exists
failure_conditions exist
stop_rule exists
fixture exists
```

## Fail rule
An engine fails when it:

```text
has no fixed order
has no verification gate
has no stop rule
has no intermediate handoff
uses vague steps
requires hidden reasoning not exposed in module slots
expands into a whole brain
cannot produce stable output
```

## One-line rule
No order, no verification, no stop rule: not an engine.
