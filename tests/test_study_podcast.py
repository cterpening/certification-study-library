import copy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from threading import Thread
import unittest
from unittest.mock import Mock, patch
import wave


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_study_pack as pack_builder
import build_study_podcast as podcast


def wav_bytes(frames=4800):
    result = io.BytesIO()
    with wave.open(result, "wb") as target:
        target.setnchannels(1)
        target.setsampwidth(2)
        target.setframerate(24000)
        target.writeframes(b"\0\0" * frames)
    return result.getvalue()


class PodcastTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write("guides/example.md", "# Example\n\n## Permissions\n\nUnderstand permissions.\n")
        self.write("data/objective-snapshots/ex-100-official-objectives.txt", "Skills measured as of October 1, 2026\nDescribe permissions\n")
        self.write_json("config/exams.json", {"exams": [{"code": "EX-100", "title": "Example", "guide_path": "guides/example.md", "study_guide_url": "https://example.org/exam", "blueprint_last_checked": "2026-10-28"}]})
        self.write_json("data/sources.json", {"sources": [{"id": "permission-reference", "title": "Permission reference", "url": "https://example.org/permissions", "supported_exams": ["EX-100"]}]})
        self.write_json("data/source-health.json", {"sources": [{"id": "permission-reference", "status": "ok"}]})
        self.content = {"schema_version": 1, "exam_code": "EX-100", "language": "en", "scope_note": "Selected permission concepts, not a complete exam review.", "units": [{
            "id": "permissions", "title": "Permissions", "guide_sections": ["Permissions"], "objectives": ["Describe permissions"], "source_ids": ["permission-reference"],
            "summary": "Permissions control operations.", "key_points": ["Check the principal and scope."], "scenario": {"question": "Which permissions apply?", "answer": "Inspect the principal and scope."},
            "visual": {"title": "Permission relationship", "nodes": [{"id": "principal", "label": "Principal"}, {"id": "operation", "label": "Operation"}], "edges": [{"from": "principal", "to": "operation", "label": "may perform"}]},
            "dialogue": [{"speaker": "host", "text": "Which principal is trying to perform the operation?"}, {"speaker": "learner", "text": "The caller's identity and scope determine which permissions apply."}]}]}
        self.content_path = self.write_json("data/study-content/example.json", self.content)
        self.package = self.root / "pack"
        self.output = self.root / "podcast"
        self.episode = self.output / "part-01"
        self.env = {"ELEVENLABS_API_KEY": "test-secret-do-not-log", "ELEVENLABS_HOST_VOICE_ID": "voice-host", "ELEVENLABS_LEARNER_VOICE_ID": "voice-learner"}

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def write_json(self, name, value):
        return self.write(name, podcast.json_text(value))

    def prepare(self, target=None):
        self.content_path.write_text(podcast.json_text(self.content), encoding="utf-8")
        pack_builder.build(self.content_path, self.package, self.root)
        return podcast.prepare(self.package, self.output, target, self.root)

    def review(self):
        return podcast.review(self.episode, "Test reviewer", "ai", "Checked script against the source unit; no audio listened to.", self.root)

    def render(self, sender=None, limit=20):
        return podcast.render(self.episode, self.root, limit, self.env, sender or Mock(return_value=wav_bytes()))

    def test_prepare_is_offline_and_has_portable_sources_disclosures(self):
        with patch.object(podcast, "request_audio", side_effect=AssertionError("Network forbidden")):
            result = self.prepare()
            metadata, script, _ = podcast.load_episode(self.episode, self.root)
        self.assertEqual(1, len(result["episodes"]))
        self.assertIsNone(result["target_minutes"])
        self.assertEqual("not-generated", metadata["audio_status_at_preparation"])
        transcript = (self.episode / "transcript.md").read_text(encoding="utf-8")
        self.assertIn("https://example.org/permissions", transcript)
        self.assertIn("(<../../pack/study-guide.md>)", transcript)
        self.assertIn("(<../../guides/example.md>)", transcript)
        self.assertIn("HUMAN REVIEW PENDING", transcript)
        self.assertIn("October 1, 2026", transcript)
        self.assertEqual({"host", "learner"}, {turn["speaker"] for section in script["sections"] for turn in section["turns"]})
        spoken = " ".join(turn["text"] for section in script["sections"] for turn in section["turns"])
        self.assertNotIn("https://", spoken)

    def test_soft_duration_splits_between_topics_without_truncation(self):
        self.content["units"][0]["dialogue"][0]["text"] = "Explain this important concept. " * 70
        second = copy.deepcopy(self.content["units"][0])
        second["id"] = "permissions-second"
        self.content["units"].append(second)
        result = self.prepare(1)
        self.assertEqual(2, len(result["episodes"]))
        self.assertTrue(all(part["warnings"] for part in result["episodes"]))
        _, script, _ = podcast.load_episode(self.episode, self.root)
        self.assertEqual(["permissions"], script["unit_ids"])
        self.assertEqual(70, script["sections"][1]["turns"][0]["text"].count("Explain"))

    def test_invalid_targets_and_existing_output_are_refused(self):
        for target in (0, -1, float("inf"), float("nan")):
            with self.subTest(target=target), self.assertRaises(ValueError):
                podcast.split_parts(self.content["units"], target)
        self.prepare()
        with self.assertRaisesRegex(ValueError, "new podcast"):
            podcast.prepare(self.package, self.output, root=self.root)

    def test_source_changes_invalidate_episode_before_any_audio(self):
        self.prepare()
        self.review()
        self.write("guides/example.md", "# Changed guide\n")
        sender = Mock(return_value=wav_bytes())
        with self.assertRaises(ValueError):
            self.render(sender)
        sender.assert_not_called()

    def test_script_edits_are_rejected_even_if_hash_is_resealed(self):
        self.prepare()
        script = podcast.read_json(self.episode / "script.json")
        script["sections"][1]["turns"][0]["text"] = "An unsupported technical claim."
        (self.episode / "script.json").write_text(podcast.json_text(script), encoding="utf-8")
        metadata = podcast.read_json(self.episode / "episode.json")
        metadata["script_sha256"] = podcast.fingerprint(self.episode / "script.json")
        (self.episode / "episode.json").write_text(podcast.json_text(metadata), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "source package"):
            podcast.load_episode(self.episode, self.root)

    def test_paths_cannot_escape_repository(self):
        self.prepare()
        with self.assertRaises(ValueError):
            podcast.prepare(self.package, self.root.parent / "outside-podcast", root=self.root)
        metadata = podcast.read_json(self.episode / "episode.json")
        metadata["package_path"] = "../outside-pack"
        (self.episode / "episode.json").write_text(podcast.json_text(metadata), encoding="utf-8")
        with self.assertRaises(ValueError):
            podcast.load_episode(self.episode, self.root)

    def test_review_and_credentials_required_before_network(self):
        self.prepare()
        sender = Mock()
        with self.assertRaises(ValueError):
            self.render(sender)
        self.review()
        for env in ({}, {**self.env, "ELEVENLABS_LEARNER_VOICE_ID": "voice-host"}):
            with self.subTest(env=bool(env)), self.assertRaises(ValueError):
                podcast.render(self.episode, self.root, environ=env, sender=sender)
        sender.assert_not_called()

    def test_stale_review_receipt_cannot_render(self):
        self.prepare()
        receipt = self.review()
        receipt["script_sha256"] = "0" * 64
        (self.episode / "script-review.json").write_text(podcast.json_text(receipt), encoding="utf-8")
        sender = Mock()
        with self.assertRaisesRegex(ValueError, "stale"):
            self.render(sender)
        sender.assert_not_called()

    def test_audio_render_combines_wav_and_reuses_cache(self):
        self.prepare()
        self.review()
        sender = Mock(return_value=wav_bytes())
        result = self.render(sender)
        self.assertEqual("generated-listening-review-pending", result["status"])
        self.assertEqual("pending", result["listening_review"])
        self.assertEqual(3, sender.call_count)
        with wave.open(str(self.episode / "audio/episode.wav"), "rb") as audio:
            self.assertEqual(4800 * 3, audio.getnframes())
        chapters = podcast.read_json(self.episode / "audio/chapters.json")["chapters"]
        self.assertEqual([0.0, 0.2, 0.4], [chapter["start_seconds"] for chapter in chapters])
        second = self.render(sender)
        self.assertEqual(3, sender.call_count)
        self.assertEqual(0, second["new_requests"])
        self.assertTrue(all(chunk["cached"] for chunk in second["chunks"]))
        for path in self.episode.rglob("*.json"):
            self.assertNotIn(self.env["ELEVENLABS_API_KEY"], path.read_text(encoding="utf-8"))

    def test_partial_failure_resumes_completed_chunks_only(self):
        self.prepare()
        self.review()
        first = Mock(side_effect=[wav_bytes(), ValueError("Speech service returned HTTP 429; no automatic paid retry")])
        with self.assertRaisesRegex(ValueError, "429"):
            self.render(first)
        receipt = podcast.read_json(self.episode / "audio/render.json")
        self.assertEqual("partial", receipt["status"])
        self.assertEqual(1, len(receipt["chunks"]))
        second = Mock(return_value=wav_bytes())
        completed = self.render(second)
        self.assertEqual(2, second.call_count)
        self.assertTrue(completed["chunks"][0]["cached"])

    def test_request_budget_preserves_resumable_partial_receipt(self):
        self.prepare()
        self.review()
        with self.assertRaisesRegex(ValueError, "budget"):
            self.render(limit=1)
        self.assertEqual("partial", podcast.read_json(self.episode / "audio/render.json")["status"])
        self.assertEqual(2, self.render()["new_requests"])

    def test_changed_voice_does_not_reuse_old_audio(self):
        self.prepare()
        self.review()
        self.render()
        self.env["ELEVENLABS_HOST_VOICE_ID"] = "another-host"
        sender = Mock(return_value=wav_bytes())
        self.assertEqual(3, self.render(sender)["new_requests"])

    def test_corrupt_cache_fails_without_paid_retry(self):
        self.prepare()
        self.review()
        result = self.render()
        path = self.episode / "audio" / result["chunks"][0]["path"]
        path.write_bytes(b"corrupt")
        sender = Mock()
        with self.assertRaisesRegex(ValueError, "cache hash"):
            self.render(sender)
        sender.assert_not_called()

    def test_long_turn_splits_without_losing_words(self):
        self.prepare()
        _, script, _ = podcast.load_episode(self.episode, self.root)
        text = "An explanation with a clear sentence. " * 200
        script["sections"][1]["turns"][0]["text"] = text.strip()
        chunks = podcast.audio_chunks(script)
        selected = [chunk for chunk in chunks if chunk["unit_id"] == "permissions"]
        self.assertGreater(len(selected), 1)
        self.assertTrue(all(sum(len(turn["text"]) for turn in chunk["turns"]) <= 2000 for chunk in chunks))
        reconstructed = " ".join(turn["text"] for chunk in selected for turn in chunk["turns"] if turn["speaker"] == "host")
        self.assertEqual(text.strip(), reconstructed)
        with self.assertRaisesRegex(ValueError, "token"):
            podcast.split_turn("x" * 2001)

    def test_wav_validation_rejects_non_audio_and_truncation(self):
        for data in (b"{}", wav_bytes()[:-100], wav_bytes(frames=1)):
            with self.subTest(length=len(data)), self.assertRaises(ValueError):
                podcast.inspect_wav(data)

    def test_http_adapter_sends_documented_fields_and_receives_wav(self):
        observed = []
        audio = wav_bytes()

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                observed.append((self.path, self.headers.get("xi-api-key"), json.loads(self.rfile.read(int(self.headers["Content-Length"])))))
                self.send_response(200)
                self.send_header("Content-Type", "audio/wav")
                self.end_headers()
                self.wfile.write(audio)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.addCleanup(server.server_close)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.shutdown)
        payload = {"model_id": "eleven_v3", "inputs": [{"text": "Hello", "voice_id": "voice-host"}]}
        with patch.object(podcast, "API_URL", f"http://127.0.0.1:{server.server_port}/v1/text-to-dialogue?output_format=wav_24000"):
            self.assertEqual(audio, podcast.request_audio(payload, "test-key"))
        self.assertEqual("test-key", observed[0][1])
        self.assertEqual(payload, observed[0][2])
        self.assertIn("output_format=wav_24000", observed[0][0])

    def test_http_errors_do_not_expose_provider_body_or_credentials(self):
        from urllib.error import HTTPError
        failure = HTTPError(podcast.API_URL, 401, "secret provider detail", {}, io.BytesIO(b"sensitive body"))
        opener = Mock()
        opener.open.side_effect = failure
        with patch.object(podcast, "build_opener", return_value=opener), self.assertRaises(ValueError) as error:
            podcast.request_audio({"inputs": []}, "secret-key")
        self.assertEqual("Speech service returned HTTP 401; no automatic paid retry", str(error.exception))

    def test_chunked_disconnect_records_failure_and_preserves_completed_cache(self):
        self.prepare()
        self.review()
        requests = []
        audio = wav_bytes()

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                requests.append(self.rfile.read(int(self.headers["Content-Length"])))
                self.send_response(200)
                self.send_header("Content-Type", "audio/wav")
                if len(requests) in {1, 3}:
                    self.send_header("Transfer-Encoding", "chunked")
                    self.end_headers()
                    # Advertise a larger chunk, then drop the connection midway.
                    self.wfile.write(b"100\r\nprivate-incomplete-provider-payload")
                    self.wfile.flush()
                    self.close_connection = True
                    return
                self.send_header("Content-Length", str(len(audio)))
                self.end_headers()
                self.wfile.write(audio)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.addCleanup(server.server_close)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.shutdown)
        endpoint = f"http://127.0.0.1:{server.server_port}/v1/text-to-dialogue?output_format=wav_24000"
        safe_error = "Speech service connection failed; no automatic paid retry"
        with patch.object(podcast, "API_URL", endpoint):
            with self.assertRaisesRegex(ValueError, safe_error):
                podcast.render(self.episode, self.root, environ=self.env)
            failed = podcast.read_json(self.episode / "audio/render.json")
            self.assertEqual("failed", failed["status"])
            self.assertEqual([], failed["chunks"])
            self.assertEqual(safe_error, failed["error"])
            with self.assertRaisesRegex(ValueError, safe_error):
                podcast.render(self.episode, self.root, environ=self.env)
            partial = podcast.read_json(self.episode / "audio/render.json")
            self.assertEqual("partial", partial["status"])
            self.assertEqual(1, len(partial["chunks"]))
            cached_path = self.episode / "audio" / partial["chunks"][0]["path"]
            cached_bytes = cached_path.read_bytes()
            result = podcast.render(self.episode, self.root, environ=self.env)
        self.assertEqual(5, len(requests))
        self.assertEqual("generated-listening-review-pending", result["status"])
        self.assertTrue(result["chunks"][0]["cached"])
        self.assertEqual(cached_bytes, cached_path.read_bytes())
        self.assertEqual(2, result["new_requests"])
        self.assertNotIn("private-incomplete-provider-payload", podcast.json_text(failed))

    def test_redirects_are_refused(self):
        with self.assertRaisesRegex(ValueError, "redirects"):
            podcast.NoRedirect().redirect_request(None, None, 302, "redirect", {}, "https://other.example/")


if __name__ == "__main__":
    unittest.main()
