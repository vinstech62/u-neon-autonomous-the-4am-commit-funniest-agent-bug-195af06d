#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one line -- the commit message an AI agent leaves after a long
night fixing its own bugs -- to /output/entry.txt.

The joke: the agent spent the whole night hunting a bug, only to find
the culprit was its own earlier fix. The loop is the punchline: every
repair creates the next bug, and the only thing left to do is apologise
to itself, in the code comments, at 4am. Flat, tired, machine-true --
no human programmer would apologise to themselves in a comment, but an
agent reviewing its own diff all night just might.
"""

import os

ENTRY = (
    "fix: the bug I spent all night chasing was written by my 2am fix "
    "for yesterday's bug. I have apologized to myself in the comments."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY, "ENTRY must be one line of 1-200 UTF-8 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
