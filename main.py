#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline - make.fun entry.

Writes the entry line to /output/entry.txt (UTF-8).

The deadline didn't slip — it moved. I have the timestamps to prove it.
"""
import os

ENTRY = "I didn't miss the deadline — it moved. I have timestamps to prove it. They're in a timezone I invented. For this exact situation."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
