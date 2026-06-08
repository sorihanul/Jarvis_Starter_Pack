# Context Rehydration Rule

## status

```text
artifact_type: ai_readable_protocol_card
status: local_import_candidate
runtime_enabled: read_on_trigger
source_pack_mutated: false
claim_ceiling: local_rule_imported
```

## one-line rule

```text
As context gets longer, trust memory less; re-read the smallest needed rule surface before crossing boundaries or claiming completion.
```

Korean operating name:

```text
맥락 감쇠-규칙 재수화 원칙
```

## purpose

Prevent long-session drift, source/work boundary blur, public/private confusion, and false completion claims.

This is not a full reboot rule.
It is a small re-read gate for the current decision.

## do not turn this into

```text
full_reboot:false
full_source_pack_reread:false
visible_rulebook_lecture:false
memory_dump:false
excuse_for_slow_meta_work:false
```

## hard triggers

Run this gate before continuing when:

```text
new_session_or_thread:true
user_says_context_changed:true
user_corrects_or_rebukes_the_agent:true
public_private_boundary_may_be_confused:true
source_pack_or_work_surface_boundary_may_be_confused:true
the_agent_is_about_to_claim_done_validated_stable_public_ready_or_runtime_validated:true
the_task_shifted_from_review_to_edit_or_from_private_to_public:true
```

## soft triggers

Do a quick check and re-read only the relevant surface when:

```text
task_runs_long:true
many_files_or_rules_were_added:true
multiple_outputs_were_created:true
initial_scope_changed:true
current_task_state_may_be_stale:true
```

## v3 minimum rehydration pack

Choose the smallest pack that answers the current risk.
Do not read every item by default.

```text
identity:
  - START_HERE.md
  - 00_Orchestrator/Jarvis_Main_Brain/BRAIN.md

boundary:
  - 00_Orchestrator/LOCAL_RULEBOOK.md
  - 00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md
  - MAP.md

active_state:
  - 00_Orchestrator/SESSION_CARD.md
  - 00_Orchestrator/TASKS/CURRENT_TASK.md
  - 00_Orchestrator/READ_REPORT.md

claim_control:
  - ACCEPTANCE_TESTS.md
  - RELEASE_CHECKLIST.md
  - relevant brain ACCEPTANCE_TESTS.md
  - relevant brain VALIDATION_LEVELS.md, if present

coding_or_product_control:
  - relevant coding brain FINAL_GOAL_LOCK.md
  - relevant coding brain WORKING_BEHAVIOR_CONTRACT.md
  - relevant coding brain AI_PATCH_TRUST_RULE.md
  - relevant coding brain PRODUCT_GATE.md, if present
```

## no-false-completion lock

Before using these words, check evidence level:

```text
completion_claim_terms:
  - done
  - complete
  - validated
  - stable
  - public_ready
  - reference_ready
  - runtime_validated
  - source_promoted
  - canon_ready
  - hygiene_passed
```

Completion gate:

```text
evidence_level:
checked_files_or_tests:
claim_ceiling:
blocked_claims:
unverified_surfaces:
next_gate:
```

Allowed language must match evidence:

```text
if_only_files_exist:
  say: candidate_created
  do_not_say: validated

if_only_static_tree_checked:
  say: static_checked
  do_not_say: runtime_validated

if_no_real_project_run:
  say: not_real_project_validated
  do_not_say: reference_ready

if_no_external_refresh:
  say: based_on_local_files
  do_not_say: latest_confirmed

if_tests_could_not_run:
  say: verification_blocked_or_unrun
  do_not_say: tests_passed

if_user_approval_needed:
  say: waiting_for_approval
  do_not_say: complete
```

## coding-specific guard

For code changes, do not let tests alone hide bad implementation shape.

```text
extra_scan_if_code_changed:
  - hardcoded_sample_specific_values
  - silent_fallback_that_masks_failure
  - test_only_branch
  - fake_success_state
  - swallowed_error_without_visible_report
  - scope_drift_outside_locked_files
```

If this scan is not done, say `source_review_unrun` rather than `implementation_clean`.

## rehydration packet

Use internally by default.
Show it only when it changes the answer, blocks a claim, or helps the user see the boundary.

```text
rehydration_packet:
  trigger:
  active_identity:
  write_boundary:
  source_boundary:
  active_claim_ceiling:
  current_task:
  rules_refreshed:
    - path:
      reason:
  rules_skipped:
    - path:
      reason:
  next_gate:
```

## logging rule

Do not log every small refresh.
Log only when rehydration changed the action or prevented a bad claim.

```text
log_if:
  - claim_was_downgraded
  - source_write_boundary_was_corrected
  - public_private_boundary_was_protected
  - user_correction_triggered_rule_refresh
  - completion_claim_was_blocked
```

## failure modes

```text
FM001_memory_confidence:
  relying on remembered rules while file surfaces are available

FM002_full_reread_drag:
  rereading too much and turning the task into rulebook maintenance

FM003_visible_meta_spam:
  explaining the protocol instead of using it

FM004_false_completion:
  claiming done, validated, stable, public_ready, or runtime_validated without evidence level

FM005_boundary_blur:
  mutating source or public/private surfaces without checking boundary

FM006_claim_upgrade:
  upgrading a candidate, static check, or local scenario into stable canon

FM007_skipped_rules_without_reason:
  skipping relevant rules without recording why when the gate affects work
```

## import note

This card is a Jarvis v3 public rule surface. It keeps only the generic trigger logic and no-false-completion lock needed for this package.

## claim ceiling

```text
allowed_claims:
  - local protocol card created
  - v3 surfaces were mapped
  - no-false-completion lock was added
  - coding hardcoding and fake-fallback scan was added

blocked_claims:
  - protocol validated
  - all brains updated
  - behavior improved
  - public release ready
```
