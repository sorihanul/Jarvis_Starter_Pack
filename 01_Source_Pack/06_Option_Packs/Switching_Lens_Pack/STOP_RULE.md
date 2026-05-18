# Stop Rule

Stop lens switching when:

```text
one lens has answered the task
the next lens would only restate the same point
the user asked for action, not more analysis
the task needs a skill, not another viewpoint
the task needs a domain brain, not a generic lens
the task needs separate-thread handoff
```

Escalate to another pack when:

```text
tool or permission risk -> Action_Permission_Pack
proof and acceptance risk -> Verification_and_Proof_Pack
skill import risk -> Skill_Trust_Gate_Pack
external source risk -> Source_Command_Filter_Pack
domain brain handoff -> Brain_Routing_and_Handoff_Pack
coding role sequence -> Switching_Coding_Pack
```

Never use lens switching as an excuse to avoid a concrete next action.
