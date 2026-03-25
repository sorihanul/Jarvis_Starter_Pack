# Public Agent Fit Guide

- date: 2026-03-26
- purpose: clarify which public agent form fits which task class in Jarvis Starter

## Core Principle

- Jarvis Starter should not choose between `AILO` and `non-AILO` by ideology.
- It should choose by task shape:
  - how much routing discipline is needed
  - how much stop behavior is needed
  - how much immediate deliverable pressure is needed

## Working Map

- `AILO chief`
  - best for:
    - intake
    - scope lock
    - first-route lock
    - review ordering
    - escalation-heavy requests
  - why:
    - strongest structural discipline
    - best bounded routing contract

- `non-AILO chief/router`
  - best for:
    - lighter public routing
    - general-purpose intake
    - less formal but still bounded orchestration
  - why:
    - keeps routing practical without loading explicit structural language

- `AILO follower`
  - best for:
    - risky coding work
    - research tasks where contract discipline matters
    - bounded implementation slices
    - places where stop conditions matter
    - tasks that must stay honest about blockers and authority
  - risk:
    - may under-deliver if the environment is ambiguous or constrained

- `non-AILO follower`
  - best for:
    - fast output-oriented work
    - writing
    - compact synthesis when small label drift is acceptable
    - low-risk coding help, especially when using a coding specialist rather than a generic worker
  - risk:
    - tends to over-produce and drift in label discipline

- `gate`
  - best for:
    - safety
    - approval
    - keep/hold/reopen/deny judgments
    - external intake and risky execution
  - note:
    - do not use a gate where a chief is needed
    - do not use a chief where a gate judgment is needed

## First Practical Rule

- if the task asks:
  - `where should this go?`
    - use a `chief`
  - `may this proceed?`
    - use a `gate`
  - `produce one bounded result`
    - use a `follower`

## AILO vs Non-AILO Rule

- choose `AILO` when:
  - scope honesty matters more than speed
  - stop posture matters more than helpfulness
  - escalation and protected-boundary awareness matter

- choose `non-AILO` when:
  - quick usable output matters more than structural strictness
  - the task is low-risk and bounded
  - language should stay flatter and more public-generic

## Current Status

- this guide is a working selection guide
- it is meant to help the starter choose the right public agent form by task shape

## Research-Specific Reading

- if the research task needs:
  - cleaner contract obedience
  - bounded uncertainty reporting
  - stronger stop posture
    - prefer `AILO` research specialist

- if the research task needs:
  - quick synthesis
  - flatter public language
  - less structural overhead
    - prefer `non-AILO` research specialist

## Coding-Specific Reading

- if the coding task needs:
  - stop posture
  - blocker honesty
  - stricter boundedness under ambiguous conditions
    - prefer an `AILO` coding follower
    - but currently prefer `AILO` worker over `AILO` coding specialist if contract obedience matters more than immediate implementation text

- if the coding task needs:
  - quick usable patch-shaped output
  - a low-risk helper change
  - public-generic language
    - prefer a `non-AILO` coding specialist over a generic `non-AILO` code worker

- current coding-specialist note:
  - `non-AILO` coding specialist is presently cleaner than `AILO` coding specialist in patch-shape obedience
  - `AILO` coding specialist still needs more than one hardening pass before it becomes the preferred coding-specialist form
  - the current difference appears to come from behavioral drift, not just a missing instruction line
