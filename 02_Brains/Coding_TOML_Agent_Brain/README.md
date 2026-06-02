# Coding TOML Agent Brain

## purpose

`Coding_TOML_Agent_Brain` is an experimental single-thread coding harness.

It keeps one main conversation, but can draft temporary TOML role-agent contracts when a bounded coding task benefits from explicit design, implementation, verification, or release roles.

## status

```text
experimental_static_ready:true
runtime_validated:false
reference_ready:false
stable_ready:false
```

This brain can be read and tested as a public document harness, but it should not be described as a validated coding runtime yet.

## use when

```text
single repo or project
bounded coding task
sequential role checkpoints are enough
multi-thread coordination is too heavy
verification gate is still required
```

## do not use when

```text
large multi-surface project
parallel sub-brain threads needed
long-running project management
independent frontend/backend/design review needed
```

For larger role-split coding work, use `Coding_Meta_Brain`.

## start here

Read `START_HERE.md` first.

For an actual boot, use:

```text
코딩 TOML 에이전트 브레인 부팅해.
```

## TOML rule

Temporary role agents should be TOML files.

Candidate examples live in:

```text
AGENTS/CANDIDATES/
```

Active task agents, if created during a real task, belong in:

```text
AGENTS/ACTIVE/
```

## operating shape

This brain separates:

```text
task intake
final goal lock
agent need decision
sequential TOML role contracts
implementation checkpoint
verification gate
release boundary
memory export candidate
```

## boundaries

- Do not create agents by default.
- Do not create an agent without role, inputs, outputs, and stop conditions.
- Do not let an implementation agent approve its own work.
- Do not publish operational files as project output.
- Do not call this stable until real solo-thread coding task evidence exists.

## main files

- `START_HERE.md`: human and agent entry point.
- `BOOT.md`: boot contract.
- `BRAIN.md`: identity and non-definition.
- `AGENTS/AGENT_SPEC.md`: TOML role-agent schema.
- `AGENTS/SEQUENCE_RULE.md`: sequential agent execution rule.
- `FUNCTION_PACKS.md`: coding operation packs.
- `REPORTS/`: verification, final report, decision trace, and runbook surfaces.

