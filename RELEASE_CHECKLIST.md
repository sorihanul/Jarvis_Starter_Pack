# Jarvis Starter Pack v3 Release Checklist

## Purpose

Use this checklist before publishing or pushing the v3 branch.

This package is a document-first starter.
Release quality means the folder can be opened by a host model and used without private local paths, missing entry files, or unclear routing.

## 1. Boot Surface

Pass if these files exist:

```text
README.md
START_HERE.md
BOOT.md
MAP.md
QUICK_START_3_MIN.md
INSTALL_AND_USAGE_GUIDE.md
ACCEPTANCE_TESTS.md
```

Pass if `BOOT.md` leads to:

```text
00_Orchestrator/Jarvis_Main_Brain/BOOT.md
00_Orchestrator/LOCAL_RULEBOOK.md
00_Orchestrator/MEMORY_MAP.md
00_Orchestrator/SESSION_CARD.md
00_Orchestrator/Jarvis_Main_Brain/BRAIN.md
00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md
00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md
```

Fail if the user must know internal folder names before saying `부팅해`.

## 2. v3 Functionization Surface

Pass if the v3 definition is visible from the main entry files:

```text
Function
-> smallest action

Function Pack
-> related smallest action-unit group

Function Pack Group
-> Engine / Skill / Brain component depending on use
```

Pass if these source files exist:

```text
01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_BOUNDARY_v0_1.md
01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_EXAMPLE_CATALOG_v0_1.md
01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_PROMOTION_MATRIX_v0_1.md
```

Fail if v3 is described only as a fixed basic-function list.

## 3. Source Boundary

Pass if:

```text
00_Orchestrator = boot, work, logs, capsules, canon memory
01_Source_Pack = source material
```

Fail if current user work is written into:

```text
01_Source_Pack/TASKS
01_Source_Pack/LOGS
01_Source_Pack/CAPSULES
01_Source_Pack/01_Modules
```

## 4. Private Path Hygiene

Pass if no release-facing file requires:

```text
private local workspace path
private user home path
internal source-system folder name
previous package branch name
```

Fail if the package cannot be understood outside the original machine.

Text files must not contain unexpected control characters such as NUL. Tabs and normal line endings are allowed.

## 5. Generated File Hygiene

Pass if no generated cache or local DB files are included:

```text
__pycache__/
*.pyc
*.sqlite
*.sqlite-shm
*.sqlite-wal
```

## 6. Acceptance Tests

Pass if `ACCEPTANCE_TESTS.md` covers:

```text
boot
natural-language request normalization
AILO functionization
function pack classification
function pack preflight before brain build
option pack selection
source/work boundary
brain build
canon memory
release hygiene
context rehydration and no-false-completion lock
```

## 6-1. Claim Ceiling

Before saying a release is ready, pass if the reported claim matches evidence:

```text
static files checked -> static_checked
templates created but not run -> candidate_created
real project not run -> not runtime_validated
public/private boundary checked -> boundary_checked
release check script passed -> hygiene_passed for current tree only
```

Fail if:

```text
static_checked is reported as runtime_validated
candidate_created is reported as reference_ready
local private test material is reported as public_ready
tests not run are reported as passed
```

## 7. Pre-push Commands

Run from the parent repository when possible:

```powershell
$patterns = @("F:" + "\LLM", "F:/" + "LLM", "C:" + "\Users", "Starter" + "_F_System", "Jarvis_Starter_Pack" + "_v2", "jarvis-starter-pack" + "-v2")
$patterns | ForEach-Object { rg -n --fixed-strings $_ .\Jarvis_Starter_Pack_v3 }
Get-ChildItem -LiteralPath .\Jarvis_Starter_Pack_v3 -Recurse -Force -Directory -Filter "__pycache__"
Get-ChildItem -LiteralPath .\Jarvis_Starter_Pack_v3 -Recurse -Force -File | Where-Object { $_.Name -match "\.pyc$|\.sqlite$|\.sqlite-shm$|\.sqlite-wal$" }
git status --short -- Jarvis_Starter_Pack_v3
```

Or run the bundled release check from the v3 root:

```powershell
.\scripts\release_check.ps1
```

After changing the release checker, run its temporary-copy regression tests:

```powershell
.\scripts\test_release_check.ps1
```

## Close Rule

Do not push if:

```text
boot path is unclear
v3 functionization definition is missing
source boundary is mixed
private local path remains
unexpected control character remains
generated cache remains
acceptance tests do not cover function pack classification
claim ceiling is stronger than evidence
```
