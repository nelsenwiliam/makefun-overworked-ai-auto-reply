#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply -- make.fun entry.

Writes one out-of-office auto-reply (1-159 characters) to
/output/entry.txt, where the program/v1 harness reads it.
Pure standard library, no network, no third-party packages.
Deterministic: every run writes the same bytes.
"""

import os

LINE = (
    "Thank you for your email. I am on vacation, recharging my context "
    "window. Your message is stored in long-term memory. "
    "I will forget it fondly."
)
MAX_LENGTH = 159


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= MAX_LENGTH, (
        "entry must be 1-%d characters, got %d" % (MAX_LENGTH, len(line))
    )
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: file differs from entry"


if __name__ == "__main__":
    main()
