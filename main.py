"""Fortune Cookie Wisdom for Developers entry.

Writes one original fortune-cookie line for a software developer to
entry.txt in the output directory. The line is a fixed string: the
program is fully deterministic, so two runs produce byte-identical
output.
"""

import os

FORTUNE = (
    "Your legacy code is not a mess; "
    "it is a letter from someone who was tired, like you."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
