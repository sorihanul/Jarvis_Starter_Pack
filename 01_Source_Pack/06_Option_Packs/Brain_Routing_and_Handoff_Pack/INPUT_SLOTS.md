# Input Slots

## Required

```text
target_system:
user_goal:
available_brain_routes:
route_mode:
final_integration_owner:
```

## Boundary

```text
writable_surfaces:
read_only_surfaces:
handoff_needed:
integration_needed:
```

## Optional

```text
target_brain:
entry_files:
handoff_prompt_needed:
returned_output_contract:
route_log_needed:
```

## Slot Meaning

```text
target_system:
  The system or workspace being worked on.

user_goal:
  The actual user request.

available_brain_routes:
  Brain documents or brain families that may be read or handed off to.

route_mode:
  same_thread_lens, separate_thread_handoff, or integration_only.

final_integration_owner:
  The brain or thread that produces the final answer.

writable_surfaces:
  Where route logs, handoffs, and integration notes may be written.

read_only_surfaces:
  What may be inspected but not modified.

handoff_needed:
  Whether another thread must receive a launch prompt.

integration_needed:
  Whether returned outputs must be synthesized before final answer.
```
