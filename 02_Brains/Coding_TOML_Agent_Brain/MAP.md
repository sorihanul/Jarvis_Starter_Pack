# Coding TOML Agent Brain Map

## purpose

This folder is a self-contained experimental template for single-thread coding tasks.

The brain creates TOML role agents only when needed, keeps them inside `AGENTS/ACTIVE/`, runs them sequentially, verifies the work, and exports reusable lessons at closeout.

## top-level surfaces

```text
START_HERE.md
BOOT.md
MAP.md
LOCAL_RULEBOOK.md
RUNTIME_BOUNDARY.md
MEMORY_MAP.md
SESSION_CARD.md
BRAIN.md
WORKFLOW_SEPARATION.md
FINAL_GOAL_LOCK.md
EXTERNAL_RESEARCH_RULE.md
WORKING_BEHAVIOR_CONTRACT.md
CRITICAL_RISK_SCAN.md
AI_PATCH_TRUST_RULE.md
DEPENDENCY_GATE.md
SECURITY_GATE.md
UNTRUSTED_CONTENT_RULE.md
MAINTAINABILITY_RULE.md
DATA_SAFETY_RULE.md
ROLLBACK_RULE.md
ENVIRONMENT_CONTRACT.md
MODE_REGISTRY.md
FUNCTION_PACKS.md
DECISION_TABLES.md
SOURCE_BINDINGS.md
OUTPUT_CONTRACT.md
ACCEPTANCE_TESTS.md
```

## work surfaces

```text
AGENTS/
TASKS/
MEMORY/
REPORTS/
LOGS/
CAPSULES/
01_PROJECT/
02_RELEASE/
```

## publish boundary

```text
publish_target: 01_PROJECT/
do_not_publish_by_default:
  AGENTS/
  TASKS/
  MEMORY/
  REPORTS/
  LOGS/
  CAPSULES/
  02_RELEASE/
```

## agent surfaces

```text
AGENTS/AGENT_SPEC.md
AGENTS/SEQUENCE_RULE.md
AGENTS/ACTIVE/
AGENTS/CANDIDATES/
AGENTS/ARCHIVE/
```

## workflow separation

`WORKFLOW_SEPARATION.md` is the core rule for this brain.
Design, implementation, and verification stay in one thread, but they must be represented as separate role contracts or explicit stages.
