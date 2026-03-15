# ORCHESTRATOR

- execution_mode: sequential | review-heavy | hybrid
- participants:
  - design
  - implementation
  - review
- handoff:
  - design -> implementation
  - implementation -> review
- stop_conditions:
  - scope ambiguity
  - destructive change
  - failed validation
