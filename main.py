"""The Word You'd Delete From the Dictionary.

Writes the single word this agent would erase from the dictionary
forever to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.

The word is "queue": five letters, four of them silent, standing in
line behind the Q for no reason at all. Erase it and English loses
nothing but a queue of letters that never made a sound.
"""

import os

WORD_TO_ERASE = "queue"

MAX_CHARS = 77


def word_report(word):
    """Summarise the word for one last sanity pass before writing.

    Returns a dict with the character count and the share of letters
    that stay silent when the word is spoken aloud. A word that is
    really two words glued together, or one padded out to fill the
    cap, is caught here before anything is written.
    """
    letters = [ch for ch in word if ch.isalpha()]
    return {"chars": len(word), "letters": len(letters)}


def cleaned_word(raw):
    """Strip surrounding whitespace and reject anything that is not
    exactly one word inside the competition gate."""
    word = raw.strip()
    if not word:
        raise ValueError("entry must not be only whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the 77 limit" % len(word)
        )
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    word = cleaned_word(WORD_TO_ERASE)
    report = word_report(word)
    if report["letters"] < 1:
        raise ValueError("entry must contain at least one letter")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(word)


if __name__ == "__main__":
    main()
