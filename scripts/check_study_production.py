#!/usr/bin/env python3
"""Exercise the authored example through both production commands without APIs."""

from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    output = ROOT / ".learning-output"
    output.mkdir(exist_ok=True)
    # The fixed parent stays inside this repository. TemporaryDirectory owns only
    # the newly created run folder and removes it after the smoke check.
    with tempfile.TemporaryDirectory(prefix="validation-", dir=output) as temporary:
        run = Path(temporary)
        commands = [
            ["build_study_pack.py", "prepare", "--exam-code", "AZ-900", "--output-dir", str(run / "authoring")],
            ["build_study_pack.py", "build", "--content", "data/study-content/az-900-governance.json", "--output-dir", str(run / "package")],
            ["build_study_pack.py", "check", "--package", str(run / "package")],
            ["build_study_podcast.py", "prepare", "--package", str(run / "package"), "--output-dir", str(run / "podcast"), "--target-minutes", "15"],
            ["build_study_podcast.py", "plan", "--episode-dir", str(run / "podcast" / "part-01")],
        ]
        for script, *arguments in commands:
            subprocess.run([sys.executable, str(ROOT / "scripts" / script), *arguments], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
