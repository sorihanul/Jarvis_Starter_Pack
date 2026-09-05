param(
  [string]$Root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"
$sourceRoot = (Resolve-Path -LiteralPath $Root).Path
$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$fixtureRoot = Join-Path $tempBase ("jarvis-release-check-" + [guid]::NewGuid().ToString("N"))
$shellPath = (Get-Process -Id $PID).Path
$utf8 = New-Object System.Text.UTF8Encoding($false)
$results = New-Object System.Collections.Generic.List[object]

try {
  New-Item -ItemType Directory -Path $fixtureRoot | Out-Null
  Get-ChildItem -LiteralPath $sourceRoot -Force |
    Where-Object { $_.Name -ne ".git" } |
    Copy-Item -Destination $fixtureRoot -Recurse -Force

  $checker = Join-Path $fixtureRoot "scripts/release_check.ps1"
  $fixtureFile = Join-Path $fixtureRoot "release-check-fixture.txt"
  $cases = @(
    @{ name = "normal_whitespace"; content = "first`tcolumn`r`nsecond`nthird"; expected_code = $null; expected_line = $null },
    @{ name = "nul_in_route"; content = "route`n$([char]0)1_Modules/example.md"; expected_code = "U+0000"; expected_line = 2 },
    @{ name = "single_line_control"; content = "broken$([char]7)text"; expected_code = "U+0007"; expected_line = 1 }
  )

  foreach ($case in $cases) {
    [IO.File]::WriteAllText($fixtureFile, $case.content, $utf8)
    $output = & $shellPath -NoProfile -NonInteractive -File $checker -Root $fixtureRoot
    $exitCode = $LASTEXITCODE
    $report = ($output -join [Environment]::NewLine) | ConvertFrom-Json

    if ($null -eq $case.expected_code) {
      if ($exitCode -ne 0 -or $report.ok -ne $true) {
        throw "Release checker rejected the clean fixture: $($output -join ' ')"
      }
    } else {
      $expected = "unexpected control character $($case.expected_code) in *release-check-fixture.txt line $($case.expected_line)"
      $matchingFailures = @($report.failures | Where-Object { $_ -like $expected })
      if ($exitCode -ne 1 -or $report.ok -ne $false -or $report.failure_count -ne 1 -or $matchingFailures.Count -ne 1) {
        throw "Release checker did not isolate the expected failure for $($case.name): $($output -join ' ')"
      }
    }

    $results.Add([pscustomobject]@{ case = $case.name; passed = $true }) | Out-Null
  }
} finally {
  # Only remove the unique fixture directory directly under the system temp root.
  if (Test-Path -LiteralPath $fixtureRoot) {
    $resolvedFixture = (Resolve-Path -LiteralPath $fixtureRoot).Path
    $fixtureParent = [IO.Path]::GetDirectoryName($resolvedFixture)
    $expectedParent = $tempBase.TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    if ($fixtureParent -ne $expectedParent -or
        $resolvedFixture -ne [IO.Path]::GetFullPath($fixtureRoot) -or
        [IO.Path]::GetFileName($resolvedFixture) -notmatch '^jarvis-release-check-[a-f0-9]{32}$') {
      throw "Refusing to remove an unexpected fixture path."
    }
    Remove-Item -LiteralPath $resolvedFixture -Recurse -Force
  }
}

[pscustomobject]@{
  ok = $true
  case_count = $results.Count
  cases = $results
} | ConvertTo-Json -Depth 5
