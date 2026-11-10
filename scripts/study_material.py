"""Versioned, offline study packs. Structural checks never constitute content review."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import textwrap
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
MAX_JSON_BYTES = 32_000_000
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
EXAM_CODE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}\Z")
BASE_INPUTS = ("config/exams.json", "data/sources.json", "data/source-health.json")
NOTICE = (
    "Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING. "
    "Structural checks do not establish factual accuracy or renew source review. "
    "The official exam blueprint is authoritative."
)


def text_sha256(text: str) -> str:
    """Hash UTF-8 text with platform-only newline differences normalized."""
    return sha256(text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")).hexdigest()


def read_json(path: Path) -> dict:
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError(f"JSON exceeds {MAX_JSON_BYTES} bytes: {path.name}")
    def unique_pairs(pairs: list[tuple[str, object]]) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path.name}")
    return value


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def safe_path(root: Path, relative: str) -> Path:
    """Accept portable relative paths only; never follow symlinks or junctions."""
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        raise ValueError("Expected a portable relative path")
    parts = PurePosixPath(relative)
    if parts.is_absolute() or any(part in ("", ".", "..") for part in relative.split("/")):
        raise ValueError(f"Unsafe relative path: {relative}")
    root = root.resolve()
    current = root
    for part in parts.parts:
        current = current / part
        if current.is_symlink() or (hasattr(current, "is_junction") and current.is_junction()):
            raise ValueError(f"Linked paths are not permitted: {relative}")
    if not current.resolve().is_relative_to(root):
        raise ValueError(f"Path escapes its root: {relative}")
    return current


def repository_relative(path: Path, root: Path) -> str:
    root = root.resolve()
    path = path.absolute()
    try:
        relative = path.relative_to(root).as_posix()
    except ValueError as exc:
        raise ValueError("Content and output paths must be inside the repository") from exc
    safe_path(root, relative)
    return relative


def fingerprints(root: Path, paths: list[str] | tuple[str, ...]) -> dict[str, str]:
    return {name: text_sha256(safe_path(root, name).read_text(encoding="utf-8")) for name in sorted(set(paths))}


def exam_context(code: str, root: Path = ROOT) -> dict:
    if not isinstance(code, str) or not EXAM_CODE.fullmatch(code):
        raise ValueError("Invalid exam code")
    exams = read_json(safe_path(root, "config/exams.json"))["exams"]
    matches = [exam for exam in exams if exam["code"].casefold() == code.casefold()]
    if len(matches) != 1:
        raise ValueError(f"Expected one published guide for {code}; use prepare for new-guide intake")
    exam = matches[0]
    guide_path = exam["guide_path"]
    objective_path = f"data/objective-snapshots/{exam['code'].lower()}-official-objectives.txt"
    guide = safe_path(root, guide_path).read_text(encoding="utf-8")
    objectives = safe_path(root, objective_path).read_text(encoding="utf-8")
    source_rows = read_json(safe_path(root, "data/sources.json"))["sources"]
    sources = {row["id"]: row for row in source_rows if exam["code"] in row.get("supported_exams", [])}
    health_rows = read_json(safe_path(root, "data/source-health.json"))["sources"]
    health = {row["id"]: row for row in health_rows if row["id"] in sources}
    inputs = [*BASE_INPUTS, guide_path, objective_path]
    status_path = f"data/objective-snapshots/{exam['code'].lower()}-official-status.json"
    status = None
    if safe_path(root, status_path).exists():
        status = read_json(safe_path(root, status_path))
        inputs.append(status_path)
    return {
        "exam": exam, "guide": guide, "objectives": objectives,
        "guide_path": guide_path, "objective_path": objective_path,
        "sources": sources, "health": health, "status": status,
        "input_paths": inputs,
        "baseline": next((line.strip() for line in objectives.splitlines() if line.strip()), "Unspecified"),
    }


def _text(value: object, name: str, maximum: int = 10000) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f"{name} needs nonempty text of at most {maximum} characters")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", value):
        raise ValueError(f"Control character in {name}")
    if re.search(r"(?:https?://|javascript:)", value, re.I):
        raise ValueError(f"Use source_ids, not embedded URLs, in {name}")
    return value


def _strings(value: object, name: str, maximum: int = 40) -> list[str]:
    if not isinstance(value, list) or not 1 <= len(value) <= maximum:
        raise ValueError(f"{name} needs 1–{maximum} entries")
    result = [_text(item, name) for item in value]
    if len(set(result)) != len(result):
        raise ValueError(f"Duplicate entry in {name}")
    return result


def _keys(value: object, expected: set[str], name: str) -> dict:
    if not isinstance(value, dict) or set(value) != expected:
        raise ValueError(f"{name} must have exactly these fields: {', '.join(sorted(expected))}")
    return value


def objective_present(objective: str, snapshot: str) -> bool:
    """Match whole contiguous snapshot lines, allowing vendor line wrapping."""
    target = " ".join(objective.split())
    # These known blueprint administration labels are not teaching objectives.
    # Matching text remains a structural check, not semantic coverage validation.
    if re.match(r"^(?:Skills measured as of\b|Skills at a glance\b|Audience profile\b)", target, re.I):
        return False
    lines = [" ".join(line.split()) for line in snapshot.splitlines() if line.strip()]
    for start in range(len(lines)):
        candidate = ""
        for line in lines[start:start + 16]:
            candidate = f"{candidate} {line}".strip()
            if candidate == target:
                return True
            if len(candidate) >= len(target):
                break
    return False


def validate_content(content: dict, context: dict) -> None:
    _keys(content, {"schema_version", "exam_code", "language", "scope_note", "units"}, "content")
    if type(content["schema_version"]) is not int or content["schema_version"] != 1:
        raise ValueError("Unsupported content schema_version")
    if content["exam_code"] != context["exam"]["code"]:
        raise ValueError("Content exam_code must match the catalog exactly")
    if content["language"] != "en":
        raise ValueError("This initial pipeline supports language 'en' only")
    _text(content["scope_note"], "scope_note")
    units = content["units"]
    if not isinstance(units, list) or not 1 <= len(units) <= 12:
        raise ValueError("A study pack needs 1–12 units")
    headings = set(re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", context["guide"], re.M))
    ids = set()
    for unit in units:
        _keys(unit, {"id", "title", "guide_sections", "objectives", "source_ids", "summary", "key_points", "scenario", "visual", "dialogue"}, "unit")
        unit_id = _text(unit["id"], "unit.id", 64)
        if not SLUG.fullmatch(unit_id) or unit_id in ids or unit_id in {"introduction", "recap"}:
            raise ValueError("Unit IDs must be unique lowercase slugs; introduction and recap are reserved")
        ids.add(unit_id)
        _text(unit["title"], "title", 180)
        _text(unit["summary"], "summary")
        _strings(unit["key_points"], "key_points", 20)
        for heading in _strings(unit["guide_sections"], "guide_sections"):
            if heading not in headings:
                raise ValueError(f"Unknown guide section: {heading}")
        for objective in _strings(unit["objectives"], "objectives"):
            if not objective_present(objective, context["objectives"]):
                raise ValueError(f"Unknown objective: {objective}")
        for source_id in _strings(unit["source_ids"], "source_ids"):
            if source_id not in context["sources"]:
                raise ValueError(f"Unregistered source for this exam: {source_id}")
        scenario = _keys(unit["scenario"], {"question", "answer"}, "scenario")
        _text(scenario["question"], "scenario.question")
        _text(scenario["answer"], "scenario.answer")
        visual = _keys(unit["visual"], {"title", "nodes", "edges"}, "visual")
        _text(visual["title"], "visual.title", 180)
        if not isinstance(visual["nodes"], list) or not 2 <= len(visual["nodes"]) <= 12:
            raise ValueError("A visual needs 2–12 nodes")
        node_ids = set()
        for node in visual["nodes"]:
            _keys(node, {"id", "label"}, "visual node")
            node_id = _text(node["id"], "node.id", 64)
            if not SLUG.fullmatch(node_id) or node_id in node_ids:
                raise ValueError("Visual node IDs must be unique lowercase slugs")
            node_ids.add(node_id)
            _text(node["label"], "node.label", 160)
        if not isinstance(visual["edges"], list) or not 1 <= len(visual["edges"]) <= 24:
            raise ValueError("A visual needs 1–24 edges")
        for edge in visual["edges"]:
            _keys(edge, {"from", "to", "label"}, "visual edge")
            if edge["from"] not in node_ids or edge["to"] not in node_ids or edge["from"] == edge["to"]:
                raise ValueError("Visual edges must connect two different declared nodes")
            _text(edge["label"], "edge.label", 100)
        dialogue = unit["dialogue"]
        if not isinstance(dialogue, list) or not 2 <= len(dialogue) <= 120:
            raise ValueError("Each unit needs 2–120 dialogue turns")
        speakers = set()
        for turn in dialogue:
            _keys(turn, {"speaker", "text"}, "dialogue turn")
            if turn["speaker"] not in ("host", "learner"):
                raise ValueError("Dialogue speakers must be host or learner")
            speakers.add(turn["speaker"])
            _text(turn["text"], "dialogue.text")
        if speakers != {"host", "learner"}:
            raise ValueError("Each unit needs both host and learner dialogue")


def _markdown(text: str) -> str:
    # All authored fields are prose. Sources and links are rendered from the catalog.
    return re.sub(r"([\\`*_{}\[\]<>|])", r"\\\1", text)


def visual_description(visual: dict) -> str:
    labels = {node["id"]: node["label"] for node in visual["nodes"]}
    return "; ".join(f"{labels[edge['from']]} — {edge['label']} → {labels[edge['to']]}" for edge in visual["edges"])


def render_svg(visual: dict) -> str:
    """Render a readable relationship list, retaining every edge without crossings."""
    rows = []
    height = 86
    labels = {node["id"]: node["label"] for node in visual["nodes"]}
    for edge in visual["edges"]:
        left = textwrap.wrap(labels[edge["from"]], 30) or [""]
        right = textwrap.wrap(labels[edge["to"]], 30) or [""]
        middle = textwrap.wrap(edge["label"], 18) or [""]
        row_height = max(len(left), len(right), len(middle) + 1) * 22 + 32
        rows.append((height, row_height, left, right, middle))
        height += row_height + 18
    title_lines = textwrap.wrap(visual["title"], 65)
    title_height = max(0, len(title_lines) - 1) * 25
    height += title_height
    output = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-labelledby="title description">',
        f'<title id="title">{escape(visual["title"])}</title>',
        f'<desc id="description">{escape(visual_description(visual))}</desc>',
        '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9" fill="#334155"/></marker></defs>',
        f'<rect width="1000" height="{height}" rx="12" fill="#f8fafc"/>',
        '<g font-family="Arial, sans-serif" fill="#0f172a">',
    ]
    for index, line in enumerate(title_lines):
        output.append(f'<text x="28" y="{36 + index * 25}" font-size="23" font-weight="bold">{escape(line)}</text>')
    for top, row_height, left, right, middle in rows:
        top += title_height
        for x, lines, fill in ((28, left, "#dbeafe"), (652, right, "#dcfce7")):
            output.append(f'<rect x="{x}" y="{top}" width="320" height="{row_height}" rx="10" fill="{fill}" stroke="#64748b"/>')
            for index, line in enumerate(lines):
                output.append(f'<text x="{x + 16}" y="{top + 30 + index * 22}" font-size="17">{escape(line)}</text>')
        arrow_y = top + row_height - 19
        output.append(f'<path d="M360,{arrow_y} H637" stroke="#334155" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
        for index, line in enumerate(middle):
            output.append(f'<text x="500" y="{top + 27 + index * 22}" text-anchor="middle" font-size="16">{escape(line)}</text>')
    return "\n".join([*output, "</g>", "</svg>", ""])


def render_artifacts(content: dict, context: dict) -> dict[str, str]:
    exam = context["exam"]
    sources = context["sources"]
    lines = [
        f"# {exam['code']} — {_markdown(exam['title'])}: visual study pack", "",
        f"> **{NOTICE}**", "",
        f"[Official exam blueprint]({exam['study_guide_url']})", "",
        f"[Full library guide](https://github.com/cterpening/certification-study-library/blob/main/{context['guide_path']}) "
        "(current repository version; this package's exact source hash is recorded in manifest.json).", "",
        f"**Accepted objective baseline:** {_markdown(context['baseline'])}", "",
        f"**Blueprint last checked in the catalog:** {exam.get('blueprint_last_checked', 'Unrecorded')}. This build performs no live source refresh.", "",
        f"**Scope:** {_markdown(content['scope_note'])}", "",
        "**VERIFY CURRENT:** Recheck volatile product details and unresolved limitations in the source guide. A matching file hash does not establish current technical accuracy.", "",
    ]
    cards = []
    artifacts = {}
    for unit in content["units"]:
        sources_md = ", ".join(f"[{_markdown(sources[sid]['title'])}]({sources[sid]['url']})" for sid in unit["source_ids"])
        diagram = f"visuals/{unit['id']}.svg"
        artifacts[diagram] = render_svg(unit["visual"])
        lines += [f"## {_markdown(unit['title'])}", "", _markdown(unit["summary"]), "", f"**Supporting sources:** {sources_md}", "", "**Published objectives:**", ""]
        lines += [f"- {_markdown(objective)}" for objective in unit["objectives"]]
        lines += ["", "**Source-guide sections:** " + "; ".join(_markdown(heading) for heading in unit["guide_sections"]), "", f"![{_markdown(unit['visual']['title'])}]({diagram})", "", "**Diagram in words:** " + _markdown(visual_description(unit["visual"])), "", "**Remember:**", ""]
        lines += [f"- {_markdown(point)}" for point in unit["key_points"]]
        lines += ["", "**Try it:** " + _markdown(unit["scenario"]["question"]), "", "**Answer and reasoning:** " + _markdown(unit["scenario"]["answer"]), ""]
        cards.append({"id": unit["id"], "question": unit["scenario"]["question"], "answer": unit["scenario"]["answer"], "objectives": unit["objectives"], "source_ids": unit["source_ids"]})
    lines += ["## Places to learn", "", "The linked source guide and registered references are a curated starting point, not a complete list or a requirement to consume everything. This focused pack does not replace the complete guide or official objectives.", ""]
    artifacts["study-guide.md"] = "\n".join(lines)
    artifacts["flashcards.json"] = json_text({"schema_version": 1, "exam_code": content["exam_code"], "content_status": "ai-generated-draft", "cards": cards})
    artifacts["units.json"] = json_text(content)
    return artifacts


def compile_content(content_path: Path, root: Path = ROOT) -> tuple[dict, dict[str, str]]:
    content_relative = repository_relative(content_path, root)
    content = read_json(safe_path(root, content_relative))
    context = exam_context(content.get("exam_code"), root)
    validate_content(content, context)
    artifacts = render_artifacts(content, context)
    manifest = {
        "schema_version": 1,
        "exam_code": content["exam_code"], "title": context["exam"]["title"],
        "blueprint_url": context["exam"]["study_guide_url"],
        "baseline": context["baseline"],
        "blueprint_last_checked": context["exam"].get("blueprint_last_checked"),
        "language": content["language"], "scope_note": content["scope_note"],
        "content_status": "ai-generated-draft", "hash_normalization": "UTF-8 text; CRLF/CR normalized to LF",
        "guide_path": context["guide_path"], "objective_path": context["objective_path"],
        "content_path": content_relative,
        "input_fingerprints": fingerprints(root, [*context["input_paths"], content_relative]),
        "artifacts": {path: text_sha256(text) for path, text in sorted(artifacts.items())},
    }
    return manifest, artifacts


def write_new_directory(output_dir: Path, files: dict[str, str], root: Path = ROOT) -> None:
    relative = repository_relative(output_dir, root)
    output_dir = safe_path(root, relative)
    if output_dir.exists():
        raise ValueError("Output directory already exists; choose a new run directory")
    for name in files:
        safe_path(output_dir, name)
    output_dir.mkdir(parents=True, exist_ok=False)
    for name, text in files.items():
        destination = safe_path(output_dir, name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8", newline="\n")


def load_package(package_dir: Path, root: Path = ROOT) -> dict:
    """Check current source binding and every expected generated artifact.

    Manifests are provenance, not signatures. Recompiling the original authored
    input prevents editing a derived artifact and merely replacing its hash.
    """
    package_dir = safe_path(root, repository_relative(package_dir, root))
    manifest = read_json(safe_path(package_dir, "manifest.json"))
    content_path = safe_path(root, manifest.get("content_path", ""))
    expected, artifacts = compile_content(content_path, root)
    if manifest != expected:
        raise ValueError("Study pack is stale or its manifest was modified; rebuild and review it")
    expected_files = {"manifest.json", *artifacts}
    actual_files = set()
    for path in package_dir.rglob("*"):
        relative = path.relative_to(package_dir).as_posix()
        safe_path(package_dir, relative)
        if path.is_file():
            actual_files.add(relative)
    if actual_files != expected_files:
        raise ValueError("Study pack file inventory differs from the expected artifacts")
    for name, text in artifacts.items():
        actual = safe_path(package_dir, name).read_text(encoding="utf-8")
        if text_sha256(actual) != text_sha256(text):
            raise ValueError(f"Study pack artifact was modified: {name}")
    return manifest
