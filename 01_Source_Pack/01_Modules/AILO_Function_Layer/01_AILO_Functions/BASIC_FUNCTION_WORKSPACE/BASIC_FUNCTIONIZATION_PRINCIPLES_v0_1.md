# Basic Functionization Principles v0.1

## Purpose
This document defines how AILO material becomes a basic function.

Basic functionization is not prompt expansion.
It is control compression.

## Basic functionization target
Convert repeated control moves into small callable contracts.

The target shape is:

```text
input_slots
-> bounded operation
-> output_schema
```

Default rule:

```text
A basic function controls execution shape.
It does not perform the final task unless explicitly defined.
```

In short:

```text
basic function
-> controls how work should proceed
-> does not replace the work itself
```

## What can become a basic function
A candidate can become a basic function when it controls:

```text
scope
route
missing slot
output shape
memory side effect
trace weight
permission gate
stop condition
```

## What cannot become a basic function
A candidate cannot become a basic function when it requires:

```text
hidden premise recovery
evidence authority comparison
domain lens judgment
reader posture change
brain-local identity
multi-step engine order
creative or strategic judgment
```

Those belong to cognitive function, skill, brain, or engine layers.

## Boundary with skill and engine

Use this split:

```text
A function controls one move.
A skill packages several moves for user-facing use.
An engine orders several moves into a verified internal mechanism.
```

If one control move is enough, do not make a skill.
If order and verification do not matter, do not make an engine.

## Functionization steps

### 1. Find the repeated control move
Do not start from a topic.
Start from repeated behavior.

Bad:

```text
memory
writing
agent
research
```

Good:

```text
decide memory side effect
lock output schema
choose first route
expose missing slot
```

### 2. Name it as a small verb
The name must describe one action.

Good:

```text
scope_lock
route_lock
missing_slot_detect
```

Bad:

```text
make_everything_clear
manage_project
think_better
```

### 3. Define input slots
Input slots must be explicit.

If the function needs information that is not present, it must expose the missing slot.

### 4. Define output schema
Output must be stable.

The same kind of input must produce the same output shape.

### 5. Define operation
Operation should be short.

Use 3 to 7 steps.
If it needs a long workflow, it is probably a skill or engine.

### 6. Define guards
Guards prevent expansion.

Examples:

```text
do not execute the task
do not open all routes
do not write canon memory
do not infer missing intent
```

### 7. Define forbids
Forbids mark hard no-go behavior.

Examples:

```text
hidden meaning judgment
global rule change
full-folder sweep by default
unconfirmed memory write
```

### 8. Define memory and trace policy
Basic functions must keep side effects explicit.

Default:

```text
memory_policy:"none"
trace_policy:"min"
```

### 9. Add fixtures
A function needs at least:

```text
positive fixture
negative fixture
real-task fixture
```

Without fixtures, it is still a candidate.

Candidate state:

```text
raw_material
-> function_candidate
-> tested_basic_function
-> stable_basic_function
-> deprecated
```

Do not skip directly from raw material to stable function.

### 10. Decide layer
Use this split:

```text
control surface
-> basic function

meaning surface
-> cognitive function
```

When a candidate fails the basic-function layer, return a failure output instead of forcing promotion:

```text
failure_output{
  ok:false,
  reason:"missing_required_input | meaning_judgment_required | unstable_output | existing_function_sufficient",
  missing_slots:[],
  suggested_layer:"cognitive_function | skill | engine"
}
```

## Promotion gate
A candidate becomes a basic function only when:

```text
repeated_need:true
control_facing:true
input_output_stable:true
existing_functions_insufficient:true
meaning_judgment_required:false
fixtures_exist:true
```

## Anti-bloat rule
Do not create a new basic function when an existing function can be tightened.

Prefer:

```text
tighten existing function
```

over:

```text
add new function
```

The common layer should stay small and stable.

Prefer:

```text
10 to 20 stable basic functions
```

over:

```text
200 overlapping function names
```

## One-line rule
Basic functionization turns repeated control behavior into a small, testable, side-effect-controlled function.
