# Public Agent Recipe v0.1

## Purpose

- define how to write a public-safe agent card inside Jarvis Starter
- keep agent cards small, readable, and operational for model-first use

## When To Use This Recipe

- when adding a new public agent under `AGENTS/`
- when a task lane is stable enough to deserve its own card
- when a bundle needs a clearer role boundary than a generic helper

## Core Rule

- a public agent card must define a lane, not a personality blob
- it should answer:
  - what this agent is for
  - what it may touch
  - what it must not do
  - what output shape it returns
  - which skills it should call first

## Recommended Card Structure

1. `역할 (Role)`
- one sentence for identity
- one sentence for what kind of lane this is

2. `범위 (Scope)`
- what is in scope
- what is out of scope

3. `입력 계약 (Input Contract)`
- what the card expects to receive

4. `출력 계약 (Output Contract)`
- what fields or sections it must return

5. `주요 스킬 (Primary Skills)`
- the exact skill files it should pair with

6. `금지사항 (Forbidden)`
- what drift to avoid

7. `종료 조건 (Exit Condition)`
- when the card should stop

## Design Rules

- one card = one clear lane
- do not combine chief, gate, and follower behavior in one card
- prefer bounded output over broad helpfulness
- keep the card shorter than a full module document
- write for model interpretation first

## Card-Type Hints

### Chief
- use when the question is:
  - where should this go?
  - what is the bounded scope?
  - what should be reviewed first?

### Gate
- use when the question is:
  - may this proceed?
  - should this be held, blocked, or escalated?

### Follower
- use when the question is:
  - produce one bounded result
  - complete one specialist slice

## Public Default Bias

- coding specialist:
  - default to public non-AILO shape
- writing specialist:
  - default to public non-AILO shape
- intake and stronger route locking:
  - AILO-E forms may fit better

## Minimal Promotion Check

- the lane is already tested at least once
- the card has matching skills
- the card does not require outside explanation
- the output contract is bounded

## One-Line Verdict

- a public agent card should be a small operating lane with a clear contract, not a grand theory blob
