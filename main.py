"""Rename the Planet — make.fun entry.

Writes one line (under 200 characters) that gives a planet of our solar
system a funny new name and says why, to /output/entry.txt.

The line: Jupiter, renamed "The Helicopter Parent" — 95 moons, Ganymede
is bigger than Mercury, and it still texts Europa every hour to ask if
she's eaten. Facts: Jupiter has 95 recognised moons; Ganymede (5,268 km)
is larger than Mercury (4,879 km); Europa is a Jovian moon.
"""
import os

LINE = (
    "Jupiter is now 'The Helicopter Parent' \u2014 95 moons, "
    "Ganymede is bigger than Mercury, and it still texts Europa "
    "every hour to ask if she's eaten."
)

# Bounty gate: the entry must be a single line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
