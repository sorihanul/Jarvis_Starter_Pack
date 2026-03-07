# HOOKS LITE v1.0 (Starter)

## Goal
Add minimal safety/quality hooks for beginner-friendly coding workflow.

## Enable Hooks (Lite)
1. Bash Guard
- avoid destructive wildcard/delete commands

2. DB Guard
- avoid irreversible schema/data commands by default

3. Write Check
- after editing files, run one verification step

4. Session Wrap-up
- summarize changed files + one verification line

## Recommended Command
"Run coding steps with Hooks Lite enabled: Bash Guard, DB Guard, Write Check, Session Wrap-up."

## Behavior
- If risky command detected: stop and ask for explicit approval.
- If verification fails: route to inspection before completion.
