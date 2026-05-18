# Host Workspace Use

## Same Thread

Use same-thread switching when the work is small.

```text
1. intake lens
2. implement lens
3. verify lens
4. release lens
```

This is the default.

## Separate Thread

Use separate-thread handoff when:

```text
the task is large
the review must be independent
the write scope should be isolated
the parent thread should keep design control
```

The parent thread writes the handoff prompt.
The child thread works inside the assigned scope.
The parent thread integrates the result.

## Subagent Reality Check

Do not promise automatic subagents unless the host tool actually provides them.

If the host supports subagents, this pack can generate the role prompt.
If the host does not, the same prompt can be pasted into another thread.

## Practical Default

```text
simple coding task:
  same thread lens switching

medium risky task:
  same thread implement + separate review handoff

large task:
  split into implementation handoff packets
```
