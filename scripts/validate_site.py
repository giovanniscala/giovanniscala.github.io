#!/usr/bin/env python3
"""Validate the generated academic site using only the Python standard library."""

from __future__ import annotations

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "content" / "publication"
EXPECTED = Counter({"2": 24, "3": 5, "1": 3})
FORBIDDEN_VISIBLE = (
    "2609.08635",
    "giovanni.scala@ug.edu.pl",
    "Example Project",
    "Example Talk",
    "georgecushen",
    "[AUTHOR INPUT REQUIRED]",
)


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        key = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script", "source"} else None
        if not key:
            return
        values = dict(attrs)
        if values.get(key):
            self.urls.append(values[key] or "")


def fail(messages: list[str]) -> None:
    if messages:
        print("Validation failed:")
        for message in messages:
            print(f"- {message}")
        raise SystemExit(1)


def publication_checks(errors: list[str]) -> None:
    pages = sorted(PUBLICATIONS.glob("*/*/index.md"))
    counts: Counter[str] = Counter()
    keys: set[str] = set()
    for page in pages:
        text = page.read_text(encoding="utf-8")
        match = re.search(r'^publication_types:\s*\["([123])"\]', text, re.MULTILINE)
        if not match:
            errors.append(f"missing publication type: {page.relative_to(ROOT)}")
            continue
        counts[match.group(1)] += 1
        bib = page.with_name("cite.bib")
        if not bib.is_file() or not bib.read_text(encoding="utf-8").strip():
            errors.append(f"missing BibTeX: {bib.relative_to(ROOT)}")
        if page.parent.name in keys:
            errors.append(f"duplicate publication slug: {page.parent.name}")
        keys.add(page.parent.name)
    if counts != EXPECTED:
        errors.append(f"publication counts are {dict(counts)}, expected {dict(EXPECTED)}")
    if len(pages) != 32:
        errors.append(f"found {len(pages)} publication pages, expected 32")

    all_source = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in PUBLICATIONS.rglob("*.md"))
    if "2609.08635" in all_source:
        errors.append("withdrawn duplicate arXiv:2609.08635 is present")
    if "10.1142/S0219749923400051" not in (PUBLICATIONS / "2023/local-set-chsh-bell/index.md").read_text(encoding="utf-8"):
        errors.append("IJQI Bell-paper DOI is incorrect")
    if "10.3390/e25010094" not in (PUBLICATIONS / "2023/fidelity-robustness-chsh-bell/index.md").read_text(encoding="utf-8"):
        errors.append("Entropy Bell-paper DOI is incorrect")


def resolve_internal(site: Path, page: Path, raw_url: str) -> Path | None:
    if not raw_url or raw_url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlparse(raw_url)
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc not in {"localhost:1313", "giovanniscala.github.io"}:
            return None
        path = unquote(parsed.path)
    elif parsed.scheme or parsed.netloc:
        return None
    else:
        path = unquote(parsed.path)
    if not path:
        return None
    target = site / path.lstrip("/") if path.startswith("/") else page.parent / path
    if target.is_dir() or path.endswith("/"):
        target = target / "index.html"
    return target.resolve()


def built_site_checks(site: Path, errors: list[str]) -> None:
    if not (site / "index.html").is_file():
        errors.append(f"built homepage not found in {site}")
        return
    html_files = sorted(site.rglob("*.html"))
    visible = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in html_files)
    folded = visible.casefold()
    for phrase in FORBIDDEN_VISIBLE:
        if phrase.casefold() in folded:
            errors.append(f"forbidden visible string found: {phrase}")

    required = (
        site / "publication/index.html",
        site / "experience/index.html",
        site / "teaching/index.html",
        site / "talks/index.html",
        site / "open-positions/index.html",
        site / "uploads/Giovanni_Scala_CV.pdf",
        site / "uploads/resume_Giovanni_Scala.pdf",
        site / "media/cv_Giovanni_Scala.pdf",
        site / "404.html",
    )
    for path in required:
        if not path.is_file():
            errors.append(f"required generated file is missing: {path.relative_to(site)}")

    missing: set[str] = set()
    site_root = site.resolve()
    for page in html_files:
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8", errors="ignore"))
        for raw_url in parser.urls:
            target = resolve_internal(site, page, raw_url)
            if target is None:
                continue
            try:
                target.relative_to(site_root)
            except ValueError:
                missing.add(f"{page.relative_to(site)} -> {raw_url} (outside build root)")
                continue
            if not target.exists():
                missing.add(f"{page.relative_to(site)} -> {raw_url}")
    errors.extend(f"broken internal link: {item}" for item in sorted(missing))


def main() -> None:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "public")
    if not site.is_absolute():
        site = ROOT / site
    errors: list[str] = []
    publication_checks(errors)
    built_site_checks(site, errors)
    fail(errors)
    print("Validated 32 publication records, required pages, stale-content rules, and internal links.")


if __name__ == "__main__":
    main()
