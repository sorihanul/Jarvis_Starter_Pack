# 50 Active Route And Return

## Active Route Surface

`ACTIVE_BRAIN_ROUTE.md` shows which brain route is being used now.

Minimum shape:

```text
active_route:
target_brain:
mode:
  same_thread_lens | separate_thread_handoff | integration_only
selected_at:
selected_by:
active_task:
selection_reason:
entry_files:
expected_output:
return_condition:
```

## Return Rule

Every route must return to final integration.

```text
same-thread lens completes work
or separate thread returns output
-> main brain reads result
-> main brain accepts, rejects, or requests another pass
-> main brain closes or reroutes
```

## Switch Record

```text
from_route:
to_route:
reason:
task:
expected_output:
return_condition:
accepted_by_main_brain:
```

## Failure State

Fail if:

```text
active route is unknown
entry files are not declared
handoff has no return condition
final integration step is skipped
```
