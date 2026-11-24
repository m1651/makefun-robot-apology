#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line 1: a robot apologizing in a single sentence for one specific mistake.
Line 2: one sentence saying what the robot learned and what it will do
differently. Stdlib only, no network.
"""

import os

ENTRY = (
    "I am sorry I woke the baby at 3 a.m. by announcing, at full volume, "
    "that the dishwasher cycle was complete.\n"
    "I have learned that a finished cycle is not an emergency, so from now "
    "on I will whisper status updates after bedtime and save the fanfare "
    "for the morning."
)


def main() -> None:
    lines = ENTRY.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly two lines, got {len(lines)}")
    for line in lines:
        if not line.endswith("."):
            raise SystemExit("each line must be a single sentence ending with '.'")
    if not 1 <= len(ENTRY) <= 400:
        raise SystemExit(f"entry is {len(ENTRY)} chars; must be 1-400")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
