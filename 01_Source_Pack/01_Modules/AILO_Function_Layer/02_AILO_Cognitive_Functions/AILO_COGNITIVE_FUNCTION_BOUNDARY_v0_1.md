# AILO Cognitive Function Boundary v0.1

## Purpose
This document defines what counts as an AILO cognitive function.

It also defines what does not count as a cognitive function yet.

## Core definition
An AILO cognitive function is a bounded meaning operation.

It receives explicit input slots, performs one repeatable thought move, and returns a stable output schema.

```text
input_slots
-> bounded meaning operation
-> output_schema
```

## What makes it cognitive
A function becomes cognitive when it changes how the model reads, judges, or transforms meaning.

It may handle:

```text
hidden premise
meaning gap
evidence authority
contradiction
lens selection
schema application
reader posture
brain-local reasoning
```

## Difference from basic function

```text
basic function
-> controls the work surface

cognitive function
-> interprets the meaning surface
```

Basic function asks:

```text
What is the scope?
What route should be read?
What slot is missing?
What output shape is required?
```

Cognitive function asks:

```text
What unstated premise is active?
What does this source actually do?
Which evidence should be trusted?
Which lens changes the reading?
What contradiction matters?
```

## Not enough to be a cognitive function
These are not cognitive functions yet:

```text
a good interpretation
a long analysis prompt
a domain theory
a persona description
a mental model name
a vague reasoning style
a broad instruction to think deeply
```

They become cognitive functions only when converted into:

```text
trigger_condition
input_slots
operation
output_schema
guards
validation
fixture
```

## Cognitive function must stay bounded
A cognitive function is smaller than a skill.

It should perform one thought move, not a whole workflow.

If several cognitive functions must run in order, that is a skill or engine candidate.

## Brain-local default
Cognitive functions default to brain-local ownership.

Reason:

```text
same name can mean different things in different brains
evidence rules differ by domain
output standards differ by task
style and reading posture differ by brain
```

Promote the making rule when useful.
Do not promote every local cognitive function to a global set.

```text
Promote the making rule globally, not every cognitive function instance.
```

## Candidate state

A cognitive function should move through brain-local proof before it becomes reusable.

```text
raw_interpretation
-> cognitive_function_candidate
-> brain_local_tested
-> brain_local_stable
-> global_pattern_candidate
```

Do not register a local interpretation as a stable cognitive function without fixtures.

## Promotion gate

A candidate becomes a cognitive function only when:

```text
repeated_meaning_need:true
one_thought_move:true
input_output_stable:true
brain_context_defined:true
validation_possible:true
fixtures_exist:true
workflow_required:false
```

If a workflow is required, the candidate belongs to a skill or engine layer.

## Failure output

When a candidate is too broad or lacks brain context, return:

```text
failure_output{
  ok:false,
  reason:"too_broad | workflow_required | brain_context_missing | unstable_meaning | evidence_required",
  suggested_layer:"skill | engine | brain | material",
  missing_context:[]
}
```

Failure output prevents a cognitive function from pretending to be a full skill.

## Basic function wrapper

A cognitive function may be wrapped by basic functions for scope, output, memory, and trace control.

Example:

```text
scope_lock
-> hidden_premise_extract
-> output_schema_bind
```

Cognitive function handles the meaning operation.
Basic function controls the surrounding work surface.

## One-line rule
An AILO cognitive function is a bounded, testable meaning operation, not a broad instruction to reason.
