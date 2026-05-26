# AILO-N Practical Use Card v0.1

## purpose

This card is the short runtime surface for AILO-N.

The full source is stored at:

```text
01_Source_Pack/00_Core/AILO_N_NOMINAL_FRAME_LAYER_v0_9N.md
```

Do not read the full source by default.
Use this card first when a task needs noun-style target frames.

Before creating persistent frames, also read:

```text
01_Source_Pack/01_Modules/AILO_Function_Layer/AILO_N_FRAME_USE_RULES_v0_1.md
```

## one-line definition

```text
AILO-N turns repeated targets into noun-slot frames so AILO verbs can act on stable, validated objects.
```

## v3 relationship

```text
AILO-V / intent layer
-> what to do

AILO function layer
-> how to split the work into functions and function packs

AILO-N
-> what reusable object the work is about
```

AILO-N does not replace verbs, functions, function packs, engines, skills, or brains.
It gives them stable targets.

For v4-style cognitive synapses:

```text
synapse
-> judgment movement

AILO-N
-> judgment target
```

## use_when

Use AILO-N when:

```text
repeated_target:true
relation_direction_must_be_preserved:true
state_source_confidence_must_remain_visible:true
candidate_needs_validation_before_assertion:true
context_packet_needed:true
```

Examples:

```text
Brain.Verifier
FunctionPack.SourceRoute
Policy.EvidenceRequired
Repo.Target
Patch.Plan
Source.DesignNote
Claim.CandidateRule
```

## do_not_use_when

Do not use AILO-N when:

```text
single_use_simple_request:true
no_reusable_target:true
frame_would_duplicate_plain_note:true
validation_rule_missing_for_persistent_use:true
execution_intent_is_inside_noun_frame:true
frame_count_would_grow_without_merge_or_discard:true
```

## frame use guardrails

```text
Frame only for repeated targets.
conf has no authority.
asserted is forbidden without source, evidence, and assertionBasis.
Execution stays outside the Frame.
When frames multiply, merge or discard them.
```

## practical frame shape

```ailo
Frame.Name{
  isa,
  role,
  consumes,
  produces,
  governedBy,
  blocks,
  validates,
  source,
  evidence,
  state,
  conf,
  assertionBasis,
  trace
};
```

This is the default v3 practical frame shape.

```text
validates
-> default slot
-> target, criteria, or output this frame validates

conf
-> optional helper slot
-> confidence_hint, not truth score
-> cannot replace source, evidence, or assertionBasis
-> cannot promote candidate to asserted
-> may be omitted when evidence is not available

state + assertionBasis
-> authority boundary
```

Compressed boot shape:

```ailo
Frame.Name{
  isa,
  role,
  consumes,
  produces,
  governedBy,
  state
};
```

Use the compressed shape only for routing, boot summaries, and short context packets.
Use the practical shape for persistent frame candidates, Canon Memory candidates, brain frames, policy frames, repo frames, patch frames, and validation objects.

Extended optional slots:

```text
id
label
alias
isa
kind
role
subject
predicate
object
content
dependsOn
governedBy
conflictsWith
supports
blocks
produces
consumes
validates
must
cannot
scope
risk
rule
source
evidence
state
conf
assertedBy
assertionBasis
reviewedAt
trace
memory
```

## state rules

```text
observed
-> extracted or seen from input

candidate
-> proposed but not verified

asserted
-> accepted for the current system context through visible basis

inferred
-> derived by a rule or graph process

deprecated
-> retained but no longer recommended

rejected
-> failed validation
```

Promotion rule:

```text
candidate -> asserted
only when source/evidence and assertionBasis are visible
```

`state:"asserted"` requires visible basis.

```text
required_for_asserted:
  source
  evidence
  assertionBasis
```

Invalid asserted frame:

```ailo
Claim.X{
  isa:Claim,
  state:"asserted",
  conf:0.95
};
```

Valid asserted frame:

```ailo
Claim.X{
  isa:Claim,
  source:[Source.A],
  evidence:[Evidence.B],
  state:"asserted",
  assertionBasis:["source_visible","evidence_matched"],
  conf:0.82
};
```

One-line authority rule:

```text
validates is a default slot.
conf is a helper slot.
state + assertionBasis decide authority.
```

## validation gates

Reject or stop when:

```text
missing_isa
undefined_target
slot_type_mismatch
relation_domain_mismatch
relation_range_mismatch
asserted_without_source_or_basis
candidate_used_as_fact
execution_instruction_inside_noun_frame
invalid_state_transition
formal_source_conflict
```

## correct verb separation

Wrong:

```ailo
Engine.Builder{
  isa:Engine,
  verify:true
};
```

Right:

```ailo
Engine.Builder{
  isa:Engine,
  state:"candidate"
};

verify{
  obj:Engine.Builder,
  rule:{check:[isa, source, assertionBasis]},
  to:"frame_verdict"
}!
```

## v3 brain frame pattern

```ailo
Brain.Verifier{
  isa:Brain,
  role:"evidence_first_verification",
  consumes:[Artifact.Target, Rule.AcceptanceCriteria],
  produces:[Report.Validation],
  governedBy:[Policy.EvidenceRequired],
  blocks:[Action.UnverifiedCompletion],
  validates:[Rule.AcceptanceCriteria, Report.Validation],
  state:"candidate",
  source:[Source.DesignNote],
  conf:0.72
};
```

Use this pattern for:

```text
Info_Research_Brain
Jarvis_Verification_Brain
Coding_Brain
future domain brains
```

## coding brain frame pattern

```ailo
Repo.Target{
  isa:Project,
  role:"codebase_under_edit",
  governedBy:[Policy.RepoLocalRules],
  blocks:[Action.ScopeViolation, Action.UnrelatedRefactor],
  validates:[Test.Unit, Test.Build],
  state:"observed"
};

Patch.Plan{
  isa:Artifact,
  consumes:[Task.UserRequest, Repo.Target],
  produces:[Artifact.Diff],
  governedBy:[Policy.ScopeLimit],
  blocks:[Action.OutOfScopeEdit],
  validates:[Test.Required, Review.ScopeCheck],
  state:"candidate"
};
```

## context packet rule

When context is too large:

```text
frame
-> preserve only isa, role, critical relations, validates, state, source, assertionBasis, conf
-> pass compact packet to the next AILO verb or brain
```

Example packet:

```text
Brain.Verifier is a Brain.
Role: evidence_first_verification.
It consumes target artifacts and acceptance criteria.
It produces validation reports.
State: candidate.
Confidence: 0.72.
```

## source rule

The full AILO-N source is the authority for:

```text
canonical slot list
relation contracts
formal mapping
state transition details
validation code details
knowledge pack shape
fixtures
```

This card is enough for:

```text
brain design
function pack target framing
Canon Memory candidate framing
context compression
quick validation of noun-frame usage
```

## stop_rule

Stop and open the full source only when:

```text
canonical_slot_dispute:true
relation_contract_needed:true
formal_mapping_needed:true
validation_code_detail_needed:true
knowledge_pack_shape_needed:true
```

## one-line rule

```text
Use AILO-N to name and validate the reusable target; use AILO verbs and function packs to act on it.
```
