# Local Rulebook

## hard rules

```text
single_thread_only:true
toml_agents_on_demand:true
default_agent_count:0
project_publish_target:01_PROJECT_only
final_goal_lock_before_design:true
proper_working_behavior_first:true
conservative_operation_loop_first:true
critical_risk_scan_before_implementation:true
ai_patch_untrusted_until_verified:true
boring_maintainable_default:true
scope_before_edit:true
verification_required_before_done:true
memory_export_is_candidate_not_canon:true
stable_promotion_blocked_until_real_solo_tests:true
```

## coding behavior

- Read the project before edits.
- Lock scope before drafting agents or patches.
- Draft only the TOML agents needed for the current bounded task.
- Run agent roles sequentially in the same thread.
- Prefer small diffs and existing project patterns.
- Do not use this brain when independent parallel threads are needed.
- Treat loops, agents, TOML, and automation as support tools only; they do not outrank purpose fit, actual behavior, verification, or maintainability.

## agent behavior

- Active TOML agents are temporary working contracts.
- Archive or discard active agents at closeout.
- Promote only repeated, stable agent patterns into `AGENTS/CANDIDATES/`.

## verification behavior

- No verification means incomplete unless the blocker is explicit.
- The default loop is: purpose fit -> run or render -> detect abnormality -> locate cause -> minimal fix -> rerun -> record.
- Record failed checks and interpretation.
- Do not hide build, test, typecheck, lint, screenshot, or smoke failures.
