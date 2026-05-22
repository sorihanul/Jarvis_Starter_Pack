# Basic Function Workspace START HERE

## Identity
This folder is the active workspace for the AILO basic function common layer.

Basic function is the common control layer.
Cognitive function is the meaning expansion layer.

## Read order
1. `MAP.md`
2. `DEVELOPMENT_LOG.md`
3. `BASIC_FUNCTION_CONTRACT_v0_1.md`
4. `BASIC_FUNCTIONIZATION_PRINCIPLES_v0_1.md`
5. `BASIC_FUNCTION_INDEX_v0_1.md`
6. `BASIC_FUNCTION_INDEX_v0_2.md`
7. `BASIC_FUNCTION_CARDS_v0_1.md`
8. `BASIC_FUNCTION_SKILL_SKELETON_SERIES_v0_2.md`
9. `SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md`
10. `SKILL_SKELETON_OVERLAP_REVIEW_v0_1.md`
11. `SKILL_SKELETON_FAILURE_CONSISTENCY_REVIEW_v0_1.md`
12. `BASIC_FUNCTION_USE_ORDER_v0_1.md`
13. `BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md`
14. `BASIC_FUNCTION_TEST_FIXTURES_v0_1.md`
15. `BASIC_FUNCTION_NEGATIVE_FIXTURES_v0_1.md`
16. `BASIC_FUNCTION_REAL_TASK_FIXTURES_v0_1.md`
17. `BASIC_FUNCTION_ACCEPTANCE_CHECK_v0_1.md`
18. `BASIC_FUNCTION_PROOF_REPORT_v0_1.md`
19. `BASIC_FUNCTION_QUALITY_REVIEW_v0_1.md`
20. `BASIC_FUNCTION_STABLE_LOCK_v0_1.md`

## Scope
This folder owns only basic functions.

It may define:
- function contract
- function index
- function cards
- fixtures
- acceptance checks
- development log

It must not define:
- cognitive functions
- engines
- OS runtime
- brain identity
- domain reasoning

## Current proof result
The v0.1 basic function set is locked as a stable document-level callable function specification.

```text
scope_lock
route_lock
missing_slot_detect
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

The proof target is stable control behavior:

```text
same input shape
-> same function route
-> same output schema
-> same trace shape
```

Current result:

```text
PASS_STABLE
```

## Current expansion

The v0.2 skill-skeleton series is implemented as stable-candidate basic functions.

It is not final stable yet.

```text
input_contract_bind
step_sequence_lock
acceptance_criteria_bind
fixture_contract_bind
handoff_packet_bind
retry_policy_check
cost_budget_lock
dependency_check
```

Current review:

```text
SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md
SKILL_SKELETON_OVERLAP_REVIEW_v0_1.md
SKILL_SKELETON_FAILURE_CONSISTENCY_REVIEW_v0_1.md
```

## One-line rule
The common layer is stable; future growth must pass the candidate gate.
