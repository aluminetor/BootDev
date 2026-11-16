"""Unit tests for viewer/build_index.py using only the Python standard library."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

VIEWER_DIR = Path(__file__).resolve().parent
if str(VIEWER_DIR) not in sys.path:
    sys.path.insert(0, str(VIEWER_DIR))

import build_index  # noqa: E402


class TestPatternsAndHelpers(unittest.TestCase):
    def test_chapter_pattern_matches_expected_names(self) -> None:
        match = build_index.CHAPTER_PATTERN.match("CH13_type_hints.py")
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "13")
        self.assertEqual(match.group(2), "type_hints")
        self.assertIsNone(build_index.CHAPTER_PATTERN.match("Desafios.py"))

    def test_humanize_name(self) -> None:
        self.assertEqual(build_index.humanize_name("type_hints"), "Type hints")
        self.assertEqual(build_index.humanize_name("PythonBeginners"), "Python Beginners")

    def test_classify_comment_line(self) -> None:
        self.assertEqual(build_index.classify_comment_line("#****#"), "separator")
        self.assertEqual(build_index.classify_comment_line("## FUNCTIONS ##"), "header")
        self.assertEqual(
            build_index.classify_comment_line("# don't touch below this line"),
            "boilerplate",
        )
        self.assertEqual(build_index.classify_comment_line("# Regular note"), "comment")

    def test_split_source_lines_normalizes_newlines(self) -> None:
        self.assertEqual(build_index.split_source_lines("a = 1\r\nb = 2\r\n"), ["a = 1", "b = 2"])

    def test_strip_comment_marker(self) -> None:
        self.assertEqual(build_index.strip_comment_marker("  # Hola mundo"), "Hola mundo")
        self.assertEqual(build_index.strip_comment_marker("#Sin espacio"), "Sin espacio")


class TestSegmentationAndAnalysis(unittest.TestCase):
    def test_analyze_strings_falls_back_on_syntax_error(self) -> None:
        source = '"""\nNota\n"""\ndef broken(:\n    pass\n'
        lines = build_index.split_source_lines(source)
        ranges, string_lines, warnings = build_index.analyze_strings(source, lines)
        self.assertEqual(ranges, [(1, 3)])
        self.assertEqual(string_lines, set())
        self.assertEqual(len(warnings), 1)

    def test_segment_exercises_handles_headers_separators_and_boilerplate(self) -> None:
        source = (
            "## Intro ##\n"
            "# Primera nota\n"
            "x = 1  # inline\n"
            "# don't touch below this line\n"
            "print(x)\n"
            "#****#\n"
            "y = 2\n"
        )
        lines = build_index.split_source_lines(source)
        ranges, string_lines, warnings = build_index.analyze_strings(source, lines)
        self.assertEqual(warnings, [])
        kinds = build_index.classify_lines(lines, ranges, string_lines)
        exercises = build_index.segment_exercises(lines, kinds, ranges)

        self.assertEqual(len(exercises), 2)
        self.assertEqual(exercises[0].title, "Intro")
        self.assertEqual(exercises[0].segments[0].type, "theory")
        self.assertEqual(exercises[0].segments[1].type, "code")
        self.assertEqual(exercises[0].segments[1].boilerplate_lines, [4])
        self.assertIsNone(exercises[1].title)

    def test_strip_strings_and_comments_removes_noise(self) -> None:
        code = 'name = "for while"  # def class\nreturn name\n'
        cleaned = build_index.strip_strings_and_comments(code)
        self.assertNotIn("for while", cleaned)
        self.assertNotIn("def class", cleaned)
        self.assertIn("return name", cleaned)


class TestIndexBuild(unittest.TestCase):
    def test_build_index_structure(self) -> None:
        index = build_index.build_index()
        self.assertEqual(index["schemaVersion"], build_index.SCHEMA_VERSION)
        self.assertGreaterEqual(len(index["courses"]), 1)
        first_course = index["courses"][0]
        numbers = [chapter["number"] for chapter in first_course["chapters"]]
        self.assertEqual(numbers, sorted(numbers))
        self.assertGreater(len(index["glossary"]), 0)


if __name__ == "__main__":
    unittest.main()
