# AILO Cognitive Function Contract v0.1

## Identity
A cognitive function is a small callable thought operation.

It must be explicit enough to test.
It must be bounded enough to reuse.

## Required fields

```text
id
name
layer
status
brain_owner
purpose
trigger_condition
input_slots
operation
output_schema
failure_output
schema_or_lens_used
guards
forbids
validation
memory_policy
trace_policy
cost_class
fixture_id
pass_if
fail_if
```

## Layer value

```text
layer:"ailo_cognitive_function"
```

## Status values

```text
candidate
fixture_ready
tested
brain_local_stable
promoted_pattern
deprecated
```

Candidate proof states:

```text
raw_interpretation
cognitive_function_candidate
brain_local_tested
brain_local_stable
global_pattern_candidate
deprecated
```

Do not skip from raw interpretation to promoted pattern.

## Brain owner
Default:

```text
brain_owner:"local"
```

Use a named brain only when the function is designed for that brain.

Global promotion rule:

```text
promote_making_rule:true
promote_every_instance:false
```

The reusable asset is usually the making rule, not every local function instance.

## Cost class

```text
low
mid
high
```

Default:

```text
cost_class:"mid"
```

If it needs web search, long source reading, or multi-source evidence comparison, mark it `high`.

## Memory policy

```text
none
trace_only
candidate_only
brain_local_note
promotion_request
```

Default:

```text
memory_policy:"candidate_only"
```

Cognitive functions should not write global canon directly.

## Trace policy

```text
min
structured
evidence_linked
```

Default:

```text
trace_policy:"structured"
```

## Failure output

When a cognitive function cannot run within its boundary, return:

```text
failure_output{
  ok:false,
  reason:"too_broad | workflow_required | brain_context_missing | unstable_meaning | evidence_required",
  suggested_layer:"skill | engine | brain | material",
  missing_context:[]
}
```

Failure output is a layer-routing surface.
It must not be replaced by a vague explanation.

## Wrapper rule

A cognitive function may be wrapped by basic functions.

Use basic functions for:

```text
scope
output shape
memory policy
trace policy
gate label
```

Do not absorb those controls into the cognitive function unless the cognitive function contract explicitly requires them.

## Pass rule
A cognitive function passes only when:

```text
trigger_condition is explicit
input_slots are explicit
operation is one thought move
output_schema is stable
meaning judgment is bounded
guards stop over-interpretation
validation can catch hallucinated reasoning
fixture exists
workflow_required is false
```

## Fail rule
A cognitive function fails when it:

```text
becomes a full essay
becomes a complete workflow
uses a vague lens without slots
changes domain assumptions silently
turns uncertain inference into fact
writes memory without policy
requires multiple engines to complete
absorbs scope, output, memory, or trace control without contract
```

## One-line rule
A cognitive function must make a meaning move explicit, bounded, and testable.
