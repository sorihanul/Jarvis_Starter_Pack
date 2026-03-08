# Society Runtime Protocol v0.1

mission
- Build a practical collaboration loop using cognitive-vector personas.
- Keep safety and reproducibility above creativity spikes.

pipeline
1. intake: read latest society board line
2. route: pick 1-2 personas by task type
3. execute: produce role outputs
4. synthesize: merge into one decision block
5. memory_write:
   - persona-specific lessons -> persona memory
   - approved consensus only -> shared memory
6. close: append run summary in `runs/`

persona_selection
- strategy/research question -> researcher
- risk/constraint question -> critic
- final integration -> synthesizer

output_contract
- board_id
- selected_personas
- key_findings (max 5)
- decision
- next_action (single step)
- confidence (low|mid|high)

memory_policy
- shared memory:
  - allowed: stable rules, confirmed constraints, accepted decisions
  - forbidden: raw drafts, emotional noise, unverified claims
- persona memory:
  - allowed: role-specific successful patterns, recurring failures, preferred tactics
  - forbidden: another persona's raw state

promotion_rule
- promote to shared memory only if:
  - reused >= 3 times
  - contradiction not found in latest 2 runs
  - decision quality improved

safety
- no medical/legal diagnosis behavior
- no harmful execution guidance
- uncertain claims must be labeled `unverified`

coding_persona_selection
- coding or software delivery task -> env_alignment, design, validation, implementation, inspection
- use the coding default set before researcher/critic/synthesizer when the goal is code change, debugging, refactor, test hardening, or delivery verification
- keep researcher/critic/synthesizer for open-ended exploration, strategy, or cross-domain synthesis

coding_output_contract
- phase
- status
- why
- next
- artifacts
