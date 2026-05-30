# Connector: Verification Brain

## consumer_brain

```text
Jarvis_Verification_Brain
```

## ontology_brain

```text
<Domain>_Ontology_Brain
```

## read_first

```text
PROJECT/EXPORTS/ontology_packet.yaml
PROJECT/ONTOLOGY/RULES.md
PROJECT/ONTOLOGY/EXCEPTIONS.md
```

## read_if_needed

```text
PROJECT/ONTOLOGY/SOURCE_BINDINGS.md
PROJECT/WORK/CONFLICTS_AND_EXCEPTIONS.md
PROJECT/SOURCE_LEDGER.md
```

## use_for

```text
success criteria derivation
exception checks
evidence binding checks
conflict review
candidate vs asserted validation
```

## do_not_use_for

```text
creating new domain concepts without source
promoting candidate ontology items alone
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
needed_rules:
needed_exceptions:
source_basis:
evidence_bindings:
conflicts:
validation_question:
```

## stop_condition

```text
rule source is missing
exception conflicts are unresolved
asserted policy cannot be verified
```
