param(
  [string]$Root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"

$rootPath = (Resolve-Path -LiteralPath $Root).Path
$failures = New-Object System.Collections.Generic.List[string]

function Add-Failure {
  param([string]$Message)
  $script:failures.Add($Message) | Out-Null
}

function Test-RequiredPath {
  param([string]$RelativePath)
  $path = Join-Path $rootPath $RelativePath
  if (-not (Test-Path -LiteralPath $path)) {
    Add-Failure "missing required path: $RelativePath"
  }
}

$requiredPaths = @(
  "README.md",
  "START_HERE.md",
  "BOOT.md",
  "MAP.md",
  "QUICK_START_3_MIN.md",
  "INSTALL_AND_USAGE_GUIDE.md",
  "ACCEPTANCE_TESTS.md",
  "RELEASE_CHECKLIST.md",
  "00_Orchestrator/Jarvis_Main_Brain/BOOT.md",
  "00_Orchestrator/LOCAL_RULEBOOK.md",
  "00_Orchestrator/MEMORY_MAP.md",
  "00_Orchestrator/SESSION_CARD.md",
  "00_Orchestrator/TASKS/CURRENT_TASK.md",
  "00_Orchestrator/Jarvis_Main_Brain/BRAIN.md",
  "00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md",
  "00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md",
  "00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md",
  "00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md",
  "00_Orchestrator/CANON_MEMORY/README.md",
  "00_Orchestrator/CANON_MEMORY/FUNCTIONIZED_CANON_RULE.md",
  "00_Orchestrator/CANON_MEMORY/INDEX.md",
  "00_Orchestrator/CANON_MEMORY/CANDIDATES/README.md",
  "00_Orchestrator/CANON_MEMORY/WIKI/README.md",
  "00_Orchestrator/CANON_MEMORY/ROUTES/INDEX.md",
  "01_Source_Pack/00_Core/AILO_N_NOMINAL_FRAME_LAYER_v0_9N.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_BOUNDARY_v0_1.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_BUILD_CARD_v0_1.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/AILO_N_FRAME_USE_RULES_v0_1.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/AILO_N_PRACTICAL_USE_CARD_v0_1.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/AILO_RELATION_TOPOLOGY_PACK_v0_1.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_EXAMPLE_CATALOG_v0_1.md",
  "01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_PROMOTION_MATRIX_v0_1.md",
  "01_Source_Pack/06_Option_Packs/AILO_N_Mini_Ontology_Pack/README.md",
  "01_Source_Pack/06_Option_Packs/AILO_N_Mini_Ontology_Pack/FRAME_SCHEMA.md",
  "01_Source_Pack/06_Option_Packs/AILO_N_Mini_Ontology_Pack/TOPOLOGY_HINT_RULE.md",
  "01_Source_Pack/06_Option_Packs/AILO_N_Mini_Ontology_Pack/VALIDATION_RULE.md"
)

foreach ($relativePath in $requiredPaths) {
  Test-RequiredPath $relativePath
}

$privatePatterns = @(
  ("F:" + "\LLM"),
  ("F:/" + "LLM"),
  ("C:" + "\Users"),
  ("Starter" + "_F_System"),
  ("F " + "system"),
  ("F " + "Omega"),
  ("F" + "-Ω"),
  ("F" + "-based"),
  ("Canonical " + "F " + "source"),
  ("Society" + "_" + "Cognitive" + "_" + "Vector"),
  ("Cognitive" + "_" + "Vector"),
  ("Jarvis_Starter_Pack" + "_v2"),
  ("jarvis-starter-pack" + "-v2")
)

$textFiles = Get-ChildItem -LiteralPath $rootPath -Recurse -Force -File |
  Where-Object {
    $_.FullName -notmatch "\\.git\\" -and
    $_.Extension -in @(".md", ".txt", ".ps1", ".py", ".json", ".toml", ".yml", ".yaml", ".gitignore", ".gitattributes", "")
  }

foreach ($file in $textFiles) {
  $content = Get-Content -LiteralPath $file.FullName -Raw -ErrorAction SilentlyContinue
  foreach ($pattern in $privatePatterns) {
    if ($content -like "*$pattern*") {
      $relative = Resolve-Path -LiteralPath $file.FullName -Relative
      Add-Failure "private/internal pattern found: $pattern in $relative"
    }
  }
}

$absoluteLocalPathRegex = [regex]'(?<![A-Za-z])[A-Za-z]:[\\/][^\s\)\]\}"''<>]+'
$unexpectedControlRegex = [regex]'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]'
foreach ($file in $textFiles) {
  $lines = @(Get-Content -LiteralPath $file.FullName -ErrorAction Stop)
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($absoluteLocalPathRegex.IsMatch($lines[$i])) {
      $relative = Resolve-Path -LiteralPath $file.FullName -Relative
      Add-Failure "absolute local path found: $relative line $($i + 1)"
    }
    foreach ($match in $unexpectedControlRegex.Matches($lines[$i])) {
      $relative = Resolve-Path -LiteralPath $file.FullName -Relative
      $codePoint = "U+{0:X4}" -f [int][char]$match.Value
      Add-Failure "unexpected control character $codePoint in $relative line $($i + 1)"
    }
  }
}

$generatedFiles = Get-ChildItem -LiteralPath $rootPath -Recurse -Force -File |
  Where-Object { $_.Name -match "\.pyc$|\.sqlite$|\.sqlite-shm$|\.sqlite-wal$" }

foreach ($file in $generatedFiles) {
  $relative = Resolve-Path -LiteralPath $file.FullName -Relative
  Add-Failure "generated file remains: $relative"
}

$pycacheDirs = Get-ChildItem -LiteralPath $rootPath -Recurse -Force -Directory -Filter "__pycache__"
foreach ($dir in $pycacheDirs) {
  $relative = Resolve-Path -LiteralPath $dir.FullName -Relative
  Add-Failure "pycache directory remains: $relative"
}

$brainBuildProtocol = Join-Path $rootPath "00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md"
if (Test-Path -LiteralPath $brainBuildProtocol) {
  $protocolContent = Get-Content -LiteralPath $brainBuildProtocol -Raw
  foreach ($required in @(
    "Function Pack Preflight",
    "sufficient_layer",
    "build_allowed",
    "TASKS/PREFLIGHT_RESULT.md",
    "FUNCTION_PACKS.md",
    "runtime_flow",
    "fixed_inventory:false",
    "brain_specific_pack_design:true",
    "do_not_grow_one_function_forever:true",
    "prefer_new_purpose_pack_when_repeated:true",
    "single_use_request_is_not_new_pack:true",
    "stable_output_contract_required:true",
    "stop_condition_required:true",
    "failure_output",
    "SOURCE_BINDINGS.md",
    "Boot Route",
    "DECISION_TABLES.md",
    "repeated_decision_count",
    "path_basis",
    "brain_root_relative",
    "starter_root_relative",
    "user_given_absolute",
    "external_url",
    "why_not_function_pack",
    "why_not_engine",
    "why_not_skill",
    "why_not_brain_component"
  )) {
    if ($protocolContent -notlike "*$required*") {
      Add-Failure "brain build protocol missing preflight marker: $required"
    }
  }
}

$canonMemoryFiles = @(
  "00_Orchestrator/CANON_MEMORY/README.md",
  "00_Orchestrator/CANON_MEMORY/INDEX.md",
  "00_Orchestrator/CANON_MEMORY/WIKI/README.md",
  "00_Orchestrator/CANON_MEMORY/ROUTES/INDEX.md"
)

foreach ($relativePath in $canonMemoryFiles) {
  $path = Join-Path $rootPath $relativePath
  if (Test-Path -LiteralPath $path) {
    $content = Get-Content -LiteralPath $path -Raw
    foreach ($required in @(
      "status",
      "confidence",
      "supersedes",
      "superseded_by",
      "related",
      "conflict_check",
      "last_reviewed"
    )) {
      if ($content -notlike "*$required*") {
        Add-Failure "canon memory file missing metadata marker: $required in $relativePath"
      }
    }
  }
}

$functionPackBuildCard = Join-Path $rootPath "01_Source_Pack/01_Modules/AILO_Function_Layer/FUNCTION_PACK_BUILD_CARD_v0_1.md"
if (Test-Path -LiteralPath $functionPackBuildCard) {
  $content = Get-Content -LiteralPath $functionPackBuildCard -Raw
  foreach ($required in @(
    "purpose",
    "use_when",
    "do_not_use_when",
    "input_condition",
    "functions",
    "output_contract",
    "stop_condition",
    "failure_output",
    "promotion_condition"
  )) {
    if ($content -notlike "*$required*") {
      Add-Failure "function pack build card missing marker: $required"
    }
  }
}

$functionizedCanonRule = Join-Path $rootPath "00_Orchestrator/CANON_MEMORY/FUNCTIONIZED_CANON_RULE.md"
if (Test-Path -LiteralPath $functionizedCanonRule) {
  $content = Get-Content -LiteralPath $functionizedCanonRule -Raw
  foreach ($required in @(
    "candidate_extract",
    "promotion_gate",
    "conflict_check",
    "supersedes_bind",
    "route_update",
    "read_report_update_if_needed",
    "canon_update_result"
  )) {
    if ($content -notlike "*$required*") {
      Add-Failure "functionized canon rule missing marker: $required"
    }
  }
}

if ($failures.Count -gt 0) {
  [pscustomobject]@{
    ok = $false
    failure_count = $failures.Count
    failures = $failures
  } | ConvertTo-Json -Depth 5
  exit 1
}

[pscustomobject]@{
  ok = $true
  checked_root = $rootPath
  required_path_count = $requiredPaths.Count
  private_pattern_count = $privatePatterns.Count
} | ConvertTo-Json -Depth 5
