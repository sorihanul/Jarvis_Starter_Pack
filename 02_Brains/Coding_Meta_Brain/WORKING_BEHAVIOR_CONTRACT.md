# Working Behavior Contract

## priority

Proper working behavior is the top success criterion.

Clean code, clever architecture, or elegant abstractions are secondary to the owner-visible behavior actually working.

## contract schema

```text
primary_user_flow:
expected_result:
data_behavior:
failure_behavior:
must_not_break:
first_version_scope:
owner_visible_done_condition:
verification_method:
evidence_required:
```

## rule

If the behavior contract is unclear, do not enter implementation.

If implementation works technically but fails the behavior contract, the task is not done.

Use `BEHAVIOR_VERIFICATION_LOOP.md` to close the conservative behavior loop:

```text
purpose -> working behavior -> problem check -> cause location -> minimal fix -> reverification -> maintainability
```
