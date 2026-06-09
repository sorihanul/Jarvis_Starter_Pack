# Behavior Verification Loop

## purpose

This document records the conservative coding loop for this experimental template.

The loop is not a claim that this brain is automated, runtime validated, or production ready. It is a working rule for how a coding case should be judged before closeout.

## priority

Correct working behavior comes first.

Automation, loops, agents, sub-brain roles, and skills are support mechanisms. They do not replace evidence that the program serves its original purpose, works correctly, and remains maintainable.

## core loop

```text
purpose_check:
  Does the program do what it was originally meant to do?

behavior_check:
  Does it actually work in the target user flow?

problem_check:
  Are there errors, regressions, edge-case failures, data risks, or usability failures?

cause_location:
  If there is a problem, locate whether it is in requirements, design, implementation, dependency, environment, or data.

minimal_fix:
  Change only the necessary scope.

reverification:
  After the fix, does the original behavior still work, and did the fix avoid breaking existing behavior?

maintainability_check:
  Is the resulting program still understandable, ordinary, and easy to maintain?
```

## done rule

Do not treat a loop, agent run, or implementation pass as done merely because it completed.

Done requires evidence that the original purpose is satisfied, the target behavior works, known problems are absent or explicitly bounded, and the implementation remains maintainable.

## use with role threads

```text
coordinator:
  owns purpose, behavior contract, done decision, and closeout

implementation_role:
  proposes the minimal implementation or fix inside the locked scope

verification_role:
  checks behavior, regressions, failure interpretation, and residual risk
```

Role separation can reduce risk, but it does not lower the evidence requirement.

## stop conditions

```text
stop_if:
  original purpose is unclear
  behavior cannot be verified
  problem cause is unknown but patching would be speculative
  fix expands beyond locked scope
  regression risk cannot be checked
  maintainability becomes worse without explicit reason
```

## output

```text
purpose_satisfied:
behavior_verified:
problems_found:
cause_location:
fix_scope:
reverification_result:
regression_check:
maintainability_result:
remaining_risk:
done_decision:
```
