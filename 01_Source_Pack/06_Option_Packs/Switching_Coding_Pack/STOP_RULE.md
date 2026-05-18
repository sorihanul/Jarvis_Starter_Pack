# Stop Rule

Stop before coding when:

```text
the target repository or files are unclear
success criteria are unknown
the requested command is destructive
the task requires secrets, credentials, or production access
the change would exceed the declared scope
the user asked for discussion only
```

Stop during coding when:

```text
unexpected unrelated changes appear in touched files
tests fail for an unclear reason
the patch requires a larger architecture decision
the task has become a new feature request
```

Stop after coding when:

```text
verification is complete
verification is blocked and the blocker is reported
the remaining work needs a separate handoff
```

## One-Line Rule

If the active lens cannot reduce risk or move the task closer to success, stop switching and return to the main task.
