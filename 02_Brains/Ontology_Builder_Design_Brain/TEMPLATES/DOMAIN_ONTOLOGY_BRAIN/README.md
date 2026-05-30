# Domain Ontology Brain Template

## purpose

Use this template when producing a brain that manages one domain ontology.

## placeholder

```text
<Domain>_Ontology_Brain/
```

## required role

```text
This brain manages the <Domain> ontology only.
It extracts, maintains, validates, exports, and connects domain concepts, relations, attributes, rules, exceptions, and conflicts.
```

## copyable starter files

This folder contains a minimal copyable skeleton.

Copy these files into a new `<Domain>_Ontology_Brain/` and replace `<Domain>` placeholders:

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
OUTPUT_CONTRACT.md
SOURCE_BINDINGS.md
ACCEPTANCE_TESTS.md
TASKS/CURRENT_TASK.md
LOGS/SESSION_OPS_LOG.md
CAPSULES/CURRENT_CAPSULE.md
```

Use `SCHEMAS/DOMAIN_ONTOLOGY_BRAIN_SCHEMA.md` as the full required surface list when the brain becomes persistent.

## first launch phrase pattern

```text
<도메인> 온톨로지 브레인 부팅해.
```

## first task pattern

```text
자료/DB를 받아 source ledger를 만들고 concept/relation/attribute candidates를 추출한다.
```
