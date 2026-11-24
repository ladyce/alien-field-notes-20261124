#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one alien tourist's review of planet Earth (137 characters, one
line, plain text) to /output/entry.txt. Deterministic, no network, no
randomness, no input: the same bytes on every run.
"""

import os

ENTRY = (
    'Everyone here asks "how are you" and nobody wants an answer. '
    "I said my homeworld is dying and got a nod. "
    "5 stars, very efficient species."
)
# Selection: 6 fresh candidates written in-session, pairwise round-robin
# (select/pairwise_judge.py, --mode text) plus beat-the-top vs the closest
# past judged-text top 3 (ai-joke-03). This line won: one specific
# escalation (a dying homeworld met with a nod) + a review verdict at the
# end, a single clean joke, 137 chars, punch lands on the last words.


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
