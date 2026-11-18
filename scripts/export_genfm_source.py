#!/usr/bin/env python3
"""Export a validated study pack as an offline ElevenLabs GenFM handoff."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from study_material import (
    NOTICE, ROOT, json_text, load_package, read_json, repository_relative,
    safe_path, text_sha256, visual_description, write_new_directory,
)


INSTRUCTIONS = """Create an educational conversation between two hosts using only the supplied
study material. One host explains; the other asks useful questions, tests a
misconception, and reasons through the supplied original practice scenarios.
Keep the unit order and teach the distinctions, decision criteria, and caveats.
Expand acronyms at first use and describe every diagram verbally. Give listeners
a moment to answer each supplied scenario before explaining its answer.

Let the content determine the length: there is no hard 15–20 minute limit. Do not
pad a short topic or omit important reasoning to hit a duration. If the material
needs multiple parts, use unit boundaries and preserve the context for each part.

Preserve the exact accepted objective baseline, selected-topic scope, uncertainty,
VERIFY CURRENT caveats, and AI-generated draft/human-review-pending status. Do
not imply complete exam coverage, human verification, or live product testing.
Use only the supplied original scenarios; do not invent or reproduce actual exam
questions. The URLs are provenance, not additional material to fetch or a reason
to change the accepted baseline. Do not invent facts or fill gaps with guesses.
Mention that the official exam blueprint is authoritative. End with a concise
recap of the decisions and distinctions taught, without reading out long URLs.
"""


def compile_export(package: Path, root: Path = ROOT) -> tuple[dict, dict[str, str]]:
    """Revalidate all upstream inputs before deriving a self-contained source."""
    package_relative = repository_relative(package, root)
    package = safe_path(root, package_relative)
    pack = load_package(package, root)
    content = read_json(safe_path(package, "units.json"))
    sources = {row["id"]: row for row in read_json(safe_path(root, "data/sources.json"))["sources"]}
    health = {row["id"]: row for row in read_json(safe_path(root, "data/source-health.json"))["sources"]}
    lines = [
        f"{pack['exam_code']} — {pack['title']}: study material for a conversation", "",
        NOTICE, "",
        f"Accepted objective baseline: {pack['baseline']}",
        f"Official exam blueprint: {pack['blueprint_url']}",
        f"Blueprint last checked in the catalog: {pack['blueprint_last_checked'] or 'Unrecorded'}.",
        "This export performs no live source refresh or new factual review.", "",
        f"Canonical library guide: {pack['guide_path']}",
        f"Guide text SHA-256: {pack['input_fingerprints'][pack['guide_path']]}",
        f"Accepted objective snapshot: {pack['objective_path']}",
        f"Scope: {pack['scope_note']}", "",
        "VERIFY CURRENT: Product details and unresolved limitations may change. "
        "This focused selection does not replace the complete guide or official objectives. "
        "Source-health records report earlier access checks, not technical verification. "
        "Matching hashes do not establish current accuracy.", "",
        "The questions below are independently authored learning scenarios, not actual exam items.", "",
    ]
    for index, unit in enumerate(content["units"], 1):
        lines += [f"Unit {index}: {unit['title']}", f"Unit ID: {unit['id']}", "", unit["summary"], ""]
        lines += ["Supporting registered sources:"]
        for source_id in unit["source_ids"]:
            source = sources[source_id]
            record = health.get(source_id, {})
            lines += [
                f"- {source['title']} [{source_id}]: {source['url']}",
                f"  Recorded access status: {record.get('status', 'Unrecorded')}; "
                f"checked at: {record.get('checked_at', 'Unrecorded')}.",
            ]
        lines += ["", "Published objectives:", *[f"- {item}" for item in unit["objectives"]]]
        lines += ["", "Canonical guide headings:", *[f"- {item}" for item in unit["guide_sections"]]]
        lines += ["", "Key points:", *[f"- {item}" for item in unit["key_points"]]]
        lines += [
            "", f"Original practice question: {unit['scenario']['question']}", "",
            f"Answer and reasoning: {unit['scenario']['answer']}", "",
            f"Diagram: {unit['visual']['title']}",
            "Diagram concepts: " + "; ".join(node["label"] for node in unit["visual"]["nodes"]),
            "Diagram relationships in words: " + visual_description(unit["visual"]), "",
        ]
    artifacts = {"source.txt": "\n".join(lines), "instructions.txt": INSTRUCTIONS}
    manifest = {
        "schema_version": 1, "format": "genfm-source-handoff",
        "exam_code": pack["exam_code"], "content_status": "ai-generated-draft",
        "package_path": package_relative,
        "package_manifest_sha256": text_sha256(safe_path(package, "manifest.json").read_text(encoding="utf-8")),
        "hash_normalization": "UTF-8 text; CRLF/CR normalized to LF",
        "artifacts": {name: text_sha256(value) for name, value in sorted(artifacts.items())},
    }
    return manifest, artifacts


def build(package: Path, output_dir: Path, root: Path = ROOT) -> dict:
    package = safe_path(root, repository_relative(package, root))
    output_dir = safe_path(root, repository_relative(output_dir, root))
    if output_dir.is_relative_to(package):
        raise ValueError("GenFM output must be outside the source package to preserve its artifact inventory")
    manifest, artifacts = compile_export(package, root)
    write_new_directory(output_dir, {**artifacts, "manifest.json": json_text(manifest)}, root)
    return manifest


def check(export_dir: Path, root: Path = ROOT) -> dict:
    """Reject stale inputs and modified exports, even after their hashes are replaced."""
    export_dir = safe_path(root, repository_relative(export_dir, root))
    manifest = read_json(safe_path(export_dir, "manifest.json"))
    package = safe_path(root, manifest.get("package_path", ""))
    expected, artifacts = compile_export(package, root)
    if manifest != expected:
        raise ValueError("GenFM export is stale or its manifest was modified; rebuild it")
    actual_files = set()
    for path in export_dir.rglob("*"):
        relative = path.relative_to(export_dir).as_posix()
        safe_path(export_dir, relative)
        if path.is_file():
            actual_files.add(relative)
    if actual_files != {"manifest.json", *artifacts}:
        raise ValueError("GenFM export file inventory differs from the expected artifacts")
    for name, expected_text in artifacts.items():
        actual = safe_path(export_dir, name).read_text(encoding="utf-8")
        if text_sha256(actual) != text_sha256(expected_text):
            raise ValueError(f"GenFM export artifact was modified: {name}")
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build_parser = commands.add_parser("build", help="Create a new offline GenFM source handoff")
    build_parser.add_argument("--package", type=Path, required=True)
    build_parser.add_argument("--output-dir", type=Path, required=True)
    check_parser = commands.add_parser("check", help="Reject stale or modified handoffs")
    check_parser.add_argument("--export", dest="export_dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            manifest = build(args.package, args.output_dir)
            print(f"Built {manifest['exam_code']} offline GenFM handoff in {args.output_dir}; no audio generated")
        else:
            manifest = check(args.export_dir)
            print(f"Verified {manifest['exam_code']} GenFM handoff against current inputs; factual/human review remains separate")
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"GenFM export error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
