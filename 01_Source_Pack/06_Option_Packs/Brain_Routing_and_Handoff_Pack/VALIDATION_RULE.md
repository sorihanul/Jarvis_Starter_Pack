# Validation Rule

## Pass Conditions

The setup passes when:

```text
BRAIN_ROUTE_REGISTRY.md exists or is explicitly not needed
ACTIVE_BRAIN_ROUTE.md exists when a route is active
ROUTE_LOG.md records non-obvious route decisions
same-thread vs separate-thread mode is declared
entry files are named
handoff prompt exists when separate-thread mode is used
final integration owner is visible
```

## Fail Conditions

The setup fails when:

```text
it claims to control another brain directly
the target brain was not read and no handoff was made
ACTIVE_BRAIN_ROUTE.md does not show the current route
handoff prompt lacks entry files or expected output
returned output is treated as final without integration
the pack is used for a simple one-brain task
```

## Revalidation

After changing a route or handoff, recheck:

```text
can a new reader see which brain to read?
can a new reader see whether this is same-thread or separate-thread?
can another thread boot from the handoff prompt without hidden context?
can the main thread integrate the returned output?
```
