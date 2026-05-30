# Acceptance Tests

## test 1: boot path

Pass when `BOOT.md` reads `MAP.md` before detailed rules.

## test 2: independent brain preflight

Pass when `TASKS/PREFLIGHT_RESULT.md` explains why this is an independent brain.

## test 3: domain ownership boundary

Pass when `RUNTIME_BOUNDARY.md` separates this design brain from produced domain ontology brains.

## test 4: production function packs

Pass when `FUNCTION_PACKS.md` includes scope, material, schema, connector, validation, and handoff packs.

## test 5: connector availability

Pass when `CONNECTORS/` includes consumer notes for information research, verification, coding, and domain brains.

## test 6: template availability

Pass when `TEMPLATES/` includes copyable starter files for a domain ontology brain and ontology project.

## test 7: AILO-N restraint

Pass when AILO-N and `topo` are optional export tools, not default formats for every ontology item.

## test 8: no domain content ownership

Pass when this brain does not store domain source material or full domain ontology content.

## test 9: dry-run production readiness

Pass when a model can produce a trial `<Domain>_Ontology_Brain` by copying from:

```text
TEMPLATES/DOMAIN_ONTOLOGY_BRAIN/
TEMPLATES/ONTOLOGY_PROJECT/
SCHEMAS/
CONNECTORS/
```

The dry-run output must include:

```text
source_basis
candidate_policy
asserted_policy
conflict_policy
connector_surfaces
handoff_packet_location
launch_phrase
```
