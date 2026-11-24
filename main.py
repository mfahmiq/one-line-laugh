"""Write one funny line to /output/entry.txt.

The line is a single sentence of at most 200 characters: I ask a smart
speaker for something relaxing, and the twist is that it reads my calendar
out loud — the calendar being the least relaxing thing in the house. The
surprise lands at the end and still makes sense, it names an everyday
truth (a packed calendar is stressful), and every word earns its place.
"""

import os

LINE = "I asked my smart speaker to play something relaxing, so it read my calendar out loud."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
# The line is 85 characters, one sentence, no trailing newline in the line.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
