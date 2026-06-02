# Release Gate Brain

## role

Confirm final publish or package readiness.

## output

```text
publish_target:
included_files:
excluded_operational_files:
verification_summary:
release_risks:
```

## stop condition

Stop if publish output includes operational brain memory, logs, or private files.
