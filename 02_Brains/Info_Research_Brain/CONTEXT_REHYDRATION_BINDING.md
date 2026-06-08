# Context Rehydration Binding

## purpose

This file connects this brain to the root Jarvis v3 context rehydration rule.

The rule is not part of normal full boot unless a trigger appears.
Use it only when context drift, boundary confusion, or completion-claim risk exists.

## root rule

```text
../../00_Orchestrator/Jarvis_Main_Brain/CONTEXT_REHYDRATION_RULE.md
```

## read-on-trigger

Read the root rule before this brain claims or decides:

```text
done
complete
validated
stable
public_ready
reference_ready
runtime_validated
source_promoted
canon_ready
hygiene_passed
```

Also read it when:

```text
public_private_boundary_unclear:true
source_or_work_surface_boundary_unclear:true
long_session_context_may_have_decayed:true
user_corrected_the_agent:true
static_check_may_be_overstated_as_runtime_validation:true
```

## local use

Use the root rule to choose the smallest needed local pack:

```text
identity:
  - START_HERE.md
  - BRAIN.md

boundary:
  - LOCAL_RULEBOOK.md
  - RUNTIME_BOUNDARY.md
  - SOURCE_BINDINGS.md

active_state:
  - SESSION_CARD.md
  - TASKS/CURRENT_TASK.md

claim_control:
  - OUTPUT_CONTRACT.md
  - ACCEPTANCE_TESTS.md
```

If a listed file does not exist in this brain, skip it with reason instead of inventing it.

## claim ceiling

Do not claim stronger status than the evidence supports.

```text
files_exist_only -> candidate_created
static_tree_checked -> static_checked
not_run_on_real_task -> not_runtime_validated
report_schema_only -> template_only
verification_unavailable -> verification_blocked_or_unrun
```

## anti-patterns

```text
full_reboot_for_small_claim:false
full_source_pack_reread:false
visible_meta_lecture:false
memory_confidence_over_file_surface:false
claim_done_without_evidence:false
```
