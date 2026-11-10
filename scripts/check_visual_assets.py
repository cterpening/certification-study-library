#!/usr/bin/env python3
"""Check a vendored visual bundle offline, without modifying its artwork.

Hashes establish agreement with the included manifest, not publisher authenticity,
current product names, licensing approval, or certification objective coverage.
Selection/catalog hashes are provenance identifiers; their source files are not
part of an exported bundle and cannot be independently verified here.
"""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "website" / "assets" / "study-icons"
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"
STATIC_ELEMENTS = set(
    "svg g defs path rect circle ellipse line polyline polygon title desc "
    "linearGradient radialGradient stop clipPath mask use text tspan".split()
)
STATIC_TAGS = {f"{{{SVG_NAMESPACE}}}{name}" for name in STATIC_ELEMENTS}
STATIC_ATTRIBUTES = set(
    "id version viewBox preserveAspectRatio width height x y x1 x2 y1 y2 cx cy r rx ry "
    "d points transform fill fill-rule fill-opacity stroke stroke-width stroke-linecap "
    "stroke-linejoin stroke-miterlimit stroke-dasharray stroke-dashoffset stroke-opacity "
    "opacity clip-path clip-rule clipPathUnits mask maskUnits maskContentUnits "
    "gradientUnits gradientTransform spreadMethod offset stop-color stop-opacity fx fy fr "
    "font-family font-size font-weight text-anchor dominant-baseline dx dy rotate href".split()
) | {f"{{{XLINK_NAMESPACE}}}href"}
MAX_SVG_BYTES = 8 * 1024 * 1024
FRAGMENT = r"#[A-Za-z_][A-Za-z0-9_.:-]*"
LOCAL_URL = re.compile(
    r"url\(\s*(?:" + FRAGMENT + r"|'" + FRAGMENT + r"'|\"" + FRAGMENT + r"\")\s*\)",
    re.IGNORECASE,
)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _text(value: object, label: str) -> str:
    _require(
        isinstance(value, str) and bool(value.strip())
        and not any(ord(char) < 32 for char in value),
        f"{label}: expected a nonempty string without control characters",
    )
    return value


def _relative(value: object) -> str:
    value = _text(value, "path")
    _require(not any(char in value for char in '\\:<>"|?*'), f"Unsafe relative path: {value!r}")
    reserved = {"CON", "PRN", "AUX", "NUL"} | {
        f"{prefix}{number}" for prefix in ("COM", "LPT") for number in range(1, 10)
    }
    for part in value.split("/"):
        _require(
            part not in ("", ".", "..") and part == part.rstrip(" .")
            and part.split(".")[0].upper() not in reserved,
            f"Unsafe relative path: {value!r}",
        )
    return value


def _unlinked(path: Path) -> Path:
    """Reject links and Windows reparse points before resolving or opening."""
    path = Path(os.path.abspath(path))
    for component in reversed((path, *path.parents)):
        info = component.lstat()
        _require(
            not stat.S_ISLNK(info.st_mode)
            and not (getattr(info, "st_file_attributes", 0) & 0x400),
            f"Symlink/junction/reparse path is forbidden: {component}",
        )
        _require(
            stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode),
            f"Expected a regular file or directory: {component}",
        )
        _require(
            not stat.S_ISREG(info.st_mode) or info.st_nlink == 1,
            f"Hard-linked file is forbidden: {component}",
        )
    return path


def _inventory(bundle: Path) -> set[str]:
    files: set[str] = set()
    folded: set[str] = set()
    def fail(error: OSError) -> None:
        raise error

    for directory, directories, names in os.walk(bundle, followlinks=False, onerror=fail):
        for name in directories + names:
            path = _unlinked(Path(directory) / name)
            relative = _relative(path.relative_to(bundle).as_posix())
            _require(relative.casefold() not in folded, f"Case-colliding path: {relative}")
            folded.add(relative.casefold())
            if name in names:
                _require(path.is_file(), f"Expected regular file: {relative}")
                files.add(relative)
    return files


def _unique_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        _require(key not in result, f"Duplicate manifest key: {key}")
        result[key] = value
    return result


def _hash(value: object, label: str) -> None:
    _require(
        isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None,
        f"{label}: expected a lowercase SHA-256 digest",
    )


def _provenance(row: dict, label: str) -> None:
    for key in ("publisher", "source_page", "source_label"):
        _text(row.get(key), f"{label}.{key}")
    reviewed = _text(row.get("review_date"), f"{label}.review_date")
    try:
        valid_date = date.fromisoformat(reviewed).isoformat() == reviewed
    except ValueError:
        valid_date = False
    _require(valid_date, f"{label}.review_date: expected a valid YYYY-MM-DD date")


def _profiles(value: object, label: str) -> set[str]:
    _require(isinstance(value, list) and bool(value), f"{label}: expected nonempty profiles")
    for profile in value:
        _text(profile, label)
    _require(len(set(value)) == len(value), f"{label}: duplicate profiles")
    return set(value)


def _svg(raw: bytes, label: str) -> None:
    _require(len(raw) <= MAX_SVG_BYTES, f"{label}: SVG exceeds the 8 MiB limit")
    text = raw.decode("utf-8-sig")
    _require("\x00" not in text, f"{label}: SVG must be UTF-8 XML")
    _require(
        re.search(r"<!\s*(?:DOCTYPE|ENTITY)", text, re.IGNORECASE) is None,
        f"{label}: DTD/entities are forbidden",
    )
    declaration = re.match(r"\A\s*<\?xml\s[^?]*\?>", text)
    if declaration:
        encoding = re.search(r"encoding\s*=\s*(['\"])([^'\"]+)\1", declaration.group(), re.IGNORECASE)
        _require(
            encoding is None or encoding.group(2).lower() == "utf-8",
            f"{label}: only UTF-8 XML encoding is supported",
        )
    without_declaration = re.sub(r"\A\s*<\?xml\s[^?]*\?>", "", text, count=1)
    _require("<?" not in without_declaration, f"{label}: processing instructions are forbidden")
    root = ET.fromstring(text)
    _require(root.tag == f"{{{SVG_NAMESPACE}}}svg", f"{label}: expected a namespaced SVG root")
    try:
        box = [float(value) for value in re.split(r"[\s,]+", root.get("viewBox", "").strip())]
    except ValueError:
        box = []
    _require(
        len(box) == 4 and all(math.isfinite(value) for value in box)
        and box[2] > 0 and box[3] > 0,
        f"{label}: viewBox must have four finite numbers and positive dimensions",
    )
    for element in root.iter():
        _require(
            element.tag in STATIC_TAGS,
            f"{label}: unsupported or active SVG element {element.tag}",
        )
        for name, value in element.attrib.items():
            local_name = name.rsplit("}", 1)[-1].lower()
            _require(
                name in STATIC_ATTRIBUTES,
                f"{label}: unsupported or active SVG attribute {name}",
            )
            _require(
                "\\" not in value and "/*" not in value,
                f"{label}: CSS escapes/comments are forbidden in SVG attributes",
            )
            if local_name == "href":
                _require(
                    re.fullmatch(FRAGMENT, value) is not None,
                    f"{label}: external SVG href is forbidden",
                )
            if re.search(r"url\s*\(", value, re.IGNORECASE):
                _require(LOCAL_URL.fullmatch(value) is not None, f"{label}: external/complex CSS URL is forbidden")


def check_bundle(path: Path | str) -> list[str]:
    """Return validation errors (empty when valid); never fetch or rewrite files."""
    try:
        bundle = _unlinked(Path(path))
        _require(bundle.is_dir(), f"Expected a bundle directory: {bundle}")
        actual_files = _inventory(bundle)
        manifest_path = _unlinked(bundle / "manifest.json")
        manifest = json.loads(manifest_path.read_bytes(), object_pairs_hook=_unique_keys)
        _require(isinstance(manifest, dict), "Manifest must be an object")
        _require(type(manifest.get("schema_version")) is int and manifest["schema_version"] == 1,
                 "Unsupported schema_version (expected integer 1)")
        _text(manifest.get("collection_id"), "collection_id")
        _provenance(manifest, "manifest")
        for key in ("selection_sha256", "catalog_sha256"):
            _hash(manifest.get(key), key)
        requested = _profiles(manifest.get("profiles"), "manifest.profiles")
        assets, notices = manifest.get("assets"), manifest.get("notices")
        _require(isinstance(assets, list) and bool(assets), "Manifest must contain nonempty assets")
        _require(isinstance(notices, list) and bool(notices), "Manifest must contain nonempty notices")
        expected_files = {"manifest.json"}
        folded_paths = {"manifest.json"}
        ids: set[str] = set()
        sources: set[str] = set()
        matched_profiles: set[str] = set()
        for row in assets + notices:
            _require(isinstance(row, dict), "Asset/notice must be an object")
            relative = _relative(row.get("path"))
            _require(relative.casefold() not in folded_paths, f"Duplicate bundle path: {relative}")
            folded_paths.add(relative.casefold())
            expected_files.add(relative)
            _hash(row.get("sha256"), f"{relative}.sha256")
        for row in assets:
            identifier = _text(row.get("id"), "asset.id")
            _require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier) is not None,
                     f"Invalid asset id: {identifier!r}")
            _require(identifier not in ids, f"Duplicate asset id: {identifier}")
            ids.add(identifier)
            _require(row["path"] == f"assets/{identifier}.svg", f"Unexpected asset path: {row['path']}")
            _text(row.get("label"), f"{identifier}.label")
            source_path = _relative(row.get("source_path"))
            _require(source_path.casefold() not in sources, f"Duplicate asset source path: {source_path}")
            sources.add(source_path.casefold())
            _provenance(row, identifier)
            for key in ("publisher", "source_page", "source_label", "review_date"):
                _require(row[key] == manifest[key], f"{identifier}: asset provenance mismatch: {key}")
            if "notes" in row:
                _text(row["notes"], f"{identifier}.notes")
            profiles = _profiles(row.get("profiles"), f"{identifier}.profiles")
            _require(bool(profiles & requested), f"{identifier}: asset matches no requested profile")
            matched_profiles.update(profiles & requested)
        _require(matched_profiles == requested, f"Requested profiles have no assets: {sorted(requested - matched_profiles)}")
        for row in notices:
            parts = row["path"].split("/")
            _require(len(parts) == 2 and parts[0] == "notices", f"Unexpected notice path: {row['path']}")
        _require(actual_files == expected_files,
                 f"Bundle inventory mismatch; missing: {sorted(expected_files - actual_files)}; "
                 f"unlisted: {sorted(actual_files - expected_files)}")
        for row in assets + notices:
            raw = _unlinked(bundle / row["path"]).read_bytes()
            _require(hashlib.sha256(raw).hexdigest() == row["sha256"], f"SHA-256 mismatch: {row['path']}")
            if Path(row["path"]).suffix.lower() == ".svg":
                _svg(raw, row["path"])
    except (OSError, ValueError, ET.ParseError) as exc:
        return [str(exc)]
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE, help="Exported bundle directory")
    args = parser.parse_args(argv)
    errors = check_bundle(args.bundle)
    if errors:
        for error in errors:
            print(f"Visual bundle check failed: {error}", file=sys.stderr)
        return 1
    print(f"Visual bundle verified offline: {args.bundle}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
