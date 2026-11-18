#!/usr/bin/env python3
"""Rebuild or check this fixed, reviewed visual exercise; no network or AI calls."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import textwrap
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from study_material import (  # noqa: E402
    json_text, load_package, read_json, safe_path, text_sha256,
)

PACKAGE = "examples/study-packs/dp-900-data-decisions"
UNIT_ID = "analytics-to-insight"
REVIEWED_UNIT_SHA256 = "68289c5b5f879ea8f6c2db3d0cd21172f6853e053bd5d7905b51a1e60e9ae845"
STAGES = (
    ("10:00", "Sale committed", "The source records the new sale."),
    ("10:03", "Ingestion done", "The pipeline has received the sale."),
    ("10:05", "Transform done", "The prepared data includes the sale."),
    ("10:10", "Report checked", "The sale is missing from the report."),
    ("10:15", "Refresh done", "The Import model now includes the sale."),
)
PANELS = {
    "study": (
        ("01  FIND THE BOUNDARY", "The refresh is incomplete", "At 10:10, ingestion and transformation are done. The stated model refresh completes at 10:15."),
        ("02  EXPLAIN THE INTERVAL", "15 minutes to the model", "10:00 to 10:15: 15 minutes. Transformation to completed refresh: 10 minutes. These are scenario timings."),
        ("03  CHOOSE THE FIRST CHECK", "Inspect refresh and mode", "Check the model refresh and data access mode. Changing the chart does not refresh the imported data."),
    ),
    "practice": (
        ("01  FIND THE BOUNDARY", "Explain the missing sale", "At 10:10, which steps are complete? Which relevant step has not completed? Explain using two timestamps."),
        ("02  EXPLAIN THE INTERVAL", "Calculate both intervals", "How long from sale to updated model? How long from completed transformation to updated model?"),
        ("03  CHOOSE THE FIRST CHECK", "Choose and justify a check", "Would you inspect the chart design or the model refresh and access mode first? Explain your choice."),
    ),
}
QUESTION = "At 10:10, the report does not include the 10:00 sale. Why?"
CAUTION = "An updated model does not guarantee that an already-open report display updates at that instant."
SCOPE = "Illustrative Import workflow only. Invented times; no service guarantee. VERIFY CURRENT: access mode and refresh settings."


def text(x: int, y: int, value: str, size: int = 18, color: str = "#163047", weight: int = 400) -> str:
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(value)}</text>'


def paragraph(x: int, y: int, value: str, width: int, size: int = 18, color: str = "#334e63", line: int = 27) -> str:
    return "\n".join(text(x, y + index * line, row, size, color) for index, row in enumerate(textwrap.wrap(value, width)))


def svg(mode: str) -> str:
    panels = PANELS[mode]
    description = " ".join([
        "DP-900. " + mode.title() + " version. " + QUESTION,
        "The invented scenario assumes a successful 10:15 Import-model refresh includes the sale.",
        *[f"{time}: {title}. {detail}" for time, title, detail in STAGES],
        "Events are shown in order; spacing is not elapsed time.",
        *[f"{heading}. {title}. {detail}" for heading, title, detail in panels],
        CAUTION, SCOPE, "AI-generated draft; human review pending. Official blueprint is authoritative.",
    ])
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1120" viewBox="0 0 1200 1120" role="img" aria-labelledby="title description">',
        f'<title id="title">DP-900 data freshness — {mode} exercise</title>',
        f'<desc id="description">{escape(description)}</desc>',
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#668093"/></marker></defs>',
        '<rect width="1200" height="1120" fill="#f3f6f7"/>',
        '<rect width="1200" height="194" fill="#102b40"/>',
        '<rect x="64" y="36" width="5" height="22" fill="#70e0be"/>',
        '<g font-family="Arial, sans-serif">',
        text(82, 53, "DP-900  /  DATA DETECTIVE 01", 16, "#bceedd", 700),
        text(64, 113, "Why is the sale missing?", 44, "#ffffff", 700),
        text(64, 151, "Follow one sale through an illustrative Power BI Import workflow.", 21, "#d7e6ef"),
        '<rect x="937" y="29" width="199" height="34" rx="17" fill="#23485e"/>',
        text(959, 52, mode.upper() + " VERSION", 15, "#ffffff", 700),
        '<rect x="64" y="222" width="1072" height="112" rx="16" fill="#fff1d5" stroke="#bd8432"/>',
        text(86, 252, "THE OBSERVATION", 14, "#68430e", 700),
        text(86, 285, QUESTION, 25, "#513612", 700),
        text(86, 313, "The times below are invented. The 10:15 refresh successfully includes this sale.", 18, "#68430e"),
        text(64, 386, "Trace the evidence", 28, weight=700),
        text(682, 384, "Event sequence — spacing is not elapsed time", 17),
        '<path d="M154 470 H1050" fill="none" stroke="#668093" stroke-width="3" marker-end="url(#arrow)"/>',
    ]
    for index, (time, title, detail) in enumerate(STAGES):
        x = 64 + index * 220
        observation = index == 3
        color = "#85500a" if observation else "#0e6654"
        fill = "#fff1d5" if observation else "#ffffff"
        out += [
            text(x + 43, 438, time, 27, color, 700),
            f'<circle cx="{x + 96}" cy="470" r="15" fill="{color}"/>',
            text(x + 91, 476, "?" if observation else str(index + 1 if index < 3 else 4), 17, "#ffffff", 700),
            f'<rect x="{x}" y="502" width="192" height="143" rx="13" fill="{fill}" stroke="#93a8b6"/>',
            text(x + 14, 532, title, 19, weight=700),
            paragraph(x + 14, 562, detail, 19, 17, line=24),
        ]
    out += [text(64, 701, "Read the reasoning" if mode == "study" else "Pause. Work it out before looking at the study version.", 25, weight=700)]
    for index, (heading, title, detail) in enumerate(panels):
        x = 64 + index * 365
        out += [
            f'<rect x="{x}" y="726" width="342" height="240" rx="14" fill="#ffffff" stroke="#b6c6cf"/>',
            text(x + 18, 755, heading, 13, "#0e6654", 700),
            text(x + 18, 790, title, 20, weight=700),
            paragraph(x + 18, 820, detail, 32, 17, line=25),
        ]
        if mode == "practice":
            out.append(f'<path d="M{x + 18} 925 H{x + 324} M{x + 18} 949 H{x + 324}" stroke="#93a8b6" fill="none"/>')
    out += [
        text(64, 998, CAUTION, 16),
        text(64, 1025, SCOPE, 15),
        text(64, 1056, "Independent AI-assisted draft · Human review pending · Selected objectives · Accepted baseline: July 21, 2026", 14),
        text(64, 1081, "Sources: Microsoft Learn — Power BI semantic models; DP-900 official study guide (authoritative exam scope).", 14),
        text(64, 1104, "Exact source links, objective mapping and text alternative: accompanying README. No Azure or Power BI execution.", 14),
        "</g></svg>\n",
    ]
    return "\n".join(out)


def compile_artifacts() -> dict[str, str]:
    package = safe_path(ROOT, PACKAGE)
    pack = load_package(package, ROOT)
    unit = next(unit for unit in read_json(package / "units.json")["units"] if unit["id"] == UNIT_ID)
    unit_hash = text_sha256(json_text(unit))
    if unit_hash != REVIEWED_UNIT_SHA256:
        raise ValueError("The source unit changed. Review the brief and visual content before updating its binding.")
    artifacts = {f"{mode}.svg": svg(mode) for mode in PANELS}
    manifest = {
        "schema_version": 1, "exam_code": pack["exam_code"], "unit_id": UNIT_ID,
        "content_status": "ai-generated-draft; human review pending",
        "source_package": PACKAGE, "source_unit_sha256": unit_hash,
        "source_package_manifest_sha256": text_sha256((package / "manifest.json").read_text(encoding="utf-8")),
        "builder_sha256": text_sha256(Path(__file__).read_text(encoding="utf-8")),
        "hash_normalization": "UTF-8 text; CRLF/CR normalized to LF",
        "artifacts": {name: text_sha256(value) for name, value in artifacts.items()},
    }
    return {**artifacts, "manifest.json": json_text(manifest)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare current inputs and regenerated outputs without writing")
    args = parser.parse_args()
    try:
        artifacts = compile_artifacts()
        for name, expected in artifacts.items():
            path = safe_path(HERE, name)
            if args.check:
                if text_sha256(path.read_text(encoding="utf-8")) != text_sha256(expected):
                    raise ValueError(f"Stale or modified visual artifact: {name}")
            else:
                path.write_text(expected, encoding="utf-8", newline="\n")
        print("Checked" if args.check else "Built", "DP-900 study/practice SVGs; factual and human review remain separate")
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        print(f"Visual exercise error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
