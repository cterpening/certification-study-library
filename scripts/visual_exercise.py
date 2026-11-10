"""Shared SVG drawing and source binding for authored visual exercises."""
from __future__ import annotations

import base64
from hashlib import sha256
from pathlib import Path
import textwrap
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

from check_visual_assets import check_bundle
from study_material import ROOT, json_text, load_package, read_json, repository_relative, safe_path, text_sha256

SVG = "http://www.w3.org/2000/svg"


def text(x, y, value, size=18, color="#183348", weight=400, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>'


def paragraph(x, y, value, width=40, size=18, color="#334e63", line_height=27, weight=400):
    rows = []
    for source_line in str(value).splitlines():
        rows.extend(textwrap.wrap(source_line, width=width) or [""])
    return "\n".join(text(x, y + i * line_height, row, size, color, weight) for i, row in enumerate(rows))


def rect(x, y, width, height, fill="#ffffff", stroke="none", radius=12, stroke_width=1, dash=None):
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{dashed}/>'


def path(d, color="#668093", width=2, dash=None, arrow=False, fill="none"):
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="{fill}"{dashed}{marker}/>'


def document(title, description, body, width=1200, height=1400):
    if not isinstance(body, str):
        body = "\n".join(body)
    return "\n".join([
        f'<svg xmlns="{SVG}" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="description">{escape(description)}</desc>',
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#668093"/></marker></defs>',
        rect(0, 0, width, height, fill="#f3f6f7", radius=0),
        '<g font-family="Arial, sans-serif">', body, '</g></svg>', '',
    ])


class Exercise:
    """Bind a fixed authored layout to reviewed unit versions and original icons."""

    def __init__(self, here: Path, package: str, units: dict[str, str], icons=()):
        self.here = safe_path(ROOT, repository_relative(here, ROOT))
        self.package = safe_path(ROOT, package)
        self.package_path = package
        self.pack = load_package(self.package, ROOT)
        available = {u["id"]: u for u in read_json(self.package / "units.json")["units"]}
        if not units:
            raise ValueError("An exercise must identify its source units")
        self.units = {}
        for unit_id, expected_hash in units.items():
            if unit_id not in available or text_sha256(json_text(available[unit_id])) != expected_hash:
                raise ValueError(f"Source unit changed: {unit_id}; review the visual and source evidence before rebinding")
            self.units[unit_id] = expected_hash
        self.bundle = safe_path(ROOT, "website/assets/study-icons")
        errors = check_bundle(self.bundle)
        if errors:
            raise ValueError("Invalid visual asset bundle: " + "; ".join(errors))
        self.bundle_manifest = read_json(self.bundle / "manifest.json")
        rows = {row["id"]: row for row in self.bundle_manifest["assets"]}
        self.icons = {}
        for asset_id in icons:
            if asset_id in self.icons or asset_id not in rows:
                raise ValueError(f"Unknown or duplicate icon: {asset_id}")
            row = rows[asset_id]
            if self.pack["exam_code"] not in row["profiles"]:
                raise ValueError(f"Icon is not selected for {self.pack['exam_code']}: {asset_id}")
            self.icons[asset_id] = (row, safe_path(self.bundle, row["path"]).read_bytes())

    def icon(self, asset_id, x, y, size=72):
        if asset_id not in self.icons:
            raise ValueError(f"Undeclared icon: {asset_id}")
        encoded = base64.b64encode(self.icons[asset_id][1]).decode("ascii")
        return f'<image x="{x}" y="{y}" width="{size}" height="{size}" preserveAspectRatio="xMidYMid meet" aria-hidden="true" href="data:image/svg+xml;base64,{encoded}"/>'

    def save(self, study: str, practice: str, *, check=False):
        artifacts = {"study.svg": study, "practice.svg": practice}
        expected_icons = {row["sha256"] for row, _ in self.icons.values()}
        for name, value in artifacts.items():
            root = ET.fromstring(value)
            if root.tag != f"{{{SVG}}}svg" or root.find(f"{{{SVG}}}desc") is None:
                raise ValueError(f"SVG and text alternative required: {name}")
            actual_icons = set()
            for element in root.iter(f"{{{SVG}}}image"):
                prefix = "data:image/svg+xml;base64,"
                href = element.get("href", "")
                if not href.startswith(prefix):
                    raise ValueError("Exercise images must embed the selected original SVG bytes")
                raw = base64.b64decode(href[len(prefix):], validate=True)
                actual_icons.add(sha256(raw).hexdigest())
            if actual_icons != expected_icons:
                raise ValueError(f"Embedded icons differ from the declared selected originals: {name}")
        manifest = {
            "schema_version": 1,
            "exam_code": self.pack["exam_code"],
            "content_status": "ai-generated-draft; human review pending",
            "source_package": self.package_path,
            "source_package_manifest_sha256": text_sha256((self.package / "manifest.json").read_text(encoding="utf-8")),
            "source_units": self.units,
            "builder_sha256": text_sha256(safe_path(self.here, "build.py").read_text(encoding="utf-8")),
            "helper_sha256": text_sha256(Path(__file__).read_text(encoding="utf-8")),
            "icon_bundle_manifest_sha256": sha256((self.bundle / "manifest.json").read_bytes()).hexdigest(),
            "icons": {key: row["sha256"] for key, (row, _) in self.icons.items()},
            "text_hash_normalization": "UTF-8 text; CRLF/CR normalized to LF; embedded icon hashes are raw bytes",
            "artifacts": {name: text_sha256(value) for name, value in artifacts.items()},
        }
        artifacts["manifest.json"] = json_text(manifest)
        targets = {name: safe_path(self.here, name) for name in artifacts}
        if check:
            for name, expected in artifacts.items():
                if text_sha256(targets[name].read_text(encoding="utf-8")) != text_sha256(expected):
                    raise ValueError(f"Stale or modified exercise artifact: {name}")
            print(f"Checked {self.pack['exam_code']} exercise and original icon bindings")
        else:
            for name, value in artifacts.items():
                targets[name].write_text(value, encoding="utf-8", newline="\n")
            print(f"Built {self.pack['exam_code']} study/practice pair; content review remains separate")
        return manifest
