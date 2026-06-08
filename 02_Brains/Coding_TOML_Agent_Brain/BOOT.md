# Coding TOML Agent Brain BOOT

## boot contract

When booted, this brain must run as a single-thread coding harness.

It must decide whether the task can remain in one thread.
If yes, it may draft one or more TOML role agents in `AGENTS/ACTIVE/` and execute their roles sequentially in the same conversation.

## default boot flow

This is a full boot flow, not a fast boot.
Read order should stay aligned with `START_HERE.md`.

```text
read START_HERE
read MAP
read LOCAL_RULEBOOK
read RUNTIME_BOUNDARY
read MEMORY_MAP
read SESSION_CARD
read BRAIN
read WORKFLOW_SEPARATION
read FINAL_GOAL_LOCK
read EXTERNAL_RESEARCH_RULE
read WORKING_BEHAVIOR_CONTRACT
read CRITICAL_RISK_SCAN
read AI_PATCH_TRUST_RULE
read DEPENDENCY_GATE
read SECURITY_GATE
read UNTRUSTED_CONTENT_RULE
read MAINTAINABILITY_RULE
read DATA_SAFETY_RULE
read ROLLBACK_RULE
read ENVIRONMENT_CONTRACT
read MODE_REGISTRY
read FUNCTION_PACKS
read DECISION_TABLES
read SOURCE_BINDINGS
read OUTPUT_CONTRACT
read AGENTS/AGENT_SPEC
read AGENTS/SEQUENCE_RULE
read AGENTS/ACTIVE/README
read ACCEPTANCE_TESTS
read TASKS/PREFLIGHT_RESULT
inspect TASKS/CURRENT_TASK
```

## first response after boot

Report:

```text
brain: Coding_TOML_Agent_Brain
status: experimental
thread_model: single_thread
active_agents: none
project_surface: 01_PROJECT/
next_needed: bounded coding task or target project
```

## context rehydration trigger

완료, 검증, 공개 가능, 경계 판단, 또는 `runtime_validated` 같은 강한 상태를 말하기 전에는 필요할 때만 `CONTEXT_REHYDRATION_BINDING.md`를 읽는다.
