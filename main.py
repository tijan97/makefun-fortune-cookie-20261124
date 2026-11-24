"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: a quiet truth about a developer's day — when you run `git blame`
on a line that embarrasses you, the author it names is always a younger
version of yourself, and they were doing their honest best at the time.
"""

import os

FORTUNE = (
    "The person git blame points to is always a younger you, "
    "and they meant well."
)


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-120 chars, one line."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only white space")
    if len(stripped) > 120:
        raise ValueError(f"entry is {len(stripped)} chars, cap is 120")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    # Read it back and re-validate what actually landed on disk.
    with open(path, encoding="utf-8") as f:
        validate(f.read())
    print(f"wrote {path}: {FORTUNE!r} ({len(FORTUNE)} chars)")


if __name__ == "__main__":
    main()
