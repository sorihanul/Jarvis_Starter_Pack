# Domain Ontology Brain Schema

## required surfaces

```text
START_HERE.md
BOOT.md
MAP.md
LOCAL_RULEBOOK.md
MEMORY_MAP.md
SESSION_CARD.md
BRAIN.md
MODE_REGISTRY.md
FUNCTION_PACKS.md
DECISION_TABLES.md
SOURCE_BINDINGS.md
OUTPUT_CONTRACT.md
ACCEPTANCE_TESTS.md
TASKS/
LOGS/
CAPSULES/
PROJECT/
CONNECTORS/
EXPORTS/
```

## required identity

```text
domain:
ontology_scope:
owns:
does_not_own:
source_policy:
candidate_policy:
asserted_policy:
conflict_policy:
connector_policy:
```

## minimum working loop

```text
intake source
extract concept candidates
extract relation candidates
extract attribute candidates
record conflicts and exceptions
bind evidence
promote only with basis
export connector packets
```

## forbidden

```text
merge_similar_terms_without_basis:true
assert_search_result_as_fact:true
let_consumer_brain_mutate_internal_ontology_by_default:true
store_raw_source_and_asserted_ontology_in_same_surface:true
```
