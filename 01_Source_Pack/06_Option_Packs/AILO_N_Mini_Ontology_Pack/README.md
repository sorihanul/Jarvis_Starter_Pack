# AILO-N Mini Ontology Pack

## purpose

This pack turns mixed information into a small operational ontology that an AI can actually use.

It is based on `Ontology_Pack`, but it uses AILO-N frames instead of general knowledge cards.

## one-line identity

```text
AILO-N Mini Ontology Pack creates reusable target frames with state, evidence, blocks, validates, and merge/discard rules.
```

## why this exists

General ontology work can become document debt when it does not change the model's behavior.

This pack is valid only when the resulting frames help the AI:

```text
route
judge state
separate candidate from asserted
check source/evidence
block unsafe action
validate outputs
handoff compact context
merge or discard duplicates
```

## relationship

```text
Ontology_Pack
-> splits material into entity, property, relation, event, action, control_rule, evidence

AILO-N Frame Use Rules
-> decides whether a target deserves a persistent frame

AILO-N Practical Use Card
-> provides the practical frame shape

AILO-N Mini Ontology Pack
-> builds a small frame set that can drive later AI behavior
```

## read order

1. `ACTIVATION_RULE.md`
2. `INPUT_SLOTS.md`
3. `FRAME_SCHEMA.md`
4. `TOPOLOGY_HINT_RULE.md`
5. `BUILD_FLOW.md`
6. `OPERATING_RULE.md`
7. `OUTPUT_CONTRACT.md`
8. `VALIDATION_RULE.md`
9. `STOP_RULE.md`
10. `USAGE_EXAMPLE.md`

Also read when needed:

```text
../Ontology_Pack/README.md
../../01_Modules/AILO_Function_Layer/AILO_N_FRAME_USE_RULES_v0_1.md
../../01_Modules/AILO_Function_Layer/AILO_N_PRACTICAL_USE_CARD_v0_1.md
../../01_Modules/AILO_Function_Layer/AILO_RELATION_TOPOLOGY_PACK_v0_1.md
```

## output

The pack produces:

```text
mini_ontology_scope
frame_candidates
accepted_frames
rejected_or_merged_frames
relation_index
topology_hints
query_table
validation_report
```

## boundary

This is not a full ontology engine.

It does not require RDF, OWL, graph databases, automated reasoners, or complete class hierarchies.

It produces a small frame set that changes how the AI reads, judges, blocks, validates, and hands off work.

`topo` hints are optional and should be used only when relation-network structure helps compression, validation, routing, or handoff.

## one-line rule

```text
Build only the frames that make the next AI action safer, clearer, or easier to verify.
```
