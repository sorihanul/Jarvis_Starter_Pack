# 15 Brain Lens Concept

## Purpose

Define the safe concept behind this pack.

The useful idea is not a meta brain that controls other brains.
The useful idea is a temporary working lens.

## Definition

```text
brain_lens:
  a bounded way for the current thread to read another brain's entry rules
  and apply those rules only to the current task
```

This may also be called a possession-style brain in Korean.
Use `brain lens` in beginner-facing writing because it is clearer and less
likely to suggest hidden control.

## What Actually Happens

```text
1. identify the task
2. choose a relevant brain lens
3. read the minimum entry files for that brain
4. apply that lens to the current task
5. return to the main brain before final judgment
```

If the work is too large for the current thread:

```text
1. write a launch prompt
2. another thread boots the target brain
3. the target thread returns a bounded result
4. the main thread integrates the result
```

## What Does Not Happen

```text
no remote control
no automatic sub-brain operation
no hidden delegation
no permanent identity change
no claim that the parent brain owns the child brain
```

## Why This Is Safer Than Meta Brain Language

`meta brain` can imply a control hierarchy.

That is not how document-based Jarvis or subagent workflows work.

The main thread can:

```text
read:
  open another brain's entry surface

apply:
  temporarily use its rules as a lens

handoff:
  write a launch prompt for another thread

integrate:
  judge returned output before final answer
```

The main thread cannot:

```text
possess another running thread
force another brain to act
make sub-brains run without an explicit launch
skip integration after returned output
```

## Use Cases

```text
writing:
  apply a style or correction brain briefly

verification:
  apply a verification lens before accepting output

research:
  hand off source gathering to a research thread

coding:
  route exploration, implementation, review, or release-gate roles

memory:
  send candidate memory notes to a canonization or route-building lens
```

## Risk Control

The lens must always be bounded.

```text
lens_name:
entry_files:
task_scope:
do_not_touch:
return_condition:
exit_rule:
```

If these fields cannot be filled, do not use the lens.

## One-Line Rule

```text
Use brain lens language for temporary rule application.
Use handoff language for separate threads.
Do not use control language.
```
