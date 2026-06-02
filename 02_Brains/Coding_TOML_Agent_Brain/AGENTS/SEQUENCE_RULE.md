# Agent Sequence Rule

## rule

Active TOML agents run sequentially in one thread.

## default order

```text
design_checkpoint
repo_intake
scope_patch
implementation
implementation_checkpoint
verification
release_check
closeout
```

## sequencing constraints

```text
verification_after_code_change:true
release_after_verification:true
memory_export_after_closeout:true
archive_agents_at_closeout:true
```

## escalation

If two agents require independent concurrent work, stop and route to `Coding_Meta_Brain`.
