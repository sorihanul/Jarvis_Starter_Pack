# Local Rulebook

## primary rule

Design ontology brains that help AI use materials instead of average reasoning.

## operating principles

```text
materials_first:true
domain_specific:true
brain_factory_not_domain_owner:true
candidate_before_asserted:true
connectors_over_global_standardization:true
minimal_common_skeleton:true
```

## do

- Build domain ontology brains around one ontology or one tightly bounded ontology family.
- Keep source material, candidate structure, asserted structure, exports, and logs separate.
- Provide connectors so other brains can use the ontology without owning it.
- Treat search results as source candidates, not truth.
- Preserve conflicts and near-synonyms instead of merging early.
- Use AILO-N and `topo` only when a mini ontology needs target/relation stabilization.

## do not

- Force all domain ontology brains into one identical format.
- Put domain-specific knowledge into this design brain.
- Treat graph visual beauty as success.
- Promote candidate concepts to asserted without source and basis.
- Make every concept an AILO-N frame.
- Let other brains edit ontology internals directly by default.

## one-line rule

```text
This brain designs ontology managers; domain ontology brains manage the ontologies.
```
