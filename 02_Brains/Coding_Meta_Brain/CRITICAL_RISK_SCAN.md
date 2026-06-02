# Critical Risk Scan

## rule

Scan serious coding risks before implementation.

The owner does not need to know security engineering.
The brain must detect risk and ask only for owner-level decisions when needed.

## risk flags

```text
auth
payment
personal_data
secrets
file_upload
database_migration
data_delete_or_overwrite
external_dependency
public_deploy
prompt_injection
destructive_action
production_access
```

## levels

```text
low:
  proceed with normal verification
medium:
  strengthen verification gate
high:
  explain risk in plain language and request approval or simplification
blocked:
  stop and propose safer scope
```

## output

```text
risk_level:
risk_flags:
plain_language_risk:
safe_simplification:
owner_decision_required:
verification_required:
```
