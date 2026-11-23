#!/usr/bin/env python3
"""Write the margin-notes text to entry.txt.

The program holds one fixed sentence and writes it unchanged on
every run. It needs nothing but the standard library and never
touches the network.
"""

from pathlib import Path
import os
import sys

SENTENCE = (
    "My grandmother's music box plays a tune I have never heard "
    "anywhere else. Yesterday I hummed it in a shop, and the woman "
    "behind the counter finished it. She did not look surprised."
)


def text_is_valid(text):
    return 1 <= len(text) <= 280 and text.strip() != ""


def output_directory():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    try:
        folder.chmod(0o755)
    except OSError:
        pass
    return folder


def main():
    if not text_is_valid(SENTENCE):
        print("error: the text must be 1-280 characters and not blank",
              file=sys.stderr)
        return 1
    target = output_directory() / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != SENTENCE:
        print("error: the written text does not match", file=sys.stderr)
        return 1
    try:
        target.chmod(0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
