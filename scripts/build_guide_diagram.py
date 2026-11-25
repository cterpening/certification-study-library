#!/usr/bin/env python3
"""Build or check one guide's inline relationship diagram and print its Markdown."""

import argparse
from pathlib import Path
import os
import re
import sys
from tempfile import TemporaryDirectory

from study_material import (
    ROOT, SLUG, _keys, _markdown, _strings, _text, exam_context, objective_present,
    read_json, render_svg, repository_relative, safe_path, validate_visual, visual_description,
)


def guide_lines(markdown: str):
    """Yield guide body lines outside front matter, fenced examples and comment blocks."""
    lines = markdown.splitlines()
    if lines and lines[0] == "---" and "---" in lines[1:]:
        lines = lines[lines.index("---", 1) + 1:]
    fence = None
    comment = False
    for line in lines:
        if fence:
            if re.fullmatch(r" {0,3}" + fence + fence[0] + r"*[ \t]*", line):
                fence = None
            continue
        if comment or line.lstrip().startswith("<!--"):
            comment = "-->" not in line
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if opening:
            fence = opening.group(1)
            continue
        yield line


def guide_headings(markdown: str):
    """Yield ATX heading text from the learner-visible guide."""
    for line in guide_lines(markdown):
        heading = re.match(r"^ {0,3}#{1,6}[ \t]+(.+?)\s*$", line)
        if heading:
            yield re.sub(r"[ \t]+#+$", "", heading.group(1))


def build_diagram(spec_path: Path, *, check: bool = False, root: Path = ROOT,
                  context: dict | None = None) -> str:
    """Validate the spec, build or compare its sibling SVG, and return the guide embed."""
    relative = repository_relative(root / spec_path, root)
    spec_path = safe_path(root, relative)
    spec = read_json(spec_path)
    _keys(spec, {"exam_code", "guide_section", "objective", "source_ids", "visual"}, "diagram")
    code = _text(spec["exam_code"], "exam_code")
    if not SLUG.fullmatch(spec_path.stem) or relative != f"guides/diagrams/{code.lower()}/{spec_path.stem}.json":
        raise ValueError("Expected guides/diagrams/<lowercase-exam-code>/<lowercase-slug>.json")
    if context is None:
        context = exam_context(code, root)
    if code != context["exam"]["code"]:
        raise ValueError("The diagram exam_code must match the catalog exactly")
    heading = _text(spec["guide_section"], "guide_section")
    if heading not in guide_headings(context["guide"]):
        raise ValueError(f"Unknown guide section: {heading}")
    objective = _text(spec["objective"], "objective")
    if not objective_present(objective, context["objectives"]):
        raise ValueError(f"Unknown objective: {objective}")
    citations = []
    for source_id in _strings(spec["source_ids"], "source_ids"):
        if source_id not in context["sources"]:
            raise ValueError(f"Unregistered source for this exam: {source_id}")
        source = context["sources"][source_id]
        citations.append(f"[{_markdown(source['title'])}]({source['url']})")
    visual = spec["visual"]
    validate_visual(visual)
    endpoints = {edge[end] for edge in visual["edges"] for end in ("from", "to")}
    unused = [node["id"] for node in visual["nodes"] if node["id"] not in endpoints]
    if unused:
        raise ValueError("Nodes without a relationship: " + ", ".join(unused))
    svg = render_svg(visual, group_origins=True)
    output = safe_path(root, relative[:-5] + ".svg")
    guide = safe_path(root, context["guide_path"])
    image_link = Path(os.path.relpath(output, guide.parent)).as_posix()
    alt = _markdown(" ".join(visual["title"].split()))
    description = _markdown(" ".join(visual_description(visual).split()))
    embed = (
        f"![{alt}]({image_link})\n\n"
        f"{description}. " + " · ".join(citations) + f"\n\n[Open full-size diagram]({image_link})"
    )

    if check:
        if not output.is_file() or output.read_text(encoding="utf-8") != svg:
            raise ValueError(f"Missing or stale guide diagram: {output.name}. Rebuild it and inspect the changes.")
    else:
        with TemporaryDirectory(dir=output.parent) as temporary:
            staged = Path(temporary) / output.name
            staged.write_text(svg, encoding="utf-8", newline="\n")
            staged.replace(output)
    return embed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="guides/diagrams/<exam>/<slug>.json")
    parser.add_argument("--check", action="store_true", help="Verify the current SVG without writing files")
    args = parser.parse_args(argv)
    try:
        print(build_diagram(args.spec, check=args.check))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Guide diagram error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
