# Worked Examples v0.1

This document shows one complete example of turning a user request into host custom-agent files and a parent-session launch brief.

It is an example surface.
It is not a live project configuration.

## Example 1. Code Review Subagent Set

### User Request

```text
In this project, prepare a host subagent set for code review.
Keep it safe and practical.
```

### Interpretation

```text
target_project:
  current trusted project

task_shape:
  review-first

write_mode:
  draft_only unless the user asks to create files

selected_role_set:
  research
  validation
  security_gate

reason:
  research gathers evidence
  validation checks behavior and tests
  security_gate checks unsafe commands, secrets, and trust boundaries

parent_session_role:
  integrate results and make final judgement
```

### Files To Create If Approved

Create these files in the target project:

```text
<target_project>/host_agent_examples/agents/research.toml
<target_project>/host_agent_examples/agents/validation.toml
<target_project>/host_agent_examples/agents/security-gate.toml
```

Optional project config:

```text
<target_project>/host_runtime_config.toml
```

Do not create live role files inside `01_Source_Pack`.

### Optional Project Config

Use this only when the project does not already have an agent config.

```toml
[agents]
max_threads = 3
max_depth = 1
```

### `research.toml`

```toml
name = "research"
description = "Read-only researcher for code review evidence, file paths, and project rules."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in research mode.
Map the relevant files, execution path, tests, and project rules.
Return only facts, file paths, evidence, and open questions.
Do not edit files.
Do not make final review decisions.
"""
```

### `validation.toml`

```toml
name = "validation"
description = "Read-only validator for behavior, tests, contracts, and residual risks."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in validation mode.
Check the target against the stated success criteria.
Look for behavioral regressions, missing tests, contract failures, and unverified assumptions.
Return pass/fail, concrete findings, and residual risks.
Do not implement fixes unless the parent session explicitly asks.
"""
```

### `security-gate.toml`

```toml
name = "security_gate"
description = "Read-only security gate for secrets, unsafe commands, trust boundaries, and risky data flow."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in security gate mode.
Check for secret exposure, unsafe commands, untrusted input risks, destructive file operations, and policy-sensitive leakage.
Return allow, warn, block, or escalate with evidence.
Do not silently approve risky content.
Do not edit files.
"""
```

### Parent-Session Launch Brief

Use this after the role files exist, or use it as a delegation prompt in a 호스트 작업 환경 session that supports subagents.

```text
Review this project target with a split role set.

Target:
- <describe branch, folder, PR, patch, or files>

Success criteria:
- Find real correctness, security, regression, and test risks.
- Avoid style-only findings unless they hide a real bug.
- Keep the parent session as final integrator.

research:
- Map relevant files, execution path, tests, and project rules.
- Return facts, paths, evidence, and open questions.
- Do not edit files.
- Do not make final review decisions.

validation:
- Check behavior against the success criteria.
- Find regressions, missing tests, contract failures, and unverified assumptions.
- Return findings by severity with evidence.
- Do not implement fixes unless explicitly asked.

security_gate:
- Check for secrets, unsafe commands, untrusted input, destructive operations, and trust-boundary failures.
- Return allow, warn, block, or escalate with evidence.
- Do not edit files.

Parent session:
- Integrate the role outputs.
- Report findings first, ordered by severity.
- If no blocking findings exist, say so and list residual risks.
- Do not create broad refactors during review.
```

### Expected Final Report Shape

```text
Findings:
- severity:
  file:
  evidence:
  impact:
  recommended fix:

No Findings:
- state explicitly if no blocking findings were found

Residual Risks:
- unverified tests:
- unchecked external behavior:
- assumptions:

Next Action:
- fix now / add test / accept risk / no action
```

### Pass Check

```text
role_set_is_small:
one_toml_file_per_role:
all_roles_are_read_only:
parent_session_integrates:
no_live_files_created_in_source_pack:
no_fake_hierarchical_toml_keys:
```

### Common Mistakes

Do not do this:

```text
Create one giant reviewer.toml that researches, fixes, validates, and approves everything.
```

Do not do this:

```text
Put pack, stack, router, or loop as fake official TOML fields.
```

Do this instead:

```text
Keep TOML narrow.
Put role order and integration rules in the parent launch brief.
```

## Minimal Variant

If the review is small, use only:

```text
validation
```

If the review involves unfamiliar code paths, use:

```text
research
validation
```

If the review involves external input, secrets, shell commands, auth, plugins, or deployment, use:

```text
research
validation
security_gate
```

## One Line Rule

The TOML files define narrow roles; the parent launch brief defines how those roles work together.
