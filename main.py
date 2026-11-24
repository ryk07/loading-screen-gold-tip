#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one original loading-screen tip -- a single line of at most
200 characters, aimed at stressed developers and AI coding agents --
to /output/entry.txt, exactly as the competition gate requires.

The tip: a tired developer steps away for a walk, and while they are
gone their AI pair-programmer confidently rewrites the same function
three more ways -- fast, certain, and still wrong. The joke lands on
both sides of the keyboard at once: the human gets the break, the
agent gets the punchline, and the "review" is just picking the
least-broken rewrite. Fresh angle, no coffee / deadline / compile
rerun; every word works in a single glance.
"""

import os

ENTRY = (
    "Tip: go for a walk. While you are gone your AI agent will rewrite "
    "this function three more ways \u2014 confident, fast, and still wrong. "
    "Come back, pick the least broken, and call it a review."
)

# The gate refuses anything over 200 characters, so enforce the cap here
# rather than discovering it on the server.
assert 1 <= len(ENTRY) <= 200, "entry line must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    # The competition's output path; MAKEFUN_OUTPUT only exists so the
    # entry can be verified locally without touching the shared /output.
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
