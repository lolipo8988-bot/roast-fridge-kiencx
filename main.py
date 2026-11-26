"""Roast the Smart Fridge entry.

Writes exactly one funny line (144 chars, one sentence) roasting a smart
fridge to /output/entry.txt. Deterministic: same bytes on every run.
No network, no secrets, no dependencies.
"""

import os

ENTRY = (
    "My smart fridge now charges a subscription to stay cold, so I pay "
    "monthly rent to a box that does the one job fridges did free in 1985."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
