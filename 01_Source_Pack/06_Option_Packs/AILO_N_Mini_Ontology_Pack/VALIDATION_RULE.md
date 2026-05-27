# Validation Rule

## structure validation

```text
scope_visible:
source_basis_visible:
frame_count_reasonable:
relation_index_present:
topology_hints_are_optional:
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
topo_not_used_as_authority:
topo_not_replacing_relation_slots:
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

## topology validation

When `topo` appears, check:

```text
known_topo_rel:
topo_to_refs_defined_or_explained:
hard_gate_has_rule_or_condition:
hard_cut_has_conflict_block_or_cannot:
anchor_has_source_or_evidence:
sink_has_output_contains_or_produces:
topo_matches_relation_slots:
```

Topology warnings should stay light.
The mini ontology should not become invalid only because a useful optional topology hint is incomplete, unless strict validation is requested.

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
