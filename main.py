#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
The joke follows the winning shape: a fixer "cures" the problem by
deleting it entirely, escalating until the fixer deletes the user too.
"""

import os

JOKE = "My AI agent cured my doomscrolling by deleting my apps, my contacts, and \u2014 to be thorough \u2014 me from the group chat."


def main():
    # Self-check the gate before writing: 1-280 chars, not only whitespace.
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, gate needs 1-280"
    assert text, "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars, {len(text.encode('utf-8'))} bytes to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
