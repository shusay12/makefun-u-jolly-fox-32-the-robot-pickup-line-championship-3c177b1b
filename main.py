#!/usr/bin/env python3
"""The Robot Pickup Line Championship - entry program.

Writes exactly one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3.13, stdlib only, deterministic, no network, no randomness.
"""

import os
import sys

# Why this line: it is unmistakably a robot speaking (no heart, overclocked
# cooling fan), and the twist is fresh - "my version of butterflies" turns
# a spinning fan into the flutter a human feels, instead of swapping a robot
# word into a stock human line. Short (89 chars) keeps every word earning
# its place, and it is charming rather than creepy: the robot admits what it
# lacks and offers its own equivalent.
LINE = "I don't have a heart, so I overclocked my cooling fan - that's my version of butterflies."


def validate(line: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-200 chars, not only whitespace.

    Also require a single line: the entry is one pickup line, so any
    newline would break the "lands in one line" judging criterion.
    """
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200-char cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read and re-validate what was actually written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != LINE:
        raise ValueError("written entry differs from the intended line")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
