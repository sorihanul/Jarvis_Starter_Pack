# 30 Main Brain And Routed Brain Rule

## Main Brain Owns

```text
user goal
scope
boundary
route decision
handoff prompt
returned-output integration
final answer
```

The main brain must not pretend that it can directly operate another brain.

## Routed Brain Owns

```text
its own entry files
its own task scope
its own output contract
its own local logs if used in a separate thread
```

The routed brain is only active if:

```text
the current thread reads its files
or another thread boots it from a launch prompt
```

## Authority Boundary

```text
routed brain output is input
main brain integration is final output
```

If the routed brain finds a blocking issue, it reports it. The main brain decides whether the overall task stops, switches route, or continues.

## Drift Guard

Fail the setup if:

```text
the main brain claims to control another brain without reading or handoff
the routed brain changes the original user goal
the final integration owner is unclear
the active route must be guessed from conversation history
```
