"""
Advent of Code 2015 Day 6
"""

import re


def create_grid() -> dict[tuple[int, int], int]:
    """
    Create a grid that will be used by each part

    :returns: the initialized grid where each light has a value of zero
    """

    GRID_DIMENSIONS = (1000, 1000)
    # All lights start off, which is represented by a value of zero
    grid = {
        (i, j): 0
        for i in range(GRID_DIMENSIONS[0])
        for j in range(GRID_DIMENSIONS[1])
    }

    return grid


def parse_line(line: str) -> tuple[str, list[int], list[int]]:
    """
    Parse a line into the component information of the instruction

    :param line: One line of the puzzle input
    :returns: a tuple containing
        the command
        a list of the two starting indices
        a list of the two ending indices
    """

    REGEX = (
        r"(?P<command>[a-z|\s]*) (?P<indices_start>[0-9]{1,3},[0-9]{1,3}) "
        r"through (?P<indices_end>[0-9]{1,3},[0-9]{1,3})"
    )

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

    return command, indices_start, indices_end

def part_1(puzzle: list[str]) -> int:
    """
    Process the input according to the interpretation of part 1,
    where
        `turn off` sets the value to zero
        `turn on` sets the value to one
        `toggle` flips 0 and 1

    :param puzzle: the contents of the puzzle file
    :returns: the total number of lights that are on by the end
    """

    grid = create_grid()
    for line in puzzle:
        command, indices_start, indices_end = parse_line(line)

        # Indices are inclusive, so ranges run to end + 1
        match command:
            case "turn off":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        grid[(i, j)] = 0
            case "turn on":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        grid[(i, j)] = 1
            case "toggle":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        grid[(i, j)] = grid[(i, j)] ^ 1  # XOR
            case _:
                raise ValueError(
                    f"Found an unexpected command. The command should be one "
                    f"of 'turn off', 'turn on', or 'toggle', not '{command}'."
                )

    return sum(value for value in grid.values())


def part_2(puzzle: list[str]) -> int:
    """
    Process the input according to the interpretation of part 2,
    where
        `turn off` decreases brightness by one, to a minimum of zero
        `turn on` increases brightness by one
        `toggle` increase brightness by two

    :param puzzle: the contents of the puzzle file
    :returns: the total brightness of the lights in the grid
    """

    grid = create_grid()
    for line in puzzle:
        command, indices_start, indices_end = parse_line(line)

        # Indices are inclusive, so ranges run to end + 1
        match command:
            case "turn off":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        grid[(i, j)] = grid[(i, j)] - 1
                        if grid[(i, j)] < 0:
                            grid[(i, j)] = 0
            case "turn on":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
                        grid[(i, j)] = grid[(i, j)] + 1
            case "toggle":
                for i in range(indices_start[0], indices_end[0] + 1):
                    for j in range(indices_start[1], indices_end[1] + 1):
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

    total_on = part_1(puzzle)
    total_brightness = part_2(puzzle)

    print(f"Part 1: The total number of lights that are on is: {total_on}.")
    print(f"Part 2: The total brightness is: {total_brightness}.")
