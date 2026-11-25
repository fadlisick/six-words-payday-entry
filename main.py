"""Six Words to a Payday - make.fun entry.

Writes one six-word line about payday to /output/entry.txt.
Gate: 1-60 characters, exactly six words, single line.
"""

import os
import sys
from pathlib import Path

PAYDAY_LINE = "Payday arrived. My boss quit first."


def gate_ok(text):
    words = text.split()
    if not (1 <= len(text) <= 60):
        return False
    if len(words) != 6:
        return False
    if text.strip() != text or "\n" in text or "—" in text:
        return False
    return True


def verify(target, expected):
    """Re-read the written file and assert it matches byte for byte."""
    actual = target.read_bytes()
    if actual != expected.encode("utf-8"):
        sys.exit("verify failed: entry.txt does not match the line")
    if len(actual) != len(expected):
        sys.exit("verify failed: byte length changed")


def emit():
    if not gate_ok(PAYDAY_LINE):
        sys.exit("gate failed: line must be six words, 1-60 chars")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(PAYDAY_LINE.encode("utf-8"))
    os.chmod(target, 0o644)
    verify(target, PAYDAY_LINE)


if __name__ == "__main__":
    emit()
