# Basic Function Workspace MAP

## Files

```text
BASIC_FUNCTION_WORKSPACE/
  START_HERE.md
  MAP.md
  DEVELOPMENT_LOG.md
  BASIC_FUNCTION_CONTRACT_v0_1.md
  BASIC_FUNCTIONIZATION_PRINCIPLES_v0_1.md
  BASIC_FUNCTION_INDEX_v0_1.md
  BASIC_FUNCTION_INDEX_v0_2.md
  BASIC_FUNCTION_CARDS_v0_1.md
  BASIC_FUNCTION_SKILL_SKELETON_SERIES_v0_2.md
  BASIC_FUNCTION_USE_ORDER_v0_1.md
  BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md
  BASIC_FUNCTION_TEST_FIXTURES_v0_1.md
  BASIC_FUNCTION_NEGATIVE_FIXTURES_v0_1.md
  BASIC_FUNCTION_REAL_TASK_FIXTURES_v0_1.md
  BASIC_FUNCTION_ACCEPTANCE_CHECK_v0_1.md
  BASIC_FUNCTION_PROOF_REPORT_v0_1.md
  BASIC_FUNCTION_QUALITY_REVIEW_v0_1.md
  BASIC_FUNCTION_STABLE_LOCK_v0_1.md
```

## File roles

- `START_HERE.md`: entry and reading order
- `MAP.md`: local file map
- `DEVELOPMENT_LOG.md`: chronological development notes
- `BASIC_FUNCTION_CONTRACT_v0_1.md`: shared function schema
- `BASIC_FUNCTIONIZATION_PRINCIPLES_v0_1.md`: how AILO material becomes a basic function
- `BASIC_FUNCTION_INDEX_v0_1.md`: function list and status
- `BASIC_FUNCTION_INDEX_v0_2.md`: v0.1 stable layer plus v0.2 tested skill-skeleton series
- `BASIC_FUNCTION_CARDS_v0_1.md`: function definitions
- `BASIC_FUNCTION_SKILL_SKELETON_SERIES_v0_2.md`: basic functions for skill skeleton construction
- `BASIC_FUNCTION_USE_ORDER_v0_1.md`: default order for using the functions
- `BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md`: intake gate for new function candidates
- `BASIC_FUNCTION_TEST_FIXTURES_v0_1.md`: small test inputs and expected outputs
- `BASIC_FUNCTION_NEGATIVE_FIXTURES_v0_1.md`: cases where functions must refuse expansion
- `BASIC_FUNCTION_REAL_TASK_FIXTURES_v0_1.md`: realistic design-task cases
- `BASIC_FUNCTION_ACCEPTANCE_CHECK_v0_1.md`: pass/fail gate for this layer
- `BASIC_FUNCTION_PROOF_REPORT_v0_1.md`: current v0.1 proof result
- `BASIC_FUNCTION_QUALITY_REVIEW_v0_1.md`: current quality review and tightening targets
- `BASIC_FUNCTION_STABLE_LOCK_v0_1.md`: stable lock for the v0.1 common layer

## Layer boundary

```text
basic function
-> common control layer

cognitive function
-> expansion layer
```

This workspace stops at the basic function layer.

## Development order

```text
contract
-> index
-> function cards
-> fixtures
-> acceptance check
-> proof note
```

## Current status

```text
contract: stable
index: stable
function_cards: v0.1 stable set
fixtures: v0.1 tested set
negative_fixtures: added
real_task_fixtures: added
use_order: added
candidate_gate: added
quality_review: stable_v0_1
functionization_principles: added
acceptance_check: stable
workspace_check: passed
function_fixture_proof: PASS_STABLE
stable_lock: added
skill_skeleton_series_v0_2: tested, not stable
```
