# Evidence Intake Usage Example v0.1

## Scenario

A user shows Jarvis a post that recommends an outside tool and says the tool is useful for agent workflows.

The user asks:

```text
Is there anything worth using?
```

## Step 1. Narrow The Question

```text
question:
  Which parts of this source can become Jarvis design rules?
```

## Step 2. Classify Sources

```text
source_label: user-provided post
source_type: commentary
observed_at: current session
version_or_date: unknown
authority_reason:
  It may point to useful ideas, but it is not enough to prove functionality.
limits:
  Do not treat claims as verified.
```

If the original documentation or actual files are available, inspect those before accepting claims.

## Step 3. Split Claims

```text
claim:
  The outside tool improves agent workflows.
claim_type: opinion
claim_state: unverified
evidence:
  user-provided post only
reason:
  No artifact or primary source has been checked yet.
design_use: hold
```

```text
claim:
  The post describes a pattern: keep reusable skills separate from the main runtime.
claim_type: inference
claim_state: plausible
evidence:
  pattern visible in the description
reason:
  The rule is useful even before adopting the tool.
design_use: allowed
```

## Step 4. Extract A Design Takeaway

```text
takeaway:
  Keep reusable skills separate from the main runtime.
evidence_state:
  plausible
design_grade:
  candidate
target_layer:
  Experience_To_Skill_Pack
use_when:
  A repeated workflow appears across tasks.
stop_when:
  The workflow is one-off or cannot be validated.
validation_needed:
  Test on one repeated Jarvis task.
reason:
  This reduces boot weight and keeps the main runtime smaller.
```

## Step 5. Final Answer Shape

```text
question:
  Is there anything worth using?

sources:
  - user-provided post: commentary

facts:
  - The post recommends an outside tool.

inferences:
  - A reusable pattern is skill separation.

opinions:
  - The tool is useful. This remains unverified.

unknowns:
  - Actual implementation quality.
  - Current feature support.
  - Runtime cost.

design_takeaways:
  - Candidate: keep reusable skills outside the main runtime.

risks:
  - Do not copy code or unique wording.
  - Do not treat marketing claims as verified.

next_step:
  Inspect the primary source or actual files if the user wants stronger judgment.
```

## Result

The post was useful as a pointer.

It was not treated as proof.

Only the reusable design rule became a candidate.
