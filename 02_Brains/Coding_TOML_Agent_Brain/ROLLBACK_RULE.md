# Rollback Rule

## rule

Every coding task needs a recovery path when changes go wrong.

## minimum rollback surfaces

```text
changed_files_list:
git_diff_or_file_copy_available:
data_backup_needed:
rollback_steps:
cannot_rollback_warning:
```

## stop condition

If the task can destroy data or break a working system and there is no rollback path, stop before implementation.
