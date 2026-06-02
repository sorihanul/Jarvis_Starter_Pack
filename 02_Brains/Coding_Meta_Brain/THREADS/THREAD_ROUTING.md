# Thread Routing

## purpose

Decide whether the case stays in one thread or splits into sub-brain threads.

## single-thread mode

Use when:

```text
small_change:true
single_project_surface:true
verification_simple:true
role_conflict_low:true
```

## multi-thread mode

Use when:

```text
frontend_backend_split:true
design_quality_required:true
integration_contract_risk:true
verification_complex:true
release_boundary_needed:true
```

## routing output

```text
thread_model:
selected_sub_brain_threads:
handoff_required:
registry_update_required:
close_condition:
```
