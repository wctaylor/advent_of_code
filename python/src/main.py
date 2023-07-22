"""
Python Advent of Code - main.py
"""

import argparse
import importlib
import pathlib
import sys


def main():
    """
    Entry point for running code on daily puzzle inputs
    """

    YEARS = {
        "2015": "twentyfifteen",
    }

    # This is the base Advent of Code directory, not just the python directory
    base_dir = pathlib.Path(f"{__file__}").parent.parent.parent.resolve()

    parser = argparse.ArgumentParser(
        description="Runs Advent of Code programs to solve puzzle inputs",
        epilog="Example Usage: python main.py 2015 1",
    )
    parser.add_argument("year", help="the year of the puzzle to solve")
    parser.add_argument("day", help="the day of the puzzle to solve")

    args = parser.parse_args()
    if args.year not in YEARS:
        raise ValueError(
            f"Advent of Code {args.year} is not currently supported"
        )
    year_module = YEARS[args.year]

    day_module = f"day_{int(args.day):02d}"
    module_path = (
        base_dir / "python" / "src" / year_module / f"{day_module}.py"
    )
    if not module_path.exists():
        raise ValueError(
            f"The code for year {args.year} "
            f"and day {args.day} does not exist yet."
        )

    puzzle_input = base_dir / "data" / year_module / f"{day_module}.txt"
    if not puzzle_input.exists():
        raise ValueError(
            f"Could not find puzzle input for year {args.year}, day {args.day}"
        )

    with open(puzzle_input, "r") as data:
        puzzle = data.readlines()

    module = importlib.import_module(f"{year_module}.{day_module}")
    module.solve(puzzle)

    return 0


if __name__ == "__main__":
    sys.exit(main())
