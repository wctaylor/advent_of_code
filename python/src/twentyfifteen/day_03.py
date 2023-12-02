"""
Advent of Code 2015 Day 3

The input is a list of characters, where each character is one of
"<", ">", "v", or "^", and each corresponds to the direction Santa
(or Robo-Santa) moves in a 2D grid.

Part 1
------
How many houses receive at least one present?

Part 2
------
How many houses receive at least one present, when the instructions are
split among Santa and Robo-Santa?
"""


def _update_coordinates(char: str, coords: tuple[int, int]) -> int:
    """
    Update the provided coordinate based on the input character

    :param char: The instruction character
    :param coord: The coordinates to update
    :returns: The updated coordinate
    """

    VALID_CHARS = {"<", ">", "^", "v"}
    if char not in VALID_CHARS:
        raise ValueError(
            f"Received a character that is not a valid instruction."
            f"The character should be an element of {VALID_CHARS}, not {char}."
        )

    if len(coords) != 2:
        raise ValueError(
            f"Received unexpected coordinates.\n"
            f"The coordinates should be a tuple of (x, y), "
            f"but received {coords}"
        )

    if char == "<":
        return (coords[0] - 1, coords[1])
    if char == ">":
        return (coords[0] + 1, coords[1])
    if char == "v":
        return (coords[0], coords[1] - 1)
    if char == "^":
        return (coords[0], coords[1] + 1)


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2015 Day 3 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    if len(puzzle) > 1:
        raise ValueError(
            f"Unexpected puzzle length: expected a length of 1, "
            f"but found {len(puzzle)}."
        )
    chars = puzzle[0]

    # The starting house receives a gift in both cases
    houses_solo = 1
    houses_team = 1

    coord_solo_santa = (0, 0)
    coord_team_robo = (0, 0)
    coord_team_santa = (0, 0)
    coord_solo_visited = {coord_solo_santa}
    coord_team_visited = {coord_team_robo, coord_team_santa}
    for char_num, char in enumerate(chars):
        # Solo Santa always updates
        coord_solo_santa = _update_coordinates(char, coord_solo_santa)
        if coord_solo_santa not in coord_solo_visited:
            houses_solo = houses_solo + 1
            coord_solo_visited.add(coord_solo_santa)

        # Team Santa and Robo-Santa alternate updating
        if char_num % 2:
            coord_team_robo = _update_coordinates(char, coord_team_robo)
            if coord_team_robo not in coord_team_visited:
                houses_team = houses_team + 1
                coord_team_visited.add(coord_team_robo)
        else:
            coord_team_santa = _update_coordinates(char, coord_team_santa)
            if coord_team_santa not in coord_team_visited:
                houses_team = houses_team + 1
                coord_team_visited.add(coord_team_santa)

    if part == 1 or part is None:
        print(f"Part 1: Santa delivers gifts to a total of {houses_solo} houses.")
    if part == 1 or part is None:
        print(
            f"Part 2: Santa and Robo-Santa deliver gifts "
            f"to a total of {houses_team} houses."
        )
