# 10 Concept

## Definition

Brain Routing and Handoff is a practical operating pattern.

It does not assume that one brain can control another brain.

The safer core concept is `brain lens`.
A brain lens means the current thread temporarily reads and applies another
brain's entry rules for one bounded task.

For details, read `15_BRAIN_LENS_CONCEPT.md`.

It assumes only three possible actions:

```text
read:
  open another brain's entry files and apply them in the current thread

handoff:
  write a launch prompt so another thread can work as that brain

integrate:
  read the returned output and make the final combined judgment
```

## Core Question

Use this method only when choosing or handing off to another brain is the real problem.

```text
Which brain should be read?
Can this be handled in the same thread?
Does this need a separate thread?
What should the handoff say?
Who integrates the returned output?
```

## Anti-Misunderstanding Rule

Avoid these expressions:

```text
control a sub-brain
operate another brain directly
remote-control a brain
make sub-brains run automatically
```

Use these expressions instead:

```text
route to a brain
read a brain
apply a brain lens
write a handoff prompt
integrate returned output
```
