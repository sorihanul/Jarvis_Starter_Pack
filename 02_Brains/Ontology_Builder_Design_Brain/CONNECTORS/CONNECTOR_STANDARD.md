# Connector Standard

## purpose

Connect produced ontology brains to other specialist brains without forcing a common brain format.

## connector shape

```text
consumer_brain:
ontology_brain:
read_first:
read_if_needed:
use_for:
do_not_use_for:
mutation_permission:
handoff_packet:
stop_condition:
```

## mutation policy

Default:

```text
consumer_brain_can_read:true
consumer_brain_can_request_update:true
consumer_brain_can_directly_edit:false
```

## handoff packet

```text
domain:
needed_concepts:
needed_relations:
needed_rules:
needed_exceptions:
source_basis:
unknowns:
conflicts:
```
