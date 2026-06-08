# Coding Meta Brain Map

## purpose

This folder is a self-contained experimental template for one coding case.

The brain operation surfaces, sub-brain library, thread contracts, memory export, project surface, and release surface live inside this folder.

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
TASKS/
THREADS/
SUB_BRAINS_LIBRARY/
AGENTS/
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
  START_HERE.md
  BOOT.md
  TASKS/
  THREADS/
  SUB_BRAINS_LIBRARY/
  AGENTS/
  MEMORY/
  REPORTS/
  LOGS/
  CAPSULES/
```

## included sub-brain library

The library is a selectable set, not an active roster.

```text
SUB_BRAINS_LIBRARY/Repo_Intake_Brain/
SUB_BRAINS_LIBRARY/Frontend_Brain/
SUB_BRAINS_LIBRARY/Backend_Brain/
SUB_BRAINS_LIBRARY/Design_Brain/
SUB_BRAINS_LIBRARY/Integration_Brain/
SUB_BRAINS_LIBRARY/Verification_Brain/
SUB_BRAINS_LIBRARY/Release_Gate_Brain/
```

## workflow separation

`WORKFLOW_SEPARATION.md` is the core rule for this brain.
Design, implementation, and verification may happen in one case workspace, but they must not collapse into one unverified narrative.

## context rehydration

`CONTEXT_REHYDRATION_BINDING.md` links this brain to the root v3 no-false-completion and claim-ceiling rule. It is read on trigger, not as mandatory startup bulk.
