# Coding TOML Agent Brain START HERE

## identity

This is an experimental single-thread coding harness.

It does not split work into multiple sub-brain threads.
It stays in one thread and drafts temporary TOML role agents only when a bounded coding task benefits from explicit role contracts.

## status

```text
experimental:true
runtime_validated:false
reference_ready:false
single_thread_system:true
toml_agents_created_on_demand:true
requires_real_solo_coding_tests:true
```

## read order

1. `BOOT.md`
2. `MAP.md`
3. `LOCAL_RULEBOOK.md`
4. `RUNTIME_BOUNDARY.md`
5. `MEMORY_MAP.md`
6. `SESSION_CARD.md`
7. `BRAIN.md`
8. `WORKFLOW_SEPARATION.md`
9. `CONSERVATIVE_OPERATION_LOOP.md`
10. `FINAL_GOAL_LOCK.md`
11. `EXTERNAL_RESEARCH_RULE.md`
12. `WORKING_BEHAVIOR_CONTRACT.md`
13. `CRITICAL_RISK_SCAN.md`
14. `AI_PATCH_TRUST_RULE.md`
15. `DEPENDENCY_GATE.md`
16. `SECURITY_GATE.md`
17. `UNTRUSTED_CONTENT_RULE.md`
18. `MAINTAINABILITY_RULE.md`
19. `DATA_SAFETY_RULE.md`
20. `ROLLBACK_RULE.md`
21. `ENVIRONMENT_CONTRACT.md`
22. `MODE_REGISTRY.md`
23. `FUNCTION_PACKS.md`
24. `DECISION_TABLES.md`
25. `SOURCE_BINDINGS.md`
26. `OUTPUT_CONTRACT.md`
27. `AGENTS/AGENT_SPEC.md`
28. `AGENTS/SEQUENCE_RULE.md`
29. `AGENTS/ACTIVE/README.md`
30. `ACCEPTANCE_TESTS.md`
31. `TASKS/PREFLIGHT_RESULT.md`
32. `TASKS/CURRENT_TASK.md`

## use when

```text
single_repo_or_project:true
task_bounded:true
roles_can_run_sequentially:true
multi_thread_overhead_not_worth_it:true
verification_gate_required:true
conservative_operation_loop_required:true
```

## do not use when

```text
large_multi_surface_project:true
parallel_sub_brain_threads_needed:true
long_running_project_management:true
independent_frontend_backend_design_review_needed:true
```

Use `Coding_Meta_Brain` for multi-thread coding case workspaces.

## launch phrase

```text
코딩 TOML 에이전트 브레인 부팅해.
```

- 완료/검증/공개 가능/경계 판단 전에는 필요할 때만 `CONTEXT_REHYDRATION_BINDING.md`를 읽는다.
