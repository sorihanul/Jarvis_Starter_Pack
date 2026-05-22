# Input Slots

Use these slots before switching lenses.

```text
task_goal:
current_material:
current_problem:
requested_lens:
default_lens:
must_not_expand:
skill_needed:
expected_output:
stop_condition:
```

## Slot Meanings

```text
task_goal:
  what the user is trying to get done

current_material:
  file, text, idea, plan, result, or decision being examined

current_problem:
  why the current view is not enough

requested_lens:
  lens explicitly requested by the user, if any

default_lens:
  lens Jarvis chooses if the user did not name one

must_not_expand:
  things this lens must not turn into

skill_needed:
  whether a skill or option pack is needed after the lens is selected

expected_output:
  what must be returned after the lens pass

stop_condition:
  when to return to the main task
```

## Minimal Packet

```text
task_goal:
active_lens:
why_this_lens:
first_focus:
do_not_expand:
output:
```
