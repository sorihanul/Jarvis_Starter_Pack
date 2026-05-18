# Validation Rule

The lens pass is valid only if it changes or confirms the task in a useful way.

## Pass Conditions

```text
active_lens_named:
why_this_lens_clear:
first_focus_clear:
do_not_expand_clear:
skill_boundary_clear:
result_changed_or_confirmed:
return_to_main_task_clear:
```

## Fail Conditions

```text
the lens is just a fancy name
the answer becomes longer but not clearer
the skill boundary is missing
the task turns into roleplay
the lens opens unrelated systems
the result does not return to the user's goal
```

## Recheck Question

Ask:

```text
Did this lens make the next action narrower, safer, or easier to judge?
```

If the answer is no, remove the lens pass.
