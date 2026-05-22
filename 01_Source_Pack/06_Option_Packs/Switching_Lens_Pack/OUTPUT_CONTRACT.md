# Output Contract

Use this format when a visible lens decision is useful.

```text
task_goal:
active_lens:
why_this_lens:
first_focus:
do_not_expand:
skill_or_pack_needed:
result:
return_to_main_task:
remaining_risk:
```

For simple work, compress to:

```text
active_lens:
result:
next_action:
```

Do not expose this contract when the user only needs the final answer.

Use the contract when:

```text
the user is designing a system
the lens choice matters
the answer must be audited later
the work will be handed off
```
