"""
Advent of Code 2015 Day 6
"""

import re


def solve_part(puzzle: list[str], part_num: int) -> int:
    """
    Each part essentially does the same thing, except uses different rules
    to update the grid, so this function uses the input part number to
    decide on the rules

    :param puzzle: the contents of the puzzle file
    :param part_num: which part to solve
    :returns: the solution to the part in question
    """

    if part_num not in {1, 2}:
        raise ValueError(
            f"The part number must be either 1 or 2, not {part_num}"
        )

    GRID_DIMENSIONS = (1000, 1000)
    # All lights start off, which is represented by a value of zero
    grid = {
        (i, j): 0
        for i in range(GRID_DIMENSIONS[0])
        for j in range(GRID_DIMENSIONS[1])
    }

    REGEX = (
        r"(?P<command>[a-z|\s]*) (?P<indices_start>[0-9]{1,3},[0-9]{1,3}) "
        r"through (?P<indices_end>[0-9]{1,3},[0-9]{1,3})"
    )
    for line in puzzle:
        rmatch = re.match(REGEX, line)
        if rmatch is None:
            raise ValueError(
                f"Found unexpected line format. The line is: {line}."
            )

        command = rmatch.group("command")
        indices_start = [
            int(value) for value in rmatch.group("indices_start").split(",")
        ]
        indices_end = [
            int(value) for value in rmatch.group("indices_end").split(",")
        ]

        # Indices are inclusive, so ranges run to end + 1
        match command:
            case "turn off":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        if part_num == 1:
                            grid[(i, j)] = 0
                        elif part_num == 2:
                            grid[(i, j)] = grid[(i, j)] - 1
                            if grid[(i, j)] < 0:
                                grid[(i, j)] = 0
            case "turn on":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        if part_num == 1:
                            grid[(i, j)] = 1
                        elif part_num == 2:
                            grid[(i, j)] = grid[(i, j)] + 1
            case "toggle":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        if part_num == 1:
                            grid[(i, j)] = grid[(i, j)] ^ 1  # XOR
                        elif part_num == 2:
                            grid[(i, j)] = grid[(i, j)] + 2
            case _:
                raise ValueError(
                    f"Found an unexpected command. The command should be one "
                    f"of 'turn off', 'turn on', or 'toggle', not '{command}'."
                )

    return sum(value for value in grid.values())


def solve(puzzle: list[str]) -> None:
    """
    Solve the 2015 Day 6 puzzle.
    The puzzle contains a series of instructions for setting the state
    of lights in a 1000 x 1000 grid.

    Part 1
    ------
    How many lights are on?

    Part 2
    ------
    What is the total brightness?

    :param puzzle: the contents of the puzzle file
    """


    total_on = solve_part(puzzle, 1)
    total_brightness = solve_part(puzzle, 2)

    print(f"Part 1: The total number of lights that are on is: {total_on}.")
    print(f"Part 2: The total brightness is: {total_brightness}.")
