# Ontology Export Packet Schema

## purpose

Define the portable packet that other brains can use without reading the whole ontology project.

## packet

```yaml
ontology_packet:
  domain:
  version:
  status:
  source_basis:
  concepts:
    - id:
      label:
      definition:
      state:
      source:
      evidence:
      aliases:
      not_same_as:
  relations:
    - from:
      relation:
      to:
      direction:
      state:
      source:
      evidence:
      uncertainty:
  attributes:
    - concept:
      field:
      type_hint:
      required:
      source:
      state:
  rules:
    - id:
      applies_to:
      blocks:
      validates:
      exception_refs:
      state:
  conflicts:
    - id:
      items:
      reason:
      status:
      next_action:
  brain_use:
    info_research:
    verification:
    coding:
    domain:
```

## rule

Consumer brains read export packets and connectors first.
They open full ontology internals only when the connector says they must.
