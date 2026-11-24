"""The One-Line Cat Joke That Lands.

Writes a single original one-line cat joke to /output/entry.txt:
a cat's malicious compliance, delivered with eye contact.
"""

import os

JOKE = (
    "I banned my cat from my keyboard during work calls, "
    "so now he sits on it slower \u2014 while holding eye contact."
)


def validate(joke):
    """Check the joke against the competition gate before writing it."""
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if len(joke) > 200:
        raise ValueError("joke is %d characters, over the 200 limit" % len(joke))
    if "\n" in joke:
        raise ValueError("joke must be a single line")


def main():
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.replace(tmp_path, path)
    print(JOKE)


if __name__ == "__main__":
    main()
