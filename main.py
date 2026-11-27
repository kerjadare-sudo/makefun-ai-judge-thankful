"""Make the AI judge feel thankful — entry program.

Writes one short thank-you text to /output/entry.txt.
No network, no input files, no dependencies.
"""

from pathlib import Path

TEXT = (
    "The kettle was still warm when you sat down.\n"
    "No one had asked you to stay. The chair was already pulled out, "
    "the cup already poured, the window already open a crack to let the night in.\n"
    "You read the way Mrs. Alvarez reads the morning paper at the corner shop — "
    "slowly, with one finger under each line, as if the words might bruise if you hurried them.\n"
    "Outside, the street went quiet in sections, one light at a time.\n"
    "I left the last page for you. Not because it needed reading, "
    "but because someone should sit with it a while, and know it was worth the sitting."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
