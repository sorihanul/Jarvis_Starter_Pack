#!/usr/bin/env python3
"""Run all current real-trial checks for manufactured skill skeletons."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "SKILL_MANUFACTURING_REAL_TRIALS_OUTPUT_v0_1.json"


COMMANDS = [
    {
        "trial": "SOURCE_REVIEW_REAL_TRIAL_v0_1",
        "cmd": [
            sys.executable,
            str(ROOT / "SOURCE_REVIEW_SKILL_SAMPLE_v0_1" / "REAL_TRIALS_v0_1" / "source_review_real_trial_runner.py"),
            str(ROOT / "SOURCE_REVIEW_SKILL_SAMPLE_v0_1" / "REAL_TRIALS_v0_1" / "SOURCE_REVIEW_REAL_TRIAL_FIXTURES_v0_1.json"),
        ],
    },
    {
        "trial": "PROMPT_VALIDATION_REAL_TRIAL_v0_1",
        "cmd": [
            sys.executable,
            str(ROOT / "PROMPT_VALIDATION_SKILL_SAMPLE_v0_1" / "REAL_TRIALS_v0_1" / "prompt_validation_real_trial_runner.py"),
            str(ROOT / "PROMPT_VALIDATION_SKILL_SAMPLE_v0_1" / "REAL_TRIALS_v0_1" / "PROMPT_VALIDATION_REAL_TRIAL_FIXTURES_v0_1.json"),
        ],
    },
    {
        "trial": "WIKI_NOTE_INTAKE_REAL_TRIAL_v0_1",
        "cmd": [
            sys.executable,
            str(ROOT / "WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1" / "REAL_TRIALS_v0_1" / "wiki_note_intake_real_trial_runner.py"),
            str(ROOT / "WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1" / "REAL_TRIALS_v0_1" / "WIKI_NOTE_INTAKE_REAL_TRIAL_FIXTURES_v0_1.json"),
        ],
    },
]


def main() -> int:
    results = []
    for item in COMMANDS:
        run = subprocess.run(item["cmd"], cwd=ROOT, text=True, capture_output=True)
        parsed = json.loads(run.stdout) if run.stdout.strip() else None
        results.append(
            {
                "trial": item["trial"],
                "returncode": run.returncode,
                "stdout": parsed,
                "stderr": run.stderr.strip(),
                "passed": run.returncode == 0 and parsed is not None and parsed.get("overall") == "PASS",
            }
        )

    passed = sum(1 for item in results if item["passed"])
    summary = {
        "suite": "SKILL_MANUFACTURING_REAL_TRIALS_v0_1",
        "trials": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "overall": "PASS" if passed == len(results) else "FAIL",
        "results": results,
    }
    OUTPUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
