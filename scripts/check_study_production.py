#!/usr/bin/env python3
"""Check the recorded episodes and exercise the study-pack and GenFM pilots."""

from hashlib import sha256
from pathlib import Path
import subprocess
import sys
import tempfile

from build_study_podcast import load_episode, require_review
from study_material import read_json


ROOT = Path(__file__).resolve().parents[1]


def check_recorded_series(slug: str) -> None:
    series_dir = ROOT / "examples/podcasts" / slug
    series = read_json(series_dir / "series.json")
    units = read_json(ROOT / "data/study-content" / f"{slug}.json")["units"]
    recorded_units = []
    for index, entry in enumerate(series["episodes"], 1):
        part = f"part-{index:02d}"
        if entry["path"] != part:
            raise ValueError(f"{slug} has an unexpected episode path")
        episode = series_dir / part
        metadata, script, _ = load_episode(episode)
        require_review(episode, metadata)
        recording = read_json(episode / "recording.json")
        if (recording["package_manifest_sha256"] != metadata["package_manifest_sha256"]
                or recording["script_sha256"] != metadata["script_sha256"]
                or recording["transcript_sha256"] != metadata["transcript_sha256"]
                or recording["mp3_sha256"] != sha256((episode / "episode.mp3").read_bytes()).hexdigest()):
            raise ValueError(f"Recording differs from its reviewed script, transcript or audio in {episode}")
        audio_check = recording["audio_check"]
        if audio_check["audio_sha256"] != recording["mp3_sha256"]:
            raise ValueError(f"Audio check refers to a different recording in {episode}")
        if audio_check["material_omissions_or_number_changes_outstanding"] != 0:
            raise ValueError(f"Recording has unresolved delivery errors in {episode}")
        if (entry["unit_ids"] != script["unit_ids"] or script["part"] != index
                or script["total_parts"] != len(series["episodes"])):
            raise ValueError(f"Episode index differs from the recorded series in {episode}")
        recorded_units.extend(script["unit_ids"])
    if recorded_units != [unit["id"] for unit in units]:
        raise ValueError(f"{slug} recordings do not cover the authored units in order")
    print(f"Verified {len(series['episodes'])} recorded episodes for {slug}.")


def main() -> None:
    for slug in ("az-900-cloud-decisions", "dp-900-data-in-motion", "az-900-governance", "dp-900-data-decisions"):
        check_recorded_series(slug)
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
