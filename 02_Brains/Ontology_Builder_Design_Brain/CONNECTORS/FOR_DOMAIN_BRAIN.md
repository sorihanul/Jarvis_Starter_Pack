# Connector: Domain Brain

## consumer_brain

```text
Domain_Brain
```

## ontology_brain

```text
<Domain>_Ontology_Brain
```

## read_first

```text
PROJECT/EXPORTS/ontology_packet.yaml
PROJECT/INDEX/QUESTION_INDEX.md
```

## read_if_needed

```text
PROJECT/INDEX/CONCEPT_INDEX.md
PROJECT/INDEX/RELATION_INDEX.md
PROJECT/ONTOLOGY/RULES.md
PROJECT/ONTOLOGY/EXCEPTIONS.md
```

## use_for

```text
domain terminology
domain relation context
domain rule and exception lookup
answer boundary
handoff to ontology brain when concept conflict appears
```

## do_not_use_for

```text
silent ontology mutation
unreviewed merge of similar terms
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
needed_rules:
needed_exceptions:
source_basis:
unknowns:
conflicts:
domain_task:
```

## stop_condition

```text
domain answer depends on unresolved concept conflict
requested term is not in packet or index
ontology update is required before safe answer
```
