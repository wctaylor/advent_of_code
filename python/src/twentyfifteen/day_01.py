"""
Advent of Code 2015 Day 1
"""


def solve(puzzle: list[str]) -> None:
    """
    Solve the 2015 Day 1 puzzle.
    The input is a list of "(" and ")" characters.
    Santa starts on floor 0.
    A "(" character tells Santa to go up,
    while a ")" character tells him to go down.

    Part 1
    ------
    On what floor does he finish?

    Part 2
    ------
    At what position in the list of characters does Santa first enter
    the basement?
    """

    chars = puzzle[0]

    floor = 0
    first_basement_entry = None
    for char_num, char in enumerate(chars):
        if char == "(":
            floor = floor + 1
        elif char == ")":
            floor = floor - 1
        else:
            raise ValueError(f"Received an unexpected input character: {char}")

        if floor == -1 and first_basement_entry is None:
            first_basement_entry = char_num + 1  # Position is 1-indexed

    print(f"Part 1: Santa ends up on floor {floor}")
    print(
        f"Part 2: Santa first ends up in the basement at position "
        f"{first_basement_entry}"
    )
