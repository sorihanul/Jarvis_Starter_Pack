# Data Safety Rule

## rule

Data loss is a critical failure.

Before operations that delete, overwrite, migrate, import, sync, or transform user data, stop and require explicit approval or a safe backup plan.

## risky data actions

```text
delete
overwrite
migration
bulk_import
bulk_update
schema_change
sync
deduplicate
cache_clear
```

## required output

```text
data_at_risk:
backup_or_rollback_available:
destructive_action:
owner_approval_required:
safe_test_plan:
```
