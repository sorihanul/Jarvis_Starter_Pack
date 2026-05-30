# Connector: Info Research Brain

## consumer_brain

```text
Info_Research_Brain
```

## ontology_brain

```text
<Domain>_Ontology_Brain
```

## read_first

```text
PROJECT/SOURCE_LEDGER.md
PROJECT/EXPORTS/ontology_packet.yaml
PROJECT/INDEX/QUESTION_INDEX.md
```

## read_if_needed

```text
PROJECT/ONTOLOGY/CONCEPTS.md
PROJECT/ONTOLOGY/RELATIONS.md
PROJECT/WORK/UNKNOWN_GAPS.md
PROJECT/WORK/CONFLICTS_AND_EXCEPTIONS.md
```

## use_for

```text
term clarification
source-aware query expansion
claim/source separation
relation-aware research planning
unknown gap list
```

## do_not_use_for

```text
asserting candidate concepts as facts
editing ontology internals directly
resolving domain conflicts without evidence
```

## mutation_permission

```text
can_read:true
can_request_update:true
can_directly_edit:false
```

## handoff_packet

```text
domain:
needed_concepts:
needed_relations:
source_basis:
unknowns:
conflicts:
research_questions:
```

## stop_condition

```text
source ledger is missing
requested claim is candidate-only
concept conflict blocks query expansion
```
