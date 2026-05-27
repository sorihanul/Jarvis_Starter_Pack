# Usage Example

## request

```text
Create a mini ontology for a brain-building workflow.
```

## mini ontology scope

```text
domain: Jarvis brain-building workflow
main_use_case: separate brain, pack, source, claim, and validation result
must_help_ai_do: route, block unsupported claims, validate output contracts
```

## frames

```ailo
Brain.Target{
  isa:Brain,
  role:"runtime_component_with_identity_boundary_memory_and_output_contract",
  consumes:[Source.DesignMaterial, Rule.LocalBoundary],
  produces:[Artifact.BrainSurface, Report.Handoff],
  governedBy:[Policy.SourceUsageRule],
  blocks:[Action.UnscopedBrainBuild],
  validates:[Contract.OutputSurface],
  source:[Source.UserRequest, Source.StarterV3],
  evidence:[Evidence.RequiredBrainFiles],
  state:"candidate",
  conf:0.72,
  assertionBasis:[],
  topo:{rel:"sink", to:[Artifact.BrainSurface, Report.Handoff], strength:"medium"},
  trace:["extracted_from_brain_build_discussion"]
};

FunctionPack.Target{
  isa:FunctionPack,
  role:"group_of_related_small_action_units",
  consumes:[Task.Goal, Constraint.Scope],
  produces:[Procedure.ReusablePack],
  governedBy:[Policy.FunctionPackBoundary],
  blocks:[Action.UnboundedProcedureGrowth],
  validates:[Contract.InputOutputStopRule],
  source:[Source.AILOFunctionLayer],
  evidence:[Evidence.FunctionPackBoundary],
  state:"asserted",
  conf:0.8,
  assertionBasis:["source_visible","contract_visible"],
  topo:{rel:"hub", to:[Contract.InputOutputStopRule], strength:"medium"},
  trace:["from_function_pack_boundary"]
};

Claim.CandidateRule{
  isa:Claim,
  role:"statement_that_requires_evidence_before_use_as_fact",
  consumes:[Source.Material],
  produces:[Decision.CandidateOrAsserted],
  governedBy:[Policy.EvidenceRequired],
  blocks:[Action.UnsourcedAssertion],
  validates:[Evidence.SourceBinding],
  source:[Source.UserMaterial],
  evidence:[],
  state:"candidate",
  conf:0.6,
  assertionBasis:[],
  topo:{rel:"gate", to:[Decision.CandidateOrAsserted], strength:"hard"},
  trace:["candidate_until_source_bound"]
};
```

## relation index

```text
from: Brain.Target
relation: consumes
to: Source.DesignMaterial
direction: Brain.Target -> Source.DesignMaterial
reason: brain construction starts from source material
source: Source.StarterV3
evidence: Evidence.RequiredBrainFiles
state: candidate

from: FunctionPack.Target
relation: validates
to: Contract.InputOutputStopRule
direction: FunctionPack.Target -> Contract.InputOutputStopRule
reason: function packs need explicit input/output/stop contracts
source: Source.AILOFunctionLayer
evidence: Evidence.FunctionPackBoundary
state: asserted
```

## query table

```text
question: Which claims cannot be used as facts?
allowed_frames: Claim.*
required_state: candidate | inferred | observed
must_check: source, evidence, assertionBasis
do_not_answer_when: state is asserted but basis is missing

question: What blocks unsupported completion?
allowed_frames: Policy.*, Claim.*, Brain.*
required_state: candidate | asserted
must_check: blocks
do_not_answer_when: blocks is empty

question: Which objects require validation before handoff?
allowed_frames: Brain.*, FunctionPack.*, Artifact.*
required_state: candidate | asserted
must_check: validates
do_not_answer_when: validates is empty
```

## validation report

```text
verdict: pass_with_risk
blocking_issues: []
major_issues:
  - Brain.Target is still candidate because assertionBasis is empty.
minor_issues:
  - Claim.CandidateRule needs evidence before promotion.
next_action:
  - bind source and evidence before using candidate frames as facts.
```
