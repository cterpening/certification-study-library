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
        self.duplicate_ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.h1_count = 0
        self.has_skip_link = False
        self.skip_targets: list[str] = []
        self.html_lang = ""
        self.main_count = 0
        self.title_parts: list[str] = []
        self._in_title = False
        self.images_missing_alt = 0
        self.labels_for: set[str] = set()
        self.controls: list[tuple[str, dict[str, str | None], bool]] = []
        self._label_depth = 0
        self.buttons: list[tuple[dict[str, str | None], str]] = []
        self._button_stack: list[tuple[dict[str, str | None], list[str]]] = []
        self.tables_without_headers = 0
        self._table_headers: list[bool] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.html_lang = str(attributes.get("lang") or "").strip()
        if tag == "title":
            self._in_title = True
        if tag == "main":
            self.main_count += 1
        if tag == "h1":
            self.h1_count += 1
        if tag == "a" and "md-skip" in str(attributes.get("class", "")).split():
            self.has_skip_link = True
            href = str(attributes.get("href") or "")
            if href.startswith("#") and len(href) > 1:
                self.skip_targets.append(unquote(href[1:]))
        if tag == "img" and "alt" not in attributes:
            self.images_missing_alt += 1
        if tag == "label":
            self._label_depth += 1
            label_for = attributes.get("for")
            if label_for:
                self.labels_for.add(str(label_for))
        if tag in {"input", "select", "textarea"}:
            self.controls.append((tag, attributes, self._label_depth > 0))
        if tag == "button":
            self._button_stack.append((attributes, []))
        if tag == "table":
            self._table_headers.append(False)
        if tag == "th" and self._table_headers:
            self._table_headers[-1] = True
        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
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

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "label" and self._label_depth:
            self._label_depth -= 1
        if tag == "button" and self._button_stack:
            attributes, text = self._button_stack.pop()
            self.buttons.append((attributes, " ".join(text).strip()))
        if tag == "table" and self._table_headers:
            if not self._table_headers.pop():
                self.tables_without_headers += 1

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._button_stack and data.strip():
            self._button_stack[-1][1].append(data.strip())

    @property
    def title(self) -> str:
        return " ".join(self.title_parts).strip()

    def unlabeled_control_count(self) -> int:
        count = 0
        for _tag, attributes, wrapped_by_label in self.controls:
            if str(attributes.get("type") or "").lower() == "hidden":
                continue
            if "disabled" in attributes:
                continue
            # Material for MkDocs emits an unused, CSS-hidden TOC state input on
            # pages without a table of contents. It has no interactive label.
            classes = str(attributes.get("class") or "").split()
            if attributes.get("id") == "__toc" and "md-toggle" in classes:
                continue
            has_name = any(
                str(attributes.get(name) or "").strip()
                for name in ("aria-label", "aria-labelledby", "title")
            )
            element_id = str(attributes.get("id") or "")
            if not has_name and not wrapped_by_label and element_id not in self.labels_for:
                count += 1
        return count

    def unnamed_button_count(self) -> int:
        return sum(
            not text
            and not any(
                str(attributes.get(name) or "").strip()
                for name in ("aria-label", "aria-labelledby", "title")
            )
            for attributes, text in self.buttons
        )


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
        relative_page = page.relative_to(site_dir)
        if not parser.html_lang:
            errors.append(f"Generated page is missing an HTML language: {relative_page}")
        if not parser.title:
            errors.append(f"Generated page is missing a document title: {relative_page}")
        if parser.main_count != 1:
            errors.append(
                f"Generated page must contain exactly one main landmark in {relative_page}: "
                f"found {parser.main_count}"
            )
        if parser.h1_count != 1:
            errors.append(
                f"Generated page must contain exactly one H1 in {relative_page}: "
                f"found {parser.h1_count}"
            )
        if relative_page != Path("404.html") and not parser.has_skip_link:
            errors.append(f"Generated page is missing a skip link: {relative_page}")
        for target in parser.skip_targets:
            if target not in parser.ids:
                errors.append(
                    f"Generated page skip link has no target in {relative_page}: #{target}"
                )
        if parser.duplicate_ids:
            errors.append(
                f"Generated page has duplicate IDs in {relative_page}: "
                + ", ".join(sorted(parser.duplicate_ids))
            )
        if parser.images_missing_alt:
            errors.append(
                f"Generated page has images without alt attributes in {relative_page}: "
                f"found {parser.images_missing_alt}"
            )
        unlabeled_controls = parser.unlabeled_control_count()
        if unlabeled_controls:
            errors.append(
                f"Generated page has unlabeled form controls in {relative_page}: "
                f"found {unlabeled_controls}"
            )
        unnamed_buttons = parser.unnamed_button_count()
        if unnamed_buttons:
            errors.append(
                f"Generated page has buttons without accessible names in {relative_page}: "
                f"found {unnamed_buttons}"
            )
        if parser.tables_without_headers:
            errors.append(
                f"Generated page has tables without header cells in {relative_page}: "
                f"found {parser.tables_without_headers}"
            )
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
