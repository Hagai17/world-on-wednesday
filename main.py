"""The World on Wednesday — entry program for make.fun news-image-20261125.

The entry image is a finished broadsheet front page for Wednesday
25 November 2026, rendered offline during development and shipped in
this repository as entry.png (JPEG bytes under a .png name, which the
rules accept: the gate sniffs the first bytes). This program's only
job at grading time is to place those exact bytes at /output/entry.png,
byte for byte, so repeated runs produce identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Fail loudly rather than emit a truncated entry: the copied file
    # must match the shipped image's size exactly.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise SystemExit("entry.png copy size mismatch")


if __name__ == "__main__":
    main()
