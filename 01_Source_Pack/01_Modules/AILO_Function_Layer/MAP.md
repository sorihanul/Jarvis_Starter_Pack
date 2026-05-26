# AILO Function System MAP

## Layout
```text
03_AILO_Function_System/
  README.md
  START_HERE.md
  MAP.md
  V3_PLACEMENT_NOTE.md
  FUNCTION_PACK_BOUNDARY_v0_1.md
  FUNCTION_PACK_BUILD_CARD_v0_1.md
  AILO_N_FRAME_USE_RULES_v0_1.md
  AILO_N_PRACTICAL_USE_CARD_v0_1.md
  FUNCTION_PACK_EXAMPLE_CATALOG_v0_1.md
  FUNCTION_PACK_PROMOTION_MATRIX_v0_1.md
  DEVELOPMENT_ROADMAP_v0_1.md
  BASIC_AND_COGNITIVE_FUNCTION_CONCEPT_v0_1.md
  BASIC_LAYER_HANDOFF_GATE_v0_1.md
  AILO_BOUNDARY_AND_FUNCTIONIZATION_PRINCIPLES_v0_1.md
  AILO_FUNCTION_MATERIAL_GATEWAY_v0_1.md

  01_AILO_Functions/
    AILO_FUNCTION_SYSTEM_FLAG_v0_1.md
    AILO_FUNCTION_MINIMUM_SET_v0_1.md
    AILO_FUNCTION_DEFINITION_v0_1.md
    BASIC_FUNCTION_WORKSPACE/
      SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md
      SKILL_SKELETON_OVERLAP_REVIEW_v0_1.md
      SKILL_SKELETON_FAILURE_CONSISTENCY_REVIEW_v0_1.md

  02_AILO_Cognitive_Functions/
    FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE_v0_1.md
    AILO_COGNITIVE_FUNCTION_BOUNDARY_v0_1.md
    AILO_COGNITIVE_FUNCTION_CONTRACT_v0_1.md
    AILO_COGNITIVE_FUNCTIONIZATION_PRINCIPLES_v0_1.md
    AILO_COGNITIVE_FUNCTION_DEFINITION_v0_1.md

  03_AILO_Engines/
    AILO_ENGINE_BOUNDARY_v0_1.md
    AILO_ENGINE_CONTRACT_v0_1.md
    AILO_ENGINEIZATION_PRINCIPLES_v0_1.md
    AILO_ENGINE_DEFINITION_v0_1.md

  04_Research_Notes/
    CLASSIFICATION_DECISION_NOTE_v0_1.md
    CODE_AS_AGENT_HARNESS_READING_NOTE_v0_1.md
    PLACEMENT_RULE_v0_1.md

  05_AILO_OS/
    IMPLEMENTATION_SEQUENCE_v0_1.md
    AILO_OS_DEFINITION_v0_1.md
    AILO_OS_HARNESS_CRITERIA_v0_1.md
    AILO_OS_HARNESS_SEED_READINESS_CHECK_v0_1.md
    AILO_OS_HARNESS_SEED_EXECUTION_CONTRACT_v0_1.md
    AILO_OS_HARNESS_SEED_TARGET_v0_1.md
    AILO_OS_THRESHOLD_RULE_v0_1.md
    HARNESS_SEED_SCOPE_LOCK_v0_1/
    HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1/
    HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2/
    NON_RUST_MINI_HARNESS_v0_1/

  06_Skill_Manufacturing_Proofs/
    README.md
    skill_skeleton_builder.py
    run_all_skill_manufacturing_proofs.py
    run_all_real_trials.py
    SKILL_MANUFACTURING_PROOF_SUMMARY_v0_1.md
    SOURCE_REVIEW_SKILL_SAMPLE_v0_1/
    PROMPT_VALIDATION_SKILL_SAMPLE_v0_1/
    WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1/
```

## Relationship to other folders
- promoted rules stay inside this package's public source layer
- reusable material stays inside public modules or option packs
- active experiments and tests stay inside package-local proof or task surfaces

In Jarvis Starter Pack v3, this copied layer lives at:

```text
01_Source_Pack/01_Modules/AILO_Function_Layer/
```

Use `V3_PLACEMENT_NOTE.md` before deciding how much of this layer to open.

## Development paths
```text
Path A: basic runtime route
AILO E++ -> AILO function system -> Rust-based AILO OS

Path B: cognitive expansion route
AILO cognitive expansion -> AILO function system -> AILO cognitive function system -> AILO engine system -> Rust-based AILO OS
```

Use `DEVELOPMENT_ROADMAP_v0_1.md` before moving from concept classification to implementation planning.

## Core split
```text
function = one smallest action
function pack = related smallest action-unit group
cognitive function = bounded meaning operation
engine = ordered verified mechanism
skill = user-callable procedure
brain component = identity/boundary/memory/output contract layer
```

Use `FUNCTION_PACK_BOUNDARY_v0_1.md` before deciding whether related functions should remain a function pack or become an engine, skill, or brain component.

Use `FUNCTION_PACK_BUILD_CARD_v0_1.md` when a model must create one function pack quickly without opening the whole function layer.

Use `AILO_N_FRAME_USE_RULES_v0_1.md` before creating or promoting persistent frames. It keeps frames limited to repeated targets, blocks authority from `conf`, forbids unsupported `asserted`, keeps execution outside frames, and requires merge/discard when frames multiply.

Use `AILO_N_PRACTICAL_USE_CARD_v0_1.md` when a repeated target needs a noun-slot frame before AILO verbs or function packs act on it.
The full AILO-N source lives at `01_Source_Pack/00_Core/AILO_N_NOMINAL_FRAME_LAYER_v0_9N.md` and is not read by default.

Use `FUNCTION_PACK_EXAMPLE_CATALOG_v0_1.md` when a model needs concrete starter packs such as Goal and Scope Pack, Read Route Pack, Output Contract Pack, Evidence and Uncertainty Pack, Permission and Stop Pack, or Skill Skeleton Pack.

Use `FUNCTION_PACK_PROMOTION_MATRIX_v0_1.md` when deciding whether a function pack group should stay as construction material or become an engine, skill, or brain component.

Use `BASIC_AND_COGNITIVE_FUNCTION_CONCEPT_v0_1.md` before classifying or implementing a new function.

Use `BASIC_LAYER_HANDOFF_GATE_v0_1.md` after the basic function layer reaches `PASS_STABLE` and the next route must be chosen.

Use `AILO_BOUNDARY_AND_FUNCTIONIZATION_PRINCIPLES_v0_1.md` before calling anything AILO or an AILO function.

Use `AILO_FUNCTION_MATERIAL_GATEWAY_v0_1.md` when a new function idea appears.
AILO is the function-making material and open gateway; the common layer accepts only proven contracts.

Functions and function packs are shared construction material:

```text
Path A
-> function
-> function pack

Path B
-> function
-> function pack
-> cognitive function
```

## Cognitive function definition path
When defining or judging an AILO cognitive function, read:

```text
02_AILO_Cognitive_Functions/FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE_v0_1.md
02_AILO_Cognitive_Functions/AILO_COGNITIVE_FUNCTION_BOUNDARY_v0_1.md
02_AILO_Cognitive_Functions/AILO_COGNITIVE_FUNCTION_CONTRACT_v0_1.md
02_AILO_Cognitive_Functions/AILO_COGNITIVE_FUNCTIONIZATION_PRINCIPLES_v0_1.md
02_AILO_Cognitive_Functions/AILO_COGNITIVE_FUNCTION_DEFINITION_v0_1.md
```

## First flag
```text
AILO E++ based AILO function system
```

Start from `01_AILO_Functions/AILO_FUNCTION_SYSTEM_FLAG_v0_1.md`.

Then use `02_AILO_Cognitive_Functions/FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE_v0_1.md` to expand into cognitive functions.

## Classification map
```text
format / slot / policy operation
-> AILO function

meaning / judgment / reasoning operation
-> AILO cognitive function

ordered functions + guards + output contract + verification
-> AILO engine

runner / registry / trace / permission / release surface
-> AILO OS
```

## Placement rule
```text
AILO function -> shared lower function layer
AILO cognitive function -> brain-local cognitive lane
AILO engine -> brain-local engine lane
AILO OS -> implementation/runtime lane
```

Jarvis v2 may carry the public/basic subset of AILO functions.
Advanced cognitive expansion may reuse the same basic layer before adding cognitive functions.

Use `04_Research_Notes/PLACEMENT_RULE_v0_1.md` when classification is clear but the target folder or target system is not clear.

Use `04_Research_Notes/CODE_AS_AGENT_HARNESS_READING_NOTE_v0_1.md` when translating external harness research into the AILO expansion path without importing foreign structure directly.

Use `05_AILO_OS/AILO_OS_THRESHOLD_RULE_v0_1.md` when deciding whether a system is still a document/spec or has become an operating layer.

Use `05_AILO_OS/AILO_OS_HARNESS_CRITERIA_v0_1.md` when deciding whether AILO OS is only a document spec or has become runnable, inspectable, stateful, and governed.

Use `05_AILO_OS/AILO_OS_HARNESS_SEED_TARGET_v0_1.md` before implementing or evaluating the first minimal AILO OS harness seed.

Use `05_AILO_OS/AILO_OS_HARNESS_SEED_EXECUTION_CONTRACT_v0_1.md` as the implementation-ready contract for the first scope-lock harness seed.

Use `05_AILO_OS/AILO_OS_HARNESS_SEED_READINESS_CHECK_v0_1.md` before deciding that the first seed is ready for a minimal prototype.

Use `05_AILO_OS/HARNESS_SEED_SCOPE_LOCK_v0_1/README.md` when checking the first one-function mock prototype proof.

Use `05_AILO_OS/HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1/README.md` when checking the explicit-function mock proof for all seven stable basic functions.

Use `05_AILO_OS/HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2/README.md` when checking the v0.2 basic functions for skill skeleton construction.

Use `05_AILO_OS/IMPLEMENTATION_SEQUENCE_v0_1.md` before deciding whether to move toward Rust.

Use `05_AILO_OS/NON_RUST_MINI_HARNESS_v0_1/README.md` as the current non-Rust starting point for observing stable basic function behavior.

Use `06_Skill_Manufacturing_Proofs/SOURCE_REVIEW_SKILL_SAMPLE_v0_1/README.md` when checking whether basic functions can manufacture a reusable skill skeleton without cognitive functions, engines, Rust, or smart routing.

Use `06_Skill_Manufacturing_Proofs/SKILL_MANUFACTURING_PROOF_SUMMARY_v0_1.md` when checking the current multi-sample proof status.

Use `06_Skill_Manufacturing_Proofs/run_all_skill_manufacturing_proofs.py` to rerun all current skill-manufacturing proof samples.

Use `06_Skill_Manufacturing_Proofs/run_all_real_trials.py` to rerun all current small real-trial checks.

Use `01_AILO_Functions/BASIC_FUNCTION_WORKSPACE/SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md` before treating v0.2 skill-skeleton functions as stable.

Use `01_AILO_Functions/BASIC_FUNCTION_WORKSPACE/SKILL_SKELETON_OVERLAP_REVIEW_v0_1.md` when checking whether v0.2 functions duplicate or drift into v0.1 stable functions.

Use `01_AILO_Functions/BASIC_FUNCTION_WORKSPACE/SKILL_SKELETON_FAILURE_CONSISTENCY_REVIEW_v0_1.md` when checking whether v0.2 failure outputs stay composable.

## Engine definition path
When defining or judging an AILO engine, read:

```text
03_AILO_Engines/AILO_ENGINE_BOUNDARY_v0_1.md
03_AILO_Engines/AILO_ENGINE_CONTRACT_v0_1.md
03_AILO_Engines/AILO_ENGINEIZATION_PRINCIPLES_v0_1.md
03_AILO_Engines/AILO_ENGINE_DEFINITION_v0_1.md
```
