# Connector: Coding Brain

## consumer_brain

```text
Coding_Brain
```

## ontology_brain

```text
<Domain>_Ontology_Brain
```

## read_first

```text
PROJECT/EXPORTS/ontology_packet.json
PROJECT/INDEX/BRAIN_USE_INDEX.md
```

## read_if_needed

```text
PROJECT/ONTOLOGY/CONCEPTS.md
PROJECT/ONTOLOGY/ATTRIBUTES.md
PROJECT/ONTOLOGY/RULES.md
PROJECT/WORK/CONFLICTS_AND_EXCEPTIONS.md
```

## use_for

```text
data model draft
field and enum candidates
validation schema candidates
domain naming consistency
test fixture hints
```

## do_not_use_for

```text
treating ontology candidates as final implementation requirements
rewriting domain ontology while coding
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
needed_attributes:
needed_rules:
source_basis:
candidate_fields:
conflicts:
implementation_target:
```

## stop_condition

```text
attribute state is candidate but implementation requires final schema
concept naming conflict affects model or enum names
validation rule has no source basis
```
