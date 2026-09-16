#!/usr/bin/env python
"""Check Amazon listing copy for field length and policy-triggering phrases.

Input is a text or Markdown file with one field per line, e.g.

    Title: Nordic Ware Cast Iron Skillet, 10 Inch, Pre-Seasoned
    Bullet 1: Even heat, no hot spots ...
    Description: ...
    Search Terms: cast iron pan skillet fry pan

Chinese labels (标题 / 五点1 / 描述 / 后台搜索词) work too. Unlabeled lines are
scanned for violations but not length-checked.

Lengths use UTF-16 code units, which is how Amazon counts. Emoji cost 2.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Common upper bounds. Site and category rules vary -- confirm in Seller Central.
LIMITS = {
    "title": ("chars", 200),
    "bullet": ("chars", 250),
    "description": ("chars", 2000),
    "a+": ("chars", 1000),
    "search terms": ("bytes", 250),
}

FIELD_RE = re.compile(
    r"^\s*(?:[-*+]\s*)?(?:#{1,6}\s*)?\**"
    r"(?P<field>"
    r"title|bullets?|bullet\s*\d*|description|a\+|search\s*terms?"
    r"|标题|五点\s*\d*|描述|后台搜索词"
    r")\**\s*[:：]\s*(?P<value>.+?)\s*$",
    re.IGNORECASE,
)

CAPS_LABEL = "all-caps word"

VIOLATIONS = [
    (r"\bfree\s+(shipping|ship|delivery)\b", "promotion/shipping"),
    (r"\b(on\s+sale|discount|coupon|% ?off|buy\s+one\s+get|bogo|clearance)\b", "promotion"),
    (r"\b(best\s*seller|number\s+one|top\s+rated|top-rated|world'?s\s+best)\b|#\s*1\b", "ranking/absolute"),
    (r"\bguarantee[ds]?\b|\b1 ?00 ?%", "absolute claim"),
    (r"\b(cures?|treats?|treatment|heals?|diagnose[sd]?|fda[- ]approved)\b", "medical/curative"),
    (r"\b(non-?toxic|100 ?% ?safe|child\s*safe|hypoallergenic)\b", "safety claim"),
    (r"\b(eco-?friendly|biodegradable|carbon\s+neutral)\b", "environmental claim"),
    (r"\b(?:www\.|https?://|\.com\b|\.net\b|@[a-z0-9.-]+\.)", "link/contact"),
    (r"[\U0001F000-\U0001FAFF\u2600-\u27BF]", "emoji/symbol"),
    (r"\b[A-Z]{3,}\b", CAPS_LABEL),
]

ALL_CAPS_OK = {
    "LED", "USB", "LCD", "OLED", "PVC", "ABS", "TPU", "SPF", "UV", "PU",
    "XXL", "XXXL", "XL", "XS", "USA", "UK", "EU", "BPA", "BBQ", "RV",
    "PSI", "GB", "TB", "MAH", "KG", "LB", "OZ", "ML", "CM", "IPX", "GPS",
    "DVD", "TV", "PC", "AC", "DC", "FT", "HR", "MIN", "PRO", "SET",
}


def utf16_len(text: str) -> int:
    return len(text.encode("utf-16-le")) // 2


def field_key(raw: str) -> str:
    name = re.sub(r"\s*\d*\s*$", "", raw.strip().lower())
    if name.startswith(("bullet", "五点")):
        return "bullet"
    if name in ("a+",):
        return "a+"
    if "search" in name or "搜索" in name:
        return "search terms"
    if name in ("title", "标题"):
        return "title"
    if name in ("description", "描述"):
        return "description"
    return "other"


def strip_markup(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    return text.replace("`", "").strip()


def scan(text: str) -> list[str]:
    hits = []
    for pattern, label in VIOLATIONS:
        found: list[str] = []
        for match in re.finditer(pattern, text, re.IGNORECASE):
            word = match.group(0).strip()
            if label == CAPS_LABEL:
                if not word.isupper() or word.replace("-", "") in ALL_CAPS_OK:
                    continue
            if word not in found:
                found.append(word)
        if found:
            hits.append(f"{label}: {', '.join(repr(w) for w in found)}")
    return hits


def setup_stdout() -> None:
    """Avoid UnicodeEncodeError for emoji on legacy console code pages."""
    try:
        if sys.stdout.isatty():
            sys.stdout.reconfigure(errors="replace")
        else:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


def main(argv: list[str]) -> int:
    setup_stdout()

    if len(argv) != 2:
        print(__doc__)
        return 2

    path = Path(argv[1])
    if not path.is_file():
        print(f"File not found: {path}")
        return 2

    fields: list[tuple[str, str, int]] = []
    loose: list[tuple[int, str]] = []

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith(("```", "---", "|")):
            continue
        match = FIELD_RE.match(line)
        if match:
            fields.append((field_key(match.group("field")), strip_markup(match.group("value")), lineno))
        else:
            loose.append((lineno, line))

    problems = 0

    if not fields:
        print("No 'field: value' lines recognised; scanning for policy words only.")
        for lineno, line in loose:
            for hit in scan(line):
                print(f"  line {lineno}  {hit}")
                problems += 1
        return 1 if problems else 0

    print(f"{'field':<14}{'length':>6}{'limit':>6}  status")
    for key, value, lineno in fields:
        unit, limit = LIMITS.get(key, ("chars", None))
        size = len(value.encode("utf-8")) if unit == "bytes" else utf16_len(value)
        if limit is None:
            status = "no reference limit"
        elif size > limit:
            status = f"over by {size - limit}"
            problems += 1
        elif size > limit * 0.95:
            status = "near limit"
        else:
            status = "OK"
        print(f"{key:<14}{size:>6}{limit if limit else '-':>6}  {status}  (line {lineno})")

    print("\nPolicy word scan (confirm every hit against your category rules):")
    found = False
    for key, value, lineno in fields:
        for hit in scan(value):
            print(f"  {key} line {lineno}  {hit}")
            found = True
            problems += 1
    for lineno, line in loose:
        for hit in scan(line):
            print(f"  unlabeled line {lineno}  {hit}")
            found = True
            problems += 1
    if not found:
        print("  none")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
