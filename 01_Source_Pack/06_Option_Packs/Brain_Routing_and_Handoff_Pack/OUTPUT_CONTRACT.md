# Output Contract

## Minimum Decision Output

Every use must make the route decision visible.

```text
selected_route:
mode:
entry_files:
expected_output:
return_condition:
final_integration_owner:
```

## Durable Outputs When Needed

```text
BRAIN_ROUTE_REGISTRY.md
ACTIVE_BRAIN_ROUTE.md
ROUTE_LOG.md
```

Use durable files only when the route is active, repeated, non-obvious, handed off to another thread, or used for later integration.

## Optional Outputs

```text
HANDOFFS/<task_id>.md
INTEGRATION_NOTES.md
```

## Route Decision Shape

```text
target:
user_goal:
selected_route:
target_brain:
mode:
why_selected:
entry_files:
expected_output:
return_condition:
not_selected:
```

## Handoff Shape

```text
target_brain:
entry_files_to_read:
task:
scope:
do_not_touch:
expected_output:
return_format:
```

## Integration Report Shape

```text
target:
user_goal:
inputs_integrated:
accepted_outputs:
rejected_outputs:
conflicts:
final_decision:
remaining_risks:
next_action:
```
