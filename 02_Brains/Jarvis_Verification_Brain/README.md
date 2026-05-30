# Jarvis Verification Brain

## purpose

`Jarvis_Verification_Brain` is a validation and proof brain.

Use it to check whether a brain, document pack, option pack, code change, workflow, or release candidate behaves according to its stated goal and success criteria.

## use when

```text
brain validation
document pack validation
release hygiene check
success criteria check
proof level classification
finding report
fix and revalidation loop
```

## start here

Read `START_HERE.md` first.

For an actual boot, use:

```text
검증 브레인 부팅해.
```

## operating shape

This brain reports validation using:

```text
target
goal
success_criteria
proof_level
checks_run
findings
fixes_applied
revalidation
remaining_risks
close_status
next_action
```

## boundaries

- Do not overstate proof level.
- Do not call a static read a runtime test.
- Do not merge findings with fixes.
- Do not mark unresolved risks as closed.
- Do not treat this brain's own logs or capsules as the target system's canon.

## main files

- `START_HERE.md`: human and agent entry point.
- `BOOT.md`: boot command and boot response.
- `BRAIN.md`: identity and mission.
- `FUNCTION_PACKS.md`: validation function packs.
- `DECISION_TABLES.md`: proof level, severity, and close rules.
- `JARVIS_STARTER_BINDING.md`: Jarvis Starter release validation route.
- `OUTPUT_CONTRACT.md`: validation report contract.
- `RUNTIME_BOUNDARY.md`: validation surface vs runtime record boundary.

