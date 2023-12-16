"""
Advent of Code 2023 Day 6

The input contains time and distance values for a number of toy boat races.
The toy boats can be charged in 1 second increments to increase their speed by
1 unit.

Given the provided time, how can you beat the distance?

Part 1
------
Determine the number of ways you could beat the record in each race.
What do you get if you multiply these numbers together?

Part 2
------
There is actually only one race.
What is the number of ways to beat this race?
"""


def _calculate_ways_to_win(time: int, distance: int) -> int:
    """
    Calculate the number of ways to win a race

    :param time: The time in which the race must be completed
    :param distance: The distance which must be travelled to win
    """

    ways_to_win = 0
    for t in range(time):
        if t * (time - t) > distance:
            ways_to_win = ways_to_win + 1

    return ways_to_win


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2023 Day 6 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    info_1 = dict()
    info_2 = dict()
    for line in puzzle:
        components = line.split(":")
        key = components[0]
        values = components[1].split()
        info_1[key] = [int(value) for value in values]
        info_2[key] = int("".join(values))

    if part == 1 or part is None:
        # Make sure all values have the same length so that we don't have a race
        # that lost some information
        if len(set(len(values) for values in info_1.values())) != 1:
            raise ValueError("Found mismatched race values")

        num_ways_to_win = list()
        for time, distance in zip(info_1["Time"], info_1["Distance"]):
            num_ways_to_win.append(_calculate_ways_to_win(time, distance))

        product = 1
        for ways_to_win in num_ways_to_win:
            product = product * ways_to_win
        print(
            f"The product of the number of ways to win each race is {product}"
        )

    if part == 2 or part is None:
        time = info_2["Time"]
        distance = info_2["Distance"]
        print(
            f"The number of ways to win the bigger race is "
            f"{_calculate_ways_to_win(time, distance)}"
        )
