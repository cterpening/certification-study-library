#!/usr/bin/env python3
"""Prepare version-bound two-host episodes; optionally render reviewed scripts.

Preparation is offline. Only the explicit render command calls ElevenLabs.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
from http.client import HTTPException
import io
import json
import math
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener
import wave

from study_material import ROOT, load_package, read_json, repository_relative, safe_path, text_sha256


API_URL = "https://api.elevenlabs.io/v1/text-to-dialogue?output_format=wav_24000"
MODEL_ID = "eleven_v3"
MAX_REQUEST_CHARACTERS = 2000
MAX_RESPONSE_BYTES = 25 * 1024 * 1024
WORDS_PER_MINUTE = 145
SPEAKERS = {"host", "learner"}


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def write_json(path: Path, value: object) -> None:
    """Replace one local receipt atomically, without following a destination link."""
    if path.is_symlink():
        raise ValueError(f"Refusing linked output: {path.name}")
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(json_text(value))
    temporary.replace(path)


def fingerprint(path: Path) -> str:
    return text_sha256(path.read_text(encoding="utf-8"))


def contained_file(directory: Path, name: str) -> Path:
    path = safe_path(directory, name)
    if not path.is_file() or path.resolve().parent != directory.resolve():
        raise ValueError(f"Missing or linked episode file: {name}")
    return path


def spoken_text(text: object) -> str:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Every dialogue turn needs spoken text")
    if re.search(r"https?://|www\.|```|\[[^\]]+\]\(", text, re.IGNORECASE):
        raise ValueError("Dialogue must describe links and code in words; keep URLs in show notes")
    if any(ord(char) < 32 and char not in "\n\t" for char in text):
        raise ValueError("Dialogue contains control characters")
    return " ".join(text.split())


def word_count(turns: list[dict]) -> int:
    return sum(len(turn["text"].split()) for turn in turns)


def split_parts(units: list[dict], target_minutes: float | None) -> list[list[dict]]:
    if target_minutes is not None and (not math.isfinite(target_minutes) or target_minutes <= 0):
        raise ValueError("Target minutes must be a finite positive number")
    if not units:
        raise ValueError("The package has no learning units")
    if target_minutes is None:
        return [units]
    target_words = target_minutes * WORDS_PER_MINUTE
    parts: list[list[dict]] = []
    current: list[dict] = []
    count = 0
    for unit in units:
        next_count = word_count(unit["dialogue"])
        if current and count + next_count > target_words:
            parts.append(current)
            current, count = [], 0
        current.append(unit)
        count += next_count
    if current:
        parts.append(current)
    return parts


def episode_script(manifest: dict, units: list[dict], part: int, total: int) -> dict:
    baseline = manifest.get("baseline", "See the accepted objective snapshot")
    checked = manifest.get("blueprint_last_checked", "not recorded")
    intro = (
        f"Welcome to our {manifest['exam_code']} study conversation, part {part} of {total}. "
        "This is an independent, AI-assisted study resource with synthetic voices. "
        "Human review is pending. The official exam blueprint is authoritative. "
        f"Our source package uses this baseline: {baseline}. "
        f"Its recorded blueprint check was {checked}; preparing this episode does not renew that review. "
        f"Today's scope: {manifest['scope_note']}"
    )
    sections = [{"unit_id": "introduction", "title": "Introduction", "turns": [
        {"speaker": "host", "text": spoken_text(intro)},
        {"speaker": "learner", "text": "We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids."},
    ]}]
    for unit in units:
        turns = []
        for turn in unit["dialogue"]:
            if turn.get("speaker") not in SPEAKERS:
                raise ValueError("Only the host and learner speakers are supported")
            turns.append({"speaker": turn["speaker"], "text": spoken_text(turn["text"])})
        if {turn["speaker"] for turn in turns} != SPEAKERS:
            raise ValueError(f"Unit {unit['id']} needs both speakers")
        sections.append({"unit_id": unit["id"], "title": unit["title"], "turns": turns})
    sections.append({"unit_id": "recap", "title": "Next steps", "turns": [
        {"speaker": "learner", "text": "Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps."},
        {"speaker": "host", "text": "Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage."},
    ]})
    return {"schema_version": 1, "exam_code": manifest["exam_code"], "language": manifest["language"],
            "part": part, "total_parts": total, "unit_ids": [unit["id"] for unit in units],
            "sections": sections}


def transcript(script: dict, package_manifest: dict, units: list[dict], sources: dict,
               companion_path: str | None = None, guide_path: str | None = None) -> str:
    lines = [f"# {package_manifest['exam_code']} study conversation — Part {script['part']}", "",
             "> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.", "",
             f"The [official blueprint]({package_manifest['blueprint_url']}) is authoritative.", "",
             f"Scope: {package_manifest['scope_note']}", "",
             f"Baseline: {package_manifest.get('baseline', 'See accepted snapshot')}. "
             f"Recorded blueprint check: {package_manifest.get('blueprint_last_checked', 'not recorded')}.", "",
             "This is a production script, not an assertion that audio has been generated or listened to.", ""]
    if companion_path:
        lines += [f"[Companion study guide, practice questions and visual aids](<{companion_path}>)", ""]
    if guide_path:
        lines += [f"[Full source study guide](<{guide_path}>)", ""]
    for section in script["sections"]:
        lines += [f"## {section['title']}", ""]
        for turn in section["turns"]:
            lines += [f"**{turn['speaker'].title()}:** {turn['text']}", ""]
    lines += ["## Show notes", "", "These registered sources are pinned through the study package's input fingerprints.", ""]
    for unit in units:
        references = ", ".join(f"[{sources[key]['title']}]({sources[key]['url']})" for key in unit["source_ids"])
        lines += [f"- **{unit['title']}** — {references}. "
                  f"Guide sections: {'; '.join(unit['guide_sections'])}."]
    return "\n".join(lines) + "\n"


def prepare(package: Path, output: Path, target_minutes: float | None = None, root: Path = ROOT) -> dict:
    package = safe_path(root, repository_relative(package, root))
    package_manifest = load_package(package, root)
    sources = {row["id"]: row for row in read_json(safe_path(root, "data/sources.json"))["sources"]}
    content = read_json(package / "units.json")
    parts = split_parts(content["units"], target_minutes)
    # Validate every part before creating the output directory.
    scripts = [episode_script(package_manifest, part, index, len(parts))
               for index, part in enumerate(parts, 1)]
    output = safe_path(root, repository_relative(output, root))
    if output.exists() or output.is_symlink():
        raise ValueError("Choose a new podcast output directory")
    output.mkdir(parents=True)
    series = {"schema_version": 1, "exam_code": package_manifest["exam_code"],
              "format": "two-host-conversation", "target_minutes": target_minutes,
              "duration_policy": "Topic boundaries; estimates only, no hard episode limit", "episodes": []}
    for index, (units, script) in enumerate(zip(parts, scripts), 1):
        episode = output / f"part-{index:02d}"
        episode.mkdir()
        write_json(episode / "script.json", script)
        companion_path = os.path.relpath(package / "study-guide.md", episode).replace("\\", "/")
        guide_path = os.path.relpath(safe_path(root, package_manifest["guide_path"]), episode).replace("\\", "/")
        (episode / "transcript.md").write_text(transcript(script, package_manifest, units, sources, companion_path, guide_path), encoding="utf-8", newline="\n")
        words = sum(word_count(section["turns"]) for section in script["sections"])
        estimate = round(words / WORDS_PER_MINUTE, 1)
        warnings = []
        if target_minutes and estimate > target_minutes:
            warnings.append("Topic or introduction exceeds the soft target; split the authored unit if a shorter part is useful.")
        metadata = {"schema_version": 1, "package_path": repository_relative(package, root),
                    "package_manifest_sha256": fingerprint(package / "manifest.json"),
                    "script_sha256": fingerprint(episode / "script.json"),
                    "transcript_sha256": fingerprint(episode / "transcript.md"),
                    "word_count": words, "estimated_minutes": estimate, "warnings": warnings,
                    "review_status_at_preparation": "script-review-pending", "audio_status_at_preparation": "not-generated"}
        write_json(episode / "episode.json", metadata)
        series["episodes"].append({"path": episode.name, "unit_ids": script["unit_ids"],
                                   "word_count": words, "estimated_minutes": estimate, "warnings": warnings})
    write_json(output / "series.json", series)
    return series


def load_episode(episode: Path, root: Path = ROOT) -> tuple[dict, dict, dict]:
    episode = safe_path(root, repository_relative(episode, root))
    metadata = read_json(contained_file(episode, "episode.json"))
    if metadata.get("schema_version") != 1:
        raise ValueError("Unsupported episode schema")
    package_value = metadata.get("package_path")
    if not isinstance(package_value, str) or not package_value or Path(package_value).is_absolute():
        raise ValueError("Episode package_path must be a relative path")
    package = safe_path(root, package_value)
    package_manifest = load_package(package, root)
    if fingerprint(package / "manifest.json") != metadata.get("package_manifest_sha256"):
        raise ValueError("Study package changed; prepare and review the episode again")
    for name, field in (("script.json", "script_sha256"), ("transcript.md", "transcript_sha256")):
        if fingerprint(contained_file(episode, name)) != metadata.get(field):
            raise ValueError(f"Episode {name} changed; update the source units and prepare again")
    script = read_json(episode / "script.json")
    units = read_json(package / "units.json")["units"]
    unit_ids = script.get("unit_ids")
    if not isinstance(unit_ids, list) or not unit_ids or len(set(unit_ids)) != len(unit_ids):
        raise ValueError("Episode needs distinct source units")
    by_id = {unit["id"]: unit for unit in units}
    if any(unit_id not in by_id for unit_id in unit_ids):
        raise ValueError("Unknown episode unit")
    selected = [by_id[unit_id] for unit_id in unit_ids]
    part, total = script.get("part"), script.get("total_parts")
    if type(part) is not int or type(total) is not int or not 1 <= part <= total <= 100:
        raise ValueError("Invalid episode part numbers")
    expected = episode_script(package_manifest, selected, part, total)
    sources = {row["id"]: row for row in read_json(safe_path(root, "data/sources.json"))["sources"]}
    companion_path = os.path.relpath(package / "study-guide.md", episode).replace("\\", "/")
    guide_path = os.path.relpath(safe_path(root, package_manifest["guide_path"]), episode).replace("\\", "/")
    if script != expected or (episode / "transcript.md").read_text(encoding="utf-8") != transcript(expected, package_manifest, selected, sources, companion_path, guide_path):
        raise ValueError("Episode content no longer matches its source package")
    return metadata, script, package_manifest


def review(episode: Path, reviewer: str, kind: str, notes: str, root: Path = ROOT) -> dict:
    episode = safe_path(root, repository_relative(episode, root))
    metadata, _, _ = load_episode(episode, root)
    if kind not in {"ai", "human"} or not reviewer.strip() or not notes.strip():
        raise ValueError("Record reviewer, ai/human review kind, and specific review notes")
    receipt = {"schema_version": 1, "reviewer": reviewer, "kind": kind,
               "notes": notes, "reviewed_at": datetime.now(timezone.utc).isoformat(),
               "script_sha256": metadata["script_sha256"],
               "package_manifest_sha256": metadata["package_manifest_sha256"],
               "scope": "Script meaning, source agreement, two-speaker delivery and spoken visual explanations; not audio listening or full guide validation"}
    write_json(episode / "script-review.json", receipt)
    return receipt


def require_review(episode: Path, metadata: dict) -> dict:
    receipt = read_json(contained_file(episode, "script-review.json"))
    if (receipt.get("schema_version") != 1 or receipt.get("kind") not in {"ai", "human"}
            or not receipt.get("reviewer") or not receipt.get("notes")
            or any(receipt.get(field) != metadata[field]
                   for field in ("script_sha256", "package_manifest_sha256"))):
        raise ValueError("Script review is missing or stale; review this exact script before rendering")
    return receipt


def split_turn(text: str, limit: int = MAX_REQUEST_CHARACTERS) -> list[str]:
    """Split a long turn at sentence or word boundaries, preserving spoken content."""
    pieces: list[str] = []
    remaining = text
    while len(remaining) > limit:
        candidates = list(re.finditer(r"[.!?]\s+", remaining[:limit + 1]))
        cut = candidates[-1].end() - 1 if candidates else remaining.rfind(" ", 0, limit + 1)
        if cut <= 0:
            raise ValueError("A dialogue token exceeds the service limit; rewrite the source unit")
        pieces.append(remaining[:cut].strip())
        remaining = remaining[cut:].strip()
    if remaining:
        pieces.append(remaining)
    return pieces


def audio_chunks(script: dict) -> list[dict]:
    chunks = []
    for section in script["sections"]:
        turns: list[dict] = []
        characters = 0
        for turn in section["turns"]:
            for text in split_turn(turn["text"]):
                if turns and characters + len(text) > MAX_REQUEST_CHARACTERS:
                    chunks.append({"unit_id": section["unit_id"], "title": section["title"], "turns": turns})
                    turns, characters = [], 0
                turns.append({"speaker": turn["speaker"], "text": text})
                characters += len(text)
        if turns:
            chunks.append({"unit_id": section["unit_id"], "title": section["title"], "turns": turns})
    return chunks


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Speech service redirects are refused")


def request_audio(payload: dict, api_key: str) -> bytes:
    request = Request(API_URL, data=json.dumps(payload).encode("utf-8"), method="POST",
                      headers={"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/wav"})
    try:
        with build_opener(NoRedirect()).open(request, timeout=90) as response:
            data = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as error:
        # Never include response bodies, headers, credentials or raw provider exceptions.
        raise ValueError(f"Speech service returned HTTP {error.code}; no automatic paid retry") from None
    except (URLError, TimeoutError, OSError, HTTPException):
        raise ValueError("Speech service connection failed; no automatic paid retry") from None
    if len(data) > MAX_RESPONSE_BYTES:
        raise ValueError("Speech response exceeds the bounded download size")
    inspect_wav(data)
    return data


def inspect_wav(data: bytes) -> tuple[int, int, int, int]:
    try:
        with wave.open(io.BytesIO(data), "rb") as audio:
            channels, width, rate, frames = audio.getnchannels(), audio.getsampwidth(), audio.getframerate(), audio.getnframes()
            if channels != 1 or width != 2 or rate != 24000 or frames < 2400:
                raise ValueError("Expected nonempty 24 kHz mono PCM WAV from speech service")
            if len(audio.readframes(frames)) != frames * channels * width:
                raise ValueError("Speech service returned truncated WAV audio")
            return channels, width, rate, frames
    except (wave.Error, EOFError):
        raise ValueError("Speech service did not return valid PCM WAV audio") from None


def render(episode: Path, root: Path = ROOT, max_new_requests: int = 20,
           environ: dict | None = None, sender=None) -> dict:
    episode = safe_path(root, repository_relative(episode, root))
    metadata, script, _ = load_episode(episode, root)
    require_review(episode, metadata)
    if type(max_new_requests) is not int or not 1 <= max_new_requests <= 100:
        raise ValueError("max-new-requests must be between 1 and 100")
    env = os.environ if environ is None else environ
    key = env.get("ELEVENLABS_API_KEY", "")
    voices = {"host": env.get("ELEVENLABS_HOST_VOICE_ID", ""),
              "learner": env.get("ELEVENLABS_LEARNER_VOICE_ID", "")}
    if not key or any(not re.fullmatch(r"[A-Za-z0-9_-]{1,100}", voice) for voice in voices.values()):
        raise ValueError("Set ELEVENLABS_API_KEY, ELEVENLABS_HOST_VOICE_ID and ELEVENLABS_LEARNER_VOICE_ID before rendering")
    if voices["host"] == voices["learner"]:
        raise ValueError("Choose two distinct host voice IDs")
    audio_dir = safe_path(episode, "audio")
    audio_dir.mkdir(exist_ok=True)
    chunks = audio_chunks(script)
    send = request_audio if sender is None else sender
    result = {"schema_version": 1, "provider": "elevenlabs", "model_id": MODEL_ID,
              "output_format": "wav_24000", "voice_ids": voices, "script_sha256": metadata["script_sha256"],
              "package_manifest_sha256": metadata["package_manifest_sha256"], "status": "in-progress",
              "listening_review": "pending", "new_requests": 0, "chunks": []}
    # A different voice/model plan must not leave a previous final episode looking current.
    final_path = safe_path(audio_dir, "episode.wav")
    if final_path.exists() or final_path.is_symlink():
        if final_path.is_symlink() or not final_path.is_file():
            raise ValueError("Invalid existing episode audio output")
        final_path.unlink()
    write_json(audio_dir / "render.json", result)
    started = time.monotonic()
    try:
        for index, chunk in enumerate(chunks, 1):
            payload = {"model_id": MODEL_ID, "language_code": script["language"],
                       "inputs": [{"text": turn["text"], "voice_id": voices[turn["speaker"]]} for turn in chunk["turns"]]}
            request_hash = text_sha256(json_text({"url": API_URL, "payload": payload}))
            name = f"chunk-{index:04d}-{request_hash[:16]}"
            wav_path, receipt_path = safe_path(audio_dir, f"{name}.wav"), safe_path(audio_dir, f"{name}.json")
            cached = False
            if wav_path.exists() or receipt_path.exists():
                if wav_path.is_symlink() or receipt_path.is_symlink() or not wav_path.is_file() or not receipt_path.is_file():
                    raise ValueError("Incomplete or linked audio cache entry; inspect it before retrying")
                receipt = read_json(receipt_path)
                if wav_path.stat().st_size > MAX_RESPONSE_BYTES:
                    raise ValueError("Audio cache entry exceeds the bounded response size")
                data = wav_path.read_bytes()
                if receipt.get("request_sha256") != request_hash or receipt.get("audio_sha256") != sha256(data).hexdigest():
                    raise ValueError("Audio cache hash mismatch; inspect it before retrying")
                inspect_wav(data)
                cached = True
            else:
                if result["new_requests"] >= max_new_requests:
                    raise ValueError("New-request budget reached; rerun to resume the remaining chunks")
                if time.monotonic() - started > 600:
                    raise ValueError("Render time budget reached; rerun to resume remaining chunks")
                result["new_requests"] += 1
                write_json(audio_dir / "render.json", result)
                data = send(payload, key)
                inspect_wav(data)
                with wav_path.open("xb") as handle:
                    handle.write(data)
                write_json(receipt_path, {"request_sha256": request_hash, "audio_sha256": sha256(data).hexdigest()})
            _, _, rate, frames = inspect_wav(data)
            result["chunks"].append({"path": wav_path.name, "unit_id": chunk["unit_id"], "title": chunk["title"],
                                     "request_sha256": request_hash, "audio_sha256": sha256(data).hexdigest(),
                                     "seconds": round(frames / rate, 3), "cached": cached})
            write_json(audio_dir / "render.json", result)
        chapters = []
        elapsed_frames = 0
        with wave.open(str(final_path), "wb") as target:
            target.setnchannels(1)
            target.setsampwidth(2)
            target.setframerate(24000)
            for chunk in result["chunks"]:
                if not chapters or chapters[-1]["unit_id"] != chunk["unit_id"]:
                    chapters.append({"unit_id": chunk["unit_id"], "title": chunk["title"], "start_seconds": round(elapsed_frames / 24000, 3)})
                with wave.open(str(audio_dir / chunk["path"]), "rb") as source:
                    target.writeframes(source.readframes(source.getnframes()))
                    elapsed_frames += source.getnframes()
        write_json(audio_dir / "chapters.json", {"chapters": chapters})
        result.update({"status": "generated-listening-review-pending", "audio_path": "episode.wav",
                       "audio_sha256": sha256(final_path.read_bytes()).hexdigest(),
                       "duration_seconds": round(elapsed_frames / 24000, 3)})
    except (ValueError, OSError) as error:
        result["status"] = "partial" if result["chunks"] else "failed"
        # Safe local error only. Raw network errors are sanitized by request_audio.
        result["error"] = str(error) if isinstance(error, ValueError) else "Local audio file operation failed"
        write_json(audio_dir / "render.json", result)
        raise ValueError(result["error"]) from None
    write_json(audio_dir / "render.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    prep = subparsers.add_parser("prepare", help="Build offline two-host scripts from a study package")
    prep.add_argument("--package", type=Path, required=True)
    prep.add_argument("--output-dir", type=Path, required=True)
    prep.add_argument("--target-minutes", type=float, help="Soft target; split only at learning-unit boundaries")
    for name in ("check", "plan", "review", "render"):
        sub = subparsers.add_parser(name)
        sub.add_argument("--episode-dir", type=Path, required=True)
        if name == "review":
            sub.add_argument("--reviewer", required=True)
            sub.add_argument("--kind", choices=("ai", "human"), required=True)
            sub.add_argument("--notes", required=True)
        if name == "render":
            sub.add_argument("--max-new-requests", type=int, default=20)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            result = prepare(args.package, args.output_dir, args.target_minutes)
        elif args.command == "review":
            result = review(args.episode_dir, args.reviewer, args.kind, args.notes)
        elif args.command == "render":
            result = render(args.episode_dir, max_new_requests=args.max_new_requests)
        else:
            metadata, script, _ = load_episode(args.episode_dir)
            result = {"status": "current", "estimated_minutes": metadata["estimated_minutes"],
                      "service_requests": len(audio_chunks(script)),
                      "characters": sum(len(turn["text"]) for section in script["sections"] for turn in section["turns"]),
                      "audio_checked": False, "note": "Plan/check makes no network calls; inspect audio/render.json for actual production state"}
        print(json_text(result), end="")
        return 0
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f"Podcast workflow failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
