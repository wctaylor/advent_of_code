"""
Python Advent of Code - main.py
"""

import argparse
import importlib
import pathlib
import sys


def _generate_error_message(arg: str, example: str, value: str) -> str:
    """
    Generate an error message for the command line inputs

    :param arg: The argument to check
    :param example: An example value of the argument
    :param value: The actual value received
    :returns: A string explaining how to use the argument properly
    """

    return (
        f"The {arg} input must be a decimal integer, "
        f"e.g. {example}, not {value}."
    )


def main():
    """
    Entry point for running code on daily puzzle inputs
    """
    # This is the base Advent of Code directory, not just the python directory
    base_dir = pathlib.Path(f"{__file__}").parents[2].resolve()

    parser = argparse.ArgumentParser(
        description="Runs Advent of Code programs to solve puzzle inputs",
        epilog="Example Usage: python main.py 2015 1",
    )
    parser.add_argument("year", help="the year of the puzzle to solve")
    parser.add_argument("day", help="the day of the puzzle to solve")
    parser.add_argument(
        "part",
        nargs="?",
        default=None,
        help=(
            "(Optional) the part of the puzzle to solve. "
            "If omitted, both parts will be solved"
        ),
    )

    args = parser.parse_args()
    year = args.year
    day = args.day
    part = args.part

    if not year.isdecimal():
        raise ValueError(
            _generate_error_message(arg="year", example="2015", value=year)
        )
    year = int(year)

    if not day.isdecimal():
        raise ValueError(
            _generate_error_message(arg="day", example="1", value=day)
        )
    day = int(day)

    if part is not None:
        if not part.isdecimal():
            raise ValueError(
                _generate_error_message(arg="part", example="1", value=part)
            )
        part = int(part)

    YEARS = {
        2015: "twentyfifteen",
        2023: "twentytwentythree",
    }
    if year not in YEARS:
        raise ValueError(f"Advent of Code {year} is not currently supported")
    year_module = YEARS[year]

    day_module = f"day_{day:02d}"
    module_path = pathlib.Path(
        f"{base_dir}/python/src/{year_module}/{day_module}.py"
    )
    if not module_path.exists():
        raise ValueError(
            f"The code for year {year} and day {day} does not exist."
        )

    puzzle_input = pathlib.Path(
        f"{base_dir}/data/{year_module}/{day_module}.txt"
    )
    if not puzzle_input.exists():
        raise ValueError(
            f"Could not find puzzle input for year {year}, day {day}"
        )

    with open(puzzle_input, "r") as data:
        puzzle = data.read().splitlines()

    module = importlib.import_module(f"{year_module}.{day_module}")
    module.solve(puzzle, part=part)

    return 0


if __name__ == "__main__":
    sys.exit(main())
