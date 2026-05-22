# TOML Subagent Build Call v0.1

This document is the build call surface for host custom-agent TOML files.

It does not make Jarvis Starter a multi-agent runtime by default.

It tells Jarvis when and how to prepare narrow host subagent role files for a target project.

## 1. When To Use

Use this surface only when the user asks for one of these:

- host subagent roles
- `host_agent_examples/agents/*.toml` files
- a research / implementation / validation / synthesis role set
- a project-specific agent roster
- role files for a larger task that benefits from split work

Do not use this surface for:

- a short answer
- a single-file small edit
- a normal brain design request
- a task that only needs an `AGENTS.md` project rule

## 2. Input Contract

If the user does not provide all fields, infer the smallest safe defaults.

```txt
target_project:
  Project folder where the TOML files should be used.
  Default: current trusted project, if clear.

requested_roles:
  Role names requested by the user.
  Default: choose from research, implementation, validation, synthesis, security_gate, writing.

task_shape:
  What kind of work the agents must support.
  Default: infer from the user request.

write_mode:
  draft_only | create_files
  Default: draft_only unless the user clearly asks to create files in a writable project.

allowed_write_root:
  Folder where files may be created.
  Default: target_project/host_agent_examples/agents when create_files is allowed.

special_limits:
  Any no-edit, no-network, no-secret, or read-only constraints.
  Default: no extra limits beyond Jarvis Starter rules.
```

## 3. Read Order

Read only the needed files.

1. `README.md`
2. `10_HOST_AGENT_UTILIZATION_v0.1.md`
3. `20_SUBAGENT_BRIEF_TEMPLATE_v0.1.md`
4. `60_HOST_STANDARD_ROLES_v0.1.md`
5. `80_HOST_SUBAGENT_BRIDGE_LITE_v0.1.md`
6. `90_ROLE_SET_LAUNCH_BRIEFS_v0.1.md`
7. `95_WORKED_EXAMPLES_v0.1.md`, only if a complete example is needed
8. `host_agent_examples/agents/*.toml.example`
9. `roles/*.toml`, only if a local fragment example is needed

Do not read the whole source pack.

## 4. Output Contract

Always return or create three things.

### A. Role Selection

```txt
selected_roles:
  - role_name:
      reason:
      sandbox:
      expected_output:
```

### B. TOML Agent Files

Use standalone custom-agent files as the default distributable-safe form.

Do not encode Jarvis hierarchy directly into TOML.

Use TOML for one executable role.
Use the subagent brief for role-set order, pack/stack meaning, and handoff.

Recommended target:

```txt
host_agent_examples/agents/<role-name>.toml
```

Minimal TOML shape:

```toml
name = "research"
description = "Read-only explorer for docs, code paths, and project structure."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in the assigned role.
Keep the scope narrow.
Return only facts, file paths, changed files, risks, or requested output.
Do not take over final integration judgment.
"""
```

### C. Subagent Brief

For each role, provide a short brief using `20_SUBAGENT_BRIEF_TEMPLATE_v0.1.md`.

```txt
role:
goal:
scope:
output:
forbidden:
notes:
```

### D. Parent Launch Brief

When two or more roles are selected, provide one parent-session launch brief.

Use `90_ROLE_SET_LAUNCH_BRIEFS_v0.1.md` when a standard pattern matches.

Use `95_WORKED_EXAMPLES_v0.1.md` when the user needs a concrete end-to-end example before applying the pattern.

## 5. Standard Role Defaults

### research

- sandbox: `read-only`
- use when: route finding, source reading, repo inspection, source comparison
- output: facts, file paths, evidence, risks
- forbidden: edits, final design authority

### implementation

- sandbox: `workspace-write`
- use when: bounded file edits are needed
- output: changed files, implementation notes, verification commands
- forbidden: broad refactor, strategy takeover

### validation

- sandbox: `read-only`
- use when: tests, contract checks, acceptance review, residual risk
- output: pass/fail, findings, remaining risks
- forbidden: implementing fixes unless separately asked

### synthesis

- sandbox: `read-only`
- use when: multiple outputs must be merged
- output: final integrated summary or report draft
- forbidden: inventing missing evidence

### security_gate

- sandbox: `read-only`
- use when: secrets, commands, external input, risky file operations
- output: allow / block / escalate with reason
- forbidden: executing risky operations

### writing

- sandbox: `workspace-write` only when edits are clearly requested
- use when: documents, prompts, user-facing prose, rewrite passes
- output: draft or changed files
- forbidden: changing facts or scope without saying so

## 6. File Creation Rule

If `write_mode = create_files`, create files only under:

```txt
<target_project>/host_agent_examples/agents/
```

Do not create generated TOML files inside `01_Source_Pack`.

`01_Source_Pack` contains examples and rules.

The target project contains the actual working agents.

## 7. Verification

After drafting or creating the role set, check:

- each role has one clear purpose
- each role has a narrow sandbox
- each role has a bounded output
- hierarchy is expressed in a brief, not fake TOML keys
- implementation roles name their writable scope
- validation roles do not take over implementation
- source-pack files were not used as a work log
- the user receives a copyable launch or delegation brief

## 8. One Line Rule

`Jarvis selects the smallest useful role set, writes TOML only for the target project, and keeps the main session as the integrator.`
