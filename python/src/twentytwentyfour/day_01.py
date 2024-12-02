"""
Advent of Code 2024 Day 1

The input contains two columns of numbers.

Part 1
------
What is the total distance between the two columns?

Part 2
------
What is the total similarity between the two columns?
"""


def _part_1(lefts: list[int], rights: list[int]) -> int:
    """
    Sum the magnitude of the differences between the left and right columns
    when both are sorted in ascending order.

    :param lefts: The left column of the puzzle input
    :param rights: The right column of the puzzle input
    :returns: The total distance between the two columns
    """

    lefts = sorted(lefts)
    rights = sorted(rights)
    distance = 0
    for left, right in zip(lefts, rights):
        d = left - right
        if d < 0:
            d = d * -1
        distance += d

    return distance


def _part_2(lefts: list[int], rights: list[int]) -> int:
    """
    Calculate the similarity between the two lists, where
    similarity = sum(<left_value> * <count_of_left_value_in_right_column>)

    :param lefts: The left column of the puzzle input
    :param rights: The right column of the puzzle input
    :returns: The total similarity between the two columns
    """

    mapping = {}
    for left in lefts:
        if left in mapping:
            continue
        count = 0
        for right in rights:
            if left == right:
                count = count + 1
        mapping[left] = count

    similarity = 0
    for left in lefts:
        similarity = similarity + left * mapping[left]

    return similarity


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2024 Day 1 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    lefts = []
    rights = []
    for line in puzzle:
        columns = line.strip().split()
        lefts.append(int(columns[0]))
        rights.append(int(columns[1]))

    if part == 1 or part is None:
        distance = _part_1(lefts, rights)
        print(f"The total distance between the lists is {distance}")

    if part == 2 or part is None:
        similarity = _part_2(lefts, rights)
        print(f"The total similarity is {similarity}")
