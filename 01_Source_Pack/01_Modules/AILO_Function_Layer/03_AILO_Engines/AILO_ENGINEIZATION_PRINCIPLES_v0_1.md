# AILO Engineization Principles v0.1

## Purpose
This document defines how AILO material becomes an engine.

Engineization is not making a longer prompt.
It is ordering functions into a verified process.

## Engineization target
Convert repeated multi-step failure-prone work into a stable pipeline.

Target shape:

```text
entry_rule
-> pipeline
-> intermediate_state_handoff
-> output_contract
-> verification_gate
-> stop_rule
```

## What can become an engine
A candidate can become an engine when the task repeatedly needs:

```text
ordered function calls
intermediate outputs
intermediate state handoff
step-by-step guards
verification before completion
failure detection
controlled stop
reusable output contract
```

## What should not become an engine
Do not create an engine for:

```text
one function
one cognitive function
one checklist
one explanation
one research idea
one domain lens
an untested workflow
```

## Engineization steps

### 1. Find repeated ordered work
Start from a task where order matters.

Good:

```text
extract intent slots before routing
classify document role before reading order
check route cost before opening sources
verify output contract before completion
```

Bad:

```text
think better
do research
write everything
manage knowledge
```

### 2. Define entry rule
The engine must know when it starts.

Example:

```text
run when user request must be converted into structured intent slots
```

### 3. Define pipeline
Each step must have input and output.

Example:

```text
step_1: scope_lock -> bounded_scope
step_2: missing_slot_detect(bounded_scope) -> missing
step_3: route_lock(bounded_scope, missing) -> first_route
```

### 4. Define intermediate state handoff
Each step output must say where it goes next.

Example:

```text
bounded_scope
-> used by missing_slot_detect and route_lock

missing
-> used by route_lock and verification_gate

first_route
-> used by output_contract
```

If step outputs do not feed later steps, check whether the candidate is only a checklist.

### 5. Define output contract
The final output must be predictable.

Example:

```text
intent_packet
route_packet
engine_draft
verification_report
```

### 6. Define guards
Guards prevent wrong expansion.

Examples:

```text
do not skip missing-slot check
do not open all sources by default
do not complete if verification fails
```

### 7. Define verification gate
The engine must prove that the pipeline result is valid.

### 8. Define failure conditions
Failure must be explicit.

Example:

```text
required slot missing
output contract incomplete
route cost too high
source authority unclear
```

### 9. Define stop rule
The engine must know where to stop.

## Promotion gate
A candidate becomes an engine only when:

```text
repeated_need:true
multi_step:true
order_matters:true
wrong_order_causes_failure:true
output_contract_stable:true
intermediate_handoff_stable:true
verification_required:true
failure_conditions_known:true
fixture_exists:true
```

## One-line rule
Engineization begins when order and verification matter more than the individual function.
