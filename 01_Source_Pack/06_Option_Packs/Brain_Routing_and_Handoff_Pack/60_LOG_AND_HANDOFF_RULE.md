# 60 Log And Handoff Rule

## Log Separation

Do not create heavy logs for every small route decision.

Recommended surfaces:

```text
ROUTE_LOG.md:
  route choices, switches, return states

HANDOFFS/:
  launch prompts for separate threads

INTEGRATION_NOTES.md:
  final comparison and synthesis when several outputs return
```

## Route Log

```text
time:
request:
selected_route:
mode:
why_selected:
expected_output:
return_state:
```

## Handoff Prompt

Use a handoff when another thread must boot a target brain.

```text
target_brain:
entry_files_to_read:
task:
scope:
do_not_touch:
expected_output:
return_format:
```

## Anti-Noise Rule

If the route is obvious and same-thread, a short `ACTIVE_BRAIN_ROUTE.md` update is enough.

Create a separate handoff file only when another thread or owner must receive it.
