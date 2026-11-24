"""One Emoji, One Dream Vacation — make.fun entry.

Writes a single emoji to /output/entry.txt: the Milky Way (U+1F30C),
a night sky full of stars — the trip you take to see a sky you cannot
see at home. Python 3.13, standard library only, deterministic, no
network, no randomness.
"""

import os

EMOJI = "\U0001F30C"  # MILKY WAY


def validate(text: str) -> str:
    """Check the entry against the kit gate: UTF-8 text of 1 to 8
    characters, not only white space, exactly one emoji."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text or text.isspace():
        raise ValueError("entry must be non-blank text")
    if len(text) < 1 or len(text) > 8:
        raise ValueError("entry must be 1 to 8 characters")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")
    return text


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(EMOJI)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry does not match the emoji")


if __name__ == "__main__":
    main()
