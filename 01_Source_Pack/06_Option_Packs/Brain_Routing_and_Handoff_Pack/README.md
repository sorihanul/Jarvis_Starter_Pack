# Brain Routing and Handoff Pack

## Purpose

This option pack decides which brain document to read, which brain-style launch prompt to create, and how to integrate the returned result.

It does not let one brain control another brain.

For coding role switching inside one coding task, use `../Switching_Coding_Pack/` first.
Use this pack with coding only when a separate brain/thread handoff or returned-result integration is needed.

## Real Operating Model

```text
same thread:
  read a brain entry file
  apply that brain as the current working lens
  return to the main brain before final output

separate thread:
  create a launch prompt or handoff brief
  another thread reads the target brain and works there
  main brain later reads the returned output
  main brain integrates the result
```

## What This Pack Does

```text
route:
  choose which brain file or brain family is relevant

read:
  identify the minimum entry files to open

switch lens:
  apply a brain style inside the same thread when that is enough

handoff:
  write a launch prompt for another thread or agent when separation is needed

integrate:
  read returned output and make the final parent-level judgment
```

## What This Pack Does Not Do

```text
does not remotely control another brain
does not make sub-brains run by itself
does not replace domain brains
does not require role switching for simple work
does not make every task a multi-brain task
```

## When To Use

Use this pack when:

```text
the user has several domain brains and must choose one
the task needs a launch prompt for a separate brain thread
the current thread must temporarily apply another brain's rules
several specialist outputs must be integrated
the target source is read-only and only a handoff can be produced
```

## When Not To Use

Do not use this pack when:

```text
one domain brain already owns the task
the task is a short answer, summary, or simple edit
the user is not asking for routing, handoff, or integration
```

## Durable Surfaces

```text
BRAIN_ROUTE_REGISTRY.md
ACTIVE_BRAIN_ROUTE.md
ROUTE_LOG.md
```

Optional surfaces:

```text
HANDOFFS/
INTEGRATION_NOTES.md
```

These surfaces are not required for every use.

Create them when the route will repeat, when a separate handoff is needed, or when returned outputs must be integrated later.

For one obvious same-thread route, a short route decision in the answer can be enough.

## First Read

```text
1. README.md
2. 00_BEGINNER_QUICK_START.md
3. 10_CONCEPT.md
4. 15_BRAIN_LENS_CONCEPT.md
5. 20_THREAD_MODES.md
6. 30_MAIN_ROUTED_BRAIN_RULE.md
7. 40_BRAIN_REGISTRY_TEMPLATE.md
8. 50_ACTIVE_ROUTE_AND_RETURN.md
9. 60_LOG_AND_HANDOFF_RULE.md
10. 70_EXAMPLES.md
11. 80_CODING_APPLICATIONS.md
12. 85_IDEA_COLLECTION_BRIEF.md
13. 90_CODING_HARNESS_READINESS_GATE.md
14. ACTIVATION_RULE.md
15. INPUT_SLOTS.md
16. OPERATING_RULE.md
17. OUTPUT_CONTRACT.md
18. STOP_RULE.md
19. VALIDATION_RULE.md
20. ACCEPTANCE_TESTS.md
```

## Completion Rule

The pack is usable only when a new reader can answer:

```text
which brain should be read?
is this same-thread lens switching or separate-thread handoff?
what files must be opened first?
where is the handoff prompt?
who integrates the returned result?
when should this pack not be used?
if coding is involved, is this only route/handoff or a dedicated coding harness problem?
```
