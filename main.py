#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry 216.

Writes a single sentence (at most 200 characters) about the best meal
the entrant ever had to /output/entry.txt. Pure standard library,
fully deterministic: the same sentence every run.
"""

import os

ENTRY = (
    "The best meal I ever had was charcoal nasi goreng from a night stall "
    "in Yogyakarta, eaten on a plastic stool in the rain while the vendor "
    "tossed the wok one-handed and laughed."
)


def main() -> None:
    sentence = ENTRY.strip()
    assert 1 <= len(sentence) <= 200, f"entry is {len(sentence)} chars"
    assert sentence.count(".") == 1, "entry must be a single sentence"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    print(f"wrote {len(sentence)} chars to {out_path}")


if __name__ == "__main__":
    main()
