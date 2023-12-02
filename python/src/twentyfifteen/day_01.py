"""
Advent of Code 2015 Day 1

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


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2015 Day 1 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    if len(puzzle) > 1:
        raise ValueError(
            f"Unexpected puzzle length: expected a length of 1, "
            f"but found {len(puzzle)}."
        )

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

    if part == 1 or part is None:
        print(f"Part 1: Santa ends up on floor {floor}")
    if part == 2 or part is None:
        print(
            f"Part 2: Santa first ends up in the basement at position "
            f"{first_basement_entry}"
        )
