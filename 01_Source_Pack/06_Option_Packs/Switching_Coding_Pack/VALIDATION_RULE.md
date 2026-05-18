# Validation Rule

A coding result passes this pack only when:

```text
the goal was restated
the active lens was clear
the file scope was respected
the change was bounded
verification was run or honestly blocked
remaining risks were reported
```

## Failure Conditions

Fail the result if:

```text
it claims automatic subagent behavior that the host does not provide
it changes files outside scope
it refactors unrelated code
it skips verification without saying so
it hides assumptions
it uses switching language without actually changing the work mode
```

## Verification Pairing

If the task is high-risk, pair this pack with `Verification_and_Proof_Pack`.

If the task includes file writes, shell, browser, or network action, pair it with `Action_Permission_Pack`.
