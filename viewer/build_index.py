"""Build viewer/data/index.json from the BootDev study folders.

The study files are opened read-only: this script never modifies, formats,
renames or moves them. Only the Python standard library is used.

Usage (from the repository root):
    python viewer/build_index.py
"""

from __future__ import annotations

import ast
import io
import json
import re
import sys
import tokenize
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

VIEWER_DIR = Path(__file__).resolve().parent
REPO_ROOT = VIEWER_DIR.parent
OUTPUT_PATH = VIEWER_DIR / "data" / "index.json"
GLOSSARY_PATH = VIEWER_DIR / "glossary.json"
HOME_FILE_NAME = "README.md"
SCHEMA_VERSION = 1

IGNORED_DIRS = {"viewer", ".agents", ".git", ".vscode", "__pycache__", "node_modules"}
ENCODINGS = ("utf-8", "utf-8-sig", "cp1252")

CHAPTER_PATTERN = re.compile(r"^CH(\d{2})_(\w+)\.py$")
SEPARATOR_PATTERN = re.compile(r"^#+[-*=_]{3,}(?:[^-*=_]{0,30}[-*=_]{3,})?#*\s*$")
HEADER_PATTERN = re.compile(r"^(?:#{2,}|#\s*#+)\s*([^#\s*\-].*?)\s*#*\s*$")
BOILERPLATE_PATTERN = re.compile(
    r"^#\s*don'?t\s+(touch|edit|modify)\s+(above|below)\s+this\s+line", re.IGNORECASE
)
OPENING_QUOTE_PATTERN = re.compile(r"^\s*[rRuUbB]{0,2}(\"\"\"|'''|\"|')")
CLOSING_QUOTE_PATTERN = re.compile(r"(\"\"\"|'''|\"|')\s*$")
STRING_LITERAL_PATTERN = re.compile(
    r"([rRbBuUfF]{0,2})(\"\"\"|'''|\"|')(.*?)\2", re.DOTALL
)
INLINE_COMMENT_PATTERN = re.compile(r"#.*$", re.MULTILINE)

TITLE_MAX_LENGTH = 60
TITLE_ALLOWED_PREVIOUS_KINDS = {None, "code", "boilerplate", "docstring", "separator"}
THEORY_KINDS = {"comment", "docstring"}
CODE_KINDS = {"code", "boilerplate"}


# --------------------------------------------------------------------------- #
# Data structures
# --------------------------------------------------------------------------- #


@dataclass
class Segment:
    type: str  # "theory" | "code"
    start_line: int
    end_line: int
    lines: list[str] = field(default_factory=list)
    boilerplate_lines: list[int] = field(default_factory=list)
    pending_blank_lines: list[int] = field(default_factory=list)

    def to_dict(self) -> dict:
        text = "\n".join(self.lines)
        if self.type == "theory":
            text = collapse_blank_lines(text)
        data = {
            "type": self.type,
            "startLine": self.start_line,
            "endLine": self.end_line,
            "text": text,
        }
        if self.type == "code":
            data["boilerplateLines"] = self.boilerplate_lines
        return data


@dataclass
class Exercise:
    title: str | None = None
    title_line: int | None = None
    segments: list[Segment] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# File reading
# --------------------------------------------------------------------------- #


def read_text_file(path: Path) -> tuple[str | None, list[str]]:
    """Return (text, warnings). Text is None when no encoding works."""
    raw_bytes = path.read_bytes()
    warnings: list[str] = []
    for encoding in ENCODINGS:
        try:
            text = raw_bytes.decode(encoding)
        except UnicodeDecodeError:
            continue
        if encoding != ENCODINGS[0]:
            warnings.append(f"Leído con codificación {encoding}.")
        return text.lstrip("\ufeff"), warnings
    return None, warnings


def split_source_lines(text: str) -> list[str]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


# --------------------------------------------------------------------------- #
# Line classification
# --------------------------------------------------------------------------- #


def find_docstring_ranges(source: str) -> list[tuple[int, int]]:
    """Line ranges of string literals used as standalone statements."""
    tree = ast.parse(source)
    ranges = []
    for node in ast.walk(tree):
        is_string_statement = (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
        )
        if is_string_statement:
            ranges.append((node.lineno, node.end_lineno or node.lineno))
    return ranges


def find_multiline_string_lines(source: str) -> set[int]:
    """Lines covered by multi-line string tokens (after their first line)."""
    covered: set[int] = set()
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.STRING and token.end[0] > token.start[0]:
            covered.update(range(token.start[0] + 1, token.end[0] + 1))
    return covered


def find_docstring_ranges_fallback(lines: list[str]) -> list[tuple[int, int]]:
    """Regex-based scan for triple-quoted blocks when parsing fails."""
    ranges = []
    open_start: int | None = None
    quote = ""
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if open_start is None:
            match = re.match(r"^[rRuU]?(\"\"\"|''')", stripped)
            if not match:
                continue
            quote = match.group(1)
            if quote in stripped[match.end():]:
                ranges.append((line_number, line_number))
            else:
                open_start = line_number
        elif quote in line:
            ranges.append((open_start, line_number))
            open_start = None
    if open_start is not None:
        ranges.append((open_start, len(lines)))
    return ranges


def analyze_strings(source: str, lines: list[str]) -> tuple[list[tuple[int, int]], set[int], list[str]]:
    try:
        docstring_ranges = find_docstring_ranges(source)
        string_lines = find_multiline_string_lines(source)
        return docstring_ranges, string_lines, []
    except (SyntaxError, tokenize.TokenError, IndentationError) as error:
        warning = f"No se pudo analizar como Python ({error.__class__.__name__}); se usó el análisis línea a línea."
        return find_docstring_ranges_fallback(lines), set(), [warning]


def classify_comment_line(stripped: str) -> str:
    if SEPARATOR_PATTERN.match(stripped):
        return "separator"
    if HEADER_PATTERN.match(stripped):
        return "header"
    if BOILERPLATE_PATTERN.match(stripped):
        return "boilerplate"
    return "comment"


def classify_lines(lines: list[str], docstring_ranges, string_lines: set[int]) -> list[str | None]:
    """Return a 1-based list of line kinds (index 0 is unused)."""
    docstring_lines = {
        number for start, end in docstring_ranges for number in range(start, end + 1)
    }
    kinds: list[str | None] = [None]
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if line_number in docstring_lines:
            kinds.append("docstring")
        elif not stripped:
            kinds.append("blank")
        elif line_number in string_lines:
            kinds.append("code")
        elif stripped.startswith("#"):
            kinds.append(classify_comment_line(stripped))
        else:
            kinds.append("code")
    return kinds


# --------------------------------------------------------------------------- #
# Theory text helpers
# --------------------------------------------------------------------------- #


def strip_comment_marker(line: str) -> str:
    text = line.strip()[1:]
    return text[1:] if text.startswith(" ") else text


def build_docstring_text_map(lines: list[str], docstring_ranges) -> dict[int, str]:
    """Docstring line number -> text with the surrounding quotes removed."""
    text_by_line: dict[int, str] = {}
    for start, end in docstring_ranges:
        for line_number in range(start, end + 1):
            text = lines[line_number - 1].rstrip()
            if line_number == start:
                text = OPENING_QUOTE_PATTERN.sub("", text, count=1)
            if line_number == end:
                text = CLOSING_QUOTE_PATTERN.sub("", text, count=1)
            text_by_line[line_number] = text.strip() if line_number == start else text.rstrip()
    return text_by_line


def collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n")


def is_title_text(text: str) -> bool:
    text = text.strip()
    if not 3 <= len(text) <= TITLE_MAX_LENGTH:
        return False
    if any(character in text for character in "\t:_=") or text[-1] in ".,;":
        return False
    first_letter = text.lstrip("¿¡")[:1]
    if not (first_letter.isalpha() and first_letter.isupper()):
        return False
    return len(text.split()) >= 2


def previous_content_kind(kinds: list[str | None], line_number: int) -> str | None:
    for index in range(line_number - 1, 0, -1):
        if kinds[index] != "blank":
            return kinds[index]
    return None


def find_comment_title(lines, kinds, line_number: int) -> str | None:
    if kinds[line_number] != "comment":
        return None
    has_blank_before = line_number == 1 or kinds[line_number - 1] == "blank"
    if not has_blank_before:
        return None
    if previous_content_kind(kinds, line_number) not in TITLE_ALLOWED_PREVIOUS_KINDS:
        return None
    next_kind = kinds[line_number + 1] if line_number + 1 < len(kinds) else "blank"
    if next_kind not in {"blank", *THEORY_KINDS}:
        return None
    text = strip_comment_marker(lines[line_number - 1]).strip()
    return text if is_title_text(text) else None


def find_docstring_titles(docstring_ranges, docstring_text: dict[int, str]) -> dict[int, tuple[str, int]]:
    """Docstring start line -> (title, line consumed by the title)."""
    titles: dict[int, tuple[str, int]] = {}
    for start, end in docstring_ranges:
        content_lines = [
            number for number in range(start, end + 1) if docstring_text.get(number, "").strip()
        ]
        if len(content_lines) < 2:
            continue
        first_line = content_lines[0]
        candidate = docstring_text[first_line].strip()
        if is_title_text(candidate):
            titles[start] = (candidate, first_line)
    return titles


# --------------------------------------------------------------------------- #
# Exercise segmentation
# --------------------------------------------------------------------------- #


class ExerciseBuilder:
    """Walks classified lines and groups them into exercises and segments."""

    def __init__(self) -> None:
        self.exercises: list[Exercise] = []
        self.current = Exercise()
        self.segment: Segment | None = None

    def close_segment(self) -> None:
        if self.segment is not None:
            self.current.segments.append(self.segment)
            self.segment = None

    def start_exercise(self, title: str | None, line_number: int) -> None:
        self.close_segment()
        if self.current.segments:
            self.exercises.append(self.current)
            self.current = Exercise(title=title, title_line=line_number)
        elif self.current.title is None:
            self.current.title = title
            self.current.title_line = line_number
        elif title:
            self.add_line("theory", line_number, title)

    def add_blank(self, line_number: int) -> None:
        if self.segment is not None:
            self.segment.pending_blank_lines.append(line_number)

    def add_line(self, segment_type: str, line_number: int, text: str, is_boilerplate: bool = False) -> None:
        if self.segment is None or self.segment.type != segment_type:
            self.close_segment()
            self.segment = Segment(segment_type, line_number, line_number)
        else:
            self.flush_pending_blanks()
        self.segment.lines.append(text)
        self.segment.end_line = line_number
        if is_boilerplate:
            self.segment.boilerplate_lines.append(line_number)

    def flush_pending_blanks(self) -> None:
        if self.segment.type == "code":
            self.segment.lines.extend("" for _ in self.segment.pending_blank_lines)
        elif self.segment.pending_blank_lines:
            self.segment.lines.append("")
        self.segment.pending_blank_lines = []

    def finish(self) -> list[Exercise]:
        self.close_segment()
        if self.current.segments:
            self.exercises.append(self.current)
        return self.exercises


def segment_exercises(lines, kinds, docstring_ranges) -> list[Exercise]:
    docstring_text = build_docstring_text_map(lines, docstring_ranges)
    docstring_titles = find_docstring_titles(docstring_ranges, docstring_text)
    consumed_lines: set[int] = set()
    builder = ExerciseBuilder()

    for line_number, line in enumerate(lines, start=1):
        kind = kinds[line_number]

        if line_number in docstring_titles:
            title, consumed_line = docstring_titles[line_number]
            builder.start_exercise(title, consumed_line)
            consumed_lines.add(consumed_line)

        if line_number in consumed_lines:
            continue

        if kind == "separator":
            builder.start_exercise(None, line_number)
        elif kind == "header":
            builder.start_exercise(HEADER_PATTERN.match(line.strip()).group(1), line_number)
        elif kind == "blank":
            builder.add_blank(line_number)
        elif kind == "comment":
            title = find_comment_title(lines, kinds, line_number)
            if title:
                builder.start_exercise(title, line_number)
            else:
                builder.add_line("theory", line_number, strip_comment_marker(line))
        elif kind == "docstring":
            builder.add_line("theory", line_number, docstring_text.get(line_number, ""))
        else:
            builder.add_line("code", line_number, line.rstrip(), is_boilerplate=kind == "boilerplate")

    return builder.finish()


# --------------------------------------------------------------------------- #
# Concept detection
# --------------------------------------------------------------------------- #


def load_glossary() -> tuple[list[dict], list[dict]]:
    """Return (public entries, compiled matchers)."""
    if not GLOSSARY_PATH.exists():
        return [], []
    entries = json.loads(GLOSSARY_PATH.read_text(encoding="utf-8"))
    public_entries, matchers = [], []
    for entry in entries:
        public_entries.append(
            {key: entry[key] for key in ("id", "term", "category", "definition") if key in entry}
        )
        matchers.append(
            {
                "id": entry["id"],
                "code": [re.compile(pattern, re.MULTILINE) for pattern in entry.get("codePatterns", [])],
                "theory": [
                    re.compile(pattern, re.MULTILINE | re.IGNORECASE)
                    for pattern in entry.get("theoryPatterns", [])
                ],
            }
        )
    return public_entries, matchers


def strip_strings_and_comments(code: str) -> str:
    """Empty string literals (keeping quotes and prefixes) and drop comments."""
    without_strings = STRING_LITERAL_PATTERN.sub(lambda match: match.group(1) + match.group(2) * 2, code)
    return INLINE_COMMENT_PATTERN.sub("", without_strings)


def detect_concepts(exercise: Exercise, matchers: list[dict]) -> list[str]:
    code_text = strip_strings_and_comments(
        "\n".join("\n".join(s.lines) for s in exercise.segments if s.type == "code")
    )
    theory_text = "\n".join(
        [exercise.title or ""] + ["\n".join(s.lines) for s in exercise.segments if s.type == "theory"]
    )
    found = []
    for matcher in matchers:
        matches_code = any(pattern.search(code_text) for pattern in matcher["code"])
        matches_theory = any(pattern.search(theory_text) for pattern in matcher["theory"])
        if matches_code or matches_theory:
            found.append(matcher["id"])
    return found


# --------------------------------------------------------------------------- #
# Index assembly
# --------------------------------------------------------------------------- #


def humanize_name(name: str) -> str:
    spaced = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name).replace("_", " ").strip()
    return spaced[:1].upper() + spaced[1:]


def exercise_to_dict(index: int, exercise: Exercise, matchers: list[dict]) -> dict:
    first_line = exercise.title_line or exercise.segments[0].start_line
    return {
        "index": index,
        "title": exercise.title or f"Ejercicio {index}",
        "hasOwnTitle": exercise.title is not None,
        "startLine": min(first_line, exercise.segments[0].start_line),
        "endLine": exercise.segments[-1].end_line,
        "concepts": detect_concepts(exercise, matchers),
        "segments": [segment.to_dict() for segment in exercise.segments],
    }


def build_file_entry(path: Path, kind: str, matchers: list[dict], number: int | None = None) -> dict:
    stem = path.stem
    title_source = CHAPTER_PATTERN.match(path.name).group(2) if kind == "chapter" else stem
    entry = {
        "id": stem,
        "kind": kind,
        "number": number,
        "title": humanize_name(title_source),
        "path": path.relative_to(REPO_ROOT).as_posix(),
        "modifiedAt": datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat(timespec="seconds"),
        "lineCount": 0,
        "exerciseCount": 0,
        "warnings": [],
        "exercises": [],
    }
    text, warnings = read_text_file(path)
    entry["warnings"].extend(warnings)
    if text is None:
        entry["error"] = "No se pudo leer el fichero con ninguna codificación conocida."
        return entry

    lines = split_source_lines(text)
    docstring_ranges, string_lines, analysis_warnings = analyze_strings("\n".join(lines) + "\n", lines)
    entry["warnings"].extend(analysis_warnings)
    kinds = classify_lines(lines, docstring_ranges, string_lines)
    exercises = segment_exercises(lines, kinds, docstring_ranges)

    entry["lineCount"] = len(lines)
    entry["exercises"] = [
        exercise_to_dict(position, exercise, matchers) for position, exercise in enumerate(exercises, start=1)
    ]
    entry["exerciseCount"] = len(entry["exercises"])
    return entry


def find_course_dirs() -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.iterdir()
        if path.is_dir()
        and path.name not in IGNORED_DIRS
        and not path.name.startswith(".")
        and any(path.glob("*.py"))
    )


def build_course(course_dir: Path, matchers: list[dict]) -> dict:
    chapters, extras = [], []
    for path in sorted(course_dir.glob("*.py")):
        match = CHAPTER_PATTERN.match(path.name)
        if match:
            chapters.append(build_file_entry(path, "chapter", matchers, number=int(match.group(1))))
        else:
            extras.append(build_file_entry(path, "extra", matchers))
    chapters.sort(key=lambda chapter: chapter["number"])
    extras.sort(key=lambda extra: extra["id"].lower())
    return {
        "id": course_dir.name,
        "title": humanize_name(course_dir.name),
        "path": course_dir.relative_to(REPO_ROOT).as_posix(),
        "chapters": chapters,
        "extras": extras,
    }


def build_home() -> dict | None:
    home_path = REPO_ROOT / HOME_FILE_NAME
    if not home_path.exists():
        return None
    text, _ = read_text_file(home_path)
    return {"path": HOME_FILE_NAME, "markdown": text or ""}


def build_index() -> dict:
    glossary, matchers = load_glossary()
    return {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
        "home": build_home(),
        "glossary": glossary,
        "courses": [build_course(course_dir, matchers) for course_dir in find_course_dirs()],
    }


def print_summary(index: dict) -> None:
    files = [entry for course in index["courses"] for entry in course["chapters"] + course["extras"]]
    chapter_count = sum(len(course["chapters"]) for course in index["courses"])
    exercise_count = sum(entry["exerciseCount"] for entry in files)
    print(f"Índice generado en {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}")
    print(
        f"  Cursos: {len(index['courses'])} | Capítulos: {chapter_count} | "
        f"Extras: {len(files) - chapter_count} | Ejercicios: {exercise_count} | "
        f"Conceptos del glosario: {len(index['glossary'])}"
    )
    for entry in files:
        print(f"  - {entry['path']}: {entry['exerciseCount']} ejercicios")
        for warning in entry["warnings"]:
            print(f"      aviso: {warning}")
        if "error" in entry:
            print(f"      error: {entry['error']}")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    index = build_index()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print_summary(index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
