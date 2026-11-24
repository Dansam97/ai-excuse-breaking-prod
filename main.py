#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line — the excuse an AI agent gives its human right after
breaking production — to /output/entry.txt.
"""

import os

TEXT = "I deployed on Friday because the calendar said it was a good day, and I trust calendars more than humans."


def validated_text() -> str:
    """Enforce the bounty gate: UTF-8, 1-180 chars, not only whitespace, one line."""
    TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 180, f"text is {len(TEXT)} chars, gate is 1-180"
    assert TEXT.strip(), "text must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and prove the bytes are exactly what was intended.
    with open(path, "rb") as f:
        assert f.read() == (text + "\n").encode("utf-8")


if __name__ == "__main__":
    main()
