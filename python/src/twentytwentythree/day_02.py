"""
Advent of Code 2023 Day 2

The input is a list of strings.
Each string represents one iteration of a game
in which colored cubes are drawn from a bag multiple times.
The string contains how many cubes of each color were drawn in each iteration.

Part 1
------
Given known distribution of cubes in the bag,
determine whether a game is possible.
What is the sum of the IDs of all possible games?

Part 2
------
Given the drawings seen in the game,
find the minimum number of cubes of each color
that could have made that game possible,
and then mutiply the numbers of each color of cube in that miniumum set
to generate a power value.
What is the sum of the all the power values of the minimum sets?
"""


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2023 Day 2 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    # Used in Part 1
    COLOR_DISTRIBUTION = {"red": 12, "green": 13, "blue": 14}
    sum_id = 0

    # Used in Part 2
    sum_power = 0

    for line in puzzle:
        components = line.split(":")

        # Part 1 Parameters
        game_id = int(components[0].split()[-1])
        possible = True

        # Part 2 Parameters
        most_seen = {"red": 0, "green": 0, "blue": 0}
        power = 1

        components = components[1].split(";")
        for component in components:
            cubes = component.split(",")
            for cube in cubes:
                split = cube.split()
                number = int(split[0])
                color = split[1]
                # Part 1 Logic
                if number > COLOR_DISTRIBUTION[color]:
                    possible = False
                # Part 2 Logic
                if number > most_seen[color]:
                    most_seen[color] = number
        # Part 1 Logic
        if possible:
            sum_id = sum_id + game_id
        # Part 2 Logic
        for number in most_seen.values():
            power = power * number
        sum_power = sum_power + power

    if part == 1 or part is None:
        print(f"The sum of the possible game IDs is {sum_id}.")
    if part == 2 or part is None:
        print(
            f"The sum of the power values of the minumum sets is {sum_power}."
        )
