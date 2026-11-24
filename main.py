#!/usr/bin/env python3
"""Write one fortune-cookie wisdom line for developers to /output/entry.txt.

Python 3.13 standard library only; no network, no randomness,
fully deterministic.

v1 line: an estimate framed as a loan from the future, with the
future as the collector. It is true about a developer's day
(estimates always slip and cost more later), it reads like a
fortune cookie (one balanced sentence, one breath), and the
turn is fresh: "interest" is both the price of time and the
debt the future collects.

Revision (v2): re-grounded the line in the developer's own day
("The estimate you give today") and made the creditor concrete:
"tomorrow" instead of the abstract "the future". A named
tomorrow that collects is a sharper image than a vague future
that does, and "collects with interest" drops the clunky
"its interest" for a cleaner landing.

Revision (v3, final): kept v2's concrete "tomorrow" but restored
v1's universal opening ("Every estimate") — a fortune cookie
speaks in universals, not in one person's today — and restored
"always", because the inevitability is the point: tomorrow does
not sometimes collect, it always does. Final line is 83 chars,
one balanced sentence, one breath.
"""

from pathlib import Path

TEXT = (
    "Every estimate is a loan from tomorrow, "
    "and tomorrow always collects with interest."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
