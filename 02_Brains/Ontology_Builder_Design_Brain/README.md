# Ontology Builder Design Brain

## purpose

`Ontology_Builder_Design_Brain` designs domain-specific ontology brains and ontology project workspaces.

It does not maintain every ontology directly. It creates the structure, schemas, templates, connectors, and export contracts that allow a produced domain ontology brain to manage one domain.

## use when

```text
domain ontology brain design
ontology project workspace design
AI-usable ontology pack design
ontology connector design
ontology export contract design
domain ontology brain production from documents or DB material
```

## do not use when

```text
one-time concept list
simple summary
single existing ontology maintenance
full graph database implementation
```

## start here

Read `START_HERE.md` first.

For an actual boot, use:

```text
온톨로지 빌더 설계 브레인 부팅해.
```

## operating shape

This brain separates:

```text
source material
candidate ontology items
promoted ontology items
conflicts and exceptions
connector surfaces
export packets
consumer brain routes
```

## boundaries

- Do not create one global ontology brain for every domain.
- Do not merge similar terms without evidence.
- Do not let consumer brains mutate ontology internals by default.
- Do not store raw material, candidate work, promoted ontology, exports, and runtime records in one surface.
- Use templates only as production starters; replace placeholders before use.

## main files

- `START_HERE.md`: human and agent entry point.
- `BOOT.md`: boot command and boot response.
- `BRAIN.md`: identity and mission.
- `FUNCTION_PACKS.md`: ontology design function packs.
- `DECISION_TABLES.md`: split, promotion, export, and handoff rules.
- `SCHEMAS/`: required structure contracts.
- `TEMPLATES/`: copyable domain ontology brain and project skeletons.
- `CONNECTORS/`: consumer-brain connector examples.
- `OUTPUT_CONTRACT.md`: produced brain and ontology project output contract.

