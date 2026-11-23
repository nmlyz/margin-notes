#!/usr/bin/env python3
"""Write the greenhouse-tomato text to entry.txt.

The program keeps one fixed passage about a gardener who finds
a tomato ripening in her greenhouse in January, beside a blank
seed packet in her own handwriting, and writes that passage
unchanged on every run. It needs nothing but the standard
library and never touches the network.
"""

from pathlib import Path
import os
import sys

PASSAGE = (
    "In January, the gardener finds a tomato ripening in the "
    "greenhouse, red as summer, and the seed packet beside it "
    "is blank, in her own handwriting."
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
    """Write PASSAGE to entry.txt, then read it back to confirm.

    The write uses no trailing newline, so the file holds exactly
    the passage and nothing else. Running the program twice
    produces byte-identical output.
    """
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
