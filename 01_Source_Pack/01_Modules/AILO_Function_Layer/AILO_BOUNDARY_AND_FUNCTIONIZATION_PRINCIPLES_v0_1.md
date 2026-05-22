# AILO Boundary and Functionization Principles v0.1

## Purpose
This document defines:

```text
what counts as AILO
what counts as AILO material
what counts as an AILO function
what must not be called an AILO function
```

## What counts as AILO
Something counts as AILO when it can be expressed as model-facing control language.

It must be reducible to at least some of these parts:

```text
intent
verb
slots
rules
guards
forbids
risk
memory policy
trace policy
output contract
validation
stop rule
```

AILO is not just a topic.
AILO is a way to turn intent into controlled model behavior.

## AILO material
AILO material is anything that can become a control part.

Examples:

```text
a repeated user instruction
a recurring failure pattern
a preferred output shape
a stop condition
a permission boundary
a memory rule
a trace rule
a slot structure
a validation rule
a model-facing verb
```

These are not automatically functions.
They are function material.

## AILO function
An AILO function is a bounded callable control unit.

It must have:

```text
name
purpose
input_slots
operation
output_schema
guards
forbids
memory_policy
trace_policy
fixture
pass_if
fail_if
```

Without stable input and output, it is not a function yet.

## AILO basic function
An AILO basic function controls the work surface.

It may control:

```text
scope
route
slot
schema
memory side effect
trace weight
gate
stop condition
```

It must not perform deep meaning judgment.

## AILO cognitive function
An AILO cognitive function performs bounded meaning work.

It may handle:

```text
hidden premise
meaning gap
evidence authority
contradiction
lens
reading posture
brain-local reasoning
```

It must still have input, output, guards, and validation.

## Not enough to be AILO
These are not AILO by themselves:

```text
good advice
general theory
domain knowledge
style preference
persona description
long prompt paragraph
unstructured instruction
```

They become AILO only when converted into slots, rules, guards, outputs, and stop conditions.

## Not enough to be an AILO function
These are not AILO functions yet:

```text
a reusable phrase without input/output
a checklist without operation
a rule without fixture
a prompt trick without validation
a domain concept without control surface
a workflow with many steps and no bounded output
```

## Functionization principle
To functionize AILO material:

```text
1. find the repeated control move
2. name the move as a small verb
3. define input slots
4. define output schema
5. define operation steps
6. define guards and forbids
7. define memory and trace policy
8. define pass_if and fail_if
9. add positive fixture
10. add negative fixture
11. decide basic or cognitive
```

## Boundary test
Ask these questions:

```text
Can it be called with input slots?
Does it return a stable output schema?
Can it fail?
Can it be tested?
Does it stay below skill or engine size?
Does it avoid hidden uncontrolled memory effects?
```

If the answer is no, it is still material, not a function.

## One-line rule
AILO is controlled intent language; an AILO function is AILO material compressed into a bounded, testable input-output control unit.
