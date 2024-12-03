"""
Advent of Code 2024 Day 3

The input contains a string of instructions to parse.

Part 1
------
What is the sum of all the valid multiplication instructions?

Part 2
------
What is the sum of all the valid multiplication instructions
that are toggled on?
"""

import re


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2024 Day 3 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    total_1 = 0
    total_2 = 0
    do_multiply = True
    for line in puzzle:
        rmatches = re.finditer(r"mul\((?P<a>\d+),(?P<b>\d+)\)", line)
        for rmatch in rmatches:
            start = rmatch.start()
            check = list(re.finditer(r"(do|don't)\(\)", line[0:start]))
            if len(check) == 0:
                pass
            elif check[-1].group() == "do()":
                do_multiply = True
            else:
                do_multiply = False

            a = int(rmatch.group("a"))
            b = int(rmatch.group("b"))
            total_1 = total_1 + a * b
            if do_multiply:
                total_2 = total_2 + a * b

    if part == 1 or part is None:
        print(f"The total of all multiplications is {total_1}")
    if part == 2 or part is None:
        print(f"The total of all multiplications is {total_2}")
