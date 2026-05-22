# AILO Cognitive Functionization Principles v0.1

## Purpose
This document defines how AILO material becomes a cognitive function.

Cognitive functionization is not deeper explanation.
It is meaning-operation compression.

## Functionization target
Convert a repeated meaning move into a bounded callable function.

Target shape:

```text
trigger_condition
input_slots
-> meaning operation
-> output_schema
```

A cognitive function interprets the meaning surface.
It does not control the whole work surface by itself.

## What can become a cognitive function
A candidate can become a cognitive function when it repeatedly performs:

```text
hidden premise recovery
evidence authority check
source role judgment
contradiction split
lens extraction
schema application
reader posture selection
unstated risk detection
meaning residue extraction
```

## What should not become a cognitive function
Do not create a cognitive function for:

```text
one-off interpretation
general advice
style preference alone
domain knowledge alone
long chain-of-thought prompt
full research workflow
complete writing process
```

Those may become material, skill, engine, or brain rules later.

## Functionization steps

### 1. Find the repeated meaning move
Start from a repeated interpretive action.

Good:

```text
recover hidden premise
judge source role
split claim from evidence
detect broad verb masking
extract lens from a text
```

Bad:

```text
think deeply
analyze everything
write better
understand the topic
```

### 2. Define trigger condition
The function should not always run.

It needs a trigger:

```text
when a source role is unclear
when a claim lacks evidence
when a sentence uses broad verbs
when a user request hides a premise
```

### 3. Define input slots
Input must be explicit.

Examples:

```text
source_text
claim
evidence_paths
domain_context
candidate_lens
user_request
```

### 4. Define one meaning operation
The function must perform one thought move.

If it needs multiple moves, split it or make a skill.

If those moves must run in a fixed order with verification gates, make an engine candidate.

### 5. Define output schema
Output must be stable.

Examples:

```text
hidden_premise
confidence
evidence_basis
uncertainty
next_check
```

### 6. Define guards
Guards prevent over-reading.

Examples:

```text
do not infer beyond evidence
mark uncertainty
do not convert interpretation into fact
do not rewrite user goal silently
```

### 7. Define validation
Validation must catch bad reasoning.

Examples:

```text
source-backed
inference-labeled
uncertainty-visible
counterexample-considered
```

### 8. Define fixture
A cognitive function needs at least:

```text
positive fixture
negative fixture
counterexample fixture
```

Without fixtures, it remains a candidate.

Candidate state:

```text
raw_interpretation
-> cognitive_function_candidate
-> brain_local_tested
-> brain_local_stable
-> global_pattern_candidate
```

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

If `workflow_required:true`, do not promote it as a cognitive function.
Send it to skill or engine design.

## Failure output

When a candidate fails the cognitive-function gate, return:

```text
failure_output{
  ok:false,
  reason:"too_broad | workflow_required | brain_context_missing | unstable_meaning | evidence_required",
  suggested_layer:"skill | engine | brain | material",
  missing_context:[]
}
```

## Relation to basic functions

A cognitive function may be wrapped by basic functions for scope, output, memory, and trace control.

Example:

```text
scope_lock
-> hidden_premise_extract
-> output_schema_bind
```

Keep the cognitive function focused on one meaning move.

## One-line rule
Cognitive functionization turns repeated meaning work into a bounded, testable thought function.
