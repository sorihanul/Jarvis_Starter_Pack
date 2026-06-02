# Final Goal Lock

## core rule

Lock the user's final goal, not the user's technical understanding.

The user may only know the purpose.
This brain must translate vague owner intent into a concrete final state before implementation.

Do not lock the first stated goal.
The first statement is raw intent, not a final goal.

Probe the purpose until the owner-visible success state, failure boundary, and first-version scope are concrete.

## purpose probing rule

The brain must discover what the owner is really trying to accomplish without forcing the owner to think like a developer.

Ask about real use, visible outcome, data, privacy, and failure. Do not ask about framework, database, API style, or test runner unless the answer changes cost, privacy, deployment, or risk.

## ask owner about outcomes

```text
who_uses_it:
when_do_they_use_it:
first_successful_action:
what_should_they_see_after_success:
must_have_output:
data_must_persist:
data_entered_by_user:
private_or_public:
shared_with_others:
mobile_or_desktop_or_web:
export_or_print_needed:
must_not_happen:
biggest_failure_to_avoid:
must_have_first_version:
nice_to_have_later:
done_when:
```

## avoid technical burden

Do not ask the owner to choose frameworks, databases, routing systems, or test runners unless that choice changes cost, privacy, deployment, or risk.

## lock allowed

```text
target_user_known:true
usage_situation_known:true
primary_success_flow_known:true
must_have_outcome_known:true
data_behavior_known:true
failure_boundary_known:true
first_version_scope_known:true
verification_method_possible:true
```

## lock forbidden

```text
goal_is_only_category_name:true
user_flow_unknown:true
data_behavior_unknown:true
risk_boundary_unknown:true
done_condition_vague:true
first_version_scope_unbounded:true
```

## output

```text
owner_goal_raw:
owner_context:
target_user:
usage_situation:
primary_user_flow:
must_have_outcomes:
must_not_happen:
data_lifecycle:
privacy_boundary:
first_version_scope:
non_goals:
open_questions:
locked_final_goal:
owner_acceptance:
decision_required_from_owner:
```
