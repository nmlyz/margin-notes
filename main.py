#!/usr/bin/env python3
"""Write the train-window text to entry.txt.

The program holds one fixed passage and writes it unchanged on
every run. It needs nothing but the standard library and never
touches the network.
"""

from pathlib import Path
import os
import sys

PASSAGE = (
    "She presses her forehead to the train window at 2 a.m., "
    "her reflection sliding over dark fields, until a farmhouse "
    "light comes on where she is sure no house stands."
)


def passage_is_valid(passage):
    return 1 <= len(passage) <= 280 and passage.strip() != ""


def destination_folder():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    try:
        folder.chmod(0o755)
    except OSError:
        pass
    return folder


def write_entry():
    if not passage_is_valid(PASSAGE):
        print("error: the text must be 1-280 characters and not blank",
              file=sys.stderr)
        return 1
    target = destination_folder() / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(PASSAGE)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != PASSAGE:
        print("error: the written text does not match", file=sys.stderr)
        return 1
    try:
        target.chmod(0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry())
