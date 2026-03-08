# Society Prototype v0.1 (Cognitive Vector)

Purpose
- Operate multiple cognitive-vector personas in a single folder.
- Keep memory separated by persona while sharing only approved consensus.

Quick Start
1. Open `protocols/SOCIETY_RUNTIME_PROTOCOL_v0.1.md`.
2. Add a society note in `board/SOCIETY_BOARD.md`.
3. Select persona(s) from `personas/*.md`.
4. Write outputs into `runs/` and update memory files.
5. Use `announcements/` only for society-wide broadcast notices.

Design Rules
- Shared memory is shallow and policy-level only.
- Persona memory is deep and isolated per persona.
- Cross-persona sharing is allowed only through shared memory summary.

Files
- `protocols/SOCIETY_RUNTIME_PROTOCOL_v0.1.md`
- `protocols\SOCIETY_ANNOUNCEMENT_POLICY_v1.0.md`
- `personas/researcher_vector_v0.1.md`
- `personas/critic_vector_v0.1.md`
- `personas/synthesizer_vector_v0.1.md`
- `memory/shared_memory_v0.1.json`
- `memory/persona/*.json`
- `board/SOCIETY_BOARD.md`
- `announcements/SOCIETY_ANNOUNCEMENTS.md`

Coding Default Set
- `personas/coding_env_alignment_vector_v1.0.md`
- `personas/coding_design_vector_v1.0.md`
- `personas/coding_validation_vector_v1.0.md`
- `personas/coding_implementation_vector_v1.0.md`
- `personas/coding_inspection_vector_v1.0.md`
- Intended for coding workflows that need `environment -> design -> validation -> implementation -> inspection` discipline.
