# Host Subagent Bridge Lite v0.1

This document explains how Jarvis Starter uses host custom agents without turning the starter into a heavy multi-agent runtime.

## 1. Identity

Jarvis Starter remains a document-based harness.

host custom-agents are optional project-level role files.

Use them only when a task benefits from split roles.

## 2. Host Custom-Agent Floor

Use the host custom-agent shape as the execution format.

Project-scoped custom agents should be prepared as:

```text
host_agent_examples/agents/<agent-name>.toml
```

Each file should define one narrow role.

Minimum fields:

```toml
name = "research"
description = "Read-only researcher for project files, docs, and evidence."
developer_instructions = """
Stay in research mode.
Return facts, paths, evidence, and risks.
Do not edit files.
"""
```

Common optional fields:

```toml
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
nickname_candidates = ["Atlas", "Delta"]
```

## 3. What Jarvis Adds

Jarvis does not change the official TOML schema.

Jarvis adds role planning before TOML creation:

```text
user request
-> decide whether subagents are useful
-> choose the smallest useful role set
-> write one TOML file per executable role
-> keep the parent session as the integrator
```

## 4. Hierarchy Rule

Host custom-agent TOML does not directly represent a full hierarchy.

Keep hierarchy outside the TOML file.

Use:

```text
role set
launch brief
handoff contract
acceptance checklist
```

Do not use:

```text
one giant hierarchical TOML file
```

## 5. Distributable Role Mapping

Use this simple mapping for distributable Jarvis Starter usage.

| Need | Distributable role form |
| --- | --- |
| source reading | `research.toml` |
| bounded file edits | `implementation.toml` |
| tests and acceptance checks | `validation.toml` |
| final merge of outputs | `synthesis.toml` |
| risky commands or secrets | `security-gate.toml` |
| writing and document work | `writing.toml` |

## 6. Pack / Stack Translation

Jarvis may speak about role sets, packs, or stacks.

Translate them like this:

```text
pack -> several role files selected together
stack -> ordered role files plus a handoff brief
router -> parent-session rule for choosing the role set
loop -> acceptance test or verification checklist
```

Do not create fake TOML keys for these concepts.

## 7. Sample Role Sets

### Code Review

```text
research
validation
security_gate
```

### Bounded Implementation

```text
research
implementation
validation
```

### Documentation Rewrite

```text
research
writing
validation
```

### External Source Intake

```text
research
security_gate
synthesis
```

### Release Check

```text
validation
security_gate
synthesis
```

## 8. File Placement Rule

Template and example files may live in this module.

Actual working files must be created in the target project:

```text
<target_project>/host_agent_examples/agents/
```

Do not create live project agents inside `01_Source_Pack`.

## 9. Use With Build Call

When the user asks Jarvis to create host subagents, use:

```text
70_TOML_SUBAGENT_BUILD_CALL_v0.1.md
```

This Lite bridge explains the conversion principle.
The build call gives the actual input and output contract.

When the user needs a ready delegation prompt, use:

```text
90_ROLE_SET_LAUNCH_BRIEFS_v0.1.md
```

That file gives copyable parent-session launch briefs for common role sets.

When the user needs to see a full example, use:

```text
95_WORKED_EXAMPLES_v0.1.md
```

That file shows how one user request becomes role selection, TOML drafts, and a parent launch brief.

## 10. Pass Conditions

Before closing the task, check:

```text
one_file_per_role:
official_schema_shape:
smallest_useful_role_set:
target_project_agents_folder:
parent_session_integrates:
source_pack_not_mutated_with_live_agents:
launch_brief_when_multiple_roles:
```

## One Line Rule

Jarvis plans the role set; Host TOML executes one narrow role at a time.
