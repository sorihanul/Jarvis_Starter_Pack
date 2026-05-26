# Validation Rule

## structure validation

```text
scope_visible:
source_basis_visible:
frame_count_reasonable:
relation_index_present:
query_table_present:
unknowns_present:
```

## frame validation

Check every frame:

```text
has_isa:
has_role_or_definition:
has_state:
has_source_when_persistent:
has_evidence_when_asserted:
has_assertionBasis_when_asserted:
conf_not_used_as_authority:
execution_not_inside_frame:
```

## relation validation

Check every relation:

```text
has_from:
has_to:
has_direction:
has_relation_type:
has_reason:
has_source_or_uncertainty:
```

## behavior validation

The mini ontology must answer:

```text
what can the AI read less because of this?
what candidate/asserted confusion does this prevent?
what action or output can this block?
what validation does this require?
what handoff packet can this support?
```

If these questions cannot be answered, the ontology is probably decorative.

## verdict

```text
pass:
  frame set changes AI behavior and passes frame/relation checks

pass_with_risk:
  useful but some frames remain candidate or evidence is partial

fail:
  decorative classification, unsupported asserted frames, or uncontrolled frame growth
```
