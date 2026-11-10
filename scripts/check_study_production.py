#!/usr/bin/env python3
"""Exercise both study/podcast pilots and their offline GenFM exports."""

from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/check_visual_assets.py")], cwd=ROOT, check=True)
    output = ROOT / ".learning-output"
    output.mkdir(exist_ok=True)
    # The fixed parent stays inside this repository. TemporaryDirectory owns only
    # the newly created run folder and removes it after the smoke check.
    with tempfile.TemporaryDirectory(prefix="validation-", dir=output) as temporary:
        run = Path(temporary)
        for exam, slug in (("AZ-900", "az-900-governance"), ("DP-900", "dp-900-data-decisions")):
            pilot = run / slug
            commands = [
                ["build_study_pack.py", "prepare", "--exam-code", exam, "--output-dir", str(pilot / "authoring")],
                ["build_study_pack.py", "build", "--content", f"data/study-content/{slug}.json", "--output-dir", str(pilot / "package")],
                ["build_study_pack.py", "check", "--package", str(pilot / "package")],
                ["build_study_podcast.py", "prepare", "--package", str(pilot / "package"), "--output-dir", str(pilot / "podcast")],
                ["build_study_podcast.py", "plan", "--episode-dir", str(pilot / "podcast" / "part-01")],
                ["export_genfm_source.py", "build", "--package", str(pilot / "package"), "--output-dir", str(pilot / "genfm")],
                ["export_genfm_source.py", "check", "--export", str(pilot / "genfm")],
            ]
            for script, *arguments in commands:
                subprocess.run([sys.executable, str(ROOT / "scripts" / script), *arguments], cwd=ROOT, check=True)
        subprocess.run(
            [sys.executable, str(ROOT / "examples/visual-exercises/dp-900-data-freshness/build.py"), "--check"],
            cwd=ROOT, check=True,
        )
        for slug in ("az-900-governance-scope", "dp-900-sql-choices"):
            subprocess.run(
                [sys.executable, str(ROOT / "examples/visual-exercises" / slug / "build.py"), "--check"],
                cwd=ROOT, check=True,
            )


if __name__ == "__main__":
    main()
