# Ontology Project Schema

## recommended layout

```text
PROJECT/
  README.md
  START_HERE.md
  MAP.md
  PROJECT_RULEBOOK.md
  INPUTS/
    RAW_DOCS/
    DB_EXPORTS/
    WEB_SOURCES/
    USER_NOTES/
  SOURCE_LEDGER.md
  WORK/
    CONCEPT_CANDIDATES.md
    RELATION_CANDIDATES.md
    ATTRIBUTE_CANDIDATES.md
    CONFLICTS_AND_EXCEPTIONS.md
    UNKNOWN_GAPS.md
    SEARCH_NOTES.md
  ONTOLOGY/
    CONCEPTS.md
    RELATIONS.md
    ATTRIBUTES.md
    RULES.md
    EXCEPTIONS.md
    SOURCE_BINDINGS.md
  EXPORTS/
    ontology_packet.yaml
    ontology_packet.json
    ailo_n_frames.md
  INDEX/
    CONCEPT_INDEX.md
    RELATION_INDEX.md
    QUESTION_INDEX.md
    BRAIN_USE_INDEX.md
```

## separation rule

```text
INPUTS -> raw material
WORK -> candidates and unresolved work
ONTOLOGY -> promoted domain structure
EXPORTS -> consumer-friendly packets
INDEX -> retrieval and brain-use routes
```

Do not collapse these surfaces unless the ontology is very small and temporary.
