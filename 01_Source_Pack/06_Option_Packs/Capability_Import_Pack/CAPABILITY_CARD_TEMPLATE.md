# Capability Card Template v0.1

## Purpose

Use this card when an outside pattern is worth adapting into Jarvis.

The card must stand alone. It must not require the reader to know the source project.

## Template

```text
capability_name:
one_line_purpose:
source_type:
source_strength: primary | secondary | commentary | mixed
import_decision: ignore | note | candidate | adapt | defer | reject

problem_it_solves:
when_to_use:
when_not_to_use:

input_conditions:
required_files_or_context:
output_form:

jarvis_layer:
  core_rule | option_pack | skill | brain_blueprint | project_workspace | test_rule

related_option_packs:

operating_rule:

workflow:
  1.
  2.
  3.

guardrails:

validation:

not_imported:

maintenance_note:
```

## Writing Rules

- Write the capability in general language.
- Do not mention source-specific names unless the analysis note requires provenance.
- Do not copy source text.
- Do not describe a feature as working until it has a local validation path.
- Prefer one capability card per reusable rule.

## Good Capability Shape

```text
problem -> trigger -> small workflow -> output -> validation -> stop rule
```

## Bad Capability Shape

```text
source summary -> admiration -> vague recommendation -> no test
```
