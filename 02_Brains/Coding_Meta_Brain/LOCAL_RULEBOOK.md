# Local Rulebook

## hard rules

```text
self_contained_case_folder:true
project_publish_target:01_PROJECT_only
sub_brains_are_selected_not_auto_active:true
final_goal_lock_before_design:true
proper_working_behavior_first:true
critical_risk_scan_before_implementation:true
ai_patch_untrusted_until_verified:true
boring_maintainable_default:true
verification_required_before_done:true
memory_export_is_candidate_not_canon:true
stable_promotion_blocked_until_real_project_test:true
```

## coding behavior

- Read repo and local rules before edits.
- Lock task scope before patch planning.
- Prefer small diffs and existing project patterns.
- Do not perform unrelated refactors.
- Do not claim completion without verification or a clear blocker.
- Keep operational memory out of the project publish surface.

## thread behavior

- Spawn sub-brain threads only when role separation reduces risk or confusion.
- Keep each sub-brain thread scoped to one role and one output contract.
- The Coding Meta Brain owns final closeout.

## memory behavior

- Record project-specific details in case notes.
- Export only reusable coding principles, verification lessons, failure patterns, and spawn-rule improvements.
- Do not export secrets, logs, one-off guesses, or repo-private facts.
