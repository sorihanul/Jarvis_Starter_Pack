# Ontology Builder Design Brain Map

## layout

```text
Ontology_Builder_Design_Brain/
  START_HERE.md
  BOOT.md
  MAP.md
  LOCAL_RULEBOOK.md
  MEMORY_MAP.md
  RUNTIME_BOUNDARY.md
  SESSION_CARD.md
  BRAIN.md
  MODE_REGISTRY.md
  FUNCTION_PACKS.md
  DECISION_TABLES.md
  SOURCE_BINDINGS.md
  OUTPUT_CONTRACT.md
  ACCEPTANCE_TESTS.md
  TASKS/
    PREFLIGHT_RESULT.md
    CURRENT_TASK.md
  LOGS/
    SESSION_OPS_LOG.md
  CAPSULES/
    CURRENT_CAPSULE.md
  SCHEMAS/
    DOMAIN_ONTOLOGY_BRAIN_SCHEMA.md
    ONTOLOGY_PROJECT_SCHEMA.md
    ONTOLOGY_EXPORT_PACKET_SCHEMA.md
  TEMPLATES/
    DOMAIN_ONTOLOGY_BRAIN/
      README.md
    ONTOLOGY_PROJECT/
      README.md
  CONNECTORS/
    CONNECTOR_STANDARD.md
    FOR_INFO_RESEARCH_BRAIN.md
    FOR_VERIFICATION_BRAIN.md
    FOR_CODING_BRAIN.md
    FOR_DOMAIN_BRAIN.md
  REPORTS/
    README.md
```

## core files

- `BRAIN.md`: identity, role, and forbidden scope
- `FUNCTION_PACKS.md`: design-time production packs
- `DECISION_TABLES.md`: repeated build decisions
- `SOURCE_BINDINGS.md`: source pack and option pack references
- `OUTPUT_CONTRACT.md`: produced brain/project/connector output format
- `SCHEMAS/`: minimal schemas for produced assets
- `TEMPLATES/`: starter shapes for generated ontology brain/project
- `CONNECTORS/`: how other brains consume ontology outputs

## boundary

This brain creates ontology brain skeletons.

It may produce a draft domain ontology if needed for testing, but long-term ontology maintenance belongs to the produced domain ontology brain.
