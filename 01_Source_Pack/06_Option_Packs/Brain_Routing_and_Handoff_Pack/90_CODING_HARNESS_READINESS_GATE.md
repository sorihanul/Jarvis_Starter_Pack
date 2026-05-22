# 90 Coding Harness Readiness Gate

## Purpose

Prevent this routing pack from being mistaken for a full coding pack.

A coding pack must solve real coding-agent failure modes, not just provide a
nice concept for role switching.

Current distributable v2 provides the minimal practical layer at:

```text
../Switching_Coding_Pack/
```

That pack handles coding lens switching and bounded handoff.
This readiness gate remains the boundary for anything larger, such as automatic
coding teams, CI control planes, long-running test operations, or multi-agent
project harnesses.

## Core Problem

Vibe coding fails when the agent moves from a loose intention to code changes
without enough control.

Common failure modes:

```text
vague_goal:
  the task sounds clear but success is not testable

hidden_scope_creep:
  the agent changes nearby code because it looks related

unbounded_editing:
  no file ownership, no do_not_touch list, no patch boundary

context_guessing:
  the agent assumes repo structure or behavior without reading it

test_theater:
  the agent says it verified but did not run or name meaningful checks

premature_refactor:
  the agent improves structure instead of fixing the requested problem

subagent_overtrust:
  the parent accepts a worker result without review or integration judgment

noise_leak:
  exploration logs, stack traces, and raw intermediate output pollute the main thread

permission_blur:
  read-only, write, shell, network, and release actions are not separated

release_overclaim:
  the agent reports done while risks, skipped checks, or untested paths remain hidden
```

## Benchmark Lessons To Absorb

These are design lessons, not source imports.

```text
Hermes-style systems:
  value:
    control plane, profile/session surfaces, model/tool/schedule visibility
  absorb_as:
    operator surface and runtime boundary, not as a copied implementation

Pi-style systems:
  value:
    session tree, tool-call hooks, package/extension boundary, RPC/headless bridge
  absorb_as:
    session lineage, before/after action gates, package manifest

OpenClaw / ClawTeam-style systems:
  value:
    team commands, worktree isolation, visible task board, agent spawn adapters
  absorb_as:
    work ownership, inbox/task coordination, explicit dispatch surface

Oh My Agent-style systems:
  value:
    single source of truth for agents and projection into multiple hosts
  absorb_as:
    source spec -> TOML role file / host prompt projection boundary

Superpowers-style systems:
  value:
    plan before build, verification before completion, subagent output review
  absorb_as:
    coding discipline skills and completion gates

Host-native direction:
  value:
    explicit subagent request, custom TOML agents, read-heavy parallel work,
    parent integration, sandbox and approval inheritance
  absorb_as:
    host-specific launch briefs, custom-agent examples, bounded parallel work
```

## Host Coding Use Contract

For a file-based AI workspace, a coding workflow must respect these rules:

```text
parent_owns:
  goal, scope, final integration, remaining risk

subagents_are_explicit:
  do not imply automatic subagent spawning

read_heavy_first:
  prefer explorer/reviewer/log-analysis subagents before parallel editors

write_work_is_bounded:
  each worker owns a clear file set or responsibility

handoff_is_complete:
  task, scope, target files, do_not_touch, success criteria, tests, return format

verification_is_named:
  report exact checks run, skipped checks, failures, and residual risk

integration_is_required:
  parent reviews worker output before final answer or release claim

cost_is_visible:
  parallel agents cost more tokens and time; do not use them for simple edits
```

## Minimum Dedicated Coding Pack Requirements

Do not create or advertise a dedicated coding pack until these are present:

```text
1_failure_taxonomy:
  explicit vibe-coding failure modes and how each is blocked

2_role_set:
  explorer, implementer, reviewer, test repair, release gate roles

3_toml_role_examples:
  narrow custom-agent TOML examples for the target host

4_parent_launch_briefs:
  copyable prompts for parent-led delegation and integration

5_permission_model:
  read-only, workspace-write, shell, network, and release boundaries

6_file_ownership_rule:
  disjoint write sets for parallel work and no unrelated refactors

7_test_and_proof_contract:
  required checks, skipped-check disclosure, failure handling

8_integration_rule:
  worker output is evidence, not final truth

9_distribution_hygiene:
  no machine-specific paths, no package-unrelated terminology, no copied external implementation

10_acceptance_tests:
  small tasks, multi-file tasks, review-only tasks, test-failure tasks, release-gate tasks
```

## Current Pack Decision

`Brain_Routing_and_Handoff_Pack` may support coding only as:

```text
route:
  choose a role or brain entry

handoff:
  write a bounded launch prompt

integrate:
  make the parent-level judgment after returned output
```

It must not claim:

```text
full coding harness
automatic agent team
complete vibe-coding solution
replacement for host custom agents
replacement for project tests
```

## Stop Rule

If a coding request needs more than route and handoff, stop calling this a
coding solution.

Escalate to a future dedicated coding workflow pack.
