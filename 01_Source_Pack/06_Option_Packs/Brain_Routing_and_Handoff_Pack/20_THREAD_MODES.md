# 20 Thread Modes

## Mode 1. Same-Thread Lens Switch

Use when the current thread can read another brain's entry files and work under that lens.

```text
main brain identifies target brain
main brain reads target brain entry files
main brain applies the target brain's rules to this task
main brain returns to final integration before answering
```

Best for:

```text
small reviews
short writing passes
quick verification
brief domain checks
```

Risk:

```text
the model may forget that this is only a temporary lens
```

## Mode 2. Separate-Thread Handoff

Use when the target brain should run in another thread or agent session.

```text
main brain writes launch prompt
other thread boots the target brain
other thread completes bounded work
other thread returns report or artifact
main brain integrates result
```

Best for:

```text
large research
heavy verification
domain-brain work
parallel exploration
```

Risk:

```text
handoff loses context if the launch prompt is vague
```

## Mode 3. Integration Only

Use when specialist outputs already exist.

```text
main brain reads outputs
main brain compares scope and evidence
main brain resolves conflict or reports unresolved conflict
main brain produces final integrated result
```

Best for:

```text
multi-thread returns
review bundles
release decisions
research synthesis
```
