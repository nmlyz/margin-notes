#!/usr/bin/env python3
"""Write one short, curious text to /output/entry.txt.

The text is fixed: the same words, byte for byte, on every run.
No network access, no dependencies beyond the standard library.
"""

import os
import sys

TEXT = """I opened the library book to find notes in the margins, in two hands. One asks the questions. The other answers them, in pencil, in my handwriting. I checked the card in the back. This book has never been borrowed before."""


def main() -> int:
    if not 1 <= len(TEXT) <= 280:
        print(f"error: text is {len(TEXT)} characters, must be 1-280",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("error: text must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
