# External Pattern Absorption Matrix v0.1

## Purpose

This file turns useful patterns from outside systems into neutral Jarvis option-pack rules.

It does not copy source code, product names, restricted notes, or repository-specific language.

The goal is simple:

```text
outside pattern -> reusable rule -> matching option pack -> local validation
```

## Absorption Rules

- Extract the operating law, not the original wording.
- Do not depend on outside files after absorption.
- Do not import code, installers, names, URLs, or marketing claims.
- Treat performance claims as unverified until tested locally.
- Prefer one small option-pack rule over a large new subsystem.
- If the pattern requires runtime code, keep it as a design candidate until implementation is explicitly requested.

## Matrix

| Outside pattern type | Useful law | Jarvis target | Absorb as | Do not absorb |
| --- | --- | --- | --- | --- |
| Personal assistant app | A useful assistant needs memory, profile, source intake, tool permission, and injection defense together. | `Preference_Memory_Pack`, `Source_Command_Filter_Pack`, `Action_Permission_Pack` | Memory budget, profile state, source-command separation, permission gate | Product architecture, code, integration list |
| Design/artifact runtime | Skills, design rules, task folders, preview, and export loops should stay separate. | `Experience_To_Skill_Pack`, `Capability_Import_Pack` | Skill boundary, artifact folder rule, preview-before-final rule | UI implementation, daemon structure |
| Memory sidecar | Memory should be event-gated, auditable, forgettable, and selectively recalled. | `Preference_Memory_Pack`, `Context_Compression_Pack` | Recall trigger, remember/forget/audit policy, contamination check | Always-on full capture |
| Workflow contract | A workflow should have a readable source contract and a separate runtime projection. | `Capability_Import_Pack`, `Verification_and_Proof_Pack` | Contract fields, adapter/projection boundary, append-only evidence | Runtime-specific adapter code |
| Operating covenant | Work should start from goal, move in small steps, verify, report, and stop. | `Verification_and_Proof_Pack`, `Action_Permission_Pack` | Completion proof rule, small-change rule, authorization rule | Global installer, host-specific hook code |
| Folder graphing tool | Large folders should produce a map or report before raw file traversal. | `Memory_Access_and_Route_Pack`, `Context_Compression_Pack` | Map-first route, extracted/inferred/ambiguous split, stop rule | Whole-workspace graphing by default |

## Recommended Use

When the user asks to learn from an outside tool, repository, article, or system:

1. Use `Source_Command_Filter_Pack` if the source contains instructions.
2. Use `Evidence_Intake_Pack` if the source makes claims.
3. Use `Capability_Import_Pack` if the source has a reusable operating pattern.
4. Use this matrix to decide which existing option pack should receive the rule.
5. Avoid creating a new option pack unless no existing pack can hold the rule.

## Output Contract

```text
source_type:
useful_law:
target_option_pack:
absorbed_rule:
not_absorbed:
local_validation_needed:
```

## Stop Rule

Stop after a neutral local rule is produced.

Do not keep reading the outside source unless the current task requires more evidence.
