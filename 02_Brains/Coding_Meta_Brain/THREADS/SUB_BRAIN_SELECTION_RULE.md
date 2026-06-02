# Sub-Brain Selection Rule

## rule

Sub-brains are selected from `SUB_BRAINS_LIBRARY/`.
They are not active by default.

## select when

```text
role_boundary_clear:true
expected_output_clear:true
verification_or_quality_risk_reduced:true
coordination_cost_acceptable:true
```

## do not select when

```text
one_file_change:true
role_overlap_high:true
expected_output_unclear:true
selection_only_adds_delay:true
```

## required selection note

Every selected sub-brain must have:

```text
role:
scope:
handoff_input:
expected_output:
close_condition:
report_target:
```
