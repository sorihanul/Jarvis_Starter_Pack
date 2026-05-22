# AILO Engine Definition v0.1

## Definition
An AILO engine is an ordered, guarded, and verified structure built from functions, cognitive functions, skills, or modules.

It exists when order matters.

In short:

```text
function
-> one bounded operation

cognitive function
-> one bounded meaning operation

engine
-> ordered process with verification and stop rule
```

A user calls a skill.
A system runs an engine.

## Primary allocation
AILO engines belong mainly to the brain-local engine lane.

Reason:
- engines need input, order, guards, output contract, verification, and failure conditions
- they are heavier than simple v2 functions
- they are used to attach specialized capability to a brain

## Engine shape

```text
id:
name:
layer:
status:
purpose:
entry_rule:
input_slots:
input_contract:
pipeline:
module_slots:
intermediate_state_handoff:
intermediate_outputs:
output_contract:
guards:
forbids:
verification_gate:
failure_conditions:
stop_rule:
memory_policy:
trace_policy:
fixture_id:
pass_if:
fail_if:
```

## Examples
```text
Intent Slot Extraction Engine
Route Cost Control Engine
Document Role / Read Order Engine
Cognition to Engine Compiler
GGS Deep Cause Lens Engine
Paper to Engine Preprocessor
```

## Engine threshold
Make an engine only when:
- several functions must run in order
- wrong order can cause failure
- intermediate state must move from one step to another
- output contract matters
- verification is required
- the process is reusable

Do not make an engine when:
- one function is enough
- one checklist is enough
- the operation has no stable output

## One-line rule
AILO engine is what happens when order, guards, output contract, verification, failure conditions, and stop rule matter.
