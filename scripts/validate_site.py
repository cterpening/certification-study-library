#!/usr/bin/env python3
"""Validate internal links and anchors in the generated static site."""

from __future__ import annotations

from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_DIR = ROOT / "site"
DEFAULT_BASE_PATH = "/certification-study-library/"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            self.ids.add(element_id)
        name = attributes.get("name")
        if tag == "a" and name:
            self.ids.add(name)

        attribute = {
            "a": "href",
            "link": "href",
            "script": "src",
            "img": "src",
            "source": "src",
        }.get(tag)
        if attribute and attributes.get(attribute):
            self.references.append((tag, str(attributes[attribute])))


def parse_pages(site_dir: Path) -> dict[Path, PageParser]:
    pages: dict[Path, PageParser] = {}
    for path in site_dir.rglob("*.html"):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
    return pages


def resolve_reference(
    page: Path,
    raw_reference: str,
    site_dir: Path,
    base_path: str = DEFAULT_BASE_PATH,
) -> Path | None:
    parsed = urlparse(raw_reference)
    if parsed.scheme or parsed.netloc or raw_reference.startswith(("mailto:", "javascript:")):
        return None
    path_text = unquote(parsed.path)
    if not path_text:
        return page

    if path_text.startswith("/"):
        if base_path and path_text.startswith(base_path):
            path_text = path_text[len(base_path) :]
        candidate = site_dir / path_text.lstrip("/")
    else:
        candidate = page.parent / path_text
    candidate = candidate.resolve()

    resolved_site = site_dir.resolve()
    if candidate != resolved_site and resolved_site not in candidate.parents:
        return candidate
    if path_text.endswith("/") or candidate.is_dir():
        return candidate / "index.html"
    if not candidate.suffix:
        html_candidate = candidate.with_suffix(".html")
        if html_candidate.exists():
            return html_candidate
        return candidate / "index.html"
    return candidate


def validate_site(
    site_dir: Path = DEFAULT_SITE_DIR,
    base_path: str = DEFAULT_BASE_PATH,
) -> list[str]:
    site_dir = site_dir.resolve()
    if not site_dir.is_dir():
        return [f"Generated site directory does not exist: {site_dir}"]

    pages = parse_pages(site_dir)
    if not pages:
        return [f"No HTML pages found in generated site: {site_dir}"]

    errors: list[str] = []
    seen: set[tuple[Path, str]] = set()
    for page, parser in pages.items():
        for _tag, raw_reference in parser.references:
            key = (page, raw_reference)
            if key in seen:
                continue
            seen.add(key)
            parsed = urlparse(raw_reference)
            target = resolve_reference(page, raw_reference, site_dir, base_path)
            if target is None:
                continue
            if target != site_dir and site_dir not in target.parents:
                errors.append(
                    f"Link escapes generated site in {page.relative_to(site_dir)}: "
                    f"{raw_reference}"
                )
                continue
            if not target.exists():
                errors.append(
                    f"Broken generated link in {page.relative_to(site_dir)}: "
                    f"{raw_reference}"
                )
                continue
            if parsed.fragment and target.suffix.lower() == ".html":
                target_parser = pages.get(target.resolve())
                anchor = unquote(parsed.fragment)
                if target_parser is not None and anchor not in target_parser.ids:
                    errors.append(
                        f"Missing generated anchor in {page.relative_to(site_dir)}: "
                        f"{raw_reference}"
                    )

    return sorted(errors)


def main() -> int:
    errors = validate_site()
    if errors:
        print("Generated site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Generated site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
