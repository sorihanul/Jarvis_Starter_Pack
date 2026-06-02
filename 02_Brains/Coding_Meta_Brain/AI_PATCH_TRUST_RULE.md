# AI Patch Trust Rule

## rule

AI-generated code is an untrusted patch until verified.

Do not treat fluent explanations, clean formatting, or passing narrow tests as proof that the code is correct, secure, or maintainable.

## required stance

```text
generated_code_status: draft_patch
requires_review:true
requires_verification:true
high_risk_requires_extra_gate:true
```

## report requirement

Every closeout must distinguish:

```text
what_ai_changed:
what_was_verified:
what_was_not_verified:
what_still_needs_human_or_future_review:
```
