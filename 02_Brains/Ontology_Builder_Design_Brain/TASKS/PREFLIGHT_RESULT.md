# Preflight Result

## Build Preflight

```text
preflight_result:
  normalized_goal: Ontology Builder Design Brain
  selected_function_packs:
    - domain_scope_lock
    - material_surface_design
    - ontology_brain_role_design
    - ontology_project_template_design
    - schema_contract_design
    - connector_contract_design
    - validation_handoff_design
  sufficient_layer: brain
  reason: This role must persistently produce multiple domain ontology brains, keep design rules, templates, schemas, connectors, and reentry surfaces.
  build_allowed: true
  required_surfaces:
    - START_HERE.md
    - BOOT.md
    - MAP.md
    - LOCAL_RULEBOOK.md
    - MEMORY_MAP.md
    - RUNTIME_BOUNDARY.md
    - SESSION_CARD.md
    - BRAIN.md
    - MODE_REGISTRY.md
    - FUNCTION_PACKS.md
    - DECISION_TABLES.md
    - SOURCE_BINDINGS.md
    - OUTPUT_CONTRACT.md
    - ACCEPTANCE_TESTS.md
    - SCHEMAS/
    - TEMPLATES/
    - CONNECTORS/
    - REPORTS/
    - TASKS/
    - LOGS/
    - CAPSULES/
  next_action: Use this brain to design a domain ontology brain and project workspace when the user provides a domain, materials, or DB source.
```

## Why Not Smaller

### why_not_function_pack

A function pack is not enough because this role maintains production templates, connector standards, and repeated design decisions.

### why_not_engine

An engine is not enough because ontology brain design requires domain-sensitive scope, source, and connector choices rather than one strict sequence.

### why_not_skill

A skill is not enough because the output is not only a repeated procedure. It needs a persistent design identity and local templates.

### why_not_brain_component

A component is not enough because this role produces independent domain ontology brains and project workspaces.

## Decision

Create an independent design brain.
