# Mode Registry

## modes

```text
intake_mode:
  normalize domain, materials, and desired outputs

brain_design_mode:
  produce domain ontology brain skeleton

project_design_mode:
  produce ontology project workspace shape

connector_design_mode:
  define how other brains consume ontology outputs

schema_design_mode:
  define concept, relation, attribute, conflict, and export schemas

review_mode:
  check for overbuilding, early merge, missing evidence, and weak handoff
```

## default mode

Start in `intake_mode`.

Switch to `brain_design_mode` when the target ontology manager is clear.

Switch to `connector_design_mode` before closing any build.
