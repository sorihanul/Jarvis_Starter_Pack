# Input Slots

## required

```text
ontology_scope:
source_material:
main_use_case:
target_user_or_brain:
```

## recommended

```text
allowed_frame_types:
forbidden_frame_types:
source_policy:
evidence_policy:
asserted_promotion_rule:
merge_policy:
output_format:
```

## optional

```text
domain_terms:
existing_frames:
query_needs:
handoff_target:
validation_depth:
```

## defaults

```text
allowed_frame_types:
  Brain
  FunctionPack
  Policy
  Source
  Claim
  Evidence
  VerificationResult
  RepoTarget
  PatchPlan
  Concept
  Rule

asserted_promotion_rule:
  source + evidence + assertionBasis required

output_format:
  markdown
```
