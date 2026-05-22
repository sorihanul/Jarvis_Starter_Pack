# Operating Rule

## Core Loop

```text
1. restate the coding goal
2. lock success criteria
3. choose one active lens
4. inspect only needed files first
5. make the smallest valid change or handoff
6. verify against the success criteria
7. report changes, checks, risks, and next action
```

## Switching Rule

Switch lens only when the job changes.

```text
intake -> implement
when scope and success criteria are clear

implement -> review
when code was changed and needs defect inspection

review -> verify
when findings or changes need proof

verify -> release
when checks are done or honestly blocked

any lens -> handoff
when another thread or specialist must continue
```

## Scope Rule

- Do not refactor nearby code just because it is ugly.
- Do not add features that were not requested.
- Do not hide assumptions.
- Prefer one small patch over a large system rewrite.
- If the task is too large, split it into handoff packets.

## Workspace Fit

In a file-based AI workspace, this pack is mainly a thinking and routing surface.

It works by:

```text
reading the relevant lens
using normal file tools
writing a bounded patch
recording checks
creating handoff text when needed
```

It does not require a special runtime to be useful.
