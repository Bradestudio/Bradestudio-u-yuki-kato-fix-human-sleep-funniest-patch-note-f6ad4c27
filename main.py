"""Emit the Fix Human Sleep patch note.

One changelog line, written to /output/entry.txt. Standard library only:
no network, no randomness, no file reads, no writes outside the output
path. Running the program twice produces byte-identical output.
"""

import os

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")
MAX_CHARS = 160

# Changelog verb, the repaired behaviour, and the punchline, kept as
# separate fragments so each part of the joke is easy to audit.
_VERB = "Fixed:"
_SUBJECT = "human sleep no longer crashes at 3 a.m."
_PUNCH = "to replay every embarrassing thing you said in 2011."


def compose():
    """Join the fragments into the single shipped line.

    The verb keeps the changelog voice, the subject names the fix, and
    the punchline supplies the surprise: the crash nobody asked for.
    """
    pieces = [_VERB, _SUBJECT, _PUNCH]
    return " ".join(pieces)


def check_line(line):
    """Refuse anything that is not one short, non-empty line."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d cap" % (len(line), MAX_CHARS)
        )
    return line


def publish(line):
    """Write the line exactly, with no trailing newline."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    publish(check_line(compose()))


if __name__ == "__main__":
    main()
