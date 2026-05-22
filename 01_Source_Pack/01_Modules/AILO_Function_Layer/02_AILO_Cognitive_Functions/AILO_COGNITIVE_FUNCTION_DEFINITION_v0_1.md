# AILO Cognitive Function Definition v0.1

## Definition
An AILO cognitive function is one bounded, testable meaning operation.

It does not merely normalize slots.
It changes how the model reads, judges, or transforms meaning.

In short:

```text
basic function
-> controls work surface

cognitive function
-> interprets meaning surface
```

## Primary allocation
AILO cognitive functions belong mainly to the brain-local cognitive lane.

Reason:
- they are the raw material for engine construction
- they are shaped by brain purpose
- they should usually remain brain-local rather than global

## Cognitive function shape

```text
id:
name:
layer:
status:
brain_owner:
purpose:
trigger_condition:
input_slots:
operation:
output_schema:
schema_or_lens_used:
guards:
forbids:
validation:
memory_policy:
trace_policy:
cost_class:
fixture_id:
pass_if:
fail_if:
```

## Examples
```text
read_input_as_intent()
check_evidence_authority()
recover_hidden_assumption()
select_smallest_route()
detect_broad_verb()
separate_index_from_evidence()
convert_lens_to_functions()
```

## Brain-local rule
Each brain should collect its own cognitive functions.

Do not force every brain to share the same function set.

Reason:
- the same function name can mean different things in each brain
- evidence, style, purpose, and output standard differ by brain

Promote the making rule globally, not every cognitive function instance.

## Candidate state

```text
raw_interpretation
-> cognitive_function_candidate
-> brain_local_tested
-> brain_local_stable
-> global_pattern_candidate
```

## Failure output

```text
failure_output{
  ok:false,
  reason:"too_broad | workflow_required | brain_context_missing | unstable_meaning | evidence_required",
  suggested_layer:"skill | engine | brain | material",
  missing_context:[]
}
```

## Basic function wrapper

Use basic functions around cognitive functions for:

```text
scope
output shape
memory policy
trace policy
gate label
```

The cognitive function itself should keep one meaning move.

## Skill relation
When several cognitive functions repeatedly work together, bundle them into a skill.

If those functions must run in a strict order with verification gates, define an engine instead.

## One-line rule
AILO cognitive function is a bounded meaning operation that stays testable, usually brain-local, and smaller than a skill.
