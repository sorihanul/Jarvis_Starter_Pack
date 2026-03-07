# ADVANCED FACTORY ADD-ON GUIDE v1.0

Purpose:
- Keep Starter Pack simple for beginners.
- Provide an optional upgrade path for users who want modular factory operation.

---

## 1) Positioning
- Starter Pack core: minimal, easy, immediate use.
- This add-on: advanced operating layer (optional).

If you are new, skip this file first.
If you already run multi-agent workflows, use this guide.

---

## 2) What This Add-on Introduces
1. `TRIPLE_FACTORY_FLOW`
- MetaSentence -> PatternOS.Unified -> PatternOS.MeaningOS

2. `STANDARD_FACTORY`
- Spec-first packaging before implementation
- Required outputs:
  - ModuleCard
  - AiloContract
  - FunctionPack
  - RuntimeBinding
  - Acceptance

3. `AILO_RUNTIME_BRIDGE`
- Controlled runtime execution path for AILO intents
- Recommended invocation: `--json-file`

---

## 3) Recommended Order (Advanced)
1. Define intent and constraints
2. Run `TRIPLE_FACTORY_FLOW`
3. Run `STANDARD_FACTORY`
4. Implement only after required outputs are complete
5. Log decisions in Agenda and finalize agreement

---

## 4) Canon Reference Paths (Current Workspace)
- `<YOUR_BRAIN_PATH>\02_Modules\MODULE_TRIPLE_FACTORY_FLOW.v0.1.md`
- `<YOUR_BRAIN_PATH>\02_Modules\MODULE_STANDARD_FACTORY.v0.1.md`
- `<YOUR_BRAIN_PATH>\02_Modules\MODULE_AILO_RUNTIME_BRIDGE.v0.1.md`
- `<YOUR_AGENT_PATH>\skills\ailo_bridge\scripts\ailo_interpreter.py`

Note:
- These paths are examples from the maintainer workspace.
- In your environment, keep the same structure and adapt absolute paths.

---

## 5) Agenda Rule (Advanced)
- Use single-file board:
  - `AGENTS/Agenda/AGENDA_LOG.md`
- Final agreement naming:
  - `AGREEMENT_YYYYMMDD_HHMMSS_TOPIC_STATUS.md`
- STATUS:
  - `APPROVED | REJECTED | OBSOLETE | DRAFT`

---

## 6) Safety Baseline
- Keep runtime policy safe by default.
- Do not bypass destructive-command guard unless explicitly intended.
- Use archive-first replacement for major updates.

---

## 7) Adoption Strategy
- Week 1: keep Starter core only
- Week 2: add Agenda discipline
- Week 3: adopt `STANDARD_FACTORY`
- Week 4: adopt full `TRIPLE_FACTORY_FLOW`

This staged rollout avoids overload and preserves Starter Pack philosophy.
