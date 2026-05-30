# DECISION TABLES

## purpose

This file fixes repeated verification judgments.

`FUNCTION_PACKS.md` defines the work flow.
`DECISION_TABLES.md` defines how labels are chosen inside that flow.

This is not a log.
This is a reusable decision surface.

## shared rules

- Do not upgrade proof level without evidence.
- Do not close as `complete` when blocking or unverified work remains.
- Do not hide missing target, missing success criteria, or missing evidence.
- If a table and a free-form judgment disagree, follow the table and report the conflict.

## proof_level_decision

| label | use when | do not use when |
| --- | --- | --- |
| `not_checked` | the target was not opened, read, or tested | any direct inspection happened |
| `read_checked` | the target or entry files were read, but no structure/test check was performed | required files, links, commands, or outputs were checked |
| `static_checked` | files, links, required surfaces, contracts, or text consistency were inspected | a real command, tool, fresh boot, or runtime flow was executed |
| `dry_run_checked` | the flow was simulated without side effects or actual runtime execution | the result depends on real execution |
| `runtime_checked` | a relevant command, tool, script, test, or live boot path was actually run and the result was observed | only file reading or static inspection happened |
| `user_confirmed` | the user reports external/live behavior that the verifier cannot directly observe | the user did not explicitly confirm it |

## severity_decision

| label | use when | examples |
| --- | --- | --- |
| `blocking` | the core purpose cannot safely proceed | missing boot entry, missing required surface, broken path basis that prevents use, unsafe action boundary |
| `major` | the core can proceed but a required contract is weak or misleading | proof level overstatement, missing revalidation path, source boundary ambiguity, repeated judgment without table |
| `minor` | the system works but consistency or usability is weaker than expected | read order mismatch, naming drift, missing example, weak wording |
| `note` | improvement idea or non-blocking observation | optional polish, future extension, documentation clarity |

## route_decision

| situation | first route |
| --- | --- |
| unknown target | ask for or identify the target before judging |
| brain/package validation | `START_HERE.md -> MAP.md -> LOCAL_RULEBOOK.md -> FUNCTION_PACKS.md -> OUTPUT_CONTRACT.md -> ACCEPTANCE_TESTS.md` |
| code validation | read scope, run or identify tests, then inspect changed files |
| document validation | read entry, map, purpose, audience, and output contract |
| release hygiene | run available release script, then scan for local paths, generated files, and cache folders |

## stop_or_close_decision

| condition | close_status | reason |
| --- | --- | --- |
| target missing | `blocked` | cannot verify an unnamed target |
| success criteria missing and cannot be inferred safely | `blocked` | cannot judge pass/fail without criteria |
| blocking finding remains | `blocked` | core use is unsafe or impossible |
| fix applied but revalidation not run | `partial` | change exists but proof is incomplete |
| static checks pass but runtime was not exercised | `partial` | usable structure, not full runtime proof |
| requested proof level achieved and no blocking/major issue remains | `complete` | success criteria are met |
| evidence is insufficient for the claim | `not_verified` | no valid proof boundary |

## revalidation_decision

| changed area | revalidate |
| --- | --- |
| boot/read order | `START_HERE.md`, `BOOT.md`, `MAP.md` |
| source/path binding | `SOURCE_BINDINGS.md`, `path_basis`, referenced paths |
| function pack flow | `FUNCTION_PACKS.md`, failure output, default combinations |
| decision labels | `DECISION_TABLES.md`, `OUTPUT_CONTRACT.md`, affected acceptance tests |
| output report shape | `OUTPUT_CONTRACT.md`, sample report fields |
| package release surface | release script, local path scan, generated file scan, cache folder scan |
| code or script | run the closest available test or command; if unavailable, label as `static_checked` only |

## sufficiency_decision

| request shape | sufficient layer |
| --- | --- |
| one small control action | function |
| related small control actions | function pack |
| ordered internal mechanism with verification gates | engine |
| user-facing repeatable procedure | skill |
| persistent identity, memory surface, output contract, and repeated local work | brain |
| existing brain needs one bounded capability | brain component |

## report_decision

Always include:

```text
target:
goal:
success_criteria:
proof_level:
findings:
revalidation:
remaining_risks:
close_status:
next_action:
```

If no issue is found, say no findings were found and state the remaining proof boundary.
