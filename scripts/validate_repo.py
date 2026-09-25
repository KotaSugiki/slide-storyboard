#!/usr/bin/env python3
"""Run dependency-free repository checks; optionally smoke-test skills CLI install."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "SKILL.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "assets/template.html",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
)
STATUS_FILES = ("README.md", "SKILL.md", "assets/template.html")
OLD_MARKERS = (chr(0x3016) + chr(0x4eee) + chr(0x6848) + chr(0x3017), chr(0x3016) + chr(0x8981) + chr(0x78ba) + chr(0x8a8d) + chr(0x3017))
NEW_MARKERS = (chr(0x3010) + chr(0x4eee) + chr(0x6848) + chr(0x3011), chr(0x3010) + chr(0x8981) + chr(0x78ba) + chr(0x8a8d) + chr(0x3011))
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


class TemplateParser(HTMLParser):
    """Capture inline scripts and catch malformed tag nesting in HTML source."""

    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.scripts: list[str] = []
        self._script_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "script":
            self._script_depth += 1
        if tag not in self.VOID_TAGS:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        return

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_depth:
            self._script_depth -= 1
        if tag in self.VOID_TAGS:
            self.errors.append(f"void tag has an end tag: </{tag}>")
            return
        if not self.stack:
            self.errors.append(f"unexpected closing tag: </{tag}>")
            return
        opening = self.stack.pop()
        if opening != tag:
            self.errors.append(f"tag mismatch: <{opening}> closed by </{tag}>")

    def handle_data(self, data: str) -> None:
        if self._script_depth:
            self.scripts.append(data)


def check_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"required file is missing: {relative}")


def check_markers(errors: list[str]) -> None:
    for relative in STATUS_FILES:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for old in OLD_MARKERS:
            if old in text:
                errors.append(f"legacy status marker {old} remains in {relative}")
        for marker in NEW_MARKERS:
            if marker not in text:
                errors.append(f"required status marker {marker} is missing from {relative}")


def check_local_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        source = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(source):
            target = match.group(1).split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local_target = target.split("#", 1)[0].split("?", 1)[0]
            if local_target and not (path.parent / local_target).resolve().is_file():
                errors.append(f"broken local Markdown link in {path.relative_to(ROOT)}: {target}")


def check_html(errors: list[str]) -> None:
    path = ROOT / "assets/template.html"
    if not path.exists():
        return
    source = path.read_text(encoding="utf-8")
    parser = TemplateParser()
    parser.feed(source)
    parser.close()
    errors.extend(f"HTML template: {error}" for error in parser.errors)
    errors.extend(f"HTML template: unclosed tag <{tag}>" for tag in parser.stack)
    for script in parser.scripts:
        if not script.strip():
            continue
        node = shutil.which("node")
        if not node:
            print("SKIP: node not found; embedded JavaScript syntax check requires Node.js")
            break
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as temp_file:
            temp_file.write(script)
            temp_path = Path(temp_file.name)
        try:
            result = subprocess.run([node, "--check", str(temp_path)], capture_output=True, text=True, check=False)
            if result.returncode:
                errors.append(f"embedded JavaScript syntax error: {result.stderr.strip()}")
        finally:
            temp_path.unlink(missing_ok=True)


def check_secrets(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or any(part in {"node_modules", ".venv"} for part in path.parts):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(f"possible credential or private key in {path.relative_to(ROOT)}")
                break


def check_skill_install(errors: list[str]) -> None:
    npx = shutil.which("npx")
    if not npx:
        errors.append("--skill-smoke requires Node.js and npm (npx was not found)")
        return
    with tempfile.TemporaryDirectory(prefix="slide-storyboard-skill-smoke-") as temp:
        temp_root = Path(temp)
        temp_source = temp_root / "source"
        shutil.copytree(ROOT / "assets", temp_source / "assets")
        shutil.copy2(ROOT / "SKILL.md", temp_source / "SKILL.md")
        env = os.environ.copy()
        env.update({
            "HOME": str(temp_root),
            "XDG_CONFIG_HOME": str(temp_root / "config"),
            "NPM_CONFIG_CACHE": str(temp_root / "npm-cache"),
            "CI": "1",
        })
        commands = (
            ([npx, "--yes", "skills", "add", ".", "--list"], "skill recognition"),
            ([npx, "--yes", "skills", "add", ".", "--skill", "slide-storyboard", "--agent", "codex", "--copy", "--yes"], "Codex copy install"),
        )
        for command, label in commands:
            try:
                result = subprocess.run(command, cwd=temp_source, env=env, capture_output=True, text=True, check=False, timeout=180)
            except subprocess.TimeoutExpired:
                errors.append(f"{label} timed out after 180 seconds")
                return
            if result.returncode:
                errors.append(f"{label} failed: {(result.stderr or result.stdout).strip()}")
                return
            print(f"PASS: {label}")
        installed = list(temp_root.rglob("SKILL.md"))
        if not any(path.parent.name == "slide-storyboard" for path in installed):
            errors.append("Codex copy install did not create a slide-storyboard/SKILL.md under the temporary home")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-smoke", action="store_true", help="run npx skills recognition and temporary Codex copy-install checks")
    args = parser.parse_args()

    errors: list[str] = []
    check_files(errors)
    check_markers(errors)
    check_local_markdown_links(errors)
    check_html(errors)
    check_secrets(errors)
    if args.skill_smoke:
        check_skill_install(errors)

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
